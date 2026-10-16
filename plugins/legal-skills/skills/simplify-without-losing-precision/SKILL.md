---
name: simplify-without-losing-precision
description: Force a plain-language restatement of a legal position that a non-lawyer client could follow, then flag where simplification hid a material nuance, for a qualified lawyer using a lawyer-supplied jurisdiction and record. Use when the lawyer wants that check. Do not use to send the restatement to the client or to drop a qualification silently.
---

# Simplify without losing precision

Restate the position in language a non-lawyer client could follow. Then flag
every material nuance the plain version hid. Jurisdiction is lawyer-supplied.
A qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Restate the position in short sentences. Keep names, dates, and numbers
   that the lawyer supplied. Do not add a legal conclusion that was not in
   the position.
3. Compare the plain version with the lawyer's version, sentence by sentence.
   Flag a hidden nuance wherever the plain version drops a condition, a
   burden, a date limit, a party, or a "we do not yet know".
4. If you cannot tell whether a dropped phrase was material, write `cannot
   tell from the supplied record` and quote the dropped phrase.
5. Do not send the restatement to the client. Do not present the plain
   version as the advice.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Plain restatement: <short sentences a non-lawyer could follow>
Hidden nuance: <what the plain version dropped; why it is material>
Could not tell: <dropped phrase; cannot tell from the supplied record>
Not sent: <the restatement stays with the lawyer>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a check on wording, not client advice>
```

Use `READY FOR HUMAN REVIEW` when the position is supplied and every material
drop is flagged. Use `READY WITH QUALIFICATIONS` when you flagged a drop whose
materiality you cannot judge from the record. Use `NOT READY` when no
position was supplied. Use `OUTSIDE SCOPE` when the request is only to send
the text to the client, or to certify that the plain version is complete
advice.

## Fail closed

Never drop a qualification silently. Never add a legal rule to make the plain
version sound complete. Never invent an authority. Never send, file, or
publish the restatement. Never assume a legal system. Never replace a doubt
with model memory. Write `cannot tell from the supplied record` instead.
Never give final legal advice.

## Example

The lawyer's sentence is that the client can end the contract if the goods
are late, provided notice is given within five days and the lateness is not
excused. The plain version says the client can end the contract if the goods
are late. The skill flags the notice condition and the excuse condition as
hidden nuance.
