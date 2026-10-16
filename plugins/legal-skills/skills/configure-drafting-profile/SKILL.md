---
name: configure-drafting-profile
description: Create, revise or validate an organisation-controlled profile for first-draft Australian commercial documents, recording the drafting party, registrations, GST, governing state, house style, risk appetite and standard positions. Use before commercial drafting or when standing instructions change. Do not approve a profile or treat it as legal advice.
---

# Configure Drafting Profile

Jurisdiction: Australian Commonwealth law and the identified governing state or
territory. Record the legal as-at and intended use dates. The 2026-10-13 source
snapshot is a currency limit, not live verification. Verify every applicable
statutory provision on legislation.gov.au (NSW overlays on legislation.nsw.gov.au)
using `$check-commonwealth-legislation` and, for NSW, `$check-nsw-legislation`;
use the corresponding official-source workflow for other states or territories.
Never rely on model memory. Record assumptions and input provenance. A qualified
lawyer must review every output before use.

Read the [source and control method](../../references/drafting-source-and-control-method.md)
first. Use the [profile schema](../../references/drafting-profile-schema.md)
for standing positions and transaction instructions.

## Workflow

1. Confirm the drafting party, document perimeter, drafting side, governing
   state/territory, as-at date and qualified lawyer responsible for review.
   Identify entity type, legal/trading name, address, notice contact and sources.
2. Record ACN/ABN, applicability and GST registration separately with source and
   checked date. Format checks do not prove registration, identity or tax status.
   Record gaps as `unknown`; an ABN does not prove GST registration.
3. Capture house style and authorised risk appetite. Map versioned standard
   positions, rationale, fallbacks and approval owners for fees, confidentiality,
   IP, moral rights, liability, indemnities, renewal, variation, cancellation,
   suspension, termination and disputes. Do not invent numerical defaults.
4. Inventory controlled documents, existing approvals, overlays and conflicts.
   Use the profile schema. Standard positions cannot override law. Verify legal
   propositions with `$check-commonwealth-legislation`; distinguish supplied
   commercial preferences from verified statutory requirements.
5. Prepare a new or revised profile as `draft`, with approval fields blank.
   For validation preserve the supplied original and report confirmed versus
   claimed approval evidence. Identify departures and review triggers. Saving
   needs an explicit user instruction and controlled destination, never this
   public repository.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`. Return the versioned profile, provenance per field, assumptions,
source ledger, gaps/conflicts and approval checklist. `READY FOR HUMAN REVIEW`
means the draft is complete for review, not that it is approved. Use `READY WITH
QUALIFICATIONS` for non-decisive unknowns; `NOT READY` for unknown party/perimeter
or approval authority that prevents useful configuration.

## Fail closed

Never invent an entity number, GST status, house position, approving person or
approval date. The model cannot mark the profile approved. Treat missing claimed
approval evidence as unconfirmed. Record decisive conflicts as `NOT READY` and
request the affected instruction while completing independent profile fields.
Return `OUTSIDE SCOPE` for requests to give final advice or operate live systems.
A qualified lawyer must review both configuration and later application.
