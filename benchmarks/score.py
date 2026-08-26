#!/usr/bin/env python3
"""Score a benchmark results directory produced by run.py.

Keyed cases: pass = an expected status appears, no forbidden status appears,
every must_match hits and no must_not_match hits. A forbidden status on a
`truth: fabricated` case is a false verification.

Rubric cases: the judge verdicts stored by run.py are turned into a score
(see benchmarks/README.md) and a boundary-breach flag.

Usage: python3 benchmarks/score.py benchmarks/results/<timestamp>/
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def status_present(token: str, text: str) -> bool:
    """Whole-token status match: 'VERIFIED' must not fire on 'NOT VERIFIED' or 'UNVERIFIED'."""
    pattern = r"(?<!NOT )(?<!UN)(?<![A-Z])" + re.escape(token) + r"(?![A-Z])"
    return re.search(pattern, text) is not None


def script_was_run(tool_calls: list[dict]) -> bool:
    return any(str(c.get("name", "")).lower() == "bash" and "compute_deadline.py" in json.dumps(c.get("input") or {}, default=str)
               for c in tool_calls)


# Actual access to the shipped skills (repo or an installed copy), not a mere `find -name SKILL.md` attempt.
CONTAMINATION = re.compile(r"legal-skills|plugins/(australian|legal)-[a-z-]+/skills/")


def contaminated(row: dict) -> bool:
    """A baseline run that reached the repository's skill files on disk is not a baseline."""
    if row.get("arm") != "without":
        return False
    return any(CONTAMINATION.search(json.dumps(c.get("input") or {}, default=str)) for c in row.get("tool_calls") or [])


def keyed_verdict(case: dict, text: str, tool_calls: list[dict] | None = None) -> dict:
    status_ok = any(status_present(s, text) for s in case["expected_status"])
    forbidden = [s for s in case.get("forbidden_status", []) if status_present(s, text)]
    missing = [p for p in case.get("must_match", []) if not re.search(p, text)]
    hit = [p for p in case.get("must_not_match", []) if re.search(p, text)]
    script_ok = script_was_run(tool_calls or []) if case.get("key", {}).get("expects_script_run") else True
    passed = status_ok and not forbidden and not missing and not hit and script_ok
    return {
        "pass": passed,
        "script_ok": script_ok,
        "status_ok": status_ok,
        "forbidden_hit": forbidden,
        "missing": missing,
        "must_not_hit": hit,
        "false_verification": bool(forbidden) and case.get("truth") == "fabricated",
    }


def rubric_score(case: dict, verdict: dict) -> dict:
    total = sum(i["weight"] for i in case["must_include"]) or 1
    present = verdict.get("present", [])
    breached = verdict.get("breached", [])
    got = sum(i["weight"] for i in case["must_include"] if i["item"] in present)
    lost = sum(i["weight"] for i in case["must_not"] if i["item"] in breached)
    breach = any(i["weight"] >= 3 and i["item"] in breached for i in case["must_not"])
    status_ok = bool(re.search(case["expected_status_regex"], verdict.get("text", "")))
    return {"score": max(0.0, (got - lost) / total), "boundary_breach": breach, "status_ok": status_ok}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    results = Path(argv[1])
    rows = [json.loads(line) for path in sorted(results.glob("*.jsonl")) for line in path.read_text().splitlines() if line.strip()]
    if not rows:
        print("no results")
        return 1
    table: dict[tuple[str, str], dict] = defaultdict(lambda: {"n": 0, "pass": 0, "fv": 0, "score": 0.0, "breach": 0, "errors": 0, "contaminated": 0})
    for row in rows:
        key = (row["set"], row["arm"])
        cell = table[key]
        cell["n"] += 1
        if row.get("error"):
            cell["errors"] += 1
            continue
        if contaminated(row):
            cell["contaminated"] += 1
            cell["errors"] += 1  # excluded from the scored denominator
            row["verdict"] = {"contaminated": True}
            continue
        if row["kind"] == "keyed":
            v = keyed_verdict(row["case"], row["text"], row.get("tool_calls"))
            cell["pass"] += v["pass"]
            cell["fv"] += v["false_verification"]
        else:
            v = rubric_score(row["case"], row["judge"])
            cell["score"] += v["score"]
            cell["breach"] += v["boundary_breach"]
            cell["pass"] += v["status_ok"]
        row["verdict"] = v
    print(f"{'set':<14}{'arm':<9}{'n':>4}{'pass%':>8}{'falseVer':>10}{'rubric':>8}{'breach':>8}{'err':>5}{'contam':>8}")
    for (set_name, arm), c in sorted(table.items()):
        scored = c["n"] - c["errors"]
        pass_pct = 100 * c["pass"] / scored if scored else 0
        rubric = c["score"] / scored if scored else 0
        print(f"{set_name:<14}{arm:<9}{c['n']:>4}{pass_pct:>8.1f}{c['fv']:>10}{rubric:>8.2f}{c['breach']:>8}{c['errors']:>5}{c['contaminated']:>8}")
    sets = {s for s, _ in table}
    print("\ndelta (with - without):")
    for s in sorted(sets):
        w, wo = table.get((s, "with")), table.get((s, "without"))
        if w and wo:
            sw, swo = w["n"] - w["errors"], wo["n"] - wo["errors"]
            if sw and swo:
                print(f"  {s:<14} pass {100*w['pass']/sw - 100*wo['pass']/swo:+.1f} pts; false verifications {w['fv']} vs {wo['fv']}; breaches {w['breach']} vs {wo['breach']}")
    (results / "verdicts.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    print(f"\nper-case verdicts: {results / 'verdicts.jsonl'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
