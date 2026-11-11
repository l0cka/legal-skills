#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ai_tool_workbooks  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "legal-skills"
TEMPLATES = PLUGIN / "ai-tool"
TOP = "legal-skills"
SECTION_HEADING = "## AI-tool mode"
NO_CODE_DIR = "no-code"
NO_CODE_NAME = "no-code.md"
NO_CODE_LINE = f"Follow the [no-code procedure]({NO_CODE_NAME}) for this skill.\n\n"
CODE_REGION = re.compile(
    r"^[ \t]*<!-- ai-tool:code -->.*?<!-- /ai-tool:code -->[ \t]*\n?|<!-- ai-tool:code -->.*?<!-- /ai-tool:code -->",
    re.DOTALL | re.MULTILINE,
)
GENERATED_HEADER = re.compile(r"\A<!-- GENERATED FILE.*?-->\n", re.DOTALL)
BUNDLE_TEXT = re.compile(r"<!-- ai-tool:bundle: (.*?) -->", re.DOTALL)
HASH_WORDS = re.compile(r"\bsha-?256\b|\bfingerprint\w*|\bhash\w*", re.IGNORECASE)
COMPUTE_HASH = re.compile(r"\b(?:compute|calculate|generate|capture|produce)\b[^.\n]*(?:sha-?256|fingerprint|hash)", re.IGNORECASE)
NEGATED = re.compile(r"\bnot\b|\bnever\b|\bno\b", re.IGNORECASE)
JSON_CODE_WORDS = re.compile(r"\.py\b|python|\bscripts/", re.IGNORECASE)
HASH_ALLOWED = ("not computed", "never state, estimate")
HASH_FACT_FILES = {"skills/format-aglc4-citations/references/source-map.md"}
ANY_MARKER = re.compile(r"<!--\s*/?ai-tool:")
CODE_WORDS = re.compile(r"\bscripts?\b|\.py\b|python", re.IGNORECASE)
EXCLUDED_TOPS = {
    "evals", "benchmarks", "tests", "scripts", "docs", "plugins", "areas", "agents",
    ".claude-plugin", ".codex-plugin", ".cursor-plugin", ".github",
}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}
SKIP_DIRS = {"__pycache__", "scripts", "agents", "evals"}
MARKDOWN_LINK = re.compile(r"\]\(([^)\s]+)")
PATH_TOKEN = re.compile(r"[A-Za-z0-9_.~<>*-]*/[A-Za-z0-9_.~/<>*-]*")
FRONT_DESCRIPTION = re.compile(r"^description:\s*(.*)$", re.MULTILINE)
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
ENTRY_FULL = (
    "Match the task to one skill below. If several apply, start with\n"
    "   `route-legal-fact-pattern`, which orders them. For any case citation start\n"
    "   with `route-case-citation`."
)
ENTRY_AREA = (
    "Match the task to one skill below. This zip holds one practice area; skills\n"
    "   from other areas are in the full bundle."
)
INLINE_LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")


class BundleError(Exception):
    pass


def load_catalog() -> dict:
    return json.loads((PLUGIN / "catalog.json").read_text(encoding="utf-8"))


def plugin_version() -> str:
    manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    return manifest["version"]


def script_backed_skills(plugin: Path = PLUGIN) -> list[str]:
    return sorted(p.parent.name for p in (plugin / "skills").glob("*/scripts") if p.is_dir())


def code_dependent_skills(plugin: Path = PLUGIN) -> list[str]:
    return sorted(
        path.parent.name
        for path in (plugin / "skills").glob("*/SKILL.md")
        if SECTION_HEADING in path.read_text(encoding="utf-8")
    )


def no_code_problems(plugin: Path) -> list[str]:
    folder = plugin / "ai-tool" / NO_CODE_DIR
    needed = set(code_dependent_skills(plugin))
    present = {path.stem for path in folder.glob("*.md")} if folder.is_dir() else set()
    problems = [f"skills/{skill}/SKILL.md: has an AI-tool mode section but no ai-tool/{NO_CODE_DIR}/{skill}.md replacement" for skill in sorted(needed - present)]
    problems += [f"ai-tool/{NO_CODE_DIR}/{skill}.md: no skill with an AI-tool mode section has this name" for skill in sorted(present - needed)]
    return problems


def source_problems(plugin: Path = PLUGIN) -> list[str]:
    problems: list[str] = no_code_problems(plugin)
    for skill in script_backed_skills(plugin):
        path = plugin / "skills" / skill / "SKILL.md"
        text = path.read_text(encoding="utf-8") if path.is_file() else ""
        if SECTION_HEADING not in text:
            problems.append(f"skills/{skill}/SKILL.md: has scripts but no '{SECTION_HEADING}' section")
        if "<!-- ai-tool:code -->" not in text:
            problems.append(f"skills/{skill}/SKILL.md: has scripts but marks no code-only passage with ai-tool:code")
    for path in sorted((plugin / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        if "<!-- ai-tool:code -->" in text and SECTION_HEADING not in text:
            problems.append(f"{path.relative_to(plugin)}: marks code-only passages but has no '{SECTION_HEADING}' section")
    for path in sorted(plugin.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if text.count("<!-- ai-tool:code -->") != text.count("<!-- /ai-tool:code -->"):
            problems.append(f"{path.relative_to(plugin)}: unbalanced ai-tool:code markers")
    return problems


def skill_description(skill: str) -> str:
    text = (PLUGIN / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    match = FRONT_DESCRIPTION.search(text.split("\n---\n", 1)[0])
    if not match:
        raise BundleError(f"skills/{skill}/SKILL.md: no description")
    return match.group(1).strip().strip("\"'")


def strip_code_regions(text: str) -> str:
    return GENERATED_HEADER.sub("", BUNDLE_TEXT.sub(r"\1", CODE_REGION.sub("", text)))


def link_no_code(text: str) -> str:
    return re.sub(rf"^{re.escape(SECTION_HEADING)}\n\n", lambda m: m.group(0) + NO_CODE_LINE, text, count=1, flags=re.MULTILINE)


def tree_files(base: Path, rel_prefix: str) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    for path in sorted(base.rglob("*")):
        parts = path.relative_to(base).parts
        if not path.is_file() or path.name in SKIP_NAMES or SKIP_DIRS & set(parts) or path.suffix == ".pyc":
            continue
        files[f"{rel_prefix}/{'/'.join(parts)}"] = path.read_bytes()
    return files


def render_router(areas: list[dict], version: str, whole: bool) -> str:
    blocks = []
    for area in areas:
        lines = [f"### {area['displayName']}", "", area["shortDescription"], ""]
        for skill in area["skills"]:
            line = f"- [`{skill}`](skills/{skill}/SKILL.md): {skill_description(skill)}"
            if (TEMPLATES / NO_CODE_DIR / f"{skill}.md").is_file():
                line += f" No-code: [procedure](skills/{skill}/{NO_CODE_NAME})."
            lines.append(line)
        blocks.append("\n".join(lines))
    template = (TEMPLATES / "ROUTER.template.md").read_text(encoding="utf-8")
    entry = ENTRY_FULL if whole else ENTRY_AREA
    return template.replace("{{version}}", version).replace("{{entry}}", entry).replace("{{areas}}", "\n\n".join(blocks))


def unlink_missing_skill_links(files: dict[str, bytes], elsewhere: set[str]) -> dict[str, bytes]:
    out = dict(files)
    for name, data in files.items():
        if not name.endswith(".md"):
            continue
        base_dir = name.rsplit("/", 1)[0] if "/" in name else ""

        def unlink(match: re.Match[str]) -> str:
            target = match.group(2).split("#", 1)[0]
            resolved = normalise(base_dir, target) if target and not re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) else None
            if resolved in elsewhere and resolved.startswith("skills/"):
                return match.group(1)
            return match.group(0)

        out[name] = INLINE_LINK.sub(unlink, data.decode("utf-8")).encode("utf-8")
    return out


def build_files(area: str | None = None, version: str | None = None) -> dict[str, bytes]:
    version = version or plugin_version()
    catalog = load_catalog()
    areas = catalog["areas"]
    if area is not None:
        areas = [a for a in areas if a["id"] == area]
        if not areas:
            raise BundleError(f"unknown practice area: {area}")
    skills = [skill for a in areas for skill in a["skills"]]

    files: dict[str, bytes] = {}
    for skill in skills:
        base = PLUGIN / "skills" / skill
        files[f"skills/{skill}/SKILL.md"] = (base / "SKILL.md").read_bytes()
        for sub in ("references", "assets"):
            if (base / sub).is_dir():
                files.update(tree_files(base / sub, f"skills/{skill}/{sub}"))
        no_code = TEMPLATES / NO_CODE_DIR / f"{skill}.md"
        if no_code.is_file():
            files[f"skills/{skill}/{NO_CODE_NAME}"] = no_code.read_bytes()
            files[f"skills/{skill}/SKILL.md"] = link_no_code(files[f"skills/{skill}/SKILL.md"].decode("utf-8")).encode("utf-8")
    files.update(tree_files(PLUGIN / "references", "references"))
    files.update(ai_tool_workbooks.bundle_workbooks(PLUGIN))
    for name in ("PRIVACY.md", "LICENSE"):
        files[name] = (PLUGIN / name).read_bytes()

    for name, data in list(files.items()):
        if name.endswith(".md"):
            files[name] = strip_code_regions(data.decode("utf-8")).encode("utf-8")

    if area is not None:
        files = unlink_missing_skill_links(files, set(build_files(None, version)) - set(files))

    scoped = dict(catalog, areas=areas)
    files["catalog.json"] = (json.dumps(scoped, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    files["ROUTER.md"] = render_router(areas, version, area is None).encode("utf-8")
    files["reference/firm/README.md"] = (TEMPLATES / "firm-README.md").read_bytes()
    files["VERSION"] = f"Legal Skills AI-tool bundle {version}\n".encode("utf-8")
    return files


def normalise(base_dir: str, target: str) -> str | None:
    parts: list[str] = []
    for seg in f"{base_dir}/{target}".split("/"):
        if seg in ("", "."):
            continue
        if seg == "..":
            if not parts:
                return None
            parts.pop()
        else:
            parts.append(seg)
    return "/".join(parts)


def check_files(files: dict[str, bytes]) -> list[str]:
    problems: list[str] = []
    names = set(files)
    for name in sorted(names):
        if not name.endswith(".md"):
            continue
        text = files[name].decode("utf-8")
        base_dir = name.rsplit("/", 1)[0] if "/" in name else ""
        if ANY_MARKER.search(text):
            problems.append(f"{name}: leftover ai-tool marker")
        in_ai_section = False
        for lineno, line in enumerate(text.splitlines(), 1):
            if line.startswith(SECTION_HEADING):
                in_ai_section = True
            elif line.startswith("## "):
                in_ai_section = False
            compute = COMPUTE_HASH.search(line)
            if compute and not NEGATED.search(line[: compute.start()]):
                problems.append(f"{name}:{lineno}: tells a no-code host to compute a hash or fingerprint: {line.strip()[:80]}")
            elif (
                HASH_WORDS.search(line)
                and not in_ai_section
                and name not in HASH_FACT_FILES
                and not any(phrase in line for phrase in HASH_ALLOWED)
            ):
                problems.append(f"{name}:{lineno}: tells a no-code host to compute a hash or fingerprint: {line.strip()[:80]}")
            if CODE_WORDS.search(line):
                problems.append(f"{name}:{lineno}: references code or a script: {line.strip()[:80]}")
            for target in MARKDOWN_LINK.findall(line):
                target = target.split("#", 1)[0]
                if not target or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                    continue
                resolved = normalise(base_dir, target.lstrip("/")) if not target.startswith("/") else normalise("", target)
                is_dir_ok = resolved is not None and any(n.startswith(resolved.rstrip("/") + "/") for n in names)
                if resolved is None or (resolved not in names and not is_dir_ok):
                    problems.append(f"{name}:{lineno}: link does not resolve inside the bundle: {target}")
            stripped = re.sub(r"\]\([^)]*\)", "]", line)
            for token in PATH_TOKEN.findall(stripped):
                if token.split("/", 1)[0] in EXCLUDED_TOPS:
                    problems.append(f"{name}:{lineno}: references a path outside the bundle: {token}")
    for name in sorted(names):
        if name.endswith(".json") and name != "catalog.json":
            for lineno, line in enumerate(files[name].decode("utf-8").splitlines(), 1):
                if JSON_CODE_WORDS.search(line):
                    problems.append(f"{name}:{lineno}: references code or a script path: {line.strip()[:80]}")
    for skill in script_backed_skills():
        path = f"skills/{skill}/SKILL.md"
        if path in names and SECTION_HEADING not in files[path].decode("utf-8"):
            problems.append(f"{path}: script-backed skill has no '{SECTION_HEADING}' section")
    for name in sorted(names):
        if not (name.startswith("skills/") and name.endswith("/SKILL.md")):
            continue
        text = files[name].decode("utf-8")
        if SECTION_HEADING not in text:
            continue
        procedure = name.rsplit("/", 1)[0] + "/" + NO_CODE_NAME
        if procedure not in names:
            problems.append(f"{name}: code-dependent skill has no {NO_CODE_NAME} replacement")
        elif f"]({NO_CODE_NAME})" not in text.split(SECTION_HEADING, 1)[1]:
            problems.append(f"{name}: AI-tool mode section does not link {NO_CODE_NAME}")
    return problems


def validate_all() -> list[str]:
    problems = source_problems()
    if problems:
        return problems
    for area in [None, *(a["id"] for a in load_catalog()["areas"])]:
        files = build_files(area)
        found = check_files(files)
        problems.extend(f"[{area or 'full'}] {p}" for p in found)
    return problems


def write_zip(files: dict[str, bytes], zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = zip_path.with_suffix(".zip.tmp")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(f"{TOP}/{name}", FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            archive.writestr(info, files[name])
    tmp.replace(zip_path)


def build(dist: Path, area: str | None, version: str) -> Path:
    files = build_files(area, version)
    problems = check_files(files)
    if problems:
        raise BundleError("\n".join(problems))
    stem = f"legal-skills-ai-{area}-{version}" if area else f"legal-skills-ai-{version}"
    zip_path = dist / f"{stem}.zip"
    write_zip(files, zip_path)
    return zip_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the AI-tool bundle zip for tools that run no code.")
    parser.add_argument("version", nargs="?", help="defaults to the plugin version")
    parser.add_argument("--dist", type=Path, default=ROOT / "dist")
    parser.add_argument("--area", help="build a zip for one practice area")
    parser.add_argument("--all-areas", action="store_true", help="also build one zip per practice area")
    args = parser.parse_args(argv)
    version = args.version or plugin_version()
    if not re.fullmatch(r"[A-Za-z0-9._-]+", version):
        print(f"BUNDLE_FAIL: invalid version {version}", file=sys.stderr)
        return 1
    targets: list[str | None] = []
    if args.area:
        targets.append(args.area)
    else:
        targets.append(None)
        if args.all_areas:
            targets.extend(a["id"] for a in load_catalog()["areas"])
    try:
        for target in targets:
            zip_path = build(args.dist.resolve(), target, version)
            with zipfile.ZipFile(zip_path) as archive:
                count = len(archive.namelist())
            print(f"BUNDLE_OK files={count} zip={zip_path}")
    except BundleError as exc:
        print(f"BUNDLE_FAIL:\n{exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
