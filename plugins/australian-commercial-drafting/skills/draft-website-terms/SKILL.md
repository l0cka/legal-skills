---
name: draft-website-terms
description: Prepare first-draft Australian SaaS or subscription website terms for consumers and small businesses, preserving consumer guarantees and flagging unfair terms, renewal, refunds and liability choices. Use for practitioner-led terms drafting, not financial products, regulated-sector compliance certification or publication.
---

# Draft Website Terms

Jurisdiction: Australian Commonwealth law and the identified governing state or
territory. Record the legal as-at and intended use dates. The 2026-10-13 source
snapshot is a currency limit, not live verification. Verify every applicable
statutory provision on legislation.gov.au (NSW overlays on legislation.nsw.gov.au)
using `$check-commonwealth-legislation` and, for NSW, `$check-nsw-legislation`;
use the corresponding official-source workflow for other states or territories.
Never rely on model memory. Record assumptions and input provenance. A qualified
lawyer must review every output before use.

Read the [source and control method](../../references/drafting-source-and-control-method.md)
first. Use the [profile schema](../../references/drafting-profile-schema.md)
for standing positions and transaction instructions.

## Workflow

1. Confirm supplier, product, customer cohorts, governing state/territory,
   service delivery, contracting/acceptance flow, term and legal/use dates.
   Collect price/GST display, billing, trial conversion, renewal reminders,
   cancellation channels, support, outages, refunds and data exit practices.
   Do not promise a feature or process the business has not confirmed.
2. Verify the *Competition and Consumer Act 2010* (Cth), Schedule 2 (ACL), on
   legislation.gov.au with `$check-commonwealth-legislation`. Check consumer
   acquisition under s 3 independently of consumer-contract/UCT coverage.
   Verify ss 60–64A and 267–269 before describing guarantees, limits or remedies.
   Non-excludable consumer guarantees and remedies survive all caps and refund
   rules; B2B customers can also be consumers. Do not insert a blanket exclusion.
   Verify ss 18 and 29(1)(m): statements about guarantee rights, exclusions and
   remedies must not mislead, including in refund and support processes.
3. Apply the [UCT checklist](../../references/unfair-contract-terms-checklist.md).
   Verify ACL ss 23–28, 224 and the 2022 amending Act's transition on
   legislation.gov.au: penalties from 9 November 2023; relevant making, renewal
   and variation dates; small-business threshold of fewer than 100 employees
   OR turnover below $10 million, with statutory counting and turnover rules.
   Record standard-form evidence and exceptions. No conclusion from a B2B label.
4. Draft full terms: supplier/product, eligibility/account security, licence
   and acceptable use, service/support commitments, order/acceptance mechanics,
   price and GST, payment, term/trial, renewal, cancellation, refunds, IP and
   customer content, confidentiality/data handling, statutory rights, liability,
   suspension/termination, data export, complaints/disputes, notices and law/forum.
   Use relevant [original clauses](../../references/clause-bank.md) as options.
5. Disclose auto-renewal price, interval, renewal timing, reminders, cut-off and
   accessible cancellation before acceptance. Distinguish change-of-mind refunds
   from mandatory remedies. Avoid all-sales-final language. Variation needs
   defined reasons, meaningful advance notice and a right to cancel without
   penalty for material disadvantage, including unused prepaid refunds. Confirm
   notice periods and implementation rather than choose arbitrary numbers.
   Separate these current ACL controls from the 2026 unfair trading reforms:
   enacted, commences 1 July 2027. Verify the amending Act's s 2 and Schedule 1
   on legislation.gov.au: future ss 28B and 48A, subscription definitions and
   exclusions in ss 48B–48C, disclosure in s 48D, prescribed ongoing notices in
   s 48E, and straightforward exit in s 48F (online where s 48F(2) applies).
   Check ss 48G–48H cohort tests, regulations and s 312 transition for new and
   existing contracts renewed, extended, continued or varied after commencement;
   s 312 lists ss 48B, 48E and 48F, so assess s 48D separately. Check s 311 for
   future s 28B conduct. Produce a current/future implementation ledger matching
   intended use dates and actual checkout, notice and cancellation processes.
   Treat a Treasury small-business extension of the unfair trading ban as a
   proposal, separately from enacted small-business subscription protections.
   Unconfirmed regulations or application need visible review markers, not
   invented timing rules or a claim that future duties are already operative.
6. State cap amount/formula, period, aggregation and indemnity interaction.
   Carve out non-excludable rights and obtain instructions for fraud, wilful
   misconduct, injury, IP, confidentiality and privacy treatment. Do not use a
   generic savings clause to cure contradictory exclusions. Check narrow
   suspension grounds, urgency, notice/cure, restoration and termination
   consequences against proportionality and the whole contract. Review forum
   and dispute access for consumer burden. Link to the privacy policy without
   implying it establishes consent. Run `review-draft-against-checklist`.

## Result contract

Use one status per requested document: `DRAFT READY FOR SOLICITOR REVIEW`,
`PARTIAL DRAFT – UNRESOLVED ISSUES`, `BLOCKED – NO DRAFT PRODUCED` or
`OUTSIDE SCOPE`. A review-ready draft has no unresolved markers; it still requires
qualified lawyer approval and is never ready to sign or publish.

Return the full working draft labelled `DRAFT – LAWYER REVIEW REQUIRED`, the
instruction table, assumptions, source ledger (official URL, provision, version,
effective date, checked date and evidence state), selected positions and departures,
and an issues register. Each `[REVIEW REQUIRED – <issue ID: missing fact or decision>]`
marker must match an entry listing every affected location, source, consequence,
options and required lawyer decision. Add `PARTIAL DRAFT – UNRESOLVED ISSUES
IDENTIFIED` inside any marked draft. Give a bounded list of next decisions and
specialist hand-offs. Save only to a user-authorised controlled destination.

## Fail closed

Block when product, supplier role or Australian perimeter cannot be identified.
Continue supported sections with visible markers for missing mechanics or choices.
Never waive ACL rights, declare UCT compliance, invent refund practices or certify
an acceptance flow. Treat unavailable official verification as not done and mark
its affected clauses and issues. Regulated products and overseas regimes are
`OUTSIDE SCOPE` for the affected part. A qualified lawyer must review before use;
publication and subscription-system changes require separate authority.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`. Verifies Commonwealth and state legislation at the
  relevant drafting date.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
