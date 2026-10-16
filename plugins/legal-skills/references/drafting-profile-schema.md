# Drafting profile schema

One controlled profile per drafting party and commercial perimeter. Store the
completed profile in the user's approved system. A profile is a factual and
commercial map, not a legal conclusion. Keep transaction-specific facts in a
separate instruction table.

```text
Profile ID and immutable version:
Status: draft / approved / retired
As-at date, review owner and review trigger:
Approved by role and approval date: human supplied only
Drafting party legal name and entity type:
Trading name, registered/service address and notice contact:
ACN and ABN: value / not applicable / unknown; source and checked date
GST registration: yes / no / unknown; source and checked date
Governing state or territory; jurisdiction preference and rationale:
Commercial perimeter: documents, products, customer classes and drafting side
House style: spelling, defined terms, numbering, tone and document format
Risk appetite: authorised owner, approval scope and version
Controlled documents: ID, version, effective date, status and source location
Standard positions, each with owner, approval, rationale and fallback:
- NDA direction, purpose boundaries, disclosure period and survival
- Fees, GST presentation, invoices, payment and disputed amounts
- Subscription period, renewal notice, cancellation and refund approach
- Variation reasons, notice channel/period and cancellation right
- IP: background, deliverables, ownership/licence and third-party rights
- Moral rights consent: creators, acts, attribution and consent scope
- Confidentiality, data handling and security responsibilities
- Liability: cap amount/formula, measurement period, aggregation and carve-outs
- Indemnities: trigger, causation, exclusions, defence and cap interaction
- Suspension, termination, cure periods, transition and data export
- Dispute escalation, notices, assignment and document precedence
Known conflicts, overlays and unknowns:
Qualified lawyer responsible for review:
```

For every field supply provenance (document/page, register record or dated
instruction), confirmer and evidence state. Validate ACN/ABN formatting without
claiming it proves identity; verify against an authorised register record when
available. ABN possession does not prove GST registration or contractor status.
`unknown` is valid and cannot become `no` or a default position. Leave human
approval fields blank in a new draft; do not invent a risk appetite or house style.

An approved profile requires a human-supplied approval role, date and immutable
version; report a claimed approval with missing evidence as unconfirmed. Retired
or draft profiles are not approved standard positions. If fresh instructions
conflict with the profile, record the departure for human review. No standing
position may override mandatory law or resolve an unknown transaction fact.

The separate instruction table records: field/choice, supplied value, source and
location, date, confirmer, evidence state, conflict and issue ID. The issues
register records: ID, document/clause/all marker locations, missing evidence or
decision, consequence, proposed options, owner and resolution status.
