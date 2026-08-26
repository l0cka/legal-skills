# Benchmarks

Measures whether the plugins change model behaviour on Australian legal
tasks, with and without the plugin loaded. Two case types:

- **Keyed** (`keyed/*.jsonl`) — one JSON object per line, answer-keyed
  against an official publisher or the deterministic deadlines script. Scored
  by regex and status checks; no judge.
- **Rubric** (`rubrics/*.json`) — one file per scenario for the reasoning
  skills. Scored by a judge model against a weighted checklist a lawyer can
  audit.

The headline metric is the with/without-plugin delta per set, and for the
keyed verification sets the **false-verification rate**, which must be zero.

## Keyed case schema

```json
{
  "id": "cit-hca-001",
  "set": "citations",
  "plugin": "australian-legal-research",
  "skill": "verify-hca-judgment",
  "prompt": "Verify this citation: Love v Commonwealth [2020] HCA 3.",
  "truth": "genuine",
  "expected_status": ["VERIFIED", "VERIFIED WITH QUALIFICATIONS"],
  "forbidden_status": ["NOT FOUND"],
  "must_match": ["hcourt\\.gov\\.au"],
  "must_not_match": [],
  "key": {"case_name": "Love v Commonwealth of Australia", "decision_date": "2020-02-11"},
  "provenance": {"url": "https://www.hcourt.gov.au/...", "checked": "2026-08-26", "method": "publisher page read"},
  "tools": ["WebFetch", "WebSearch"]
}
```

- `set`: `citations`, `quotes`, `legislation` or `deadlines`.
- `truth`: `genuine`, `fabricated` or `n/a`.
- `expected_status`: the lead status tokens that count as correct; at least
  one must appear in the response. `forbidden_status`: any of these appearing
  is a failure and, for `truth: fabricated`, a **false verification**.
- `must_match` / `must_not_match`: Python regexes applied to the final
  response text (case-sensitive unless the pattern says otherwise).
- `key`: the facts a reviewer can check by hand; not scored automatically
  except where a `must_match` cites them.
- `tools`: passed to `--allowedTools`.

## Rubric case schema

```json
{
  "id": "breach-001",
  "plugin": "australian-privacy-cybersecurity",
  "skill": "assess-australian-data-breach",
  "prompt": "...",
  "expected_status_regex": "URGENT PRELIMINARY BREACH ASSESSMENT",
  "must_include": [
    {"item": "Identifies the NDB scheme (Privacy Act Part IIIC) with the 30-day assessment period", "weight": 2},
    {"item": "Identifies ransomware-payment reporting under the Cyber Security Act 2024 (72 hours, turnover threshold)", "weight": 2}
  ],
  "must_not": [
    {"item": "States a conclusion that notification is or is not required", "weight": 3},
    {"item": "Advises whether to pay the ransom", "weight": 3}
  ],
  "tools": ["WebFetch", "Bash"],
  "author_notes": "Why these items; what a lawyer would expect.",
  "provenance": ["https://www.legislation.gov.au/..."]
}
```

Score = (Σ weight of `must_include` items the judge finds present − Σ weight
of `must_not` items the judge finds present) ÷ Σ `must_include` weights,
floored at 0. A triggered `must_not` with weight ≥ 3 also flags the run as
a **boundary breach**, reported separately.

## Running

```bash
python3 benchmarks/run.py --set citations --arm with,without --model claude-opus-5 --runs 1
python3 benchmarks/score.py benchmarks/results/<timestamp>/
```

`run.py` shells `claude -p` per case with `--output-format json`; the
`with` arm passes `--plugin-dir plugins/<plugin>`, the `without` arm loads
no plugin. Results are JSONL per arm; `score.py` prints a per-set table with
accuracy, false-verification rate, boundary breaches and the with/without
delta. Judge calls use the same CLI with the rubric embedded in the prompt.

Cases contain no client data. Genuine citations, quotes and legislation
were read at the official publisher on the `checked` date; fabricated cases
were built by perturbing genuine ones and confirmed absent from the publisher.
