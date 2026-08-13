#!/usr/bin/env python3
"""Validate the Legal Skills registry, marketplaces, and plugin packages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_TARGETS = {"claude-cowork", "chatgpt-work"}


class ValidationError(Exception):
    """Raised when repository state violates the marketplace contract."""


def load_json(relative_path: str) -> dict[str, Any]:
    path = ROOT / relative_path
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError(f"missing required file: {relative_path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"invalid JSON in {relative_path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{relative_path}: root must be an object")
    return data


def require_slug(value: Any, location: str) -> str:
    if not isinstance(value, str) or not SLUG.fullmatch(value):
        raise ValidationError(f"{location}: expected a lowercase hyphenated name")
    return value


def require_semver(value: Any, location: str) -> str:
    if not isinstance(value, str) or not SEMVER.fullmatch(value):
        raise ValidationError(f"{location}: expected a semantic version")
    return value


def plugin_entries(data: dict[str, Any], location: str) -> list[dict[str, Any]]:
    entries = data.get("plugins")
    if not isinstance(entries, list):
        raise ValidationError(f"{location}.plugins: expected an array")
    if not all(isinstance(entry, dict) for entry in entries):
        raise ValidationError(f"{location}.plugins: every entry must be an object")
    names = [require_slug(entry.get("name"), f"{location}.plugins[].name") for entry in entries]
    if len(names) != len(set(names)):
        raise ValidationError(f"{location}.plugins: plugin names must be unique")
    return entries


def parse_skill_name(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValidationError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValidationError(f"{path.relative_to(ROOT)}: unterminated YAML frontmatter")
    match = re.search(r"(?m)^name:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text[4:end])
    if not match:
        raise ValidationError(f"{path.relative_to(ROOT)}: frontmatter requires name")
    return require_slug(match.group(1).strip(), f"{path.relative_to(ROOT)}: name")


def validate_manifest(plugin_name: str, provider: str) -> dict[str, Any]:
    relative = f"plugins/{plugin_name}/.{provider}-plugin/plugin.json"
    manifest = load_json(relative)
    if manifest.get("name") != plugin_name:
        raise ValidationError(f"{relative}.name: must equal {plugin_name}")
    require_semver(manifest.get("version"), f"{relative}.version")
    if manifest.get("license") != "MIT":
        raise ValidationError(f"{relative}.license: must be MIT")
    if manifest.get("skills") != "./skills/":
        raise ValidationError(f"{relative}.skills: must be ./skills/")
    for field in ("description", "repository"):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            raise ValidationError(f"{relative}.{field}: required non-empty string")
    author = manifest.get("author")
    if not isinstance(author, dict) or not isinstance(author.get("name"), str):
        raise ValidationError(f"{relative}.author.name: required string")
    return manifest


def validate() -> tuple[int, int]:
    codex_path = ".agents/plugins/marketplace.json"
    claude_path = ".claude-plugin/marketplace.json"
    codex = load_json(codex_path)
    claude = load_json(claude_path)
    registry = load_json("skills.json")

    if codex.get("name") != "legal-skills":
        raise ValidationError(f"{codex_path}.name: must be legal-skills")
    if claude.get("name") != "legal-skills":
        raise ValidationError(f"{claude_path}.name: must be legal-skills")
    if registry.get("registry_version") != 1:
        raise ValidationError("skills.json.registry_version: must be 1")

    codex_entries = plugin_entries(codex, codex_path)
    claude_entries = plugin_entries(claude, claude_path)
    codex_by_name = {entry["name"]: entry for entry in codex_entries}
    claude_by_name = {entry["name"]: entry for entry in claude_entries}

    plugin_root = ROOT / "plugins"
    directories = {
        path.name
        for path in plugin_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }
    if set(codex_by_name) != directories:
        raise ValidationError(
            f"{codex_path}: entries {sorted(codex_by_name)} do not match plugin directories {sorted(directories)}"
        )
    if set(claude_by_name) != directories:
        raise ValidationError(
            f"{claude_path}: entries {sorted(claude_by_name)} do not match plugin directories {sorted(directories)}"
        )

    discovered_skills: dict[str, tuple[str, str]] = {}
    for plugin_name in sorted(directories):
        require_slug(plugin_name, f"plugins/{plugin_name}")
        codex_manifest = validate_manifest(plugin_name, "codex")
        claude_manifest = validate_manifest(plugin_name, "claude")
        version = codex_manifest["version"]
        if claude_manifest["version"] != version:
            raise ValidationError(f"plugins/{plugin_name}: provider manifest versions differ")

        codex_source = codex_by_name[plugin_name].get("source")
        expected_path = f"./plugins/{plugin_name}"
        if codex_source != {"source": "local", "path": expected_path}:
            raise ValidationError(f"{codex_path}: invalid source for {plugin_name}")
        policy = codex_by_name[plugin_name].get("policy")
        if policy != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
            raise ValidationError(f"{codex_path}: invalid policy for {plugin_name}")
        if not isinstance(codex_by_name[plugin_name].get("category"), str):
            raise ValidationError(f"{codex_path}: category required for {plugin_name}")

        claude_entry = claude_by_name[plugin_name]
        if claude_entry.get("source") != expected_path:
            raise ValidationError(f"{claude_path}: invalid source for {plugin_name}")
        if claude_entry.get("version") != version:
            raise ValidationError(f"{claude_path}: version mismatch for {plugin_name}")

        skill_root = ROOT / "plugins" / plugin_name / "skills"
        if not skill_root.is_dir():
            raise ValidationError(f"plugins/{plugin_name}/skills: missing directory")
        for skill_file in sorted(skill_root.glob("*/SKILL.md")):
            skill_name = skill_file.parent.name
            require_slug(skill_name, str(skill_file.parent.relative_to(ROOT)))
            if parse_skill_name(skill_file) != skill_name:
                raise ValidationError(
                    f"{skill_file.relative_to(ROOT)}: frontmatter name must equal {skill_name}"
                )
            if skill_name in discovered_skills:
                raise ValidationError(f"duplicate skill name: {skill_name}")
            discovered_skills[skill_name] = (plugin_name, version)

    registry_entries = registry.get("skills")
    if not isinstance(registry_entries, list):
        raise ValidationError("skills.json.skills: expected an array")
    registry_by_name: dict[str, dict[str, Any]] = {}
    for entry in registry_entries:
        if not isinstance(entry, dict):
            raise ValidationError("skills.json.skills: every entry must be an object")
        name = require_slug(entry.get("name"), "skills.json.skills[].name")
        if name in registry_by_name:
            raise ValidationError(f"skills.json: duplicate skill name {name}")
        registry_by_name[name] = entry

    if set(registry_by_name) != set(discovered_skills):
        raise ValidationError(
            "skills.json: entries do not match discovered SKILL.md directories"
        )
    for skill_name, (plugin_name, plugin_version) in discovered_skills.items():
        entry = registry_by_name[skill_name]
        if entry.get("path") != f"plugins/{plugin_name}/skills/{skill_name}":
            raise ValidationError(f"skills.json: invalid path for {skill_name}")
        if entry.get("plugin") != f"plugins/{plugin_name}":
            raise ValidationError(f"skills.json: invalid plugin for {skill_name}")
        if entry.get("plugin_version") != plugin_version:
            raise ValidationError(f"skills.json: version mismatch for {skill_name}")
        targets = entry.get("targets")
        if not isinstance(targets, list) or set(targets) != EXPECTED_TARGETS:
            raise ValidationError(f"skills.json: invalid targets for {skill_name}")
        if not isinstance(entry.get("source"), str) or not entry["source"].strip():
            raise ValidationError(f"skills.json: source provenance required for {skill_name}")

    return len(directories), len(discovered_skills)


def main() -> int:
    try:
        plugin_count, skill_count = validate()
    except (OSError, ValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Validated {plugin_count} plugin(s) and {skill_count} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
