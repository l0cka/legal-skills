# Australian estate planning source and control method

## Scope

Use this method when extracting an instruction record from a completed
instruction sheet or filling a firm precedent for a New South Wales estate
planning matter — a will, an enduring power of attorney or an appointment of
enduring guardian. Every output of every workflow is a draft until the
responsible solicitor reviews it, and no output may be presented as a
finished or executable document.

The workflows serve Australian legal practitioners only. Route rather than
duplicate:

- point-in-time verification of Acts belongs to the Australian Legal
  Research plugin (`$check-nsw-legislation` and its sibling jurisdiction
  checkers) where that plugin is available, and otherwise to the official
  publisher directly;
- self-represented parties, jurisdictions other than New South Wales,
  advance care directives, superannuation death benefit nominations, trusts
  and testamentary trusts, and probate or administration are `OUTSIDE
  SCOPE` — flagged, never assessed; and
- testamentary capacity, undue influence, family provision and notional
  estate exposure, and tax consequences are the responsible solicitor's
  calls in every workflow, flagged and never resolved.

## The marker-only assembly rule

The workflows never compose a legal document and never rewrite precedent
wording. Document text changes only at explicit factual `{{field_name}}`
markers or registered `{{clause_choice:clause_point}}` markers in a firm
precedent (see the marker syntax guide), and every fill returns:

1. a **change manifest** — every location changed, the marker removed, the
   value inserted, reconciled against the precedent so any difference
   outside a marker site makes the result `NOT READY`;
2. a **gap report** — every unfilled marker, unused instruction-record field,
   and unresolved clause choice (each of which makes that document `NOT
   READY`); and
3. the **draft banner** — `DRAFT — SOLICITOR REVIEW REQUIRED` above every
   document, outside the copyable document body.

No registered precedent for a document type means that document is
`NOT READY`. There is no generic fallback document, in any circumstance.
Each clause-choice marker also requires a confirmed, closed clause-choice
register of firm-approved variants. A playbook may identify a registered
variant, but only the responsible solicitor may confirm its identifier and
verbatim text for insertion. The workflow never composes or adapts clause text.

This is an instruction-level contract rather than a deterministic script —
a deliberate decision recorded in `docs/adr/0001` of this repository: the
pack must remain plain markdown deployable on platforms that cannot execute
bundled code.

## Snapshot of the framework

At 20 August 2026 — a research snapshot, not a cached rule; every live
workflow must recheck each source:

1. **Wills** — Succession Act 2006 No 80 (NSW), current version 14 July
   2023 to date. Execution formalities in Part 2.1 (ss 5–10), revocation in
   ss 11–13, the 30-day survivorship construction default in s 35.
2. **Enduring powers of attorney** — Powers of Attorney Act 2003 No 53
   (NSW), current version 2 March 2025 to date. Creation requirements,
   prescribed witness classes and the witness certificate in s 19;
   attorney acceptance in s 20.
3. **Enduring guardianship** — Guardianship Act 1987 No 257 (NSW), current
   version 27 March 2021 to date. Appointment in Part 2 (ss 5–6E),
   including the prescribed-form requirement, eligible witness
   certification and appointee acceptance in s 6C.
4. **Prescribed forms** — the forms for enduring powers of attorney and
   enduring guardianship appointments are prescribed by regulation. The
   regulations were not verified for this snapshot: any reliance on a
   prescribed form carries a `form-prescription` qualification until the
   current regulation is checked.

The provision texts relied on by these workflows are recorded, with their
version lines and access date, in the NSW execution formalities reference.

## Sources

The only authority for NSW legislation is the official publisher,
legislation.nsw.gov.au. Treat commentary, firm knowledge bases, search
results and model memory as discovery material, never authority. When the
deployment platform allows web access, re-verify every cited provision
against the official publisher before relying on it; when it does not, the
dated formalities reference governs and the solicitor verifies manually.

## Firm material and precedence

Firm-connected material — registered precedents, the instruction-sheet
template, a connected drafting playbook, cached field maps and clause-choice
registers — is profile content: it configures the workflows but is never
authority for the law.
If profile content conflicts with a verified source, surface the conflict
and stop the affected conclusion. Playbook positions may identify only
registered variants, and every insertion requires solicitor confirmation and
is noted in the change manifest; where the playbook is silent or absent, the
marker remains, the clause choice goes to the gap report and the document is
`NOT READY`.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  application, form-prescription or extraction-provenance qualification
  remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

`extraction-provenance` qualifies a field extracted from an unregistered or
free-form instruction sheet, or from handwriting: the value was found but
its mapping is lower-confidence and the extraction gate must say so.

## Human control

The model may draft an instruction record, a field map or a filled document
set, but cannot mark it approved, confirmed or ready to execute — only the
responsible solicitor can. The workflows never:

- decide which documents a client needs;
- assess testamentary capacity or undue influence;
- resolve a conflict between instructions, or between an instruction and a
  playbook position;
- determine that an execution formality has been satisfied; or
- witness, execute, file, register or submit anything.
