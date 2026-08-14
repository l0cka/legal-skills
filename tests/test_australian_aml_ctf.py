from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "australian-aml-ctf"


class AustralianAmlCtfPluginTests(unittest.TestCase):
    EXPECTED_SKILLS = {
        "configure-aml-ctf-practice-profile",
        "map-designated-services",
        "review-aml-ctf-program",
        "map-reporting-obligations",
        "track-aml-ctf-developments",
    }

    REQUIRED_HEADINGS = ("## Workflow", "## Result contract", "## Fail closed")
    REQUIRED_STATUSES = (
        "`READY FOR HUMAN REVIEW`",
        "`READY WITH QUALIFICATIONS`",
        "`NOT READY`",
        "`OUTSIDE SCOPE`",
    )

    def test_plugin_contains_expected_skills(self) -> None:
        actual = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, self.EXPECTED_SKILLS)

    def test_every_skill_has_workflow_contract_and_fail_closed(self) -> None:
        for name in self.EXPECTED_SKILLS:
            path = PLUGIN / "skills" / name / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            for heading in self.REQUIRED_HEADINGS:
                self.assertIn(heading, text, path)
            for status in self.REQUIRED_STATUSES:
                self.assertIn(status, text, path)

    def test_every_skill_uses_shared_method(self) -> None:
        self.assertTrue(
            (PLUGIN / "references" / "aml-ctf-source-and-control-method.md").is_file()
        )
        self.assertTrue(
            (PLUGIN / "references" / "aml-ctf-practice-profile-schema.md").is_file()
        )
        self.assertTrue((PLUGIN / "references" / "lpp-carve-outs.md").is_file())
        for name in self.EXPECTED_SKILLS:
            text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("aml-ctf-source-and-control-method.md", text, name)

    def test_skills_never_conclude_suspicion_or_privilege(self) -> None:
        reporting_text = (
            PLUGIN / "skills" / "map-reporting-obligations" / "SKILL.md"
        ).read_text(encoding="utf-8")
        lowered = reporting_text.lower()
        self.assertIn("never conclude", lowered)
        self.assertIn("privilege", lowered)
        self.assertIn("responsible lawyer", lowered)
        self.assertIn("tipping-off", lowered)

    def test_unmapped_services_fail_closed(self) -> None:
        map_text = (
            PLUGIN / "skills" / "map-designated-services" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("cannot be determined", map_text)
        self.assertIn("$check-commonwealth-legislation", map_text)

    def test_depth_routes_to_sibling_plugins(self) -> None:
        program_text = (
            PLUGIN / "skills" / "review-aml-ctf-program" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("$assess-australian-privacy-issues", program_text)
        self.assertIn("$check-commonwealth-legislation", program_text)
        self.assertIn("$map-designated-services", program_text)

    def test_designated_services_registry_covers_table_6(self) -> None:
        registry_path = (
            PLUGIN
            / "skills"
            / "map-designated-services"
            / "references"
            / "designated-services-registry.json"
        )
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        items = {entry["item"] for entry in registry["items"]}
        self.assertEqual(items, set(range(1, 10)))
        self.assertTrue(
            registry["statutory_basis"]["guidance_source"].startswith("https://")
        )
        self.assertIn("cannot be determined", registry["note"])

    def test_watch_register_items_name_primary_sources(self) -> None:
        register_path = (
            PLUGIN
            / "skills"
            / "track-aml-ctf-developments"
            / "references"
            / "watch-register.json"
        )
        register = json.loads(register_path.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(register["watch_items"]), 4)
        for item in register["watch_items"]:
            self.assertTrue(item["primary_sources"], item["id"])
            self.assertIn("expected_trigger", item, item["id"])


if __name__ == "__main__":
    unittest.main()
