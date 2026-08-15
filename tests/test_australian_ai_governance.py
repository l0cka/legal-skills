from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-ai-governance"


class AustralianAiGovernancePluginTests(unittest.TestCase):
    # Structural conventions are covered by test_plugin_structure.py; this
    # file keeps only the plugin's legal invariants.

    def test_pending_instruments_stay_watch_items(self) -> None:
        for name in ("map-ai-regulatory-obligations", "track-ai-regulatory-developments"):
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            lowered = text.lower()
            self.assertIn("watch item", lowered, name)
            self.assertIn("never", lowered, name)
            self.assertNotIn("standards for ai are in force", lowered, name)

    def test_depth_routes_to_sibling_plugins(self) -> None:
        map_text = (
            PLUGIN / "skills" / "map-ai-regulatory-obligations" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("$assess-ai-privacy-cybersecurity-use-case", map_text)
        self.assertIn("$assess-automated-decision-transparency", map_text)
        board_text = (
            PLUGIN / "skills" / "assess-board-ai-oversight" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("$assess-director-duties-governance", board_text)
        self.assertIn("$check-commonwealth-legislation", board_text)

    def test_government_registry_covers_all_jurisdictions(self) -> None:
        registry_path = (
            PLUGIN
            / "skills"
            / "triage-government-ai-use-case"
            / "references"
            / "government-ai-assurance-registry.json"
        )
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        jurisdictions = {entry["jurisdiction"] for entry in registry["jurisdictions"]}
        self.assertEqual(
            jurisdictions,
            {"Cth", "NSW", "Vic", "Qld", "WA", "SA", "Tas", "ACT", "NT"},
        )
        for entry in registry["jurisdictions"]:
            self.assertIn(
                entry["verification"],
                {"verified-2026-08-14", "verified-with-caveat", "lead-verify-before-use"},
                entry["jurisdiction"],
            )
            for instrument in entry["instruments"]:
                self.assertTrue(
                    instrument["official_source"].startswith("https://"),
                    entry["jurisdiction"],
                )

    def test_watch_register_items_name_primary_sources(self) -> None:
        register_path = (
            PLUGIN
            / "skills"
            / "track-ai-regulatory-developments"
            / "references"
            / "watch-register.json"
        )
        register = json.loads(register_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(register["watch_items"]), 5)
        for item in register["watch_items"]:
            self.assertTrue(item["primary_sources"], item["id"])
            self.assertIn("expected_trigger", item, item["id"])


if __name__ == "__main__":
    unittest.main()
