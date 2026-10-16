from __future__ import annotations

import datetime as dt
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_repository", ROOT / "scripts" / "validate_repository.py")
assert SPEC and SPEC.loader
validate_repository = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validate_repository
SPEC.loader.exec_module(validate_repository)

PLUGIN = "demo-plugin"
SKILL = "demo-skill"
AREA = "demo-area"
README_REGIONS = ("badges", "counts", "area-table", "install-agent", "install-codex", "install-claude")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_json(path: Path, payload: dict) -> None:
    write(path, json.dumps(payload, indent=2) + "\n")


def update_json(path: Path, **changes) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update(changes)
    write_json(path, data)


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


def demo_area(**changes) -> dict:
    area = {
        "id": AREA,
        "displayName": "Demo Area",
        "shortDescription": "Demo area for tests.",
        "lawCheckedOn": dt.date.today().isoformat(),
        "skills": [SKILL],
    }
    area.update(changes)
    return area


def update_area(plugin_dir: Path, **changes) -> None:
    update_json(plugin_dir / "catalog.json", areas=[demo_area(**changes)])


def build_repo(root: Path) -> None:
    regions = "\n\n".join(f"<!-- generated:{r} -->\n<!-- end:{r} -->" for r in README_REGIONS)
    write(root / "README.md", f"# Demo marketplace\n\n{regions}\n")
    write_json(
        root / "skills.json",
        {"registry_version": 3, "sources": {SKILL: "Original test fixture."}},
    )
    plugin_dir = root / "plugins" / PLUGIN
    write_json(
        plugin_dir / ".claude-plugin" / "plugin.json",
        {
            "name": PLUGIN,
            "version": "0.1.0",
            "description": "Demo plugin used by validator tests.",
            "keywords": ["australian-law", "demo"],
        },
    )
    write_json(
        plugin_dir / "catalog.json",
        {
            "displayName": "Demo Plugin",
            "shortDescription": "Demo plugin for tests.",
            "longDescription": "A demo plugin used by the validator and generator tests.",
            "defaultPrompt": ["Use the demo skill."],
            "whatItDoes": ["Demonstrates the fixture."],
            "boundaries": ["Never leaves the test suite."],
            "areas": [demo_area()],
        },
    )
    write(plugin_dir / "README.md", "# Demo plugin\n\n<!-- generated:area-table -->\n<!-- end:area-table -->\n")
    write(plugin_dir / "areas" / AREA / "README.md", "# Demo area\n")
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

    def assert_error(self, fragment: str) -> None:
        with self.assertRaises(validate_repository.ValidationError) as ctx:
            validate_repository.validate(self.root)
        self.assertIn(fragment, str(ctx.exception))

    def test_valid_repository_passes(self) -> None:
        self.assertEqual(validate_repository.validate(self.root), (1, 1))

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
        (self.plugin_dir / "skills" / "stray-skill").mkdir()
        self.assert_error("skill directory missing SKILL.md")

    def test_missing_plugin_readme_fails(self) -> None:
        (self.plugin_dir / "README.md").unlink()
        self.assert_error("missing plugin README")

    def test_skill_without_source_fails(self) -> None:
        update_json(self.root / "skills.json", sources={SKILL: ""})
        self.assert_error(f"source provenance required for {SKILL}")

    def test_placeholder_source_fails(self) -> None:
        update_json(self.root / "skills.json", sources={SKILL: "TODO(human): provenance sentence"})
        self.assert_error(f"source provenance required for {SKILL}")

    def test_new_skill_without_source_fails(self) -> None:
        skill_dir = self.plugin_dir / "skills" / "new-skill"
        write(skill_dir / "SKILL.md", "---\nname: new-skill\ndescription: New.\n---\n")
        write(skill_dir / "agents" / "openai.yaml", openai_agent_yaml())
        update_area(self.plugin_dir, skills=[SKILL, "new-skill"])
        self.assert_error("source provenance required for new-skill")

    def test_skill_outside_every_area_fails(self) -> None:
        skill_dir = self.plugin_dir / "skills" / "new-skill"
        write(skill_dir / "SKILL.md", "---\nname: new-skill\ndescription: New.\n---\n")
        self.assert_error("skills in no area ['new-skill']")

    def test_area_naming_unknown_skill_fails(self) -> None:
        update_area(self.plugin_dir, skills=[SKILL, "ghost-skill"])
        self.assert_error("areas name unknown skills ['ghost-skill']")

    def test_missing_area_guide_fails(self) -> None:
        (self.plugin_dir / "areas" / AREA / "README.md").unlink()
        self.assert_error("missing area guide")

    def test_source_for_removed_skill_fails(self) -> None:
        update_json(self.root / "skills.json", sources={SKILL: "x", "gone-skill": "y"})
        self.assert_error("unknown skill(s) ['gone-skill']")

    def test_area_stale_law_check_fails(self) -> None:
        update_area(self.plugin_dir, lawCheckedOn=(dt.date.today() - dt.timedelta(days=200)).isoformat())
        self.assert_error("areas.demo-area.lawCheckedOn")

    def test_law_check_due_within_warning_window(self) -> None:
        today = dt.date(2026, 10, 16)
        update_area(self.plugin_dir, lawCheckedOn=(today - dt.timedelta(days=160)).isoformat())
        self.assertEqual(
            validate_repository.law_checks_due(self.root, today),
            [
                f"{PLUGIN} area {AREA}: lawCheckedOn 2026-05-09 expires in 23 day(s); "
                "re-check it against the official sources"
            ],
        )

    def test_recent_law_check_is_not_due(self) -> None:
        today = dt.date(2026, 10, 16)
        update_area(self.plugin_dir, lawCheckedOn=(today - dt.timedelta(days=100)).isoformat())
        self.assertEqual(validate_repository.law_checks_due(self.root, today), [])

    def test_area_malformed_law_check_fails(self) -> None:
        update_area(self.plugin_dir, lawCheckedOn="26 August 2026")
        self.assert_error("lawCheckedOn")

    def test_missing_plugin_catalog_fails(self) -> None:
        (self.plugin_dir / "catalog.json").unlink()
        self.assert_error(f"plugins/{PLUGIN}/catalog.json")

    def test_plugin_catalog_empty_list_field_fails(self) -> None:
        update_json(self.plugin_dir / "catalog.json", defaultPrompt=[])
        self.assert_error("'defaultPrompt' must be a non-empty array")

    def test_invalid_manifest_version_fails(self) -> None:
        update_json(self.plugin_dir / ".claude-plugin" / "plugin.json", version="one")
        self.assert_error("version must be a semantic version")

    def test_manifest_name_mismatch_fails(self) -> None:
        update_json(self.plugin_dir / ".claude-plugin" / "plugin.json", name="other-plugin")
        self.assert_error("name must equal the directory name")


if __name__ == "__main__":
    unittest.main()
