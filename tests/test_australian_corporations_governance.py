from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-corporations-governance"


class AustralianCorporationsGovernancePluginTests(unittest.TestCase):
    # Structural conventions are covered by test_plugin_structure.py; this
    # file keeps only the plugin's legal invariants.

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
