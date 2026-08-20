from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-estate-planning"
SKILL = PLUGIN / "skills" / "assemble-nsw-estate-documents" / "SKILL.md"
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
    files = [SKILL, PLUGIN / "README.md", PLUGIN / "CONTEXT.md", PLUGIN / "catalog.json"]
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
        self.assertIn(banner, self.read(SKILL))
        self.assertIn(banner, self.read(REFERENCES / "estate-planning-source-and-control-method.md"))

    def test_no_precedent_fails_closed_with_no_generic_fallback(self) -> None:
        skill = self.read(SKILL)
        self.assertIn("`NOT READY`", skill)
        self.assertIn("never substitute a generic document", skill)
        method = self.read(REFERENCES / "estate-planning-source-and-control-method.md")
        self.assertIn("There is no generic fallback document", method)

    def test_marker_only_fill_rule_is_stated_everywhere_it_matters(self) -> None:
        for path in (
            SKILL,
            REFERENCES / "estate-planning-source-and-control-method.md",
            REFERENCES / "marker-syntax-guide.md",
        ):
            self.assertIn("{{field_name}}", self.read(path), path.name)
        guide = self.read(REFERENCES / "marker-syntax-guide.md")
        self.assertIn("no conditional, loop or block syntax", guide)
        self.assertIn("per-slot", guide)

    def test_change_manifest_reconciliation_fails_closed(self) -> None:
        method = self.read(REFERENCES / "estate-planning-source-and-control-method.md")
        self.assertIn("outside a marker site", method)
        self.assertIn("`NOT READY`", method)
        self.assertIn("change manifest", self.read(SKILL).lower())

    def test_extraction_gate_and_no_invented_values(self) -> None:
        skill = self.read(SKILL)
        self.assertIn("cannot be determined", skill)
        self.assertIn("provenance", skill.lower())
        self.assertIn("extraction gate", skill.lower())
        schema = self.read(REFERENCES / "instruction-record-schema.md")
        self.assertIn("Never fill a plausible value", schema)

    def test_schema_covers_all_three_document_types(self) -> None:
        schema = self.read(REFERENCES / "instruction-record-schema.md")
        for heading in (
            "## Will",
            "## Enduring power of attorney",
            "## Appointment of enduring guardian",
            "## Missing required fields",
        ):
            self.assertIn(heading, schema)

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
        text = self.read(REFERENCES / "nsw-execution-formalities.md")
        self.assertIn("never determine that a formality has been satisfied", text.lower())
        self.assertIn("never state that a formality has been satisfied", self.read(SKILL).lower())

    def test_playbook_rules_keep_facts_and_law_above_playbook(self) -> None:
        rules = self.read(REFERENCES / "playbook-usage-rules.md")
        self.assertIn("Silent means solicitor", rules)
        self.assertIn("Instructions beat playbook", rules)
        self.assertIn("Playbook never fills a factual field", rules)
        self.assertIn("Law beats playbook", rules)

    def test_excluded_matters_route_outside_scope(self) -> None:
        skill = self.read(SKILL)
        self.assertIn("`OUTSIDE SCOPE`", skill)
        for excluded in ("self-represented", "advance care directive", "superannuation"):
            self.assertIn(excluded, skill.lower())


if __name__ == "__main__":
    unittest.main()
