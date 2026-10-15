---
name: configure-consumer-competition-profile
description: Create or validate a controlled Australian consumer and competition business profile before assessment. Use for scope, evidence owners and approval controls. Do not use to approve a profile, determine coverage or import confidential matter data into the public repository.
---

# Configure Consumer Competition Profile

Australian Commonwealth law and ACL application in the identified state or territory.
Snapshot 2026-10-13; verify law at the conduct date and intended decision horizon.
Record assumptions explicitly; no missing fact defaults to a favourable answer.
Every output requires review by a qualified lawyer and does not replace professional judgment.

Read the [source and control method](../../references/consumer-competition-source-and-control-method.md)
and [official source register](../../references/official-source-register.md).
Verify every statutory citation at legislation.gov.au through `$check-commonwealth-legislation`;
for state or territory application use its official legislation publisher. Record provision,
version, effective date, checked date, observation and evidence state. If unavailable, say
'verify against <official source>' and leave the affected proposition not verified.

## Workflow

1. Confirm entity, Australian jurisdictions, factual as-at date, scope and responsible lawyer.
2. Read the [profile schema](../../references/consumer-competition-profile-schema.md).
   Take the employment profile schema's Profile ID, Profile version, Status,
   As-at date, Approved by role, Approved at and Review due fields, and the
   `$configure-employment-profile` workflow's existing-profile/version capture,
   requester/approving-role check, unknown-field handling and human decision gate.
   Apply those controls to this business profile only; do not create an employment
   assessment or import workforce, award, headcount or coverage fields.
   Model status stays draft; preserve IDs/version history and leave approval blank.
3. Inventory products, supplier/manufacturer/importer roles, customer cohorts, markets,
   representations, transactions, financial evidence, safety systems and document versions.
   Record each as evidenced, disputed or unknown with source/date/confirmer.
4. Separate alleged legal coverage, exemptions and immunities from facts. Flag conflicts
   and missing evidence; legal thresholds belong to the relying assessment.
5. Produce a draft profile, change log and validation/gap table. Leave approved-by and
   approved-at blank; name the authorised human who must approve. Save only when the
   user names a controlled destination; no confidential data belongs in this repository.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`. Evidence states apply to individual propositions separately.

Profile draft; field validation; evidence and assumption register; changes from prior version; responsible approver and review triggers.
Every finding records source, version, pinpoint, checked date, assumptions, evidence
state, missing step and responsible qualified lawyer. No output is approval to act.

## Fail closed

Unresolved authority or decisive facts prevent a coverage conclusion. Never infer approval from use of an earlier profile or a request to configure it.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`.
  Verifies legislation, instruments, commencement and case-law leads at
  official publishers.
- `australian-employment-fair-work` (hand-off):
  `configure-employment-profile`. Reuses controlled profile approval and
  versioning patterns without importing coverage conclusions.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
