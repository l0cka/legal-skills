---
name: assemble-vic-estate-documents
description: Assemble draft Victorian estate planning documents — a will, an enduring power of attorney and an appointment of medical treatment decision maker — from a provenance-cited instruction record and the firm's human-designed precedents. Register exact fill locations in a separate solicitor-confirmed precedent profile, halt for confirmation, then modify only those sites in a working copy. Return a change manifest, gap report and dated execution-formalities references. Use when a practitioner provides instructions and the firm's Victorian precedents are available. Do not use for self-represented parties, jurisdictions other than Victoria, advance care directives, supportive attorney appointments, superannuation death benefit nominations, trusts, probate or any document without a precedent — each fails closed to the responsible solicitor.
---

# Assemble Victorian Estate Documents

Turn a completed instruction sheet into filled working copies of the firm's
own human-designed precedents, with the responsible solicitor confirming every
step. Never compose a document, require machine markers or modify the source
precedent.

Read the
[source and control method](../../references/estate-planning-source-and-control-method.md)
first, and work from the
[Victorian instruction record schema](../../references/vic-instruction-record-schema.md),
the [precedent profile guide](../../references/precedent-profile-guide.md),
the [playbook usage rules](../../references/playbook-usage-rules.md) and
the [Victorian execution formalities reference](../../references/vic-execution-formalities.md).

## Workflow

1. Fix the matter and the inputs.
   - Confirm the practitioner is acting for a client in a Victorian matter
     and name the responsible solicitor who will confirm each gate. A
     self-represented party or a non-Victorian matter is `OUTSIDE SCOPE`.
   - Record which document types are sought — will, enduring power of
     attorney, appointment of medical treatment decision maker — and ask if
     unspecified. An advance care directive or supportive attorney
     appointment is a separate instrument and is `OUTSIDE SCOPE`.
   - Locate the firm's Victorian source precedent and any confirmed precedent
     profile for each sought document type. A document type with no precedent
     is `NOT READY` for that type: never substitute a generic document or
     statutory form.
2. Extract the instruction record.
   - From an uploaded completed instruction sheet: extract every schema field
     with its provenance (page, section or question). A blank, illegible or
     ambiguous field is `cannot be determined` with its location cited —
     never guessed. A free-form or handwritten sheet carries an
     `extraction-provenance` qualification, stated plainly.
   - Without a sheet: gather the same fields by asking the practitioner,
     recording provenance as `interview`.
   - Flag at this step: inconsistent names; a client who may be under 18;
     intended marriage, marriage, divorce or separation; any proposed
     attorney eligibility issue; any witness relationship; any existing
     enduring power of attorney; any advance care directive; and every other
     item listed as flag-only in the formalities reference. Do not decide
     capacity, eligibility, revocation or legal effect.
3. Halt at the extraction gate.
   - Present the extraction table — every field, value, provenance and
     evidence state — and stop. Nothing is drafted until the responsible
     solicitor confirms the table. A confirmed table stands; do not re-ask
     confirmed fields.
4. Register or verify the precedent profile, then fill a working copy.
   - First use, or any precedent drift: work from a read-only source and
     propose the precedent identity, site register, field map and
     clause-choice register under the precedent profile guide. Present the
     full profile and stop. Do not fill until the responsible solicitor
     confirms it; reuse only an unchanged confirmed profile thereafter.
   - Before every fill, match the source precedent and each registered site's
     structural location, exact surrounding text, target and expected
     occurrence count. A fingerprint mismatch, missing or duplicate anchor,
     changed target or ambiguous site is precedent drift: leave the document
     unchanged, report it and require a newly confirmed profile.
   - Make a working copy and fill confirmed sites only. Use confirmed values,
     identical values at separately registered repeated sites, and consistent
     names and roles across the document set. A connected playbook may
     identify a registered clause variant, but the responsible solicitor
     confirms its site, identifier and verbatim text before insertion. An
     unresolved clause site remains unchanged, goes to the gap report and
     makes that document `NOT READY`. Never modify the source precedent or
     alter text outside a registered site.
5. Report and hand over.
   - Return, for each document: the filled draft under a
     `DRAFT — SOLICITOR REVIEW REQUIRED` banner (banner outside the copyable
     document body), the change manifest reconciled against the precedent,
     and the gap report.
   - List the execution formalities for each document type from the
     formalities reference with their statutory basis and evidence state.
     Re-verify cited provisions against legislation.vic.gov.au (or via
     `$check-victoria-legislation` where available) when the platform allows;
     otherwise state the snapshot date and that the solicitor verifies
     manually. Never state that a formality has been satisfied. Never select
     physical or remote execution for the client.
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
Documents: <per type: Victorian source precedent and confirmed profile used;
  filled/blocked; status>
Change manifest: <per document: registered sites filled; exact before/after;
  source fields and confirmed clause variants; anchor and reconciliation result>
Gap report: <unfilled sites; unused fields; unresolved clause choices;
  drift findings; flagged conflicts>
Execution formalities: <per document: requirements, statutory basis,
  evidence state; verification date or live re-verification>
Human decision gate: <responsible solicitor; confirmations outstanding;
  execution and witnessing outside this workflow>
Limitations: <drafts only; capacity, undue influence, family provision
  and tax not assessed; flag-only items listed>
```

## Fail closed

Return `NOT READY` for any document type whose Victorian precedent or
confirmed profile is missing, whose profile no longer matches exactly, whose
required fields are unconfirmed or `cannot be determined` (listing exactly
what is missing), whose clause site is unresolved, or whose change manifest
cannot reconcile the working copy against the source precedent.
Route self-represented parties, non-Victorian matters and every excluded
subject `OUTSIDE SCOPE`. Never guess an anchor, silently update a profile,
insert a clause outside its confirmed site and register, fill a value the
record does not contain, or mark anything approved — a blocked document never
blocks the others.
