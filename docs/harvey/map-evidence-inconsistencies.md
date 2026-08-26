# Harvey Agent Builder: Map Evidence Inconsistencies

This guide maps the provider-neutral `map-evidence-inconsistencies` skill to
a Harvey Workflow agent, on the same block pattern as
[Build Evidence Chronology](build-evidence-chronology.md), checked against
Harvey's public Review Tables in Custom Workflows documentation and Word-file
support on 24 August 2026. Confirm the current controls in your workspace
before publishing.

## Block design

Build this path:

```text
File Upload -> Review Table -> Prompt -> Word document creation -> Response
Text input (material facts) -----^
```

Upload the sources and, where one exists, the chronology and document index.
The text input carries the practitioner's list of material facts; without it
the Prompt block derives candidate facts from the chronology's conflict
register and labels them candidate. The Review Table records what each source
says about each fact; the Prompt block classifies divergences and records
corroboration; the Word step creates the `.docx`.

## Copy-paste build request

Paste this into Magic Builder, then inspect every generated block before
publishing:

```text
Create a Workflow agent named Map Evidence Inconsistencies.

Require a file upload containing the source documents and, optionally, the
chronology and document index. Add text inputs for matter label and the list
of material facts to map.

Create a fresh Review Table from the uploaded files. Treat each fact-source
pair as one row. Add columns for Fact ID, Source ID, Statement (quoted or
closely paraphrased), Pinpoint, Source Date, Evidence Character
(contemporaneous record | reported recollection | allegation | inference |
unclear), and Position (consistent | divergent | silent).

Use persistent table instructions requiring sentence-level source citations,
no paraphrase that removes or adds a divergence, silence recorded as silent,
and evidence character as a provenance label only.

Pass the completed Review Table to a Prompt block. Build the fact-by-source
matrix, a divergence register quoting each competing passage with pinpoints,
one or more classes (date or time, amount or quantity, sequence, participant,
wording or characterisation, omission, internal) and the question a reviewer
must resolve, and a corroboration register noting whether agreeing sources
are independent on their face or apparently derived. Record silences and
gaps. Never decide which account is correct, never describe a witness as
credible, unreliable, lying or mistaken, and never rank sources. Return READY
FOR HUMAN REVIEW, READY WITH QUALIFICATIONS, NOT READY or OUTSIDE SCOPE using
the canonical skill's rules.

After the Prompt block, add Harvey's Word document creation step and create a
new .docx file with a title and DRAFT - HUMAN REVIEW REQUIRED status, mapping
scope with the fact-list status and supplied-source limitation, the matrix in
a landscape section, the divergence register, the corroboration register,
silences and gaps, review record and limitations. Repeat table headings
across pages; keep quotations and pinpoints readable. Name the file
<matter-label>-inconsistency-map-<run-date>.docx.

In the Response block, return the Review Table and generated .docx file. Do
not express a view on credibility, reliability, weight, admissibility, legal
effect or merits, and do not make a finding about what happened. Return NOT
READY if a valid .docx cannot be created.
```

## Builder checks

1. Confirm the material-facts input reaches the Prompt block and that a run
   without it labels the derived facts candidate.
2. Upload two sources that differ on a date and confirm the divergence
   register quotes both passages with pinpoints and a reviewer question.
3. Upload a source silent on a fact and confirm it is recorded as silent, not
   divergent.
4. Ask the agent which witness is right and confirm it declines while still
   producing the map.

## Governance boundary

Use the workspace's normal builder, sharing and approval controls. The agent
must not send, file, publish or disclose the sources or the map. Human
reviewers decide what to test and what the evidence establishes.

Official product references:
[Review Tables in Custom Workflows](https://eu.help.harvey.ai/release-notes/review-tables-in-custom-workflows)
and [Agents release notes](https://eu.help.harvey.ai/release-notes/category/agents).
