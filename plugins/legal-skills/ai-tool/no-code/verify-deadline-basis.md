# No-code procedure: verify deadline basis

Use this when the host cannot run code. Every step of [this skill](SKILL.md)
applies except the table fingerprint, which stays not computed.

A spreadsheet cannot do this honestly. The fingerprint is not computed here:
it is a digest of the exact table bytes, so the model and the person never
state, estimate or invent one. A person with code access computes and compares
it before an update is applied.

## Manual change check

For each table entry the matter relies on, fill one row:

| Table | Entry id | Field | Previous text | Current official text | Same? | Source URL | Version | Checked date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

1. Copy the previous table entry and the official current text side by side.
2. Compare every field the computation relies on: citation, period length
   and unit, trigger, rollover, excluded ranges, short-period threshold,
   holidays, coverage dates and uncertain windows.
3. Mark any difference in wording, number, date or source URL as a change.
   Never reconcile a difference silently.
4. Record the outcome per entry: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`
   or `NOT VERIFIED`, with source URL, version identifier and checked date.
5. Write `fingerprint not computed, a person with code computes it` in the
   Changes line of the result.

## Effect on the deadline workbook

[deadline-calculator.xlsx](../../references/deadline-calculator.xlsx) is
built from the tables of this release. A table update applied after release
reaches the workbook only in the next release. Until then, a rule or holiday
table that changed is identify-only for that matter. For a registry whose
holidays are not in the release, the workbook's `custom` holiday column takes
dates that this procedure has verified.
