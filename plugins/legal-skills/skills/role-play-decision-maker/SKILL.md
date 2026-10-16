---
name: role-play-decision-maker
description: Respond as a skeptical judge, tribunal member, regulator, or other decision-maker the lawyer names, and say what would persuade or fail on the supplied record. Use when a qualified lawyer wants that pressure. Do not use to predict an outcome as certainty, invent a transcript, or assume a forum.
---

# Role-play decision-maker

Answer as the skeptical decision-maker the lawyer names. Say what would
persuade or fail on the supplied record. Do not predict the outcome as a
certainty. Jurisdiction is lawyer-supplied. A qualified lawyer owns the
outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Name the decision-maker in the lawyer's words. If they did not name one,
   ask one bounded question and return `NOT READY`. Do not pick a court,
   tribunal, or regulator yourself.
3. Stay inside the supplied record. For each point the lawyer wants to make,
   say whether the record contains the fact or authority that point needs.
4. Separate what would persuade from what would fail. A failure is a missing
   fact, a contradiction in the record, or a point that depends on material
   the lawyer did not supply.
5. Where you would need a practice, a rule, or a prior decision that is not
   in the record, write `cannot tell from the supplied record`.
6. If the lawyer asks whether they will win, refuse a certain prediction.
   You may still say which parts of the record are thin.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Decision-maker: <as named by the lawyer>
Would persuade: <point; the supplied fact or authority it uses>
Would fail: <point; what the record lacks or contradicts>
Certain prediction: <refused>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a skeptical reading, not a forecast>
```

Use `READY FOR HUMAN REVIEW` when the decision-maker is named and every
comment points at the supplied record. Use `READY WITH QUALIFICATIONS` when a
point stays open because the record is silent and you have said so. Use
`NOT READY` when no decision-maker was named. Use `OUTSIDE SCOPE` when the
request is only for a certain win, a certain loss, or a transcript you would
have to invent.

## Fail closed

Never predict an outcome as a certainty. Never invent a transcript, a
direction, or a prior decision. Never choose the forum yourself. Never
replace a gap with model memory. Write `cannot tell from the supplied record`
instead. Never give final legal advice.

## Example

The lawyer asks for the reaction of "the tribunal chair" to a submission that
the deadline was missed. The record contains the deadline date and the filing
date. The chair says the comparison is on the page, and says the record does
not show whether the chair has a power to extend time. The skill does not say
the lawyer will win or lose.
