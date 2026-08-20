from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-estate-planning"
NSW_SKILL = PLUGIN / "skills" / "assemble-nsw-estate-documents" / "SKILL.md"
VIC_SKILL = PLUGIN / "skills" / "assemble-vic-estate-documents" / "SKILL.md"
SKILLS = (NSW_SKILL, VIC_SKILL)
REFERENCES = PLUGIN / "references"

# The pack must stay deployable on any text-based agent platform, so no
# shipped file may name one (docs/adr/0001). Lowercase substrings.
FORBIDDEN_PLATFORM_NAMES = (
    "harvey",
    "chatgpt",
    "openai",
    "copilot",
    "gemini",
    "cowork",
    "claude",
)


def shipped_files() -> list[Path]:
    files = [*SKILLS, PLUGIN / "README.md", PLUGIN / "CONTEXT.md", PLUGIN / "catalog.json"]
    files.extend(sorted(REFERENCES.glob("*.md")))
    return files


class AustralianEstatePlanningPluginTests(unittest.TestCase):
    # Structural conventions are covered by test_plugin_structure.py; this
    # file keeps only the plugin's legal and design invariants.

    def read(self, path: Path) -> str:
        # Whitespace-normalized so asserted phrases survive line wrapping.
        return " ".join(path.read_text(encoding="utf-8").split())

    def test_no_platform_names_in_shipped_content(self) -> None:
        for path in shipped_files():
            lowered = self.read(path).lower()
            for name in FORBIDDEN_PLATFORM_NAMES:
                self.assertNotIn(name, lowered, f"{path.name} names a platform")

    def test_draft_banner_is_mandated(self) -> None:
        banner = "DRAFT — SOLICITOR REVIEW REQUIRED"
        for skill in SKILLS:
            self.assertIn(banner, self.read(skill))
        self.assertIn(banner, self.read(REFERENCES / "estate-planning-source-and-control-method.md"))

    def test_no_precedent_fails_closed_with_no_generic_fallback(self) -> None:
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("`NOT READY`", skill)
            self.assertIn("never substitute a generic document", skill)
        method = self.read(REFERENCES / "estate-planning-source-and-control-method.md")
        self.assertIn("There is no generic fallback document", method)

    def test_human_precedents_do_not_require_machine_markers(self) -> None:
        for path in (
            *SKILLS,
            REFERENCES / "estate-planning-source-and-control-method.md",
            REFERENCES / "precedent-profile-guide.md",
            PLUGIN / "README.md",
        ):
            text = self.read(path)
            self.assertNotIn("{{field_name}}", text, path.name)
            self.assertNotIn("{{clause_choice:", text, path.name)
        self.assertIn("does not need machine markers", self.read(
            REFERENCES / "precedent-profile-guide.md"
        ))

    def test_precedent_profile_contract_and_registration_gate(self) -> None:
        guide = self.read(REFERENCES / "precedent-profile-guide.md")
        for term in (
            "precedent identity",
            "site register",
            "field map",
            "clause-choice register",
            "structural_location",
            "before_text",
            "target_text",
            "after_text",
            "expected_occurrences",
            "confirmation record",
        ):
            self.assertIn(term, guide)
        self.assertIn("Do not edit the precedent", guide)
        self.assertIn("Stop. The profile is not usable", guide)
        self.assertIn("must not fill a document in the same unconfirmed step", guide)

    def test_clause_choices_use_confirmed_profile_sites(self) -> None:
        guide = self.read(REFERENCES / "precedent-profile-guide.md")
        self.assertIn("closed list of approved variants", guide)
        self.assertIn("verbatim clause text", guide)
        self.assertIn("responsible solicitor confirms", guide)

        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("unresolved clause site", skill)
            self.assertIn("`NOT READY`", skill)

        catalog = self.read(PLUGIN / "catalog.json")
        self.assertIn("sidecar", catalog.lower())
        self.assertNotIn("{{", catalog)

    def test_change_manifest_reconciliation_fails_closed(self) -> None:
        method = self.read(REFERENCES / "estate-planning-source-and-control-method.md")
        self.assertIn("any unregistered change", method)
        self.assertIn("`NOT READY`", method)
        for skill in SKILLS:
            self.assertIn("change manifest", self.read(skill).lower())

    def test_source_precedent_is_unchanged_and_drift_fails_closed(self) -> None:
        guide = self.read(REFERENCES / "precedent-profile-guide.md")
        self.assertIn("Never modify the registered source precedent", guide)
        self.assertIn("precedent drift", guide)
        for finding in ("mismatch", "missing anchor", "duplicate match", "changed target text"):
            self.assertIn(finding, guide)
        self.assertIn("require a newly confirmed profile", guide)
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("working copy", skill)
            self.assertIn("precedent drift", skill)
            self.assertIn("never guess an anchor", skill.lower())

    def test_extraction_gate_and_no_invented_values(self) -> None:
        for skill in SKILLS:
            text = self.read(skill)
            self.assertIn("cannot be determined", text)
            self.assertIn("provenance", text.lower())
            self.assertIn("extraction gate", text.lower())
        for schema in ("instruction-record-schema.md", "vic-instruction-record-schema.md"):
            self.assertIn("Never fill a plausible value", self.read(REFERENCES / schema))

    def test_schema_covers_all_three_document_types(self) -> None:
        schema = self.read(REFERENCES / "instruction-record-schema.md")
        for heading in (
            "## Will",
            "## Enduring power of attorney",
            "## Appointment of enduring guardian",
            "## Missing required fields",
        ):
            self.assertIn(heading, schema)

        vic_schema = self.read(REFERENCES / "vic-instruction-record-schema.md")
        for heading in (
            "## Will",
            "## Enduring power of attorney",
            "## Appointment of medical treatment decision maker",
            "## Missing required fields",
        ):
            self.assertIn(heading, vic_schema)

    def test_formalities_reference_is_dated_and_official_publisher_only(self) -> None:
        text = self.read(REFERENCES / "nsw-execution-formalities.md")
        self.assertIn("20 August 2026", text)
        for version_line in (
            "Current version for 14 July 2023 to date",
            "Current version for 2 March 2025 to date",
            "Current version for 27 March 2021 to date",
        ):
            self.assertIn(version_line, text)
        for host in re.findall(r"https?://([^/\s)]+)", text) + re.findall(
            r"\b([a-z0-9.-]+\.gov\.au)\b", text
        ):
            self.assertEqual(host, "legislation.nsw.gov.au")

    def test_formalities_never_declared_satisfied(self) -> None:
        for reference in ("nsw-execution-formalities.md", "vic-execution-formalities.md"):
            text = self.read(REFERENCES / reference)
            self.assertIn("never determine", text.lower())
            self.assertIn("formality has been satisfied", text.lower())
        for skill in SKILLS:
            self.assertIn("never state that a formality has been satisfied", self.read(skill).lower())

    def test_victorian_formalities_are_dated_and_official(self) -> None:
        text = self.read(REFERENCES / "vic-execution-formalities.md")
        self.assertIn("20 August 2026", text)
        for version in ("version 036", "version 007", "version 012"):
            self.assertIn(version, text)
        for host in re.findall(r"https?://([^/\s)]+)", text) + re.findall(
            r"\b([a-z0-9.-]+\.gov\.au)\b", text
        ):
            self.assertEqual(host.removeprefix("www."), "legislation.vic.gov.au")

    def test_playbook_rules_keep_facts_and_law_above_playbook(self) -> None:
        rules = self.read(REFERENCES / "playbook-usage-rules.md")
        self.assertIn("Silent means solicitor", rules)
        self.assertIn("Instructions beat playbook", rules)
        self.assertIn("Playbook never fills a factual field", rules)
        self.assertIn("Law beats playbook", rules)

    def test_playbook_clause_choice_contract_fails_closed(self) -> None:
        rules = self.read(REFERENCES / "playbook-usage-rules.md")
        self.assertIn("registered variant", rules)
        self.assertIn("responsible solicitor confirms", rules)
        self.assertIn("`NOT READY`", rules)

        method = self.read(REFERENCES / "estate-planning-source-and-control-method.md")
        self.assertIn("clause-choice register", method)
        self.assertIn("confirmed profile", method)

    def test_excluded_matters_route_outside_scope(self) -> None:
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("`OUTSIDE SCOPE`", skill)
            for excluded in ("self-represented", "advance care directive", "superannuation"):
                self.assertIn(excluded, skill.lower())


if __name__ == "__main__":
    unittest.main()
