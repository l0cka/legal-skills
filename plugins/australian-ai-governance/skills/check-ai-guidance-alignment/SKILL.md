---
name: check-ai-guidance-alignment
description: Assess an organisation's AI governance documentation against the current Australian voluntary guidance layers — the National AI Centre's Guidance for AI Adoption (AI6) as primary, the Voluntary AI Safety Standard's 10 guardrails as the superseded-but-current detail catalogue and AS ISO/IEC 42001 as the certifiable management-system crosswalk — labelling every layer voluntary or mandatory-via-regulator. Use for gap assessments, AI policy reviews and pre-certification readiness. Do not use to certify against any standard, conclude legal compliance or assess privacy or board depth owned by other skills.
---

# Check AI Guidance Alignment

Compare supplied AI governance documentation with the voluntary guidance
layers, reporting alignment and gaps as evidence for a human reviewer — never
a certification or a compliance conclusion.

Read the [source and control method](../../references/ai-governance-source-and-control-method.md)
and use the approved [profile schema](../../references/ai-governance-profile-schema.md)
profile.

## Workflow

1. Fix the documentation set.
   - Take version-identified AI policies, risk frameworks, registers,
     assessment templates and board records from the approved profile. Record
     any document whose status or version is `unknown` and exclude invented
     content.
2. Verify the guidance layer at the assessment date.
   - Fetch or confirm the current AI6 guidance text at ai.gov.au, the VAISS
     10-guardrail catalogue at industry.gov.au and the supersession labelling
     in the method reference. Treat the practice and guardrail names in this
     plugin as routing leads; assess against the verified current text, not
     from memory.
3. Assess against AI6 first.
   - Work through the six essential practices (accountability; stakeholder
     engagement and redress; risk management; transparency, including an AI
     register; testing and monitoring; human oversight and decommissioning).
     For each, record what the documentation shows, what is absent and what
     is ambiguous, with document identifiers.
4. Drill into detail layers where warranted.
   - Use the VAISS guardrails as the detailed control catalogue for practices
     that need finer-grained checks, stating the superseded-as-primary
     labelling. Where the organisation targets certification, map findings to
     AS ISO/IEC 42001 clauses as a crosswalk, noting certification is a
     third-party process this skill cannot perform.
   - Mark every expectation `voluntary` unless a regulator overlay from the
     profile makes equivalent conduct a supervisory expectation (for example
     the APRA AI letter for APRA-regulated entities) — then label it
     `mandatory-via-regulator` with the source.
5. Set the human decision gate.
   - Rank gaps by the risk of the organisation's actual AI use categories.
     Identify the reviewer who owns remediation and any routing to
     `$assess-board-ai-oversight` or `$map-ai-regulatory-obligations`.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Documentation set: <IDs, titles, versions, effective dates>
Profile: <approved identifier and version; AI use categories>
Guidance layer verified: <AI6, VAISS, 42001 sources and checked dates>
Alignment by practice: <practice; documented evidence; gap; ambiguity>
Detail-layer findings: <guardrail or clause; finding; label voluntary/mandatory-via-regulator>
Gap ranking: <gap; affected use category; risk basis>
Human decision gate: <remediation owner and routed follow-ups>
Limitations: <no certification, no legal-compliance conclusion>
```

## Fail closed

Return `NOT READY` when the documentation set, its versions or the current
guidance text cannot be established. Never assess from memorised practice or
guardrail wording, never present voluntary guidance as law, never call the
result a certification, and never fill a documentation gap with assumed
content.
