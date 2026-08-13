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
SCRIPT = (
    ROOT / "plugins" / "australian-privacy-cybersecurity" / "skills"
    / "check-australian-privacy-principles" / "scripts" / "compare_app_inventory.py"
)
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
