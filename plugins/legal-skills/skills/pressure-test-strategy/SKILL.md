---
name: pressure-test-strategy
description: Challenge a qualified lawyer's procedural and commercial strategy choices, including forum, timing, settlement bands, and escalation, for unstated risks and path dependence. Use on the lawyer-supplied jurisdiction and record. Do not use to file, to contact a counterparty, or to pick a forum the lawyer did not name.
---

# Pressure-test strategy

Challenge the lawyer's choice of forum, timing, settlement, or escalation.
Name unstated risks and path dependence. Do not take the step. Jurisdiction is lawyer-supplied.
A qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. State the choice in the lawyer's words. If they named no choice, ask one
   bounded question and return `NOT READY`.
3. List risks the lawyer did not state that follow from the supplied facts.
   If a risk needs a legal rule or a forum practice that was not supplied,
   write `cannot tell from the supplied record` and name the missing input.
4. State the path dependence. What later choice becomes harder, or closes, if
   this choice is taken. Use only consequences the supplied facts support, or
   label the consequence as an assumption.
5. Do not recommend a replacement forum, a filing date, or a settlement
   number. You may show how the lawyer's own alternatives, if they stated
   any, change the risks.
6. If the lawyer asks you to file, send, or contact a counterparty, refuse
   that part. Keep the challenge when a choice was stated.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Choice: <forum, timing, settlement band, or escalation, in the lawyer's words>
Unstated risks: <risk; supplied fact it rests on, or missing input>
Path dependence: <what a later choice loses or gains>
Alternatives the lawyer already named: <alternative; how the risk changes>
Refused: <any request to file or contact>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a challenge, not a decision to take the step>
```

Use `READY FOR HUMAN REVIEW` when the choice is stated and every risk is tied
to the record or labelled as a gap. Use `READY WITH QUALIFICATIONS` when a
material risk cannot be assessed without a missing input and you have said
so. Use `NOT READY` when no choice was stated. Use `OUTSIDE SCOPE` when the
request is only to file, to contact someone, or to pick a forum the lawyer
did not name.

## Fail closed

Never file a document. Never contact a counterparty or send a settlement
figure. Never pick a forum, a date, or a number the lawyer did not propose.
Never invent a procedural rule. Never replace a gap with model memory. Write
`cannot tell from the supplied record` instead. Never give final legal
advice.

## Example

The lawyer plans to file tomorrow and to email a settlement band of 40 to 50.
The record does not show a response deadline. The skill flags that the filing
may close the settlement path, and that the deadline for filing was not
supplied. It does not send the email or file.
