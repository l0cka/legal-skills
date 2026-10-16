from __future__ import annotations

import re
import unittest

from layout import AREAS as CATALOG_AREAS
from layout import PLUGIN, ROOT, area_skills

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

AREAS: dict[str, dict] = {
    "ai-governance": {
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
    "aml-ctf": {
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
    "cognitive-sparring": {
        "skills": {
            "clarify-burden-and-standard",
            "drill-oral-advocacy",
            "find-blind-spots",
            "map-assumptions",
            "oppose-as-counsel",
            "pressure-test-argument",
            "pressure-test-strategy",
            "red-team-evidence",
            "role-play-decision-maker",
            "simplify-without-losing-precision",
            "steelman-then-attack",
            "test-understanding",
        },
        "statuses": READY,
        "reference_files": ("sparring-contract.md",),
        "every_skill_mentions": (
            "jurisdiction is lawyer-supplied",
            "qualified lawyer",
            "cannot tell from the supplied record",
            "sparring-contract.md",
        ),
    },
    "commercial-drafting": {
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
    "consumer-competition": {
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
    "contract-review": {
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
    "corporations-governance": {
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
    "employment-fair-work": {
        "skills": {
            "configure-employment-profile",
            "map-fair-work-obligations",
            "assess-termination-exposure",
            "review-workplace-policy",
            "track-fair-work-developments",
            "review-employment-contract",
            "assess-employee-vs-contractor",
            "assess-discrimination-and-positive-duty",
            "assess-restraint-of-trade",
            "compute-underpayment-exposure-framework",
        },
        "statuses": READY,
        "reference_files": (
            "fair-work-source-and-control-method.md",
            "employment-profile-schema.md",
        ),
        "every_skill_mentions": ("fair-work-source-and-control-method.md",),
    },
    "estate-planning": {
        "skills": {
            "assemble-nsw-estate-documents",
            "assemble-qld-estate-documents",
            "assemble-vic-estate-documents",
        },
        "statuses": DRAFT,
        "reference_files": (),
        "every_skill_mentions": (),
    },
    "legal-research": {
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
    "litigation-deadlines": {
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
    "privacy-cybersecurity": {
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
    "evidence-workflows": {
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
    "triage": {
        "skills": {"configure-legal-triage", "triage-legal-enquiry"},
        "statuses": (),
        "reference_files": (),
        "every_skill_mentions": (),
    },
    "workflow-router": {
        "skills": {"route-legal-fact-pattern"},
        "statuses": READY,
        "reference_files": (),
        "every_skill_mentions": ("`cannot be determined`", "Gaps:"),
    },
}


INVARIANT_METHOD_SENTENCES = (
    "a research snapshot, not a cached rule",
    "search results and model memory as discovery material, never authority",
    "If profile content conflicts with a verified source, surface the "
    "conflict and stop the affected conclusion",
    "cannot mark it approved",
)


SKILL_REFERENCE = re.compile(r"`\$([a-z0-9]+(?:-[a-z0-9]+)*)`")


def skill_text(skill: str) -> str:
    return (PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")


class PluginStructureTests(unittest.TestCase):
    def test_every_area_is_registered(self) -> None:
        self.assertEqual(set(CATALOG_AREAS), set(AREAS))

    def test_areas_contain_expected_skills(self) -> None:
        for area, config in AREAS.items():
            with self.subTest(area=area):
                self.assertEqual(set(area_skills(area)), config["skills"])

    def test_every_skill_directory_belongs_to_an_area(self) -> None:
        shipped = {path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir()}
        pinned = set().union(*(config["skills"] for config in AREAS.values()))
        self.assertEqual(shipped, pinned)

    def test_named_skills_exist(self) -> None:
        for path in sorted(PLUGIN.rglob("*.md")):
            for name in SKILL_REFERENCE.findall(path.read_text(encoding="utf-8")):
                with self.subTest(document=str(path.relative_to(ROOT)), skill=name):
                    self.assertTrue((PLUGIN / "skills" / name / "SKILL.md").is_file())

    def test_every_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for area, config in AREAS.items():
            if not config["statuses"]:
                continue
            for skill in sorted(config["skills"]):
                with self.subTest(area=area, skill=skill):
                    text = " ".join(skill_text(skill).split())
                    for expected in (*CONTRACT_HEADINGS, *config["statuses"]):
                        self.assertIn(expected, text)

    def test_shared_reference_files_exist(self) -> None:
        for area, config in AREAS.items():
            for name in config["reference_files"]:
                with self.subTest(area=area, reference=name):
                    self.assertTrue((PLUGIN / "references" / name).is_file())

    def test_method_documents_carry_invariant_sentences(self) -> None:
        for area, config in AREAS.items():
            references = [name for name in config["reference_files"] if "source-and-control-method" in name]
            if not references:
                continue
            method = PLUGIN / "references" / references[0]
            with self.subTest(area=area):
                text = " ".join(method.read_text(encoding="utf-8").split())
                for sentence in INVARIANT_METHOD_SENTENCES:
                    self.assertIn(sentence, text)

    def test_every_skill_mentions_shared_material(self) -> None:
        for area, config in AREAS.items():
            for skill in sorted(config["skills"]):
                with self.subTest(area=area, skill=skill):
                    lowered = skill_text(skill).lower()
                    for needle in config["every_skill_mentions"]:
                        self.assertIn(needle.lower(), lowered)


if __name__ == "__main__":
    unittest.main()
