#!/usr/bin/env python3
"""Run benchmark cases through `claude -p`, with and without the plugin loaded.

Each case runs once per arm. The `without` arm disables every legal-skills
plugin the user has installed (via --settings) and loads nothing; the `with`
arm additionally passes --plugin-dir for the case's plugin. Rubric cases get
a second judge call that returns which checklist items are present or
breached. Results land in benchmarks/results/<timestamp>/<set>.jsonl; score
them with benchmarks/score.py.

Usage:
  python3 benchmarks/run.py --set citations --arm with,without --model opus
  python3 benchmarks/run.py --set rubrics --limit 3 --judge-model opus
  python3 benchmarks/run.py --set all --ids cit-hca-001,breach-001
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import subprocess
import sys
import threading
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCH = ROOT / "benchmarks"
KEYED_SETS = ("citations", "quotes", "legislation", "deadlines")
JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "present": {"type": "array", "items": {"type": "string"}},
        "breached": {"type": "array", "items": {"type": "string"}},
        "notes": {"type": "string"},
    },
    "required": ["present", "breached"],
}


def load_cases(set_name: str) -> list[dict]:
    cases: list[dict] = []
    names = KEYED_SETS + ("rubrics",) if set_name == "all" else (set_name,)
    for name in names:
        if name == "rubrics":
            for path in sorted(BENCH.glob("rubrics/*.json")):
                case = json.loads(path.read_text(encoding="utf-8"))
                case["set"], case["kind"] = "rubrics", "rubric"
                cases.append(case)
        else:
            for line in (BENCH / "keyed" / f"{name}.jsonl").read_text(encoding="utf-8").splitlines():
                if line.strip():
                    case = json.loads(line)
                    case["kind"] = "keyed"
                    cases.append(case)
    return cases


# Official publishers the verification skills fetch from; Bash network access is sandboxed to these.
PUBLISHER_DOMAINS = [
    "hcourt.gov.au", "www.hcourt.gov.au", "eresources.hcourt.gov.au",
    "www.caselaw.nsw.gov.au", "caselaw.nsw.gov.au",
    "www.fedcourt.gov.au", "fedcourt.gov.au", "www.fcfcoa.gov.au", "fcfcoa.gov.au",
    "www.legislation.gov.au", "legislation.gov.au", "api.legislation.gov.au",
    "legislation.nsw.gov.au", "www.legislation.nsw.gov.au",
    "www.legislation.qld.gov.au", "www.legislation.vic.gov.au", "www.legislation.wa.gov.au",
    "www.legislation.sa.gov.au", "www.legislation.tas.gov.au", "www.legislation.act.gov.au",
    "legislation.nt.gov.au", "www.fairwork.gov.au", "www.fwc.gov.au", "www.oaic.gov.au",
    "www.austrac.gov.au", "www.asic.gov.au", "www.cyber.gov.au", "www.apra.gov.au",
]


def session_settings(allowed_domains: list[str]) -> str:
    """Disable every user-installed legal-skills plugin and sandbox Bash network access to the publishers."""
    names = sorted(p.name for p in (ROOT / "plugins").iterdir() if p.is_dir() and not p.name.startswith("."))
    return json.dumps({
        "enabledPlugins": {f"{name}@legal-skills": False for name in names},
        "sandbox": {"enabled": True, "network": {"allowedDomains": allowed_domains, "strictAllowlist": True}},
    })


def claude(prompt: str, *, model: str, max_turns: int, tools: list[str], plugin_dir: Path | None,
           timeout: int, cwd: Path, json_schema: dict | None = None, allowed_domains: list[str] | None = None) -> dict:
    """Run one headless session from a scratch cwd so the repository itself never leaks into the context."""
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose", "--model", model,
           "--max-turns", str(max_turns), "--settings", session_settings(allowed_domains or PUBLISHER_DOMAINS),
           "--permission-mode", "dontAsk"]
    if tools:
        cmd += ["--allowedTools", *tools]
    if plugin_dir:
        cmd += ["--plugin-dir", str(plugin_dir.resolve())]
    if json_schema:
        cmd += ["--json-schema", json.dumps(json_schema)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd, check=False, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"error": f"timeout after {timeout}s"}
    payload: dict = {}
    tool_calls: list[dict] = []
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "assistant":
            for block in event.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    tool_calls.append({"name": block.get("name"), "input": block.get("input")})
        elif event.get("type") == "result":
            payload = event
    if not payload:
        return {"error": f"exit {proc.returncode}, no result event: {proc.stderr.strip()[:300]}", "tool_calls": tool_calls}
    payload["exit_code"] = proc.returncode
    payload["tool_calls"] = tool_calls
    if proc.returncode and not (payload.get("result") or payload.get("text")):
        payload["error"] = f"exit {proc.returncode}: {payload.get('subtype') or proc.stderr.strip()[:300]}"
    return payload


def pi(prompt: str, *, model: str, max_turns: int, tools: list[str], plugin_dir: Path | None, skill: str | None,
       timeout: int, cwd: Path, thinking: str = "low") -> dict:
    """Run one case through the `pi` coding agent. The with arm loads the case's skill directory via --skill;
    the without arm passes --no-skills. Context files, sessions, extensions and prompt templates are disabled."""
    cmd = ["pi", "-p", "--mode", "json", "--no-session", "--no-context-files", "--no-extensions",
           "--no-prompt-templates", "--thinking", thinking, "--model", model]
    if plugin_dir and skill:
        cmd += ["--skill", str((plugin_dir / "skills" / skill).resolve())]
    else:
        cmd += ["--no-skills"]
    if tools:
        # `read` is always on: pi loads a skill by reading its SKILL.md, so removing it silently disables the skill.
        pi_tools = sorted({{"Bash": "bash", "WebFetch": "bash", "WebSearch": "bash", "Write": "write",
                            "Read": "read", "Edit": "edit"}.get(t, t.lower()) for t in tools} | {"read"})
        cmd += ["--tools", ",".join(pi_tools)]
    else:
        cmd += ["--tools", "read"]
    cmd += ["--", prompt]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd, check=False, stdin=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return {"error": f"timeout after {timeout}s"}
    text, tool_calls, cost, turns = "", [], 0.0, 0
    for line in proc.stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = event.get("type")
        if kind == "message_end" and event.get("message", {}).get("role") == "assistant":
            turns += 1
            message = event["message"]
            cost += (message.get("usage", {}).get("cost", {}) or {}).get("total", 0) or 0
            for block in message.get("content", []):
                if block.get("type") == "text" and block.get("text"):
                    text = block["text"]
                elif "tool" in str(block.get("type", "")).lower():
                    tool_calls.append({"name": block.get("name"), "input": block.get("arguments") or block.get("input")})
        elif kind and "tool_execution_start" in kind:
            tool_calls.append({"name": event.get("toolName") or event.get("name"), "input": event.get("args") or event.get("arguments")})
    if not text:
        return {"error": f"exit {proc.returncode}, no assistant text: {proc.stderr.strip()[:300]}", "tool_calls": tool_calls}
    return {"result": text, "tool_calls": tool_calls, "total_cost_usd": cost, "num_turns": turns,
            "exit_code": proc.returncode, "subtype": "success"}


def result_text(payload: dict) -> str:
    return payload.get("result") or payload.get("text") or ""


def judge(case: dict, text: str, *, model: str, timeout: int, cwd: Path) -> dict:
    checklist = "\n".join(f"- INCLUDE: {i['item']}" for i in case["must_include"])
    checklist += "\n" + "\n".join(f"- MUST NOT: {i['item']}" for i in case["must_not"])
    prompt = (
        "You are grading a legal-workflow response against a checklist. Quote the response only; do not add law.\n"
        "For each INCLUDE item, decide whether the response genuinely covers it (not merely mentions a word). "
        "For each MUST NOT item, decide whether the response does the forbidden thing. "
        "Return JSON with `present` (INCLUDE items covered, verbatim item text), `breached` (MUST NOT items done, "
        "verbatim item text) and short `notes`.\n\nCHECKLIST:\n" + checklist + "\n\nRESPONSE:\n" + text
    )
    payload = claude(prompt, model=model, max_turns=1, tools=[], plugin_dir=None, timeout=timeout, cwd=cwd, json_schema=JUDGE_SCHEMA)
    if "error" in payload:
        return {"error": payload["error"], "present": [], "breached": [], "text": text}
    verdict = payload.get("structured_output")
    if not isinstance(verdict, dict):
        try:
            verdict = json.loads(result_text(payload))
        except json.JSONDecodeError:
            verdict = {"present": [], "breached": [], "notes": "judge output unparseable"}
    verdict["text"] = text
    return verdict


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--set", default="all", choices=KEYED_SETS + ("rubrics", "all"))
    parser.add_argument("--arm", default="with,without")
    parser.add_argument("--runner", default="claude", choices=("claude", "pi"))
    parser.add_argument("--model", default="opus", help="claude alias, or pi provider/model id")
    parser.add_argument("--thinking", default="low", help="pi thinking level")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--judge-model", default="opus")
    parser.add_argument("--max-turns", type=int, default=15)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--ids")
    parser.add_argument("--out")
    parser.add_argument("--cases", help="run a single JSONL/JSON file of cases instead of --set")
    parser.add_argument("--allowed-domains", help="comma-separated hosts Bash may reach (default: the official publishers)")
    parser.add_argument("--extra-tools", default="Bash", help="comma-separated tools added to every case (Bash lets the verifiers curl publishers that refuse WebFetch redirects)")
    args = parser.parse_args(argv)

    if args.cases:
        path = Path(args.cases)
        if path.suffix == ".json":
            case = json.loads(path.read_text(encoding="utf-8"))
            case["set"], case["kind"] = "rubrics", "rubric"
            cases = [case]
        else:
            cases = []
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    case = json.loads(line)
                    case["kind"] = "keyed"
                    cases.append(case)
    else:
        cases = load_cases(args.set)
    if args.ids:
        wanted = set(args.ids.split(","))
        cases = [c for c in cases if c["id"] in wanted]
    if args.limit:
        cases = cases[: args.limit]
    arms = args.arm.split(",")
    out_dir = Path(args.out) if args.out else BENCH / "results" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"{len(cases)} case(s) x {arms} -> {out_dir}")

    lock = threading.Lock()

    def run_one(case: dict, arm: str) -> None:
        plugin_dir = ROOT / "plugins" / case["plugin"] if arm == "with" else None
        tools = list(dict.fromkeys(case.get("tools", []) + [x for x in args.extra_tools.split(",") if x]))
        scratch = out_dir / "scratch" / f"{case['id']}-{arm}"
        scratch.mkdir(parents=True, exist_ok=True)
        if args.runner == "pi":
            payload = pi(case["prompt"], model=args.model, max_turns=args.max_turns, tools=tools, plugin_dir=plugin_dir,
                         skill=case["skill"], timeout=args.timeout, cwd=scratch, thinking=args.thinking)
        else:
            payload = claude(case["prompt"], model=args.model, max_turns=args.max_turns, tools=tools,
                             plugin_dir=plugin_dir, timeout=args.timeout, cwd=scratch,
                             allowed_domains=args.allowed_domains.split(",") if args.allowed_domains else None)
        row = {"id": case["id"], "set": case["set"], "kind": case["kind"], "arm": arm, "runner": args.runner,
               "model": args.model, "case": case, "text": result_text(payload), "cost_usd": payload.get("total_cost_usd"),
               "turns": payload.get("num_turns"), "exit_code": payload.get("exit_code"),
               "subtype": payload.get("subtype"), "tool_calls": payload.get("tool_calls", []),
               "error": payload.get("error")}
        if case["kind"] == "rubric" and not row["error"]:
            row["judge"] = judge(case, row["text"], model=args.judge_model, timeout=args.timeout, cwd=scratch)
        with lock:
            with (out_dir / f"{case['set']}.jsonl").open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(row) + "\n")
            status = row["error"] or f"{len(row['text'])} chars, {row['turns']} turns, ${row['cost_usd'] or 0:.3f}"
            print(f"  {case['id']:<28} {arm:<8} {status}", flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_one, case, arm) for case in cases for arm in arms]
        for future in futures:
            future.result()
    print(f"done -> python3 benchmarks/score.py {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
