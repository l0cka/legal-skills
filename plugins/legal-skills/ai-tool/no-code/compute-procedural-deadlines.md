# No-code procedure: compute procedural deadlines

Use this when the host cannot run code. It replaces the deterministic
computation step of [this skill](SKILL.md) with a spreadsheet a person
completes. The model never does date arithmetic: it identifies the rule and
the inputs, and a person reads the date from the workbook.

The workbook is [deadline-calculator.xlsx](../../references/deadline-calculator.xlsx).
It is built from the same [computation-rule tables](../../references/computation-rules/)
and [holiday tables](../../references/holidays/) as this release, and its
formulas reproduce every refusal of the deterministic computation. Open it in
Excel or another spreadsheet that recalculates formulas.

## Before you start

1. Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md).
2. Have an approved profile per the
   [deadline profile schema](../../references/deadline-profile-schema.md),
   a named confirmer and a diary system of record. Without them the workbook
   shows `NOT READY` and no date.
3. Criminal procedure, and court-fixed or discretionary dates, are outside the
   workbook. Its Scope sheet lists what it does not cover.

## Steps

1. The model fixes the forum, the procedural step and the governing rule
   from the tables, and states the lawyer-supplied trigger event and date as
   an assumption. It names the row to pick (`<table id> / <rule id>`).
2. A person opens the Calculator sheet and fills the yellow cells: forum and
   rule, trigger event, trigger date, whether the date is contested, matter
   type, the registry holiday table (federal courts and the ART only), the
   approved profile, whether it is approved, the confirmer and the diary
   system.
3. The person reads the Status cell:
   - `CANDIDATE DATE - NOT BINDING UNTIL CONFIRMED`: a candidate date and day
     are shown with the provisions applied, warnings and holiday caveats.
   - `IDENTIFY-ONLY - NOT COMPUTED`: the Reason cell says why (unverified
     rule, provision or holiday table, a date outside coverage or in an
     uncertain window, a short period that counts only business days, a
     rollover into an excluded range). Do not count around it.
   - `NOT READY` or `OUTSIDE SCOPE`: a gate failed; the Reason cell names it.
4. The person gives the model the Status, Candidate date, Reason and Warnings
   cells as text. Never upload a filled workbook to the AI tool: its Engine
   and Working sheets hold working dates with no gate applied. The model reports them as supplied and never adjusts,
   rounds or re-derives a date.
5. A candidate is never the binding deadline. The named confirmer confirms
   the date against the official source and enters it in the diary system of
   record before any reliance.

## Holiday tables

Each State and Territory forum uses its own table. For federal courts and the
ART pick the table of the registry where the act is to be done. For a
registry not listed, fill the `custom` column of the Holidays sheet and its
HolidayTables row (evidence `verified`, coverage dates, source and who
verified it). Until that row says `verified` and names the source and the
verifier, the workbook refuses. It takes up to 100 dates; rows below are
ignored.

## Report

Lead with `READY FOR HUMAN REVIEW` when the workbook shows a candidate date,
otherwise with `IDENTIFY-ONLY - NOT COMPUTED`, `NOT READY` or `OUTSIDE SCOPE`
as the workbook shows. Use the result contract in the skill's AI-tool mode
section, filled from the workbook cells:

```text
Step: <forum; procedural step; governing rule citation>
Trigger: <lawyer-supplied trigger event and date; stated as assumption>
Rule: <period rule id; period length and unit; rollover>
Source: <Source cell; Evidence cell>
Inputs needed: <trigger date, registry location, holiday table, court directions>
Result: <workbook candidate date and day, as read by <person> | not computed, with the Reason cell>
Warnings: <Warnings and Holiday caveats cells>
Human decision gate: <confirmer; diary entry pending confirmation>
Limitations: <identify-only or workbook candidate; not a diary system; every date needs confirmation>
```

If nobody can open the workbook, fall back to the identify-only output in the
skill's AI-tool mode section: `Result: not computed`.

## Limits

- A table entry verified after this release reaches the workbook only in the
  next release. Do not edit the Rules, Engine or Working sheets.
- Counting is scanned up to 120 days and a rollover up to 15 days; longer
  periods are refused.
- The workbook is not a diary system and never makes a date binding.
