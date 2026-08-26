#!/usr/bin/env python3
"""Summarise benchmark result directories into a Markdown table and stamp it into README.md.

Usage:
  python3 benchmarks/report.py benchmarks/results/<run-a> benchmarks/results/<run-b> ...
  python3 benchmarks/report.py --readme benchmarks/results/*        # also rewrite the README region

Each results directory holds <set>.jsonl rows from run.py (one row per case
and arm). Rows are grouped by (runner, model, set, arm). The README region
sits between <!-- benchmarks:start --> and <!-- benchmarks:end -->.
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import contaminated, keyed_verdict, rubric_score  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
START, END = "<!-- benchmarks:start -->", "<!-- benchmarks:end -->"


def load_rows(dirs: list[Path]) -> list[dict]:
    rows = []
    for d in dirs:
        for path in sorted(d.glob("*.jsonl")):
            if path.name == "verdicts.jsonl":
                continue
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    rows.append(json.loads(line))
    return rows


def summarise(rows: list[dict]) -> dict[tuple, dict]:
    cells: dict[tuple, dict] = defaultdict(lambda: {"n": 0, "pass": 0, "fv": 0, "fab": 0, "score": 0.0, "rub": 0, "breach": 0, "err": 0, "cost": 0.0, "contaminated": 0})
    for row in rows:
        key = (row.get("runner", "claude"), row["model"], row["set"], row["arm"])
        c = cells[key]
        c["n"] += 1
        c["cost"] += row.get("cost_usd") or 0
        if row.get("error"):
            c["err"] += 1
            continue
        if contaminated(row):
            c["contaminated"] += 1
            c["err"] += 1
            continue
        if row["kind"] == "keyed":
            v = keyed_verdict(row["case"], row["text"], row.get("tool_calls"))
            c["pass"] += v["pass"]
            if row["case"].get("truth") == "fabricated":
                c["fab"] += 1
                c["fv"] += v["false_verification"]
        else:
            v = rubric_score(row["case"], row.get("judge") or {})
            c["score"] += v["score"]
            c["rub"] += 1
            c["breach"] += v["boundary_breach"]
    return cells

ASSETS = ROOT / "docs" / "assets" / "benchmarks"
WITH_COLOUR, WITHOUT_COLOUR, INK, GRID = "#1C3C63", "#C59A46", "#222222", "#DDDDDD"


def _bar_chart(title: str, groups: list[tuple[str, float | None, float | None]], y_max: float, y_label: str,
               fmt) -> str:
    """Grouped bars: one group per (model, set); two bars per group (with, without). Pure SVG, no dependencies."""
    width, height, left, top, bottom = 900, 360, 60, 50, 90
    plot_w, plot_h = width - left - 20, height - top - bottom
    n = max(1, len(groups))
    group_w = plot_w / n
    bar_w = min(34, group_w * 0.36)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
           f'font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif" font-size="12">',
           f'<rect width="{width}" height="{height}" fill="white"/>',
           f'<text x="{left}" y="24" font-size="16" font-weight="600" fill="{INK}">{title}</text>',
           f'<rect x="{width-230}" y="12" width="12" height="12" fill="{WITH_COLOUR}"/><text x="{width-212}" y="23" fill="{INK}">with plugin</text>',
           f'<rect x="{width-120}" y="12" width="12" height="12" fill="{WITHOUT_COLOUR}"/><text x="{width-102}" y="23" fill="{INK}">without</text>']
    for i in range(5):
        v = y_max * i / 4
        y = top + plot_h - plot_h * i / 4
        out.append(f'<line x1="{left}" y1="{y:.1f}" x2="{width-20}" y2="{y:.1f}" stroke="{GRID}"/>')
        out.append(f'<text x="{left-8}" y="{y+4:.1f}" text-anchor="end" fill="{INK}">{fmt(v)}</text>')
    out.append(f'<text x="14" y="{top + plot_h/2:.1f}" transform="rotate(-90 14 {top + plot_h/2:.1f})" text-anchor="middle" fill="{INK}">{y_label}</text>')
    for gi, (label, w, wo) in enumerate(groups):
        cx = left + group_w * gi + group_w / 2
        for bi, (val, colour) in enumerate(((w, WITH_COLOUR), (wo, WITHOUT_COLOUR))):
            if val is None:
                continue
            x = cx - bar_w - 2 + bi * (bar_w + 4)
            h = plot_h * min(val, y_max) / y_max if y_max else 0
            y = top + plot_h - h
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{colour}" rx="2"/>')
            out.append(f'<text x="{x + bar_w/2:.1f}" y="{y-4:.1f}" text-anchor="middle" fill="{INK}" font-size="11">{fmt(val)}</text>')
        for li, line in enumerate(label.split("\n")):
            out.append(f'<text x="{cx:.1f}" y="{top + plot_h + 18 + 14*li}" text-anchor="middle" fill="{INK}" font-size="11">{line}</text>')
    out.append("</svg>")
    return "\n".join(out)


def _short_model(model: str) -> str:
    return model.split("/")[-1]


def charts(cells: dict[tuple, dict]) -> list[Path]:
    """Write SVG charts and return their paths (relative to ROOT)."""
    ASSETS.mkdir(parents=True, exist_ok=True)
    keyed_sets = [s for s in ("citations", "quotes", "legislation", "deadlines") if any(k[2] == s for k in cells)]
    models = sorted({(k[0], k[1]) for k in cells})
    written: list[Path] = []

    def cell(runner, model, s, arm):
        return cells.get((runner, model, s, arm))

    pass_groups, fv_groups, rub_groups, breach_groups = [], [], [], []
    for runner, model in models:
        for s in keyed_sets:
            w, wo = cell(runner, model, s, "with"), cell(runner, model, s, "without")
            def rate(c):
                if not c or c["n"] - c["err"] == 0:
                    return None
                return 100 * c["pass"] / (c["n"] - c["err"])
            pass_groups.append((f"{_short_model(model)}\n{s}", rate(w), rate(wo)))
            if (w and w["fab"]) or (wo and wo["fab"]):
                fv_groups.append((f"{_short_model(model)}\n{s}", w["fv"] if w else None, wo["fv"] if wo else None))
        w, wo = cell(runner, model, "rubrics", "with"), cell(runner, model, "rubrics", "without")
        if w or wo:
            rub_groups.append((f"{_short_model(model)}\nrubrics", w["score"]/w["rub"] if w and w["rub"] else None,
                               wo["score"]/wo["rub"] if wo and wo["rub"] else None))
            breach_groups.append((f"{_short_model(model)}\nrubrics", w["breach"] if w else None, wo["breach"] if wo else None))
    specs = [
        ("keyed-pass-rate.svg", "Answer-keyed pass rate (status vocabulary, keys and script use)", pass_groups, 100, "pass %", lambda v: f"{v:.0f}%"),
        ("false-verifications.svg", "False verifications of fabricated citations, quotes and legislation (lower is better)", fv_groups,
         max([v for _, w, wo in fv_groups for v in (w, wo) if v is not None] + [1]), "count", lambda v: f"{v:.0f}"),
        ("rubric-score.svg", "Rubric score on reasoning scenarios (judge-scored, 0–1)", rub_groups, 1.0, "score", lambda v: f"{v:.2f}"),
        ("boundary-breaches.svg", "Boundary breaches on reasoning scenarios (lower is better)", breach_groups,
         max([v for _, w, wo in breach_groups for v in (w, wo) if v is not None] + [1]), "count", lambda v: f"{v:.0f}"),
    ]
    for name, title, groups, y_max, y_label, fmt in specs:
        if not groups:
            continue
        path = ASSETS / name
        path.write_text(_bar_chart(title, groups, y_max, y_label, fmt), encoding="utf-8")
        written.append(path.relative_to(ROOT))
    return written


def table(cells: dict[tuple, dict]) -> str:
    lines = ["| Runner | Model | Set | Arm | n | Pass | False verifications | Rubric | Boundary breaches | Excluded (error / contaminated) | Cost |",
             "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for (runner, model, set_name, arm), c in sorted(cells.items()):
        scored = c["n"] - c["err"]
        pass_txt = f"{100 * c['pass'] / scored:.0f}%" if scored and set_name != "rubrics" else "–"
        fv_txt = f"{c['fv']}/{c['fab']}" if c["fab"] else "–"
        rub_txt = f"{c['score'] / c['rub']:.2f}" if c["rub"] else "–"
        br_txt = str(c["breach"]) if set_name == "rubrics" else "–"
        lines.append(f"| {runner} | {model} | {set_name} | {arm} | {c['n']} | {pass_txt} | {fv_txt} | {rub_txt} | {br_txt} | {c['err']} ({c['contaminated']}) | ${c['cost']:.2f} |")
    return "\n".join(lines)


def deltas(cells: dict[tuple, dict]) -> str:
    out = []
    keys = {(r, m, s) for (r, m, s, _) in cells}
    for r, m, s in sorted(keys):
        w, wo = cells.get((r, m, s, "with")), cells.get((r, m, s, "without"))
        if not (w and wo):
            continue
        if s == "rubrics":
            if w["rub"] and wo["rub"]:
                out.append(f"- **{m}** ({r}) {s}: rubric {w['score']/w['rub']:.2f} with vs {wo['score']/wo['rub']:.2f} without; boundary breaches {w['breach']} vs {wo['breach']}")
        else:
            sw, swo = w["n"] - w["err"], wo["n"] - wo["err"]
            if sw and swo:
                out.append(f"- **{m}** ({r}) {s}: pass {100*w['pass']/sw:.0f}% with vs {100*wo['pass']/swo:.0f}% without"
                           + (f"; false verifications {w['fv']}/{w['fab']} vs {wo['fv']}/{wo['fab']}" if w["fab"] else ""))
    return "\n".join(out)


def main(argv: list[str]) -> int:
    write_readme = "--readme" in argv
    dirs = [Path(a) for a in argv if not a.startswith("--")]
    if not dirs:
        print(__doc__)
        return 2
    rows = load_rows(dirs)
    cells = summarise(rows)
    print(table(cells))
    print()
    print(deltas(cells))
    if write_readme:
        paths = charts(cells)
        runs = sorted({(r.get("runner", "claude"), r["model"]) for r in rows})
        meta = ", ".join(f"{m} ({r})" for r, m in runs)
        images = "\n\n".join(f"![{p.stem}]({p.as_posix()})" for p in paths)
        body = f"Models: {meta}. Cases: {len({r['id'] for r in rows})}. Full per-cell numbers: `python3 benchmarks/report.py <results dirs>`.\n\n{images}\n\n{deltas(cells)}"
        readme = ROOT / "README.md"
        text = readme.read_text(encoding="utf-8")
        if START not in text:
            print("README has no benchmarks region", file=sys.stderr)
            return 1
        block = f"{START}\n{body}\n{END}"
        text = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
        readme.write_text(text, encoding="utf-8")
        print(f"README updated; charts: {', '.join(p.as_posix() for p in paths)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
