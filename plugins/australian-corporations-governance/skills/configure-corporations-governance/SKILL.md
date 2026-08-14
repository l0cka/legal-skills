---
name: configure-corporations-governance
description: Create, revise or validate an organisation-controlled governance profile for an Australian company, recording entity type, regulatory overlays, governing documents, replaceable-rules posture, board authority, delegations, committees, records and approval metadata. Use before other corporations-governance skills or when governance inputs change. Do not use to approve the profile, store client or matter data, decide legal application, or configure a CATSI Act corporation or non-company entity.
---

# Configure Corporations Governance

Create a controlled map of the company and its approved governance sources.
The profile supplies inputs to later workflows; it is not legal advice and does
not establish that any rule applies.

Read the [source and control method](../../references/governance-source-and-control-method.md)
and [profile schema](../../references/governance-profile-schema.md) first.

## Workflow

1. Confirm the perimeter.
   - Record the entity type, registration basis, governance perimeter and as-at
     date from a controlled source.
   - Record every overlay as `yes`, `no` or `unknown`. Never convert missing
     information to `no`.
   - Return `OUTSIDE SCOPE` for a CATSI Act corporation or non-company entity.
     Mark listed, APRA-regulated and ACNC-registered companies for specialist
     overlay configuration before consequential use.
2. Inventory controlled documents.
   - Capture the document ID, title, version, effective date, approval state
     and controlled source location for the constitution and each other
     governance instrument.
   - Record whether replaceable rules apply, are displaced, are modified or are
     unknown. Do not infer this from the existence of a constitution alone.
3. Map authority and accountability.
   - Identify board and member-reserved powers, quorum and voting sources,
     delegations, committees, registers, record owners and calendar owners.
   - Record the exact document and clause for each internal rule. Surface gaps
     and conflicts; do not reconcile them.
4. Apply legal-source controls.
   - Use `$check-commonwealth-legislation` for any proposition that depends on
     the *Corporations Act 2001* (Cth). Do not copy a cached statutory rule into
     the profile as if it were an organisation fact.
5. Prepare the profile for human approval.
   - Follow the schema exactly. Mark it `draft`; leave approval fields blank.
   - Give an authorised reviewer a bounded list of missing evidence, conflicts
     and overlay checks. The reviewer supplies approval, version and review date.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Requested configuration: <new / revision / validation>
Entity and perimeter: <type, registration basis and covered entities>
Profile version and status: <identifier and draft/approved/retired>
As-at date: <date>
Overlays: <yes/no/unknown with controlling evidence>
Controlled documents: <ID, version, status and source location>
Authority map: <powers, reservations, quorum, voting and delegations>
Accountability map: <committees, registers, records and calendar owners>
Gaps or conflicts: <bounded list>
Verified legal sources: <exact official URLs, provisions and checked date>
Approval required: <authorised role and unresolved items>
Limitations: <scope and facts not established>
```

## Fail closed

Return `NOT READY` when the registration basis, decisive overlay, governing
document status or approval authority is unknown. Never invent a constitution,
replaceable-rule posture, delegation, committee, reviewer or approval date.
Never place privileged advice, confidential board content, credentials or
personal data in a reusable profile or this public repository.
