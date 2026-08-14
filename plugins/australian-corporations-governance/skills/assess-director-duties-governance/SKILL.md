---
name: assess-director-duties-governance
description: Issue-spot Australian company governance and director or officer duty risks for a proposed or completed decision using verified Corporations Act provisions, an approved governance profile and version-controlled organisation documents. Use for decision authority, purpose, care, information, reliance, delegation, conflicts, solvency and record-process checks. Do not use to conclude breach, validity, privilege or solvency, provide final legal advice, or substitute for specialist listed, APRA, ACNC, CATSI, transaction or insolvency review.
---

# Assess Director Duties Governance

Assess whether the decision process gives the authorised human reviewer the
evidence needed to address governance and duty issues. Do not predict or declare
legal liability.

Read the [source and control method](../../references/governance-source-and-control-method.md)
and use the approved [profile schema](../../references/governance-profile-schema.md).

## Workflow

1. Fix the decision and time.
   - Separate proposed conduct from completed conduct. Record the decision,
     decision-maker roles, relevant dates, entities and requested question.
   - Do not request unnecessary personal data. Refer to sensitive people and
     documents by controlled identifiers where possible.
2. Check readiness and overlays.
   - Require an approved, current governance profile and version-controlled
     governing documents. Record any uncertainty.
   - Stop the affected analysis if a listed, APRA, ACNC or CATSI overlay may
     change the applicable duty or process and has not been reviewed.
3. Verify the legal framework.
   - Use `$check-commonwealth-legislation` for each material statutory
     proposition at the relevant date, including application and commencement.
   - Treat ss 180–190, 191–196, 198A–198F and 588G only as routing leads. Verify
     the actual provision and check for other relevant Parts, instruments and
     modifications.
   - If a supplied case citation is material, use `$route-case-citation` and an
     available official-court verifier. Citation existence does not establish
     treatment, ratio or application; escalate substantive case research.
4. Build an issue matrix.
   - Address authority and reserved matters; purpose and interests; information,
     care and challenge; reliance and delegation; conflicts and participation;
     financial position and solvency indicators; benefits or related parties;
     and records, reasons and follow-up controls.
   - For each issue, distinguish fact, internal control, verified law, guidance,
     inference and unresolved question. Link the exact evidence.
5. Set the human decision gate.
   - State what can be improved before the decision and what needs retrospective
     fact confirmation. Identify the responsible lawyer, company secretary,
     board or specialist reviewer. Do not recommend approval as a legal conclusion.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Requested assessment: <decision and question>
Entity, roles and relevant date: <controlled facts>
Profile and document versions: <approved identifiers>
Applicable overlays: <checked status and separate-review needs>
Issue matrix: <issue; evidence; source type; evidence state; risk; missing fact>
Process safeguards: <actions available before or after the decision>
Verified legal sources: <official URLs, provisions, versions and checked date>
Guidance and case-law limits: <separately labelled material>
Human decision gate: <reviewer, decision and unresolved items>
Limitations: <no breach, validity, privilege or solvency conclusion>
```

## Fail closed

Return `NOT READY` when authority, applicable law, decisive facts, document
versions or a material conflict cannot be established. Do not infer assent from
silence, independence from a title, solvency from incomplete accounts, or a
business-judgment protection from process labels. Never state that a director
has complied with or breached a duty; present issue spotting for human advice.
