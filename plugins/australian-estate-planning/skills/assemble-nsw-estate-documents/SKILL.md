---
name: assemble-nsw-estate-documents
description: Assemble draft NSW estate planning documents — a will, an enduring power of attorney and an appointment of enduring guardian — by extracting a provenance-cited instruction record from a completed client instruction sheet, halting for the responsible solicitor to confirm the extraction table, then filling the firm's own registered precedents at explicit {{field_name}} markers only, returning a change manifest, gap report and dated execution-formalities references with every fill. Use when a practitioner has a completed instruction sheet, or gives instructions directly, and the firm's precedents are available. Do not use for self-represented parties, jurisdictions other than NSW, advance care directives, superannuation death benefit nominations, trusts, probate, or to draft any document without a precedent — each of these fails closed to the responsible solicitor.
---

# Assemble NSW Estate Documents

Turn a completed instruction sheet into filled drafts of the firm's own
precedents, with the responsible solicitor confirming every step. Never
compose a document; only fill markers in a precedent.

Read the
[source and control method](../../references/estate-planning-source-and-control-method.md)
first, and work from the
[instruction record schema](../../references/instruction-record-schema.md),
the [marker syntax guide](../../references/marker-syntax-guide.md),
the [playbook usage rules](../../references/playbook-usage-rules.md) and
the [NSW execution formalities reference](../../references/nsw-execution-formalities.md).

## Workflow

1. Fix the matter and the inputs.
   - Confirm the practitioner is acting for a client in a New South Wales
     matter and name the responsible solicitor who will confirm each gate.
     A self-represented party or a non-NSW matter is `OUTSIDE SCOPE`.
   - Record which document types are sought — will, enduring power of
     attorney, appointment of enduring guardian — and ask if unspecified.
   - Locate the firm's precedent for each sought document type. A document
     type with no precedent is `NOT READY` for that type: never substitute
     a generic document.
2. Extract the instruction record.
   - From an uploaded completed instruction sheet: extract every schema
     field with its provenance (page, section or question). A blank,
     illegible or ambiguous field is `cannot be determined` with its
     location cited — never guessed. A free-form or handwritten sheet
     carries an `extraction-provenance` qualification, stated plainly.
   - Without a sheet: gather the same fields by asking the practitioner,
     recording provenance as `interview`.
   - Flag at this step: any person named inconsistently, any witness who
     is also a beneficiary (Succession Act 2006 (NSW) s 10), any
     instruction suggesting an intended marriage, divorce or separation
     (ss 12–13), any indication the client may be a minor (s 5), and any
     matter listed as flag-only in the formalities reference.
3. Halt at the extraction gate.
   - Present the extraction table — every field, value, provenance,
     evidence state — and stop. Nothing is drafted until the responsible
     solicitor confirms the table. A confirmed table stands; do not
     re-ask confirmed fields.
4. Map and fill each precedent.
   - First use of a precedent: propose the field map (marker ↔ schema
     field) for the solicitor to confirm; reuse confirmed maps thereafter.
   - Fill markers per the marker syntax guide: confirmed values only,
     identical values at repeated sites, names and roles consistent
     across the whole document set. Adopt connected playbook positions
     per the playbook usage rules; send every uncovered clause choice to
     the gap report. Never alter any text outside a marker site.
5. Report and hand over.
   - Return, for each document: the filled draft under a
     `DRAFT — SOLICITOR REVIEW REQUIRED` banner (banner outside the
     copyable document body), the change manifest reconciled against the
     precedent, and the gap report.
   - List the execution formalities for each document type from the
     formalities reference with their statutory basis and evidence state.
     Re-verify cited provisions against legislation.nsw.gov.au (or via
     `$check-nsw-legislation` where available) when the platform allows;
     otherwise state the snapshot date and that the solicitor verifies
     manually. Never state that a formality has been satisfied.
   - Name the responsible solicitor as confirmer of the final documents.
     Execution, witnessing and any filing happen entirely outside this
     workflow.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`,
`NOT READY` or `OUTSIDE SCOPE` — assessed per document type where they
differ.

```text
Matter: <client; document types sought; responsible solicitor>
Instruction record: <confirmed at extraction gate on <date>; fields with
  qualifications listed>
Documents: <per type: precedent used; filled/blocked; status>
Change manifest: <per document: marker sites filled; playbook positions
  adopted; reconciliation result>
Gap report: <unfilled markers; unused fields; clause choices awaiting the
  solicitor; flagged conflicts>
Execution formalities: <per document: requirements, statutory basis,
  evidence state; verification date or live re-verification>
Human decision gate: <responsible solicitor; confirmations outstanding;
  execution and witnessing outside this workflow>
Limitations: <drafts only; capacity, undue influence, family provision
  and tax not assessed; flag-only items listed>
```

## Fail closed

Return `NOT READY` for any document type whose precedent is missing, whose
required fields are unconfirmed or `cannot be determined` (listing exactly
what is missing), or whose change manifest cannot reconcile the output
against the precedent. Route self-represented parties, non-NSW matters and
every excluded subject `OUTSIDE SCOPE`. Never pick a clause alternative
the playbook does not cover, never fill a value the record does not
contain, never mark anything approved — a blocked document never blocks
the others.
