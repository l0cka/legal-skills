"""Structural checks for the `claude plugin eval` suites under plugins/*/evals/.

The runner itself is early access, so CI cannot execute the cases. This test
keeps every case loadable: a prompt with a name, at least one grader, and
grader frontmatter the runner accepts (compilable regex, a tool name, or LLM
criteria).
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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


if __name__ == "__main__":
    unittest.main()
