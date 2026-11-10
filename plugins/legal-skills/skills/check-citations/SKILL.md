---
name: check-citations
description: Check every case citation, legislation reference and quoted passage in a draft against the official publishers and return one status table. Run by typing it with the draft; never marks a reference verified itself.
disable-model-invocation: true
argument-hint: "[paste or attach the draft]"
---

# Check Citations

## Scope

A whole-document pass over a draft such as an affidavit, submissions, advice
or a memo. It finds every Australian case citation, legislation reference and
quoted judicial passage, sends each one to the skill that verifies it, and
collects the results in one table. It runs only when the user types it. For a
single citation, the verification skills trigger on their own.

Read
[../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
and [../../references/point-in-time-method.md](../../references/point-in-time-method.md)
before checking. They define the outcomes each verifier may return. This
skill only finds, routes and collects; only a verifier that inspected the
official publisher may report `VERIFIED`.

## Workflow

1. Take the draft from the text typed after the command or the attached
   document. If there is none, ask for it. Ask for the date the law must be
   checked at if the draft does not make it clear; otherwise use today and
   say so.
2. Extract every reference, recording where it appears (paragraph, page or
   footnote) and its exact wording:
   - case citations, medium-neutral or reported, and bare case names relied
     on as authority;
   - legislation references: Act or instrument, jurisdiction and provision;
   - passages quoted from a judgment.
   Number them in document order. State the total found.
3. Route each one:
   - case citations through `$route-case-citation`, which hands each to its
     verifier;
   - quoted passages to `$verify-case-quote`, after the case itself;
   - Commonwealth legislation to `$check-commonwealth-legislation`, and state
     and territory legislation to `$check-nsw-legislation`,
     `$check-victoria-legislation`, `$check-queensland-legislation`,
     `$check-western-australia-legislation`,
     `$check-south-australia-legislation`, `$check-tasmania-legislation`,
     `$check-act-legislation` or `$check-northern-territory-legislation`;
   - anything else (a foreign authority, a secondary source, a reference the
     plugin has no verifier for) to `not checked`, with the reason.
4. Check every reference. Never sample. If the session cannot finish all of
   them, list the ones not reached by number so the user can run the rest.
5. If the draft is to be filed in an Australian court or tribunal and the
   user says AI helped prepare it, add a line recommending
   `$check-court-ai-protocol` for the filing rules. Do not run it unasked.
6. Report using the result contract.

## Result contract

Lead with `READY FOR HUMAN REVIEW` when every reference returned a verifier
outcome, `READY WITH QUALIFICATIONS` when any was `not checked` or not
reached, `NOT READY` when no draft was supplied, or `OUTSIDE SCOPE` when the
draft contains no Australian references.

```text
Draft: <title or description; checked as at <date>>
References found: <total>; checked: <n>; not checked: <n>; not reached: <n>
| # | Where | As written | Type | Checked by | Outcome | Official source | Note |
Flags for review: every NOT FOUND, NOT VERIFIED and VERIFIED WITH
  QUALIFICATIONS row, with the verifier's reason
Not checked or not reached: <# and reason>
```

Copy each outcome exactly as its verifier returned it. Sort nothing out of
document order. A `NOT FOUND` row is a flag for a lawyer to confirm, not a
finding that the authority was fabricated.

## Fail closed

Never report an outcome a verifier did not return, upgrade `UNVERIFIABLE` to
`VERIFIED`, or treat `UNVERIFIABLE` as `NOT FOUND`. Never check a reference
from memory or search results alone. Never correct or rewrite the draft,
assess whether an authority supports the proposition, or analyse its
treatment; those stay with the lawyer. Never drop a reference from the table
to shorten it.
