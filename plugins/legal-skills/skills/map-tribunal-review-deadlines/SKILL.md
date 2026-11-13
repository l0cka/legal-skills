---
name: map-tribunal-review-deadlines
description: Candidate merits-review and tribunal deadlines (ART, NCAT, QCAT, VCAT), never by model arithmetic. Use after a government or tribunal decision. For court steps use `$compute-procedural-deadlines`. Never concludes a period has expired.
---

# Map Tribunal Review Deadlines

<!-- ai-tool:code -->
## Scope

Map and compute candidate merits-review and tribunal deadlines for Australian
administrative and civil decisions, with computed coverage staged to the ART,
NCAT, QCAT and VCAT and identify-only output for other tribunals, using the
bundled deterministic script — never model arithmetic. Every migration-review
output carries a mandatory non-extendable and jurisdictional-deadline warning
with a specialist-review flag. Use when a practitioner needs candidate review
or internal-appeal deadlines after a government or tribunal decision. Do not
use for criminal matters, to conclude that a period has expired or been
extended, or when the notification date is contested — those fail closed to
the responsible lawyer.

Map candidate review deadlines from the tribunal computation-rule tables and
compute only through the bundled script. The enabling enactment frequently
fixes its own period — the general tribunal layer is a candidate, never a
conclusion.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md),
use an approved profile per the
[deadline profile schema](../../references/deadline-profile-schema.md), and
run [compute_deadline.py](../compute-procedural-deadlines/scripts/compute_deadline.py)
against the [computation-rule tables](../../references/computation-rules/).

For court steps use `$compute-procedural-deadlines`.

## Workflow

1. Fix the decision and the inputs.
   - Record the decision, the decision-maker, the tribunal, and the
     lawyer-supplied notification date as an assumption. A contested or
     unknown notification date is `NOT READY`.
2. Locate every candidate period.
   - Take the general tribunal-layer candidate from the tribunal's table
     (`art`, `ncat`, `qcat`), and flag that the Act conferring the decision
     may fix a different period (for QCAT, s 6(7) of the QCAT Act says so
     expressly). Verify the conferring Act through
     `$check-commonwealth-legislation` or the applicable state checker.
   - For VCAT no general default period exists — the enabling enactment
     always fixes the period (see the `vcat` table note); identify the
     conferring provision and route its verification before any candidate
     is stated.
   - For tribunals without a table, produce identify-only output naming the
     enabling Act.
3. Compute through the script only.
   - Run the script per candidate. For ART steps, pass `holiday_table` from
     the profile's `registry_holiday_table`; if the profile names none, ask
     the user which registry the act is to be done in before running the
     script. Report `computed` and `identify_only`
     results faithfully, with every warning.
   - For any migration matter, always include the warning that migration
     time limits are non-extendable or jurisdictional and have changed
     repeatedly, and flag specialist review before reliance. Never conclude
     that a migration period has expired or that an extension is available.
4. Set the human decision gate.
   - Name the confirmer who must confirm each candidate, resolve the
     conferring-Act period and enter dates in the diary system of record.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Decision: <decision; decision-maker; tribunal; notification date assumption>
Candidates: <period; basis; script result (candidate date | identify-only);
  evidence state>
Conferring-Act check: <provision verified or routed; evidence state>
Migration warning: <present on every migration matter; specialist review>
Human decision gate: <confirmer; decisions required; diary entry pending>
Limitations: <every candidate provisional until confirmed; enabling
  enactment may differ; not a diary system>
```

## Fail closed

Return `NOT READY` when the decision, tribunal or notification date cannot
be established. Never compute around a script refusal, never conclude a
period has expired or been extended, never omit the migration warning from
a migration matter, and route criminal matters `OUTSIDE SCOPE`.
<!-- /ai-tool:code -->

## AI-tool mode

Use this section when the host cannot run
code. The AI-tool bundle ships this section and
leaves the code steps out; hosts that can run code ignore it. General rules:
[AI-tool mode](../../references/ai-tool-mode.md).

This host cannot run the deterministic computation, and the model must never
do date arithmetic. Deliver identify-only output for each candidate. A
candidate date for a tribunal general period may come only from the deadline
calculator workbook, filled and read by a person as the no-code procedure
describes.

0. Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
   and use an approved profile per the
   [deadline profile schema](../../references/deadline-profile-schema.md). With
   no approved profile, or no named confirmer and diary system of record, the
   result is `NOT READY`.
1. Record the decision, the decision-maker, the tribunal and the
   lawyer-supplied notification date as an assumption. A contested or unknown
   date is `NOT READY`. Criminal matters are `OUTSIDE SCOPE`.
2. Open the tribunal's table in [computation rules](../../references/computation-rules/)
   (`art`, `ncat`, `qcat`, `vcat`) and copy the general period: citation,
   length and unit, rollover, warnings, source URL and evidence state. For ART
   steps ask which registry the act is to be done in if the profile names no
   `registry_holiday_table`. The Act conferring the decision often fixes its
   own period (for QCAT, s 6(7) of the QCAT Act says so expressly). Name it and route its
   verification through the matching legislation checker. VCAT has no general
   period, so name the enabling provision. For other tribunals name the
   enabling Act.
3. Never state, estimate or adjust a date, never present a candidate as the
   binding deadline, and never conclude that a period
   has expired or been extended.
4. On every migration matter include the warning that migration time limits are
   non-extendable or jurisdictional and have changed repeatedly, and flag
   specialist review before reliance.

Lead with `READY FOR HUMAN REVIEW` (only for a workbook candidate a person
supplied), `IDENTIFY-ONLY - NOT COMPUTED`, `NOT READY` or `OUTSIDE SCOPE`.

```text
Decision: <decision; decision-maker; tribunal; notification date assumption>
Candidates: <period; basis; source; evidence state; result: not computed or workbook candidate as read by <person>>
Conferring-Act check: <provision named or routed; evidence state>
Migration warning: <present on every migration matter; specialist review>
Inputs needed: <notification date, registry holiday table, conferring Act period>
Human decision gate: <confirmer; decisions required; diary entry pending>
Limitations: <identify-only; enabling enactment may differ; not a diary system>
```
