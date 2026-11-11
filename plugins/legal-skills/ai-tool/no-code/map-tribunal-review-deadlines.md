# No-code procedure: map tribunal review deadlines

Use this when the host cannot run code. It replaces the deterministic
computation step of [this skill](SKILL.md). The model never does date
arithmetic.

For a tribunal general period that is in the tables (`art`, `ncat`, `qcat`),
a person reads the candidate date from
[deadline-calculator.xlsx](../../references/deadline-calculator.xlsx),
following the [compute-procedural-deadlines procedure](../compute-procedural-deadlines/no-code.md).
Everything else stays identify-only.

## Steps

1. Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
   and confirm the approved profile, the named confirmer and the diary system
   of record. Without them the result is `NOT READY`.
2. Record the decision, the decision-maker, the tribunal and the
   lawyer-supplied notification date as an assumption. A contested or unknown
   date is `NOT READY`. Criminal matters are `OUTSIDE SCOPE`.
3. Check the conferring Act first. It often fixes its own period (for QCAT,
   s 6(7) of the QCAT Act says so). Name the provision and route its
   verification through the matching legislation checker. When the conferring
   Act fixes the period, the workbook's general period does not apply: the
   result for that candidate is identify-only, `not computed`.
4. VCAT has no general period. Name the enabling provision; identify-only.
5. Only for a general period that applies, a person picks the tribunal row in
   the Calculator sheet (`art / art-general-review-application`,
   `ncat / ncat-internal-appeal`, `qcat / qcat-review-application`). The
   `art / migration-judicial-review` row is the statutory time limit for
   judicial review in a court, not a tribunal general period: treat it as
   identify-only here and flag specialist review. For the ART pick the registry holiday
   table. The person supplies the Status, Candidate date, Reason and Warnings
   cells as text.
6. Never conclude that a period has expired or been extended, and never
   present a candidate as the binding deadline.
7. On every migration matter include the warning that migration time limits
   are non-extendable or jurisdictional and have changed repeatedly, and flag
   specialist review before reliance.

## Report

```text
Decision: <decision; decision-maker; tribunal; notification date assumption>
Candidates: <period; basis; source; evidence state; workbook result as read by <person> | not computed>
Conferring-Act check: <provision named or routed; evidence state>
Migration warning: <present on every migration matter; specialist review>
Inputs needed: <notification date, registry holiday table, conferring Act period>
Human decision gate: <confirmer; decisions required; diary entry pending>
Limitations: <candidate only; enabling enactment may differ; not a diary system>
```
