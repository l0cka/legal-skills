"""Tests for the australian-legal-research plugin.

One file per plugin: plugin-wide structure, then one section per skill
family (Commonwealth lookup, change tracing, NSW lookup, case law,
AGLC4 citation). Formerly six topic-named files from before the 2026
plugin merge.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-legal-research"


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- Plugin-wide structure -------------------------------------------------


class AustralianLegalResearchPluginTests(unittest.TestCase):
    def test_unified_plugin_contains_every_expected_skill(self) -> None:
        expected = {
            "check-commonwealth-legislation",
            "trace-commonwealth-legislative-change",
            "check-nsw-legislation",
            "check-victoria-legislation",
            "check-queensland-legislation",
            "check-western-australia-legislation",
            "check-south-australia-legislation",
            "check-tasmania-legislation",
            "check-act-legislation",
            "check-northern-territory-legislation",
            "route-case-citation",
            "verify-hca-judgment",
            "verify-nsw-judgment",
            "verify-federal-judgment",
            "verify-case-quote",
            "format-aglc4-citations",
        }
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, expected)

    JURISDICTION_CHECKERS = (
        "check-commonwealth-legislation",
        "check-nsw-legislation",
        "check-victoria-legislation",
        "check-queensland-legislation",
        "check-western-australia-legislation",
        "check-south-australia-legislation",
        "check-tasmania-legislation",
        "check-act-legislation",
        "check-northern-territory-legislation",
    )

    STATE_TERRITORY_CHECKERS = JURISDICTION_CHECKERS[2:]

    REQUIRED_HEADINGS = (
        "## Workflow",
        "## Result contract",
        "## Fail closed",
    )

    REQUIRED_STATUSES = (
        "`VERIFIED`",
        "`VERIFIED WITH QUALIFICATIONS`",
        "`NOT VERIFIED`",
        "`OUTSIDE SCOPE`",
    )

    REQUIRED_CONTRACT_FIELDS = (
        "Requested check:",
        "Jurisdiction:",
        "As at:",
        "Official title:",
        "Currency flags:",
        "Official sources:",
        "Checked:",
        "Limitations and review:",
    )

    def test_every_checker_has_workflow_contract_and_fail_closed(self) -> None:
        for name in self.JURISDICTION_CHECKERS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, path)
            for status in self.REQUIRED_STATUSES:
                self.assertIn(status, text, path)
            for field in self.REQUIRED_CONTRACT_FIELDS:
                self.assertIn(field, text, path)

    def test_state_territory_checkers_link_shared_method(self) -> None:
        shared = PLUGIN / "references" / "point-in-time-method.md"
        self.assertTrue(shared.is_file())
        for name in self.STATE_TERRITORY_CHECKERS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            self.assertIn("../../references/point-in-time-method.md", text, path)
            self.assertIn("Case law is outside scope", text, path)


# --- Commonwealth legislation lookup ---------------------------------------

FRL_SCRIPT = (
    PLUGIN / "skills" / "check-commonwealth-legislation" / "scripts" / "frl_lookup.py"
)
FRL_SKILL = FRL_SCRIPT.parents[1] / "SKILL.md"
FRL = load_script("frl_lookup", FRL_SCRIPT)


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
        text = FRL_SKILL.read_text(encoding="utf-8")
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
            [
                sys.executable,
                str(FRL_SCRIPT),
                "check",
                "not-an-id",
                "--as-at",
                "2024-01-01",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Title ID must look like", result.stderr)


# --- Commonwealth legislative change tracing -------------------------------

TRACE_SCRIPT = (
    PLUGIN
    / "skills"
    / "trace-commonwealth-legislative-change"
    / "scripts"
    / "frl_change_trace.py"
)
TRACE_SKILL = TRACE_SCRIPT.parents[1] / "SKILL.md"
TRACE_METHOD = TRACE_SCRIPT.parents[1] / "references" / "change-tracing-method.md"
TRACE = load_script("frl_change_trace", TRACE_SCRIPT)


def version(
    register_id: str,
    start: str,
    compilation: str,
    *,
    reasons: list[dict] | None = None,
    unincorporated: bool = False,
    retrospective_start: str | None = None,
) -> dict:
    return {
        "titleId": "C2004A03712",
        "registerId": register_id,
        "start": start,
        "end": None,
        "retrospectiveStart": retrospective_start or start,
        "retrospectiveEnd": None,
        "registeredAt": start,
        "compilationNumber": compilation,
        "status": "InForce",
        "hasUnincorporatedAmendments": unincorporated,
        "reasons": reasons or [],
    }


class CommonwealthChangeTraceTests(unittest.TestCase):
    def test_rejects_invalid_or_non_increasing_interval(self) -> None:
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_title_id("Privacy Act 1988")
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_interval("2024-02-30", "2024-06-01")
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_interval("2024-06-01", "2024-06-01")
        with self.assertRaises(TRACE.TraceError):
            TRACE.validate_interval("2024-06-02", "2024-06-01")

    def test_endpoint_match_is_fail_closed(self) -> None:
        versions = [version("C2024C00001", "2024-01-01T00:00:00", "1")]
        selected = TRACE.select_endpoint(
            versions,
            {"registerId": "C2024C00001", "start": "2024-01-01T00:00:00"},
        )
        self.assertEqual(selected["compilationNumber"], "1")
        with self.assertRaises(TRACE.TraceError):
            TRACE.select_endpoint(
                versions,
                {"registerId": "C9999C99999", "start": "2024-01-01T00:00:00"},
            )

    @patch.object(TRACE, "api_get")
    def test_trace_enumerates_every_transition_and_normalizes_reasons(self, api_get) -> None:
        first = version("C2024C00001", "2024-01-01T00:00:00", "1")
        middle = version(
            "C2024C00002",
            "2024-03-01T00:00:00",
            "2",
            reasons=[
                {
                    "affect": "Amend",
                    "affectedByTitle": {
                        "titleId": "C2024A00010",
                        "name": "Example Amendment Act 2024",
                        "seriesType": "Act",
                        "year": 2024,
                        "number": 10,
                        "provisions": "sch 1 (item 3)",
                    },
                }
            ],
        )
        last = version("C2024C00003", "2024-05-01T00:00:00", "3")
        api_get.side_effect = [
            {
                "id": "C2004A03712",
                "name": "Privacy Act 1988",
                "collection": "Act",
                "hasCommencedUnincorporatedAmendments": False,
                "versions": [last, first, middle],
            },
            {"registerId": first["registerId"], "start": first["start"]},
            {"registerId": last["registerId"], "start": last["start"]},
        ]

        result = TRACE.trace("C2004A03712", "2024-01-15", "2024-06-01")

        self.assertEqual(
            [item["registerId"] for item in result["transitions"]],
            ["C2024C00002", "C2024C00003"],
        )
        affecting = result["transitions"][0]["reasons"][0]["affectingTitle"]
        self.assertEqual(affecting["provisions"], "sch 1 (item 3)")
        self.assertEqual(
            affecting["officialUrl"],
            "https://www.legislation.gov.au/C2024A00010",
        )
        self.assertIn("navigation evidence", result["warnings"][1])

    @patch.object(TRACE, "api_get")
    def test_same_compilation_and_currency_flags_do_not_overclaim(self, api_get) -> None:
        only = version(
            "C2024C00001",
            "2024-01-01T00:00:00",
            "1",
            unincorporated=True,
            retrospective_start="2023-12-15T00:00:00",
        )
        api_get.side_effect = [
            {
                "id": "C2004A03712",
                "name": "Privacy Act 1988",
                "collection": "Act",
                "hasCommencedUnincorporatedAmendments": True,
                "versions": [only],
            },
            {"registerId": only["registerId"], "start": only["start"]},
            {"registerId": only["registerId"], "start": only["start"]},
        ]

        result = TRACE.trace("C2004A03712", "2024-01-15", "2024-02-01")

        self.assertTrue(result["sameCompilation"])
        self.assertEqual(result["transitions"], [])
        self.assertTrue(
            result["currencyFlags"]["currentTitleHasCommencedUnincorporatedAmendments"]
        )
        self.assertTrue(result["currencyFlags"]["retrospectiveFieldsDiffer"])
        self.assertIn("not that legal operation was unchanged", result["warnings"][0])

    def test_skill_and_method_preserve_critical_boundaries(self) -> None:
        skill = " ".join(TRACE_SKILL.read_text(encoding="utf-8").split())
        method = " ".join(TRACE_METHOD.read_text(encoding="utf-8").split())
        for phrase in (
            "INTERVENING CHANGES WITH NO NET CHANGE",
            "compilation reasons as navigation evidence",
            "Do not infer legal operation",
            "commenced but unincorporated amendment",
            "Never say that a compilation commenced",
            "Do not transfer that label to HTML, EPUB",
            "limit one trace to 10",
        ):
            self.assertIn(phrase, skill)
        for phrase in (
            "endpoint-only diff",
            "commencement separate from incorporation",
            "does not itself commence",
            "Do not call HTML, EPUB",
            "application, savings and transitional",
            "replacement compilations",
        ):
            self.assertIn(phrase, method)

    def test_cli_rejects_malformed_input_without_network(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(TRACE_SCRIPT),
                "trace",
                "not-an-id",
                "--from",
                "2024-01-01",
                "--to",
                "2024-06-01",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn("Title ID must look like", result.stderr)


# --- NSW legislation lookup ------------------------------------------------

NSW_SCRIPT = PLUGIN / "skills" / "check-nsw-legislation" / "scripts" / "nsw_lookup.py"
NSW_SKILL = NSW_SCRIPT.parents[1] / "SKILL.md"
NSW_METHOD = NSW_SCRIPT.parents[1] / "references" / "nsw-legislation-method.md"
NSW = load_script("nsw_lookup", NSW_SCRIPT)


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
        text = " ".join(NSW_SKILL.read_text(encoding="utf-8").split())
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
        text = " ".join(NSW_METHOD.read_text(encoding="utf-8").split())
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
                str(NSW_SCRIPT),
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


# --- Case law verification -------------------------------------------------

parse_citation = load_script(
    "parse_citation",
    PLUGIN / "skills" / "route-case-citation" / "scripts" / "parse_citation.py",
)


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
        self.assertLessEqual(self.EXPECTED_SKILLS, actual)

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
            self.assertIn(
                "not evidence of fabrication",
                (
                    PLUGIN / "references" / "case-law-verification-method.md"
                ).read_text(encoding="utf-8"),
            )
            self.assertIn("`UNVERIFIABLE`, not `NOT FOUND`", text, name)

    def test_router_never_verifies(self) -> None:
        text = (PLUGIN / "skills" / "route-case-citation" / "SKILL.md").read_text(
            encoding="utf-8"
        )
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


# --- AGLC4 citation formatting ---------------------------------------------

CITATION_SKILL = PLUGIN / "skills" / "format-aglc4-citations"

CITATION_REFERENCE_FILES = (
    "general-rules.md",
    "domestic-sources.md",
    "secondary-sources.md",
    "international-materials.md",
    "foreign-domestic-sources.md",
    "citation-templates-and-audit.md",
    "source-map.md",
)

CITATION_REQUIRED_HEADINGS = (
    "## Workflow",
    "## Output rules",
    "## When AGLC4 has no rule",
    "## Source boundary",
)


class AustralianLegalCitationPluginTests(unittest.TestCase):
    def test_plugin_contains_citation_skill(self) -> None:
        skills = {path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir()}
        self.assertIn("format-aglc4-citations", skills)

    def test_skill_has_required_headings(self) -> None:
        text = (CITATION_SKILL / "SKILL.md").read_text(encoding="utf-8")
        for heading in CITATION_REQUIRED_HEADINGS:
            self.assertIn(heading, text)

    def test_skill_links_every_reference_file(self) -> None:
        text = (CITATION_SKILL / "SKILL.md").read_text(encoding="utf-8")
        for name in CITATION_REFERENCE_FILES:
            self.assertTrue((CITATION_SKILL / "references" / name).is_file(), name)
            self.assertIn(f"references/{name}", text, name)

    def test_no_firm_specific_branding_remains(self) -> None:
        for path in [
            CITATION_SKILL / "SKILL.md",
            PLUGIN / "README.md",
            *sorted((CITATION_SKILL / "references").iterdir()),
        ]:
            text = path.read_text(encoding="utf-8")
            for marker in ("G+T", "Gilbert", "user-supplied"):
                self.assertNotIn(marker, text, f"{path.name} contains {marker!r}")

    def test_source_map_preserves_provenance_and_limits(self) -> None:
        text = (CITATION_SKILL / "references" / "source-map.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Melbourne University Law Review Association", text)
        self.assertIn("SHA-256", text)
        self.assertIn("## Missing appendices", text)
        self.assertIn("does not bundle or reproduce the publication", text)

    def test_skill_separates_formatting_from_verification(self) -> None:
        text = (CITATION_SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("never invent", text)
        self.assertIn(
            "Treat source verification and citation formatting as separate findings", text
        )


if __name__ == "__main__":
    unittest.main()
