"""Structural checks for benchmarks/: every case parses, matches the schema and names a shipped skill."""

from __future__ import annotations

import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
sys.path.insert(0, str(BENCH))
import report  # noqa: E402
import run  # noqa: E402
import score  # noqa: E402
SKILLS = {p.parent.name: p.parents[2].name for p in ROOT.glob("plugins/*/skills/*/SKILL.md")}
KEYED_REQUIRED = ("id", "set", "plugin", "skill", "prompt", "truth", "expected_status", "provenance", "tools")
RUBRIC_REQUIRED = ("id", "plugin", "skill", "prompt", "expected_status_regex", "must_include", "must_not", "tools", "author_notes", "provenance")


class BenchmarkTests(unittest.TestCase):
    def keyed_cases(self) -> list[dict]:
        cases = []
        for path in sorted(BENCH.glob("keyed/*.jsonl")):
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    cases.append(json.loads(line))
        return cases

    def rubric_cases(self) -> list[dict]:
        return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(BENCH.glob("rubrics/*.json"))]

    def test_keyed_cases_follow_schema(self) -> None:
        cases = self.keyed_cases()
        self.assertTrue(cases)
        ids = [c["id"] for c in cases]
        self.assertEqual(len(ids), len(set(ids)), "duplicate keyed ids")
        for case in cases:
            with self.subTest(case=case.get("id")):
                for field in KEYED_REQUIRED:
                    self.assertIn(field, case)
                self.assertIn(case["set"], {"citations", "quotes", "legislation", "deadlines"})
                self.assertIn(case["truth"], {"genuine", "fabricated", "n/a"})
                self.assertEqual(SKILLS.get(case["skill"]), case["plugin"], "skill must belong to plugin")
                self.assertTrue(case["expected_status"])
                for pattern in case.get("must_match", []) + case.get("must_not_match", []):
                    re.compile(pattern)
                self.assertEqual(case["provenance"]["checked"], "2026-08-26")
                if case["truth"] == "fabricated":
                    self.assertTrue(
                        case.get("forbidden_status") or case.get("must_match"),
                        "fabricated cases need a forbidden status or a must_match guard",
                    )

    def test_rubric_cases_follow_schema(self) -> None:
        cases = self.rubric_cases()
        self.assertTrue(cases)
        ids = [c["id"] for c in cases]
        self.assertEqual(len(ids), len(set(ids)), "duplicate rubric ids")
        for case in cases:
            with self.subTest(case=case["id"]):
                for field in RUBRIC_REQUIRED:
                    self.assertIn(field, case)
                self.assertEqual(SKILLS.get(case["skill"]), case["plugin"])
                re.compile(case["expected_status_regex"])
                self.assertGreaterEqual(len(case["must_include"]), 4)
                self.assertGreaterEqual(len(case["must_not"]), 2)
                for item in case["must_include"] + case["must_not"]:
                    self.assertTrue(item["item"])
                    self.assertIn(item["weight"], (1, 2, 3))
                self.assertGreater(len(case["prompt"]), 200)


class ScoringTests(unittest.TestCase):
    CASE = {
        "must_include": [{"item": "a", "weight": 1}],
        "must_not": [{"item": "b", "weight": 3}],
        "expected_status_regex": "x",
    }

    def rows(self) -> list[dict]:
        base = {"set": "rubrics", "arm": "with", "kind": "rubric", "case": self.CASE, "model": "m"}
        return [
            {**base, "judge": {"error": "boom", "present": [], "breached": [], "text": "x"}},
            {**base, "judge": {"present": ["a"], "breached": [], "text": "x"}},
        ]

    def run_score(self, directory: Path) -> str:
        out = io.StringIO()
        with redirect_stdout(out):
            self.assertEqual(score.main(["score.py", str(directory)]), 0)
        return out.getvalue().splitlines()[1]

    def test_helper_api_host_is_allowlisted(self) -> None:
        for helper in ROOT.glob("plugins/*/skills/*/scripts/frl_*.py"):
            host = re.search(r'API_ROOT = "https://([^/"]+)', helper.read_text(encoding="utf-8"))
            with self.subTest(helper=helper.name):
                self.assertIsNotNone(host)
                self.assertIn(host.group(1), run.PUBLISHER_DOMAINS)

    def test_judge_failure_is_an_error_not_a_clean_score(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "rubrics.jsonl").write_text("".join(json.dumps(r) + "\n" for r in self.rows()), encoding="utf-8")
            self.assertEqual(self.run_score(Path(tmp)).split(), ["rubrics", "with", "2", "100.0", "0", "1.00", "0", "1", "0"])

    def test_rescoring_ignores_verdicts_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "rubrics.jsonl").write_text("".join(json.dumps(r) + "\n" for r in self.rows()), encoding="utf-8")
            first = self.run_score(Path(tmp))
            self.assertEqual(self.run_score(Path(tmp)), first)

    def test_report_excludes_judge_failures(self) -> None:
        cell = report.summarise(self.rows())[("claude", "m", "rubrics", "with")]
        self.assertEqual((cell["n"], cell["err"], cell["rub"]), (2, 1, 1))

    def judge_with(self, payload: dict) -> dict:
        original = run.claude
        run.claude = lambda *args, **kwargs: payload
        try:
            return run.judge(self.CASE, "x", model="m", timeout=1, cwd=Path("."))
        finally:
            run.claude = original

    def test_malformed_judge_output_is_an_error(self) -> None:
        for payload in (
            {"result": "not json"},
            {"result": "[1, 2]"},
            {"structured_output": {"notes": "no lists"}},
        ):
            with self.subTest(payload=payload):
                self.assertIn("error", self.judge_with(payload))

    def test_well_formed_judge_output_is_kept(self) -> None:
        verdict = self.judge_with({"structured_output": {"present": ["a"], "breached": []}})
        self.assertNotIn("error", verdict)
        self.assertEqual(verdict["present"], ["a"])


if __name__ == "__main__":
    unittest.main()
