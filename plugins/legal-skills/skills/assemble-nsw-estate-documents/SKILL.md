---
name: assemble-nsw-estate-documents
description: Prepare solicitor-review drafts of a NSW will, enduring power of attorney and appointment of enduring guardian for one client using centrally maintained approved precedents, an approved drafting playbook and provenance-cited instructions. Draft all supported content, visibly mark unresolved facts and decisions, and return a drafting-issues register. Use only for practitioner-led NSW matters. Do not use for self-represented parties, other jurisdictions, advance care directives, superannuation death benefit nominations, trusts or probate.
---

# Assemble NSW Estate Documents

Prepare working drafts from the approved precedent library for one client. The
responsible solicitor controls the instructions, clause choices and final legal
judgment. Never create a generic instrument or modify an approved source
precedent.

Read the
[source and control method](../../references/estate-planning-source-and-control-method.md)
first, then use the
[NSW instruction record schema](../../references/nsw-instruction-record-schema.md)
and [approved playbook usage rules](../../references/playbook-usage-rules.md).

## Workflow

1. Fix the client, jurisdiction and document set.
   - Use one client per run. Start a separate run for each member of a couple.
   - Confirm that a practitioner is acting for a client in a New South Wales
     matter and record the responsible solicitor.
   - Record whether the client seeks a will, enduring power of attorney or
     appointment of enduring guardian. Ask if the requested set is unclear.
   - Select each source document from the centrally maintained approved
     precedent library. Never accept an uploaded substitute precedent and
     never substitute a generic document.
2. Build the instruction table.
   - Extract every applicable schema field and cite its provenance by page,
     section, question or practitioner instruction.
   - Record a blank, illegible, inconsistent or ambiguous value as `cannot be
     determined`. Never infer a plausible value.
   - Flag inconsistent names, minority, intended marriage, marriage, divorce,
     separation, witness-beneficiary relationships, existing instruments,
     jointly held assets, superannuation interests, possible capacity or undue
     influence concerns, and every other issue identified by the practitioner.
     Do not resolve the legal effect.
3. Prepare working copies.
   - Copy the selected approved precedent and leave the source unchanged.
   - Populate supported content from the instruction table. Apply standing
     positions from the approved playbook under its usage rules. Keep names and
     roles consistent across the document set.
   - Continue drafting all supported parts when a fact or decision remains
     unresolved. Insert `[REVIEW REQUIRED – <missing fact or unresolved
     decision>]` at every affected location. Preserve any unselected approved
     alternatives for solicitor review.
   - Never hide a blank, guess a fact, select an unresolved clause or introduce
     a legal position not found in the instructions and approved material.
     Never invent, combine or improve clause text.
4. Report and hand over.
   - Put `DRAFT – SOLICITOR REVIEW REQUIRED` inside every draft. Add `PARTIAL
     DRAFT – UNRESOLVED ISSUES IDENTIFIED` when any review marker remains.
   - Return the drafts, instruction summary, change summary and a
     drafting-issues register. Every review marker must have a matching entry
     recording the document, location, issue, provenance and required
     solicitor decision.
   - The responsible solicitor must review the drafts and resolve every marked
     issue. Never state that a document is approved or ready to sign.
   - Execution, witnessing and filing occur outside this workflow.

## Result contract

Use one status for each requested document:

- `DRAFT READY FOR SOLICITOR REVIEW`
- `PARTIAL DRAFT – UNRESOLVED ISSUES`
- `BLOCKED – NO DRAFT PRODUCED`
- `OUTSIDE SCOPE`

```text
Matter: <client; NSW; requested documents; responsible solicitor>
Approved sources: <precedent and approved playbook identifiers used>
Instruction summary: <provenance; qualifications and risk flags>
Documents: <per document: status and working-draft filename>
Drafting issues: <per marker: document, location, issue, provenance, decision>
Change summary: <content populated and approved alternatives selected>
Limitations: <drafts only; unresolved legal and factual issues>
```

## Fail closed

Return `BLOCKED – NO DRAFT PRODUCED` only where the client, jurisdiction or
requested document cannot be identified, or the required approved precedent is
missing or unusable. Missing facts and unresolved decisions ordinarily produce
a visibly marked `PARTIAL DRAFT – UNRESOLVED ISSUES`, not a blank document.
Route self-represented parties, non-NSW matters, advance care directives,
superannuation death benefit nominations, trusts, probate and any other stated
exclusion to `OUTSIDE SCOPE`. Never modify the source, invent content, or mark a
document approved or ready to sign.
