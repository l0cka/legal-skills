#!/usr/bin/env python3
"""Validate the hand-edited Legal Skills sources.

The canonical plugin sources are loaded (and shape-checked) by
generate_registry.py; `generate_registry.py --check` then guarantees every
generated surface matches them. This script covers what generation does not:
law-check currency, plugin READMEs, skill packages, and skills.json provenance.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_registry import SLUG, GenerationError, is_text, load_plugins  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_LINE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
MAX_DESCRIPTION_LENGTH = 1024
OPENAI_AGENT_KEYS = ("display_name", "short_description", "default_prompt")
REGISTRY_VERSION = 2
# A plugin whose legal content has not been re-checked within this window fails
# validation: re-verify the plugin against the official sources, fix anything
# stale, then set catalog.json lawCheckedOn to the check date.
LAW_CHECK_MAX_AGE_DAYS = 183


class ValidationError(Exception):
    """Raised when repository state violates the marketplace contract."""


def parse_frontmatter(relative: Path, text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValidationError(f"{relative}: missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValidationError(f"{relative}: unterminated YAML frontmatter")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        match = FRONTMATTER_LINE.match(line)
        if not match:
            raise ValidationError(f"{relative}: malformed frontmatter line: {line!r}")
        key, value = match.group(1), match.group(2).strip()
        if key in fields:
            raise ValidationError(f"{relative}: duplicate frontmatter key {key}")
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        fields[key] = value.strip()
    return fields


def validate_skill(root: Path, skill_dir: Path) -> None:
    relative = skill_dir.relative_to(root)
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValidationError(f"{relative}: skill directory missing SKILL.md")
    if not SLUG.fullmatch(skill_dir.name):
        raise ValidationError(f"{relative}: expected a lowercase hyphenated name")

    text = skill_file.read_text(encoding="utf-8")
    fields = parse_frontmatter(relative / "SKILL.md", text)
    if fields.get("name") != skill_dir.name:
        raise ValidationError(f"{relative}/SKILL.md: frontmatter name must equal {skill_dir.name}")
    description = fields.get("description", "")
    if not description:
        raise ValidationError(f"{relative}/SKILL.md: frontmatter requires a non-empty description")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        raise ValidationError(
            f"{relative}/SKILL.md: description exceeds {MAX_DESCRIPTION_LENGTH} characters"
        )

    for match in MARKDOWN_LINK.finditer(text):
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if not (skill_dir / target.split("#", 1)[0]).resolve().exists():
            raise ValidationError(f"{relative}/SKILL.md: broken relative link: {target}")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if not agent_file.is_file():
        raise ValidationError(f"{relative}/agents/openai.yaml: missing ChatGPT Work interface file")
    agent_text = agent_file.read_text(encoding="utf-8")
    for key in OPENAI_AGENT_KEYS:
        if not re.search(rf"(?m)^\s*{key}:\s*\S", agent_text):
            raise ValidationError(f"{relative}/agents/openai.yaml: missing required key {key}")


def validate_law_checked_on(relative: str, value: str, today: dt.date | None = None) -> None:
    try:
        checked = dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ValidationError(f"{relative}.lawCheckedOn: expected YYYY-MM-DD") from exc
    today = today or dt.date.today()
    if checked > today:
        raise ValidationError(f"{relative}.lawCheckedOn: {value} is in the future")
    if (today - checked).days > LAW_CHECK_MAX_AGE_DAYS:
        raise ValidationError(
            f"{relative}.lawCheckedOn: {value} is older than {LAW_CHECK_MAX_AGE_DAYS} days; "
            "re-check the plugin against the official sources and update the date"
        )


def load_sources(root: Path) -> dict[str, Any]:
    try:
        registry = json.loads((root / "skills.json").read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValidationError("missing required file: skills.json") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in skills.json:{exc.lineno}:{exc.colno}: {exc.msg}") from exc
    if not isinstance(registry, dict) or registry.get("registry_version") != REGISTRY_VERSION:
        raise ValidationError(f"skills.json.registry_version: must be {REGISTRY_VERSION}")
    sources = registry.get("sources")
    if not isinstance(sources, dict) or not all(isinstance(v, dict) for v in sources.values()):
        raise ValidationError("skills.json.sources: expected an object of plugin objects")
    return sources


def validate(root: Path = ROOT) -> tuple[int, int]:
    try:
        plugins = load_plugins(root)
    except GenerationError as exc:
        raise ValidationError(str(exc)) from exc
    sources = load_sources(root)

    seen_skills: set[str] = set()
    for plugin in plugins:
        name = plugin["name"]
        plugin_dir = root / "plugins" / name
        validate_law_checked_on(f"plugins/{name}/catalog.json", plugin["catalog"]["lawCheckedOn"])
        if not (plugin_dir / "README.md").is_file():
            raise ValidationError(f"plugins/{name}/README.md: missing plugin README")

        for skill_dir in sorted(path for path in (plugin_dir / "skills").iterdir() if path.is_dir()):
            validate_skill(root, skill_dir)
            if skill_dir.name in seen_skills:
                raise ValidationError(f"duplicate skill name: {skill_dir.name}")
            seen_skills.add(skill_dir.name)

        recorded = sources.get(name, {})
        for skill in plugin["skills"]:
            if not is_text(recorded.get(skill)):
                raise ValidationError(
                    f"skills.json: source provenance required for {name}/{skill}; add a "
                    "sentence recording where the workflow came from"
                )
        stale = sorted(set(recorded) - set(plugin["skills"]))
        if stale:
            raise ValidationError(f"skills.json: {name} lists unknown skill(s) {stale}")

    unknown_plugins = sorted(set(sources) - {plugin["name"] for plugin in plugins})
    if unknown_plugins:
        raise ValidationError(f"skills.json: unknown plugin(s) {unknown_plugins}")
    return len(plugins), len(seen_skills)


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
