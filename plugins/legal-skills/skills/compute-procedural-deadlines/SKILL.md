---
name: compute-procedural-deadlines
description: Compute candidate Australian civil court deadlines from a lawyer-supplied trigger date, never by model arithmetic. Use for defences, appeals and other rule-fixed steps. Not for criminal procedure or contested trigger dates.
---

# Compute Procedural Deadlines

<!-- ai-tool:code -->
## Scope

Compute candidate procedural deadlines for Australian civil litigation from a
lawyer-supplied trigger event using the bundled deterministic script and
evidence-gated computation-rule tables — the model never performs date
arithmetic. Computed coverage spans the federal courts and the superior and
lower courts of every State and Territory. State and Territory forums use
their own verified holiday table. The federal courts and the ART have none:
the request must name the registry's holiday table or the script refuses any
business-day or rollover computation. Steps without a verified table entry
receive identify-only output naming the governing rule. Use when a practitioner needs candidate dates for defences,
appeals or other rule-fixed steps after filing, service or judgment. Do not
use for criminal procedure, for court-fixed or discretionary dates, or when
the trigger date is contested — those fail closed to the responsible lawyer,
and every computed date is provisional until confirmed.

Compute candidate deadlines with the bundled script and nothing else. A
refusal from the script is a correct result: report the governing rule and
the reason, and never fill the gap with model arithmetic.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md),
use an approved profile per the
[deadline profile schema](../../references/deadline-profile-schema.md), and
run [compute_deadline.py](scripts/compute_deadline.py) against the
[computation-rule tables](../../references/computation-rules/) and
[holiday tables](../../references/holidays/).

## Workflow

1. Fix the trigger and the forum.
   - Record the forum, the procedural step, the lawyer-supplied trigger
     date and what the trigger was (service, filing, judgment). A contested
     or unknown trigger date is `NOT READY` — never assume one.
2. Locate the governing rule.
   - Find the matching period rule in the forum's computation-rule table.
     A step with no table entry is identify-only: name the governing rule
     if known and route verification to `$verify-deadline-basis`.
3. Run the script.
   - Call `scripts/compute_deadline.py` with the table id, period rule id
     and trigger date (plus `holiday_table` from the profile's
     `registry_holiday_table` for federal court and ART steps). Report the script's output
     faithfully: `computed` results as candidate dates with the provisions
     applied and every warning; `identify_only` results with the stated
     reason.
   - Never adjust, round or re-derive a date the script produced or
     refused. If holiday caveats flag registry-location uncertainty,
     surface them.
4. Set the human decision gate.
   - Name the confirmer who must confirm each candidate date and enter it
     in the diary system of record before any reliance.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Step: <forum; procedural step; governing rule citation>
Trigger: <lawyer-supplied trigger event and date; stated as assumption>
Script result: <computed candidate date and day | identify-only with reason>
Provisions applied: <citations from the script output; evidence states>
Warnings: <script warnings, holiday caveats, staging limits>
Human decision gate: <confirmer; diary entry pending confirmation>
Limitations: <candidate only; not a diary system; script-only arithmetic>
```

## Fail closed

Return `NOT READY` when the trigger date, forum or governing rule cannot be
established. Report every script refusal as identify-only output — never
compute around an unverified table, an uncovered holiday range or an
unsupported period. Route criminal procedure `OUTSIDE SCOPE`, and never
present a candidate date as the binding deadline.
<!-- /ai-tool:code -->

## AI-tool mode

Use this section when the host cannot run
code. The AI-tool bundle ships this section and
leaves the code steps out; hosts that can run code ignore it. General rules:
[AI-tool mode](../../references/ai-tool-mode.md).

This host cannot run the deterministic computation, and the model must never
do date arithmetic. Deliver identify-only output: the rule, its source, the
inputs a person needs and `not computed`.

0. Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
   and use an approved profile per the
   [deadline profile schema](../../references/deadline-profile-schema.md). With
   no approved profile, or no named confirmer and diary system of record, the
   result is `NOT READY`.
1. Fix the forum, the procedural step and the lawyer-supplied trigger date and
   event. A contested or unknown trigger date is `NOT READY`. Criminal
   procedure, and court-fixed or discretionary dates, are `OUTSIDE SCOPE` or
   identify-only: name the governing rule and route them to the responsible
   lawyer.
2. Open the forum's table in [computation rules](../../references/computation-rules/)
   (`cth-federal-courts`, `nsw-courts`, `vic-courts`, `qld-courts`,
   `wa-courts`, `sa-courts`, `tas-courts`, `act-courts`, `nt-courts`, `art`,
   `ncat`, `qcat`, `vcat`). Find the period rule whose trigger matches.
3. Copy from the rule: its citation, period length and unit, rollover,
   warnings, source URL and evidence state. Name the holiday table in
   [holidays](../../references/holidays/) that a person needs. For federal
   court and ART steps the registry's holiday table must come from the
   profile or the person.
4. If no rule matches, or its evidence state is `pending-verification`, say so
   and route verification to `$verify-deadline-basis`.
5. Never state, estimate or adjust a date, and never present a candidate as
   the binding deadline. Give the person the inputs to count it themselves or
   in a diary system.

Lead with `IDENTIFY-ONLY - NOT COMPUTED`, `NOT READY` or `OUTSIDE SCOPE`.

```text
Step: <forum; procedural step; governing rule citation>
Trigger: <lawyer-supplied trigger event and date; stated as assumption>
Rule: <period rule id; period length and unit; rollover>
Source: <source URL; evidence state and checked date>
Inputs needed: <trigger date, registry location, holiday table, court directions>
Result: not computed
Warnings: <rule warnings; holiday caveats>
Human decision gate: <confirmer; diary entry pending confirmation>
Limitations: <identify-only; not a diary system; every date needs confirmation>
```
