from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-legal-research"
SKILL = PLUGIN / "skills" / "format-aglc4-citations"

REFERENCE_FILES = (
    "general-rules.md",
    "domestic-sources.md",
    "secondary-sources.md",
    "international-materials.md",
    "foreign-domestic-sources.md",
    "citation-templates-and-audit.md",
    "source-map.md",
)

REQUIRED_HEADINGS = (
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
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for heading in REQUIRED_HEADINGS:
            self.assertIn(heading, text)

    def test_skill_links_every_reference_file(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        for name in REFERENCE_FILES:
            self.assertTrue((SKILL / "references" / name).is_file(), name)
            self.assertIn(f"references/{name}", text, name)

    def test_no_firm_specific_branding_remains(self) -> None:
        for path in [SKILL / "SKILL.md", PLUGIN / "README.md", *sorted((SKILL / "references").iterdir())]:
            text = path.read_text(encoding="utf-8")
            for marker in ("G+T", "Gilbert", "user-supplied"):
                self.assertNotIn(marker, text, f"{path.name} contains {marker!r}")

    def test_source_map_preserves_provenance_and_limits(self) -> None:
        text = (SKILL / "references" / "source-map.md").read_text(encoding="utf-8")
        self.assertIn("Melbourne University Law Review Association", text)
        self.assertIn("SHA-256", text)
        self.assertIn("## Missing appendices", text)
        self.assertIn("does not bundle or reproduce the publication", text)

    def test_skill_separates_formatting_from_verification(self) -> None:
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("never invent", text)
        self.assertIn(
            "Treat source verification and citation formatting as separate findings", text
        )


if __name__ == "__main__":
    unittest.main()
