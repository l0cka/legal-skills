from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CONTRACT_HEADINGS = ("## Workflow", "## Result contract", "## Fail closed")
READY = (
    "`READY FOR HUMAN REVIEW`",
    "`READY WITH QUALIFICATIONS`",
    "`NOT READY`",
    "`OUTSIDE SCOPE`",
)
DRAFT = (
    "`DRAFT READY FOR SOLICITOR REVIEW`",
    "`PARTIAL DRAFT – UNRESOLVED ISSUES`",
    "`BLOCKED – NO DRAFT PRODUCED`",
    "`OUTSIDE SCOPE`",
)

PLUGINS: dict[str, dict] = {
    "australian-ai-governance": {
        "skills": {
            "configure-ai-governance-profile",
            "map-ai-regulatory-obligations",
            "assess-board-ai-oversight",
            "check-ai-guidance-alignment",
            "triage-government-ai-use-case",
            "track-ai-regulatory-developments",
        },
        "statuses": READY,
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
        "statuses": READY,
        "reference_files": (
            "aml-ctf-source-and-control-method.md",
            "aml-ctf-practice-profile-schema.md",
            "lpp-carve-outs.md",
        ),
        "every_skill_mentions": ("aml-ctf-source-and-control-method.md",),
    },
    "australian-commercial-drafting": {
        "skills": {
            "configure-drafting-profile",
            "draft-nda",
            "draft-website-terms",
            "draft-privacy-policy",
            "draft-services-agreement",
            "review-draft-against-checklist",
        },
        "statuses": (),
        "reference_files": (
            "drafting-source-and-control-method.md",
            "drafting-profile-schema.md",
            "clause-bank.md",
            "unfair-contract-terms-checklist.md",
        ),
        "every_skill_mentions": ("drafting-source-and-control-method.md",),
    },
    "australian-consumer-competition": {
        "skills": {
            "configure-consumer-competition-profile",
            "assess-consumer-guarantees",
            "review-marketing-claims",
            "map-merger-notification",
            "assess-cartel-and-rpm-risk",
            "map-product-safety-obligations",
            "track-accc-developments",
        },
        "statuses": READY,
        "reference_files": (
            "consumer-competition-source-and-control-method.md",
            "consumer-competition-profile-schema.md",
            "official-source-register.md",
            "merger-pathways.md",
        ),
        "every_skill_mentions": (
            "consumer-competition-source-and-control-method.md",
            "official-source-register.md",
            "$check-commonwealth-legislation",
            "qualified lawyer",
            "2026-10-13",
        ),
    },
    "australian-contract-review": {
        "skills": {
            "configure-review-playbook",
            "triage-inbound-nda",
            "review-commercial-agreement",
            "check-unfair-contract-terms",
            "review-limitation-and-indemnity-regime",
            "build-negotiation-redline-memo",
            "track-contract-renewals",
        },
        "statuses": READY,
        "reference_files": (
            "review-source-and-control-method.md",
            "review-playbook-schema.md",
            "statutory-verification-leads.md",
            "state-liability-verification-route.md",
        ),
        "every_skill_mentions": ("review-source-and-control-method.md",),
    },
    "australian-corporations-governance": {
        "skills": {
            "configure-corporations-governance",
            "assess-director-duties-governance",
            "prepare-board-decision-record",
            "review-corporations-governance-framework",
            "maintain-corporations-governance-calendar",
        },
        "statuses": READY,
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
    "australian-employment-fair-work": {
        "skills": {
            "configure-employment-profile",
            "map-fair-work-obligations",
            "assess-termination-exposure",
            "review-workplace-policy",
            "track-fair-work-developments",
        },
        "statuses": READY,
        "reference_files": (
            "fair-work-source-and-control-method.md",
            "employment-profile-schema.md",
        ),
        "every_skill_mentions": ("fair-work-source-and-control-method.md",),
    },
    "australian-estate-planning": {
        "skills": {
            "assemble-nsw-estate-documents",
            "assemble-qld-estate-documents",
            "assemble-vic-estate-documents",
        },
        "statuses": DRAFT,
        "reference_files": (),
        "every_skill_mentions": (),
    },
    "australian-legal-research": {
        "skills": {
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
        },
        "statuses": (),
        "reference_files": ("point-in-time-method.md", "case-law-verification-method.md"),
        "every_skill_mentions": (),
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
        "statuses": READY,
        "reference_files": (
            "litigation-deadlines-source-and-control-method.md",
            "deadline-profile-schema.md",
        ),
        "every_skill_mentions": (
            "litigation-deadlines-source-and-control-method.md",
            "provisional",
        ),
    },
    "australian-privacy-cybersecurity": {
        "skills": {
            "assess-ai-privacy-cybersecurity-use-case",
            "assess-australian-data-breach",
            "assess-australian-privacy-issues",
            "assess-automated-decision-transparency",
            "assess-statutory-privacy-tort",
            "check-australian-privacy-principles",
            "map-australian-cyber-incident-obligations",
            "route-australian-privacy-jurisdiction",
        },
        "statuses": (),
        "reference_files": (),
        "every_skill_mentions": (),
    },
    "legal-evidence-workflows": {
        "skills": {
            "build-document-index",
            "build-evidence-chronology",
            "build-privilege-log",
            "map-evidence-inconsistencies",
        },
        "statuses": READY,
        "reference_files": (),
        "every_skill_mentions": (),
    },
    "legal-triage": {
        "skills": {"configure-legal-triage", "triage-legal-enquiry"},
        "statuses": (),
        "reference_files": (),
        "every_skill_mentions": (),
    },
    "legal-workflow-router": {
        "skills": {"route-legal-fact-pattern"},
        "statuses": READY,
        "reference_files": (),
        "every_skill_mentions": ("`not installed`", "Install first:"),
    },
}


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
    def test_every_plugin_is_registered(self) -> None:
        shipped = {path.parent.name for path in (ROOT / "plugins").glob("*/catalog.json")}
        self.assertEqual(shipped, set(PLUGINS))

    def test_plugins_contain_expected_skills(self) -> None:
        for plugin, config in PLUGINS.items():
            with self.subTest(plugin=plugin):
                skills_dir = ROOT / "plugins" / plugin / "skills"
                actual = {path.name for path in skills_dir.iterdir() if path.is_dir()}
                self.assertEqual(actual, config["skills"])

    def test_every_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for plugin, config in PLUGINS.items():
            if not config["statuses"]:
                continue
            for skill in sorted(config["skills"]):
                with self.subTest(plugin=plugin, skill=skill):
                    text = " ".join(skill_text(plugin, skill).split())
                    for expected in (*CONTRACT_HEADINGS, *config["statuses"]):
                        self.assertIn(expected, text)

    def test_shared_reference_files_exist(self) -> None:
        for plugin, config in PLUGINS.items():
            for name in config["reference_files"]:
                with self.subTest(plugin=plugin, reference=name):
                    self.assertTrue((ROOT / "plugins" / plugin / "references" / name).is_file())

    def test_method_documents_carry_invariant_sentences(self) -> None:
        for plugin, config in PLUGINS.items():
            references = [name for name in config["reference_files"] if "source-and-control-method" in name]
            if not references:
                continue
            method = ROOT / "plugins" / plugin / "references" / references[0]
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
