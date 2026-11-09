---
name: check-court-ai-protocol
description: Check which Australian court or tribunal generative AI practice note applies to a document being filed, what it bans and what disclosure it needs. Use before filing affidavits, witness statements, expert reports or submissions prepared with AI help.
---

# Check Court AI Protocol

## Scope

Identify the court or tribunal instrument on generative AI that governs a
document a practitioner is preparing for an Australian proceeding, and
return what it prohibits, what statement or disclosure it requires and what
the practitioner must verify personally. Use before filing or serving an
affidavit, witness statement, character reference, expert report, written
submission, summary of argument or bundle that was prepared with any AI
tool, this assistant included. Do not use to certify that a document
complies, to decide whether AI use must be disclosed, to draft evidence, or
for professional conduct rules and regulator guidance, which are separate
from court instruments.

Work from the [protocol register](references/court-ai-protocol-register.json).
It is a dated snapshot. Each entry records whether the instrument itself was
read at the court's own website and on what date. These instruments changed
often in 2025 and 2026, and several adopt another court's practice note "as
amended", so the register is a lead and never the authority.

## Workflow

1. Fix the forum and the document.
   - Record the court or tribunal, the list or division if the instrument
     turns on it, the document type, who prepared it, and how any AI tool
     was used (drafting, summarising, translating, checking, formatting).
   - Record `cannot be determined` for a fact the user has not supplied.
     Ask one bounded question when the forum or document type is missing,
     because the answer changes the instrument.
2. Find the instrument.
   - Match the forum to the register. A forum with no entry is not a forum
     with no rule: search that court's own practice notes, practice
     directions and guidelines pages before saying none was found.
   - Check whether court rules also apply. In New South Wales, the Uniform
     Civil Procedure Rules were reported to be amended in 2025 on
     statements about AI in affidavits and witness statements. Verify the
     current rule with `$check-nsw-legislation` before relying on it.
3. Read the instrument at the court's own website.
   - Open the official source in the register, or the court's current
     practice note index if the link has moved. Record the title, number,
     issue date, commencement date and any amendment note as published.
   - Where one instrument adopts another, open the adopted instrument too.
   - If the instrument cannot be opened, report the register entry as an
     unverified lead and give the manual path. Never state a requirement
     from the register alone as current.
4. Extract the requirements for this document.
   - Prohibitions on generating the content of the document with AI.
   - Any statement the document must carry, where it goes, and any leave
     the practitioner must seek first.
   - Disclosure of AI use, whether mandatory or on the court's direction.
   - Verification duties for citations, authorities and quotations, and
     whether an AI tool may be used to do the verifying.
   - Limits on entering confidential, suppressed, subpoenaed or
     implied-undertaking material into an AI tool.
   - Quote the paragraph number for each requirement.
5. Compare with how the document was prepared.
   - Set each requirement beside the recorded AI use and mark it `met on
     the stated facts`, `not met on the stated facts` or `cannot be
     determined`. Route every cited authority to `$route-case-citation` and
     every quotation to `$verify-case-quote`.
6. Set the human decision gate.
   - Name the practitioner responsible for the document. They decide what
     is filed, what is disclosed and whether leave is sought.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Forum and document: <court or tribunal; list; document type; preparer>
AI use recorded: <tool; what it did; stated by whom>
Instrument: <title and number; issued; commenced; official URL opened; checked date>
Adopted instruments and rules: <instrument or rule; official URL opened; or none found>
Requirements: <paragraph; requirement; met / not met / cannot be determined on the stated facts>
Verification still to do: <authorities and quotations routed; by whom>
Human decision gate: <responsible practitioner; decisions required before filing>
Limitations: <register is a snapshot; sources not opened; no compliance certificate>
```

Use `READY FOR HUMAN REVIEW` when the instrument was opened at the court's
own website in this session and every requirement is assessed. Use `READY
WITH QUALIFICATIONS` when a requirement rests on the register because the
source could not be opened, or when no instrument was found for the forum
after searching. Use `NOT READY` when the forum or document type is unknown.
Use `OUTSIDE SCOPE` for non-Australian forums and for professional conduct
questions.

## Fail closed

Never say a document complies, is safe to file or needs no disclosure. Never
state a requirement as current from the register or from memory when the
instrument was not opened in this session. Never treat silence in the
register as permission. Never draft or rewrite the content of an affidavit,
witness statement or character reference, and never supply the wording of a
witness's evidence.
