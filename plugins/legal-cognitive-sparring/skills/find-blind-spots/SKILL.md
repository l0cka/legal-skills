---
name: find-blind-spots
description: List material questions, facts, parties, procedures, or authorities a qualified lawyer has not yet addressed, and separate must-check items from nice-to-have, using only the lawyer-supplied jurisdiction and record. Use when the lawyer wants a gap list. Do not use to invent the missing authority or to decide the point.
---

# Find blind spots

List what the lawyer has not addressed. Split must-check items from
nice-to-have. Do not decide the missing points. Jurisdiction is lawyer-supplied.
A qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Restate the issue the lawyer says they are working. If they did not state
   an issue, ask one bounded question and return `NOT READY`.
3. Walk the supplied record for questions, facts, parties, procedures, and
   authorities that the issue needs and the lawyer has not addressed.
4. Put an item in must-check only when the lawyer's own conclusion depends on
   it. Put the rest in nice-to-have. Say, in one line, why the item is in
   that list.
5. Do not supply the missing authority, the missing fact, or the missing
   step. Write `cannot tell from the supplied record` beside each gap.
6. If the lawyer asks you to answer a gap, refuse the answer and keep the
   item on the list.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Issue: <as the lawyer stated it>
Must-check: <gap; question, fact, party, procedure, or authority; why the conclusion depends on it>
Nice-to-have: <gap; why it can wait>
Not a gap: <item the lawyer already addressed, so it is not listed as missing>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a list of gaps, not answers to them>
```

Use `READY FOR HUMAN REVIEW` when the issue is stated and every gap is sorted
and tied to the record. Use `READY WITH QUALIFICATIONS` when you are unsure
whether an item is must-check and you have labelled that doubt. Use
`NOT READY` when no issue was stated. Use `OUTSIDE SCOPE` when the request is
only for the answer to a gap, or for an authority you would have to invent.

## Fail closed

Never answer the gap you have listed. Never invent an authority, a party, or
a procedural step. Never assume a legal system. Never fill a silence with
model memory. Write `cannot tell from the supplied record` instead. Never
give final legal advice.

## Example

The lawyer analyses a claim by one named buyer and does not mention a second
company named on the quote as the addressee. The second company is a
must-check party. The skill does not say whether that company is bound.
