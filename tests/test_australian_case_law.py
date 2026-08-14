from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-case-law"

_spec = importlib.util.spec_from_file_location(
    "parse_citation",
    PLUGIN / "skills" / "route-case-citation" / "scripts" / "parse_citation.py",
)
parse_citation = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(parse_citation)


class AustralianCaseLawPluginTests(unittest.TestCase):
    EXPECTED_SKILLS = {
        "route-case-citation",
        "verify-hca-judgment",
        "verify-nsw-judgment",
        "verify-federal-judgment",
        "verify-case-quote",
    }

    VERIFICATION_SKILLS = (
        "verify-hca-judgment",
        "verify-nsw-judgment",
        "verify-federal-judgment",
        "verify-case-quote",
    )

    REQUIRED_HEADINGS = (
        "## Workflow",
        "## Result contract",
        "## Fail closed",
    )

    REQUIRED_STATUSES = (
        "`VERIFIED`",
        "`VERIFIED WITH QUALIFICATIONS`",
        "`UNVERIFIABLE`",
        "`NOT FOUND`",
        "`OUTSIDE SCOPE`",
    )

    REQUIRED_CONTRACT_FIELDS = (
        "Requested check:",
        "Jurisdiction:",
        "Official sources:",
        "Checked:",
        "Limitations and review:",
    )

    def test_plugin_contains_expected_skills(self) -> None:
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, self.EXPECTED_SKILLS)

    def test_every_verification_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for name in self.VERIFICATION_SKILLS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, path)
            for status in self.REQUIRED_STATUSES:
                self.assertIn(status, text, path)
            for field in self.REQUIRED_CONTRACT_FIELDS:
                self.assertIn(field, text, path)

    def test_verification_skills_reference_the_shared_method(self) -> None:
        reference = PLUGIN / "references" / "case-law-verification-method.md"
        self.assertTrue(reference.is_file())
        for name in self.EXPECTED_SKILLS:
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("case-law-verification-method.md", text, name)

    def test_verification_skills_distinguish_unverifiable_from_not_found(self) -> None:
        for name in self.VERIFICATION_SKILLS:
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("not evidence of fabrication", (PLUGIN / "references" / "case-law-verification-method.md").read_text(encoding="utf-8"))
            self.assertIn("`UNVERIFIABLE`, not `NOT FOUND`", text, name)

    def test_router_never_verifies(self) -> None:
        text = (PLUGIN / "skills" / "route-case-citation" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Routing itself never outputs `VERIFIED`", text)


class ParseCitationTests(unittest.TestCase):
    def test_neutral_hca_citation_routes_to_hca_skill(self) -> None:
        record = parse_citation.parse("[2023] HCA 12")
        self.assertEqual(record["citation_type"], "medium-neutral")
        self.assertEqual(record["year"], 2023)
        self.assertEqual(record["number"], 12)
        self.assertEqual(record["route"], "verify-hca-judgment")

    def test_neutral_nsw_citation_routes_to_nsw_skill(self) -> None:
        record = parse_citation.parse("Smith v Jones [2021] NSWCA 300")
        self.assertEqual(record["jurisdiction"], "New South Wales")
        self.assertEqual(record["route"], "verify-nsw-judgment")

    def test_neutral_fcfcoa_citation_routes_to_federal_skill(self) -> None:
        record = parse_citation.parse("[2022] FedCFamC1A 5")
        self.assertEqual(record["route"], "verify-federal-judgment")

    def test_unsupported_jurisdiction_is_recognised_without_route(self) -> None:
        record = parse_citation.parse("[2020] VSC 1")
        self.assertEqual(record["court"], "Supreme Court of Victoria")
        self.assertIsNone(record["route"])
        self.assertIn("not yet supported", record["note"])

    def test_unknown_court_identifier_has_no_route(self) -> None:
        record = parse_citation.parse("[2020] ZZZ 1")
        self.assertIsNone(record["route"])
        self.assertIn("unrecognised court identifier", record["note"])

    def test_reported_clr_citation_routes_with_resolution_note(self) -> None:
        record = parse_citation.parse("(1992) 175 CLR 1")
        self.assertEqual(record["citation_type"], "reported")
        self.assertEqual(record["series"], "Commonwealth Law Reports")
        self.assertEqual(record["route"], "verify-hca-judgment")
        self.assertIn("resolve to a medium-neutral citation", record["note"])

    def test_unrecognised_series_has_no_route(self) -> None:
        record = parse_citation.parse("(2001) 52 NSWCCR 100")
        self.assertEqual(record["citation_type"], "reported")
        self.assertIsNone(record["route"])

    def test_case_name_without_citation_is_unknown(self) -> None:
        record = parse_citation.parse("Smith v Jones")
        self.assertEqual(record["citation_type"], "unknown")
        self.assertIsNone(record["route"])


if __name__ == "__main__":
    unittest.main()
