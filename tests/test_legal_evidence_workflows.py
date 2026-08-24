"""Focused controls for the legal-evidence-workflows plugin."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "legal-evidence-workflows"
SKILL = PLUGIN / "skills" / "build-evidence-chronology" / "SKILL.md"
HARVEY_GUIDE = ROOT / "docs" / "harvey" / "build-evidence-chronology.md"


class LegalEvidenceWorkflowTests(unittest.TestCase):
    def test_skill_requires_native_structured_review_when_available(self) -> None:
        text = " ".join(SKILL.read_text(encoding="utf-8").lower().split())
        self.assertIn("native review-table or structured document-review", text)
        self.assertIn("do not replace an available native table with prose", text)
        self.assertIn("each document or coherent file group as a source row", text)

    def test_skill_preserves_traceability_and_conflicts(self) -> None:
        text = " ".join(SKILL.read_text(encoding="utf-8").lower().split())
        for phrase in (
            "preserve the source's exact date and time wording",
            "never invent one",
            "keep inconsistent accounts as separate entries",
            "never convert silence into evidence",
            "do not claim the chronology is complete",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_skill_reserves_legal_and_evidentiary_judgments(self) -> None:
        text = SKILL.read_text(encoding="utf-8").lower()
        for term in ("credibility", "weight", "admissibility", "legal effect", "merits"):
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_skill_requires_a_valid_docx_deliverable(self) -> None:
        text = " ".join(SKILL.read_text(encoding="utf-8").lower().split())
        for phrase in (
            "create a new `.docx` file",
            "`draft - human review required`",
            "repeat table headings across pages",
            "runtime cannot create a valid `.docx`",
            "do not substitute markdown, pdf, a spreadsheet or prose-only output",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_harvey_guide_maps_every_required_block(self) -> None:
        text = HARVEY_GUIDE.read_text(encoding="utf-8")
        for block in ("File Upload", "Review Table", "Prompt", "Response"):
            with self.subTest(block=block):
                self.assertIn(block, text)
        self.assertIn("sentence-level source citations", text)
        self.assertIn("one source row", text)
        self.assertIn("event-level chronology", text)
        self.assertIn("Word document creation", text)
        self.assertIn("generated `.docx`", text)


if __name__ == "__main__":
    unittest.main()
