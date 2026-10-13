---
name: assess-employee-vs-contractor
description: Issue-spot Australian worker classification under Fair Work Act ss 15AA–15AD and sham contracting under s 357, including high-income opt-out evidence. Use before contractor drafting or engagement review; never classify conclusively from an ABN, label or income alone.
---

# Assess Employee vs Contractor

Jurisdiction: Australian worker classification for Fair Work purposes, subject
to the provision's coverage and date-specific application. Tax, superannuation
and other statutory definitions require separate tests. Verify Commonwealth
provisions at legislation.gov.au using `$check-commonwealth-legislation`.
Currency is limited to the linked extension reference, not a universal or
current-law classification assurance.

Read the [source and control
method](../../references/fair-work-source-and-control-method.md), reuse the
[employment profile schema](../../references/employment-profile-schema.md) and
consult the [extension source
checklist](../../references/employment-extension-sources.md). Assume only
evidenced instructions and documents; unknown facts stay unknown. Every output
requires review by a qualified lawyer before reliance.

## Workflow

1. Reuse `$configure-employment-profile` and the employment profile schema;
   record engager entity, jurisdiction and coverage basis, worker identity by
   controlled label, engagement dates, contract versions and actual work
   evidence. Request control, delegation/substitution, tools, financial risk,
   exclusivity, integration, payment and ability to build a separate business.
   Preserve conflicting accounts.
2. Build the legal-test gate by date and coverage. Verify ss 15AA–15AD at
   legislation.gov.au with `$check-commonwealth-legislation`, including s
   15AA(3) exclusions and transition/application provisions. Section 15AA
   commenced on 26 August 2024; distinguish the whole relationship test from
   tests that may apply outside its statutory operation. Consider both contract
   rights and actual performance where s 15AA applies. Do not use a checklist
   score as a classification decision.
3. Test high-income opt-out separately. Verify s 15C and regulation 1.08AA on
   legislation.gov.au; obtain the contractor high income threshold for the
   relevant year and earnings basis, rather than substitute an employee
   threshold. Inspect the individual's written election, earnings statement,
   timing, any engager notice, s 15AC effect and s 15AD revocation. High
   earnings alone do not create an opt-out, remove all employee rights or prove
   contractor status. Route any notice deadline to
   `$compute-procedural-deadlines`, recording unavailable verified coverage as
   identify-only.
4. Check s 357 misrepresentation and the employer's reasonable-belief defence,
   commenced 27 February 2024, against legislation.gov.au. Record what was
   represented, when, who knew what, advice sought and evidence supporting the
   belief; distinguish the defence from a final finding. An ABN, invoices or a
   contractual recital is not sufficient classification evidence.
5. Name `$draft-services-agreement` in australian-commercial-drafting only after
   the classification issue is put to the qualified lawyer. Reuse that plugin's
   unfair-contract-terms-checklist.md, including its UTPA 2026 notes, for
   relevant services-contract questions; do not transplant consumer rules into
   employment automatically. If privacy issues arise, use
   `$assess-australian-privacy-issues`. Tax, superannuation, workers
   compensation and other statutory definitions need separate specialist tests.
6. Return competing characterisation arguments, evidence gaps, applicable test
   and consequences requiring review. A qualified lawyer decides classification
   before contractor-dependent wording is settled.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

Return: Date/coverage/test gate; contract and performance evidence;
employee/contractor arguments; contractor threshold source and year; opt-out
notices/effect/revocation; s 357 representation/defence evidence; drafting
hand-off. Include scope/date/assumptions, evidence state for each proposition,
official source URL/identifier, version, provision or clause, actual checked
date, unresolved issue/resolver and qualified lawyer decisions. Snapshot dates
never substitute for the date a source was actually accessed. An unavailable
named skill means its step was not done; name the plugin to install.

## Fail closed

No relationship evidence or applicable test unverified: `NOT READY` for
classification. Conflicting facts: `READY WITH QUALIFICATIONS` for issue
spotting only. Other statutory classification regimes: `OUTSIDE SCOPE`. Never
issue a conclusive employee/contractor certificate or manufacture an opt-out.
Unverified law is labelled `NOT VERIFIED` with “verify against <official
source>”; stop the affected conclusion while completing supported issue
spotting. No saving outside the approved matter system, sending, filing, signing
or payment is authorised by invocation of this skill.

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
- `australian-commercial-drafting` (hand-off): `draft-services-agreement`.
  Provides services drafting, clause review and the existing UCT checklist and
  UTPA 2026 notes.
- `australian-privacy-cybersecurity` (hand-off):
  `assess-australian-privacy-issues`. Assesses personnel-data, confidentiality
  and privacy application questions.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
