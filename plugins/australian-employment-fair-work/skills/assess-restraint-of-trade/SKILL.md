---
name: assess-restraint-of-trade
description: Issue-spot Australian employment restraints against verified common-law reasonableness, NSW restraint legislation and the status of proposed Commonwealth non-compete reforms. Use for exit or clause reviews; never certify enforceability, assume a 2027 ban is in force or send demands.
---

# Assess Restraint of Trade

Jurisdiction: Australia; Fair Work application requires a verified national
system basis. State overlays are separately identified. Snapshot: 2026-10-13;
this is a research baseline, not a current-law assurance. Verify every relied-on
provision, threshold and commencement at its official publisher for the relevant
date, using `$check-commonwealth-legislation` for Commonwealth law.

Read the [source and control method](../../references/fair-work-source-and-control-method.md),
reuse the [employment profile schema](../../references/employment-profile-schema.md)
and consult the [extension source checklist](../../references/employment-extension-sources.md).
Assume only evidenced instructions and documents; unknown facts stay unknown.
Every output requires review by a qualified lawyer before reliance.

## Workflow

1. Reuse `$configure-employment-profile` and the employment profile schema. Obtain the full contract, variation and execution dates, governing law, work locations, role, income year/basis, departure circumstances, intended activity and exact restraint wording. Separate non-compete, client/worker non-solicitation, non-dealing, confidentiality and IP protections.
2. Build a common-law reasonableness issues table: claimed legitimate interest and evidence, employee access/influence, duration, geography, restricted activities/persons, public interest, bargaining context and narrower alternatives. Distinguish employment from sale-of-business restraints. Verify applicable judgments using `$route-case-citation` at their official court publishers before asserting rules, severance or enforceability. Unverified case leads remain discovery only; cascading alternatives do not guarantee enforcement.
3. For NSW, verify Restraints of Trade Act 1976 s 4 at legislation.nsw.gov.au with `$check-nsw-legislation`. Do not import that statutory treatment into other states. The official text could not be retrieved for this snapshot: verify against legislation.nsw.gov.au before asserting its effect, public-policy test or remedial powers. Keep any NSW-specific outcome unresolved until the official provision is checked.
4. Check Commonwealth reform status using Treasury's non-compete review and consultation pages, Parliament and legislation.gov.au with `$trace-commonwealth-legislative-change`. At the snapshot the ban for employees below the high income threshold is announced/proposed only; Treasury describes 2027 as intended timing contingent on legislation. No enacted Act or commencement date was confirmed. Do not tell an employee their current clause is void because of a promised 2027 change. Record any later verified enactment as enacted, not yet in force (commences <verified date>) where applicable; do not infer commencement from a press release.
5. Distinguish the relevant employee high income threshold from the contractor threshold and verify the relevant year/earnings rules; do not cache a dollar figure or assume all restraint types/cohorts share the proposed ban. Use `$assess-employee-vs-contractor` where worker status is disputed. Examine transition, making/variation dates and scope of any enacted reform before applying it.
6. For confidentiality/data issues use `$assess-australian-privacy-issues`; for clause options name `$review-draft-against-checklist` and the commercial-drafting clause-bank.md. Record urgent litigation and interim-relief questions for a qualified lawyer; route candidate procedural dates to `$compute-procedural-deadlines`.
7. Return clause-specific arguments, evidence gaps, reform status and proportionate options. Qualified lawyer review is required before advice, demands or enforcement; no enforceability certificate.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

Return: Exact clause and category; governing-law gate; legitimate-interest/reasonableness evidence; verified case sources; NSW source status; Commonwealth proposal/enactment/commencement record; threshold year/source; options and urgent human decisions. Include scope/date/assumptions, evidence state for each
proposition, official source URL/identifier, version, provision or clause,
actual checked date, unresolved issue/resolver and qualified lawyer decisions.
Snapshot dates never substitute for the date a source was actually accessed.
An unavailable named skill means its step was not done; name the plugin to install.

## Fail closed

No restraint text or governing law: `NOT READY`. Unverified NSW provision or case blocks its legal-effect conclusion. Foreign law or sale-of-business merits: `OUTSIDE SCOPE`. No injunction prediction, sending demands, deleting evidence or assurance that a proposal invalidates existing terms.
Unverified law is labelled `NOT VERIFIED` with “verify against <official source>”;
stop the affected conclusion while completing supported issue spotting.
No saving outside the approved matter system, sending, filing, signing or payment
is authorised by invocation of this skill.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`, `route-case-citation`,
  `trace-commonwealth-legislative-change`. Verifies the Fair Work Act and
  related legislation and case-law leads against the official sources.
- `australian-litigation-deadlines` (required):
  `compute-procedural-deadlines`. Computes the Fair Work Commission time
  limits the termination assessment flags.
- `australian-commercial-drafting` (hand-off):
  `review-draft-against-checklist`. Provides services drafting, clause review
  and the existing UCT checklist and UTPA 2026 notes.
- `australian-privacy-cybersecurity` (hand-off):
  `assess-australian-privacy-issues`. Assesses personnel-data, confidentiality
  and privacy application questions.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
