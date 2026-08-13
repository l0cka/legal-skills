from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-privacy-cybersecurity" / "skills"


class PrivacyCyberRegistryTests(unittest.TestCase):
    def test_state_breach_commencement_boundaries(self) -> None:
        path = PLUGIN / "route-australian-privacy-jurisdiction" / "references" / "state-territory-coverage.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        by_code = {item["code"]: item for item in data["jurisdictions"]}
        self.assertEqual(by_code["NSW"]["breach"]["commencement"], "2023-11-28")
        self.assertEqual(by_code["QLD"]["breach"]["commencement_local_government"], "2026-07-01")
        self.assertEqual(by_code["WA"]["general_privacy"]["commencement"], "2026-07-01")
        self.assertEqual(by_code["WA"]["breach"]["commencement"], "2027-01-01")
        self.assertEqual(by_code["VIC"]["breach"]["status"], "standards-based scheme")

    def test_health_and_surveillance_boundaries_are_explicit(self) -> None:
        health = (PLUGIN / "route-australian-privacy-jurisdiction" / "references" / "health-information-overlays.md").read_text(encoding="utf-8")
        surveillance = (PLUGIN / "route-australian-privacy-jurisdiction" / "references" / "surveillance-workplace-map.md").read_text(encoding="utf-8")
        self.assertIn("PPIP Part 6A does not apply solely because HRIP applies", health)
        self.assertIn("Workplace Surveillance Act 2005", surveillance)
        self.assertIn("Workplace Privacy Act 2011", surveillance)
        self.assertIn("remained a proposal", surveillance)

    def test_cyber_registry_has_current_transitions_and_clocks(self) -> None:
        path = PLUGIN / "map-australian-cyber-incident-obligations" / "references" / "cyber-regime-registry.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        by_id = {item["id"]: item for item in data["regimes"]}
        self.assertIn("12 hours", by_id["soci-part-2b"]["clock_prompt"])
        self.assertIn("72 hours", by_id["cyber-extortion-payment"]["clock_prompt"])
        self.assertIn("ceased 2025-04-04", by_id["telecommunications-soci"]["supersedes"])
        self.assertEqual(by_id["smart-device-security"]["commencement"], "2026-03-04")
        self.assertEqual(by_id["apra-cps-230"]["latest_checked_version"], "effective 2026-07-01")
        self.assertIn("two days", by_id["telco-dfv"]["clock_prompt"])
        self.assertIn("do not assume", by_id["asic-reportable-situations"]["trigger_prompt"])
        self.assertIn("do not label general ACSC reporting mandatory", by_id["acsc-general-assistance"]["trigger_prompt"])

    def test_cyber_workflow_blocks_common_overstatements(self) -> None:
        skill = (PLUGIN / "map-australian-cyber-incident-obligations" / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "A 30-day NDB assessment period is not a 30-day notification deadline",
            "limited-use provisions do not themselves create legal professional privilege",
            "do not fold CDR safeguards into the APPs",
            "A single reporting portal is not a single-report safe harbour",
        ):
            self.assertIn(phrase, " ".join(skill.split()))

    def test_tort_is_independent_and_future_decisions_are_date_gated(self) -> None:
        tort = (PLUGIN / "assess-statutory-privacy-tort" / "SKILL.md").read_text(encoding="utf-8")
        adm = (PLUGIN / "assess-automated-decision-transparency" / "references" / "automated-decision-method.md").read_text(encoding="utf-8")
        self.assertIn("independent from APP coverage", tort)
        self.assertIn("10 December 2026", adm)
        self.assertIn("arrangement, use or acquisition occurred earlier", adm)


if __name__ == "__main__":
    unittest.main()
