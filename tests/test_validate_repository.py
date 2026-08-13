from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repository", ROOT / "scripts" / "validate_repository.py"
)
validate_repository = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_repository
SPEC.loader.exec_module(validate_repository)

PLUGIN = "demo-plugin"
SKILL = "demo-skill"
KEYWORDS = ["australian-law", "demo"]
DESCRIPTION = "Demo plugin used by validator tests."


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    write(path, json.dumps(payload, indent=2) + "\n")


def plugin_manifest() -> dict:
    return {
        "name": PLUGIN,
        "version": "0.1.0",
        "description": DESCRIPTION,
        "author": {"name": "l0cka"},
        "repository": "https://example.invalid/legal-skills",
        "license": "MIT",
        "keywords": list(KEYWORDS),
        "skills": "./skills/",
    }


def skill_markdown(name: str = SKILL, description: str = "Demo skill for tests.") -> str:
    return (
        f"---\nname: {name}\ndescription: {description}\n---\n\n"
        f"# Demo Skill\n\nSee [the method](references/method.md).\n"
    )


def openai_agent_yaml() -> str:
    return (
        "interface:\n"
        '  display_name: "Demo Skill"\n'
        '  short_description: "Demo skill"\n'
        '  default_prompt: "Use $demo-skill."\n'
    )


def build_repo(root: Path) -> None:
    write_json(
        root / ".agents" / "plugins" / "marketplace.json",
        {
            "name": "legal-skills",
            "plugins": [
                {
                    "name": PLUGIN,
                    "source": {"source": "local", "path": f"./plugins/{PLUGIN}"},
                    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                    "category": "Productivity",
                    "description": DESCRIPTION,
                    "version": "0.1.0",
                    "keywords": list(KEYWORDS),
                }
            ],
        },
    )
    write_json(
        root / ".claude-plugin" / "marketplace.json",
        {
            "name": "legal-skills",
            "plugins": [
                {
                    "name": PLUGIN,
                    "source": f"./plugins/{PLUGIN}",
                    "description": DESCRIPTION,
                    "version": "0.1.0",
                    "category": "Productivity",
                    "tags": list(KEYWORDS),
                }
            ],
        },
    )
    write_json(
        root / "skills.json",
        {
            "registry_version": 1,
            "skills": [
                {
                    "name": SKILL,
                    "version": "0.1.0",
                    "path": f"plugins/{PLUGIN}/skills/{SKILL}",
                    "plugin": f"plugins/{PLUGIN}",
                    "plugin_version": "0.1.0",
                    "targets": ["claude-cowork", "chatgpt-work"],
                    "source": "Original test fixture.",
                }
            ],
        },
    )
    plugin_dir = root / "plugins" / PLUGIN
    write_json(plugin_dir / ".codex-plugin" / "plugin.json", plugin_manifest())
    write_json(plugin_dir / ".claude-plugin" / "plugin.json", plugin_manifest())
    write(plugin_dir / "README.md", "# Demo plugin\n")
    skill_dir = plugin_dir / "skills" / SKILL
    write(skill_dir / "SKILL.md", skill_markdown())
    write(skill_dir / "references" / "method.md", "# Method\n")
    write(skill_dir / "agents" / "openai.yaml", openai_agent_yaml())


class ValidateRepositoryTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        build_repo(self.root)
        self.plugin_dir = self.root / "plugins" / PLUGIN
        self.skill_dir = self.plugin_dir / "skills" / SKILL

    def validate(self) -> tuple[int, int]:
        return validate_repository.validate(self.root)

    def assert_error(self, fragment: str) -> None:
        with self.assertRaises(validate_repository.ValidationError) as ctx:
            self.validate()
        self.assertIn(fragment, str(ctx.exception))

    def test_valid_repository_passes(self) -> None:
        self.assertEqual(self.validate(), (1, 1))

    def test_missing_description_fails(self) -> None:
        write(self.skill_dir / "SKILL.md", f"---\nname: {SKILL}\n---\n\n# Demo\n")
        self.assert_error("non-empty description")

    def test_overlong_description_fails(self) -> None:
        write(self.skill_dir / "SKILL.md", skill_markdown(description="x" * 1025))
        self.assert_error("exceeds 1024")

    def test_malformed_frontmatter_line_fails(self) -> None:
        write(
            self.skill_dir / "SKILL.md",
            f"---\nname: {SKILL}\nnot yaml at all\ndescription: ok\n---\n\n# Demo\n",
        )
        self.assert_error("malformed frontmatter")

    def test_frontmatter_name_mismatch_fails(self) -> None:
        write(self.skill_dir / "SKILL.md", skill_markdown(name="other-skill"))
        self.assert_error(f"frontmatter name must equal {SKILL}")

    def test_broken_relative_link_fails(self) -> None:
        (self.skill_dir / "references" / "method.md").unlink()
        self.assert_error("broken relative link")

    def test_missing_openai_agent_file_fails(self) -> None:
        (self.skill_dir / "agents" / "openai.yaml").unlink()
        self.assert_error("missing ChatGPT Work interface file")

    def test_openai_agent_file_missing_key_fails(self) -> None:
        write(
            self.skill_dir / "agents" / "openai.yaml",
            'interface:\n  display_name: "Demo"\n  short_description: "Demo"\n',
        )
        self.assert_error("missing required key default_prompt")

    def test_skill_directory_without_skill_md_fails(self) -> None:
        stray = self.plugin_dir / "skills" / "stray-skill"
        stray.mkdir()
        self.assert_error("skill directory missing SKILL.md")

    def test_missing_plugin_readme_fails(self) -> None:
        (self.plugin_dir / "README.md").unlink()
        self.assert_error("missing plugin README")

    def test_claude_marketplace_description_drift_fails(self) -> None:
        path = self.root / ".claude-plugin" / "marketplace.json"
        catalog = json.loads(path.read_text(encoding="utf-8"))
        catalog["plugins"][0]["description"] = "Something else."
        write_json(path, catalog)
        self.assert_error(f"description mismatch for {PLUGIN}")

    def test_codex_marketplace_keywords_drift_fails(self) -> None:
        path = self.root / ".agents" / "plugins" / "marketplace.json"
        catalog = json.loads(path.read_text(encoding="utf-8"))
        catalog["plugins"][0]["keywords"] = ["different"]
        write_json(path, catalog)
        self.assert_error(f"keywords mismatch for {PLUGIN}")

    def test_registry_skill_version_must_be_semver(self) -> None:
        path = self.root / "skills.json"
        registry = json.loads(path.read_text(encoding="utf-8"))
        registry["skills"][0]["version"] = "not-a-version"
        write_json(path, registry)
        self.assert_error(f"version for {SKILL}")

    def test_provider_manifest_version_drift_fails(self) -> None:
        path = self.plugin_dir / ".claude-plugin" / "plugin.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["version"] = "0.2.0"
        write_json(path, manifest)
        self.assert_error("provider manifest versions differ")

    def test_provider_manifest_description_drift_fails(self) -> None:
        path = self.plugin_dir / ".claude-plugin" / "plugin.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["description"] = "Something else."
        write_json(path, manifest)
        self.assert_error("provider manifest descriptions differ")


if __name__ == "__main__":
    unittest.main()
