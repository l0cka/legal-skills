---
name: review-corporations-governance-framework
description: Review an Australian company's governance framework against verified Corporations Act requirements, an approved governance profile and version-controlled organisation documents, producing an evidence-per-finding gap and action matrix. Use for board and committee authority, delegations, conflicts, information flows, records, policies, review cycles and accountability. Do not certify compliance, assess director liability, treat voluntary guidance as law, or replace specialist listed, APRA, ACNC, CATSI or sector review.
---

# Review Corporations Governance Framework

Review the design and evidenced operation of governance controls. A policy's
existence does not prove implementation, and an implementation sample does not
prove legal compliance.

Read the [source and control method](../../references/governance-source-and-control-method.md)
and use the approved [profile schema](../../references/governance-profile-schema.md).

## Workflow

1. Set the review perimeter.
   - Record covered entities, period, governance functions, sample basis and
     excluded matters. Require an approved, current profile.
   - Identify listed, APRA, ACNC, CATSI and sector overlays before setting
     criteria. Route decisive overlays to the appropriate specialist review.
2. Build the criteria register.
   - Use `$check-commonwealth-legislation` for each material statutory criterion
     and record application, version and checked date.
   - Add approved constitution, replaceable-rule mapping, delegations, charters,
     policies and prior resolutions as separately labelled internal criteria.
   - Label ASIC and other regulator material as guidance. Label ASX or APRA
     consultation drafts as drafts, never current requirements.
3. Test design and operation separately.
   - Cover decision authority and reserved matters; board and committee terms;
     conflicts; delegations; information and challenge; financial oversight;
     registers and records; policy ownership; escalation; and review cycles.
   - For each control, test whether it is designed and approved, then whether
     supplied evidence shows operation during the review period.
4. Grade each finding.
   - Use `SATISFIED`, `PARTLY SATISFIED`, `NOT SATISFIED`, `NOT TESTED` or
     `OUTSIDE SCOPE`. Give one evidence state and source for every grade.
   - Separate legal gaps, internal-control gaps, evidence gaps and improvement
     opportunities. Do not call a voluntary practice mandatory.
5. Prepare a governed action plan.
   - Assign proposed owner role, priority, dependency, review gate and evidence
     of completion. Human owners decide whether to accept, remediate or obtain
     advice; the model does not certify closure.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Review perimeter and period: <entities, functions, sample and exclusions>
Profile and document versions: <approved identifiers>
Applicable overlays: <checked status and separate-review needs>
Criteria register: <criterion; source type; exact source; evidence state>
Findings: <control; design grade; operation grade; evidence; gap type; impact>
Action plan: <action; owner role; priority; dependency; review gate; evidence>
Verified legal sources: <official URLs, provisions, versions and checked date>
Guidance and draft material: <separately labelled sources>
Human sign-off: <responsible reviewer and open decisions>
Limitations: <no compliance certification or liability conclusion>
```

## Fail closed

Return `NOT READY` when the review perimeter, applicable regime, approved
criteria, document versions or evidence base is materially incomplete. Grade
untested operation `NOT TESTED`, not satisfied. Never infer implementation from
a document title, treat a draft standard as current, certify compliance or mark
an action closed without human-approved completion evidence.
