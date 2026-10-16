---
name: map-tribunal-review-deadlines
description: Map and compute candidate merits-review and tribunal deadlines for Australian administrative and civil decisions, with computed coverage staged to the ART, NCAT, QCAT and VCAT and identify-only output for other tribunals, using the bundled deterministic script — never model arithmetic. Every migration-review output carries a mandatory non-extendable and jurisdictional-deadline warning with a specialist-review flag. Use when a practitioner needs candidate review or internal-appeal deadlines after a government or tribunal decision. Do not use for criminal matters, to conclude that a period has expired or been extended, or when the notification date is contested — those fail closed to the responsible lawyer.
---

# Map Tribunal Review Deadlines

Map candidate review deadlines from the tribunal computation-rule tables and
compute only through the bundled script. The enabling enactment frequently
fixes its own period — the general tribunal layer is a candidate, never a
conclusion.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md),
use an approved profile per the
[deadline profile schema](../../references/deadline-profile-schema.md), and
run [compute_deadline.py](../compute-procedural-deadlines/scripts/compute_deadline.py)
against the [computation-rule tables](../../references/computation-rules/).

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
   - Run the script per candidate. Report `computed` and `identify_only`
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
