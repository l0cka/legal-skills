---
name: draft-services-agreement
description: Prepare a first-draft Australian B2B services or contractor agreement and SOW covering scope, fees, GST, IP, moral rights, confidentiality, risk allocation and exit. Flag worker classification and sham contracting for employment review; do not label employment as contracting or approve execution.
---

# Draft Services Agreement

Jurisdiction: Australian Commonwealth law and the identified governing state or
territory. Record the legal as-at and intended use dates. The 2026-10-14 source
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

1. Identify customer and supplier, drafting side, entity types, governing
   state/territory, service model, personnel/subcontracting and legal/use dates.
   Collect scope, deliverables, dependencies, milestones, acceptance, changes,
   fees, invoice/payment mechanics, GST status and notices with provenance.
2. If an individual supplies labour or facts suggest employee-like control,
   flag classification and sham contracting. An ABN, invoice or contractor label
   is not decisive. Hand off to
   `$configure-employment-profile`
   and
   `$map-fair-work-obligations`.
   Verify Fair Work Act 2009 ss 15AA–15AD and 357–359 on legislation.gov.au
   with `$check-commonwealth-legislation`. Section 357(2) requires the employer
   to prove a reasonable belief that the contract was for services; this defence
   applies from 27 February 2024. Section 15AA commenced on 26 August 2024;
   assess the real substance, practical reality and whole relationship, including
   performance as well as terms, subject to coverage, transition and ss 15AB–15AD
   opt-out rules (s 15AC addresses effect, s 15AD revocation). Verify the Closing
   Loopholes No. 2 Act 2024, s 2 table items 11 and 21, Schedule 1 Parts 9 and 15.
   Mark classification-dependent clauses
   unresolved pending specialist/lawyer review; continue independent B2B sections.
   Do not claim that drafting an independent-contractor recital cures the risk.
3. Prepare a complete agreement and SOW. Include scope/exclusions, milestones,
   objective acceptance and rework, customer dependencies, change control,
   personnel, fees/payment/disputed invoices, GST, expenses, records and term.
   Confirm taxable supply/invoice treatment under the GST Act on legislation.gov.au
   if relied on; an ABN is not GST registration. Distinguish GST-inclusive and
   exclusive prices, adjustments and reimbursement treatment.
4. Obtain an express ownership OR licence choice for deliverables. Identify
   background IP, newly created rights, third-party/open-source components,
   transfer trigger, licence scope, sublicensing and chain of title. Verify
   Copyright Act 1968 ss 196–197 and Part IX, especially s 195AW for films/works
   in films, s 195AWA for other works and s 195AWB for invalidated consents,
   on legislation.gov.au. Obtain creator-specific written moral rights consents
   for identified acts/omissions and attribution requirements; moral rights
   are not assigned with copyright. Do not presume a company can consent for
   every individual author or replace consents with a blanket waiver.
5. Draft confidentiality, permitted disclosures, security/data responsibilities,
   insurance if instructed, warranties, liability and indemnities. Define cap
   formula/period/aggregation, carve-outs for non-excludable liability and
   instructed risk categories, and interaction with indemnities. State triggers,
   causation, mitigation, defence control and settlement protections. Never
   invent insurance levels or assign every risk to the counterparty by default.
6. Draft termination, objective breach triggers, cure periods, convenience exit
   if instructed, suspension, accrued fees, unused prepaid amounts, transition,
   data return/export and survival. Include escalation/mediation, urgent relief,
   notices, assignment, precedence, governing law/jurisdiction and authority/
   execution blocks. Use relevant [original clauses](../../references/clause-bank.md).
7. Apply the [UCT checklist](../../references/unfair-contract-terms-checklist.md)
   and verify ACL Schedule 2 ss 3, 23–28 and 60–64A on legislation.gov.au when
   relevant: B2B services can attract consumer guarantees and small-business
   UCT protection. Reconcile the SOW, IP, cap, indemnity and exit provisions.
   Run `review-draft-against-checklist` before handover.

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

Block when the service model, drafting roles or Australian perimeter cannot be
identified. Missing fees, IP choices, caps or dates produce marked partial drafts.
Unresolved worker status blocks classification-dependent wording, not all supported
commercial work. Record an unavailable employment hand-off as not made. Do not
invent consents, ownership, registration or legal verification. Employment
contracts and specialist regulated agreements are `OUTSIDE SCOPE` for the affected
part. A qualified lawyer must review all clauses and execution; never sign or send.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`. Verifies Commonwealth and state legislation at the
  relevant drafting date.
- `australian-employment-fair-work` (hand-off):
  `configure-employment-profile`, `map-fair-work-obligations`. Assesses worker
  classification and sham-contracting concerns before contractor wording is
  settled.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
