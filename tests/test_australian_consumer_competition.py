from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-consumer-competition"


class ConsumerCompetitionContractTests(unittest.TestCase):
    def test_each_skill_has_an_eval_and_lawyer_gate(self) -> None:
        prompts = [path.read_text() for path in (PLUGIN / "evals").glob("*/prompt.md")]
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                self.assertTrue(any(f"Use {path.parent.name}." in text for text in prompts))
                self.assertIn("qualified lawyer", path.read_text())

    def test_watch_register_has_controlled_states_and_official_sources(self) -> None:
        register = json.loads((PLUGIN / "skills/track-accc-developments/references/watch-register.json").read_text())
        self.assertEqual(register["as_at"], "2026-10-13")
        items = register["watch_items"]
        self.assertEqual(len({item["id"] for item in items}), len(items))
        for item in items:
            with self.subTest(item=item["id"]):
                self.assertTrue(item["status_at_snapshot"])
                self.assertTrue(item["expected_trigger"])
                self.assertTrue(item["primary_sources"])
                for source in item["primary_sources"]:
                    self.assertTrue(source.startswith(("https://www.legislation.gov.au/", "https://www.accc.gov.au/", "https://www.productsafety.gov.au/")))
        general = next(item for item in items if item["id"] == "general-safety")
        self.assertIn("UNCONFIRMED", general["status_at_snapshot"])
        future = next(item for item in items if item["id"] == "utpa-2026")
        self.assertIn("not yet in force", future["status_at_snapshot"])

    def test_dependencies_name_existing_skills_and_do_not_link_across_plugins(self) -> None:
        catalog = json.loads((PLUGIN / "catalog.json").read_text())
        self.assertEqual(set(catalog["handsOffTo"]), {"australian-commercial-drafting", "australian-employment-fair-work", "australian-privacy-cybersecurity"})
        for path in PLUGIN.rglob("*.md"):
            text = path.read_text()
            self.assertNotIn("../../../australian-", text)
            self.assertNotIn("../../../../australian-", text)


if __name__ == "__main__":
    unittest.main()
