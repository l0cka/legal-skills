#!/usr/bin/env python3
"""Assert the README plugin and skill badges match the validated repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_repository import ROOT, ValidationError, validate


def main() -> int:
    try:
        plugin_count, skill_count = validate()
    except (OSError, ValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    checks = {
        f"plugins-{plugin_count}-": "plugin badge",
        f"skills-{skill_count}-": "skill badge",
    }
    failures = [
        f"README.md: {label} does not show the validated count ({needle.rstrip('-')})"
        for needle, label in checks.items()
        if needle not in readme
    ]
    badge_counts = re.findall(r"badge/(?:plugins|skills)-(\d+)-", readme)
    if len(badge_counts) != 2:
        failures.append("README.md: expected exactly one plugin badge and one skill badge")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1
    print(f"README badges match: {plugin_count} plugin(s), {skill_count} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
