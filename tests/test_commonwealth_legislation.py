from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "plugins"
    / "australian-legislation"
    / "skills"
    / "check-commonwealth-legislation"
    / "scripts"
    / "frl_lookup.py"
)
SKILL = SCRIPT.parents[1] / "SKILL.md"

SPEC = importlib.util.spec_from_file_location("frl_lookup", SCRIPT)
assert SPEC and SPEC.loader
FRL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(FRL)


class FrlLookupTests(unittest.TestCase):
    def test_rejects_invalid_title_id_and_date(self) -> None:
        with self.assertRaises(FRL.LookupError):
            FRL.validate_title_id("Privacy Act 1988")
        with self.assertRaises(FRL.LookupError):
            FRL.validate_as_at("2024-02-30")

    def test_search_url_escapes_odata_quote(self) -> None:
        url = FRL.search_url("Director's Order", 5)
        self.assertIn("director%27%27s+order", url)
        self.assertIn("%24top=5", url)

    def test_version_match_is_fail_closed(self) -> None:
        versions = [
            {"registerId": "C2024C00001", "start": "2024-01-01T00:00:00"},
            {"registerId": "C2024C00002", "start": "2024-07-01T00:00:00"},
        ]
        selected = FRL.select_expanded_version(
            versions,
            {"registerId": "C2024C00001", "start": "2024-01-01T00:00:00"},
        )
        self.assertEqual(selected["registerId"], "C2024C00001")
        with self.assertRaises(FRL.LookupError):
            FRL.select_expanded_version(
                versions,
                {"registerId": "C9999C99999", "start": "2024-01-01T00:00:00"},
            )

    @patch.object(FRL, "api_get")
    def test_check_preserves_currency_flags_and_caveat(self, api_get) -> None:
        api_get.side_effect = [
            {
                "id": "C2004A01224",
                "name": "Legislation Act 2003",
                "status": "InForce",
                "hasCommencedUnincorporatedAmendments": True,
                "versions": [
                    {
                        "registerId": "C2019C00084",
                        "start": "2019-02-24T00:00:00",
                        "hasUnincorporatedAmendments": True,
                    }
                ],
            },
            {"registerId": "C2019C00084", "start": "2019-02-24T00:00:00"},
        ]
        result = FRL.check("C2004A01224", "2024-01-01")
        self.assertTrue(
            result["currencyFlags"][
                "currentTitleHasCommencedUnincorporatedAmendments"
            ]
        )
        self.assertIn("does not establish commencement", result["warning"])

    def test_skill_contains_critical_fail_closed_controls(self) -> None:
        text = SKILL.read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "OUTSIDE SCOPE",
            "NOT VERIFIED",
            "commenced but unincorporated amendments",
            "Do not equate an as-made effective date with commencement",
            "Call a PDF authorised only after confirming",
        ):
            self.assertIn(phrase, normalized)

    def test_cli_rejects_malformed_input_without_network(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "check", "not-an-id", "--as-at", "2024-01-01"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Title ID must look like", result.stderr)


if __name__ == "__main__":
    unittest.main()
