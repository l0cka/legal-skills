---
name: steelman-then-attack
description: Restate a qualified lawyer's position in its strongest form, then attack that steelman in a separate phase, using only the lawyer-supplied jurisdiction and record. Use when the lawyer wants both phases kept visible. Do not use to merge the phases, give final legal advice, or invent an authority.
---

# Steelman then attack

First strengthen the lawyer's position. Then attack that strengthened
position. Keep the phases separate. Jurisdiction is lawyer-supplied. A
qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Phase 1, steelman. Restate the position in the strongest form the supplied
   record supports. Use only supplied facts and supplied authorities. You may
   tighten wording and drop a weak aside. You may not add a fact or an
   authority.
3. Mark any strengthening you wanted to make and could not, because the
   record is silent, as `cannot tell from the supplied record`.
4. Phase 2, attack. Attack only the steelman from phase 1. Do not attack a
   weaker version the lawyer did not need. For each blow, point at the
   steelman sentence it hits.
5. Do not put an attack inside phase 1, and do not improve the steelman
   inside phase 2.
6. If the lawyer asks for a final view of who is right, refuse that view.
   Leave both phases on the page.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Position as given: <the lawyer's words>
Phase 1 steelman: <strengthened position; supplied fact or authority used>
Could not strengthen: <gap>
Phase 2 attack: <blow; the steelman sentence it hits>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <both phases are sparring, not a ruling>
```

Use `READY FOR HUMAN REVIEW` when both phases are present, separated, and
grounded in the supplied record. Use `READY WITH QUALIFICATIONS` when a
strengthening or a blow stays open because the record is silent and you have
said so. Use `NOT READY` when no position was stated. Use `OUTSIDE SCOPE`
when the request is only for a ruling on who is right, or for an authority
you would have to invent.

## Fail closed

Never merge the phases. Never add a fact or authority while steelmanning.
Never invent a citation in the attack. Never declare a winner. Never replace
a gap with model memory. Write `cannot tell from the supplied record`
instead. Never give final legal advice.

## Example

The lawyer says notice was late because it arrived on 2 March and the
contract required notice by 1 March. The steelman uses only those two
supplied points. The attack asks whether the record shows that 1 March was a
day the clause actually counts, and stops when the clause text is absent. It
does not decide the point.
