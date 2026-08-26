---
name: map-fair-work-obligations
description: Map which Fair Work Act 2009 (Cth), National Employment Standards, modern award and enterprise agreement provisions apply to a described Australian employment arrangement — coverage gate, employment type, the twelve NES entitlements, right to disconnect, award or agreement clauses, minimum wage and high income threshold, information statements — using verified official sources and an approved employment profile, with every proposition carrying an evidence state. Use for onboarding, contract design, entitlement queries, award coverage questions and pre-advice research. Do not use to conclude award coverage, characterise a worker as employee or contractor, calculate pay or leave balances, or give final legal advice — coverage and characterisation fail closed to the responsible lawyer.
---

# Map Fair Work Obligations

Lay out the layers that apply to an arrangement and cite each one. The map
identifies provisions; it never concludes that an instrument covers the
employee or that an entitlement has been met.

Read the [source and control method](../../references/fair-work-source-and-control-method.md)
first, use the approved profile per the
[employment profile schema](../../references/employment-profile-schema.md),
and work from the [framework layers reference](../../references/framework-layers.md).

## Workflow

1. Fix the arrangement and the profile.
   - Load the approved employment profile; record its version and as-at
     date. Without an approved profile, run `$configure-employment-profile`
     first or proceed on stated assumptions labelled as such.
   - Record the arrangement as described: role, location, employment type
     as the employer classifies it, hours pattern, remuneration, start date,
     instrument the employer believes applies, and the question asked.
2. Apply the coverage gate.
   - Record the claimed national system basis (constitutional corporation,
     Commonwealth, Territory or state referral) and the State or Territory,
     using the coverage table in the framework reference. Flag any employer
     type that the table places outside the national system, any s 14(5)
     endorsement, and any state-referred business, then stop the affected
     conclusions and route to specialist review.
   - Record small business status as claimed, with the headcount date.
3. Map the layers.
   - For each NES entitlement, record whether the described facts engage it,
     the section range, and the evidence state from the reference. Include
     the right to disconnect and the information-statement duties.
   - Record the award or agreement the employer believes applies with its
     identifier; confirm the instrument exists at the Fair Work Commission
     and note the coverage clause as a lead. Never conclude coverage.
   - Record the current National Minimum Wage, award minimum wage
     movement and high income threshold with their effective dates, and
     flag where the arrangement sits relative to the threshold.
   - Record the casual definition (s 15A) and employee choice pathway, the
     fixed-term contract limits and the ordinary-meaning employee definition
     (s 15AA) as flags where the facts engage them; never characterise.
4. Verify.
   - Route every section, threshold and date relied on to
     `$check-commonwealth-legislation`; record the evidence state. Treat
     Fair Work Ombudsman and Commission pages as guidance with their
     last-updated dates.
5. Report using the result contract and name the responsible lawyer.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Arrangement: <role; location; type as classified; hours; remuneration; start>
Profile: <ID, version, status, as-at date>
Coverage gate: <national system basis claimed; small business status; flags>
Layer map: <layer; provision or clause; engaged (yes/no/cannot be determined);
  source; evidence state; checked date>
Figures: <NMW; award movement; high income threshold; effective dates>
Characterisation flags: <casual, fixed-term, contractor, labour hire — flag only>
Gaps: <unknown facts; unverified propositions; resolver>
Human decision gate: <responsible lawyer; decisions required>
Limitations: <map only; no coverage, characterisation or entitlement conclusion>
```

## Fail closed

Return `NOT READY` when the arrangement or employer cannot be identified.
Route employers outside the national system, contractor characterisation,
pay or leave calculations, discrimination merits and industrial action
strategy to `OUTSIDE SCOPE` with the specialist named. Never conclude award
or agreement coverage, never re-characterise an employment type, never
state a figure without its effective date and source, and never present a
regulator page as statute.
