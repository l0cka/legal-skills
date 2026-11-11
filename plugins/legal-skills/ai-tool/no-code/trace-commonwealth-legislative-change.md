# No-code procedure: trace Commonwealth legislative change

Use this when the host cannot run code. It replaces the change-trace lookup
in [this skill](SKILL.md) with a side-by-side comparison a person or a
browsing tool makes. A spreadsheet cannot stand in for this: the
compilations are live records on the official register, and whether a
change matters is a legal judgement.

Method: [change tracing method](references/change-tracing-method.md).

## Steps

1. Open the title on `legislation.gov.au` and its All versions page. List
   every compilation between the two dates, including both endpoints.
2. Open the provision in each compilation and copy its text into the table
   below, one row per compilation.
3. Compare each row with the one before. Mark where the text changes,
   reverts or is absent. Any difference in wording, numbering or heading is a
   change.
4. For each change, read the compilation endnotes and amendment history to
   find the amending Act or instrument and the schedule item. Open that Act
   to confirm its commencement.

## Comparison table

| Compilation | Register ID | Start date | End date | Provision text (or absent) | Changed from previous? | Amending law and item | Commencement confirmed |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Result

If the compilations could not be opened, return `NOT VERIFIED` with the steps
above and ask the person to supply them. Otherwise follow the skill's result
contract, cite only pages opened and say that the comparison was manual.
