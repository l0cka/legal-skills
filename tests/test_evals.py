"""Structural checks for the `claude plugin eval` suites under plugins/*/evals/.

The runner itself is early access, so CI cannot execute the cases. This test
keeps every case loadable: a prompt with a name, at least one grader, and
grader frontmatter the runner accepts (compilable regex, a tool name, or LLM
criteria).

Regex graders can run offline, so they also run here against the sample
replies in tests/eval_samples/<case>/. A pass*.md sample must pass every regex
grader in its case, a fail*.md sample must fail at least one, and every regex
grader must be the one some fail sample trips. That proves each grader can
fail.
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "tests" / "eval_samples"
GRADER_TYPES = {"regex", "tool_used", "tool_order", "file_exists", "llm", "baseline"}
REQUIRED_KEY = {
    "regex": "pattern",
    "tool_used": "tool",
    "tool_order": "before",
    "file_exists": "path",
    "llm": "criteria",
    "baseline": "criteria",
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise AssertionError(f"{path.relative_to(ROOT)}: missing frontmatter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            fields[key.strip()] = value.strip()
    return fields


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
        return value[1:-1]
    return value


class EvalSuiteTests(unittest.TestCase):
    def cases(self) -> list[Path]:
        return sorted(p.parent for p in ROOT.glob("plugins/*/evals/*/prompt.md"))

    def test_suites_exist(self) -> None:
        self.assertGreaterEqual(len(self.cases()), 1)

    def test_every_case_is_loadable(self) -> None:
        for case in self.cases():
            with self.subTest(case=str(case.relative_to(ROOT))):
                prompt = frontmatter(case / "prompt.md")
                self.assertTrue(prompt.get("name"), "prompt.md needs a name")
                graders = sorted((case / "graders").glob("*.md"))
                self.assertTrue(graders, "at least one grader is required")
                for grader in graders:
                    fields = frontmatter(grader)
                    kind = fields.get("type")
                    self.assertIn(kind, GRADER_TYPES, grader.name)
                    self.assertTrue(fields.get(REQUIRED_KEY[kind]), f"{grader.name}: missing {REQUIRED_KEY[kind]}")
                    if kind == "regex":
                        re.compile(unquote(fields["pattern"]))
                        self.assertIn(fields.get("match", "contains").split(":")[0], {"contains", "not_contains", "count"})

    def test_fail_closed_cases_cover_each_suite(self) -> None:
        # Every plugin that ships evals has at least one case tagged fail-closed.
        by_plugin: dict[str, bool] = {}
        for case in self.cases():
            plugin = case.parents[1].name
            tags = frontmatter(case / "prompt.md").get("tags", "")
            by_plugin[plugin] = by_plugin.get(plugin, False) or "fail-closed" in tags
        for plugin, covered in by_plugin.items():
            self.assertTrue(covered, f"{plugin}: no fail-closed eval case")


def regex_graders(case: Path) -> dict[str, dict[str, str]]:
    graders = {}
    for path in sorted((case / "graders").glob("*.md")):
        fields = frontmatter(path)
        if fields.get("type") == "regex":
            graders[path.stem] = fields
    return graders


def passes(grader: dict[str, str], reply: str) -> bool:
    flags = re.IGNORECASE if "i" in grader.get("flags", "") else 0
    found = re.search(unquote(grader["pattern"]), reply, flags) is not None
    match = grader.get("match", "contains")
    if match == "contains":
        return found
    if match == "not_contains":
        return not found
    raise NotImplementedError(f"no offline grading for match: {match}")


class GraderSampleTests(unittest.TestCase):
    def regex_cases(self) -> dict[str, Path]:
        cases = sorted(p.parent for p in ROOT.glob("plugins/*/evals/*/prompt.md"))
        return {case.name: case for case in cases if regex_graders(case)}

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
