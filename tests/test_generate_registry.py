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
    PLUGIN,
    SKILL,
    build_repo,
    openai_agent_yaml,
    skill_markdown,
    update_json,
    validate_repository,
    write,
)

OTHER = "other-plugin"
OTHER_SKILL = "check-other-source"


def add_other_plugin(root: Path) -> None:
    """A second plugin whose skill the demo plugin can depend on."""
    source = root / "plugins" / PLUGIN
    target = root / "plugins" / OTHER
    for name in (".claude-plugin/plugin.json", "catalog.json"):
        write(target / name, (source / name).read_text(encoding="utf-8"))
    update_json(target / ".claude-plugin" / "plugin.json", name=OTHER)
    write(target / "README.md", "# Other plugin\n")
    skill_dir = target / "skills" / OTHER_SKILL
    write(skill_dir / "SKILL.md", skill_markdown(OTHER_SKILL))
    write(skill_dir / "references" / "method.md", "# Method\n")
    write(skill_dir / "agents" / "openai.yaml", openai_agent_yaml())
    registry = root / "skills.json"
    data = json.loads(registry.read_text(encoding="utf-8"))
    data["sources"][OTHER] = {OTHER_SKILL: "Original test fixture."}
    registry.write_text(json.dumps(data), encoding="utf-8")


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

    def test_evidence_states_stamp_into_method_document(self) -> None:
        catalog_path = self.root / "plugins" / PLUGIN / "catalog.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["evidenceStates"] = {
            "qualifications": ["commencement", "application"],
            "unverifiable": ["official source", "decisive fact"],
        }
        catalog_path.write_text(json.dumps(catalog), encoding="utf-8")
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

    def reference_other_skill(self) -> Path:
        add_other_plugin(self.root)
        skill_file = self.root / "plugins" / PLUGIN / "skills" / SKILL / "SKILL.md"
        write(skill_file, skill_markdown() + f"\nVerify with `${OTHER_SKILL}`.\n")
        return skill_file

    def test_undeclared_cross_plugin_reference_fails(self) -> None:
        self.reference_other_skill()
        with self.assertRaisesRegex(generate_registry.GenerationError, "does not declare"):
            self.generate()

    def test_declared_dependency_without_reference_fails(self) -> None:
        add_other_plugin(self.root)
        update_json(self.root / "plugins" / PLUGIN / "catalog.json", requires={OTHER: "Verifies."})
        with self.assertRaisesRegex(generate_registry.GenerationError, "no file in the plugin"):
            self.generate()

    def test_dependency_declared_twice_fails(self) -> None:
        self.reference_other_skill()
        update_json(
            self.root / "plugins" / PLUGIN / "catalog.json",
            requires={OTHER: "Verifies."},
            handsOffTo={OTHER: "Takes depth."},
        )
        with self.assertRaisesRegex(generate_registry.GenerationError, "both requires"):
            self.generate()

    def test_declared_dependency_stamps_skill_and_readmes(self) -> None:
        skill_file = self.reference_other_skill()
        update_json(
            self.root / "plugins" / PLUGIN / "catalog.json",
            requires={OTHER: "Verifies the source."},
        )
        generate_registry.apply(self.generate())
        skill = skill_file.read_text(encoding="utf-8")
        self.assertIn(f"- `{OTHER}` (required): `{OTHER_SKILL}`. Verifies the source.", skill)
        self.assertIn("Never perform that step from memory", " ".join(skill.split()))
        readme = (self.root / "plugins" / PLUGIN / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"- `{OTHER}` (required) — Verifies the source.", readme)
        index = (self.root / "plugins" / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"(requires `{OTHER}`; law checked", " ".join(index.split()))
        other_readme = (self.root / "plugins" / OTHER / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("plugin-dependencies", other_readme)
        self.assertEqual(generate_registry.check(self.generate()), [])
        validate_repository.validate(self.root)

    def test_dependency_section_removed_with_reference(self) -> None:
        skill_file = self.reference_other_skill()
        catalog = self.root / "plugins" / PLUGIN / "catalog.json"
        update_json(catalog, requires={OTHER: "Verifies the source."})
        generate_registry.apply(self.generate())
        update_json(catalog, requires={})
        text = skill_file.read_text(encoding="utf-8").replace(f"Verify with `${OTHER_SKILL}`.\n", "")
        write(skill_file, text)
        generate_registry.apply(self.generate())
        self.assertEqual(skill_file.read_text(encoding="utf-8"), skill_markdown())

    def test_router_is_exempt_from_dependency_declarations(self) -> None:
        add_other_plugin(self.root)
        router = self.root / "plugins" / generate_registry.ROUTER_PLUGIN
        write(router / "README.md", "# Router\n")
        for name in (".claude-plugin/plugin.json", "catalog.json"):
            write(router / name, (self.root / "plugins" / PLUGIN / name).read_text(encoding="utf-8"))
        update_json(router / ".claude-plugin" / "plugin.json", name=generate_registry.ROUTER_PLUGIN)
        skill_dir = router / "skills" / "route-demo"
        write(skill_dir / "SKILL.md", skill_markdown("route-demo") + f"\nRoute to `{OTHER_SKILL}`.\n")
        write(skill_dir / "references" / "method.md", "# Method\n")
        update_json(
            self.root / "plugins" / OTHER / "catalog.json",
            requires={PLUGIN: "Verifies."},
        )
        write(
            self.root / "plugins" / OTHER / "skills" / OTHER_SKILL / "SKILL.md",
            skill_markdown(OTHER_SKILL) + f"\nVerify with `${SKILL}`.\n",
        )
        outputs = self.generate()
        skill_map = outputs[router / "references" / "skill-map.md"]
        self.assertIn(f"Plugin dependencies: Requires `{PLUGIN}`.", skill_map)
        self.assertNotIn(skill_dir / "SKILL.md", outputs)

    def bundle(self) -> Path:
        return self.root / generate_registry.BUNDLE_DIR

    def test_bundle_carries_every_skill_and_reference(self) -> None:
        add_other_plugin(self.root)
        write(self.root / "plugins" / PLUGIN / "references" / "shared.md", "# Shared\n")
        generate_registry.apply(self.generate())
        bundle = self.bundle()
        for skill in (SKILL, OTHER_SKILL):
            self.assertTrue((bundle / "skills" / skill / "SKILL.md").is_file(), skill)
            self.assertTrue((bundle / "skills" / skill / "agents" / "openai.yaml").is_file(), skill)
        self.assertEqual((bundle / "references" / "shared.md").read_text(encoding="utf-8"), "# Shared\n")
        manifest = json.loads((bundle / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], generate_registry.BUNDLE_NAME)
        self.assertEqual(manifest["version"], "0.2.0")
        catalog = json.loads((self.root / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
        entry = catalog["plugins"][-1]
        self.assertEqual(entry["name"], generate_registry.BUNDLE_NAME)
        self.assertEqual(entry["source"]["path"], "./bundles/legal-skills-all")
        claude = json.loads((self.root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertNotIn(generate_registry.BUNDLE_NAME, [plugin["name"] for plugin in claude["plugins"]])

    def test_bundle_copies_regenerated_skill_text(self) -> None:
        add_other_plugin(self.root)
        update_json(self.root / "plugins" / PLUGIN / "catalog.json", requires={OTHER: "Verifies."})
        write(
            self.root / "plugins" / PLUGIN / "skills" / SKILL / "SKILL.md",
            skill_markdown() + f"\nVerify with `${OTHER_SKILL}`.\n",
        )
        outputs = self.generate()
        source = self.root / "plugins" / PLUGIN / "skills" / SKILL / "SKILL.md"
        copy = self.bundle() / "skills" / SKILL / "SKILL.md"
        self.assertIn("## Other plugins", outputs[copy])
        self.assertEqual(outputs[copy], outputs[source])

    def test_bundle_removes_orphans_and_mirrors_mode(self) -> None:
        script = self.root / "plugins" / PLUGIN / "skills" / SKILL / "scripts" / "run.py"
        write(script, "#!/usr/bin/env python3\n")
        script.chmod(0o755)
        copies: dict[Path, Path] = {}
        generate_registry.apply(generate_registry.generate(self.root, copies), copies)
        copy = self.bundle() / "skills" / SKILL / "scripts" / "run.py"
        self.assertTrue(generate_registry.is_executable(copy))
        script.unlink()
        copies = {}
        outputs = generate_registry.generate(self.root, copies)
        self.assertEqual(generate_registry.check(outputs, copies), [copy])
        generate_registry.apply(outputs, copies)
        self.assertFalse(copy.exists())
        self.assertEqual(generate_registry.check(generate_registry.generate(self.root)), [])

    def test_bundle_path_collision_fails(self) -> None:
        add_other_plugin(self.root)
        for plugin in (PLUGIN, OTHER):
            write(self.root / "plugins" / plugin / "references" / "method.md", "# Method\n")
        with self.assertRaisesRegex(generate_registry.GenerationError, "both map to"):
            self.generate()

    def test_bundle_version_sums_plugin_versions(self) -> None:
        plugins = [{"version": "0.1.2"}, {"version": "0.3.0"}, {"version": "1.0.1"}]
        self.assertEqual(generate_registry.bundle_version(plugins), "1.4.3")

    def test_number_word(self) -> None:
        self.assertEqual(generate_registry.number_word(7), "seven")
        self.assertEqual(generate_registry.number_word(48), "forty-eight")
        self.assertEqual(generate_registry.number_word(30), "thirty")


if __name__ == "__main__":
    unittest.main()
