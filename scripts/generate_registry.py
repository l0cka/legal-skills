#!/usr/bin/env python3
"""Generate the Legal Skills distribution surfaces from the canonical sources.

Canonical, hand-edited sources per plugin:
  plugins/<name>/.claude-plugin/plugin.json  (name, version, description, keywords)
  plugins/<name>/catalog.json                (displayName, shortDescription,
                                              longDescription, defaultPrompt,
                                              whatItDoes, boundaries)
  plugins/<name>/skills/<skill>/...          (the skill packages)
  skills.json                                (per-skill `source` provenance only)

Everything else this script writes is machine-owned: do not edit those files
by hand. Run with --check (CI does) to fail when any generated file is stale.
"""

from __future__ import annotations

import argparse
import json
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
TARGETS = ["claude-cowork", "chatgpt-work"]
TARGETS_BADGE = (
    '  <img alt="Claude Cowork and ChatGPT Work" '
    'src="https://img.shields.io/badge/works%20with-'
    'Claude%20Cowork%20%2B%20ChatGPT%20Work-c59a46?style=flat-square">'
)

MANIFEST_DATA_FIELDS = ("name", "version", "description", "keywords")
CATALOG_STRING_FIELDS = ("displayName", "shortDescription", "longDescription")
CATALOG_LIST_FIELDS = ("defaultPrompt", "whatItDoes", "boundaries")
EVIDENCE_STATE_KEYS = ("qualifications", "unverifiable")

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


def load_plugin(plugin_dir: Path) -> dict[str, Any]:
    manifest = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
    for field in MANIFEST_DATA_FIELDS:
        value = manifest.get(field)
        ok = isinstance(value, list) and value if field == "keywords" else (
            isinstance(value, str) and value.strip()
        )
        if not ok:
            raise GenerationError(
                f"{plugin_dir.name}/.claude-plugin/plugin.json: field {field!r} is required"
            )
    catalog = load_json(plugin_dir / "catalog.json")
    for field in CATALOG_STRING_FIELDS:
        if not isinstance(catalog.get(field), str) or not catalog[field].strip():
            raise GenerationError(f"{plugin_dir.name}/catalog.json: field {field!r} is required")
    for field in CATALOG_LIST_FIELDS:
        value = catalog.get(field)
        if (
            not isinstance(value, list)
            or not value
            or not all(isinstance(item, str) and item.strip() for item in value)
        ):
            raise GenerationError(
                f"{plugin_dir.name}/catalog.json: field {field!r} must be a "
                "non-empty array of strings"
            )
    states = catalog.get("evidenceStates")
    method_path = None
    if states is not None:
        for key in EVIDENCE_STATE_KEYS:
            value = states.get(key) if isinstance(states, dict) else None
            if (
                not isinstance(value, list)
                or not value
                or not all(isinstance(item, str) and item.strip() for item in value)
            ):
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
    }


def load_plugins(root: Path) -> list[dict[str, Any]]:
    plugin_dirs = sorted(
        path
        for path in (root / "plugins").iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    plugins = [load_plugin(path) for path in plugin_dirs]
    for plugin, path in zip(plugins, plugin_dirs):
        if plugin["name"] != path.name:
            raise GenerationError(
                f"{path.name}/.claude-plugin/plugin.json: name must equal the directory name"
            )
    return plugins


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


def agents_marketplace(plugins: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "name": MARKETPLACE_NAME,
        "interface": {
            "displayName": MARKETPLACE_DISPLAY_NAME,
            "description": MARKETPLACE_DESCRIPTION,
        },
        "plugins": [
            {
                "name": plugin["name"],
                "source": {"source": "local", "path": f"./plugins/{plugin['name']}"},
                "policy": POLICY,
                "category": CATEGORY,
                "description": plugin["description"],
                "version": plugin["version"],
                "keywords": plugin["keywords"],
            }
            for plugin in plugins
        ],
    }


def skills_registry(root: Path, plugins: list[dict[str, Any]]) -> dict[str, Any]:
    existing: dict[str, str] = {}
    registry_path = root / "skills.json"
    if registry_path.is_file():
        for entry in load_json(registry_path).get("skills", []):
            if isinstance(entry, dict) and isinstance(entry.get("name"), str):
                existing[entry["name"]] = entry.get("source", "")
    entries = []
    for plugin in plugins:
        for skill in plugin["skills"]:
            entries.append(
                {
                    "name": skill,
                    "path": f"plugins/{plugin['name']}/skills/{skill}",
                    "plugin": f"plugins/{plugin['name']}",
                    "plugin_version": plugin["version"],
                    "targets": TARGETS,
                    # Provenance is the one hand-written registry field. A new
                    # skill is scaffolded with "" and validation fails closed
                    # until a human records where the workflow came from.
                    "source": existing.get(skill, ""),
                }
            )
    entries.sort(key=lambda entry: entry["path"])
    return {"registry_version": 1, "skills": entries}


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
        entry = (
            f"- [**{plugin['catalog']['displayName']}**]({plugin['name']}/README.md) — "
            f"{plugin['catalog']['shortDescription']}"
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
        "| Plugin | Skills | What it does | Boundaries |",
        "| --- | :---: | --- | --- |",
    ]
    for plugin in plugins:
        catalog = plugin["catalog"]
        does = "".join(f"<li>{item}</li>" for item in catalog["whatItDoes"])
        bounds = "".join(f"<li>{item}</li>" for item in catalog["boundaries"])
        lines.append(
            f"| [**{catalog['displayName']}**](plugins/{plugin['name']}/README.md) "
            f"| {len(plugin['skills'])} | <ul>{does}</ul> | <ul>{bounds}</ul> |"
        )
    return "\n".join(lines)


def install_agent_region(plugins: list[dict[str, Any]]) -> str:
    names = [f"`{plugin['name']}`" for plugin in plugins]
    listed = ", ".join(names[:-1]) + f", and {names[-1]}"
    word = number_word(len(plugins))
    request = (
        f"Add the plugin marketplace `{OWNER}/{MARKETPLACE_NAME}`, then install "
        f"its {word} plugins: {listed} (all `@{MARKETPLACE_NAME}`, user scope if "
        f"supported). Leave other marketplaces and plugins unchanged. Verify all "
        f"{word} are available and report the result. If you cannot manage "
        f"plugins, give me the exact manual steps and stop."
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
    }
    for region, content in regions.items():
        text = replace_region(text, region, content, "README.md")
    return text


def generate(root: Path = ROOT) -> dict[Path, str]:
    plugins = load_plugins(root)
    skill_count = sum(len(plugin["skills"]) for plugin in plugins)
    outputs: dict[Path, str] = {}
    for plugin in plugins:
        plugin_dir = root / "plugins" / plugin["name"]
        outputs[plugin_dir / ".claude-plugin" / "plugin.json"] = dumps(claude_manifest(plugin))
        outputs[plugin_dir / ".codex-plugin" / "plugin.json"] = dumps(codex_manifest(plugin))
        if plugin["method_path"] is not None:
            outputs[plugin["method_path"]] = method_document(plugin)
    outputs[root / ".claude-plugin" / "marketplace.json"] = dumps(claude_marketplace(plugins))
    outputs[root / ".agents" / "plugins" / "marketplace.json"] = dumps(
        agents_marketplace(plugins)
    )
    outputs[root / "skills.json"] = dumps(skills_registry(root, plugins))
    outputs[root / "plugins" / "README.md"] = plugins_readme(plugins)
    outputs[root / "README.md"] = root_readme(root, plugins, skill_count)
    return outputs


def apply(outputs: dict[Path, str]) -> list[Path]:
    changed = []
    for path, content in sorted(outputs.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            path.write_text(content, encoding="utf-8")
            changed.append(path)
    return changed


def check(outputs: dict[Path, str]) -> list[Path]:
    return [
        path
        for path, content in sorted(outputs.items())
        if not path.is_file() or path.read_text(encoding="utf-8") != content
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify generated files are current instead of writing them",
    )
    args = parser.parse_args(argv)
    try:
        outputs = generate()
    except GenerationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    if args.check:
        stale = check(outputs)
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
    changed = apply(outputs)
    for path in changed:
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"Generated {len(outputs)} file(s); {len(changed)} changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
