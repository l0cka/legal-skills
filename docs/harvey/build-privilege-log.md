# Harvey Agent Builder: Build Privilege Log

This guide maps the provider-neutral `build-privilege-log` skill to a Harvey
Workflow agent, on the same block pattern as
[Build Evidence Chronology](build-evidence-chronology.md), checked against
Harvey's public Review Tables in Custom Workflows documentation and Word-file
support on 24 August 2026. Confirm the current controls in your workspace
before publishing.

## Block design

Build this path:

```text
File Upload -> Review Table -> Prompt -> Word document creation -> Response
Text inputs (framework, bases) --^
```

The text inputs carry the practitioner's instructed framework (the Evidence
Act provisions, court rules or principles) and the bases to consider. Without
them the Prompt block logs under descriptive bases only and flags the gap. The
Review Table records what each document shows on its face; the Prompt block
assembles the log, waiver-flag register and part-privilege candidates; the
Word step creates the `.docx`.

## Copy-paste build request

Paste this into Magic Builder, then inspect every generated block before
publishing:

```text
Create a Workflow agent named Build Privilege Log.

Require a file upload containing the documents under review. Add text inputs
for matter label, the production or disclosure obligation answered, the
instructed legal framework, and the bases to consider.

Create a fresh Review Table from the uploaded files. Treat each document or
coherent family (an email chain, an advice and its enclosures) as one source
row. Add columns for Source ID, Document Date, Document Type, Author and
Role, Recipients and Roles, Lawyer Involvement (on the face | stated by
practitioner | cannot be determined), Purpose or Subject on the Face,
Confidentiality Markings, Third-Party Circulation, Candidate Basis,
Supporting Facts and Pinpoints, Facts Against the Claim, Waiver Flags, and
Reviewer Status.

Use persistent table instructions requiring sentence-level source citations,
roles and purpose taken only from the document's face, every basis labelled
"candidate", and no inference that a copied lawyer was giving advice.

Pass the completed Review Table to a Prompt block. Assemble the privilege log
table, a waiver-flag register (circulation outside the client and its
advisers, forwarding, quotation, reference in a non-privileged document, each
with a question for the practitioner), part-privilege and redaction
candidates, and an unreadable-or-undetermined list. Never decide that a
document is privileged, not privileged or that privilege is waived, and never
state a conclusion on dominant purpose. Return READY FOR HUMAN REVIEW, READY
WITH QUALIFICATIONS, NOT READY or OUTSIDE SCOPE using the canonical skill's
rules.

After the Prompt block, add Harvey's Word document creation step and create a
new .docx file. If an approved privilege-log template or court-prescribed form
is embedded in the workflow, populate a working copy; otherwise use a clean
professional legal-review layout. The Word document must contain a title and
DRAFT - HUMAN REVIEW REQUIRED status, log scope with the instructed framework
and supplied-source limitation, the privilege log table with every basis
column labelled candidate, the waiver-flag register, part-privilege
candidates, unreadable items, review record and limitations. Use a landscape
section when needed; repeat table headings across pages. Name the file
<matter-label>-privilege-log-<run-date>.docx.

In the Response block, return the Review Table and generated .docx file. Do
not assert a claim to a court or regulator, decide waiver, or apply a
non-Australian privilege rule the practitioner has not supplied. Return NOT
READY if a valid .docx cannot be created.
```

## Builder checks

1. Confirm the framework and bases text inputs reach the Prompt block and
   that a run without them flags the gap rather than choosing a framework.
2. Upload an advice forwarded to an outsider and confirm a waiver flag with a
   practitioner question appears, and no waiver finding.
3. Upload a mixed family and confirm a part-privilege candidate lists the
   pages or passages.
4. Confirm every basis column in the `.docx` carries the word "candidate".

## Governance boundary

Use the workspace's normal builder, sharing and approval controls. The agent
must not produce, send, file or disclose any document or the log. The
practitioner decides every claim.

Official product references:
[Review Tables in Custom Workflows](https://eu.help.harvey.ai/release-notes/review-tables-in-custom-workflows)
and [Agents release notes](https://eu.help.harvey.ai/release-notes/category/agents).
