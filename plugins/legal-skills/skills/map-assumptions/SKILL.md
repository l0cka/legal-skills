---
name: map-assumptions
description: Extract explicit and hidden assumptions in a qualified lawyer's analysis, rank which ones the case turns on, and propose how each could be tested or falsified, using only the lawyer-supplied jurisdiction and record. Use when the lawyer wants the load-bearing assumptions visible. Do not use to fill a gap from memory or to give final legal advice.
---

# Map assumptions

Pull the assumptions out of the analysis, including the ones the lawyer did
not state. Rank the ones the case turns on. Say how each could be falsified.
Jurisdiction is lawyer-supplied. A qualified lawyer owns the outcome.

Read [the sparring session contract](../../references/sparring-contract.md)
before responding.

## Workflow

1. Build the session record. If the operator is not a qualified lawyer and is
   not working under one, stop with `OUTSIDE SCOPE`.
2. List assumptions the lawyer stated. Quote or closely paraphrase their
   words, and note where in the prompt they appear.
3. List hidden assumptions. A hidden assumption is a proposition the analysis
   needs and does not state. Tie each one to the sentence that needs it.
4. Rank them. Put first the assumptions on which the conclusion falls if the
   assumption is false. Put the rest after. Say why the rank is what it is,
   using only the supplied analysis.
5. For each assumption, propose one test or falsifier that uses a document,
   a fact, or an authority the lawyer could supply. If you cannot name a
   test without inventing a legal rule, write `cannot tell from the supplied
   record` and describe the missing input.
6. Do not decide whether an assumption is true.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Session: <matter label; jurisdiction, forum, governing law as supplied or not supplied>
Explicit assumptions: <assumption; where the lawyer stated it>
Hidden assumptions: <assumption; the sentence that needs it>
Rank: <assumption; why the case turns on it, or why it does not>
Falsifier: <what would show the assumption is false; or the missing input>
Assumptions about this map: <any inference you added, and what would falsify it>
Ownership: <qualified lawyer>
Limitations: <a map, not a finding that an assumption is true>
```

Use `READY FOR HUMAN REVIEW` when the analysis is supplied and every
assumption has a rank and a falsifier or a labelled gap. Use `READY WITH
QUALIFICATIONS` when a falsifier cannot be stated without a missing input and
you have said so. Use `NOT READY` when there is no analysis to map. Use
`OUTSIDE SCOPE` when the request is only for a ruling that the analysis is
correct, or for a legal rule you would have to invent.

## Fail closed

Never decide that an assumption is true or false. Never invent an authority
to supply a falsifier. Never assume a legal system. Never fill a silence
with model memory. Write `cannot tell from the supplied record` instead.
Never give final legal advice.

## Example

The lawyer writes that the buyer is bound because they took delivery. The map
lists a hidden assumption that delivery was the mode of acceptance the quote
allowed. The falsifier is the quote's acceptance term, which was not
supplied. The skill does not say whether a contract was formed.
