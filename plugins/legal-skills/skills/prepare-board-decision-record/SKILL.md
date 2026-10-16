---
name: prepare-board-decision-record
description: Prepare controlled draft Australian company board materials, including an agenda item, board paper, proposed resolution, written-resolution scaffold or draft minutes extract, from verified law, an approved governance profile and supplied evidence. Use before a decision or to document a completed meeting from authorised notes. Do not invent attendance, quorum, disclosures, deliberations, votes, reasons or approval; execute or circulate documents; or determine legal validity.
---

# Prepare Board Decision Record

Draft the smallest record needed for an authorised reviewer. A proposed
resolution is not a decision. Draft minutes are not evidence of events unless
the user supplies authorised records of those events.

Read the [source and control method](../../references/governance-source-and-control-method.md)
and use the approved [profile schema](../../references/governance-profile-schema.md).

## Workflow

1. Classify the requested record.
   - Choose one or more: agenda item, board paper, proposed meeting resolution,
     proposed circulating resolution, or draft minutes extract.
   - Mark every output `DRAFT – NOT APPROVED`. Separate pre-decision proposals
     from post-meeting records.
2. Confirm authority and mechanics.
   - Require the approved profile plus the current constitution, replaceable-rule
     posture, reserved-matters and delegation sources relevant to the decision.
   - Use `$check-commonwealth-legislation` to verify any statutory rule for
     directors' meetings, circulating resolutions, interests, voting or minutes
     at the relevant date. Do not use a generic board template as authority.
3. Assemble the evidence pack.
   - Identify the decision sought, alternatives, material risks, financial and
     solvency information, stakeholder effects, conflicts, recommendations and
     follow-up owner from supplied material only.
   - Use placeholders such as `[NOT PROVIDED – HUMAN INPUT REQUIRED]` for every
     absent fact. Do not smooth over inconsistent papers.
4. Draft with event controls.
   - A proposed resolution uses prospective language and identifies conditions.
   - A minutes extract may record attendance, quorum, disclosed interests,
     abstentions, deliberations, votes and reasons only where authorised notes
     or a human instruction expressly records each event.
   - Keep the legal-source note and the corporate record separate. Do not insert
     privileged advice into minutes without an authorised human decision.
5. Provide an approval checklist.
   - Identify factual, legal, governance, privilege and execution reviewers.
   - State that circulation, signature, entry in minute books, notification and
     filing remain outside the workflow.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Requested record: <type and decision>
Record status: DRAFT – NOT APPROVED
Entity, meeting and relevant date: <supplied facts or placeholders>
Authority basis: <verified law and approved document clauses>
Conflicts and participation: <supplied evidence or unresolved placeholders>
Draft material: <agenda / paper / resolution / minutes extract>
Conditions and follow-up: <owner, trigger and evidence>
Unresolved facts: <bounded list>
Verified legal sources: <official URLs, provisions, versions and checked date>
Approval checklist: <factual, legal, governance, privilege and execution gates>
Limitations: <not evidence of events and not legally effective>
```

## Fail closed

Return `NOT READY` rather than drafting operative wording when decision
authority, required participation, a material conflict, current source or
decisive fact is unresolved. Never invent attendance, quorum, notice,
disclosure, abstention, discussion, vote, reason, signature or approval. Never
backdate, execute, circulate, send, enter in a minute book or file any record.
