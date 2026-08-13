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
    ROOT
    / "plugins"
    / "australian-privacy-cybersecurity"
    / "skills"
    / "check-australian-privacy-principles"
    / "scripts"
    / "compare_app_inventory.py"
)

SPEC = importlib.util.spec_from_file_location("compare_app_inventory", SCRIPT)
assert SPEC and SPEC.loader
APP_COMPARE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(APP_COMPARE)


def inventory(compilation_id: str = "C2099C00001") -> dict:
    return {
        "title_id": "C2004A03712",
        "compilation_id": compilation_id,
        "as_at": "2099-01-01",
        "source_url": "https://www.legislation.gov.au/C2004A03712/2099-01-01",
        "coverage": {
            "schedule": "Schedule 1",
            "complete": True,
            "method": "Inspected the complete official Schedule 1 text",
        },
        "principles": [
            {
                "identifier": "Principle Alpha",
                "heading": "First synthetic principle",
                "clause_range": "A.1–A.3",
                "text": "Synthetic statutory text for testing only.",
            },
            {
                "identifier": "Principle Beta",
                "heading": "Second synthetic principle",
                "clause_range": "B.1–B.2",
                "text": "Different synthetic statutory text for testing only.",
            },
        ],
    }


class AppInventoryComparisonTests(unittest.TestCase):
    def test_new_compilation_with_same_full_text_is_verified(self) -> None:
        earlier = inventory()
        later = inventory("C2099C00002")
        later["as_at"] = "2099-07-01"
        result = APP_COMPARE.compare_inventories(earlier, later)
        self.assertEqual(result["status"], APP_COMPARE.VERIFIED)
        self.assertTrue(result["comparison"]["compilation_changed"])
        self.assertEqual(result["changes"]["modified"], [])

    def test_full_text_change_blocks_reliance(self) -> None:
        earlier = inventory()
        later = copy.deepcopy(earlier)
        later["compilation_id"] = "C2099C00002"
        later["principles"][0]["text"] += " Amended text."
        result = APP_COMPARE.compare_inventories(earlier, later)
        self.assertEqual(result["status"], APP_COMPARE.CHANGE_DETECTED)
        self.assertEqual(
            result["changes"]["modified"][0]["changed_fields"],
            ["text_sha256"],
        )

    def test_added_and_reordered_principles_are_detected_without_fixed_count(self) -> None:
        earlier = inventory()
        later = copy.deepcopy(earlier)
        later["principles"].reverse()
        later["principles"].append(
            {
                "identifier": "Principle Gamma",
                "heading": "New synthetic principle",
                "clause_range": "C.1",
                "text": "New synthetic statutory text for testing only.",
            }
        )
        result = APP_COMPARE.compare_inventories(earlier, later)
        self.assertEqual(result["status"], APP_COMPARE.CHANGE_DETECTED)
        self.assertEqual(
            [item["identifier"] for item in result["changes"]["added"]],
            ["Principle Gamma"],
        )
        self.assertTrue(result["changes"]["reordered"])

    def test_incomplete_or_non_official_inventory_fails_closed(self) -> None:
        incomplete = inventory()
        incomplete["coverage"]["complete"] = False
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.validate_inventory(incomplete)

        unofficial = inventory()
        unofficial["source_url"] = "https://www.oaic.gov.au/example"
        with self.assertRaises(APP_COMPARE.InventoryError):
            APP_COMPARE.validate_inventory(unofficial)

    def test_cli_emits_hashes_not_full_statutory_text(self) -> None:
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
        self.assertEqual(result.returncode, 0)
        self.assertIn("text_sha256", result.stdout)
        self.assertNotIn(source["principles"][0]["text"], result.stdout)


if __name__ == "__main__":
    unittest.main()
