---
name: draft-nda
description: Prepare a first-draft mutual or one-way Australian NDA from evidenced party details and commercial instructions, with purpose, exclusions, duration and permitted disclosure. Use for practitioner-led commercial confidentiality drafting; do not use to guarantee secrecy, draft restraints or approve execution.
---

# Draft NDA

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

1. Identify both legal parties, drafting side, mutual or one-way direction,
   defined purpose, governing state/territory, intended start date and reviewer.
   Confirm affiliates, representatives and past disclosures; never backdate.
2. Build a provenance-cited instruction table for the disclosure window,
   definition, permitted use, recipients, exclusions, duration, survival,
   security, compelled disclosure, return trigger and retention exceptions.
   Apply approved profile positions only within their scope. Surface conflicts.
3. Draft full operative text using original wording or authorised privately
   supplied material. Read relevant [clause bank](../../references/clause-bank.md)
   examples. Include parties, purpose, confidential information and derived
   material, exclusions for public/prior-known/independently developed/lawfully
   received information, permitted use, reasonable protection, need-to-know
   representatives and their responsibility, and lawful compelled disclosure.
   Preserve protected disclosures and reporting rights; do not suppress them.
4. Set the disclosure term separately from surviving obligations. Present
   instructed trade-secret treatment as a separate choice. Draft return or
   destruction, lawful retention and routine backup handling that match actual
   capabilities. Include no licence beyond the purpose, no obligation to proceed,
   relief that may be sought subject to the court's discretion, notices,
   governing law/jurisdiction and appropriate authority/execution blocks.
5. Reconcile defined terms, dates and one-way roles. Do not turn a one-way NDA
   into mutual duties silently. Check any liability or indemnity interaction;
   apply the [UCT checklist](../../references/unfair-contract-terms-checklist.md)
   if standard-form consumer/small-business coverage is possible. Verify any
   statutory proposition with `$check-commonwealth-legislation`. Run
   `review-draft-against-checklist` before handing over.

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

Block only when the Australian perimeter, party roles or requested NDA cannot be
identified sufficiently to draft. Missing dates, terms, recipient details or
commercial choices ordinarily produce a marked partial draft, not invented values.
Never guarantee an injunction or absolute deletion. Mark unresolved source-dependent
wording and law as not verified. Restraints, settlement releases and final legal
opinions are `OUTSIDE SCOPE`. A qualified lawyer must review all wording.

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
