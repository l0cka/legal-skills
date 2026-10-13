from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-contract-review"


class AustralianContractReviewTests(unittest.TestCase):
    def test_each_skill_has_failure_eval_and_review_controls(self) -> None:
        prompts = [path.read_text(encoding="utf-8") for path in (PLUGIN / "evals").glob("*/prompt.md")]
        for path in (PLUGIN / "skills").glob("*/SKILL.md"):
            with self.subTest(skill=path.parent.name):
                text = path.read_text(encoding="utf-8").split("<!-- generated:plugin-dependencies -->")[0]
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
        for path in PLUGIN.rglob("*.md"):
            for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                with self.subTest(document=str(path.relative_to(ROOT)), target=target):
                    resolved = (path.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(resolved.is_relative_to(PLUGIN))
                    self.assertTrue(resolved.is_file())

    def test_shared_workflows_are_named_and_dependencies_declared(self) -> None:
        catalog = json.loads((PLUGIN / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(set(catalog["requires"]), {"australian-commercial-drafting", "australian-legal-research"})
        self.assertEqual(set(catalog["handsOffTo"]), {"australian-employment-fair-work", "australian-privacy-cybersecurity"})
        expected = {
            "configure-review-playbook": ("configure-drafting-profile", "configure-employment-profile"),
            "review-commercial-agreement": ("draft-services-agreement", "assess-australian-privacy-issues", "map-fair-work-obligations"),
            "track-contract-renewals": ("draft-website-terms", "check-commonwealth-legislation"),
        }
        for name, owners in expected.items():
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8").split("<!-- generated:plugin-dependencies -->")[0]
            for owner in owners:
                with self.subTest(skill=name, owner=owner):
                    self.assertIn(f"`${owner}`", text)
        references = {path.name for path in (PLUGIN / "references").iterdir()}
        self.assertNotIn("unfair-contract-terms-checklist.md", references)
        self.assertNotIn("employment-profile-schema.md", references)

    def test_statutory_limits_and_unverified_state_leads_remain_explicit(self) -> None:
        leads = (PLUGIN / "references" / "statutory-verification-leads.md").read_text(encoding="utf-8")
        for control in (
            "C2026C00405", "C2026C00429", "upfront price not exceeding $5 million",
            "no upfront-price ceiling", "commences 1 July 2027", "Section 312 lists ss 48B, 48E and 48F",
            "not listed\nin s 312", "verify actual\nregulations", "not authority for a general monetary cap",
        ):
            self.assertIn(control, leads)
        route = (PLUGIN / "references" / "state-liability-verification-route.md").read_text(encoding="utf-8")
        for control in ("403", "NOT VERIFIED", "verify against", "s 7(3)", "Chapter 2\nPart 2"):
            self.assertIn(control, route)


if __name__ == "__main__":
    unittest.main()
