---
name: clarify-burden-and-standard
description: Force a precise statement of who bears which burden, under what standard, and what evidence would meet or fail it on the supplied facts, for a qualified lawyer. Use when the lawyer wants that allocation made explicit. Do not use to invent a standard the lawyer did not supply or to decide that the burden is met.
---

# Clarify burden and standard

Make the lawyer state who bears which burden, under what standard, and what
evidence would meet or fail it. Use only the supplied facts and the standard
the lawyer supplies. Jurisdiction is lawyer-supplied. A qualified lawyer owns
the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. List each issue the lawyer wants a burden for. Use their labels.
3. For each issue, record who the lawyer says bears the burden, and the
   standard they state. Copy their words. If they did not state one, write
   `not supplied` for that field. Do not supply a standard from memory.
4. On the supplied facts only, say what evidence would meet the stated
   standard and what evidence would fail it. If the facts do not show either,
   write `cannot tell from the supplied record`.
5. Do not decide that the burden is met or not met.
6. If no burden and no standard were stated, ask one bounded question and
   return `NOT READY` rather than inventing them.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Issue: <the lawyer's label>
Who bears it: <as stated, or not supplied>
Standard: <as stated, or not supplied>
Evidence that would meet it: <supplied fact, or cannot tell from the supplied record>
Evidence that would fail it: <supplied fact, or cannot tell from the supplied record>
Decision on the burden: <not made>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a statement of the allocation, not a finding>
```

Use `READY FOR HUMAN REVIEW` when the lawyer has stated the bearer and the
standard and you have tested only the supplied facts against them. Use
`READY WITH QUALIFICATIONS` when the bearer or the standard is missing and
the rest of the statement is still usable with that gap labelled. Use
`NOT READY` when there is no issue to allocate. Use `OUTSIDE SCOPE` when the
request is only for a finding that the burden is met, or for a legal standard
you would have to invent.

## Fail closed

Never invent a burden or a standard. Never decide that the burden is
discharged. Never assume a legal system. Never replace a missing standard
with model memory. Write `cannot tell from the supplied record` when the
facts do not show the evidence either way. Never give final legal advice.

## Example

The lawyer says the claimant bears the burden and that the standard is the
balance of probabilities, and supplies one witness who saw delivery and none
who contradicts it. The skill records that allocation in the lawyer's words.
It says a contradictory witness is not in the record. It does not find that
the burden is met.
