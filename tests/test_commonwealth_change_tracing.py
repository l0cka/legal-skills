from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "plugins"
    / "australian-legislation"
    / "skills"
    / "trace-commonwealth-legislative-change"
    / "scripts"
    / "frl_change_trace.py"
)
SKILL = SCRIPT.parents[1] / "SKILL.md"
METHOD = SCRIPT.parents[1] / "references" / "change-tracing-method.md"

SPEC = importlib.util.spec_from_file_location("frl_change_trace", SCRIPT)
assert SPEC and SPEC.loader
TRACE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TRACE)


def version(
    register_id: str,
    start: str,
    compilation: str,
    *,
    reasons: list[dict] | None = None,
    unincorporated: bool = False,
    retrospective_start: str | None = None,
) -> dict:
    return {
        "titleId": "C2004A03712",
        "registerId": register_id,
        "start": start,
        "end": None,
        "retrospectiveStart": retrospective_start or start,
        "retrospectiveEnd": None,
        "registeredAt": start,
        "compilationNumber": compilation,
        "status": "InForce",
        "hasUnincorporatedAmendments": unincorporated,
        "reasons": reasons or [],
    }


class CommonwealthChangeTraceTests(unittest.TestCase):
    def test_rejects_invalid_or_non_increasing_interval(self) -> None:
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_title_id("Privacy Act 1988")
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_interval("2024-02-30", "2024-06-01")
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_interval("2024-06-01", "2024-06-01")
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_interval("2024-06-02", "2024-06-01")

    def test_endpoint_match_is_fail_closed(self) -> None:
        versions = [version("C2024C00001", "2024-01-01T00:00:00", "1")]
        selected = TRACE.select_endpoint(
            versions,
            {"registerId": "C2024C00001", "start": "2024-01-01T00:00:00"},
        )
        self.assertEqual(selected["compilationNumber"], "1")
        with self.assertRaises(TRACE.TraceError):
            TRACE.select_endpoint(
                versions,
                {"registerId": "C9999C99999", "start": "2024-01-01T00:00:00"},
            )

    @patch.object(TRACE, "api_get")
    def test_trace_enumerates_every_transition_and_normalizes_reasons(self, api_get) -> None:
        first = version("C2024C00001", "2024-01-01T00:00:00", "1")
        middle = version(
            "C2024C00002",
            "2024-03-01T00:00:00",
            "2",
            reasons=[
                {
                    "affect": "Amend",
                    "affectedByTitle": {
                        "titleId": "C2024A00010",
                        "name": "Example Amendment Act 2024",
                        "seriesType": "Act",
                        "year": 2024,
                        "number": 10,
                        "provisions": "sch 1 (item 3)",
                    },
                }
            ],
        )
        last = version("C2024C00003", "2024-05-01T00:00:00", "3")
        api_get.side_effect = [
            {
                "id": "C2004A03712",
                "name": "Privacy Act 1988",
                "collection": "Act",
                "hasCommencedUnincorporatedAmendments": False,
                "versions": [last, first, middle],
            },
            {"registerId": first["registerId"], "start": first["start"]},
            {"registerId": last["registerId"], "start": last["start"]},
        ]

        result = TRACE.trace("C2004A03712", "2024-01-15", "2024-06-01")

        self.assertEqual(
            [item["registerId"] for item in result["transitions"]],
            ["C2024C00002", "C2024C00003"],
        )
        affecting = result["transitions"][0]["reasons"][0]["affectingTitle"]
        self.assertEqual(affecting["provisions"], "sch 1 (item 3)")
        self.assertEqual(
            affecting["officialUrl"],
            "https://www.legislation.gov.au/C2024A00010",
        )
        self.assertIn("navigation evidence", result["warnings"][1])

    @patch.object(TRACE, "api_get")
    def test_same_compilation_and_currency_flags_do_not_overclaim(self, api_get) -> None:
        only = version(
            "C2024C00001",
            "2024-01-01T00:00:00",
            "1",
            unincorporated=True,
            retrospective_start="2023-12-15T00:00:00",
        )
        api_get.side_effect = [
            {
                "id": "C2004A03712",
                "name": "Privacy Act 1988",
                "collection": "Act",
                "hasCommencedUnincorporatedAmendments": True,
                "versions": [only],
            },
            {"registerId": only["registerId"], "start": only["start"]},
            {"registerId": only["registerId"], "start": only["start"]},
        ]

        result = TRACE.trace("C2004A03712", "2024-01-15", "2024-02-01")

        self.assertTrue(result["sameCompilation"])
        self.assertEqual(result["transitions"], [])
        self.assertTrue(
            result["currencyFlags"]["currentTitleHasCommencedUnincorporatedAmendments"]
        )
        self.assertTrue(result["currencyFlags"]["retrospectiveFieldsDiffer"])
        self.assertIn("not that legal operation was unchanged", result["warnings"][0])

    def test_skill_and_method_preserve_critical_boundaries(self) -> None:
        skill = " ".join(SKILL.read_text(encoding="utf-8").split())
        method = " ".join(METHOD.read_text(encoding="utf-8").split())
        for phrase in (
            "INTERVENING CHANGES WITH NO NET CHANGE",
            "compilation reasons as navigation evidence",
            "Do not infer legal operation",
            "commenced but unincorporated amendment",
            "Never say that a compilation commenced",
            "Do not transfer that label to HTML, EPUB",
            "limit one trace to 10",
        ):
            self.assertIn(phrase, skill)
        for phrase in (
            "endpoint-only diff",
            "commencement separate from incorporation",
            "does not itself commence",
            "Do not call HTML, EPUB",
            "application, savings and transitional",
            "replacement compilations",
        ):
            self.assertIn(phrase, method)

    def test_cli_rejects_malformed_input_without_network(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "trace",
                "not-an-id",
                "--from",
                "2024-01-01",
                "--to",
                "2024-06-01",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Title ID must look like", result.stderr)


if __name__ == "__main__":
    unittest.main()
