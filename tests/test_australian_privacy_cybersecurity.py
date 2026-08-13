from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-privacy-cybersecurity"


class AustralianPrivacyCybersecurityTests(unittest.TestCase):
    def test_issue_skill_has_authority_and_scope_controls(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "assess-australian-privacy-issues"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "$check-commonwealth-legislation",
            "$check-nsw-legislation",
            "$trace-commonwealth-legislative-change",
            "$check-australian-privacy-principles",
            "APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED",
            "case law is outside scope",
            "PRIMARY TEXT CHECK REQUIRED",
            "PRELIMINARY LAW AND ISSUE MAP — HUMAN REVIEW REQUIRED",
        ):
            self.assertIn(phrase, normalized)

    def test_breach_skill_preserves_approval_and_deadline_controls(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "assess-australian-data-breach"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "Do not take containment action",
            "$check-australian-privacy-principles",
            "Do not equate detection, confirmation, containment",
            "Calculate a deadline only after verifying the trigger",
            "Reserve all notification and legal conclusions",
            "URGENT PRELIMINARY BREACH ASSESSMENT — HUMAN DECISION REQUIRED",
        ):
            self.assertIn(phrase, normalized)

    def test_harvey_influence_is_attributed_without_bundled_task_material(self) -> None:
        readme = (PLUGIN / "README.md").read_text(encoding="utf-8")
        readme = " ".join(readme.split())
        self.assertIn("MIT-licensed Harvey AI `harvey-labs`", readme)
        self.assertIn("No task facts, client artefacts or legal answers", readme)

    def test_ai_use_case_skill_has_suitability_and_approval_controls(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "assess-ai-privacy-cybersecurity-use-case"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "$check-commonwealth-legislation",
            "$check-nsw-legislation",
            "$check-australian-privacy-principles",
            "PILOT ONLY",
            "NOT SUITABLE ON CURRENT INFORMATION",
            "Case law: Outside scope and not considered",
            "Do not approve, procure, deploy, connect, upload data to",
        ):
            self.assertIn(phrase, normalized)

    def test_app_verifier_does_not_assume_a_fixed_framework(self) -> None:
        text = (
            PLUGIN
            / "skills"
            / "check-australian-privacy-principles"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        normalized = " ".join(text.split())
        for phrase in (
            "Never assume that the number, numbering, heading or text",
            "$check-commonwealth-legislation",
            "$trace-commonwealth-legislative-change",
            "fingerprints normalized full text",
            "APP FRAMEWORK NOT VERIFIED – DO NOT RELY",
        ):
            self.assertIn(phrase, normalized)


if __name__ == "__main__":
    unittest.main()
