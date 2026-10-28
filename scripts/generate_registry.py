#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

PLUGIN_NAME = "legal-skills"
MARKETPLACE_NAME = "legal-skills"
MARKETPLACE_DISPLAY_NAME = "Legal Skills"
MARKETPLACE_DESCRIPTION = "Open-source, governed legal workflow plugin maintained by l0cka."
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
ROUTER_AREA = "workflow-router"

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DESCRIPTION_LINE = re.compile(r"^description:\s*(.+)$", re.M)
MANIFEST_DATA_FIELDS = ("name", "version", "description", "keywords")
CATALOG_STRING_FIELDS = ("displayName", "shortDescription", "longDescription")
CATALOG_LIST_FIELDS = ("defaultPrompt", "whatItDoes", "boundaries")
AREA_STRING_FIELDS = ("id", "displayName", "shortDescription", "lawCheckedOn")
EVIDENCE_STATE_KEYS = ("qualifications", "unverifiable")

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
    pass


def describe(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def number_word(value: int) -> str:
    if not 0 <= value <= 999:
        raise GenerationError(f"number_word supports 0-999, got {value}")
    hundreds, rest = divmod(value, 100)
    if hundreds:
        word = f"{ONES[hundreds]} hundred"
        return f"{word} and {number_word(rest)}" if rest else word
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


def load_area(plugin_dir: Path, area: Any, index: int) -> dict[str, Any]:
    where = f"{plugin_dir.name}/catalog.json areas[{index}]"
    if not isinstance(area, dict):
        raise GenerationError(f"{where}: must be an object")
    for field in AREA_STRING_FIELDS:
        if not is_text(area.get(field)):
            raise GenerationError(f"{where}: field {field!r} is required")
    if not SLUG.fullmatch(area["id"]):
        raise GenerationError(f"{where}: id must be lowercase and hyphenated")
    if not is_text_list(area.get("skills")):
        raise GenerationError(f"{where}: skills must be a non-empty array of skill names")
    states = area.get("evidenceStates")
    method = area.get("methodDocument")
    if (states is None) != (method is None):
        raise GenerationError(f"{where}: evidenceStates and methodDocument go together")
    if states is not None:
        for key in EVIDENCE_STATE_KEYS:
            if not isinstance(states, dict) or not is_text_list(states.get(key)):
                raise GenerationError(
                    f"{where}: evidenceStates.{key} must be a non-empty array of strings"
                )
        if not (plugin_dir / "references" / method).is_file():
            raise GenerationError(f"{where}: methodDocument references/{method} not found")
    return area


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
    raw_areas = catalog.get("areas")
    if not isinstance(raw_areas, list) or not raw_areas:
        raise GenerationError(f"{plugin_dir.name}/catalog.json: areas must be a non-empty array")
    areas = [load_area(plugin_dir, area, index) for index, area in enumerate(raw_areas)]
    ids = [area["id"] for area in areas]
    if len(set(ids)) != len(ids):
        raise GenerationError(f"{plugin_dir.name}/catalog.json: duplicate area id")
    skills = sorted(path.parent.name for path in (plugin_dir / "skills").glob("*/SKILL.md"))
    if not skills:
        raise GenerationError(f"{plugin_dir.name}: no skills found under skills/")
    assigned = [skill for area in areas for skill in area["skills"]]
    duplicated = sorted({skill for skill in assigned if assigned.count(skill) > 1})
    if duplicated:
        raise GenerationError(f"{plugin_dir.name}/catalog.json: skills in more than one area {duplicated}")
    unassigned = sorted(set(skills) - set(assigned))
    if unassigned:
        raise GenerationError(f"{plugin_dir.name}/catalog.json: skills in no area {unassigned}")
    unknown = sorted(set(assigned) - set(skills))
    if unknown:
        raise GenerationError(f"{plugin_dir.name}/catalog.json: areas name unknown skills {unknown}")
    return {
        "name": manifest["name"],
        "version": manifest["version"],
        "description": manifest["description"],
        "keywords": manifest["keywords"],
        "catalog": catalog,
        "areas": areas,
        "skills": skills,
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


def all_areas(plugins: list[dict[str, Any]]) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    return [(plugin, area) for plugin in plugins for area in plugin["areas"]]


def badges_region(area_count: int, skill_count: int) -> str:
    area_word = number_word(area_count).capitalize()
    skill_word = number_word(skill_count).capitalize()
    return "\n".join(
        [
            f'  <img alt="{area_word} practice areas" '
            f'src="https://img.shields.io/badge/practice%20areas-{area_count}-31547a?style=flat-square">',
            f'  <img alt="{skill_word} skills" '
            f'src="https://img.shields.io/badge/skills-{skill_count}-31547a?style=flat-square">',
            TARGETS_BADGE,
        ]
    )


def counts_region(area_count: int, skill_count: int) -> str:
    return (
        f"One plugin, `{PLUGIN_NAME}`, holds {number_word(skill_count)} skills "
        f"across {number_word(area_count)} practice areas:"
    )


def area_table(plugins: list[dict[str, Any]], link_prefix: str) -> str:
    lines = [
        "| Practice area | Skills | Description | Law checked |",
        "| --- | :---: | --- | :---: |",
    ]
    for plugin, area in all_areas(plugins):
        prefix = link_prefix.format(plugin=plugin["name"])
        lines.append(
            f"| [**{area['displayName']}**]({prefix}areas/{area['id']}/README.md) "
            f"| {len(area['skills'])} | {area['shortDescription']} "
            f"| {area['lawCheckedOn']} |"
        )
    return "\n".join(lines)


def install_agent_region() -> str:
    request = (
        f"Add the plugin marketplace `{OWNER}/{MARKETPLACE_NAME}` and install "
        f"its `{PLUGIN_NAME}` plugin (user scope if supported). Verify the "
        f"plugin is available and report the result."
    )
    wrapped = textwrap.wrap(request, width=74, break_on_hyphens=False, break_long_words=False)
    return "```text\n" + "\n".join(wrapped) + "\n```"


def install_codex_region(plugins: list[dict[str, Any]]) -> str:
    lines = [f"codex plugin marketplace add {OWNER}/{MARKETPLACE_NAME}"]
    lines += [f"codex plugin add {plugin['name']}@{MARKETPLACE_NAME}" for plugin in plugins]
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
        EVIDENCE_STATE_QUALIFIED.format(qualifications=joined(states["qualifications"])),
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


def replace_region(text: str, region: str, content: str, path: str) -> str:
    begin = f"<!-- generated:{region} -->"
    end = f"<!-- end:{region} -->"
    start = text.find(begin)
    stop = text.find(end)
    if start == -1 or stop == -1 or stop < start:
        raise GenerationError(f"{path}: missing generated region markers for {region!r}")
    return text[: start + len(begin)] + "\n" + content + "\n" + text[stop:]


def read_required(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise GenerationError(f"{describe(path)}: missing") from exc


def root_readme(root: Path, plugins: list[dict[str, Any]]) -> str:
    area_count = sum(len(plugin["areas"]) for plugin in plugins)
    skill_count = sum(len(plugin["skills"]) for plugin in plugins)
    text = read_required(root / "README.md")
    regions = {
        "badges": badges_region(area_count, skill_count),
        "counts": counts_region(area_count, skill_count),
        "area-table": area_table(plugins, "plugins/{plugin}/"),
        "install-agent": install_agent_region(),
        "install-codex": install_codex_region(plugins),
        "install-claude": install_claude_region(plugins),
    }
    for region, content in regions.items():
        text = replace_region(text, region, content, "README.md")
    return text


def plugin_readme(root: Path, plugin: dict[str, Any]) -> str:
    path = root / "plugins" / plugin["name"] / "README.md"
    return replace_region(read_required(path), "area-table", area_table([plugin], ""), describe(path))


def skill_description(root: Path, plugin: str, skill: str) -> str:
    text = (root / "plugins" / plugin / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    match = DESCRIPTION_LINE.search(text)
    if not match:
        raise GenerationError(f"{plugin}/skills/{skill}/SKILL.md: missing description")
    return match.group(1).strip()


def skill_map(root: Path, plugin: dict[str, Any]) -> str:
    lines = [
        "<!-- GENERATED FILE - do not edit. Built from each SKILL.md description by",
        "     scripts/generate_registry.py -->",
        "",
        "# Skill map",
        "",
        "Every skill the router may name, grouped by practice area. The description",
        "is the skill's own trigger text: what it does, when to use it and when not to.",
        "",
    ]
    for area in plugin["areas"]:
        if area["id"] == ROUTER_AREA:
            continue
        lines += [f"## {area['displayName']} (`{area['id']}`)", ""]
        for skill in area["skills"]:
            lines.append(f"- **`{skill}`** — {skill_description(root, plugin['name'], skill)}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate(root: Path = ROOT) -> dict[Path, str]:
    plugins = load_plugins(root)
    outputs: dict[Path, str] = {}
    for plugin in plugins:
        plugin_dir = root / "plugins" / plugin["name"]
        outputs[plugin_dir / ".claude-plugin" / "plugin.json"] = dumps(claude_manifest(plugin))
        outputs[plugin_dir / ".codex-plugin" / "plugin.json"] = dumps(codex_manifest(plugin))
        outputs[plugin_dir / "README.md"] = plugin_readme(root, plugin)
        for area in plugin["areas"]:
            if "methodDocument" in area:
                method = plugin_dir / "references" / area["methodDocument"]
                outputs[method] = replace_region(
                    method.read_text(encoding="utf-8"),
                    "evidence-states",
                    evidence_states_region(area["evidenceStates"]),
                    method.name,
                )
        if any(area["id"] == ROUTER_AREA for area in plugin["areas"]):
            outputs[plugin_dir / "references" / "skill-map.md"] = skill_map(root, plugin)
    outputs[root / ".claude-plugin" / "marketplace.json"] = dumps(claude_marketplace(plugins))
    outputs[root / ".agents" / "plugins" / "marketplace.json"] = dumps(agents_marketplace(plugins))
    outputs[root / "README.md"] = root_readme(root, plugins)
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
    parser = argparse.ArgumentParser(
        description="Generate the Legal Skills distribution surfaces from the canonical sources."
    )
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
