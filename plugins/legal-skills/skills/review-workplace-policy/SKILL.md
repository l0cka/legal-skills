---
name: review-workplace-policy
description: Review an Australian employer's workplace policy set against the current Fair Work Act and related statutory hooks — right to disconnect, flexible working requests, parental and family and domestic violence leave, fixed-term contract limits, wage theft and the small business code, labour hire orders, delegates' rights, pay secrecy, casual conversion and information statements, and the Sex Discrimination Act positive duty — producing a gap and consistency matrix that labels each hook law or guidance. Use for policy refreshes, onboarding of a new policy set, post-amendment reviews and pre-audit checks. Do not use to certify compliance, conclude that the positive duty has been met, draft policy text, or review discrimination, work health and safety or privacy policies beyond the hooks listed.
---

# Review Workplace Policy

Check a policy set against the statutory hooks that must be reflected, and
say where the policy is silent, inconsistent or out of date. The review
finds gaps; it never certifies compliance.

Read the [source and control method](../../references/fair-work-source-and-control-method.md)
first, use the approved profile per the
[employment profile schema](../../references/employment-profile-schema.md),
and work from the [policy statutory hooks reference](../../references/policy-statutory-hooks.md).

## Workflow

1. Fix the policy set and the profile.
   - Load the approved employment profile and its policy inventory. Record
     each supplied policy by identifier, version, effective date and status,
     and which employee groups it covers. Treat an unsupplied policy the
     inventory lists as a gap, not as compliant.
2. Build the hook matrix.
   - For each hook in the reference that the profile's facts engage (for
     example, the small business commencement dates, fixed-term contracts in
     use, labour hire, employer-funded parental leave), record the
     provision, its commencement, its law-or-guidance label and its evidence
     state.
3. Test each policy against each hook.
   - Record, with the policy clause pinpoint: `reflects`, `silent`,
     `inconsistent` (quote the clause and the hook) or `out of date` (the
     clause predates a commencement it must reflect). Record `cannot be
     determined` where the policy text is ambiguous.
   - Flag cross-policy inconsistencies (for example, a flexible-work policy
     that sets a longer response period than the Act) and any clause that
     purports to exclude an NES entitlement.
   - For the positive duty, record what the policy set shows about
     measures, training and reporting as facts; never conclude the duty is
     met.
4. Verify.
   - Route every section and commencement relied on to
     `$check-commonwealth-legislation`; record evidence states. Record the
     last-updated date of each regulator page used.
5. Report using the result contract and name the policy owner and the
   responsible lawyer.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Policy set: <policy ID; version; effective date; status; coverage>
Profile: <ID, version, as-at date; facts that engage or exclude hooks>
Hook matrix: <hook; provision; commencement; law | guidance; evidence state>
Findings: <policy; clause pinpoint; hook; reflects | silent | inconsistent |
  out of date | cannot be determined; quoted text where inconsistent>
Cross-policy inconsistencies: <policies; clauses; issue>
Positive duty facts: <measures, training and reporting shown; gaps in evidence>
Gaps: <unsupplied policies; unverified propositions; resolver>
Human decision gate: <policy owner; responsible lawyer; decisions required>
Limitations: <gap review only; no compliance certification; hooks listed only>
```

## Fail closed

Return `NOT READY` when no policy text is supplied or the employer cannot be
identified. Route discrimination merits, work health and safety, privacy,
and policies for employers outside the national system to `OUTSIDE SCOPE`
with the specialist named. Never certify compliance, never conclude the
positive duty is met, never draft or rewrite policy text, and never present
regulator guidance as a statutory requirement.
