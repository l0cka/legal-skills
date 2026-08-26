from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-estate-planning"
NSW_SKILL = PLUGIN / "skills" / "assemble-nsw-estate-documents" / "SKILL.md"
VIC_SKILL = PLUGIN / "skills" / "assemble-vic-estate-documents" / "SKILL.md"
QLD_SKILL = PLUGIN / "skills" / "assemble-qld-estate-documents" / "SKILL.md"
SKILLS = (NSW_SKILL, VIC_SKILL, QLD_SKILL)
REFERENCES = PLUGIN / "references"
METHOD = REFERENCES / "estate-planning-source-and-control-method.md"
NSW_HARVEY_GUIDE = ROOT / "docs" / "harvey" / "prepare-nsw-estate-planning-drafts.md"
VIC_HARVEY_GUIDE = ROOT / "docs" / "harvey" / "prepare-victorian-estate-planning-drafts.md"
QLD_HARVEY_GUIDE = ROOT / "docs" / "harvey" / "prepare-queensland-estate-planning-drafts.md"
DEPLOYMENT_ADR = ROOT / "docs" / "adr" / "0003-private-deployment-estate-drafting.md"

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
    def read(self, path: Path) -> str:
        return " ".join(path.read_text(encoding="utf-8").split())

    def test_plugin_exposes_only_three_jurisdiction_skills(self) -> None:
        skill_dirs = sorted(
            path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir()
        )
        self.assertEqual(
            skill_dirs,
            [
                "assemble-nsw-estate-documents",
                "assemble-qld-estate-documents",
                "assemble-vic-estate-documents",
            ],
        )

    def test_skills_publish_the_simplified_result_contract(self) -> None:
        for path in SKILLS:
            skill = self.read(path)
            for heading in ("## Workflow", "## Result contract", "## Fail closed"):
                self.assertIn(heading, skill)
            for status in (
                "`DRAFT READY FOR SOLICITOR REVIEW`",
                "`PARTIAL DRAFT – UNRESOLVED ISSUES`",
                "`BLOCKED – NO DRAFT PRODUCED`",
                "`OUTSIDE SCOPE`",
            ):
                self.assertIn(status, skill)

    def test_each_skill_uses_one_client_and_the_approved_precedent_library(self) -> None:
        for path in SKILLS:
            skill = self.read(path).lower()
            self.assertIn("one client per run", skill)
            self.assertIn("approved precedent library", skill)
            self.assertIn("never accept an uploaded substitute precedent", skill)

    def test_instruction_table_drives_drafting_without_a_mid_run_pause(self) -> None:
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("instruction table", skill.lower())
            self.assertIn("provenance", skill.lower())
            self.assertNotIn("instruction confirmation gate", skill.lower())
            self.assertNotIn("Draft only after", skill)
            self.assertIn("review the drafts", skill)

    def test_partial_drafts_make_every_unresolved_issue_visible(self) -> None:
        for path in (*SKILLS, METHOD):
            text = self.read(path)
            for phrase in (
                "DRAFT – SOLICITOR REVIEW REQUIRED",
                "PARTIAL DRAFT – UNRESOLVED ISSUES IDENTIFIED",
                "[REVIEW REQUIRED – <missing fact or unresolved decision>]",
                "PARTIAL DRAFT – UNRESOLVED ISSUES",
                "drafting-issues register",
            ):
                self.assertIn(phrase, text)
        for path in SKILLS:
            self.assertIn("Every review marker must have a matching entry", self.read(path))

    def test_active_pack_has_no_profile_architecture(self) -> None:
        forbidden = (
            "sidecar",
            "precedent profile",
            "site register",
            "exact anchor",
            "precedent drift",
        )
        for path in shipped_files():
            text = self.read(path).lower()
            for phrase in forbidden:
                self.assertNotIn(phrase, text, f"{path.name} retains {phrase}")

    def test_no_platform_names_in_shipped_content(self) -> None:
        for path in shipped_files():
            lowered = self.read(path).lower()
            for name in FORBIDDEN_PLATFORM_NAMES:
                self.assertNotIn(name, lowered, f"{path.name} names a platform")

    def test_harvey_guides_use_supported_vault_configuration(self) -> None:
        expected = (
            (NSW_HARVEY_GUIDE, "Prepare NSW Estate Planning Drafts", "jurisdiction: NSW"),
            (
                VIC_HARVEY_GUIDE,
                "Prepare Victorian Estate Planning Drafts",
                "jurisdiction: VIC",
            ),
            (
                QLD_HARVEY_GUIDE,
                "Prepare Queensland Estate Planning Drafts",
                "jurisdiction: QLD",
            ),
        )
        for path, agent_name, jurisdiction in expected:
            guide = self.read(path)
            self.assertIn(agent_name, guide)
            self.assertIn(jurisdiction, guide)
            self.assertIn("one client", guide.lower())
            self.assertIn("embedded Vault", guide)
            self.assertIn("<ADD EXACT", guide)
            self.assertIn("Do not permit a user-uploaded precedent", guide)
            self.assertNotIn("Copy-paste build request", guide)
            self.assertNotIn("## Private configuration", guide)
            self.assertNotIn("```yaml", guide)
            self.assertNotIn("instruction confirmation", guide.lower())

        adr = self.read(DEPLOYMENT_ADR)
        self.assertIn("status: accepted", adr)
        self.assertIn("separate jurisdictional agents", adr)
        self.assertIn("embedded jurisdiction Vault", adr)
        self.assertNotIn("private configuration is the operational source of truth", adr)

    def test_no_approved_precedent_blocks_without_generic_fallback(self) -> None:
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("`BLOCKED – NO DRAFT PRODUCED`", skill)
            self.assertIn("never substitute a generic document", skill)
        method = self.read(METHOD)
        self.assertIn("There is no generic fallback document", method)
        self.assertIn("uploaded substitute must not be used", method)

    def test_source_precedent_remains_unchanged(self) -> None:
        for path in (*SKILLS, METHOD):
            text = self.read(path).lower()
            self.assertIn("working cop", text)
            self.assertIn("source unchanged", text)

    def test_clause_choices_remain_solicitor_controlled(self) -> None:
        method = self.read(METHOD)
        for phrase in (
            "approved playbook",
            "client's express instructions",
            "Never invent, combine or improve clause text",
        ):
            self.assertIn(phrase, method)
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("playbook-usage-rules.md", skill)
            self.assertIn("Never invent, combine or improve clause text", skill)

        rules = self.read(REFERENCES / "playbook-usage-rules.md")
        self.assertIn("standing drafting positions", rules)
        self.assertIn("Apply an approved playbook position", rules)
        self.assertIn("Never use the playbook to supply a client fact", rules)

    def test_approved_material_placeholders_are_deployment_fillable(self) -> None:
        method = self.read(METHOD)
        for placeholder in (
            "<NSW APPROVED LIBRARY NAME>",
            "<NSW WILL PRECEDENT FILE NAME>",
            "<NSW DRAFTING PLAYBOOK FILE NAME>",
            "<VICTORIAN APPROVED LIBRARY NAME>",
            "<VICTORIAN WILL PRECEDENT FILE NAME>",
            "<VICTORIAN DRAFTING PLAYBOOK FILE NAME>",
            "<QUEENSLAND APPROVED LIBRARY NAME>",
            "<QUEENSLAND WILL PRECEDENT FILE NAME>",
            "<QUEENSLAND DRAFTING PLAYBOOK FILE NAME>",
        ):
            self.assertIn(placeholder, method)
        self.assertNotIn("live verification", method.lower())

    def test_extraction_never_invents_values(self) -> None:
        for path in SKILLS:
            text = self.read(path)
            self.assertIn("cannot be determined", text)
            self.assertIn("Never infer a plausible value", text)
        for schema in (
            "nsw-instruction-record-schema.md",
            "vic-instruction-record-schema.md",
            "qld-instruction-record-schema.md",
        ):
            self.assertIn("Never fill a plausible value", self.read(REFERENCES / schema))

    def test_schemas_cover_document_types_and_risk_flags(self) -> None:
        schema = self.read(REFERENCES / "nsw-instruction-record-schema.md")
        for heading in (
            "## Scope and risk flags",
            "## Will",
            "## Enduring power of attorney",
            "## Appointment of enduring guardian",
            "## Missing required fields",
        ):
            self.assertIn(heading, schema)

        vic_schema = self.read(REFERENCES / "vic-instruction-record-schema.md")
        for heading in (
            "## Scope and risk flags",
            "## Will",
            "## Enduring power of attorney",
            "## Appointment of medical treatment decision maker",
            "## Missing required fields",
        ):
            self.assertIn(heading, vic_schema)

        qld_schema = self.read(REFERENCES / "qld-instruction-record-schema.md")
        for heading in (
            "## Scope and risk flags",
            "## Will",
            "## Enduring power of attorney",
            "## Missing required fields",
        ):
            self.assertIn(heading, qld_schema)

        for text in (schema, vic_schema, qld_schema):
            for flag in ("marriage", "divorce", "jointly held assets", "superannuation", "capacity"):
                self.assertIn(flag, text.lower())

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
        for reference in (
            "nsw-execution-formalities.md",
            "vic-execution-formalities.md",
            "qld-execution-formalities.md",
        ):
            text = self.read(REFERENCES / reference)
            self.assertIn("never determine", text.lower())
            self.assertIn("formality has been satisfied", text.lower())

    def test_victorian_formalities_are_dated_and_official(self) -> None:
        text = self.read(REFERENCES / "vic-execution-formalities.md")
        self.assertIn("20 August 2026", text)
        for version in ("version 036", "version 007", "version 012"):
            self.assertIn(version, text)
        for host in re.findall(r"https?://([^/\s)]+)", text) + re.findall(
            r"\b([a-z0-9.-]+\.gov\.au)\b", text
        ):
            self.assertEqual(host.removeprefix("www."), "legislation.vic.gov.au")

    def test_queensland_formalities_are_dated_and_official(self) -> None:
        text = self.read(REFERENCES / "qld-execution-formalities.md")
        self.assertIn("26 August 2026", text)
        self.assertIn("Current as at 28 April 2026", text)
        self.assertIn("Remote witnessing — none in force", text)
        allowed = {"legislation.qld.gov.au", "publications.qld.gov.au", "publicguardian.qld.gov.au"}
        for host in re.findall(r"https?://([^/\s)]+)", text) + re.findall(
            r"\b([a-z0-9.-]+\.gov\.au)\b", text
        ):
            self.assertIn(host.removeprefix("www."), allowed)

    def test_excluded_matters_route_outside_scope(self) -> None:
        for path in SKILLS:
            skill = self.read(path)
            self.assertIn("`OUTSIDE SCOPE`", skill)
            excluded_terms = ("self-represented", "superannuation")
            excluded_terms += ("advance health directive",) if path is QLD_SKILL else ("advance care directive",)
            for excluded in excluded_terms:
                self.assertIn(excluded, skill.lower())


if __name__ == "__main__":
    unittest.main()
