#!/usr/bin/env python3
"""Generate the Legal Skills distribution surfaces from the canonical sources.

Canonical, hand-edited sources per plugin:
  plugins/<name>/.claude-plugin/plugin.json  (name, version, description, keywords)
  plugins/<name>/catalog.json                (displayName, shortDescription,
                                              longDescription, lawCheckedOn,
                                              defaultPrompt, whatItDoes,
                                              boundaries; optional requires
                                              and handsOffTo)
  plugins/<name>/skills/<skill>/...          (the skill packages)

skills.json (per-skill provenance) is also hand-edited but not generated.
Everything this script writes is machine-owned: do not edit those files by
hand. That includes the all-in-one bundle under bundles/, a copy of every
plugin's skills/ and references/ trees. Run with --check (CI does) to fail
when any generated file is stale.
"""

from __future__ import annotations

import argparse
import json
import re
import stat
import sys
import textwrap
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

MARKETPLACE_NAME = "legal-skills"
MARKETPLACE_DISPLAY_NAME = "Legal Skills"
MARKETPLACE_DESCRIPTION = "Open-source, governed legal workflow plugins maintained by l0cka."
OWNER = "l0cka"
REPOSITORY = "https://github.com/l0cka/legal-skills"
AUTHOR = {"name": OWNER, "url": "https://github.com/l0cka"}
LICENSE = "MIT"
SKILLS_PATH = "./skills/"
CATEGORY = "Productivity"
CAPABILITIES = ["Read"]
BRAND_COLOR = "#1C3C63"
POLICY = {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
TARGETS_BADGE = (
    '  <img alt="Claude Cowork and ChatGPT Work" '
    'src="https://img.shields.io/badge/works%20with-'
    'Claude%20Cowork%20%2B%20ChatGPT%20Work-c59a46?style=flat-square">'
)

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MANIFEST_DATA_FIELDS = ("name", "version", "description", "keywords")
CATALOG_STRING_FIELDS = ("displayName", "shortDescription", "longDescription", "lawCheckedOn")
CATALOG_LIST_FIELDS = ("defaultPrompt", "whatItDoes", "boundaries")
EVIDENCE_STATE_KEYS = ("qualifications", "unverifiable")
# Cross-plugin dependency kinds declared in catalog.json as {plugin: reason}.
# "requires": a skill in this plugin invokes the other plugin's skills as a
# step of its own workflow (for example official-source verification).
# "handsOffTo": a skill routes part of a matter to the other plugin for depth.
DEPENDENCY_KINDS = {"requires": "required", "handsOffTo": "hand-off"}

# Canonical evidence-state contract, stamped into each declaring plugin's
# source-and-control method document. The convention is documented in
# docs/source-and-control-method-core.md; per-plugin qualification lists are
# declared in catalog.json under "evidenceStates".
EVIDENCE_STATES_HEADER = "Assign one state to every material proposition:"
EVIDENCE_STATE_VERIFIED = (
    "`VERIFIED` — the exact current or point-in-time official source and "
    "relevant text were checked in this session;"
)
EVIDENCE_STATE_QUALIFIED = (
    "`VERIFIED WITH QUALIFICATIONS` — the source was checked but a "
    "{qualifications} qualification remains;"
)
EVIDENCE_STATE_UNVERIFIED = "`NOT VERIFIED` — the {unverifiable} could not be confirmed; or"
EVIDENCE_STATE_OUTSIDE = (
    "`OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow."
)

# The all-in-one bundle: every shipped skill in one plugin, listed only in the
# .agents marketplace. Its skills/ and references/ trees mirror the plugins'
# own, so the skills' ../../references/ links resolve unchanged, and copying
# both trees into an .agents/ directory installs every skill without a
# marketplace.
BUNDLE_NAME = "legal-skills-all"
BUNDLE_DIR = Path("bundles") / BUNDLE_NAME
BUNDLE_TREES = ("skills", "references")
BUNDLE_SKIPPED = ("__pycache__",)
BUNDLE_KEYWORDS = ["legal-workflows", "australian-law", "bundle", "responsible-ai"]

ONES = (
    "zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen"
).split()
TENS = "twenty thirty forty fifty sixty seventy eighty ninety".split()


class GenerationError(Exception):
    """Raised when a canonical source is missing or malformed."""


def describe(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def number_word(value: int) -> str:
    if not 0 <= value <= 99:
        raise GenerationError(f"number_word supports 0-99, got {value}")
    if value < 20:
        return ONES[value]
    tens, ones = divmod(value, 10)
    word = TENS[tens - 2]
    return f"{word}-{ONES[ones]}" if ones else word


def dumps(data: Any) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GenerationError(f"missing canonical source: {describe(path)}") from exc
    except json.JSONDecodeError as exc:
        raise GenerationError(
            f"invalid JSON in {describe(path)}:{exc.lineno}: {exc.msg}"
        ) from exc
    if not isinstance(data, dict):
        raise GenerationError(f"{describe(path)}: root must be an object")
    return data


def is_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_text_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(is_text(item) for item in value)


def load_plugin(plugin_dir: Path) -> dict[str, Any]:
    manifest_path = f"{plugin_dir.name}/.claude-plugin/plugin.json"
    manifest = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
    for field in MANIFEST_DATA_FIELDS:
        check_field = is_text_list if field == "keywords" else is_text
        if not check_field(manifest.get(field)):
            raise GenerationError(f"{manifest_path}: field {field!r} is required")
    if manifest["name"] != plugin_dir.name or not SLUG.fullmatch(plugin_dir.name):
        raise GenerationError(
            f"{manifest_path}: name must equal the directory name and be lowercase and hyphenated"
        )
    if not SEMVER.fullmatch(manifest["version"]):
        raise GenerationError(f"{manifest_path}: version must be a semantic version")
    catalog = load_json(plugin_dir / "catalog.json")
    for field in CATALOG_STRING_FIELDS:
        if not is_text(catalog.get(field)):
            raise GenerationError(f"{plugin_dir.name}/catalog.json: field {field!r} is required")
    for field in CATALOG_LIST_FIELDS:
        if not is_text_list(catalog.get(field)):
            raise GenerationError(
                f"{plugin_dir.name}/catalog.json: field {field!r} must be a "
                "non-empty array of strings"
            )
    states = catalog.get("evidenceStates")
    method_path = None
    if states is not None:
        for key in EVIDENCE_STATE_KEYS:
            if not isinstance(states, dict) or not is_text_list(states.get(key)):
                raise GenerationError(
                    f"{plugin_dir.name}/catalog.json: evidenceStates.{key} must be "
                    "a non-empty array of strings"
                )
        methods = sorted(
            (plugin_dir / "references").glob("*source-and-control-method.md")
        )
        if len(methods) != 1:
            raise GenerationError(
                f"{plugin_dir.name}: evidenceStates declared but found "
                f"{len(methods)} *source-and-control-method.md file(s) under references/"
            )
        method_path = methods[0]
    dependencies: dict[str, dict[str, str]] = {}
    for field in DEPENDENCY_KINDS:
        declared = catalog.get(field, {})
        if not isinstance(declared, dict) or not all(
            SLUG.fullmatch(str(key)) and is_text(value) for key, value in declared.items()
        ):
            raise GenerationError(
                f"{plugin_dir.name}/catalog.json: {field!r} must map plugin names to "
                "a non-empty reason"
            )
        dependencies[field] = dict(sorted(declared.items()))
    overlap = sorted(set(dependencies["requires"]) & set(dependencies["handsOffTo"]))
    if overlap:
        raise GenerationError(
            f"{plugin_dir.name}/catalog.json: {overlap} declared as both requires and handsOffTo"
        )
    skills = sorted(
        path.parent.name
        for path in (plugin_dir / "skills").glob("*/SKILL.md")
    )
    if not skills:
        raise GenerationError(f"{plugin_dir.name}: no skills found under skills/")
    return {
        "name": manifest["name"],
        "version": manifest["version"],
        "description": manifest["description"],
        "keywords": manifest["keywords"],
        "catalog": catalog,
        "skills": skills,
        "method_path": method_path,
        "dependencies": dependencies,
    }


def load_plugins(root: Path) -> list[dict[str, Any]]:
    plugin_dirs = sorted(
        path
        for path in (root / "plugins").iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    return [load_plugin(path) for path in plugin_dirs]


def claude_manifest(plugin: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": plugin["name"],
        "version": plugin["version"],
        "description": plugin["description"],
        "author": AUTHOR,
        "homepage": f"{REPOSITORY}/tree/main/plugins/{plugin['name']}",
        "repository": REPOSITORY,
        "license": LICENSE,
        "keywords": plugin["keywords"],
        "skills": SKILLS_PATH,
    }


def codex_manifest(plugin: dict[str, Any]) -> dict[str, Any]:
    catalog = plugin["catalog"]
    manifest = claude_manifest(plugin)
    manifest["interface"] = {
        "displayName": catalog["displayName"],
        "shortDescription": catalog["shortDescription"],
        "longDescription": catalog["longDescription"],
        "developerName": OWNER,
        "category": CATEGORY,
        "capabilities": CAPABILITIES,
        "websiteURL": REPOSITORY,
        "defaultPrompt": catalog["defaultPrompt"],
        "brandColor": BRAND_COLOR,
    }
    return manifest


def claude_marketplace(plugins: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "name": MARKETPLACE_NAME,
        "owner": {"name": OWNER},
        "metadata": {"description": MARKETPLACE_DESCRIPTION},
        "plugins": [
            {
                "name": plugin["name"],
                "source": f"./plugins/{plugin['name']}",
                "description": plugin["description"],
                "version": plugin["version"],
                "category": CATEGORY,
                "tags": plugin["keywords"],
            }
            for plugin in plugins
        ],
    }


def agents_marketplace(plugins: list[dict[str, Any]], bundle: dict[str, Any]) -> dict[str, Any]:
    """The .agents catalog: every plugin, then the all-in-one bundle."""
    return {
        "name": MARKETPLACE_NAME,
        "interface": {
            "displayName": MARKETPLACE_DISPLAY_NAME,
            "description": MARKETPLACE_DESCRIPTION,
        },
        "plugins": [
            {
                "name": plugin["name"],
                "source": {"source": "local", "path": plugin.get("path", f"./plugins/{plugin['name']}")},
                "policy": POLICY,
                "category": CATEGORY,
                "description": plugin["description"],
                "version": plugin["version"],
                "keywords": plugin["keywords"],
            }
            for plugin in [*plugins, bundle]
        ],
    }


def plugins_readme(plugins: list[dict[str, Any]]) -> str:
    lines = [
        "<!-- GENERATED FILE - do not edit. Edit plugin.json/catalog.json and",
        "     run: python3 scripts/generate_registry.py -->",
        "",
        "# Plugins",
        "",
        "Canonical plugin packages live in this directory.",
        "",
    ]
    for plugin in plugins:
        notes = [dependency_summary(plugin["dependencies"])]
        notes.append(f"law checked {plugin['catalog']['lawCheckedOn']}")
        entry = (
            f"- [**{plugin['catalog']['displayName']}**]({plugin['name']}/README.md) — "
            f"{plugin['catalog']['shortDescription']} "
            f"({'; '.join(note for note in notes if note)})"
        )
        lines.extend(
            textwrap.wrap(
                entry,
                width=78,
                subsequent_indent="  ",
                break_on_hyphens=False,
                break_long_words=False,
            )
        )
    lines.extend(["", "See [Adding a plugin](../docs/adding-a-plugin.md)."])
    return "\n".join(lines) + "\n"


def badges_region(plugins: list[dict[str, Any]], skill_count: int) -> str:
    plugin_word = number_word(len(plugins)).capitalize()
    skill_word = number_word(skill_count).capitalize()
    return "\n".join(
        [
            f'  <img alt="{plugin_word} plugins" '
            f'src="https://img.shields.io/badge/plugins-{len(plugins)}-31547a?style=flat-square">',
            f'  <img alt="{skill_word} skills" '
            f'src="https://img.shields.io/badge/skills-{skill_count}-31547a?style=flat-square">',
            TARGETS_BADGE,
        ]
    )


def counts_region(plugins: list[dict[str, Any]], skill_count: int) -> str:
    return (
        f"The marketplace contains {number_word(len(plugins))} plugins and "
        f"{number_word(skill_count)} skills:"
    )


def table_region(plugins: list[dict[str, Any]]) -> str:
    lines = [
        "| Plugin | Skills | Description | Law checked |",
        "| --- | :---: | --- | :---: |",
    ]
    for plugin in plugins:
        catalog = plugin["catalog"]
        lines.append(
            f"| [**{catalog['displayName']}**](plugins/{plugin['name']}/README.md) "
            f"| {len(plugin['skills'])} | {catalog['shortDescription']} "
            f"| {catalog['lawCheckedOn']} |"
        )
    return "\n".join(lines)


def install_agent_region(plugins: list[dict[str, Any]]) -> str:
    word = number_word(len(plugins))
    request = (
        f"Add the plugin marketplace `{OWNER}/{MARKETPLACE_NAME}` and install "
        f"all {word} of its plugins (user scope if supported). Verify the "
        f"plugins are available and report the result."
    )
    wrapped = textwrap.wrap(
        request, width=74, break_on_hyphens=False, break_long_words=False
    )
    return "```text\n" + "\n".join(wrapped) + "\n```"


def install_codex_region(plugins: list[dict[str, Any]]) -> str:
    lines = [f"codex plugin marketplace add {OWNER}/{MARKETPLACE_NAME}"]
    lines += [
        f"codex plugin add {plugin['name']}@{MARKETPLACE_NAME}" for plugin in plugins
    ]
    return "```bash\n" + "\n".join(lines) + "\n```"


def install_claude_region(plugins: list[dict[str, Any]]) -> str:
    lines = [f"claude plugin marketplace add {OWNER}/{MARKETPLACE_NAME}"]
    lines += [
        f"claude plugin install {plugin['name']}@{MARKETPLACE_NAME} --scope user"
        for plugin in plugins
    ]
    return "```bash\n" + "\n".join(lines) + "\n```"


def install_bundle_region() -> str:
    bundle = BUNDLE_DIR.as_posix()
    return "\n".join(
        [
            "```bash",
            "# Codex or ChatGPT Work: one plugin from the .agents marketplace",
            f"codex plugin marketplace add {OWNER}/{MARKETPLACE_NAME}",
            f"codex plugin add {BUNDLE_NAME}@{MARKETPLACE_NAME}",
            "",
            "# Or copy the skills straight into an .agents directory",
            "# (~/.agents for your user, or .agents at a project root)",
            f"git clone --depth 1 {REPOSITORY}.git",
            "mkdir -p ~/.agents",
            f"cp -R {MARKETPLACE_NAME}/{bundle}/skills {MARKETPLACE_NAME}/{bundle}/references ~/.agents/",
            "```",
        ]
    )


def bundle_version(plugins: list[dict[str, Any]]) -> str:
    """Sum each version component across the plugins.

    Any plugin release raises the bundle version, because a bump either raises
    a component's sum or raises a more significant one while resetting a lower.
    """
    parts = [
        [int(part) for part in SEMVER.fullmatch(plugin["version"]).groups()[:3]]  # type: ignore[union-attr]
        for plugin in plugins
    ]
    return ".".join(str(sum(column)) for column in zip(*parts))


def bundle_plugin(plugins: list[dict[str, Any]], skill_count: int) -> dict[str, Any]:
    return {
        "name": BUNDLE_NAME,
        "path": f"./{BUNDLE_DIR.as_posix()}",
        "version": bundle_version(plugins),
        "description": (
            f"Every Legal Skills workflow in one plugin: all {number_word(skill_count)} "
            f"skills from the {number_word(len(plugins))} plugins, generated from their "
            "canonical sources. Install this or the individual plugins, not both."
        ),
        "keywords": BUNDLE_KEYWORDS,
    }


def bundle_manifest(bundle: dict[str, Any], plugins: list[dict[str, Any]]) -> dict[str, Any]:
    names = ", ".join(plugin["catalog"]["displayName"] for plugin in plugins)
    return {
        "name": bundle["name"],
        "version": bundle["version"],
        "description": bundle["description"],
        "author": AUTHOR,
        "homepage": f"{REPOSITORY}/tree/main/{BUNDLE_DIR.as_posix()}",
        "repository": REPOSITORY,
        "license": LICENSE,
        "keywords": bundle["keywords"],
        "skills": SKILLS_PATH,
        "interface": {
            "displayName": f"{MARKETPLACE_DISPLAY_NAME} (all)",
            "shortDescription": "Every Legal Skills plugin's skills in one install.",
            "longDescription": (
                f"Bundles the skills and shared references of every Legal Skills plugin: {names}. "
                "Each skill keeps its own sources, result contract and human-review gates; the "
                "bundle adds no legal logic. It is regenerated from the individual plugins on "
                "every change, so it never drifts from them."
            ),
            "developerName": OWNER,
            "category": CATEGORY,
            "capabilities": CAPABILITIES,
            "websiteURL": REPOSITORY,
            "defaultPrompt": [
                "Route this fact pattern: which Legal Skills workflows does it engage, and in what order?",
                "Check these Australian citations against the official publishers.",
                "Which skills in this bundle apply to a data breach at an Australian company?",
            ],
            "brandColor": BRAND_COLOR,
        },
    }


def bundle_readme(bundle: dict[str, Any], plugins: list[dict[str, Any]], skill_count: int) -> str:
    lines = [
        "<!-- GENERATED FILE - do not edit. Built from plugins/ by",
        "     scripts/generate_registry.py -->",
        "",
        f"# {MARKETPLACE_DISPLAY_NAME} (all)",
        "",
        *wrap_paragraph(
            f"`{BUNDLE_NAME}` installs every Legal Skills workflow at once: "
            f"{number_word(skill_count)} skills from {number_word(len(plugins))} plugins. "
            "It is a generated copy of each plugin's `skills/` and `references/` "
            "trees, so every skill behaves exactly as it does in its own plugin, "
            "with the same sources, result contract and human-review gates."
        ),
        "",
        *wrap_paragraph(
            "Install either this bundle or the individual plugins, not both: "
            "installing both loads every skill twice."
        ),
        "",
        "## Install",
        "",
        install_bundle_region(),
        "",
        *wrap_paragraph(
            "Copying into `.agents/` needs both trees: the skills link to shared "
            "files at `../../references/`. Copy again to update."
        ),
        "",
        "## Included plugins",
        "",
    ]
    for plugin in plugins:
        skills = ", ".join(f"`{skill}`" for skill in plugin["skills"])
        lines.extend(
            textwrap.wrap(
                f"- [**{plugin['catalog']['displayName']}**](../../plugins/{plugin['name']}/README.md) "
                f"{plugin['version']}, law checked {plugin['catalog']['lawCheckedOn']}: {skills}",
                width=78,
                subsequent_indent="  ",
                break_on_hyphens=False,
                break_long_words=False,
            )
        )
    lines += [
        "",
        "## Before you rely on it",
        "",
        *wrap_paragraph(
            "Every skill prepares work for a lawyer or other qualified person to "
            "check and approve. None of them gives legal advice or replaces "
            "professional judgment. Each plugin's README states its jurisdiction, "
            "sources and currency limits."
        ),
        "",
        "Licence: MIT. See [LICENSE](../../LICENSE).",
    ]
    return "\n".join(lines) + "\n"


def bundle_sources(root: Path, plugins: list[dict[str, Any]]) -> dict[Path, Path]:
    """Map each bundle file to the plugin file it copies."""
    sources: dict[Path, Path] = {}
    for plugin in plugins:
        plugin_dir = root / "plugins" / plugin["name"]
        for tree in BUNDLE_TREES:
            for path in sorted((plugin_dir / tree).rglob("*")):
                relative = path.relative_to(plugin_dir)
                if (
                    not path.is_file()
                    or path.suffix == ".pyc"
                    or any(part in BUNDLE_SKIPPED for part in relative.parts)
                ):
                    continue
                target = root / BUNDLE_DIR / relative
                if target in sources:
                    raise GenerationError(
                        f"{describe(path)} and {describe(sources[target])} both map to "
                        f"{describe(target)} in the {BUNDLE_NAME} bundle; rename one"
                    )
                sources[target] = path
    return sources


def joined(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " or " + items[-1]


def evidence_states_region(states: dict[str, Any]) -> str:
    bullets = (
        EVIDENCE_STATE_VERIFIED,
        EVIDENCE_STATE_QUALIFIED.format(
            qualifications=joined(states["qualifications"])
        ),
        EVIDENCE_STATE_UNVERIFIED.format(unverifiable=joined(states["unverifiable"])),
        EVIDENCE_STATE_OUTSIDE,
    )
    lines = [EVIDENCE_STATES_HEADER, ""]
    for bullet in bullets:
        lines.extend(
            textwrap.wrap(
                f"- {bullet}",
                width=78,
                subsequent_indent="  ",
                break_on_hyphens=False,
                break_long_words=False,
            )
        )
    return "\n".join(lines)


def method_document(plugin: dict[str, Any]) -> str:
    path = plugin["method_path"]
    text = path.read_text(encoding="utf-8")
    region = evidence_states_region(plugin["catalog"]["evidenceStates"])
    return replace_region(text, "evidence-states", region, path.name)


def replace_region(text: str, region: str, content: str, path: str) -> str:
    begin = f"<!-- generated:{region} -->"
    end = f"<!-- end:{region} -->"
    start = text.find(begin)
    stop = text.find(end)
    if start == -1 or stop == -1 or stop < start:
        raise GenerationError(f"{path}: missing generated region markers for {region!r}")
    return text[: start + len(begin)] + "\n" + content + "\n" + text[stop:]


def root_readme(root: Path, plugins: list[dict[str, Any]], skill_count: int) -> str:
    path = root / "README.md"
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise GenerationError("README.md: missing") from exc
    regions = {
        "badges": badges_region(plugins, skill_count),
        "counts": counts_region(plugins, skill_count),
        "plugin-table": table_region(plugins),
        "install-agent": install_agent_region(plugins),
        "install-codex": install_codex_region(plugins),
        "install-claude": install_claude_region(plugins),
        "install-bundle": install_bundle_region(),
    }
    for region, content in regions.items():
        text = replace_region(text, region, content, "README.md")
    return text


ROUTER_PLUGIN = "legal-workflow-router"
DESCRIPTION_LINE = re.compile(r"^description:\s*(.+)$", re.M)


def skill_map(root: Path, plugins: list[dict[str, Any]]) -> str:
    """Generated reference for the router: every shipped skill with its trigger text."""
    lines = [
        "<!-- GENERATED FILE - do not edit. Built from each SKILL.md description by",
        "     scripts/generate_registry.py -->",
        "",
        "# Skill map",
        "",
        "Every skill the router may name, grouped by plugin. The description is the",
        "skill's own trigger text: what it does, when to use it and when not to.",
        "",
    ]
    for plugin in plugins:
        if plugin["name"] == ROUTER_PLUGIN:
            continue
        lines.append(f"## {plugin['catalog']['displayName']} (`{plugin['name']}`)")
        lines.append("")
        summary = dependency_summary(plugin["dependencies"])
        if summary:
            lines.extend(wrap_paragraph(f"Plugin dependencies: {summary[0].upper()}{summary[1:]}."))
            lines.append("")
        for skill in plugin["skills"]:
            text = (root / "plugins" / plugin["name"] / "skills" / skill / "SKILL.md").read_text(
                encoding="utf-8"
            )
            match = DESCRIPTION_LINE.search(text)
            if not match:
                raise GenerationError(f"{plugin['name']}/skills/{skill}/SKILL.md: missing description")
            lines.append(f"- **`{skill}`** — {match.group(1).strip()}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


DEPENDENCY_REGION = "plugin-dependencies"
SCANNED_SUFFIXES = (".md", ".json")


def strip_region(text: str, region: str) -> str:
    begin = f"<!-- generated:{region} -->"
    end = f"<!-- end:{region} -->"
    start = text.find(begin)
    stop = text.find(end)
    if start == -1 and stop == -1:
        return text
    if start == -1 or stop == -1 or stop < start:
        raise GenerationError(f"unbalanced generated region markers for {region!r}")
    return text[:start] + text[stop + len(end):]


def stamp_trailing_region(text: str, region: str, content: str | None) -> str:
    """Own a region at the end of a hand-written file: add, refresh or remove it."""
    body = strip_region(text, region).rstrip("\n") + "\n"
    if content is None:
        return body
    return f"{body}\n<!-- generated:{region} -->\n{content}\n<!-- end:{region} -->\n"


def referenced_skills(files: list[Path], owners: dict[str, str], plugin: str) -> dict[str, set[str]]:
    """Other plugins' skills named in the given files, grouped by owning plugin."""
    found: dict[str, set[str]] = {}
    for path in files:
        text = strip_region(path.read_text(encoding="utf-8"), DEPENDENCY_REGION)
        for skill, owner in owners.items():
            if owner != plugin and re.search(rf"(?<![\w-]){re.escape(skill)}(?![\w-])", text):
                found.setdefault(owner, set()).add(skill)
    return found


def scanned_files(directory: Path) -> list[Path]:
    return sorted(
        path
        for path in directory.rglob("*")
        if path.is_file()
        and path.suffix in SCANNED_SUFFIXES
        and path.name != "catalog.json"
        and not any(part in (".claude-plugin", ".codex-plugin") for part in path.parts)
    )


def plugin_dependencies(root: Path, plugins: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Derive each plugin's cross-plugin skill references and check them against catalog.json.

    The router is exempt: it names every skill by design and never invokes one.
    """
    owners = {skill: plugin["name"] for plugin in plugins for skill in plugin["skills"]}
    names = set(owners.values())
    result: dict[str, dict[str, Any]] = {}
    for plugin in plugins:
        name = plugin["name"]
        declared = plugin["dependencies"]
        declared_names = set(declared["requires"]) | set(declared["handsOffTo"])
        if name == ROUTER_PLUGIN:
            if declared_names:
                raise GenerationError(f"{name}/catalog.json: the router declares no dependencies")
            continue
        plugin_dir = root / "plugins" / name
        unknown = sorted(declared_names - names - {name})
        if unknown or name in declared_names:
            raise GenerationError(
                f"{name}/catalog.json: dependencies name unknown or self plugin(s) "
                f"{unknown or [name]}"
            )
        used = referenced_skills(scanned_files(plugin_dir), owners, name)
        undeclared = sorted(set(used) - declared_names)
        if undeclared:
            raise GenerationError(
                f"{name}: names skills from {undeclared} but catalog.json does not declare "
                "them under requires or handsOffTo"
            )
        unused = sorted(declared_names - set(used))
        if unused:
            raise GenerationError(
                f"{name}/catalog.json: declares {unused} but no file in the plugin names "
                "one of their skills"
            )
        per_skill = {
            skill: referenced_skills(scanned_files(plugin_dir / "skills" / skill), owners, name)
            for skill in plugin["skills"]
        }
        result[name] = {"declared": declared, "per_skill": per_skill}
    return result


def dependency_lines(declared: dict[str, dict[str, str]], used: dict[str, set[str]]) -> list[str]:
    lines = []
    for field, label in DEPENDENCY_KINDS.items():
        for other, reason in declared[field].items():
            if other not in used:
                continue
            skills = ", ".join(f"`{skill}`" for skill in sorted(used[other]))
            lines.extend(
                textwrap.wrap(
                    f"- `{other}` ({label}): {skills}. {reason}",
                    width=78,
                    subsequent_indent="  ",
                    break_on_hyphens=False,
                    break_long_words=False,
                )
            )
    return lines


MISSING_PLUGIN_RULE = (
    "If a named skill is not available in this session, say so and name the "
    "plugin to install. Treat the step it would have performed as not done: "
    "record the affected proposition as not verified, or the hand-off as not "
    "made. Never perform that step from memory or substitute a different skill."
)


def wrap_paragraph(text: str) -> list[str]:
    return textwrap.wrap(text, width=78, break_on_hyphens=False, break_long_words=False)


def skill_dependency_section(declared: dict[str, dict[str, str]], used: dict[str, set[str]]) -> str | None:
    if not used:
        return None
    lines = [
        "## Other plugins",
        "",
        *wrap_paragraph(
            "This skill names skills from other Legal Skills plugins. Install a "
            "required plugin alongside this one; install a hand-off plugin when "
            "the matter needs that depth."
        ),
        "",
        *dependency_lines(declared, used),
        "",
        *wrap_paragraph(MISSING_PLUGIN_RULE),
    ]
    return "\n".join(lines)


def readme_dependency_section(declared: dict[str, dict[str, str]]) -> str | None:
    if not any(declared[field] for field in DEPENDENCY_KINDS):
        return None
    lines = ["## Plugin dependencies", ""]
    for field, label in DEPENDENCY_KINDS.items():
        for other, reason in declared[field].items():
            lines.extend(
                textwrap.wrap(
                    f"- `{other}` ({label}) — {reason}",
                    width=78,
                    subsequent_indent="  ",
                    break_on_hyphens=False,
                    break_long_words=False,
                )
            )
    lines += [
        "",
        *wrap_paragraph(
            "Install every required plugin with this one. A skill whose required "
            "or hand-off plugin is missing reports the step as not done rather "
            "than performing it from memory."
        ),
    ]
    return "\n".join(lines)


def dependency_summary(declared: dict[str, dict[str, str]]) -> str:
    parts = []
    for field, label in (("requires", "requires"), ("handsOffTo", "hands off to")):
        if declared[field]:
            parts.append(f"{label} " + ", ".join(f"`{other}`" for other in declared[field]))
    return "; ".join(parts)


def generate(root: Path = ROOT, copies: dict[Path, Path] | None = None) -> dict[Path, str]:
    """Build every generated file. Bundle copies are also recorded in ``copies``
    (bundle path -> plugin path) so apply and check can mirror the file mode."""
    plugins = load_plugins(root)
    skill_count = sum(len(plugin["skills"]) for plugin in plugins)
    dependencies = plugin_dependencies(root, plugins)
    outputs: dict[Path, str] = {}
    for plugin in plugins:
        plugin_dir = root / "plugins" / plugin["name"]
        if plugin["name"] in dependencies:
            found = dependencies[plugin["name"]]
            readme = plugin_dir / "README.md"
            if readme.is_file():
                outputs[readme] = stamp_trailing_region(
                    readme.read_text(encoding="utf-8"),
                    DEPENDENCY_REGION,
                    readme_dependency_section(found["declared"]),
                )
            for skill, used in found["per_skill"].items():
                skill_file = plugin_dir / "skills" / skill / "SKILL.md"
                outputs[skill_file] = stamp_trailing_region(
                    skill_file.read_text(encoding="utf-8"),
                    DEPENDENCY_REGION,
                    skill_dependency_section(found["declared"], used),
                )
        outputs[plugin_dir / ".claude-plugin" / "plugin.json"] = dumps(claude_manifest(plugin))
        outputs[plugin_dir / ".codex-plugin" / "plugin.json"] = dumps(codex_manifest(plugin))
        if plugin["method_path"] is not None:
            outputs[plugin["method_path"]] = method_document(plugin)
    outputs[root / ".claude-plugin" / "marketplace.json"] = dumps(claude_marketplace(plugins))
    bundle = bundle_plugin(plugins, skill_count)
    outputs[root / ".agents" / "plugins" / "marketplace.json"] = dumps(
        agents_marketplace(plugins, bundle)
    )
    if (root / "plugins" / ROUTER_PLUGIN).is_dir():
        outputs[root / "plugins" / ROUTER_PLUGIN / "references" / "skill-map.md"] = skill_map(root, plugins)
    outputs[root / "plugins" / "README.md"] = plugins_readme(plugins)
    outputs[root / "README.md"] = root_readme(root, plugins, skill_count)
    sources = bundle_sources(root, plugins)
    for target, source in sources.items():
        # A plugin file this run regenerates is copied in its regenerated form.
        outputs[target] = outputs.get(source) or source.read_text(encoding="utf-8")
    bundle_dir = root / BUNDLE_DIR
    outputs[bundle_dir / ".codex-plugin" / "plugin.json"] = dumps(bundle_manifest(bundle, plugins))
    outputs[bundle_dir / "README.md"] = bundle_readme(bundle, plugins, skill_count)
    if copies is not None:
        copies.update(sources)
    return outputs


def is_executable(path: Path) -> bool:
    return bool(path.stat().st_mode & stat.S_IXUSR)


def orphans(outputs: dict[Path, str]) -> list[Path]:
    """Files in a generated bundle that no plugin file produces any more."""
    manifest = Path(".codex-plugin") / "plugin.json"
    bundle_dirs = [
        path.parents[1]
        for path in outputs
        if path.parts[-len(BUNDLE_DIR.parts) - 2:] == (*BUNDLE_DIR.parts, *manifest.parts)
    ]
    return sorted(
        path
        for bundle_dir in bundle_dirs
        if bundle_dir.is_dir()
        for path in bundle_dir.rglob("*")
        if path.is_file()
        and path not in outputs
        and path.suffix != ".pyc"
        and not any(part in BUNDLE_SKIPPED for part in path.parts)
    )


def mode_differs(path: Path, copies: dict[Path, Path]) -> bool:
    return path in copies and is_executable(path) != is_executable(copies[path])


def apply(outputs: dict[Path, str], copies: dict[Path, Path] | None = None) -> list[Path]:
    copies = copies or {}
    changed = []
    for path, content in sorted(outputs.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            changed.append(path)
        if mode_differs(path, copies):
            path.chmod(copies[path].stat().st_mode)
            if path not in changed:
                changed.append(path)
    for path in orphans(outputs):
        path.unlink()
        changed.append(path)
    return changed


def check(outputs: dict[Path, str], copies: dict[Path, Path] | None = None) -> list[Path]:
    copies = copies or {}
    stale = [
        path
        for path, content in sorted(outputs.items())
        if not path.is_file()
        or path.read_text(encoding="utf-8") != content
        or mode_differs(path, copies)
    ]
    return stale + orphans(outputs)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated files are current instead of writing them",
    )
    args = parser.parse_args(argv)
    copies: dict[Path, Path] = {}
    try:
        outputs = generate(copies=copies)
    except GenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.check:
        stale = check(outputs, copies)
        if stale:
            for path in stale:
                print(f"STALE: {path.relative_to(ROOT)}", file=sys.stderr)
            print(
                "Generated files are out of date. Run: python3 scripts/generate_registry.py",
                file=sys.stderr,
            )
            return 1
        print(f"All {len(outputs)} generated file(s) are current.")
        return 0
    changed = apply(outputs, copies)
    for path in changed:
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"Generated {len(outputs)} file(s); {len(changed)} changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
