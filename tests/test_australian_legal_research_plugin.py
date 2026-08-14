from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-legal-research"


class AustralianLegalResearchPluginTests(unittest.TestCase):
    def test_unified_plugin_contains_every_expected_skill(self) -> None:
        expected = {
            "check-commonwealth-legislation",
            "trace-commonwealth-legislative-change",
            "check-nsw-legislation",
            "check-victoria-legislation",
            "check-queensland-legislation",
            "check-western-australia-legislation",
            "check-south-australia-legislation",
            "check-tasmania-legislation",
            "check-act-legislation",
            "check-northern-territory-legislation",
            "route-case-citation",
            "verify-hca-judgment",
            "verify-nsw-judgment",
            "verify-federal-judgment",
            "verify-case-quote",
            "format-aglc4-citations",
        }
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, expected)

    def test_superseded_plugin_directories_are_absent(self) -> None:
        for name in (
            "commonwealth-legislation",
            "nsw-legislation",
            "state-territory-legislation",
            "australian-legislation",
            "australian-case-law",
            "australian-legal-citation",
        ):
            self.assertFalse((ROOT / "plugins" / name).exists())

    JURISDICTION_CHECKERS = (
        "check-commonwealth-legislation",
        "check-nsw-legislation",
        "check-victoria-legislation",
        "check-queensland-legislation",
        "check-western-australia-legislation",
        "check-south-australia-legislation",
        "check-tasmania-legislation",
        "check-act-legislation",
        "check-northern-territory-legislation",
    )

    STATE_TERRITORY_CHECKERS = JURISDICTION_CHECKERS[2:]

    REQUIRED_HEADINGS = (
        "## Workflow",
        "## Result contract",
        "## Fail closed",
    )

    REQUIRED_STATUSES = (
        "`VERIFIED`",
        "`VERIFIED WITH QUALIFICATIONS`",
        "`NOT VERIFIED`",
        "`OUTSIDE SCOPE`",
    )

    REQUIRED_CONTRACT_FIELDS = (
        "Requested check:",
        "Jurisdiction:",
        "As at:",
        "Official title:",
        "Currency flags:",
        "Official sources:",
        "Checked:",
        "Limitations and review:",
    )

    def test_every_checker_has_workflow_contract_and_fail_closed(self) -> None:
        for name in self.JURISDICTION_CHECKERS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, path)
            for status in self.REQUIRED_STATUSES:
                self.assertIn(status, text, path)
            for field in self.REQUIRED_CONTRACT_FIELDS:
                self.assertIn(field, text, path)

    def test_state_territory_checkers_link_shared_method(self) -> None:
        shared = PLUGIN / "references" / "point-in-time-method.md"
        self.assertTrue(shared.is_file())
        for name in self.STATE_TERRITORY_CHECKERS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            self.assertIn("../../references/point-in-time-method.md", text, path)
            self.assertIn("Case law is outside scope", text, path)


if __name__ == "__main__":
    unittest.main()
