from __future__ import annotations

import json
import unittest
from pathlib import Path

from layout import PLUGIN, area_eval_files, area_skill_files

ROOT = Path(__file__).resolve().parents[1]
AREA = "consumer-competition"
LINK_PATTERNS = (
    r'\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))',
    r'^\s{0,3}\[[^\]]+\]:\s*(?:<([^>]+)>|([^\s]+))',
    r'(?:href|src)\s*=\s*[\"\']([^\"\']+)[\"\']',
)
OFFICIAL_PREFIXES = (
    "https://www.legislation.gov.au/",
    "https://www.accc.gov.au/",
    "https://www.productsafety.gov.au/",
    "https://ministers.treasury.gov.au/",
)


class ConsumerCompetitionContractTests(unittest.TestCase):
    def test_each_skill_has_an_eval_and_lawyer_gate(self) -> None:
        prompts = [path.read_text() for path in area_eval_files(AREA, "prompt.md")]
        for path in area_skill_files(AREA):
            with self.subTest(skill=path.parent.name):
                self.assertTrue(any(f"Use {path.parent.name}." in text for text in prompts))
                self.assertIn("qualified lawyer", path.read_text())
        self.assertTrue(any("happy-path" in text for text in prompts))

    def test_watch_register_has_controlled_states_and_official_sources(self) -> None:
        register_path = PLUGIN / "skills/track-accc-developments/references/watch-register.json"
        register = json.loads(register_path.read_text())
        self.assertEqual(register["as_at"], "2026-10-13")
        items = register["watch_items"]
        self.assertEqual(len({item["id"] for item in items}), len(items))
        self.assertEqual(len({item["expected_trigger"] for item in items}), len(items))
        for item in items:
            with self.subTest(item=item["id"]):
                self.assertTrue(item["status_at_snapshot"])
                self.assertTrue(item["expected_trigger"])
                self.assertTrue(item["primary_sources"])
                for source in item["primary_sources"]:
                    self.assertTrue(source.startswith(OFFICIAL_PREFIXES))
        general = next(item for item in items if item["id"] == "general-safety")
        self.assertIn("compilation 167", general["status_at_snapshot"])
        self.assertTrue(any("treasury.gov.au" in source for source in general["primary_sources"]))
        forms = next(item for item in items if item["id"] == "merger-forms")
        self.assertIn("UNCONFIRMED", forms["status_at_snapshot"])
        self.assertIn("https://www.legislation.gov.au/F2025L01604/latest", forms["primary_sources"])
        future = next(item for item in items if item["id"] == "utpa-2026")
        self.assertIn("not yet in force", future["status_at_snapshot"])

    def test_hand_off_owners_exist(self) -> None:
        for owner in ("draft-website-terms", "configure-employment-profile", "assess-australian-privacy-issues"):
            with self.subTest(owner=owner):
                self.assertTrue((PLUGIN / "skills" / owner / "SKILL.md").is_file())
                self.assertTrue(any(f"`${owner}`" in path.read_text() for path in area_skill_files(AREA)))


if __name__ == "__main__":
    unittest.main()
