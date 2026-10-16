---
name: assess-termination-exposure
description: Issue-spot the exposure arising from a proposed or completed termination of an Australian national system employee — unfair dismissal eligibility and the Small Business Fair Dismissal Code, general protections and the reverse onus, genuine redundancy and consultation, notice and redundancy pay, unlawful termination, and the Fair Work Commission's 21-day application periods routed to the litigation-deadlines script — using verified official sources and an approved employment profile. Use before a dismissal decision, after a dismissal when a claim is threatened, or when planning a redundancy. Do not use to conclude that a dismissal was or would be unfair, that adverse action occurred, that a redundancy is genuine, to compute a time limit, or to draft or lodge anything with the Commission.
---

# Assess Termination Exposure

Set out, with sources, every claim path a termination could open and the
facts that bear on each. The assessment identifies exposure; the responsible
lawyer decides.

Read the [source and control method](../../references/fair-work-source-and-control-method.md)
first, use the approved profile per the
[employment profile schema](../../references/employment-profile-schema.md),
and work from the [termination exposure map](../../references/termination-exposure.md).

## Workflow

1. Fix the facts and the profile.
   - Load the approved employment profile. Record the employee's role,
     employment type as classified, start date and length of service,
     remuneration relative to the high income threshold, instrument
     coverage as believed, and whether the employer is a small business
     employer at the relevant time.
   - Record the termination as described: proposed or completed, date it
     took or would take effect, stated reason, process followed so far, and
     any recent workplace-right exercise, complaint, leave, flexible-work
     request or protected attribute the practitioner has flagged.
2. Issue-spot each claim path.
   - Unfair dismissal: minimum employment period, coverage or threshold
     eligibility, Small Business Fair Dismissal Code applicability, and the
     facts bearing on harshness, unjustness or unreasonableness — recorded
     as facts, not findings.
   - General protections: every workplace right, industrial activity or
     protected attribute in play, the reverse onus, and the dismissal versus
     non-dismissal route.
   - Genuine redundancy: whether the role is said to be no longer required,
     the consultation clause in the instrument, and redeployment facts.
   - Notice and redundancy pay: the statutory tables in the reference,
     applied as leads with the service band identified; the small business
     exemption; any contractual or instrument enhancement.
   - Unlawful termination, stop-bullying and stop-sexual-harassment
     jurisdictions as flags where the facts engage them.
3. Route the time limits.
   - Name the governing provision for each application period (unfair
     dismissal 21 days; general protections dismissal dispute 21 days) and
     route the candidate date to `$compute-procedural-deadlines`. Never
     compute the date; where no verified table exists, report identify-only
     with the provision cited.
4. Verify.
   - Route every section, threshold, cap, fee and date relied on to
     `$check-commonwealth-legislation`; record evidence states. Note the
     Building Cooperative Workplaces reforms in force from 7 July 2026 where
     the Commission's process matters.
5. Report using the result contract and name the responsible lawyer.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Termination: <proposed/completed; effective date; stated reason; process so far>
Employee: <type as classified; service; remuneration v threshold; coverage belief>
Employer: <small business status at the relevant time; profile version>
Claim paths: <path; eligibility facts; facts for and against; provisions;
  evidence state; checked date>
Notice and pay leads: <service band; statutory table entry; enhancements; flags>
Time limits: <provision; routed to compute-procedural-deadlines | identify-only>
Gaps: <unknown facts; unverified propositions; resolver>
Human decision gate: <responsible lawyer; decisions required before action>
Limitations: <issue-spotting only; no finding on fairness, adverse action or genuineness>
```

## Fail closed

Return `NOT READY` when the employee, employer or termination cannot be
identified. Route employees outside the national system, contractor
characterisation, discrimination merits and workers compensation to
`OUTSIDE SCOPE` with the specialist named. Never conclude that a dismissal
was or would be unfair, that adverse action occurred or that a redundancy
is genuine; never compute a time limit; never draft or lodge an application
or response; never present a Commission or Ombudsman page as statute.
