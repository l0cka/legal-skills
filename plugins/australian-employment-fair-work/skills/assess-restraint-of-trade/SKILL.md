---
name: assess-restraint-of-trade
description: Issue-spot Australian employment restraints against verified common-law reasonableness, NSW restraint legislation and the status of proposed Commonwealth non-compete reforms. Use for exit or clause reviews; never certify enforceability, assume a 2027 ban is in force or send demands.
---

# Assess Restraint of Trade

Jurisdiction: Australian employment restraints under applicable common law, with
a separate NSW statutory limb and a Commonwealth proposal-status track. Verify
judgments at official court publishers with `$route-case-citation`, NSW
legislation at legislation.nsw.gov.au with `$check-nsw-legislation`, and any
Commonwealth enactment at legislation.gov.au with
`$check-commonwealth-legislation`. Determine governing law separately from Fair
Work coverage. Currency is limited to the linked extension reference.

The NSW Restraints of Trade Act 1976 limb is unverified at this snapshot because
NSW sites block automated retrieval: verify against legislation.nsw.gov.au
before asserting its statutory content or effect.

Read the [source and control
method](../../references/fair-work-source-and-control-method.md), reuse the
[employment profile schema](../../references/employment-profile-schema.md) and
consult the [extension source
checklist](../../references/employment-extension-sources.md). Assume only
evidenced instructions and documents; unknown facts stay unknown. Every output
requires review by a qualified lawyer before reliance.

## Workflow

1. Reuse `$configure-employment-profile` and the employment profile schema.
   Obtain the full contract, variation and execution dates, governing law, work
   locations, role, income year/basis, departure circumstances, intended
   activity and exact restraint wording. Separate non-compete, client/worker
   non-solicitation, non-dealing, confidentiality and IP protections. Flag the
   co-worker non-solicitation row for the announced/proposed only reform track
   in step 4; do not treat client and co-worker terms as the same category.
2. Build a common-law reasonableness issues table: claimed legitimate interest
   and evidence, employee access/influence, duration, geography, restricted
   activities/persons, public interest, bargaining context and narrower
   alternatives. Distinguish employment from sale-of-business restraints. Verify
   applicable judgments using `$route-case-citation` at their official court
   publishers before asserting rules, severance or enforceability. Unverified
   case leads remain discovery only; cascading alternatives do not guarantee
   enforcement. Flag each cascading row for the announced/proposed only
   restriction in the watch-register item; keep the current-law and proposal
   analyses separate.
3. For NSW, verify Restraints of Trade Act 1976 s 4 at legislation.nsw.gov.au
   with `$check-nsw-legislation`. Do not import that statutory treatment into
   other states. The official text could not be retrieved for this snapshot:
   verify against legislation.nsw.gov.au before asserting its effect,
   public-policy test or remedial powers. Keep any NSW-specific outcome
   unresolved until the official provision is checked.
4. Use `$track-fair-work-developments` and the [watch
   register](../track-fair-work-developments/references/watch-register.json),
   item `non-compete-ban`, as the owner of proposal status. Recheck its official
   Treasury draft and any later Parliament/Federal Register record with
   `$trace-commonwealth-legislative-change`. The item maps the proposed cohort,
   co-worker non-solicitation ban, cascading restriction, no-poach/wage-fixing
   changes, draft commencement and provision-specific application. Treat all of
   these as announced/proposed only, not current prohibitions. Treasury's 2027
   policy expectation does not fix a legal start date; draft clause 2 proposes
   quarter-day commencement after Royal Assent. No enacted Act or commencement
   date was confirmed. Do not tell an employee their clause is void because of
   the proposal. Record a later verified enactment as enacted, not yet in force
   (commences <verified date>) where applicable.
5. Distinguish the relevant employee high income threshold from the contractor
   threshold and verify the relevant year/earnings rules; do not cache a dollar
   figure or assume all restraint types/cohorts share the proposed ban. Use
   `$assess-employee-vs-contractor` where worker status is disputed. Examine
   transition, making/variation dates and scope of any enacted reform before
   applying it.
6. For confidentiality/data issues use `$assess-australian-privacy-issues`; for
   clause options name `$review-draft-against-checklist` and the
   commercial-drafting clause-bank.md. Record urgent litigation and
   interim-relief questions for a qualified lawyer; route candidate procedural
   dates to `$compute-procedural-deadlines`.
7. Return clause-specific arguments, evidence gaps, reform status and
   proportionate options. Qualified lawyer review is required before advice,
   demands or enforcement; no enforceability certificate.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

Return: Exact clause and category; governing-law gate;
legitimate-interest/reasonableness evidence; verified case sources; NSW source
status; watch-register item and source evidence; co-worker/cascading proposal
flags; Commonwealth proposal/enactment/commencement record; threshold
year/source; options and urgent human decisions. Include scope/date/assumptions,
evidence state for each proposition, official source URL/identifier, version,
provision or clause, actual checked date, unresolved issue/resolver and
qualified lawyer decisions. Snapshot dates never substitute for the date a
source was actually accessed. An unavailable named skill means its step was not
done; name the plugin to install.

## Fail closed

No restraint text or governing law: `NOT READY`. Unverified NSW provision or
case blocks its legal-effect conclusion. Foreign law or sale-of-business merits:
`OUTSIDE SCOPE`. No injunction prediction, sending demands, deleting evidence or
assurance that a proposal invalidates existing terms. Unverified law is labelled
`NOT VERIFIED` with “verify against <official source>”; stop the affected
conclusion while completing supported issue spotting. No saving outside the
approved matter system, sending, filing, signing or payment is authorised by
invocation of this skill.

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
  `compute-procedural-deadlines`. Computes candidate FWC, AHRC and court
  deadlines only where a verified rule is available; otherwise identifies the
  provision without calculating a date.
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
