"""Focused controls for the legal-evidence-workflows plugin."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "legal-evidence-workflows"
SKILL = PLUGIN / "skills" / "build-evidence-chronology" / "SKILL.md"
HARVEY_GUIDE = ROOT / "docs" / "harvey" / "build-evidence-chronology.md"
EXPECTED_SKILLS = [
    "build-document-index",
    "build-evidence-chronology",
    "build-privilege-log",
    "map-evidence-inconsistencies",
]
REQUIRED_STATUSES = (
    "`READY FOR HUMAN REVIEW`",
    "`READY WITH QUALIFICATIONS`",
    "`NOT READY`",
    "`OUTSIDE SCOPE`",
)


def skill_text(name: str) -> str:
    path = PLUGIN / "skills" / name / "SKILL.md"
    return " ".join(path.read_text(encoding="utf-8").lower().split())


class LegalEvidenceWorkflowTests(unittest.TestCase):
    def test_plugin_exposes_the_four_evidence_skills(self) -> None:
        skill_dirs = sorted(path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir())
        self.assertEqual(skill_dirs, EXPECTED_SKILLS)

    def test_every_skill_shares_the_review_table_docx_and_status_conventions(self) -> None:
        for name in EXPECTED_SKILLS:
            text = skill_text(name)
            with self.subTest(skill=name):
                self.assertIn("native review-table or structured document-review", text)
                self.assertIn("do not replace an available native table with prose", text)
                self.assertIn("create a new `.docx` file", text)
                self.assertIn("`draft - human review required`", text)
                self.assertIn("repeat table headings across pages", text)
                self.assertIn("runtime cannot create a valid `.docx`", text)
                self.assertIn("do not substitute markdown, pdf, a spreadsheet or prose-only output", text)
                self.assertIn("## fail closed", text)
                for status in REQUIRED_STATUSES:
                    self.assertIn(status.lower(), text)
                for term in ("credibility", "weight", "admissibility", "merits"):
                    self.assertIn(term, text)

    def test_skill_requires_native_structured_review_when_available(self) -> None:
        text = skill_text("build-evidence-chronology")
        self.assertIn("each document or coherent file group as a source row", text)

    def test_skill_preserves_traceability_and_conflicts(self) -> None:
        text = skill_text("build-evidence-chronology")
        for phrase in (
            "preserve the source's exact date and time wording",
            "never invent one",
            "keep inconsistent accounts as separate entries",
            "never convert silence into evidence",
            "do not claim the chronology is complete",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_document_index_never_omits_or_judges(self) -> None:
        text = skill_text("build-document-index")
        for phrase in (
            "never omit a supplied file",
            "never describe what a document proves",
            "an id never changes",
            "never renumber the supplied scheme",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_privilege_log_leaves_every_claim_to_the_practitioner(self) -> None:
        text = skill_text("build-privilege-log")
        for phrase in (
            "never decide that a document is privileged",
            "never state a conclusion on dominant purpose",
            "never infer legal advice from a lawyer's name alone",
            "flag; never decide waiver",
            "record a basis as `candidate` only",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)

    def test_inconsistency_map_ranks_nothing(self) -> None:
        text = skill_text("map-evidence-inconsistencies")
        for phrase in (
            "never decide which account is correct",
            "record silence as silence",
            "rank sources",
            "never convert silence into evidence",
            "never merge divergent accounts into one agreed fact",
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
