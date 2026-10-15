---
name: compute-underpayment-exposure-framework
description: Prepare an Australian underpayment exposure framework using verified entitlement sources, payroll evidence, limitation leads and intentional-underpayment offence screening. Framework only: never invent award rates, compute a final liability or equate every error with wage theft.
---

# Compute Underpayment Exposure Framework

Jurisdiction: Australian national system wage entitlements and related Fair Work
proceedings, subject to verified coverage and historical instruments.
State-system wages and separate tax, superannuation and criminal merits require
specialist review. Verify Commonwealth law at legislation.gov.au with
`$check-commonwealth-legislation` and instruments at fwc.gov.au. Currency is
limited to the linked extension reference; each pay period needs its own source.

Read the [source and control
method](../../references/fair-work-source-and-control-method.md), reuse the
[employment profile schema](../../references/employment-profile-schema.md) and
consult the [extension source
checklist](../../references/employment-extension-sources.md). Assume only
evidenced instructions and documents; unknown facts stay unknown. Every output
requires review by a qualified lawyer before reliance.

## Workflow

1. Reuse `$configure-employment-profile` and the employment profile schema.
   Record coverage, worker cohorts, employment/classification scenarios,
   affected date range, agreements, contracts, actual duties, time/roster
   records, payslips, bank payments and deductions. Identify missing evidence
   and preserve originals; do not overwrite payroll records. Verify s 557C at
   legislation.gov.au when records or payslips are missing: identify the
   relevant allegation, specified civil provision, record/inspection/payslip
   obligation, noncompliance and any reasonable excuse. Do not equate an
   incomplete data export with a proved statutory breach.
2. Use `$map-fair-work-obligations` to build a dated entitlement-source
   schedule. Verify instruments at fwc.gov.au and statutory provisions at
   legislation.gov.au. Split on classification, instrument, annual wage review,
   employment-type and rate-effective dates; apply each historical source to its
   own period. Do not infer an award or fabricate a rate from job title, model
   memory or current pay guides.
3. Specify the back-pay worksheet without computing a final exposure:
   worker/cohort, period, verified classification/clause/rate, units/hours,
   ordinary pay, overtime, penalties, allowances, leave/loading, required gross
   amount, evidenced paid amount allocated to that entitlement, legally
   supported offset, difference and source. Distinguish casual loading,
   annualised wages and contractual set-offs, using
   `$review-employment-contract` and verified law. Never net unrelated excess
   payments across entitlements/periods without legal support. Keep gross
   back-pay, tax/withholding, superannuation specialist issues, interest,
   penalties and remediation costs separate; avoid double-counting. Unknown
   units/rates remain blank with a resolver. Include a separate s 557C
   evidence/burden column and disputed-hours scenarios for lawyer review. Where
   its statutory conditions apply in proceedings, the employer bears the burden
   of disproving the relevant allegation, subject to the reasonable-excuse
   exception; this does not supply a rate, decide credibility or establish
   criminal guilt.
4. Record limitation leads separately. On legislation.gov.au verify s 544 (civil
   applications within six years of contravention, subject to its specific
   scope), s 545(5) (underpayment order look-back) and s 327C(2) (criminal
   proceedings within six years of offence). These are distinct triggers, not
   one global six-year rule. Identify each due date/contravention and route
   candidate dates to `$compute-procedural-deadlines`; report identify-only if
   verified computation support is unavailable. Preserve earlier records for
   other claims and do not use an assumed cut-off to delete evidence.
5. Screen criminal risk separately from arithmetic. Verify Fair Work Act s 327A
   at legislation.gov.au: intentional conduct and intentional failure to pay
   covered required amounts, with statutory exclusions and application rules.
   Use the [policy statutory hooks](../../references/policy-statutory-hooks.md)
   as the owner of the wage-theft commencement snapshot and reverify its
   official sources; distinguish due dates, conduct periods and transition
   before applying it. An accidental error is not automatically this offence.
   Record escalation evidence without finding intent or guilt. Check ss
   327B–327C and the Voluntary Small Business Wage Compliance Code at
   legislation.gov.au; neither headcount alone nor back-payment guarantees
   immunity from civil liability or prosecution. State offences require
   specialist verification.
6. Return source/data gaps, worksheet design, cohort scenarios, limitation
   hand-offs and counsel escalation. Do not invent interest or penalty figures.
   A qualified lawyer and payroll specialist must validate application, units,
   rates and proposed remediation before any calculation, payment or disclosure.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

Return: Coverage/cohort/date assumptions; historical entitlement-source
schedule; blank auditable back-pay worksheet; records and rate gaps; s 557C
allegation/obligation/noncompliance/exception evidence; distinct
civil/look-back/criminal limitation triggers; s 327A
intent/exclusion/commencement screening; separate back-pay/interest/penalties;
reviewer and payroll owner. Include scope/date/assumptions, evidence state for
each proposition, official source URL/identifier, version, provision or clause,
actual checked date, unresolved issue/resolver and qualified lawyer decisions.
Snapshot dates never substitute for the date a source was actually accessed. An
unavailable named skill means its step was not done; name the plugin to install.

## Fail closed

Unknown instrument, rate or hours: `NOT READY` for monetary exposure; provide
supported framework rows only. State-system wages, tax, superannuation and
criminal merits: `OUTSIDE SCOPE` for specialist conclusions. No final
calculation, award-rate invention, liability/guilt finding, payment or regulator
contact. Unverified law is labelled `NOT VERIFIED` with “verify against
<official source>”; stop the affected conclusion while completing supported
issue spotting. No saving outside the approved matter system, sending, filing,
signing or payment is authorised by invocation of this skill.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`.
  Verifies the Fair Work Act and related legislation and case-law leads
  against the official sources.
- `australian-litigation-deadlines` (required):
  `compute-procedural-deadlines`. Computes candidate FWC, AHRC and court
  deadlines only where a verified rule is available; otherwise identifies the
  provision without calculating a date.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
