from __future__ import annotations

import datetime as dt
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-litigation-deadlines"
SCRIPT = (
    PLUGIN / "skills" / "compute-procedural-deadlines" / "scripts"
    / "compute_deadline.py"
)
SPEC = importlib.util.spec_from_file_location("compute_deadline", SCRIPT)
assert SPEC and SPEC.loader
ENGINE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ENGINE
SPEC.loader.exec_module(ENGINE)

VERIFIED = {"state": "verified"}


class AustralianLitigationDeadlinesPluginTests(unittest.TestCase):
    EXPECTED_SKILLS = {
        "configure-litigation-deadline-profile",
        "map-limitation-periods",
        "compute-procedural-deadlines",
        "map-tribunal-review-deadlines",
        "maintain-deadline-register",
        "verify-deadline-basis",
    }

    REQUIRED_HEADINGS = ("## Workflow", "## Result contract", "## Fail closed")
    REQUIRED_STATUSES = (
        "`READY FOR HUMAN REVIEW`",
        "`READY WITH QUALIFICATIONS`",
        "`NOT READY`",
        "`OUTSIDE SCOPE`",
    )

    def skill_text(self, name: str) -> str:
        return (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")

    def test_plugin_contains_expected_skills(self) -> None:
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, self.EXPECTED_SKILLS)

    def test_every_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for name in self.EXPECTED_SKILLS:
            text = self.skill_text(name)
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, name)
            for status in self.REQUIRED_STATUSES:
                self.assertIn(status, text, name)

    def test_every_skill_uses_shared_method_and_states_provisional(self) -> None:
        self.assertTrue(
            (
                PLUGIN / "references"
                / "litigation-deadlines-source-and-control-method.md"
            ).is_file()
        )
        self.assertTrue((PLUGIN / "references" / "deadline-profile-schema.md").is_file())
        for name in self.EXPECTED_SKILLS:
            text = self.skill_text(name)
            self.assertIn("litigation-deadlines-source-and-control-method.md", text, name)
            self.assertIn("provisional", text.lower(), name)

    def test_script_only_arithmetic_is_stated(self) -> None:
        for name in ("compute-procedural-deadlines", "map-tribunal-review-deadlines"):
            lowered = self.skill_text(name).lower()
            self.assertIn("never", lowered, name)
            self.assertIn("arithmetic", lowered, name)
            self.assertIn("compute_deadline.py", self.skill_text(name), name)

    def test_migration_matters_always_carry_warning(self) -> None:
        lowered = self.skill_text("map-tribunal-review-deadlines").lower()
        self.assertIn("migration", lowered)
        self.assertIn("jurisdictional", lowered)
        self.assertIn("specialist review", lowered)

    def test_limitation_mapping_fails_closed_and_routes_verification(self) -> None:
        text = self.skill_text("map-limitation-periods")
        self.assertIn("cannot be determined", text)
        self.assertIn("conservative marker", text)
        self.assertIn("$check-commonwealth-legislation", text)
        self.assertIn("$check-nsw-legislation", text)

    def test_register_is_not_the_diary(self) -> None:
        lowered = self.skill_text("maintain-deadline-register").lower()
        self.assertIn("not the practice's diary", lowered)
        self.assertIn("provenance", lowered)


class ShippedTableTests(unittest.TestCase):
    def test_holiday_tables_are_verified_with_coverage(self) -> None:
        holiday_dir = PLUGIN / "references" / "holidays"
        tables = sorted(holiday_dir.glob("*.json"))
        self.assertGreaterEqual(len(tables), 2)
        for path in tables:
            table = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(table["evidence"]["state"], "verified", path.name)
            self.assertTrue(table["source_url"].startswith("https://"), path.name)
            cover_from = dt.date.fromisoformat(table["coverage"]["from"])
            cover_to = dt.date.fromisoformat(table["coverage"]["to"])
            for day in table["holidays"]:
                self.assertTrue(
                    cover_from <= dt.date.fromisoformat(day) <= cover_to, path.name
                )

    def test_rule_table_entries_are_verified_or_pending_with_notes(self) -> None:
        rules_dir = PLUGIN / "references" / "computation-rules"
        tables = sorted(rules_dir.glob("*.json"))
        self.assertTrue(tables, "no shipped computation-rule tables found")
        verified = pending = 0
        for path in tables:
            table = json.loads(path.read_text(encoding="utf-8"))
            entries = table["computation_provisions"] + table["period_rules"]
            for entry in entries:
                label = f"{path.name}:{entry['id']}"
                self.assertTrue(entry.get("citation") or entry.get("summary"), label)
                evidence = entry["evidence"]
                self.assertIn(
                    evidence["state"], ("verified", "pending-verification"), label
                )
                if evidence["state"] == "verified":
                    verified += 1
                    for field in ("checked", "method", "version"):
                        self.assertTrue(evidence.get(field), f"{label}:{field}")
                    self.assertTrue(entry["source_url"].startswith("https://"), label)
                else:
                    pending += 1
                    self.assertTrue(evidence.get("note"), label)
        self.assertGreater(verified, 0)
        self.assertGreater(pending, 0)

    def test_vcat_ships_no_general_period_rule(self) -> None:
        table = json.loads(
            (PLUGIN / "references" / "computation-rules" / "vcat.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(table["period_rules"], [])
        self.assertIn("NO general default review period", table["note"])

    def test_shipped_verified_rule_computes(self) -> None:
        result = ENGINE.compute(
            {
                "table_id": "nsw-courts",
                "period_rule_id": "ucpr-defence-after-service",
                "trigger_date": "2026-08-14",
            },
            PLUGIN / "references",
        )
        self.assertEqual(result["status"], "computed", result)
        self.assertEqual(result["candidate_date"], "2026-09-11")
        self.assertIn("r 14.3(1)", result["citation"])
        self.assertTrue(
            any("registry" in warning for warning in result["warnings"]), result
        )

    def test_shipped_fcr_rule_applies_december_exclusion(self) -> None:
        result = ENGINE.compute(
            {
                "table_id": "cth-federal-courts",
                "period_rule_id": "fcr-defence-after-service",
                "trigger_date": "2026-12-10",
            },
            PLUGIN / "references",
        )
        self.assertEqual(result["status"], "computed", result)
        self.assertEqual(result["candidate_date"], "2027-01-29")
        self.assertIn("r 16.32", result["citation"])

    def test_shipped_qld_rule_rolls_over_brisbane_show_day(self) -> None:
        result = ENGINE.compute(
            {
                "table_id": "qld-courts",
                "period_rule_id": "qld-ucpr-noid-after-service",
                "trigger_date": "2026-07-15",
            },
            PLUGIN / "references",
        )
        self.assertEqual(result["status"], "computed", result)
        # 28 days lands on Wednesday 2026-08-12, the Royal Queensland Show
        # holiday in Brisbane, and rolls to Thursday.
        self.assertEqual(result["candidate_date"], "2026-08-13")
        self.assertIn("r 137(1)", result["citation"])
        self.assertTrue(
            any("registry" in warning for warning in result["warnings"]), result
        )

    def test_shipped_qld_christmas_eve_is_a_business_day(self) -> None:
        result = ENGINE.compute(
            {
                "table_id": "qld-courts",
                "period_rule_id": "qld-ucpr-noid-after-service",
                "trigger_date": "2026-11-26",
            },
            PLUGIN / "references",
        )
        self.assertEqual(result["status"], "computed", result)
        # Christmas Eve is a part-day holiday (6pm to midnight) and is not
        # a non-business day in the Queensland table.
        self.assertEqual(result["candidate_date"], "2026-12-24")

    def test_shipped_qcat_rule_computes_with_enabling_act_warning(self) -> None:
        result = ENGINE.compute(
            {
                "table_id": "qcat",
                "period_rule_id": "qcat-review-application",
                "trigger_date": "2026-08-14",
            },
            PLUGIN / "references",
        )
        self.assertEqual(result["status"], "computed", result)
        self.assertEqual(result["candidate_date"], "2026-09-11")
        self.assertIn("s 33(3)", result["citation"])
        self.assertTrue(
            any("enabling Act" in warning for warning in result["warnings"]), result
        )

    def test_shipped_pending_rule_refuses_to_compute(self) -> None:
        result = ENGINE.compute(
            {
                "table_id": "vic-courts",
                "period_rule_id": "vic-scr-appearance-after-service",
                "trigger_date": "2026-08-14",
            },
            PLUGIN / "references",
        )
        self.assertEqual(result["status"], "identify_only")
        self.assertIn("verify-deadline-basis", result["reason"])
        self.assertIn("r 8.04", result["citation"])


# (table_key, unit, length, rollover, trigger, expected)
FIXTURES = [
    ("nsw", "calendar_days", 28, "next_business_day", "2026-08-14", "2026-09-11"),
    ("nsw", "calendar_days", 28, "next_business_day", "2026-08-15", "2026-09-14"),
    ("nsw", "calendar_days", 14, "next_business_day", "2026-12-11", "2026-12-29"),
    ("nsw", "calendar_days", 7, "next_business_day", "2026-04-18", "2026-04-28"),
    ("nsw", "calendar_days", 1, "next_business_day", "2026-01-23", "2026-01-27"),
    ("nsw", "calendar_days", 28, "none", "2026-08-15", "2026-09-12"),
    ("nsw", "calendar_days", 10, "next_business_day", "2027-03-16", "2027-03-30"),
    ("nsw", "clear_days", 5, "none", "2026-08-14", "2026-08-20"),
    ("nsw", "clear_days", 2, "next_business_day", "2026-04-01", "2026-04-07"),
    ("nsw", "business_days", 10, "none", "2026-08-14", "2026-08-28"),
    ("nsw", "business_days", 3, "none", "2026-04-01", "2026-04-08"),
    ("nsw", "business_days", 5, "none", "2026-12-23", "2027-01-04"),
    ("nsw", "business_days", 3, "none", "2027-12-23", "2027-12-30"),
    ("nsw", "months", 1, "none", "2026-01-31", "2026-02-28"),
    ("nsw", "months", 1, "none", "2026-01-30", "2026-02-28"),
    ("nsw", "months", 3, "none", "2026-11-30", "2027-02-28"),
    ("nsw", "months", 1, "none", "2028-01-31", "2028-02-29"),
    ("nsw", "months", 4, "next_business_day", "2026-02-08", "2026-06-09"),
    ("nsw", "years", 1, "none", "2028-02-29", "2029-02-28"),
    ("nsw", "years", 6, "none", "2026-08-14", "2032-08-14"),
    ("vic", "business_days", 3, "none", "2026-04-02", "2026-04-09"),
    ("vic", "business_days", 1, "none", "2026-11-02", "2026-11-04"),
    ("vic", "calendar_days", 7, "next_business_day", "2026-09-18", "2026-09-28"),
    ("vic", "calendar_days", 7, "next_business_day", "2026-03-02", "2026-03-10"),
]

REFUSALS = [
    ("nsw", "business_days", 10, "none", "2027-12-27", "does not cover"),
    ("nsw", "calendar_days", 5, "next_business_day", "2027-12-27", "does not cover"),
    ("vic", "business_days", 5, "none", "2027-09-20", "uncertain holiday window"),
    ("nsw", "backwards_days", 5, "none", "2026-08-14", "unsupported period unit"),
]

FCR_EFFECTS = {
    "excluded_ranges": [{"from": "12-24", "to": "01-14"}],
    "short_period_threshold_days": 5,
}

# FCR-style reckoning: days 24 Dec to 14 Jan not counted (uses NSW holidays)
EFFECTS_FIXTURES = [
    ("fcrx", "calendar_days", 28, "next_business_day", "2026-12-10", "2027-01-29"),
    ("fcrx", "calendar_days", 6, "next_business_day", "2026-12-28", "2027-01-20"),
    ("fcrx", "calendar_days", 23, "next_business_day", "2026-12-02", "2027-01-18"),
    ("fcrx", "calendar_days", 28, "next_business_day", "2026-08-14", "2026-09-11"),
    ("fcrx", "business_days", 10, "none", "2026-12-18", "2027-01-25"),
]

EFFECTS_REFUSALS = [
    ("fcrx", "calendar_days", 5, "next_business_day", "2026-08-14",
     "business days in periods of"),
    ("fcrx", "months", 2, "none", "2026-11-30", "excluded ranges"),
    ("winhol", "calendar_days", 7, "next_business_day", "2026-12-12",
     "would enter an excluded range"),
]


def rule_id(unit: str, length: int, rollover: str) -> str:
    return f"{unit}-{length}-{rollover}"


def build_rules_table(
    table_key: str,
    combos: set[tuple[str, int, str]],
    holiday_table: str | None = None,
    effects: dict | None = None,
) -> dict:
    provision = {
        "id": "test-provision",
        "citation": "Test Interpretation Provision s 1",
        "role": "time_computation",
        "summary": "Test.",
        "evidence": dict(VERIFIED),
    }
    if effects:
        provision["time_computation_effects"] = effects
    return {
        "table_id": f"test-{table_key}",
        "jurisdiction": table_key.upper(),
        "forums": ["Test forum"],
        "holiday_table": holiday_table or table_key,
        "note": "Synthetic verified table for engine tests.",
        "computation_provisions": [provision],
        "period_rules": [
            {
                "id": rule_id(unit, length, rollover),
                "label": "Test rule",
                "citation": "Test Rules r 1",
                "trigger": "Test trigger",
                "period": {"length": length, "unit": unit},
                "rollover": rollover,
                "applies_provisions": ["test-provision"],
                "evidence": dict(VERIFIED),
            }
            for unit, length, rollover in sorted(combos)
        ],
    }


class ComputationEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        cls.tables_dir = Path(cls._tmp.name)
        (cls.tables_dir / "computation-rules").mkdir()
        shutil.copytree(
            PLUGIN / "references" / "holidays", cls.tables_dir / "holidays"
        )
        cases = FIXTURES + [case[:5] for case in REFUSALS]
        for table_key in ("nsw", "vic"):
            combos = {
                (unit, length, rollover)
                for key, unit, length, rollover, *_ in cases
                if key == table_key
            }
            table = build_rules_table(table_key, combos)
            path = cls.tables_dir / "computation-rules" / f"test-{table_key}.json"
            path.write_text(json.dumps(table), encoding="utf-8")

        effects_cases = EFFECTS_FIXTURES + [case[:5] for case in EFFECTS_REFUSALS]
        for table_key, holiday_key in (("fcrx", "nsw"), ("winhol", "winhol")):
            combos = {
                (unit, length, rollover)
                for key, unit, length, rollover, *_ in effects_cases
                if key == table_key
            }
            table = build_rules_table(
                table_key, combos, holiday_table=holiday_key, effects=FCR_EFFECTS
            )
            path = cls.tables_dir / "computation-rules" / f"test-{table_key}.json"
            path.write_text(json.dumps(table), encoding="utf-8")
        (cls.tables_dir / "holidays" / "winhol.json").write_text(
            json.dumps(
                {
                    "table_id": "winhol",
                    "jurisdiction": "TEST",
                    "source_url": "https://example.invalid/",
                    "checked": "2026-08-14",
                    "evidence": dict(VERIFIED),
                    "coverage": {"from": "2026-01-01", "to": "2026-12-31"},
                    "holidays": ["2026-12-21", "2026-12-22", "2026-12-23"],
                    "uncertain_windows": [],
                    "caveats": [],
                }
            ),
            encoding="utf-8",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def run_engine(
        self, table_key: str, unit: str, length: int, rollover: str, trigger: str
    ) -> dict:
        return ENGINE.compute(
            {
                "table_id": f"test-{table_key}",
                "period_rule_id": rule_id(unit, length, rollover),
                "trigger_date": trigger,
            },
            self.tables_dir,
        )

    def test_hand_derived_fixtures(self) -> None:
        for table_key, unit, length, rollover, trigger, expected in FIXTURES:
            with self.subTest(f"{table_key} {unit} {length} {rollover} {trigger}"):
                result = self.run_engine(table_key, unit, length, rollover, trigger)
                self.assertEqual(result["status"], "computed", result)
                self.assertEqual(result["candidate_date"], expected)
                self.assertIn("Test Rules r 1", result["provisions_applied"])
                self.assertIn("not a diary", result["disclaimer"])

    def test_refusals_fail_closed(self) -> None:
        for table_key, unit, length, rollover, trigger, reason in REFUSALS:
            with self.subTest(f"{table_key} {unit} {length} {trigger}"):
                result = self.run_engine(table_key, unit, length, rollover, trigger)
                self.assertEqual(result["status"], "identify_only", result)
                self.assertIn(reason, result["reason"])

    def test_excluded_range_fixtures(self) -> None:
        for table_key, unit, length, rollover, trigger, expected in EFFECTS_FIXTURES:
            with self.subTest(f"{table_key} {unit} {length} {trigger}"):
                result = self.run_engine(table_key, unit, length, rollover, trigger)
                self.assertEqual(result["status"], "computed", result)
                self.assertEqual(result["candidate_date"], expected)

    def test_excluded_range_refusals_fail_closed(self) -> None:
        for table_key, unit, length, rollover, trigger, reason in EFFECTS_REFUSALS:
            with self.subTest(f"{table_key} {unit} {length} {trigger}"):
                result = self.run_engine(table_key, unit, length, rollover, trigger)
                self.assertEqual(result["status"], "identify_only", result)
                self.assertIn(reason, result["reason"])

    def test_every_nsw_2026_holiday_rolls_to_a_business_day(self) -> None:
        table = json.loads(
            (self.tables_dir / "holidays" / "nsw.json").read_text(encoding="utf-8")
        )
        holidays = {dt.date.fromisoformat(day) for day in table["holidays"]}
        for holiday in sorted(day for day in holidays if day.year == 2026):
            trigger = holiday - dt.timedelta(days=1)
            result = self.run_engine(
                "nsw", "calendar_days", 1, "next_business_day", trigger.isoformat()
            )
            self.assertEqual(result["status"], "computed", holiday)
            rolled = dt.date.fromisoformat(result["candidate_date"])
            self.assertGreater(rolled, holiday)
            self.assertLess(rolled.weekday(), 5, holiday)
            self.assertNotIn(rolled, holidays, holiday)

    def test_unverified_holiday_table_refuses(self) -> None:
        unverified = json.loads(
            (self.tables_dir / "holidays" / "nsw.json").read_text(encoding="utf-8")
        )
        unverified["table_id"] = "unv"
        unverified["evidence"] = {"state": "pending-verification"}
        (self.tables_dir / "holidays" / "unv.json").write_text(
            json.dumps(unverified), encoding="utf-8"
        )
        table = build_rules_table(
            "unv", {("calendar_days", 1, "next_business_day")}
        )
        (self.tables_dir / "computation-rules" / "test-unv.json").write_text(
            json.dumps(table), encoding="utf-8"
        )
        result = self.run_engine(
            "unv", "calendar_days", 1, "next_business_day", "2026-08-14"
        )
        self.assertEqual(result["status"], "identify_only")
        self.assertIn("holiday table unv", result["reason"])

    def test_pending_rule_and_pending_provision_refuse(self) -> None:
        table = build_rules_table("nsw", {("calendar_days", 3, "none")})
        table["table_id"] = "test-pending"
        table["period_rules"][0]["evidence"] = {"state": "pending-verification"}
        path = self.tables_dir / "computation-rules" / "test-pending.json"
        path.write_text(json.dumps(table), encoding="utf-8")
        result = ENGINE.compute(
            {
                "table_id": "test-pending",
                "period_rule_id": rule_id("calendar_days", 3, "none"),
                "trigger_date": "2026-08-14",
            },
            self.tables_dir,
        )
        self.assertEqual(result["status"], "identify_only")

        table["period_rules"][0]["evidence"] = dict(VERIFIED)
        table["computation_provisions"][0]["evidence"] = {
            "state": "pending-verification"
        }
        path.write_text(json.dumps(table), encoding="utf-8")
        result = ENGINE.compute(
            {
                "table_id": "test-pending",
                "period_rule_id": rule_id("calendar_days", 3, "none"),
                "trigger_date": "2026-08-14",
            },
            self.tables_dir,
        )
        self.assertEqual(result["status"], "identify_only")
        self.assertIn("test-provision", result["reason"])

    def test_unknown_rule_and_bad_trigger_are_errors(self) -> None:
        with self.assertRaises(ValueError):
            ENGINE.compute(
                {
                    "table_id": "test-nsw",
                    "period_rule_id": "no-such-rule",
                    "trigger_date": "2026-08-14",
                },
                self.tables_dir,
            )
        with self.assertRaises(ValueError):
            ENGINE.compute(
                {
                    "table_id": "test-nsw",
                    "period_rule_id": rule_id(
                        "calendar_days", 28, "next_business_day"
                    ),
                    "trigger_date": "14/08/2026",
                },
                self.tables_dir,
            )

    def test_cli_round_trip(self) -> None:
        request = self.tables_dir / "request.json"
        request.write_text(
            json.dumps(
                {
                    "table_id": "test-nsw",
                    "period_rule_id": rule_id(
                        "calendar_days", 28, "next_business_day"
                    ),
                    "trigger_date": "2026-08-14",
                }
            ),
            encoding="utf-8",
        )
        exit_code = ENGINE.main(
            ["--input", str(request), "--tables-dir", str(self.tables_dir)]
        )
        self.assertEqual(exit_code, 0)
        bad = self.tables_dir / "bad.json"
        bad.write_text(json.dumps({"table_id": "test-nsw"}), encoding="utf-8")
        exit_code = ENGINE.main(
            ["--input", str(bad), "--tables-dir", str(self.tables_dir)]
        )
        self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
