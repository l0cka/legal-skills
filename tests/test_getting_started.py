"""Invariants for the four typed commands in the getting-started area."""

from __future__ import annotations

import re
import unittest

from layout import PLUGIN, area_skills

AREA = "getting-started"


def frontmatter(skill: str) -> str:
    text = (PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    return text.split("\n---\n", 1)[0]


def body(skill: str) -> str:
    return " ".join((PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8").split())


class GettingStartedTests(unittest.TestCase):
    def test_commands_start_only_when_typed(self) -> None:
        for skill in area_skills(AREA):
            with self.subTest(skill=skill):
                self.assertRegex(frontmatter(skill), r"(?m)^disable-model-invocation: true$")
                agent = (PLUGIN / "skills" / skill / "agents" / "openai.yaml").read_text(encoding="utf-8")
                self.assertRegex(agent, r"(?m)^policy:\n  allow_implicit_invocation: false$")

    def test_only_these_skills_are_typed_only(self) -> None:
        typed_only = {
            path.parent.name
            for path in (PLUGIN / "skills").glob("*/SKILL.md")
            if re.search(r"(?m)^disable-model-invocation: true$", frontmatter(path.parent.name))
        }
        self.assertEqual(typed_only, set(area_skills(AREA)))

    def test_setup_drafts_through_configure_skills_and_never_approves(self) -> None:
        text = body("setup")
        configure = {path.parent.name for path in (PLUGIN / "skills").glob("configure-*/SKILL.md")}
        for skill in sorted(configure):
            with self.subTest(skill=skill):
                self.assertIn(f"`${skill}`", text)
        for needle in ("Never approve a profile", "Write nothing before that confirmation", "Never overwrite"):
            self.assertIn(needle, text)

    def test_start_runs_the_router_one_approved_step_at_a_time(self) -> None:
        text = body("start")
        self.assertIn("`$route-legal-fact-pattern`", text)
        self.assertIn("Never run a step the user has not approved", text)
        self.assertIn("Never answer the legal question", text)

    def test_check_citations_routes_to_every_verifier_and_never_verifies_itself(self) -> None:
        text = body("check-citations")
        verifiers = {"route-case-citation", "verify-case-quote"} | {
            path.parent.name for path in (PLUGIN / "skills").glob("check-*-legislation/SKILL.md")
        }
        for skill in sorted(verifiers):
            with self.subTest(skill=skill):
                self.assertIn(f"`${skill}`", text)
        self.assertIn("only a verifier that inspected the official publisher may report `VERIFIED`", text)
        self.assertIn("Never sample", text)

    def test_help_lists_only_the_skill_map(self) -> None:
        self.assertIn("skill-map.md", body("help"))
        self.assertIn("never name a skill that is not in it", body("help"))


if __name__ == "__main__":
    unittest.main()
