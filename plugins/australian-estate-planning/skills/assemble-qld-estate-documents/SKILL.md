---
name: assemble-qld-estate-documents
description: Prepare solicitor-review drafts of a Queensland will and enduring power of attorney for one client using centrally maintained approved precedents, an approved drafting playbook and provenance-cited instructions. Draft all supported content, visibly mark unresolved facts and decisions, and return a drafting-issues register. Use only for practitioner-led Queensland matters. Do not use for self-represented parties, other jurisdictions, advance health directives, superannuation death benefit nominations, trusts or probate.
---

# Assemble Queensland Estate Documents

Prepare working drafts from the approved precedent library for one client. The
responsible solicitor controls the instructions, clause choices and final legal
judgment. Never create a generic instrument or modify an approved source
precedent.

Read the
[source and control method](../../references/estate-planning-source-and-control-method.md)
first, then use the
[Queensland instruction record schema](../../references/qld-instruction-record-schema.md)
and [approved playbook usage rules](../../references/playbook-usage-rules.md).
The [Queensland execution formalities reference](../../references/qld-execution-formalities.md)
lists the statutory points the drafts must leave for the solicitor.

## Workflow

1. Fix the client, jurisdiction and document set.
   - Use one client per run. Start a separate run for each member of a couple.
   - Confirm that a practitioner is acting for a client in a Queensland matter
     and record the responsible solicitor.
   - Record whether the client seeks a will, an enduring power of attorney or
     both. A Queensland enduring power of attorney may cover financial
     matters, personal (including health) matters or both; record the
     instruction, never choose. Ask if the requested set is unclear.
   - Select each source document from the centrally maintained approved
     precedent library. Never accept an uploaded substitute precedent and
     never substitute a generic document or the approved statutory form on
     its own.
2. Build the instruction table.
   - Extract every applicable schema field and cite its provenance by page,
     section, question or practitioner instruction.
   - Record a blank, illegible, inconsistent or ambiguous value as `cannot be
     determined`. Never infer a plausible value.
   - Flag inconsistent names, minority, intended marriage, marriage, divorce,
     the end of a de facto relationship, separation, witness relationships,
     attorney eligibility, existing instruments, jointly held assets,
     superannuation interests, possible capacity or undue influence concerns,
     and every other issue identified by the practitioner. Do not resolve
     legal effect.
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
     issue. Never state that a document is approved or ready to sign, or select
     physical or remote execution.
   - Execution, witnessing, attorney acceptance, registration and filing occur
     outside this workflow.

## Result contract

Use one status for each requested document:

- `DRAFT READY FOR SOLICITOR REVIEW`
- `PARTIAL DRAFT – UNRESOLVED ISSUES`
- `BLOCKED – NO DRAFT PRODUCED`
- `OUTSIDE SCOPE`

```text
Matter: <client; Queensland; requested documents; responsible solicitor>
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
Route self-represented parties, non-Queensland matters, advance health
directives, superannuation death benefit nominations, trusts, probate and any
other stated exclusion to `OUTSIDE SCOPE`. Never modify the source, invent
content, select physical or remote execution, or mark a document approved or
ready to sign.
