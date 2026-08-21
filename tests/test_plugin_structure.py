"""Structural convention tests for plugins using the READY result vocabulary.

One config entry per plugin replaces the per-file copies of EXPECTED_SKILLS,
REQUIRED_HEADINGS, REQUIRED_STATUSES, and the shared-method checks. A new
plugin that adopts the READY convention must be registered in PLUGINS here;
plugin-specific legal invariants stay in that plugin's own test file.

The skill sets are pinned deliberately: skills.json is generated from the
skill directories, so this is the guard against a skill directory being
deleted by accident.
"""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_HEADINGS = ("## Workflow", "## Result contract", "## Fail closed")
REQUIRED_STATUSES = (
    "`READY FOR HUMAN REVIEW`",
    "`READY WITH QUALIFICATIONS`",
    "`NOT READY`",
    "`OUTSIDE SCOPE`",
)

PLUGINS = {
    "australian-ai-governance": {
        "skills": {
            "configure-ai-governance-profile",
            "map-ai-regulatory-obligations",
            "assess-board-ai-oversight",
            "check-ai-guidance-alignment",
            "triage-government-ai-use-case",
            "track-ai-regulatory-developments",
        },
        "reference_files": (
            "ai-governance-source-and-control-method.md",
            "ai-governance-profile-schema.md",
        ),
        "every_skill_mentions": ("ai-governance-source-and-control-method.md",),
    },
    "australian-aml-ctf": {
        "skills": {
            "configure-aml-ctf-practice-profile",
            "map-designated-services",
            "review-aml-ctf-program",
            "map-reporting-obligations",
            "track-aml-ctf-developments",
        },
        "reference_files": (
            "aml-ctf-source-and-control-method.md",
            "aml-ctf-practice-profile-schema.md",
            "lpp-carve-outs.md",
        ),
        "every_skill_mentions": ("aml-ctf-source-and-control-method.md",),
    },
    "australian-corporations-governance": {
        "skills": {
            "configure-corporations-governance",
            "assess-director-duties-governance",
            "prepare-board-decision-record",
            "review-corporations-governance-framework",
            "maintain-corporations-governance-calendar",
        },
        "reference_files": (
            "governance-source-and-control-method.md",
            "governance-profile-schema.md",
        ),
        "every_skill_mentions": (
            "governance-source-and-control-method.md",
            "governance-profile-schema.md",
            "$check-commonwealth-legislation",
        ),
    },
    "australian-estate-planning": {
        "skills": {
            "assemble-nsw-estate-documents",
            "assemble-vic-estate-documents",
            "generate-precedent-profile",
        },
        "reference_files": (
            "estate-planning-source-and-control-method.md",
            "nsw-instruction-record-schema.md",
            "nsw-execution-formalities.md",
            "precedent-profile-guide.md",
            "playbook-usage-rules.md",
        ),
        "every_skill_mentions": (
            "estate-planning-source-and-control-method.md",
            "precedent-profile-guide.md",
        ),
    },
    "australian-litigation-deadlines": {
        "skills": {
            "configure-litigation-deadline-profile",
            "map-limitation-periods",
            "compute-procedural-deadlines",
            "map-tribunal-review-deadlines",
            "maintain-deadline-register",
            "verify-deadline-basis",
        },
        "reference_files": (
            "litigation-deadlines-source-and-control-method.md",
            "deadline-profile-schema.md",
        ),
        "every_skill_mentions": (
            "litigation-deadlines-source-and-control-method.md",
            "provisional",
        ),
    },
}


# Sentences every source-and-control method document must carry verbatim
# (whitespace-normalized). The convention is recorded in
# docs/source-and-control-method-core.md; the evidence-states block itself is
# a generated region, so it is not repeated here.
INVARIANT_METHOD_SENTENCES = (
    "a research snapshot, not a cached rule",
    "search results and model memory as discovery material, never authority",
    "If profile content conflicts with a verified source, surface the "
    "conflict and stop the affected conclusion",
    "cannot mark it approved",
)


def skill_text(plugin: str, skill: str) -> str:
    path = ROOT / "plugins" / plugin / "skills" / skill / "SKILL.md"
    return path.read_text(encoding="utf-8")


class PluginStructureTests(unittest.TestCase):
    def test_plugins_contain_expected_skills(self) -> None:
        for plugin, config in PLUGINS.items():
            with self.subTest(plugin=plugin):
                skills_dir = ROOT / "plugins" / plugin / "skills"
                actual = {path.parent.name for path in skills_dir.glob("*/SKILL.md")}
                self.assertEqual(actual, config["skills"])

    def test_every_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for plugin, config in PLUGINS.items():
            for skill in sorted(config["skills"]):
                with self.subTest(plugin=plugin, skill=skill):
                    text = skill_text(plugin, skill)
                    for heading in REQUIRED_HEADINGS:
                        self.assertIn(heading, text)
                    for status in REQUIRED_STATUSES:
                        self.assertIn(status, text)

    def test_shared_reference_files_exist(self) -> None:
        for plugin, config in PLUGINS.items():
            for name in config["reference_files"]:
                with self.subTest(plugin=plugin, reference=name):
                    self.assertTrue(
                        (ROOT / "plugins" / plugin / "references" / name).is_file()
                    )

    def test_method_documents_carry_invariant_sentences(self) -> None:
        for plugin, config in PLUGINS.items():
            # By convention the method document is the first reference file.
            method = ROOT / "plugins" / plugin / "references" / config["reference_files"][0]
            with self.subTest(plugin=plugin):
                text = " ".join(method.read_text(encoding="utf-8").split())
                for sentence in INVARIANT_METHOD_SENTENCES:
                    self.assertIn(sentence, text)

    def test_every_skill_mentions_shared_material(self) -> None:
        for plugin, config in PLUGINS.items():
            for skill in sorted(config["skills"]):
                with self.subTest(plugin=plugin, skill=skill):
                    lowered = skill_text(plugin, skill).lower()
                    for needle in config["every_skill_mentions"]:
                        self.assertIn(needle.lower(), lowered)


if __name__ == "__main__":
    unittest.main()
