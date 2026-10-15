---
name: red-team-evidence
description: Challenge the evidence basis of a qualified lawyer's position on provenance, hearsay or weight risks as the lawyer frames them, gaps, and what a competent opponent would attack. Use on the lawyer-supplied record. Do not use to decide admissibility or to invent a source.
---

# Red-team evidence

Challenge the evidence the lawyer is relying on. Stay inside the risks the
lawyer has framed. Do not rule on admissibility. Jurisdiction is lawyer-supplied.
A qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. List each piece of evidence the lawyer relies on. For each, record the
   provenance they gave. Who made it, when, and from what the lawyer says.
3. If provenance is missing, say so. Write `cannot tell from the supplied
   record`. Do not reconstruct a source.
4. Record hearsay and weight risks only in the words the lawyer used to frame
   them. If the lawyer framed no such risk, you may note that an opponent
   could ask about provenance. Do not apply an evidence code from memory.
5. List the attacks a competent opponent would make using only contradictions,
   gaps, and provenance limits that are in the record.
6. Do not decide that an item is admissible, inadmissible, or of a stated
   weight.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Evidence: <item; provenance the lawyer gave, or not supplied>
Risk as framed: <the lawyer's hearsay or weight frame, or not framed>
Opponent's attack: <attack grounded in the record>
Admissibility: <not decided>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a challenge list, not a ruling>
```

Use `READY FOR HUMAN REVIEW` when each relied-on item has a provenance note
and an opponent's attack or an explicit "no attack on this record". Use
`READY WITH QUALIFICATIONS` when provenance is missing and the attack is
limited to that gap. Use `NOT READY` when the lawyer has not identified the
evidence to challenge. Use `OUTSIDE SCOPE` when the request is only for an
admissibility ruling or a source you would have to invent.

## Fail closed

Never decide admissibility or weight. Never invent a document, a witness, or
a quotation. Never import an evidence rule the lawyer did not supply. Never
replace missing provenance with model memory. Write `cannot tell from the supplied record` instead.
Never give final legal advice.

## Example

The lawyer relies on a manager's note of what a driver said about delivery.
The lawyer calls it hearsay and does not supply the driver's own statement.
The skill records that frame and the missing driver statement as the
opponent's attack. It does not rule the note inadmissible.
