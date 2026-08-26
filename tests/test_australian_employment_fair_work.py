"""Plugin-specific controls for australian-employment-fair-work."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-employment-fair-work"
REFERENCES = PLUGIN / "references"


def read(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


class FairWorkPluginTests(unittest.TestCase):
    def test_no_skill_computes_a_time_limit(self) -> None:
        termination = read(PLUGIN / "skills" / "assess-termination-exposure" / "SKILL.md").lower()
        self.assertIn("$compute-procedural-deadlines", termination)
        self.assertIn("never compute the date", termination)
        self.assertIn("21 days", termination)

    def test_conclusions_stay_with_the_lawyer(self) -> None:
        phrases = {
            "assess-termination-exposure": "never conclude that a dismissal was or would be unfair",
            "review-workplace-policy": "never certify compliance",
            "map-fair-work-obligations": "never conclude award or agreement coverage",
            "configure-employment-profile": "never characterise a worker",
            "track-fair-work-developments": "never describe a pending instrument",
        }
        for skill, phrase in phrases.items():
            with self.subTest(skill=skill):
                self.assertIn(phrase, read(PLUGIN / "skills" / skill / "SKILL.md").lower())

    def test_references_are_dated_with_evidence_states(self) -> None:
        for name in ("framework-layers.md", "termination-exposure.md", "policy-statutory-hooks.md"):
            text = read(REFERENCES / name)
            with self.subTest(reference=name):
                self.assertIn("26 August 2026", text)
                self.assertIn("`VERIFIED`", text)
                self.assertIn("$check-commonwealth-legislation", text)

    def test_figures_carry_effective_dates(self) -> None:
        text = read(REFERENCES / "framework-layers.md")
        self.assertIn("$190,100", text)
        self.assertIn("1 July 2026", text)
        self.assertIn("C2026C00355", text)

    def test_watch_register_items_name_primary_sources(self) -> None:
        register = json.loads(
            (PLUGIN / "skills" / "track-fair-work-developments" / "references" / "watch-register.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(register["as_at"], "2026-08-26")
        self.assertGreaterEqual(len(register["watch_items"]), 10)
        for item in register["watch_items"]:
            with self.subTest(item=item["id"]):
                for key in ("item", "status_at_snapshot", "expected_trigger"):
                    self.assertTrue(item[key])
                self.assertTrue(item["primary_sources"])
                for url in item["primary_sources"]:
                    self.assertTrue(url.startswith("https://"))


if __name__ == "__main__":
    unittest.main()
