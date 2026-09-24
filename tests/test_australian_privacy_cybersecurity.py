"""Tests for the australian-privacy-cybersecurity plugin.

One file per plugin: skill controls, then the shipped jurisdiction
registries, then the APP inventory comparison script.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-privacy-cybersecurity"
SKILLS = PLUGIN / "skills"


class AustralianPrivacyCybersecurityTests(unittest.TestCase):
    def test_issue_skill_has_authority_and_scope_controls(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "assess-australian-privacy-issues"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "$check-commonwealth-legislation",
            "$check-nsw-legislation",
            "$trace-commonwealth-legislative-change",
            "$check-australian-privacy-principles",
            "$route-australian-privacy-jurisdiction",
            "$assess-statutory-privacy-tort",
            "$assess-automated-decision-transparency",
            "$map-australian-cyber-incident-obligations",
            "APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED",
            "case law is outside scope",
            "PRIMARY TEXT CHECK REQUIRED",
            "PRELIMINARY LAW AND ISSUE MAP — HUMAN REVIEW REQUIRED",
        ):
            self.assertIn(phrase, normalized)

    def test_breach_skill_preserves_approval_and_deadline_controls(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "assess-australian-data-breach"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "Do not take containment action",
            "$check-australian-privacy-principles",
            "$map-australian-cyber-incident-obligations",
            "$assess-statutory-privacy-tort",
            "Do not equate detection, confirmation, containment",
            "Calculate a deadline only after verifying the trigger",
            "Reserve all notification and legal conclusions",
            "URGENT PRELIMINARY BREACH ASSESSMENT — HUMAN DECISION REQUIRED",
        ):
            self.assertIn(phrase, normalized)

    def test_harvey_influence_is_attributed_without_bundled_task_material(self) -> None:
        readme = (PLUGIN / "README.md").read_text(encoding="utf-8")
        readme = " ".join(readme.split())
        self.assertIn("MIT-licensed Harvey AI `harvey-labs`", readme)
        self.assertIn("No task facts, client artefacts or legal answers", readme)

    def test_ai_use_case_skill_has_suitability_and_approval_controls(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "assess-ai-privacy-cybersecurity-use-case"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "$check-commonwealth-legislation",
            "$check-nsw-legislation",
            "$check-australian-privacy-principles",
            "$route-australian-privacy-jurisdiction",
            "$assess-statutory-privacy-tort",
            "$assess-automated-decision-transparency",
            "PILOT ONLY",
            "NOT SUITABLE ON CURRENT INFORMATION",
            "Case law: Outside scope and not considered",
            "Do not approve, procure, deploy, connect, upload data to",
        ):
            self.assertIn(phrase, normalized)

    def test_app_verifier_does_not_assume_a_fixed_framework(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "check-australian-privacy-principles"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "Never assume that the text, application perimeter, instruments",
            "$check-commonwealth-legislation",
            "$trace-commonwealth-legislative-change",
            "INVENTORY SCHEMA VALID",
            "GUIDANCE REFRESH REQUIRED",
            "APP FRAMEWORK NOT VERIFIED – DO NOT RELY",
        ):
            self.assertIn(phrase, normalized)


# --- Jurisdiction registries ----------------------------------------------


class PrivacyCyberRegistryTests(unittest.TestCase):
    def test_state_breach_commencement_boundaries(self) -> None:
        path = SKILLS / "route-australian-privacy-jurisdiction" / "references" / "state-territory-coverage.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        by_code = {item["code"]: item for item in data["jurisdictions"]}
        self.assertEqual(by_code["NSW"]["breach"]["commencement"], "2023-11-28")
        self.assertEqual(by_code["QLD"]["breach"]["commencement_local_government"], "2026-07-01")
        self.assertEqual(by_code["WA"]["general_privacy"]["commencement"], "2026-07-01")
        self.assertEqual(by_code["WA"]["breach"]["commencement"], "2027-01-01")
        self.assertEqual(by_code["VIC"]["breach"]["status"], "standards-based scheme")

    def test_health_and_surveillance_boundaries_are_explicit(self) -> None:
        health = (SKILLS / "route-australian-privacy-jurisdiction" / "references" / "health-information-overlays.md").read_text(encoding="utf-8")
        surveillance = (SKILLS / "route-australian-privacy-jurisdiction" / "references" / "surveillance-workplace-map.md").read_text(encoding="utf-8")
        self.assertIn("PPIP Part 6A does not apply solely because HRIP applies", health)
        self.assertIn("Workplace Surveillance Act 2005", surveillance)
        self.assertIn("Workplace Privacy Act 2011", surveillance)
        self.assertIn("remained a proposal", surveillance)

    def test_cyber_registry_has_current_transitions_and_clocks(self) -> None:
        path = SKILLS / "map-australian-cyber-incident-obligations" / "references" / "cyber-regime-registry.json"
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
        skill = (SKILLS / "map-australian-cyber-incident-obligations" / "SKILL.md").read_text(encoding="utf-8")
        for phrase in (
            "A 30-day NDB assessment period is not a 30-day notification deadline",
            "limited-use provisions do not themselves create legal professional privilege",
            "do not fold CDR safeguards into the APPs",
            "A single reporting portal is not a single-report safe harbour",
        ):
            self.assertIn(phrase, " ".join(skill.split()))

    def test_tort_is_independent_and_future_decisions_are_date_gated(self) -> None:
        tort = (SKILLS / "assess-statutory-privacy-tort" / "SKILL.md").read_text(encoding="utf-8")
        adm = (SKILLS / "assess-automated-decision-transparency" / "references" / "automated-decision-method.md").read_text(encoding="utf-8")
        self.assertIn("independent from APP coverage", tort)
        self.assertIn("10 December 2026", adm)
        self.assertIn("arrangement, use or acquisition occurred earlier", adm)


# --- APP inventory comparison script ---------------------------------------

SCRIPT = SKILLS / "check-australian-privacy-principles" / "scripts" / "compare_app_inventory.py"
SPEC = importlib.util.spec_from_file_location("compare_app_inventory", SCRIPT)
assert SPEC and SPEC.loader
APP_COMPARE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(APP_COMPARE)


def digest(character: str) -> str:
    return character * 64


def inventory(
    compilation_id: str = "C2026C00001",
    as_at: str = "2026-02-01",
    effective_from: str = "2026-01-01",
) -> dict:
    url = f"https://www.legislation.gov.au/C2004A03712/{compilation_id}"
    return {
        "title_id": "C2004A03712",
        "compilation_id": compilation_id,
        "as_at": as_at,
        "source": {
            "canonical_url": url,
            "final_url": url,
            "retrieved_at": "2026-08-14T10:00:00+10:00",
            "raw_sha256": digest("a"),
            "effective_from": effective_from,
            "effective_to": None,
        },
        "coverage": {
            "schedule": "Schedule 1",
            "complete": True,
            "method": "Synthetic fixture; never legal verification",
        },
        "principles": [
            {"identifier": "Principle Alpha", "heading": "Alpha", "clause_range": "A.1", "text": "Synthetic alpha text."},
            {"identifier": "Principle Beta", "heading": "Beta", "clause_range": "B.1", "text": "Synthetic beta text."},
        ],
        "framework_layers": {
            "application_perimeter": {"sha256": digest("b"), "sources": ["synthetic perimeter fixture"]},
            "applicable_instruments": {"sha256": digest("c"), "sources": ["synthetic instruments fixture"]},
            "guidance": {"sha256": digest("d"), "sources": ["synthetic guidance fixture"]},
        },
    }


class AppInventoryComparisonTests(unittest.TestCase):
    def test_schema_validation_never_claims_framework_verified(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.json"
            path.write_text(json.dumps(inventory()), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "validate", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(result.returncode, 0)
        self.assertIn(APP_COMPARE.SCHEMA_VALID, result.stdout)
        self.assertNotIn("APP FRAMEWORK VERIFIED", result.stdout)

    def test_wrong_title_unrelated_url_and_date_mismatch_fail(self) -> None:
        wrong_title = inventory()
        wrong_title["title_id"] = "C2004A00000"
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.validate_inventory(wrong_title)

        unrelated = inventory()
        unrelated["source"]["canonical_url"] = "https://www.legislation.gov.au/C2004A00000/C2026C00001"
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.validate_inventory(unrelated)

        outside_period = inventory(as_at="2025-12-31")
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.validate_inventory(outside_period)

    def test_compilation_url_binding_fails_closed(self) -> None:
        source = inventory()
        source["source"]["canonical_url"] = "https://www.legislation.gov.au/C2004A03712/C2025C99999"
        source["source"]["final_url"] = source["source"]["canonical_url"]
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.validate_inventory(source)

    def test_unchanged_text_is_not_overstated_as_verified(self) -> None:
        earlier = inventory()
        later = inventory("C2026C00002", "2026-07-01", "2026-06-01")
        result = APP_COMPARE.compare_inventories(earlier, later)
        self.assertEqual(result["status"], APP_COMPARE.TEXT_UNCHANGED)
        self.assertNotEqual(result["status"], "APP FRAMEWORK VERIFIED")

    def test_text_and_application_layer_changes_block_reuse(self) -> None:
        earlier = inventory()
        text_change = inventory("C2026C00002", "2026-07-01", "2026-06-01")
        text_change["principles"][0]["text"] += " Changed."
        self.assertEqual(
            APP_COMPARE.compare_inventories(earlier, text_change)["status"],
            APP_COMPARE.CHANGE_DETECTED,
        )

        perimeter_change = inventory("C2026C00002", "2026-07-01", "2026-06-01")
        perimeter_change["framework_layers"]["application_perimeter"]["sha256"] = digest("e")
        result = APP_COMPARE.compare_inventories(earlier, perimeter_change)
        self.assertEqual(result["status"], APP_COMPARE.CHANGE_DETECTED)
        self.assertTrue(result["changes"]["framework_layers"]["application_perimeter"])

    def test_guidance_change_has_separate_refresh_status(self) -> None:
        earlier = inventory()
        later = inventory("C2026C00002", "2026-07-01", "2026-06-01")
        later["framework_layers"]["guidance"]["sha256"] = digest("f")
        result = APP_COMPARE.compare_inventories(earlier, later)
        self.assertEqual(result["status"], APP_COMPARE.TEXT_UNCHANGED)
        self.assertEqual(result["guidance_status"], APP_COMPARE.GUIDANCE_REFRESH)

    def test_horizon_crossing_automated_decision_change_is_detected(self) -> None:
        source = inventory(as_at="2026-08-14")
        before = APP_COMPARE.compare_inventories(source, copy.deepcopy(source), "2026-12-09")
        after = APP_COMPARE.compare_inventories(source, copy.deepcopy(source), "2026-12-10")
        self.assertEqual(before["known_future_amendments"], [])
        self.assertEqual(after["status"], APP_COMPARE.APPLICATION_REVIEW)
        self.assertEqual(after["known_future_amendments"][0]["source_title_id"], "C2024A00128")
        self.assertIn("arrangement", after["known_future_amendments"][0]["application"])

    def test_reverse_chronology_and_same_id_inconsistency_fail(self) -> None:
        later = inventory("C2026C00002", "2026-07-01", "2026-06-01")
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.compare_inventories(later, inventory())

        inconsistent = inventory()
        inconsistent["principles"][0]["text"] += " Inconsistent."
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.compare_inventories(inventory(), inconsistent)

    def test_cli_emits_hashes_not_statutory_text(self) -> None:
        source = inventory()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "validate", str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertIn("text_sha256", result.stdout)
        self.assertNotIn(source["principles"][0]["text"], result.stdout)


if __name__ == "__main__":
    unittest.main()
