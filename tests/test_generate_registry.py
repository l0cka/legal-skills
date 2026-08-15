from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "generate_registry", ROOT / "scripts" / "generate_registry.py"
)
generate_registry = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = generate_registry
SPEC.loader.exec_module(generate_registry)

from test_validate_repository import (  # noqa: E402
    PLUGIN,
    SKILL,
    build_repo,
    openai_agent_yaml,
    skill_markdown,
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

    def test_check_flags_tampered_generated_file(self) -> None:
        generate_registry.apply(self.generate())
        catalog_path = self.root / ".claude-plugin" / "marketplace.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["plugins"][0]["version"] = "9.9.9"
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
        self.assertEqual(generate_registry.check(self.generate()), [catalog_path])

    def test_new_skill_is_scaffolded_with_empty_source(self) -> None:
        skill_dir = self.root / "plugins" / PLUGIN / "skills" / "new-skill"
        write(skill_dir / "SKILL.md", skill_markdown(name="new-skill"))
        write(skill_dir / "agents" / "openai.yaml", openai_agent_yaml())
        generate_registry.apply(self.generate())
        registry = json.loads((self.root / "skills.json").read_text(encoding="utf-8"))
        by_name = {entry["name"]: entry for entry in registry["skills"]}
        self.assertEqual(set(by_name), {SKILL, "new-skill"})
        self.assertEqual(by_name["new-skill"]["source"], "")
        self.assertEqual(by_name[SKILL]["source"], "Original test fixture.")

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
        registry = json.loads((self.root / "skills.json").read_text(encoding="utf-8"))
        self.assertEqual(registry["skills"][0]["plugin_version"], "0.2.0")

    def test_evidence_states_stamp_into_method_document(self) -> None:
        catalog_path = self.root / "plugins" / PLUGIN / "catalog.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["evidenceStates"] = {
            "qualifications": ["commencement", "application"],
            "unverifiable": ["official source", "decisive fact"],
        }
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
        method = (
            self.root / "plugins" / PLUGIN / "references"
            / "demo-source-and-control-method.md"
        )
        write(
            method,
            "# Method\n\n## Evidence states\n\n"
            "<!-- generated:evidence-states -->\n"
            "<!-- end:evidence-states -->\n",
        )
        generate_registry.apply(self.generate())
        text = " ".join(method.read_text(encoding="utf-8").split())
        self.assertIn("commencement or application qualification remains", text)
        self.assertIn("the official source or decisive fact could not be", text)
        self.assertEqual(generate_registry.check(self.generate()), [])

    def test_evidence_states_without_method_document_fails(self) -> None:
        catalog_path = self.root / "plugins" / PLUGIN / "catalog.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["evidenceStates"] = {
            "qualifications": ["commencement"],
            "unverifiable": ["official source"],
        }
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
        with self.assertRaises(generate_registry.GenerationError):
            self.generate()

    def test_missing_catalog_json_fails(self) -> None:
        (self.root / "plugins" / PLUGIN / "catalog.json").unlink()
        with self.assertRaises(generate_registry.GenerationError):
            self.generate()

    def test_missing_readme_region_marker_fails(self) -> None:
        readme = self.root / "README.md"
        text = readme.read_text(encoding="utf-8").replace("<!-- end:plugin-table -->", "")
        readme.write_text(text, encoding="utf-8")
        with self.assertRaises(generate_registry.GenerationError):
            self.generate()

    def test_number_word(self) -> None:
        self.assertEqual(generate_registry.number_word(7), "seven")
        self.assertEqual(generate_registry.number_word(48), "forty-eight")
        self.assertEqual(generate_registry.number_word(30), "thirty")


if __name__ == "__main__":
    unittest.main()
