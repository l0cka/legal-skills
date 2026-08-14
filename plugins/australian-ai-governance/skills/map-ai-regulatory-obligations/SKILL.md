---
name: map-ai-regulatory-obligations
description: Map which Australian regulatory instruments currently bind a described AI use case — privacy, sector regulator, consumer, online-safety and government-use tracks — and separately flag pending instruments such as the proposed Australian Standards for AI as watch items using verified official sources and an approved AI-governance profile. Use for AI adoption decisions, procurement, product launches or governance reviews needing an obligations map. Do not use for privacy or automated-decision depth, EU AI Act analysis, breach conclusions or final legal advice.
---

# Map AI Regulatory Obligations

Build an obligations map that separates what binds the organisation now from
what is only proposed. Never assert a pending instrument as in force.

Read the [source and control method](../../references/ai-governance-source-and-control-method.md)
and use the approved [profile schema](../../references/ai-governance-profile-schema.md)
profile.

## Workflow

1. Fix the use case and time.
   - Record the AI system or use case, its purpose, who it affects, the data
     involved, the deployment status (proposed, pilot, live) and the date of
     assessment.
   - Require an approved, current AI-governance profile; record any gap.
2. Map the currently binding layer.
   - Privacy: if personal information is involved, route depth to
     `$assess-ai-privacy-cybersecurity-use-case` and, for automated decisions,
     `$assess-automated-decision-transparency`. Record only the routing result.
   - Sector regulators: apply profile overlays — APRA-regulated entities
     (CPS 220/230/234 plus the April 2026 APRA AI letter as supervisory
     expectations), ASIC licensees (existing licensee obligations; REP 798 as
     guidance), TGA where intended purpose makes the system a medical device,
     eSafety industry codes for relevant online services.
   - Consumer law: flag misleading-or-deceptive-conduct exposure for AI
     claims and outputs under the Australian Consumer Law.
   - Government entities: route to `$triage-government-ai-use-case`.
   - Verify each statutory proposition with `$check-commonwealth-legislation`
     or the relevant state skill at the assessment date.
3. Map the voluntary layer.
   - State the AI6 guidance and VAISS guardrail catalogue as voluntary, with
     the supersession labelling from the method reference. Note AS ISO/IEC
     42001 certification as optional. Route documentation assessment to
     `$check-ai-guidance-alignment`.
4. Map the pending layer as watch items only.
   - Proposed Australian Standards for AI, OAIC automated-decision guidance,
     ASX Corporate Governance Council fifth edition, second-tranche privacy
     reform and any live consultation touching the use case. Record each with
     its expected trigger and route monitoring to
     `$track-ai-regulatory-developments`.
   - Flag EU footprint from the profile for specialist review without
     assessing EU law.
5. Set the human decision gate.
   - Identify unresolved applicability questions and the reviewer who must
     resolve them. Do not conclude compliance or non-compliance.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Use case: <system, purpose, affected people, data, status, date>
Profile: <approved identifier and version>
Binding now: <instrument; publisher; why it applies; evidence state; source URL>
Routed depth: <privacy, government, board or other skill routings and results>
Voluntary layer: <AI6/VAISS/42001 status with supersession labels>
Watch items (not law): <pending instrument; expected trigger; monitoring route>
Specialist flags: <EU footprint or other outside-scope exposure>
Human decision gate: <reviewer and unresolved applicability questions>
Limitations: <no compliance conclusion, pending items are not obligations>
```

## Fail closed

Return `NOT READY` when the use case, a decisive profile overlay or the
current text of a material instrument cannot be established. Never present a
watch item, consultation draft or announcement as a current obligation, never
default an overlay to `no`, and never restate regulator guidance as statute.
