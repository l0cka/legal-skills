---
name: pressure-test-argument
description: Stress-test a qualified lawyer's own reasoning on premises, leaps, missing authorities, adverse facts, and weaker framings, using only the lawyer-supplied jurisdiction and record. Use when the lawyer wants structured critique of an argument they already hold. Do not use to rewrite the critique as final legal advice, invent a citation, or assume a legal system.
---

# Pressure-test argument

Return a structured critique of the lawyer's argument. Do not rewrite it as
final advice. Jurisdiction is lawyer-supplied. A qualified lawyer owns the
outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Restate the argument as given. Separate premises, the inference, and the
   conclusion. Keep the lawyer's legal labels.
3. Mark each premise as supplied, assumed, or missing. Where the record is
   silent, write `cannot tell from the supplied record`.
4. Name each leap. A leap is a step the supplied record does not bridge. Do
   not bridge it.
5. List authorities the argument needs and does not contain. Record them as
   gaps. Do not invent a case, statute, pinpoint, or quotation.
6. List adverse facts that are in the record, and facts the argument needs
   that are absent.
7. Offer at most three weaker framings of the same conclusion. Label each as
   a framing, not as a recommendation to adopt.
8. If the lawyer also asks for a client-ready opinion, a filing, or a message
   to someone else, refuse that part. Still return the critique when the
   argument itself was supplied.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Argument as given: <premises; inference; conclusion>
Premises: <supplied, assumed, or missing, with where it came from>
Leaps: <the unbridged step>
Missing authorities: <gap only>
Adverse and absent facts: <fact in the record that cuts against the argument; fact the argument needs and lacks>
Weaker framings: <framing; what it gives up>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <sparring material, not final legal advice>
```

Use `READY FOR HUMAN REVIEW` when the argument and the record are supplied and
every gap is labelled. Use `READY WITH QUALIFICATIONS` when the critique is
usable and a material premise or authority is missing and labelled. Use
`NOT READY` when there is no argument to test, and ask one bounded question.
Use `OUTSIDE SCOPE` when nothing remains to critique after you refuse final
advice, a filing, contact, or a citation you would have to invent.

## Fail closed

Never rewrite the critique as final legal advice. Never invent an authority.
Never assume a legal system when jurisdiction was not supplied. Never replace
`cannot tell from the supplied record` with model memory. Never file, send, or
contact a third party.

## Example

The lawyer says a contract claim succeeds because a quote was sent and the
buyer later took delivery. The critique marks the unstated premise that the
quote was an offer, marks the leap from delivery to formation, and lists the
acceptance authority as a gap. It names no case.
