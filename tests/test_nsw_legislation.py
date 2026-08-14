from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "plugins"
    / "australian-legal-research"
    / "skills"
    / "check-nsw-legislation"
    / "scripts"
    / "nsw_lookup.py"
)
SKILL = SCRIPT.parents[1] / "SKILL.md"
METHOD = SCRIPT.parents[1] / "references" / "nsw-legislation-method.md"

SPEC = importlib.util.spec_from_file_location("nsw_lookup", SCRIPT)
assert SPEC and SPEC.loader
NSW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(NSW)


class NswLookupTests(unittest.TestCase):
    def test_rejects_invalid_identifier_and_date(self) -> None:
        with self.assertRaises(NSW.LookupInputError):
            NSW.validate_identifier("Privacy Act 1988")
        with self.assertRaises(NSW.LookupInputError):
            NSW.validate_as_at("2024-02-30")

    def test_builds_current_official_urls(self) -> None:
        result = NSW.build_urls("ACT-1987-015", "inforce")
        self.assertEqual(result["identifier"], "act-1987-015")
        self.assertEqual(result["presentCollection"], "inforce")
        self.assertEqual(result["selectedVersionRouteCollection"], "inforce")
        self.assertEqual(result["selector"], "current")
        self.assertEqual(
            result["statusPage"],
            "https://legislation.nsw.gov.au/view/html/inforce/current/act-1987-015",
        )
        self.assertTrue(result["legislativeHistory"].endswith("/lh"))
        self.assertTrue(result["xml"].endswith("/xml"))

    def test_builds_historical_repealed_urls(self) -> None:
        result = NSW.build_urls("sl-2008-0179", "repealed", "2013-12-13")
        self.assertEqual(result["presentCollection"], "repealed")
        self.assertEqual(result["selectedVersionRouteCollection"], "inforce")
        self.assertEqual(
            result["currentTitlePage"],
            "https://legislation.nsw.gov.au/view/html/repealed/current/sl-2008-0179",
        )
        self.assertEqual(
            result["statusPage"],
            "https://legislation.nsw.gov.au/view/html/inforce/2013-12-13/sl-2008-0179",
        )
        for field in ("wholeHtml", "wholePdf", "legislativeHistory", "xml"):
            self.assertIn("/inforce/2013-12-13/sl-2008-0179", result[field])
        self.assertIn("does not prove the title operated", result["warning"])

    def test_skill_contains_critical_fail_closed_controls(self) -> None:
        text = " ".join(SKILL.read_text(encoding="utf-8").split())
        for phrase in (
            "OUTSIDE SCOPE",
            "NOT VERIFIED",
            "usually updated within 3 working days",
            "A Bill listed under \"See also\" is not an amendment",
            "HTML and PDF versions in the In force and Repealed collections",
            "environmental planning instrument map",
            "Do not cite a generated URL as a source used unless it resolved",
        ):
            self.assertIn(phrase, text)

    def test_method_preserves_authorisation_boundary(self) -> None:
        text = " ".join(METHOD.read_text(encoding="utf-8").split())
        for phrase in (
            "Bills",
            "as-made titles before 2000",
            "Maps associated with environmental planning instruments",
            "Documents adopted by reference",
        ):
            self.assertIn(phrase, text)

    def test_cli_rejects_malformed_input_without_network(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "urls",
                "not-an-id",
                "--collection",
                "inforce",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("identifier must look like", result.stderr)


if __name__ == "__main__":
    unittest.main()
