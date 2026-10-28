from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from layout import PLUGIN, area_eval_files, area_skills

AREA = "work-health-safety"
REFERENCES = PLUGIN / "references"
CHECKERS = (
    "$check-commonwealth-legislation",
    "$check-nsw-legislation",
    "$check-victoria-legislation",
    "$check-queensland-legislation",
    "$check-western-australia-legislation",
    "$check-south-australia-legislation",
    "$check-tasmania-legislation",
    "$check-act-legislation",
    "$check-northern-territory-legislation",
)


def read(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def skill(name: str) -> str:
    return read(PLUGIN / "skills" / name / "SKILL.md")


class WorkHealthSafetyTests(unittest.TestCase):
    def test_every_jurisdiction_routes_to_its_own_checker(self) -> None:
        for name in ("whs-source-and-control-method.md", "whs-framework.md"):
            text = read(REFERENCES / name)
            for checker in CHECKERS:
                with self.subTest(reference=name, checker=checker):
                    self.assertIn(checker, text)
        self.assertIn("Never apply one jurisdiction's checker or text to another", read(REFERENCES / "whs-source-and-control-method.md"))

    def test_conclusions_stay_with_the_lawyer(self) -> None:
        phrases = {
            "map-whs-duties": "never conclude a breach",
            "assess-notifiable-incident": "never decide that an incident is or is not notifiable",
            "assess-officer-due-diligence": "never conclude that an officer did or did not exercise due diligence",
            "review-psychosocial-risk-controls": "never certify compliance",
            "track-whs-developments": "never describe a model-law amendment",
        }
        for name, phrase in phrases.items():
            with self.subTest(skill=name):
                self.assertIn(phrase, skill(name).lower())

    def test_victoria_is_never_mapped_onto_model_sections(self) -> None:
        for name in ("map-whs-duties", "assess-officer-due-diligence"):
            with self.subTest(skill=name):
                self.assertRegex(skill(name), r"[Nn]ever map (a model WHS Act section|the model due diligence elements) onto Victoria")
        self.assertIn("Never map a model WHS Act section onto Victoria", read(REFERENCES / "whs-framework.md"))

    def test_model_law_is_never_law_in_force(self) -> None:
        for name in ("map-whs-duties", "assess-notifiable-incident", "track-whs-developments"):
            with self.subTest(skill=name):
                self.assertRegex(skill(name).lower(), r"model-law amendment[^.]*(law in force|in force in a jurisdiction)")

    def test_incident_assessment_puts_the_urgent_block_first(self) -> None:
        text = skill("assess-notifiable-incident")
        contract = text.split("## Result contract", 1)[1]
        self.assertTrue(contract.split("```text", 1)[1].lstrip().startswith("URGENT PRELIMINARY INCIDENT ASSESSMENT HUMAN DECISION REQUIRED"))
        self.assertIn("never treat awareness time and incident time as the same", text.lower())

    def test_no_skill_computes_a_time_limit(self) -> None:
        self.assertIn("$compute-procedural-deadlines", read(REFERENCES / "whs-source-and-control-method.md"))
        self.assertIn("do not compute it", skill("assess-notifiable-incident"))

    def test_framework_reference_records_what_was_checked(self) -> None:
        text = read(REFERENCES / "whs-framework.md")
        self.assertIn("28 October 2026", text)
        self.assertIn("C2024C00243", text)
        for state in ("`VERIFIED WITH QUALIFICATIONS`", "`NOT VERIFIED`"):
            self.assertIn(state, text)

    def test_watch_register_items_name_primary_sources(self) -> None:
        register = json.loads(
            (PLUGIN / "skills" / "track-whs-developments" / "references" / "watch-register.json").read_text(encoding="utf-8")
        )
        self.assertEqual(register["as_at"], "2026-10-28")
        ids = {item["id"] for item in register["watch_items"]}
        self.assertIn("model-incident-notification-2025", ids)
        for item in register["watch_items"]:
            with self.subTest(item=item["id"]):
                self.assertTrue(item["primary_sources"])
                for url in item["primary_sources"]:
                    self.assertTrue(re.match(r"https://(www\.)?[a-z.]+\.gov\.au/", url), url)

    def test_every_skill_has_an_eval(self) -> None:
        prompts = " ".join(read(path) for path in area_eval_files(AREA, "prompt.md"))
        for name in area_skills(AREA):
            with self.subTest(skill=name):
                self.assertIn(name, prompts)


if __name__ == "__main__":
    unittest.main()
