from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-corporations-governance"


class AustralianCorporationsGovernancePluginTests(unittest.TestCase):
    EXPECTED_SKILLS = {
        "configure-corporations-governance",
        "assess-director-duties-governance",
        "prepare-board-decision-record",
        "review-corporations-governance-framework",
        "maintain-corporations-governance-calendar",
    }

    REQUIRED_HEADINGS = ("## Workflow", "## Result contract", "## Fail closed")
    REQUIRED_STATUSES = (
        "`READY FOR HUMAN REVIEW`",
        "`READY WITH QUALIFICATIONS`",
        "`NOT READY`",
        "`OUTSIDE SCOPE`",
    )

    def test_plugin_contains_expected_skills(self) -> None:
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, self.EXPECTED_SKILLS)

    def test_every_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for name in self.EXPECTED_SKILLS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, path)
            for status in self.REQUIRED_STATUSES:
                self.assertIn(status, text, path)

    def test_every_skill_uses_shared_controls(self) -> None:
        self.assertTrue((PLUGIN / "references" / "governance-source-and-control-method.md").is_file())
        self.assertTrue((PLUGIN / "references" / "governance-profile-schema.md").is_file())
        for name in self.EXPECTED_SKILLS:
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("governance-source-and-control-method.md", text, name)
            self.assertIn("governance-profile-schema.md", text, name)
            self.assertIn("$check-commonwealth-legislation", text, name)

    def test_board_record_skill_prohibits_invented_events_and_actions(self) -> None:
        text = (PLUGIN / "skills" / "prepare-board-decision-record" / "SKILL.md").read_text(encoding="utf-8")
        lowered = text.lower()
        for control in ("never invent attendance", "never\nbackdate", "draft – not approved"):
            self.assertIn(control, lowered)

    def test_calendar_prohibits_guessed_deadlines_and_filing(self) -> None:
        text = (PLUGIN / "skills" / "maintain-corporations-governance-calendar" / "SKILL.md").read_text(encoding="utf-8")
        lowered = text.lower()
        for control in ("cached deadline", "use\n`tbc`", "never rely on", "create a regulator filing"):
            self.assertIn(control, lowered)


if __name__ == "__main__":
    unittest.main()
