# Harvey Agent Builder: Build Evidence Chronology

This guide maps the provider-neutral `build-evidence-chronology` skill to a
Harvey Workflow agent. It was checked against Harvey's public Review Tables in
Custom Workflows documentation and Word-file support for custom agents on
24 August 2026. Confirm the current controls in your workspace before publishing
because product capabilities and permissions can change.

## Block design

Build this path:

```text
File Upload -> Review Table -> Prompt -> Word document creation -> Response
Optional text inputs -----------^
```

Use a fresh **Review Table** block for each run. Connect the File Upload block
as its context. Treat each uploaded document or coherent file group as a source
row; the downstream Prompt block converts source-level extractions into the
event-level chronology. Pass that chronology to Harvey's Word document creation
step and attach both the Review Table and generated `.docx` to the Response
block.

The public documentation currently permits one Review Table or Table Selection
block per workflow. Do not design this workflow around multiple tables unless
the workspace now supports them.

## Copy-paste build request

Paste this into Magic Builder, then inspect every generated block before
publishing:

```text
Create a Workflow agent named Build Evidence Chronology.

Require a file upload containing the evidence documents. Add optional text
inputs for matter label, date range and issue focus.

Create a fresh Review Table from the uploaded files. Treat each document or
coherent file group as one source row. Add columns for Source ID, Document
Date, Document Type, Author or Sender, Recipients or Participants, Event
Candidates, Exact Date Wording, Supporting Passage and Pinpoint, Evidence
Character, Contradiction or Uncertainty, and Reviewer Status.

Use persistent table instructions requiring sentence-level source citations,
exact date wording, no invented pinpoints, and these evidence-character values:
contemporaneous record, reported recollection, allegation, inference, or
unclear. State that these are provenance labels, not findings about truth,
weight or admissibility.

Pass the completed Review Table to a Prompt block. In that block, create an
event-level chronology with columns for Event ID, Recorded Date and Time,
Normalised Date and Time, Event, People or Entities, Source IDs and Pinpoints,
Evidence Character, Conflict ID, and Notes or Gaps. Keep conflicting accounts
as separate rows linked by a Conflict ID. Do not infer missing events or order
same-day events without source support.

Also produce a source register, conflict register, evidence-gap list and
supplied-source limitation. Return READY FOR HUMAN REVIEW, READY WITH
QUALIFICATIONS, NOT READY or OUTSIDE SCOPE using the canonical skill's rules.

After the Prompt block, add Harvey's Word document creation step and create a
new .docx file. If an approved chronology template is embedded in the workflow,
populate a working copy of that template; otherwise use a clean professional
legal-review layout. The Word document must contain a title and DRAFT - HUMAN
REVIEW REQUIRED status, review scope and supplied-source limitation, a
source-linked chronology table, conflict register, evidence gaps, source
register, review record and limitations.

Use a landscape chronology section when needed. Repeat table headings across
pages, allow rows to expand, keep source pinpoints readable and do not shrink
text merely to reduce the page count. Name the file
<matter-label>-evidence-chronology-<run-date>.docx, using a safe generic matter
label when none is supplied.

In the Response block, return the Review Table and generated .docx file. A
plain-text response may summarise status and limitations but must not replace
the Word deliverable. Do not assess credibility, evidentiary weight,
admissibility, legal effect or merits. Do not claim completeness beyond the
supplied and readable documents. Return NOT READY if a valid .docx cannot be
created.
```

## Builder checks

1. Confirm the Review Table receives the uploaded files as context.
2. Confirm every extraction column requests a source citation or pinpoint.
3. Confirm the Prompt block uses the Review Table, not the raw files alone.
4. Confirm the Word step receives the event-level chronology and creates a new
   `.docx` rather than plain text, PDF or spreadsheet output.
5. Confirm the Response returns both the Review Table and generated `.docx`;
   then open the file and test a conflicting account, an ambiguous date and an
   unreadable attachment before seeking workspace approval.

## Governance boundary

Use the workspace's normal builder, sharing and approval controls. The agent
must not send, file, publish or disclose the source documents or chronology.
Human reviewers decide whether extracted events are accurate and whether the
output may be used in a matter.

Official product references:
[Review Tables in Custom Workflows](https://eu.help.harvey.ai/release-notes/review-tables-in-custom-workflows)
and [Agents release notes](https://eu.help.harvey.ai/release-notes/category/agents).
