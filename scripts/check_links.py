#!/usr/bin/env python3
"""Check that every external URL cited under plugins/ still resolves.

Legal-research skills route users to official publishers; a moved page is a
silent failure for them. This script extracts http(s) URLs from every file
under plugins/ (markdown, JSON, YAML, Python) and requests each once.

Exit 1 when any URL is dead: DNS failure, connection refused, or HTTP 404/410.
Bot-blocked responses (401, 403, 429) and timeouts are reported as warnings,
not failures, because several official publishers refuse non-browser clients.
"""

from __future__ import annotations

import concurrent.futures
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = re.compile(r"https?://[^\s<>()\[\]\"'`;]+")
DEAD = {404, 410}
BLOCKED = {401, 403, 429}
TIMEOUT = 20
USER_AGENT = "Mozilla/5.0 (compatible; legal-skills-link-check; +https://github.com/l0cka/legal-skills)"
# Documentation placeholders and format templates, never meant to resolve.
SKIP = re.compile(r"[{}]|://[^/]*\.(test|example|invalid)(/|$)|://example\.(com|org|net)")


def collect(root: Path) -> dict[str, set[str]]:
    found: dict[str, set[str]] = {}
    for path in sorted((root / "plugins").rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".json", ".yaml", ".yml", ".py"}:
            continue
        for match in URL.findall(path.read_text(encoding="utf-8", errors="replace")):
            url = match.rstrip(".:*,")
            if SKIP.search(url):
                continue
            found.setdefault(url, set()).add(str(path.relative_to(root)))
    return found


def probe(url: str) -> tuple[str, int | str]:
    # ponytail: curl rather than urllib — legislation.gov.au and other Akamai-fronted
    # publishers hang urllib's TLS handshake but answer curl immediately.
    result = subprocess.run(
        ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", "-L", "--http1.1",
         "-m", str(TIMEOUT), "-A", USER_AGENT, url],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 28:
        return url, "timeout"
    if result.returncode == 6:
        return url, "error: could not resolve host"
    if result.returncode == 7:
        return url, "error: connection refused"
    if result.returncode:
        return url, f"error: curl exit {result.returncode} {result.stderr.strip()}"
    return url, int(result.stdout.strip() or 0)


def main() -> int:
    urls = collect(ROOT)
    print(f"Checking {len(urls)} URL(s) under plugins/")
    dead: list[str] = []
    warnings: list[str] = []
    # ponytail: 8 workers and one GET each; add per-host throttling if publishers start rate-limiting.
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for url, status in pool.map(probe, sorted(urls)):
            where = ", ".join(sorted(urls[url]))
            if status in DEAD or (isinstance(status, str) and status.startswith("error")):
                dead.append(f"DEAD {status}: {url}\n  in {where}")
            elif status in BLOCKED or status == "timeout":
                warnings.append(f"WARN {status}: {url}\n  in {where}")
    for line in warnings:
        print(line)
    for line in dead:
        print(line, file=sys.stderr)
    print(f"{len(dead)} dead, {len(warnings)} blocked or timed out, {len(urls) - len(dead) - len(warnings)} ok")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
