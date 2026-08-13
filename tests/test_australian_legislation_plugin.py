from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-legislation"


class AustralianLegislationPluginTests(unittest.TestCase):
    def test_unified_plugin_contains_every_jurisdiction_checker(self) -> None:
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
        }
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, expected)

    def test_superseded_plugin_directories_are_absent(self) -> None:
        for name in (
            "commonwealth-legislation",
            "nsw-legislation",
            "state-territory-legislation",
        ):
            self.assertFalse((ROOT / "plugins" / name).exists())

    def test_new_checkers_fail_closed_and_exclude_case_law(self) -> None:
        new_checkers = (
            "check-victoria-legislation",
            "check-queensland-legislation",
            "check-western-australia-legislation",
            "check-south-australia-legislation",
            "check-tasmania-legislation",
            "check-act-legislation",
            "check-northern-territory-legislation",
        )
        for name in new_checkers:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = " ".join(path.read_text(encoding="utf-8").split())
            self.assertIn("NOT VERIFIED", text, path)
            self.assertIn("Case law is outside scope", text, path)
            self.assertIn("official", text, path)


if __name__ == "__main__":
    unittest.main()
