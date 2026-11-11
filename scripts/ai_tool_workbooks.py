#!/usr/bin/env python3

from __future__ import annotations

import datetime as dt
import io
import json
import re
import zipfile
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

DEADLINE_WORKBOOK = "references/deadline-calculator.xlsx"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
FIXED_STAMP = "2026-01-01T00:00:00Z"
CORE_STAMP = re.compile(r"(<dcterms:(created|modified)[^>]*>)[^<]*(</dcterms:\2>)")
SUPPORTED_UNITS = ("calendar_days", "clear_days", "business_days", "months", "years")
CUSTOM_HOLIDAYS = "custom"
HOLIDAY_ROWS = 100
WINDOW_ROWS = 40
SCAN_DAYS = 120
ROLL_DAYS = 15
EXCLUDED_BLOCKS = 2
MAX_RULE_ROWS = 200
CIVIL = "Civil step fixed by a rule"
OUT_OF_SCOPE_TYPES = ("Criminal procedure", "Court-fixed or discretionary date")
STATUS_CANDIDATE = "CANDIDATE DATE - NOT BINDING UNTIL CONFIRMED"
STATUS_IDENTIFY = "IDENTIFY-ONLY - NOT COMPUTED"
DATE_FORMAT = "yyyy-mm-dd"
WORKING_NOTE = "Working values for review only. No gate is applied here, so no date on this sheet is a result. Read dates only on the Calculator sheet."
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
OUTPUT_FILL = PatternFill("solid", fgColor="E2EFDA")
WRAP = Alignment(wrap_text=True, vertical="top")
BOLD = Font(bold=True)

CALCULATOR_INPUTS = (
    ("rule", "Forum and rule", "Pick from the list. Rules come from the computation-rule tables; a step not listed is identify-only."),
    ("event", "Trigger event", "What happened: service, filing, judgment or notification. Supplied by the lawyer."),
    ("trigger", "Trigger date", "Lawyer-supplied date (YYYY-MM-DD). Never estimate it."),
    ("contested", "Is the trigger date contested or unknown?", "Answer No only when the lawyer confirms the date. Yes means NOT READY."),
    ("matter", "Matter type", "Criminal procedure and court-fixed or discretionary dates are OUTSIDE SCOPE."),
    ("registry", "Registry holiday table", "Needed when the rule says registry choice (federal courts, ART): the table of the registry where the act is to be done."),
    ("profile", "Approved deadline profile", "Name and version of the approved profile."),
    ("approved", "Is that profile approved?", "Yes only when the profile's approval is recorded."),
    ("confirmer", "Named confirmer", "The person who must confirm the date before reliance."),
    ("diary", "Diary system of record", "Where the confirmed date is entered."),
)

CALCULATOR_OUTPUTS = (
    ("status", "Status"),
    ("candidate", "Candidate date"),
    ("day", "Candidate day"),
    ("reason", "Reason"),
    ("table", "Forum table"),
    ("label", "Step"),
    ("citation", "Governing rule"),
    ("ruletrigger", "Rule's trigger"),
    ("period", "Period"),
    ("rollover", "Rollover"),
    ("provisions", "Provisions applied"),
    ("holidays", "Holiday table used"),
    ("warnings", "Warnings"),
    ("caveats", "Holiday caveats"),
    ("source", "Source"),
    ("evidence", "Evidence"),
    ("gate", "Human decision gate"),
    ("limits", "Limitations"),
)

RULE_COLUMNS = (
    "key", "table_id", "rule_id", "label", "citation", "trigger", "length", "unit", "rollover",
    "rule_evidence", "provision_evidence", "provisions", "ex1_from", "ex1_to", "ex2_from", "ex2_to",
    "short_threshold", "holiday_table", "registry_choice", "warnings", "source_url", "checked", "forums",
)

NUMERIC_RULE_COLUMNS = {"length", "ex1_from", "ex1_to", "ex2_from", "ex2_to", "short_threshold"}

HOLIDAY_TABLE_COLUMNS = ("table_id", "evidence", "coverage_from", "coverage_to", "source_url", "checked", "caveats", "verified_by")

SCOPE_ROWS = (
    ("Criminal procedure", "OUTSIDE SCOPE. Route to the responsible lawyer."),
    ("Court-fixed or discretionary dates", "OUTSIDE SCOPE or identify-only. A court order or direction fixes the date."),
    ("Contested or unknown trigger date", "NOT READY. Never assume a trigger date."),
    ("Forum or step not in the Rules sheet", "Identify-only. Name the governing rule and route verification to verify-deadline-basis."),
    ("VCAT", "No general review period. The enabling enactment fixes the period: identify-only."),
    ("Tribunal step whose conferring Act fixes its own period", "The conferring Act governs (for QCAT, s 6(7) of the QCAT Act says so). Identify-only until that Act is checked."),
    ("Migration matters", "Time limits are non-extendable or jurisdictional and have changed repeatedly. Specialist review before reliance."),
    ("Rule or provision in pending-verification state", "Identify-only. Verify it with verify-deadline-basis first."),
    ("Dates outside a holiday table's coverage or in an uncertain window", "Identify-only. Refresh or confirm the holiday table first."),
)

ABOUT_LINES = (
    "Deadline calculator: candidate dates only",
    "",
    "This workbook counts a candidate date from a lawyer-supplied trigger date, the period rule picked on the Calculator sheet and the holiday table of the registry. The model never does this arithmetic; the sheet's formulas do, and a person checks the result.",
    "",
    "Safeguards built into the Calculator sheet:",
    "1. No date is shown unless the profile is approved, a confirmer and a diary system of record are named, the trigger date is confirmed and the matter is in scope.",
    "2. Every refusal of the deterministic computation is reproduced: unverified rules, provisions or holiday tables, dates outside coverage or in an uncertain holiday window, short periods that count only business days, and a rollover into an excluded range.",
    "3. A candidate date is never the binding deadline. The named confirmer confirms it against the official source and enters it in the diary system of record before reliance.",
    "4. The Scope sheet lists what this workbook does not cover.",
    "",
    "Sheets: Calculator (inputs and result), Rules (period rules from the computation-rule tables), HolidayTables and Holidays (holiday data per registry, with a custom column a person fills and verifies), Windows (uncertain holiday windows), Scope (out-of-scope matters), Engine and Working (the formulas, open for review).",
    "",
    "Counting method: the trigger day is not counted. Calendar days add the period; clear days add one more day; months and years use the corresponding date, or the last day of a shorter month. Excluded ranges are skipped. Business days skip weekends and the registry's holidays. Rollover moves a last day that is not a business day to the next business day.",
    "",
    "The custom holiday column is for a registry not listed. Enter each holiday date, then set its HolidayTables row to verified, with coverage dates, source and the name of the person who verified it. Until then the sheet refuses any computation that needs it.",
    "",
    "Limits: day counts and business-day periods are scanned up to 120 days after the trigger, and a rollover up to 15 days; beyond that the sheet refuses. Excluded ranges are written as month and day (1224 is 24 December). The custom holiday column takes up to 100 dates and the Windows sheet up to 40 added windows; anything typed below those rows is ignored. Every sheet is protected without a password to prevent accidental edits; only the yellow cells are unlocked.",
    "",
    "Do not overwrite cells on the Rules, Engine or Working sheets. Edit the computation-rule tables instead and use a newer release of this workbook.",
)


def cell_ref(sheet: str, column: int, row: int) -> str:
    return f"{sheet}!${get_column_letter(column)}${row}"


def column_range(sheet: str, column: int, first: int, last: int) -> str:
    letter = get_column_letter(column)
    return f"{sheet}!${letter}${first}:${letter}${last}"


def quoted(text: str) -> str:
    return '"' + text.replace('"', '""') + '"'


def iso(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def month_day(value: str) -> int:
    month, day = map(int, value.split("-"))
    dt.date(2000, month, day)
    return month * 100 + day


def mark_input(cell) -> None:
    cell.fill = INPUT_FILL
    cell.protection = Protection(locked=False)


def evidence_message(kind: str, ident: str, state: object) -> str:
    return (
        f"{kind} {ident} is in evidence state {state!r}, not 'verified'; verify it "
        "against the official publisher with verify-deadline-basis first"
    )


def resolve_provisions(table: dict, rule: dict) -> tuple[str, list[str], list[int], int]:
    provisions = {p["id"]: p for p in table.get("computation_provisions", [])}
    applied: list[str] = []
    ranges: list[int] = []
    threshold = 0
    for prov_id in rule.get("applies_provisions", []):
        provision = provisions.get(prov_id)
        if provision is None:
            return f"provision {prov_id!r} referenced by rule {rule['id']} is not in the table", [], [], 0
        state = (provision.get("evidence") or {}).get("state")
        if state != "verified":
            return evidence_message("provision", prov_id, state), [], [], 0
        applied.append(provision["citation"])
        effects = provision.get("time_computation_effects") or {}
        for entry in effects.get("excluded_ranges", []):
            ranges.extend((month_day(entry["from"]), month_day(entry["to"])))
        threshold = max(threshold, effects.get("short_period_threshold_days", 0))
    if len(ranges) > 2 * EXCLUDED_BLOCKS:
        raise ValueError(f"rule {rule['id']}: more than {EXCLUDED_BLOCKS} excluded ranges")
    return "verified", applied, ranges + [0] * (2 * EXCLUDED_BLOCKS - len(ranges)), threshold


def rule_rows(rule_tables: list[dict]) -> list[list[object]]:
    rows: list[list[object]] = []
    for table in sorted(rule_tables, key=lambda t: t["table_id"]):
        placeholder = bool(table.get("holiday_table_placeholder"))
        for rule in table.get("period_rules", []):
            provision_evidence, applied, ranges, threshold = resolve_provisions(table, rule)
            evidence = rule.get("evidence") or {}
            period = rule.get("period") or {}
            rows.append([
                f"{table['table_id']} / {rule['id']}",
                table["table_id"],
                rule["id"],
                rule.get("label") or "",
                rule.get("citation") or "",
                rule.get("trigger") or "",
                period.get("length"),
                period.get("unit") or "",
                rule.get("rollover", "none"),
                evidence.get("state") or "",
                provision_evidence,
                "; ".join(applied),
                *ranges,
                threshold,
                "registry choice" if placeholder else (table.get("holiday_table") or ""),
                "yes" if placeholder else "no",
                " | ".join(rule.get("warnings", [])),
                rule.get("source_url") or "",
                evidence.get("checked") or "",
                "; ".join(table.get("forums", [])),
            ])
    if len(rows) > MAX_RULE_ROWS:
        raise ValueError(f"more than {MAX_RULE_ROWS} period rules")
    return rows


class Formulas:
    def __init__(self, sheet) -> None:
        self.sheet = sheet
        self.cells: dict[str, str] = {}
        sheet.append(["Name", "Value", "Meaning"])
        for cell in sheet[1]:
            cell.font = BOLD

    def add(self, name: str, formula: str, meaning: str, date: bool = False) -> str:
        row = self.sheet.max_row + 1
        self.sheet.cell(row, 1, name)
        target = self.sheet.cell(row, 2, "=" + formula.format(**self.cells))
        if date:
            target.number_format = DATE_FORMAT
        self.sheet.cell(row, 3, meaning)
        self.cells[name] = cell_ref(self.sheet.title, 2, row)
        return self.cells[name]


class Layout:
    def __init__(self, holiday_count: int, window_count: int) -> None:
        self.rule_last = 1 + MAX_RULE_ROWS
        self.tables_last = 2 + holiday_count
        self.holiday_last = 1 + HOLIDAY_ROWS
        self.custom_col = holiday_count + 1
        self.windows_last = 1 + window_count + WINDOW_ROWS
        self.scan_first = 2
        self.scan_last = self.scan_first + SCAN_DAYS - 1
        self.roll_first = self.scan_last + 3
        self.roll_last = self.roll_first + ROLL_DAYS - 1
        self.picked_first = 2
        self.picked_last = 1 + HOLIDAY_ROWS

    def scan(self, column: int) -> str:
        return column_range("Working", column, self.scan_first, self.scan_last)

    def roll(self, column: int) -> str:
        return column_range("Working", column, self.roll_first, self.roll_last)

    def picked(self, column: int) -> str:
        return column_range("Working", column, self.picked_first, self.picked_last)

    def window(self, column: int) -> str:
        return column_range("Windows", column, 2, self.windows_last)

    def rule(self, name: str) -> str:
        return column_range("Rules", RULE_COLUMNS.index(name) + 1, 2, self.rule_last)

    def table(self, column: int) -> str:
        return column_range("HolidayTables", column, 2, self.tables_last)


def write_about(ws) -> None:
    for line in ABOUT_LINES:
        ws.append([line])
    ws["A1"].font = Font(bold=True, size=14)
    ws.column_dimensions["A"].width = 120
    for row in ws.iter_rows():
        row[0].alignment = Alignment(wrap_text=True)


def write_rules(ws, rule_tables: list[dict]) -> None:
    ws.append(list(RULE_COLUMNS))
    for row in rule_rows(rule_tables):
        ws.append(row)
    ws.freeze_panes = "A2"


def write_holiday_tables(ws, holiday_tables: list[dict]) -> None:
    ws.append(list(HOLIDAY_TABLE_COLUMNS))
    for table in holiday_tables:
        ws.append([
            table["table_id"],
            (table.get("evidence") or {}).get("state") or "",
            iso(table["coverage"]["from"]),
            iso(table["coverage"]["to"]),
            table.get("source_url") or "",
            table.get("checked") or "",
            " | ".join(table.get("caveats", [])),
            "",
        ])
    ws.append([CUSTOM_HOLIDAYS, "not verified", None, None, "", "", "Filled by the firm for a registry not listed.", ""])
    custom = ws.max_row
    for row in ws.iter_rows(min_row=2, max_row=custom):
        row[2].number_format = DATE_FORMAT
        row[3].number_format = DATE_FORMAT
    for col in (2, 3, 4, 5, 6, 8):
        mark_input(ws.cell(custom, col))
    state = DataValidation(type="list", formula1='"verified,not verified"', allow_blank=False)
    ws.add_data_validation(state)
    state.add(f"B{custom}")
    dates = DataValidation(type="date", operator="greaterThan", formula1="1")
    ws.add_data_validation(dates)
    dates.add(f"C{custom}:D{custom}")
    ws.freeze_panes = "A2"


def write_holidays(ws, holiday_tables: list[dict], layout: Layout) -> None:
    for index, table in enumerate(holiday_tables, 1):
        ws.cell(1, index, table["table_id"]).font = BOLD
        for offset, day in enumerate(sorted(table["holidays"])):
            ws.cell(2 + offset, index, iso(day)).number_format = DATE_FORMAT
    ws.cell(1, layout.custom_col, CUSTOM_HOLIDAYS).font = BOLD
    for row in range(2, layout.holiday_last + 1):
        cell = ws.cell(row, layout.custom_col)
        mark_input(cell)
        cell.number_format = DATE_FORMAT
    dates = DataValidation(type="date", operator="greaterThan", formula1="1")
    ws.add_data_validation(dates)
    letter = get_column_letter(layout.custom_col)
    dates.add(f"{letter}2:{letter}{layout.holiday_last}")
    ws.freeze_panes = "A2"


def write_windows(ws, holiday_tables: list[dict], layout: Layout) -> None:
    ws.append(["holiday_table", "from", "to", "reason"])
    for table in holiday_tables:
        for window in table.get("uncertain_windows", []):
            ws.append([table["table_id"], iso(window["from"]), iso(window["to"]), window.get("reason", "uncertain window")])
    for row in range(ws.max_row + 1, layout.windows_last + 1):
        for col in range(1, 5):
            mark_input(ws.cell(row, col))
    for row in ws.iter_rows(min_row=2, max_row=layout.windows_last):
        row[1].number_format = DATE_FORMAT
        row[2].number_format = DATE_FORMAT
    ws.freeze_panes = "A2"


def write_scope(ws) -> None:
    ws.append(["Matter or forum", "How this workbook treats it"])
    for row in SCOPE_ROWS:
        ws.append(list(row))
    ws.column_dimensions["A"].width = 50
    ws.column_dimensions["B"].width = 100


def write_calculator_inputs(ws, layout: Layout) -> dict[str, str]:
    ws["A1"] = "Deadline calculator: candidate dates only"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = "A candidate date is never the binding deadline. The named confirmer confirms it against the official source and enters it in the diary system of record before reliance."
    ws["A2"].alignment = WRAP
    ws.merge_cells("A2:C2")
    ws.row_dimensions[2].height = 32
    ws["A3"] = "Inputs (yellow)"
    ws["A3"].font = BOLD
    lists = {
        "rule": f"=Rules!$A$2:$A${layout.rule_last}",
        "contested": '"No,Yes"',
        "matter": quoted(",".join((CIVIL, *OUT_OF_SCOPE_TYPES))),
        "registry": f"=HolidayTables!$A$2:$A${layout.tables_last}",
        "approved": '"Yes,No"',
    }
    inputs: dict[str, str] = {}
    for row, (name, label, help_text) in enumerate(CALCULATOR_INPUTS, 4):
        ws.cell(row, 1, label)
        target = ws.cell(row, 2)
        mark_input(target)
        ws.cell(row, 3, help_text).alignment = WRAP
        inputs[name] = cell_ref("Calculator", 2, row)
        if name == "trigger":
            target.number_format = DATE_FORMAT
            check = DataValidation(type="date", operator="greaterThan", formula1="1")
        elif name in lists:
            check = DataValidation(type="list", formula1=lists[name], allow_blank=True)
        else:
            continue
        ws.add_data_validation(check)
        check.add(target.coordinate)
    for letter, width in (("A", 38), ("B", 60), ("C", 70)):
        ws.column_dimensions[letter].width = width
    return inputs


def excluded_test(day: str, e: dict[str, str]) -> str:
    md = f"(MONTH({day})*100+DAY({day}))"
    parts = []
    for block in range(1, EXCLUDED_BLOCKS + 1):
        start, end = f"N({e[f'ex{block}_from']})", f"N({e[f'ex{block}_to']})"
        parts.append(f"AND({start}>0,IF({start}<={end},AND({md}>={start},{md}<={end}),OR({md}>={start},{md}<={end})))")
    return f"IF(OR({','.join(parts)}),1,0)"


def business_test(day: str, layout: Layout) -> str:
    return f"IF(AND(WEEKDAY({day},2)<6,COUNTIF({layout.picked(10)},{day})=0),1,0)"


def usable_test(day: str, e: dict[str, str], layout: Layout) -> str:
    windows = f"COUNTIFS({layout.window(1)},{e['hol_id']},{layout.window(2)},\"<=\"&{day},{layout.window(3)},\">=\"&{day})"
    return f"IF(AND({day}>={e['cover_from']},{day}<={e['cover_to']},{windows}=0),1,0)"


def unusable_reason(layout: Layout) -> str:
    day = "{unusable_day}"
    window = "INDEX({column},{{window_row}})"
    start, end, why = (window.format(column=layout.window(column)) for column in (2, 3, 4))
    return (
        f"IF(OR({day}<{{cover_from}},{day}>{{cover_to}}),"
        f"\"holiday table \"&{{hol_id}}&\" covers \"&TEXT({{cover_from}},\"yyyy-mm-dd\")&\" to \"&TEXT({{cover_to}},\"yyyy-mm-dd\")&\" and does not cover \"&TEXT({day},\"yyyy-mm-dd\")&\"; refresh the table before computing dates in that range\","
        f"TEXT({day},\"yyyy-mm-dd\")&\" falls in an uncertain holiday window (\"&TEXT({start},\"yyyy-mm-dd\")&\" to \"&TEXT({end},\"yyyy-mm-dd\")&\"): \"&{why})"
    )


def state_repr(cell: str) -> str:
    return f"IF({cell}=\"\",\"None\",\"'\"&{cell}&\"'\")"


def not_verified(cell: str) -> str:
    return f"NOT(EXACT({cell},\"verified\"))"


def write_window_hits(ws, e: dict[str, str], layout: Layout) -> None:
    ws.cell(1, 5, "touches the refused day").font = BOLD
    for row in range(2, layout.windows_last + 1):
        ws.cell(row, 5, f"=IF(AND(A{row}<>\"\",A{row}={e['hol_id']},N(B{row})<={e['unusable_day']},N(C{row})>={e['unusable_day']}),1,0)")


def write_working(ws, e: dict[str, str], layout: Layout) -> None:
    ws.append(["day", "date", "excluded", "business day", "usable", "counted", "running count", "refused"])
    for index in range(SCAN_DAYS):
        row = layout.scan_first + index
        day = f"B{row}"
        ws.cell(row, 1, index + 1)
        ws.cell(row, 2, f"=IF({e['trig']}=0,0,{e['trig']}+A{row})").number_format = DATE_FORMAT
        ws.cell(row, 3, "=" + excluded_test(day, e))
        ws.cell(row, 4, "=" + business_test(day, layout))
        ws.cell(row, 5, "=" + usable_test(day, e, layout))
        ws.cell(row, 6, f"=IF(C{row}=1,0,IF({e['unit']}=\"business_days\",D{row},1))")
        ws.cell(row, 7, f"=F{row}" if index == 0 else f"=G{row - 1}+F{row}")
        ws.cell(row, 8, f"=IF(AND({e['unit']}=\"business_days\",C{row}=0,E{row}=0),1,0)")
    ws.cell(layout.roll_first - 1, 1, "rollover from the last day").font = BOLD
    for index in range(ROLL_DAYS):
        row = layout.roll_first + index
        day = f"B{row}"
        ws.cell(row, 1, index)
        ws.cell(row, 2, f"=IF({e['raw']}=0,0,{e['raw']}+A{row})").number_format = DATE_FORMAT
        ws.cell(row, 3, "=" + excluded_test(day, e))
        ws.cell(row, 4, "=" + business_test(day, layout))
        ws.cell(row, 5, "=" + usable_test(day, e, layout))
        ws.cell(row, 6, f"=IF(OR(C{row}=1,E{row}=0,D{row}=1),1,0)")
    ws.cell(1, 10, "holiday of the chosen table").font = BOLD
    ws.cell(1, 11, "not a date").font = BOLD
    grid = f"Holidays!$A$2:${get_column_letter(layout.custom_col)}${layout.holiday_last}"
    for index in range(HOLIDAY_ROWS):
        row = layout.picked_first + index
        pick = f"INDEX({grid},{index + 1},{e['hol_col']})"
        ws.cell(row, 10, f"=IF({e['hol_col']}=0,0,IF(ISNUMBER({pick}),INT({pick}),0))").number_format = DATE_FORMAT
        ws.cell(row, 11, f"=IF({e['hol_col']}=0,0,IF(OR(ISNUMBER({pick}),{pick}=\"\"),0,1))")


def write_engine(ws, inputs: dict[str, str], layout: Layout) -> Formulas:
    f = Formulas(ws)
    header = f"Holidays!$A$1:${get_column_letter(layout.custom_col)}$1"
    f.add("idx", f"IF({inputs['rule']}=\"\",0,IFERROR(MATCH({inputs['rule']},{layout.rule('key')},0),0))", "Row of the picked rule in the Rules sheet; 0 when none")
    for name in RULE_COLUMNS[1:]:
        text = "" if name in NUMERIC_RULE_COLUMNS else "&\"\""
        f.add(name, f"IF({{idx}}=0,\"\",INDEX({layout.rule(name)},{{idx}}){text})", f"Rules column {name}")
    f.add("trig", f"IF(ISNUMBER({inputs['trigger']}),INT({inputs['trigger']}),0)", "Trigger date; 0 when not a date", date=True)
    f.add("length_n", "N({length})", "Period length as a number")
    f.add("has_excl", "AND({idx}>0,N({ex1_from})>0)", "An applied provision declares an excluded range")
    f.add("needs_hol", "OR({unit}=\"business_days\",{rollover}=\"next_business_day\")", "A holiday table is needed")
    f.add("hol_id", f"IF({{registry_choice}}=\"yes\",IF({inputs['registry']}=\"\",\"\",{inputs['registry']}),{{holiday_table}})", "Holiday table: the registry choice for federal courts and the ART, else the forum's own")
    f.add("hol_row", f"IF({{hol_id}}=\"\",0,IFERROR(MATCH({{hol_id}},{layout.table(1)},0),0))", "Row of the holiday table")
    f.add("hol_col", f"IF({{hol_id}}=\"\",0,IFERROR(MATCH({{hol_id}},{header},0),0))", "Column of the holiday table in the Holidays sheet")
    f.add("hol_ev", f"IF({{hol_row}}=0,\"\",INDEX({layout.table(2)},{{hol_row}})&\"\")", "Holiday table evidence state")
    f.add("hol_named", f"IF({{hol_row}}=0,FALSE,AND(INDEX({layout.table(5)},{{hol_row}})&\"\"<>\"\",OR({{hol_id}}<>\"{CUSTOM_HOLIDAYS}\",INDEX({layout.table(8)},{{hol_row}})&\"\"<>\"\")))", "The table names its source and, for the custom table, who verified it")
    f.add("cover_from", f"IF({{hol_row}}=0,0,N(INDEX({layout.table(3)},{{hol_row}})))", "Holiday table coverage start", date=True)
    f.add("cover_to", f"IF({{hol_row}}=0,0,N(INDEX({layout.table(4)},{{hol_row}})))", "Holiday table coverage end", date=True)
    f.add("hol_caveats", f"IF({{hol_row}}=0,\"\",INDEX({layout.table(7)},{{hol_row}}))", "Holiday table caveats")
    f.add("bad_entries", f"SUM({layout.picked(11)})", "Holiday cells that are not dates")
    f.add("count_pos", f"IFERROR(MATCH({{length_n}},{layout.scan(7)},0),0)", "Scan day on which the count reaches the period length")
    f.add("count_bad", f"IFERROR(MATCH(1,{layout.scan(8)},0),0)", "First scanned business-count day the holiday table cannot answer")
    f.add("count_bad_day", f"IF({{count_bad}}=0,0,INDEX({layout.scan(2)},{{count_bad}}))", "Date of that day", date=True)
    f.add(
        "raw",
        "IF({trig}=0,0,IF({unit}=\"calendar_days\",IF({has_excl},IF({count_pos}=0,0,{trig}+{count_pos}),{trig}+{length_n}),"
        "IF({unit}=\"clear_days\",{trig}+{length_n}+1,IF({unit}=\"months\",EDATE({trig},{length_n}),"
        "IF({unit}=\"years\",EDATE({trig},12*{length_n}),IF({unit}=\"business_days\",IF({count_pos}=0,0,{trig}+{count_pos}),0))))))",
        "Last day of the period before rollover",
        date=True,
    )
    f.add("apply_roll", "AND({rollover}=\"next_business_day\",{unit}<>\"business_days\")", "Rollover applies")
    f.add("roll_pos", f"IFERROR(MATCH(1,{layout.roll(6)},0),0)", "First day from the last day that is excluded, unusable or a business day")
    f.add("roll_day", f"IF({{roll_pos}}=0,0,INDEX({layout.roll(2)},{{roll_pos}}))", "That day", date=True)
    f.add("roll_excluded", f"IF({{roll_pos}}=0,0,INDEX({layout.roll(3)},{{roll_pos}}))", "That day is excluded")
    f.add("roll_usable", f"IF({{roll_pos}}=0,0,INDEX({layout.roll(5)},{{roll_pos}}))", "The holiday table answers for that day")
    f.add("rolled", "IF({apply_roll},{roll_day},{raw})", "Working value only, not a result: no gate is applied here; read dates on the Calculator sheet", date=True)
    f.add("count_refused", "AND({count_bad}>0,OR({count_pos}=0,{count_bad}<={count_pos}))", "The business-day count reaches a day the holiday table cannot answer")
    f.add("unusable_day", "IF({count_refused},{count_bad_day},{roll_day})", "The day the holiday table cannot answer", date=True)
    f.add("window_row", f"IFERROR(MATCH(1,{layout.window(5)},0),0)", "First uncertain window touching that day")
    units = ",".join(f"{{unit}}=\"{unit}\"" for unit in SUPPORTED_UNITS)
    refusals = (
        (not_verified("{rule_evidence}"), f"\"period rule \"&{{rule_id}}&\" is in evidence state \"&{state_repr('{rule_evidence}')}&\", not 'verified'; verify it against the official publisher with verify-deadline-basis first\""),
        (not_verified("{provision_evidence}"), "{provision_evidence}"),
        (f"NOT(OR({units}))", "\"unsupported period unit '\"&{unit}&\"'; the period fails closed\""),
        ("NOT(OR({rollover}=\"none\",{rollover}=\"next_business_day\"))", "\"unsupported rollover '\"&{rollover}&\"'; the period fails closed\""),
        ("NOT(AND(ISNUMBER({length}),{length_n}>=1,{length_n}=INT({length_n})))", "\"period length must be a positive integer, got \"&IF({length}=\"\",\"None\",IF(ISNUMBER({length}),{length},\"'\"&{length}&\"'\"))"),
        ("AND({has_excl},{unit}<>\"calendar_days\",{unit}<>\"business_days\")", "\"an applied provision declares excluded ranges, which the tables express only for calendar_days and business_days periods, not '\"&{unit}&\"'; the period fails closed\""),
        ("AND(N({short_threshold})>0,{unit}=\"calendar_days\",{length_n}<=N({short_threshold}))", "\"an applied provision counts only business days in periods of \"&{short_threshold}&\" days or less, which a calendar_days rule cannot express; the period fails closed\""),
        ("AND({needs_hol},{registry_choice}=\"yes\",{hol_id}=\"\")", "\"this forum has no fixed holiday table; the request must name the holiday_table of the registry where the act is to be done\""),
        ("AND({needs_hol},{hol_row}=0)", "\"holiday table \"&{hol_id}&\" is not in the HolidayTables sheet\""),
        (f"AND({{needs_hol}},{not_verified('{hol_ev}')})", f"\"holiday table \"&{{hol_id}}&\" is in evidence state \"&{state_repr('{hol_ev}')}&\", not 'verified'; verify it against the official publisher with verify-deadline-basis first\""),
        ("AND({needs_hol},NOT({hol_named}))", "\"holiday table \"&{hol_id}&\" does not name its source and the person who verified it; fill them in the HolidayTables sheet first\""),
        ("AND({needs_hol},{bad_entries}>0)", "\"holiday table \"&{hol_id}&\" has an entry that is not a date; fix it before computing\""),
        ("{count_refused}", unusable_reason(layout)),
        ("{raw}=0", f"\"the period runs past this workbook's {SCAN_DAYS}-day scan; the period fails closed\""),
        ("AND({apply_roll},{roll_pos}=0)", f"\"no business day within {ROLL_DAYS} days of the last day; the period fails closed\""),
        ("AND({apply_roll},{roll_excluded}=1)", "\"rolling the last day would enter an excluded range at \"&TEXT({roll_day},\"yyyy-mm-dd\")&\"; the interaction of the next-business-day rule with the excluded-days provision is not settled by the tables and needs the responsible lawyer\""),
        ("AND({apply_roll},{roll_usable}=0)", unusable_reason(layout)),
    )
    expr = "\"\""
    for condition, message in reversed(refusals):
        expr = f"IF({condition},{message},{expr})"
    f.add("refusal", f"IF({{idx}}=0,\"no rule picked\",IF({{trig}}=0,\"no trigger date\",IFERROR({expr},\"the sheet could not evaluate this rule; the period fails closed\")))", "Why the computation is refused; empty when it computes")
    gates = (
        (f"{inputs['matter']}=\"\"", "\"NOT READY\"", "\"answer Matter type\""),
        (f"{inputs['matter']}<>{quoted(CIVIL)}", "\"OUTSIDE SCOPE\"", f"{inputs['matter']}&\" is outside this workbook: route it to the responsible lawyer\""),
        ("{idx}=0", "\"NOT READY\"", "\"pick a forum and rule; a step not listed is identify-only\""),
        (f"{inputs['approved']}<>\"Yes\"", "\"NOT READY\"", "\"no approved deadline profile\""),
        (f"OR(TRIM({inputs['profile']})=\"\",TRIM({inputs['confirmer']})=\"\",TRIM({inputs['diary']})=\"\")", "\"NOT READY\"", "\"name the approved profile, the confirmer and the diary system of record\""),
        (f"OR(TRIM({inputs['event']})=\"\",{{trig}}=0)", "\"NOT READY\"", "\"enter the lawyer-supplied trigger event and date\""),
        (f"{inputs['contested']}<>\"No\"", "\"NOT READY\"", "\"the trigger date is contested or unknown\""),
        ("{refusal}<>\"\"", f"\"{STATUS_IDENTIFY}\"", "{refusal}"),
    )
    status = f"\"{STATUS_CANDIDATE}\""
    reason = "\"computed from the rule and holiday table shown; confirm before reliance\""
    for condition, gate_status, gate_reason in reversed(gates):
        status = f"IF({condition},{gate_status},{status})"
        reason = f"IF({condition},{gate_reason},{reason})"
    f.add("status", f"IFERROR({status},\"NOT READY\")", "Result status")
    f.add("reason", f"IFERROR({reason},\"the sheet could not evaluate the inputs\")", "Reason for the status")
    f.add("computed", f"{{status}}=\"{STATUS_CANDIDATE}\"", "A candidate date may be shown")
    for letter, width in (("A", 18), ("B", 60), ("C", 60)):
        ws.column_dimensions[letter].width = width
    return f


def write_calculator_outputs(ws, inputs: dict[str, str], e: dict[str, str]) -> dict[str, str]:
    def show(value: str) -> str:
        return f"=IF({e['computed']},{value},\"not computed\")"

    formulas = {
        "status": f"={e['status']}",
        "candidate": show(e["rolled"]),
        "day": show(f"TEXT({e['rolled']},\"dddd\")"),
        "reason": f"={e['reason']}",
        "table": f"={e['table_id']}&IF({e['forums']}=\"\",\"\",\" (\"&{e['forums']}&\")\")",
        "label": f"={e['label']}",
        "citation": f"={e['citation']}",
        "ruletrigger": f"={e['trigger']}",
        "period": f"=IF({e['idx']}=0,\"\",{e['length']}&\" \"&SUBSTITUTE({e['unit']},\"_\",\" \"))",
        "rollover": f"=SUBSTITUTE({e['rollover']},\"_\",\" \")",
        "provisions": f"={e['citation']}&IF({e['provisions']}=\"\",\"\",\"; \"&{e['provisions']})",
        "holidays": f"=IF({e['needs_hol']},IF({e['hol_id']}=\"\",\"registry choice needed\",{e['hol_id']}),\"not needed\")",
        "warnings": f"={e['warnings']}",
        "caveats": f"=IF({e['needs_hol']},{e['hol_caveats']},\"\")",
        "source": f"={e['source_url']}",
        "evidence": f"=IF({e['idx']}=0,\"\",\"rule: \"&{e['rule_evidence']}&\" (checked \"&{e['checked']}&\"); provisions: \"&IF({e['provision_evidence']}=\"verified\",\"verified\",\"not verified\")&IF({e['needs_hol']},\"; holiday table: \"&{e['hol_ev']},\"\"))",
        "gate": f"=\"Confirm by \"&IF({inputs['confirmer']}=\"\",\"(no confirmer named)\",{inputs['confirmer']})&\"; enter in \"&IF({inputs['diary']}=\"\",\"(no diary system named)\",{inputs['diary']})&\" before any reliance\"",
        "limits": "=\"Candidate only, never the binding deadline. Not a diary system. Court directions, the registry location and the enabling enactment can change the date.\"",
    }
    first = 5 + len(CALCULATOR_INPUTS)
    ws.cell(first, 1, "Result (do not edit)").font = BOLD
    outputs: dict[str, str] = {}
    for row, (name, label) in enumerate(CALCULATOR_OUTPUTS, first + 1):
        ws.cell(row, 1, label)
        target = ws.cell(row, 2, formulas[name])
        target.fill = OUTPUT_FILL
        target.alignment = WRAP
        if name == "candidate":
            target.number_format = DATE_FORMAT
        if name == "status":
            target.font = BOLD
        outputs[f"out_{name}"] = cell_ref("Calculator", 2, row)
    return outputs


def build_deadline_workbook(rule_tables: list[dict], holiday_tables: list[dict]) -> tuple[Workbook, dict[str, str]]:
    holiday_tables = sorted(holiday_tables, key=lambda t: t["table_id"])
    for table in holiday_tables:
        if len(table["holidays"]) > HOLIDAY_ROWS:
            raise ValueError(f"holiday table {table['table_id']}: more than {HOLIDAY_ROWS} holidays")
    windows = sum(len(t.get("uncertain_windows", [])) for t in holiday_tables)
    layout = Layout(len(holiday_tables), windows)

    wb = Workbook()
    about = wb.active
    about.title = "About"
    sheets = {name: wb.create_sheet(name) for name in ("Calculator", "Rules", "HolidayTables", "Holidays", "Windows", "Scope", "Engine", "Working")}
    wb.active = 1
    write_about(about)
    write_rules(sheets["Rules"], rule_tables)
    write_holiday_tables(sheets["HolidayTables"], holiday_tables)
    write_holidays(sheets["Holidays"], holiday_tables, layout)
    write_windows(sheets["Windows"], holiday_tables, layout)
    write_scope(sheets["Scope"])
    inputs = write_calculator_inputs(sheets["Calculator"], layout)
    engine = write_engine(sheets["Engine"], inputs, layout)
    write_working(sheets["Working"], engine.cells, layout)
    write_window_hits(sheets["Windows"], engine.cells, layout)
    for name in ("Engine", "Working"):
        sheets[name].cell(1, 13, WORKING_NOTE).font = BOLD
    outputs = write_calculator_outputs(sheets["Calculator"], inputs, engine.cells)
    for ws in wb.worksheets:
        ws.protection.sheet = True
    wb.calculation.fullCalcOnLoad = True
    return wb, {**{f"in_{name}": ref for name, ref in inputs.items()}, **engine.cells, **outputs}


def workbook_bytes(wb: Workbook) -> bytes:
    raw = io.BytesIO()
    wb.save(raw)
    out = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(raw.getvalue())) as source, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as target:
        for info in source.infolist():
            data = source.read(info.filename)
            if info.filename == "docProps/core.xml":
                data = CORE_STAMP.sub(lambda m: m.group(1) + FIXED_STAMP + m.group(3), data.decode("utf-8")).encode("utf-8")
            entry = zipfile.ZipInfo(info.filename, FIXED_TIME)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.create_system = 3
            entry.external_attr = 0o644 << 16
            target.writestr(entry, data)
    return out.getvalue()


def load_tables(references: Path) -> tuple[list[dict], list[dict]]:
    rules = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((references / "computation-rules").glob("*.json"))]
    holidays = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((references / "holidays").glob("*.json"))]
    return rules, holidays


def deadline_calculator(references: Path) -> bytes:
    wb, _ = build_deadline_workbook(*load_tables(references))
    wb.properties.creator = "Legal Skills"
    wb.properties.title = "Deadline calculator: candidate dates only"
    return workbook_bytes(wb)


def bundle_workbooks(plugin: Path) -> dict[str, bytes]:
    return {DEADLINE_WORKBOOK: deadline_calculator(plugin / "references")}
