---
name: configure-ai-governance-profile
description: Create or update a controlled Australian AI-governance profile recording entity type, sector, regulatory overlays, government track, EU footprint, AI inventory maturity and version-identified governing documents, so the other AI-governance skills run against approved facts. Use for first-time setup, overlay changes, new AI use categories or scheduled profile review. Do not use to assess a use case, conclude that an instrument applies, approve the profile or store matter facts, personal data or privileged content.
---

# Configure AI Governance Profile

Prepare a draft profile an authorised human can approve. The model records
facts and gaps; it never supplies approval.

Read the [source and control method](../../references/ai-governance-source-and-control-method.md)
and follow the [profile schema](../../references/ai-governance-profile-schema.md).

## Workflow

1. Fix the entity and purpose.
   - Record the controlled entity label, entity type and, for government
     entities, jurisdiction. Do not collect unnecessary personal data.
   - Record why the profile is being created or changed and the as-at date.
2. Work through the overlays.
   - Ask for each overlay in the schema (APRA, ASIC licensee, eSafety-relevant
     service, TGA/SaMD, Commonwealth agency, state or territory agency, EU
     footprint) and record `yes`, `no` or `unknown`. Never default a missing
     answer to `no`.
   - Where an overlay is `yes` or `unknown`, note the separate regime and the
     skill or specialist that owns its depth.
3. Record AI adoption facts.
   - AI inventory maturity, AI use categories in scope, and board-level AI
     oversight arrangements, each tied to a document identifier where one
     exists.
   - List governing documents with ID, title, version, effective date, status
     and source location. Mark any document the organisation cannot produce
     as `unknown`, not assumed.
4. Validate against the schema.
   - Confirm every required field is present or explicitly `unknown`. Record
     conflicts between supplied documents without choosing between them.
5. Mark the profile `draft` and set the human gate.
   - Leave `Approved by role` and `Approved at` blank. Name the review-due
     date and the role expected to approve. State where the organisation
     should store the approved profile (its own governed system, not this
     repository).

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Profile action: <create or update, and why>
Entity: <controlled label, type, jurisdiction>
Overlays: <each schema overlay with yes/no/unknown and routing note>
AI adoption facts: <inventory maturity, use categories, board oversight>
Governing documents: <ID; title; version; effective date; status; location>
Gaps and conflicts: <missing answers, document conflicts, unresolved items>
Profile status: draft — approval fields blank
Human decision gate: <approving role, review-due date, storage location>
Limitations: <facts recorded, no applicability or adequacy conclusion>
```

## Fail closed

Return `NOT READY` when the entity type, a decisive overlay or the status of a
material governing document cannot be established. Return `OUTSIDE SCOPE` for
entities outside Australian jurisdiction. Never mark a profile approved, never
default an overlay to `no`, and never invent a document, version or oversight
arrangement the organisation has not supplied.
