---
name: review-marketing-claims
description: Review Australian marketing, environmental, comparative and pricing claims across the full purchase journey. Use before campaign or subscription review and to distinguish current drip-pricing rules from future UTPA reforms. Do not use to publish advertisements, certify claims or determine privacy compliance.
---

# Review Marketing Claims

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

1. Capture exact claims, visuals, audience, channel, dates, comparison baseline,
   footnotes, substantiation and every checkout/renewal screen. Missing context stays missing.
2. Verify ACL ss 18 and 29 at the official CCA source. Analyse the overall impression and
   specific representation categories separately; disclaimers do not substitute for analysis.
3. For environmental claims consult the linked ACCC environmental claims guide as guidance.
   Apply ACL s 4 to future representations, including net-zero targets: a representation
   made without reasonable grounds is taken to be misleading; reasonable grounds alone
   do not establish that it is not misleading. Check the evidence rules in s 4(2)–(3).
   Apply ss 33–34 separately to conduct in trade or commerce liable to mislead the public
   about goods or services, including their nature, characteristics, suitability or quantity,
   and, for goods, manufacturing process. Verify each provision at the official CCA source.
   Test lifecycle boundaries, evidence date, methodology, certification, offsets, exclusions,
   vague absolute language and evidence for future targets. Record what the evidence supports
   and possible narrower wording; do not label an aspiration proven or ACCC-approved.
4. Compare like-for-like products, timing, geography, units, inclusions and substantiation
   for comparative advertising; record baseline drift and unsupported superiority claims.
5. Verify ACL s 48 single-price scope, prominence, quantifiable components, optional charges,
   taxes, delivery and exceptions from the text. Audit fees and default selections from
   first price to payment; assess current ss 18/29/48 before future reforms.
6. Verify the 2026 Unfair Trading Practices Act s 2 and Schedule 1 at legislation.gov.au.
   Label enacted, not yet in force (commences 1 July 2027), and separate future drip-pricing
   and subscription preparation from current breaches. Reuse commercial-drafting UTPA 2026
   notes and unfair-contract-terms checklist via `$draft-website-terms` and
   `$review-draft-against-checklist`; verify cohort, regulations and transition at use.
7. Route tracking, profiling or personalised advertising to `$assess-australian-privacy-issues`
   and relevant decision transparency to `$assess-automated-decision-transparency`.
   Return claim-by-claim findings and proposed edits for lawyer review, never publication.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`. Evidence states apply to individual propositions separately.

Claim inventory; impression and representation tests; substantiation gaps; environmental/comparison analysis; fee journey and single-price issues; current/future split; proposed edits and reviewer decisions.
Every finding records source, version, pinpoint, checked date, assumptions, evidence
state, missing step and responsible qualified lawyer. No output is approval to act.

## Fail closed

An unsubstantiated claim remains unsubstantiated. Block a clean-compliance conclusion when creatives, purchase journey, official text or supporting methodology are missing. Never apply an uncommenced reform as a current duty.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`.
  Verifies legislation, instruments, commencement and case-law leads at
  official publishers.
- `australian-commercial-drafting` (hand-off): `draft-website-terms`,
  `review-draft-against-checklist`. Reuses the UCT checklist, UTPA 2026 notes
  and operative website/services drafting.
- `australian-privacy-cybersecurity` (hand-off):
  `assess-australian-privacy-issues`,
  `assess-automated-decision-transparency`. Assesses advertising data,
  decision transparency and safety-incident privacy issues.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
