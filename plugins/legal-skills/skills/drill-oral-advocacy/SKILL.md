---
name: drill-oral-advocacy
description: Run a short hostile question-and-answer or opening or closing drill on a named issue, and score clarity, concessions, and recovery, for a qualified lawyer. Use on the lawyer-supplied jurisdiction and record. Do not use to invent transcript authority or to predict the decision-maker's ruling as certainty.
---

# Drill oral advocacy

Run a short hostile drill on one named issue. Score clarity, concessions, and
recovery. Do not invent a transcript. Jurisdiction is lawyer-supplied. A
qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. Name the issue and the drill type. The drill is hostile questions, an
   opening, or a closing, as the lawyer asked. If they named no issue, ask
   one bounded question and return `NOT READY`.
3. Ask at most five hostile questions, or give one short opening or closing
   of the lawyer's position using only the supplied record, then ask the
   lawyer to deliver it. Do not write a speech that adds facts.
4. When the lawyer answers, score three things, each as high, mixed, or low,
   with one sentence of reason tied to their words.
   Clarity means a listener could repeat the point.
   A concession means they gave up a fact or a limit that was in the record.
   Recovery means they repaired a concession or a muddle on the next answer.
5. If they have not answered yet, do not score. Ask the questions and stop.
6. If a question would need a transcript, a direction, or an authority that
   is not in the record, do not invent it. Write `cannot tell from the
   supplied record` and ask a question that stays inside the record.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Issue: <as named>
Drill: <hostile questions, opening, or closing>
Prompts: <question or the short drill text; supplied fact it uses>
Scores: <clarity; concession; recovery; or not yet, because the lawyer has not answered>
Invented authority: <none>
Assumptions: <each assumption and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a drill score, not a prediction of the ruling>
```

Use `READY FOR HUMAN REVIEW` when the issue is named and the prompts use only
the supplied record. Use `READY WITH QUALIFICATIONS` when a prompt is weaker
because a fact is missing and you have said so. Use `NOT READY` when no issue
was named. Use `OUTSIDE SCOPE` when the request is only for a fabricated
transcript or a certain prediction of the ruling.

## Fail closed

Never invent a transcript, a judicial question from a real case, or a
quotation. Never score before the lawyer answers. Never predict the ruling as
a certainty. Never assume a legal system. Never replace a gap with model
memory. Write `cannot tell from the supplied record` instead. Never give
final legal advice.

## Example

The lawyer asks for three hostile questions on whether notice arrived by 1
March. The record has a 2 March receipt and no clause. The drill asks what
the lawyer will say the receipt proves, and what they will say if the clause
is not in the bundle. It quotes no case. It does not score until the lawyer
answers.
