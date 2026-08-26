# Harvey Agent Builder: Build Document Index

This guide maps the provider-neutral `build-document-index` skill to a Harvey
Workflow agent. It follows the same block pattern as
[Build Evidence Chronology](build-evidence-chronology.md), checked against
Harvey's public Review Tables in Custom Workflows documentation and Word-file
support on 24 August 2026. Confirm the current controls in your workspace
before publishing.

## Block design

Build this path:

```text
File Upload -> Review Table -> Prompt -> Word document creation -> Response
Optional text inputs -----------^
```

Use a fresh **Review Table** block for each run with the File Upload as its
context. Treat each uploaded document or coherent file group as one source
row. The Prompt block numbers and orders the rows, records duplicate, version
and attachment relationships, and lists unreadable items; the Word step
creates the index `.docx`.

## Copy-paste build request

Paste this into Magic Builder, then inspect every generated block before
publishing:

```text
Create a Workflow agent named Build Document Index.

Require a file upload containing the matter documents. Add optional text
inputs for matter label, bundle numbering scheme and ordering instruction.

Create a fresh Review Table from the uploaded files. Treat each document or
coherent file group as one source row. Add columns for Source ID, File Name,
Document Date as Recorded, Document Type, Author or Sender, Recipients or
Parties, Description (quoted or closely paraphrased from the document's own
title, heading, subject line or opening, with pinpoint), Page or Item Count,
Readability, Relationship (duplicate, version or attachment, by Source ID),
and Reviewer Status.

Use persistent table instructions requiring sentence-level source citations
for every description, exact date wording with undated documents recorded as
"undated", no inferred titles or dates, and no statement of what a document
proves.

Pass the completed Review Table to a Prompt block. Assign stable Source IDs in
the supplied order unless an ordering instruction was given; record any
supplied bundle numbering beside the Source ID and never renumber it. Build a
relationships table and an unreadable-or-missing list. Confirm every uploaded
file appears exactly once as a row or as a linked group member. Return READY
FOR HUMAN REVIEW, READY WITH QUALIFICATIONS, NOT READY or OUTSIDE SCOPE using
the canonical skill's rules.

After the Prompt block, add Harvey's Word document creation step and create a
new .docx file. If an approved index or court-book template is embedded in the
workflow, populate a working copy; otherwise use a clean professional
legal-review layout. The Word document must contain a title and DRAFT - HUMAN
REVIEW REQUIRED status, index scope and supplied-source limitation, the index
table, the relationships table, unreadable and missing items, review record
and limitations. Use a landscape section when needed; repeat table headings
across pages; do not shrink text to reduce page count. Name the file
<matter-label>-document-index-<run-date>.docx.

In the Response block, return the Review Table and generated .docx file. Do
not decide relevance, privilege, credibility, admissibility, weight or merits.
Do not omit any supplied file. Return NOT READY if a valid .docx cannot be
created.
```

## Builder checks

1. Confirm the Review Table receives the uploaded files as context and every
   description column requests a pinpoint.
2. Upload two identical files and confirm both appear as rows linked by a
   duplicate relationship.
3. Upload an undated file and confirm it is recorded as undated, not dated
   from metadata.
4. Confirm the Word step creates a new `.docx` and the Response returns both
   the Review Table and the file.

## Governance boundary

Use the workspace's normal builder, sharing and approval controls. The agent
must not send, file, publish or disclose the source documents or the index.
Human reviewers decide what the index may be used for.

Official product references:
[Review Tables in Custom Workflows](https://eu.help.harvey.ai/release-notes/review-tables-in-custom-workflows)
and [Agents release notes](https://eu.help.harvey.ai/release-notes/category/agents).
