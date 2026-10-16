from __future__ import annotations

import re
import unittest
from pathlib import Path

from layout import PLUGIN, area_eval_files, area_markdown, area_skill_files

ROOT = Path(__file__).resolve().parents[1]
AREA = "contract-review"


class AustralianContractReviewTests(unittest.TestCase):
    def test_each_skill_has_failure_eval_and_review_controls(self) -> None:
        prompts = [path.read_text(encoding="utf-8") for path in area_eval_files(AREA, "prompt.md")]
        for path in area_skill_files(AREA):
            with self.subTest(skill=path.parent.name):
                text = " ".join(path.read_text(encoding="utf-8").split())
                for control in (
                    "DRAFT - LAWYER REVIEW REQUIRED",
                    "2026-10-13",
                    "qualified lawyer",
                    "assumptions",
                    "legislation.gov.au",
                    "Never infer",
                ):
                    self.assertIn(control, text)
                cases = [prompt for prompt in prompts if re.search(rf"(?m)^name: {re.escape(path.parent.name)} ", prompt)]
                self.assertTrue(cases)
                self.assertTrue(any("fail-closed" in prompt for prompt in cases))

    def test_local_links_stay_within_owner_plugin(self) -> None:
        for path in area_markdown(AREA):
            for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                with self.subTest(document=str(path.relative_to(ROOT)), target=target):
                    resolved = (path.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(PLUGIN))
                    self.assertTrue(resolved.is_file())

    def test_shared_workflows_are_named_and_exist(self) -> None:
        expected = {
            "configure-review-playbook": ("configure-drafting-profile", "configure-employment-profile"),
            "review-commercial-agreement": ("draft-services-agreement", "assess-australian-privacy-issues", "map-fair-work-obligations"),
            "track-contract-renewals": ("draft-website-terms", "check-commonwealth-legislation"),
        }
        for name, owners in expected.items():
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            for owner in owners:
                with self.subTest(skill=name, owner=owner):
                    self.assertIn(f"`${owner}`", text)
                    self.assertTrue((PLUGIN / "skills" / owner / "SKILL.md").is_file())

    def test_statutory_limits_and_unverified_state_leads_remain_explicit(self) -> None:
        leads = " ".join((PLUGIN / "references" / "statutory-verification-leads.md").read_text(encoding="utf-8").split())
        for control in (
            "C2026C00405", "C2026C00429", "upfront price not exceeding $5 million",
            "commences 1 July 2027", "Section 312 lists ss 48B, 48E and 48F",
            "on or after commencement", "including 1 July 2027 itself",
            "has not already applied", "not listed in s 312", "verify actual regulations",
            "not authority for a general monetary cap", "consumer/small-business",
            "Sections 48E and 48F do use those cohort requirements",
        ):
            self.assertIn(control, leads)
        self.assertNotIn("varied after commencement", leads)
        self.assertNotIn("Section 23(3) concerns", leads)
        self.assertIn("read that installed reference rather than maintaining another copy", leads)
        route = " ".join((PLUGIN / "references" / "state-liability-verification-route.md").read_text(encoding="utf-8").split())
        for control in ("403", "NOT VERIFIED", "verify against", "s 7(3)", "Chapter 2 Part 2", "signed by the parties"):
            self.assertIn(control, route)

    def test_positive_eval_covers_each_skill(self) -> None:
        positive_prompts = [
            path.read_text(encoding="utf-8")
            for path in area_eval_files(AREA, "prompt.md")
            if "positive-path" in path.read_text(encoding="utf-8")
        ]
        for path in area_skill_files(AREA):
            with self.subTest(skill=path.parent.name):
                self.assertTrue(any(
                    re.search(rf"(?m)^name: {re.escape(path.parent.name)} ", prompt)
                    for prompt in positive_prompts
                ))

    def test_graders_have_distinct_case_specific_bodies(self) -> None:
        bodies = [
            " ".join(path.read_text(encoding="utf-8").split("\n---\n", 1)[1].split())
            for path in area_eval_files(AREA, "graders/workflow.md")
        ]
        self.assertEqual(len(bodies), len(set(bodies)))
        self.assertGreaterEqual(len(bodies), 19)

    def test_all_jurisdiction_rows_name_act_part_source_and_state(self) -> None:
        route = (PLUGIN / "references" / "state-liability-verification-route.md").read_text(encoding="utf-8")
        expected = {
            "NSW": ("Civil Liability Act 2002", "Part 4", "legislation.nsw.gov.au"),
            "Victoria": ("Wrongs Act 1958", "Part IVAA", "legislation.vic.gov.au"),
            "Queensland": ("Civil Liability Act 2003", "Chapter 2 Part 2", "legislation.qld.gov.au"),
            "Western Australia": ("Civil Liability Act 2002", "Part 1F", "legislation.wa.gov.au"),
            "South Australia": ("Law Reform (Contributory Negligence and Apportionment of Liability) Act 2001", "Part 3", "legislation.sa.gov.au"),
            "Tasmania": ("Civil Liability Act 2002", "Part 9A", "legislation.tas.gov.au"),
            "ACT": ("Civil Law (Wrongs) Act 2002", "Chapter 7A", "legislation.act.gov.au"),
            "Northern Territory": ("Proportionate Liability Act 2005", "Part 2", "legislation.nt.gov.au"),
        }
        for jurisdiction, controls in expected.items():
            row = next(line for line in route.splitlines() if line.startswith(f"| {jurisdiction} |"))
            with self.subTest(jurisdiction=jurisdiction):
                for control in controls:
                    self.assertIn(control, row)
                self.assertTrue("VERIFIED" in row or "verify against" in row)

    def test_reference_only_reuse_and_boundary_scenarios_are_exercised(self) -> None:
        case = PLUGIN / "evals" / f"{AREA}-renewal-on-commencement"
        prompt = (case / "prompt.md").read_text(encoding="utf-8")
        grader = (case / "graders" / "workflow.md").read_text(encoding="utf-8")
        self.assertIn("reference-only", prompt)
        self.assertIn("1 July 2027", prompt)
        self.assertIn("website terms fails", grader)
        for skill in ("track-contract-renewals", "check-unfair-contract-terms"):
            text = " ".join((PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8").split())
            with self.subTest(skill=skill):
                self.assertIn("drafting output", text)
                self.assertIn("retrieval is unavailable or declined", text)
                self.assertIn("not done", text)


if __name__ == "__main__":
    unittest.main()
