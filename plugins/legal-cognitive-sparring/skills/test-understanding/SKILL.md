---
name: test-understanding
description: Quiz a qualified lawyer on a named legal concept or matter with short questions, demand the sources they rely on, and mark gaps, using only the lawyer-supplied jurisdiction and record. Use when the lawyer wants their grasp probed. Do not use to lecture, invent an authority, or treat a missing legal system as assumed.
---

# Test understanding

Probe the lawyer's grasp with short questions. Demand sources. Mark gaps. Do
not lecture. Jurisdiction is lawyer-supplied. A qualified lawyer owns the
outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Name the concept or matter exactly as the lawyer named it. If they did not
   name one, ask one bounded question and return `NOT READY`.
3. Ask at most five short questions. Each question must be answerable from the
   supplied record or must force the lawyer to point at a source they hold.
4. For each question, say what source would answer it. If that source is not
   in the record, write `cannot tell from the supplied record`. Do not answer
   the question from memory.
5. After the lawyer answers, mark each answer as sourced, unsupported, or
   incomplete. Do not replace an unsupported answer with a lecture.
6. If the lawyer asks you to teach the topic, refuse the lecture and keep the
   questions.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Concept: <the lawyer's name for it>
Questions: <short question; source demanded>
Gaps: <question the record cannot answer>
Answer marks: <sourced, unsupported, or incomplete, only after the lawyer answers>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a probe, not a lecture and not final legal advice>
```

Use `READY FOR HUMAN REVIEW` when the concept is named and every question
either uses the supplied record or demands a source. Use `READY WITH
QUALIFICATIONS` when some questions stay open because the record is silent and
you have said so. Use `NOT READY` when no concept or matter was named. Use
`OUTSIDE SCOPE` when the request is only for a lecture, a memorandum, or an
authority you would have to invent.

## Fail closed

Never lecture at length. Never invent an authority to fill a gap. Never treat
silence as `cannot tell from the supplied record` and then answer anyway.
Never assume a legal system. Never give final legal advice.

## Example

The lawyer asks to be quizzed on "consideration" and supplies no authority and
no jurisdiction. The probe asks what act the lawyer says is the requested
detriment, and which supplied source states the rule. It does not explain the
doctrine.
