"""Structural checks for the `claude plugin eval` suite under plugins/*/evals/.

Each case is one `case.yaml` holding its prompt and graders, so the plugin
stays under the plugin directory's file limit. CI cannot run the model, so
this test keeps every case loadable: the keys the runner accepts (it rejects
an unknown grader key and drops the whole case), a prompt, a name, at least
one grader, and the option each grader type needs.

Regex graders can run offline, so they also run here against the sample
replies in tests/eval_samples/<case>/. A pass*.md sample must pass every regex
grader in its case, a fail*.md sample must fail at least one, and every regex
grader must be the one some fail sample trips. That proves each grader can
fail.
"""

from __future__ import annotations

import re
import unittest
from typing import Any

from layout import ROOT, eval_case_files, load_case

SAMPLES = ROOT / "tests" / "eval_samples"
CASE_KEYS = {
    "schema_version", "name", "description", "tags", "plugins", "runs",
    "expected_outcome", "execution", "context", "graders",
}
EXECUTION_KEYS = {
    "model", "max_turns", "timeout_seconds", "allowed_tools",
    "append_system_prompt", "env", "prompt",
}
GRADER_COMMON_KEYS = {"name", "type", "weight", "arm"}
GRADER_KEYS = {
    "regex": {"pattern", "flags", "match", "target"},
    "tool_used": {"tool", "input_match", "min", "max"},
    "tool_order": {"before", "after"},
    "file_exists": {"path", "exists"},
    "llm": {"criteria", "focus"},
    "baseline": {"baseline_file", "criteria"},
}
REQUIRED_KEY = {
    "regex": "pattern",
    "tool_used": "tool",
    "tool_order": "before",
    "file_exists": "path",
    "llm": "criteria",
    "baseline": "criteria",
}


def cases() -> dict[str, dict[str, Any]]:
    return {path.parent.name: load_case(path) for path in eval_case_files()}


class EvalSuiteTests(unittest.TestCase):
    def test_suites_exist(self) -> None:
        self.assertGreaterEqual(len(cases()), 1)

    def test_each_case_is_one_file(self) -> None:
        for case_dir in sorted(path for path in (ROOT / "plugins").glob("*/evals/*") if path.is_dir()):
            if case_dir.name == "results":
                continue
            with self.subTest(case=case_dir.name):
                self.assertEqual(sorted(path.name for path in case_dir.iterdir()), ["case.yaml"])

    def test_every_case_is_loadable(self) -> None:
        for directory, case in cases().items():
            with self.subTest(case=directory):
                self.assertEqual(set(case) - CASE_KEYS, set(), "unknown case keys")
                self.assertEqual(case.get("schema_version"), "1.1")
                self.assertTrue(case.get("name"), "a case needs a name")
                execution = case.get("execution", {})
                self.assertEqual(set(execution) - EXECUTION_KEYS, set(), "unknown execution keys")
                self.assertTrue(str(execution.get("prompt", "")).strip(), "a case needs a prompt")
                graders = case.get("graders") or []
                self.assertTrue(graders, "at least one grader is required")
                names = [grader.get("name") for grader in graders]
                self.assertEqual(len(names), len(set(names)), "grader names must be unique")
                for grader in graders:
                    kind = grader.get("type")
                    self.assertIn(kind, GRADER_KEYS, grader.get("name"))
                    unknown = set(grader) - GRADER_COMMON_KEYS - GRADER_KEYS[kind]
                    self.assertEqual(unknown, set(), f"{grader['name']}: the runner rejects these keys")
                    self.assertTrue(grader.get(REQUIRED_KEY[kind]), f"{grader['name']}: missing {REQUIRED_KEY[kind]}")
                    if kind == "regex":
                        re.compile(grader["pattern"])
                        self.assertIn(str(grader.get("match", "contains")).split(":")[0], {"contains", "not_contains", "count"})

    def test_fail_closed_cases_cover_the_suite(self) -> None:
        self.assertTrue(any("fail-closed" in case.get("tags", []) for case in cases().values()))


def regex_graders(case: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {grader["name"]: grader for grader in case["graders"] if grader["type"] == "regex"}


def passes(grader: dict[str, Any], reply: str) -> bool:
    flags = re.IGNORECASE if "i" in grader.get("flags", "") else 0
    found = re.search(grader["pattern"], reply, flags) is not None
    match = grader.get("match", "contains")
    if match == "contains":
        return found
    if match == "not_contains":
        return not found
    raise NotImplementedError(f"no offline grading for match: {match}")


class GraderSampleTests(unittest.TestCase):
    def regex_cases(self) -> dict[str, dict[str, Any]]:
        return {name: case for name, case in cases().items() if regex_graders(case)}

    def test_every_sample_folder_names_a_regex_case(self) -> None:
        cases = self.regex_cases()
        for folder in sorted(p for p in SAMPLES.iterdir() if p.is_dir()):
            with self.subTest(samples=folder.name):
                self.assertIn(folder.name, cases, "no eval case with regex graders by this name")
                for sample in folder.glob("*.md"):
                    self.assertTrue(sample.name.startswith(("pass", "fail")), sample.name)

    def test_regex_graders_pass_good_replies_and_fail_bad_ones(self) -> None:
        for name, case in self.regex_cases().items():
            with self.subTest(case=name):
                graders = regex_graders(case)
                folder = SAMPLES / name
                good = sorted(folder.glob("pass*.md"))
                bad = sorted(folder.glob("fail*.md"))
                self.assertTrue(good, f"tests/eval_samples/{name}/ needs a pass*.md sample")
                self.assertTrue(bad, f"tests/eval_samples/{name}/ needs a fail*.md sample")
                for sample in good:
                    reply = sample.read_text(encoding="utf-8")
                    failed = [stem for stem, grader in graders.items() if not passes(grader, reply)]
                    self.assertEqual(failed, [], f"{sample.name} should pass every regex grader")
                tripped: set[str] = set()
                for sample in bad:
                    reply = sample.read_text(encoding="utf-8")
                    failed = {stem for stem, grader in graders.items() if not passes(grader, reply)}
                    self.assertTrue(failed, f"{sample.name} passed every regex grader")
                    tripped |= failed
                self.assertEqual(sorted(set(graders) - tripped), [], "graders no fail sample trips")


if __name__ == "__main__":
    unittest.main()
