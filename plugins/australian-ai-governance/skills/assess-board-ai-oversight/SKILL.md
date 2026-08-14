---
name: assess-board-ai-oversight
description: Issue-spot board and director-duty exposure for Australian AI adoption and board-level AI use — care-and-diligence engagement with AI-influenced information, reliance and delegation limits, board AI policy and record controls, and regulator overlays — using verified Corporations Act provisions, verified case-law leads and an approved AI-governance profile. Use for board AI policies, AI-assisted board packs, oversight reviews and APRA or ASIC-regulated AI adoption. Do not use to conclude breach or compliance, assess general board process outside AI, or give final legal advice.
---

# Assess Board AI Oversight

Assess whether board-level AI governance gives the authorised human reviewer
the evidence needed to address director-duty exposure. Do not predict or
declare liability.

Read the [source and control method](../../references/ai-governance-source-and-control-method.md)
and use the approved [profile schema](../../references/ai-governance-profile-schema.md)
profile.

## Workflow

1. Fix the question and facts.
   - Separate two postures: the board's oversight of organisational AI
     adoption, and directors' own use of AI in board work. Record which is in
     issue, the entities, roles and relevant dates.
2. Verify the legal framework.
   - Use `$check-commonwealth-legislation` for ss 180–190 of the
     *Corporations Act 2001* (Cth) at the relevant date. Treat s 180 (care
     and diligence over AI-influenced information) and s 189 (reliance is
     available for information or advice from persons, not from AI systems)
     as routing leads to be verified, not cached rules.
   - For case-law leads including *ASIC v Bekier (Liability Judgment)* [2026]
     FCA 196, use `$route-case-citation` and an official-court verifier, and
     check for appeal or later treatment before relying on any proposition.
     Present Bekier's expectations — board AI use controlled and transparent,
     governed by formally adopted policies, never displacing the director's
     own judgment — as first-instance judicial guidance.
3. Apply the guidance layer, labelled as guidance.
   - AICD/HTI Director's Guide V2, ASIC REP 798 and the Governance
     Institute's agentic-AI paper are professional-body or regulator
     material, never law.
   - For APRA-regulated entities, layer the April 2026 APRA AI letter's
     board expectations (AI strategy consistent with risk appetite,
     monitoring and reporting, third-party dependency triggers) over
     CPS 220/230/234 and record them as supervisory expectations.
4. Build the issue matrix.
   - Address: adopted board AI policy and its scope; disclosure of AI use in
     board processes; directors' active testing of AI-influenced information;
     reliance and delegation boundaries; minutes and record controls for
     AI-assisted work; agentic-AI authority boundaries; and regulator-overlay
     expectations. For each issue, distinguish fact, internal control,
     verified law, guidance, inference and unresolved question, and link the
     evidence.
   - Route general decision-process and conflicts depth to
     `$assess-director-duties-governance`.
5. Set the human decision gate.
   - State what can be improved before the next board decision, the
     responsible reviewer, and unresolved items. Do not recommend approval as
     a legal conclusion.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Requested assessment: <oversight posture and question>
Entity, roles and relevant date: <controlled facts>
Profile: <approved identifier and version; decisive overlays>
Verified legal sources: <provisions, versions, URLs and checked date>
Case-law leads: <citation; verification status; propositions used as guidance>
Guidance layer: <AICD, REP 798, APRA letter and other material, labelled>
Issue matrix: <issue; evidence; source type; evidence state; risk; missing fact>
Routed depth: <$assess-director-duties-governance and other routings>
Human decision gate: <reviewer, decision and unresolved items>
Limitations: <no breach, compliance or board-effectiveness conclusion>
```

## Fail closed

Return `NOT READY` when the oversight posture, decisive facts, document
versions or the current text of a material provision cannot be established.
Never state that a director has complied with or breached a duty, never treat
an unverified case citation or professional-body guidance as law, and never
infer that a board policy exists from the fact that AI is in use.
