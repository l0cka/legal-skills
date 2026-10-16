---
name: review-draft-against-checklist
description: Review an Australian commercial draft for missing clauses, inconsistent instructions, undefined terms, broken references, placeholders and unfair-contract-terms risk. Return a prioritised issues table for a qualified lawyer; do not certify enforceability or silently rewrite the supplied draft.
---

# Review Draft Against Checklist

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

1. Fix document/version, document family, drafting side, governing state or
   territory, legal/use date, instructions and profile versions. Preserve the
   supplied draft. Review is read-only unless edits are expressly requested.
   If pages, schedules, attachments or incorporated documents are absent, state
   the review perimeter and do not infer their content.
2. Check the appropriate family coverage: NDA purpose/exclusions/term/survival/
   return/no licence/relief; subscription guarantees/renewal/refunds/variation/
   cap/suspension/exit; privacy APP mapping/data flows/marketing/current-future
   duties; services SOW/payment/GST/IP/moral rights/indemnities/termination/disputes.
   Treat confirmed intentional omissions separately from unexplained gaps.
3. Inventory defined terms and every usage, including case/plural differences,
   unused definitions and inconsistent party names/roles. Resolve each internal
   cross-reference, schedule, link and precedence rule against the actual draft;
   report missing/ambiguous targets and conflicting definitions. Check dates,
   amounts, percentages, cap formula/period, renewal and notice timing, survival,
   IP rights and indemnity/cap interactions across all supplied documents.
4. Sweep for blank placeholders: empty brackets/fields, angle-bracket values,
   underscores, TBD/TBC, alternatives not selected, `[REVIEW REQUIRED – ...]`
   markers and empty signature/date fields. Separate intentional execution
   blanks from unresolved substantive content. Match every marker to the issues
   register, including duplicates and orphan register entries. Never count a
   clause as complete simply because a heading exists.
5. Apply the [UCT checklist](../../references/unfair-contract-terms-checklist.md),
   including coverage and transition, ACL Schedule 2 ss 23–25 grey-list risks,
   standard form under s 27 and whole-contract/legitimate-interest analysis.
   Verify on legislation.gov.au with `$check-commonwealth-legislation`; confirm
   consumer guarantees and statutory-rights carve-outs independently. A generic
   savings sentence cannot cure conflicting no-refund, cap or termination text.
6. For privacy policy coverage or automated-decision questions hand off to
   `$check-australian-privacy-principles`
   or
   `$assess-automated-decision-transparency`.
   For worker-status/sham-contracting questions hand off to
   `$map-fair-work-obligations`.
   Record unavailable assessments and statutory verification as not performed.
7. Prioritise consequential risks first, then substantive choices and drafting
   defects. Give proposed corrections or decision options without silently
   selecting commercial positions. Any requested revised draft must preserve
   visible unresolved markers and include a change summary.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`. This is review coverage/readiness, not draft approval. A reviewed
draft with issues may have a complete review; report its unresolved issues clearly.

Return document/version/perimeter, jurisdictions, dates, assumptions, instruction
sources and a table with: issue ID; priority; exact clause/location; issue/evidence;
consequence; applicable official source/version/provision/date/evidence state;
proposed correction/options; required decision/owner; resolution status. Include
coverage by checklist area, unavailable material/verification, marker-register
reconciliation and required qualified lawyer review. Use `potential UCT risk`;
never state a court's determination or give an unsupported clean bill of health.

## Fail closed

Return `NOT READY` if no usable draft or review perimeter exists. Return
`READY WITH QUALIFICATIONS` for a bounded partial review with missing material
or verification and list each unreviewed area. Foreign-law or final enforceability
opinions are `OUTSIDE SCOPE`. Never infer missing schedules, certify compliance,
approve execution, overwrite sources or hide placeholders. A qualified lawyer
must decide legal application, commercial changes and final wording.
