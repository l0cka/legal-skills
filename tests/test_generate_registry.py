from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("generate_registry", ROOT / "scripts" / "generate_registry.py")
assert SPEC and SPEC.loader
generate_registry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = generate_registry
SPEC.loader.exec_module(generate_registry)

from test_validate_repository import (  # noqa: E402
    AREA,
    PLUGIN,
    SKILL,
    build_repo,
    demo_area,
    openai_agent_yaml,
    skill_markdown,
    update_area,
    update_json,
    validate_repository,
    write,
)


class GenerateRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        build_repo(self.root)

    def generate(self) -> dict[Path, str]:
        return generate_registry.generate(self.root)

    def test_generated_output_is_current_and_idempotent(self) -> None:
        generate_registry.apply(self.generate())
        self.assertEqual(generate_registry.check(self.generate()), [])
        self.assertEqual(generate_registry.apply(self.generate()), [])

    def test_generated_surfaces_pass_validation(self) -> None:
        generate_registry.apply(self.generate())
        validate_repository.validate(self.root)
        manifest = json.loads(
            (self.root / "plugins" / PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(manifest["skills"], "./skills/")

    def test_check_flags_tampered_generated_file(self) -> None:
        generate_registry.apply(self.generate())
        catalog_path = self.root / ".claude-plugin" / "marketplace.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["plugins"][0]["version"] = "9.9.9"
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
        self.assertEqual(generate_registry.check(self.generate()), [catalog_path])

    def test_version_bump_propagates_from_single_master(self) -> None:
        manifest_path = self.root / "plugins" / PLUGIN / ".claude-plugin" / "plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["version"] = "0.2.0"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        generate_registry.apply(self.generate())
        for relative in (
            ".claude-plugin/marketplace.json",
            ".agents/plugins/marketplace.json",
            f"plugins/{PLUGIN}/.codex-plugin/plugin.json",
        ):
            data = json.loads((self.root / relative).read_text(encoding="utf-8"))
            entries = data["plugins"] if "plugins" in data else [data]
            self.assertEqual(entries[0]["version"], "0.2.0", relative)

    def declare_evidence_states(self, method: str | None = "demo-source-and-control-method.md") -> None:
        update_area(
            self.root / "plugins" / PLUGIN,
            methodDocument=method,
            evidenceStates={
                "qualifications": ["commencement", "application"],
                "unverifiable": ["official source", "decisive fact"],
            },
        )

    def test_evidence_states_stamp_into_method_document(self) -> None:
        self.declare_evidence_states()
        method = self.root / "plugins" / PLUGIN / "references" / "demo-source-and-control-method.md"
        write(
            method,
            "# Method\n\n## Evidence states\n\n<!-- generated:evidence-states -->\n<!-- end:evidence-states -->\n",
        )
        generate_registry.apply(self.generate())
        text = " ".join(method.read_text(encoding="utf-8").split())
        self.assertIn("commencement or application qualification remains", text)
        self.assertIn("the official source or decisive fact could not be", text)
        self.assertEqual(generate_registry.check(self.generate()), [])

    def test_evidence_states_without_method_document_fails(self) -> None:
        self.declare_evidence_states()
        with self.assertRaisesRegex(generate_registry.GenerationError, "not found"):
            self.generate()

    def test_evidence_states_without_method_field_fails(self) -> None:
        update_area(
            self.root / "plugins" / PLUGIN,
            evidenceStates={"qualifications": ["commencement"], "unverifiable": ["official source"]},
        )
        with self.assertRaisesRegex(generate_registry.GenerationError, "go together"):
            self.generate()

    def test_missing_catalog_json_fails(self) -> None:
        (self.root / "plugins" / PLUGIN / "catalog.json").unlink()
        with self.assertRaises(generate_registry.GenerationError):
            self.generate()

    def test_missing_readme_region_marker_fails(self) -> None:
        readme = self.root / "README.md"
        text = readme.read_text(encoding="utf-8").replace("<!-- end:area-table -->", "")
        readme.write_text(text, encoding="utf-8")
        with self.assertRaises(generate_registry.GenerationError):
            self.generate()

    def test_skill_in_two_areas_fails(self) -> None:
        update_json(
            self.root / "plugins" / PLUGIN / "catalog.json",
            areas=[demo_area(), demo_area(id="second-area")],
        )
        with self.assertRaisesRegex(generate_registry.GenerationError, "more than one area"):
            self.generate()

    def test_area_table_and_install_name_the_single_plugin(self) -> None:
        generate_registry.apply(self.generate())
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"(plugins/{PLUGIN}/areas/{AREA}/README.md) | 1 |", readme)
        self.assertIn(f"claude plugin install {PLUGIN}@legal-skills --scope user", readme)
        plugin_readme = (self.root / "plugins" / PLUGIN / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"(areas/{AREA}/README.md)", plugin_readme)

    def test_router_area_gets_skill_map_of_other_areas(self) -> None:
        router_skill = self.root / "plugins" / PLUGIN / "skills" / "route-demo"
        write(router_skill / "SKILL.md", skill_markdown("route-demo", "Routes demo matters."))
        write(router_skill / "references" / "method.md", "# Method\n")
        write(router_skill / "agents" / "openai.yaml", openai_agent_yaml())
        update_json(
            self.root / "plugins" / PLUGIN / "catalog.json",
            areas=[demo_area(), demo_area(id=generate_registry.ROUTER_AREA, skills=["route-demo"])],
        )
        skill_map = self.generate()[self.root / "plugins" / PLUGIN / "references" / "skill-map.md"]
        self.assertIn(f"## Demo Area (`{AREA}`)", skill_map)
        self.assertIn(f"- **`{SKILL}`** — Demo skill for tests.", skill_map)
        self.assertNotIn("route-demo", skill_map)

    def test_number_word(self) -> None:
        self.assertEqual(generate_registry.number_word(7), "seven")
        self.assertEqual(generate_registry.number_word(48), "forty-eight")
        self.assertEqual(generate_registry.number_word(30), "thirty")
        self.assertEqual(generate_registry.number_word(103), "one hundred and three")
        self.assertEqual(generate_registry.number_word(200), "two hundred")


if __name__ == "__main__":
    unittest.main()
