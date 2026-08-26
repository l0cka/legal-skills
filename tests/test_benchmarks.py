"""Structural checks for benchmarks/: every case parses, matches the schema and names a shipped skill."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
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


if __name__ == "__main__":
    unittest.main()
