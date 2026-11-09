#!/usr/bin/env python3
"""Print the changelog section for the current plugin version.

The release workflow uses the output as the body of a draft GitHub Release.
Exit status 3 means the changelog has no dated section for the version, so
the version is still unreleased and no draft should be made.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "plugins" / "legal-skills" / ".claude-plugin" / "plugin.json"
CHANGELOG = ROOT / "CHANGELOG.md"
NO_SECTION = 3


def plugin_version() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]


def section_for(changelog: str, version: str) -> tuple[str, str] | None:
    """Return (title, body) of the dated section that names the version."""
    heading = re.compile(
        rf"^## (\d{{4}}-\d{{2}}-\d{{2}} - {re.escape(version)}(?![\d.]).*)$",
        re.MULTILINE,
    )
    match = heading.search(changelog)
    if match is None:
        return None
    following = re.search(r"^## ", changelog[match.end():], re.MULTILINE)
    end = match.end() + following.start() if following else len(changelog)
    return match.group(1).strip(), changelog[match.end():end].strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="store_true", help="print the plugin version only")
    parser.add_argument("--title", action="store_true", help="print the section title only")
    args = parser.parse_args()

    version = plugin_version()
    if args.version:
        print(version)
        return 0
    section = section_for(CHANGELOG.read_text(encoding="utf-8"), version)
    if section is None:
        print(f"CHANGELOG.md has no dated section for {version}", file=sys.stderr)
        return NO_SECTION
    title, body = section
    sys.stdout.write(f"{title}\n" if args.title else body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
