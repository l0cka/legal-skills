from __future__ import annotations

import datetime as dt
import importlib.util
import io
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import formulas
from layout import PLUGIN
from test_australian_litigation_deadlines import (
    EFFECTS_FIXTURES,
    EFFECTS_REFUSALS,
    ENGINE,
    FIXTURES,
    REFUSALS,
    build_rules_table,
    rule_id,
    write_engine_tables,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("ai_tool_workbooks", ROOT / "scripts" / "ai_tool_workbooks.py")
assert SPEC and SPEC.loader
workbooks = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = workbooks
SPEC.loader.exec_module(workbooks)

EPOCH = dt.date(1899, 12, 30)
GATES = {
    "event": "Service of the originating process",
    "contested": "No",
    "matter": workbooks.CIVIL,
    "profile": "Test profile v1",
    "approved": "Yes",
    "confirmer": "Responsible lawyer",
    "diary": "Firm diary",
}
SHIPPED_TRIGGERS = ("2026-12-10", "2027-12-20")
OUTPUTS = ("out_status", "out_candidate", "out_reason", "out_provisions", "out_warnings", "out_caveats")


def serial(value: str) -> int:
    return (dt.date.fromisoformat(value) - EPOCH).days


def plain(value: object) -> object:
    while hasattr(value, "value"):
        value = value.value
    if hasattr(value, "shape"):
        value = value.flat[0]
    if hasattr(value, "item"):
        value = value.item()
    return value


class Calculator:
    def __init__(self, tables_dir: Path, workdir: Path) -> None:
        wb, self.cells = workbooks.build_deadline_workbook(*workbooks.load_tables(tables_dir))
        self.path = workdir / "calc.xlsx"
        self.path.write_bytes(workbooks.workbook_bytes(wb))
        self.model = formulas.ExcelModel().loads(str(self.path)).finish()

    def key(self, ref: str) -> str:
        sheet, cell = ref.split("!")
        return f"'[{self.path.name}]{sheet.upper()}'!{cell.replace('$', '')}"

    def run(self, rule: str, trigger: str, registry: str = "", overrides: dict | None = None, cells: dict | None = None) -> dict:
        values = {**GATES, "rule": rule, "trigger": serial(trigger), "registry": registry, **(overrides or {})}
        inputs = {self.key(self.cells[f"in_{name}"]): value for name, value in values.items()}
        inputs.update({self.key(ref): value for ref, value in (cells or {}).items()})
        outputs = [self.key(self.cells[name]) for name in OUTPUTS]
        solution = self.model.calculate(inputs=inputs, outputs=outputs)
        result = {name: plain(solution[key]) for name, key in zip(OUTPUTS, outputs)}
        candidate = result["out_candidate"]
        if isinstance(candidate, (int, float)):
            result["out_candidate"] = (EPOCH + dt.timedelta(days=int(candidate))).isoformat()
        return result


class WorkbookAgreementMixin:
    def assert_agrees(self, engine: dict, sheet: dict, context: str) -> None:
        if engine["status"] == "computed":
            self.assertEqual(sheet["out_status"], workbooks.STATUS_CANDIDATE, f"{context}: {sheet}")
            self.assertEqual(sheet["out_candidate"], engine["candidate_date"], context)
        else:
            self.assertEqual(sheet["out_status"], workbooks.STATUS_IDENTIFY, f"{context}: {engine} {sheet}")
            self.assertEqual(sheet["out_candidate"], "not computed", context)
            self.assertEqual(sheet["out_reason"], engine["reason"], context)
            shown = [part for part in sheet["out_warnings"].split(" | ") if part]
            caveats = [part for part in sheet["out_caveats"].split(" | ") if part]
            self.assertEqual(engine["warnings"][: len(shown)], shown, context)
            self.assertLessEqual(set(engine["warnings"][len(shown):]), set(caveats), context)


class EngineCaseTests(WorkbookAgreementMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.tables_dir = Path(cls._tmp.name) / "tables"
        cls.tables_dir.mkdir()
        write_engine_tables(cls.tables_dir)
        pending = build_rules_table("nsw", {("calendar_days", 3, "none")})
        pending["table_id"] = "test-pending"
        pending["period_rules"][0]["evidence"] = {"state": "pending-verification"}
        provision = build_rules_table("nsw", {("calendar_days", 3, "none")})
        provision["table_id"] = "test-provision"
        provision["computation_provisions"][0]["evidence"] = {"state": "pending-verification"}
        provision["period_rules"][0]["warnings"] = ["Test rule warning kept on refusal."]
        unverified = json.loads((cls.tables_dir / "holidays" / "nsw.json").read_text(encoding="utf-8"))
        unverified["table_id"] = "unv"
        unverified["evidence"] = {"state": "pending-verification"}
        (cls.tables_dir / "holidays" / "unv.json").write_text(json.dumps(unverified), encoding="utf-8")
        unv = build_rules_table("unv", {("calendar_days", 1, "next_business_day")})
        edge = build_rules_table("vic", {("calendar_days", 1, "next_business_day")})
        edge["table_id"] = "test-edge"
        template = edge["period_rules"][0]
        edge["period_rules"] = [
            {**template, "id": "bad-rollover", "rollover": "previous_business_day"},
            {**template, "id": "zero-length", "period": {"length": 0, "unit": "calendar_days"}},
            {**template, "id": "fraction-length", "period": {"length": 1.5, "unit": "calendar_days"}},
            {**template, "id": "missing-provision", "applies_provisions": ["no-such-provision"], "warnings": ["Test warning one.", "Test warning two."]},
            {**template, "id": "no-evidence", "evidence": {}},
            {**template, "id": "window-roll"},
            {**template, "id": "long-business", "period": {"length": 200, "unit": "business_days"}, "rollover": "none"},
        ]
        long_holidays = json.loads((cls.tables_dir / "holidays" / "nsw.json").read_text(encoding="utf-8"))
        long_holidays["table_id"] = "longhol"
        long_holidays["holidays"] = sorted({*long_holidays["holidays"], *(f"2026-08-{day:02d}" for day in range(1, 32))})
        (cls.tables_dir / "holidays" / "longhol.json").write_text(json.dumps(long_holidays), encoding="utf-8")
        longhol = build_rules_table("longhol", {("calendar_days", 1, "next_business_day")})
        boundary = []
        for key, coverage_to, windows in (
            ("edgecov", "2026-08-17", []),
            ("edgewin", "2026-12-31", [{"from": "2026-08-18", "to": "2026-08-18", "reason": "Test window on a weekday."}]),
        ):
            holidays = json.loads((cls.tables_dir / "holidays" / "nsw.json").read_text(encoding="utf-8"))
            holidays.update(table_id=key, coverage={"from": "2026-01-01", "to": coverage_to}, uncertain_windows=windows)
            holidays["holidays"] = [day for day in holidays["holidays"] if day <= coverage_to]
            (cls.tables_dir / "holidays" / f"{key}.json").write_text(json.dumps(holidays), encoding="utf-8")
            boundary.append(build_rules_table(key, {("business_days", 1, "none"), ("business_days", 2, "none")}))
        for table in (pending, provision, unv, edge, longhol, *boundary):
            path = cls.tables_dir / "computation-rules" / f"{table['table_id']}.json"
            path.write_text(json.dumps(table), encoding="utf-8")
        cls.calc = Calculator(cls.tables_dir, Path(cls._tmp.name))

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def compare(self, table_id: str, unit: str, length: int, rollover: str, trigger: str) -> tuple[dict, dict]:
        rule = rule_id(unit, length, rollover)
        engine = ENGINE.compute({"table_id": table_id, "period_rule_id": rule, "trigger_date": trigger}, self.tables_dir)
        sheet = self.calc.run(f"{table_id} / {rule}", trigger)
        self.assert_agrees(engine, sheet, f"{table_id} {rule} {trigger}")
        return engine, sheet

    def test_hand_derived_fixtures_agree(self) -> None:
        for table_key, unit, length, rollover, trigger, expected in FIXTURES + EFFECTS_FIXTURES:
            with self.subTest(f"{table_key} {unit} {length} {rollover} {trigger}"):
                engine, sheet = self.compare(f"test-{table_key}", unit, length, rollover, trigger)
                self.assertEqual(sheet["out_candidate"], expected)

    def test_refusals_agree_and_give_the_same_reason(self) -> None:
        for table_key, unit, length, rollover, trigger, reason in REFUSALS + EFFECTS_REFUSALS:
            with self.subTest(f"{table_key} {unit} {length} {trigger}"):
                engine, sheet = self.compare(f"test-{table_key}", unit, length, rollover, trigger)
                self.assertIn(reason, engine["reason"])
                self.assertIn(reason, sheet["out_reason"])

    def test_unverified_rule_provision_and_holiday_table_refuse(self) -> None:
        for table_id, unit, length, rollover, reason in (
            ("test-pending", "calendar_days", 3, "none", "verify-deadline-basis"),
            ("test-provision", "calendar_days", 3, "none", "test-provision"),
            ("test-unv", "calendar_days", 1, "next_business_day", "holiday table unv"),
        ):
            with self.subTest(table_id):
                engine, sheet = self.compare(table_id, unit, length, rollover, "2026-08-14")
                self.assertIn(reason, engine["reason"])
                self.assertIn(reason, sheet["out_reason"])

    def test_edge_refusals_match_the_engine_reason(self) -> None:
        for rule, trigger in (
            ("bad-rollover", "2026-08-14"),
            ("zero-length", "2026-08-14"),
            ("fraction-length", "2026-08-14"),
            ("missing-provision", "2026-08-14"),
            ("no-evidence", "2026-08-14"),
            ("window-roll", "2027-08-31"),
        ):
            with self.subTest(rule):
                engine = ENGINE.compute({"table_id": "test-edge", "period_rule_id": rule, "trigger_date": trigger}, self.tables_dir)
                self.assert_agrees(engine, self.calc.run(f"test-edge / {rule}", trigger), rule)
                self.assertEqual(engine["status"], "identify_only", engine)

    def test_count_ending_on_the_first_unusable_weekday_refuses(self) -> None:
        for table_key, length, reason in (
            ("edgecov", 1, "does not cover 2026-08-18"),
            ("edgecov", 2, "does not cover 2026-08-18"),
            ("edgewin", 1, "uncertain holiday window"),
            ("edgewin", 2, "uncertain holiday window"),
        ):
            with self.subTest(f"{table_key} {length}"):
                engine, sheet = self.compare(f"test-{table_key}", "business_days", length, "none", "2026-08-17")
                self.assertEqual(engine["status"], "identify_only", engine)
                self.assertIn(reason, sheet["out_reason"])

    def test_scan_limits_refuse_where_the_engine_computes(self) -> None:
        for rule, trigger, reason in (
            ("test-edge / long-business", "2026-08-14", "120-day scan"),
            ("test-longhol / calendar_days-1-next_business_day", "2026-07-31", "no business day within 15 days"),
        ):
            with self.subTest(rule):
                table_id, rule_name = rule.split(" / ")
                engine = ENGINE.compute({"table_id": table_id, "period_rule_id": rule_name, "trigger_date": trigger}, self.tables_dir)
                self.assertEqual(engine["status"], "computed", engine)
                sheet = self.calc.run(rule, trigger)
                self.assertEqual(sheet["out_status"], workbooks.STATUS_IDENTIFY, sheet)
                self.assertEqual(sheet["out_candidate"], "not computed")
                self.assertIn(reason, sheet["out_reason"])

    def test_every_nsw_2026_holiday_rolls_like_the_engine(self) -> None:
        table = json.loads((self.tables_dir / "holidays" / "nsw.json").read_text(encoding="utf-8"))
        for holiday in sorted(day for day in table["holidays"] if day.startswith("2026")):
            trigger = (dt.date.fromisoformat(holiday) - dt.timedelta(days=1)).isoformat()
            with self.subTest(holiday):
                self.compare("test-nsw", "calendar_days", 1, "next_business_day", trigger)


class ShippedWorkbookTests(WorkbookAgreementMixin, unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.references = PLUGIN / "references"
        cls.calc = Calculator(cls.references, Path(cls._tmp.name))
        cls.rule_tables, cls.holiday_tables = workbooks.load_tables(cls.references)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def compare(self, table_id: str, rule: str, trigger: str, registry: str = "") -> dict:
        request = {"table_id": table_id, "period_rule_id": rule, "trigger_date": trigger}
        if registry:
            request["holiday_table"] = registry
        engine = ENGINE.compute(request, self.references)
        sheet = self.calc.run(f"{table_id} / {rule}", trigger, registry)
        context = f"{table_id} {rule} {trigger} {registry}"
        self.assert_agrees(engine, sheet, context)
        if engine["status"] == "computed":
            self.assertEqual(sheet["out_provisions"], "; ".join(engine["provisions_applied"]), context)
            shown = [part for cell in ("out_warnings", "out_caveats") for part in sheet[cell].split(" | ") if part]
            self.assertEqual(shown, engine["warnings"], context)
        return sheet

    def test_every_shipped_rule_agrees_with_the_engine(self) -> None:
        for table in self.rule_tables:
            registries = ("", "nsw", "act") if table.get("holiday_table_placeholder") else ("",)
            for rule in table["period_rules"]:
                for trigger in SHIPPED_TRIGGERS:
                    for registry in registries:
                        with self.subTest(f"{table['table_id']} {rule['id']} {trigger} {registry}"):
                            self.compare(table["table_id"], rule["id"], trigger, registry)

    def test_documented_shipped_dates(self) -> None:
        for table_id, rule, trigger, registry, expected in (
            ("nsw-courts", "ucpr-defence-after-service", "2026-08-14", "", "2026-09-11"),
            ("cth-federal-courts", "fcr-defence-after-service", "2026-12-10", "nsw", "2027-01-29"),
            ("cth-federal-courts", "fcr-defence-after-service", "2026-09-07", "nsw", "2026-10-06"),
            ("cth-federal-courts", "fcr-defence-after-service", "2026-09-07", "vic", "2026-10-05"),
            ("qld-courts", "qld-ucpr-noid-after-service", "2026-07-15", "", "2026-08-13"),
            ("qld-courts", "qld-ucpr-noid-after-service", "2026-11-26", "", "2026-12-24"),
            ("qcat", "qcat-review-application", "2026-08-14", "", "2026-09-11"),
        ):
            with self.subTest(f"{table_id} {trigger} {registry}"):
                self.assertEqual(self.compare(table_id, rule, trigger, registry)["out_candidate"], expected)

    def test_placeholder_forum_without_registry_refuses(self) -> None:
        sheet = self.compare("art", "art-general-review-application", "2026-03-19")
        self.assertIn("holiday_table of the registry", sheet["out_reason"])

    def test_gates_hide_the_date(self) -> None:
        rule = "nsw-courts / ucpr-defence-after-service"
        self.assertEqual(self.calc.run(rule, "2026-08-14")["out_candidate"], "2026-09-11")
        for overrides, status in (
            ({"approved": "No"}, "NOT READY"),
            ({"approved": ""}, "NOT READY"),
            ({"profile": ""}, "NOT READY"),
            ({"confirmer": ""}, "NOT READY"),
            ({"confirmer": " "}, "NOT READY"),
            ({"event": "  "}, "NOT READY"),
            ({"diary": ""}, "NOT READY"),
            ({"event": ""}, "NOT READY"),
            ({"contested": "Yes"}, "NOT READY"),
            ({"contested": ""}, "NOT READY"),
            ({"matter": ""}, "NOT READY"),
            ({"trigger": ""}, "NOT READY"),
            ({"rule": ""}, "NOT READY"),
            ({"matter": "Criminal procedure"}, "OUTSIDE SCOPE"),
            ({"matter": "Court-fixed or discretionary date"}, "OUTSIDE SCOPE"),
        ):
            with self.subTest(overrides):
                result = self.calc.run(rule, "2026-08-14", overrides=overrides)
                self.assertEqual(result["out_status"], status, result)
                self.assertEqual(result["out_candidate"], "not computed")

    def custom_cells(self, state: str, dates: list[object], verifier: str = "Registry clerk") -> dict:
        custom_row = len(self.holiday_tables) + 2
        cells = {
            f"HolidayTables!B{custom_row}": state,
            f"HolidayTables!C{custom_row}": serial("2026-01-01"),
            f"HolidayTables!D{custom_row}": serial("2027-12-31"),
            f"HolidayTables!E{custom_row}": "https://example.invalid/holidays",
            f"HolidayTables!H{custom_row}": verifier,
        }
        column = workbooks.get_column_letter(len(self.holiday_tables) + 1)
        for index, value in enumerate(dates):
            cells[f"Holidays!{column}{index + 2}"] = value
        return cells

    def test_custom_holiday_table_fails_closed_until_verified(self) -> None:
        vic = next(t for t in self.holiday_tables if t["table_id"] == "vic")
        dates = [serial(day) for day in vic["holidays"]]
        rule = "cth-federal-courts / fcr-defence-after-service"
        expected = ENGINE.compute(
            {"table_id": "cth-federal-courts", "period_rule_id": "fcr-defence-after-service", "trigger_date": "2026-09-07", "holiday_table": "vic"},
            self.references,
        )["candidate_date"]
        unverified = self.calc.run(rule, "2026-09-07", "custom", cells=self.custom_cells("not verified", dates))
        self.assertEqual(unverified["out_status"], workbooks.STATUS_IDENTIFY)
        self.assertIn("not 'verified'", unverified["out_reason"])
        verified = self.calc.run(rule, "2026-09-07", "custom", cells=self.custom_cells("verified", dates))
        self.assertEqual(verified["out_candidate"], expected)
        unnamed = self.calc.run(rule, "2026-09-07", "custom", cells=self.custom_cells("verified", dates, verifier=""))
        self.assertEqual(unnamed["out_status"], workbooks.STATUS_IDENTIFY)
        self.assertIn("the person who verified it", unnamed["out_reason"])
        lower = self.calc.run(rule, "2026-09-07", "custom", cells=self.custom_cells("Verified", dates))
        self.assertEqual(lower["out_status"], workbooks.STATUS_IDENTIFY)
        typo = self.calc.run(rule, "2026-09-07", "custom", cells=self.custom_cells("verified", [*dates, "2026-13-01"]))
        self.assertEqual(typo["out_status"], workbooks.STATUS_IDENTIFY)
        self.assertIn("not a date", typo["out_reason"])


class WorkbookFileTests(unittest.TestCase):
    def test_generation_is_deterministic_with_fixed_metadata(self) -> None:
        first = workbooks.deadline_calculator(PLUGIN / "references")
        second = workbooks.deadline_calculator(PLUGIN / "references")
        self.assertEqual(first, second)
        with zipfile.ZipFile(io.BytesIO(first)) as archive:
            self.assertTrue(all(info.date_time == workbooks.FIXED_TIME for info in archive.infolist()))
            core = archive.read("docProps/core.xml").decode()
        self.assertEqual(core.count(workbooks.FIXED_STAMP), 2)

    def test_scope_and_safeguards_are_written_in_the_workbook(self) -> None:
        wb, _ = workbooks.build_deadline_workbook(*workbooks.load_tables(PLUGIN / "references"))
        scope = " ".join(str(c.value) for row in wb["Scope"].iter_rows() for c in row)
        for phrase in ("Criminal procedure", "VCAT", "Migration", "OUTSIDE SCOPE"):
            self.assertIn(phrase, scope)
        about = " ".join(str(c.value) for row in wb["About"].iter_rows() for c in row)
        self.assertIn("never the binding deadline", about)
        self.assertIn("never the binding deadline", wb["Calculator"]["A2"].value)
        for name in ("Engine", "Working"):
            self.assertEqual(wb[name]["M1"].value, workbooks.WORKING_NOTE)
        for ws in wb.worksheets:
            self.assertTrue(ws.protection.sheet, ws.title)
        unlocked = {
            f"{ws.title}!{cell.coordinate}"
            for ws in wb.worksheets
            for row in ws.iter_rows()
            for cell in row
            if not cell.protection.locked
        }
        shipped = len(workbooks.load_tables(PLUGIN / "references")[1])
        custom, last_shipped = (workbooks.get_column_letter(index) for index in (shipped + 1, shipped))
        for ref in ("Calculator!B4", "Calculator!B13", f"Holidays!{custom}2", f"Holidays!{custom}101"):
            self.assertIn(ref, unlocked)
        for ref in ("Calculator!B16", "Holidays!A2", f"Holidays!{last_shipped}2", "HolidayTables!B2", "Windows!A2", "Rules!A2"):
            self.assertNotIn(ref, unlocked)


if __name__ == "__main__":
    unittest.main()
