# Block Design and Data Flow

How to choose, order and connect the blocks of a Harvey Workflow agent in
Agent Builder, and how data moves between them. Labels follow the
[source policy](README.md#source-policy). Checked 25 August 2026.

## The block vocabulary

**Documented.** Harvey's own worked examples use five block kinds, described
in plain language: "Ask the user to upload", "Ask the user to describe",
"Use a prompt to", "Display ... to the user", and "Branch the workflow based
on".
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))
**Indexed.** Later release notes add a Review Table block ("Create and run
tailored review workflows directly within Workflow Builder", 4 March 2026),
Word file creation and editing (13 May 2026), PowerPoint and Excel creation
(17 June 2026), Deep Analysis (18 February 2026), web access (21 October
2025) and optional input steps (2 December 2025).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

This framework names them: **Input** (file upload or text), **Review Table**,
**Prompt**, **Branch**, **File creation** (Word, PowerPoint, Excel) and
**Response**. Confirm the labels in your workspace; the canvas names change.

## 1. Draw the path before you open the builder

**Documented.** Harvey's design criteria for a workflow are "Simple",
"General" and "Enduring"; "You can start simple and add complexity as
needed."
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))

Apply it: write the path as one line of block names with arrows, as the
per-skill guides in `docs/harvey/` do, and keep it in the build notes:

```text
Input -> Review Table -> Prompt -> File creation -> Response
```

If the line needs more than six blocks or a second Branch, it is two agents.

## 2. Every block has one named input and one named output

**Documented.** "Workflow Builder allows you to tag the contents of previous
input blocks in your prompts with an @-mention, directing Harvey to focus on
the right context at each step."
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))

Apply it: name each block's output in the build notes (`@instruction_sheet`,
`@source_table`, `@chronology`) and wire the next block to that name. A
Prompt block that is not @-mentioned by any later block is either the last
step or dead. Data that is not @-mentioned is not reliably in scope
([prompt principle 2](prompt-and-instruction-design.md#2-wire-context-with--mentions-not-prose-descriptions)).

## 3. Extract with a Review Table, reason with a Prompt

**Indexed.** Review Table cells carry "transparent reasoning, sentence-level
citations" (1 April 2026); verified cells can be preserved on re-runs
(6 January 2026) and locked (12 August 2026).
([Review Tables release notes](https://help.harvey.ai/release-notes/category/review-tables))
**Documented.** Review Table models are trained to "abstain from answering
when not applicable".
([Applied Compute blog](https://www.harvey.ai/blog/training-frontier-review-table-models-with-applied-compute))

Apply it: anything that must be traced to a passage in a source document is
a Review Table column, not a Prompt block instruction. The Prompt block that
follows consumes the table and does synthesis, ordering and drafting. This
split is why the evidence chronology guide puts extraction in a table and
event ordering in a prompt. A Prompt block reading raw files for facts is a
design smell; it loses cell-level provenance and the abstain behaviour.

**Inference.** Wire the Input block to the Review Table as its context, and
the Review Table to the Prompt, not the raw Input to the Prompt. Check the
number of Review Table blocks the workspace allows per workflow before
designing a second one; the existing evidence chronology guide assumes one.

## 4. Chain prompts; hide intermediate outputs

**Documented.** "Prompt chaining ... connect multiple prompt blocks ... The
output of the first block is passed internally to the second, so users only
see the final, polished result."
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))

Apply it: split at the seams of the method. Extract, classify, draft and
check are four Prompt blocks when the Review Table does not already cover
extraction. Each block gets one `### Task`
([prompt principle 5](prompt-and-instruction-design.md#5-one-question-per-sentence-one-job-per-block)).
Keep the intermediate outputs visible in the Response only while testing;
remove them before publishing.

## 5. Branch on a classified value, not on free text

**Documented.** Harvey's example branches on the user's answer about deal
leverage, with a separate Prompt block per branch.
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))
**Indexed.** Conditional columns let a column "reference responses in
existing columns as context" (15 April 2026).
([Review Tables release notes](https://help.harvey.ai/release-notes/category/review-tables))

Apply it: branch on a text Input with fixed options, or on a classification
column, never on a free-response Prompt output. Every branch ends in the same
Response block with the same status vocabulary. Use a Branch to route
jurisdiction only when the two paths share most of their blocks; the estate
planning guides keep NSW and Victoria as separate agents because they share
almost nothing.

## 6. Make an input optional only when embedded content is a valid substitute

**Indexed.** Optional Steps let users "skip inputs and use embedded content
automatically" (2 December 2025).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

Apply it: a required Input is the only mechanism that stops a run without
matter material. Keep the primary upload required. Make an Input optional
only for filters and labels (matter label, date range, issue focus), and
name the fallback in the Prompt (`If @date_range is empty, cover all dated
events`). See
[vaults principle 5](vaults-and-knowledge-sources.md#5-embed-the-vault-in-the-agent-let-uploads-be-optional).

## 7. Create the file in a File creation block, not in prose

**Indexed.** Custom agents can "create, populate, and update Word documents"
(13 May 2026) and create PowerPoint and Excel files (17 June 2026).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))
**Documented.** File creation returns "a citation-backed explanation for its
work".
([Create and edit files blog](https://www.harvey.ai/blog/create-and-edit-files-in-harvey))

Apply it: the deliverable is a file, so the File creation block is
mandatory whenever the skill's output is a document. The block takes the
final Prompt output (or the Review Table) as its @-mentioned input and an
embedded template where one exists. A plain-text response may summarise
status but never replaces the file; the Response returns both. Return
`NOT READY` if the file cannot be created.

## 8. Put the human checkpoint where the decision is, and state it

**Documented.** Agent Builder treats "human-in-the-loop checkpoints as a
core feature" and the agent "flags moments where pre-defined critical user
inputs would improve the results".
([Introducing Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder))
**Indexed.** Review Table cells can be verified and preserved on re-run
(6 January 2026) and locked (12 August 2026).
([Review Tables release notes](https://help.harvey.ai/release-notes/category/review-tables))

**Inference.** Public pages do not describe a general mid-run approval pause
inside a block agent. Design the checkpoint as a boundary between two runs:
run one produces the Review Table; a human verifies and locks cells; run two
consumes the verified table. Where a single run must do both, the Response
carries the status token and the human decides afterwards. Do not design a
block that waits for approval unless the workspace documents one.

## 9. Add Deep Analysis and web access only where the method needs them

**Indexed.** Deep Analysis in Custom Workflows (18 February 2026); Web in
Custom Workflows (21 October 2025).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

Apply it: a drafting or extraction agent runs on supplied documents and the
embedded Vault. Enable web access only for a research step that the skill
already defines as web-sourced, and say so in the Response so the reader
knows which findings came from outside the matter. Deep Analysis is for
open questions across many sources, not for a bounded extraction.

## 10. Let Harvey build the first draft; inspect every block before publishing

**Indexed.** Words to Workflows builds "the first draft" from a description
(24 July 2025); Magic Builder lets you "create, refine, and update block-based
workflow agents through natural conversation" (13 May 2026); Improve
Workflows Automatically has Harvey "analyze your workflow design and
recommend improvements" (28 January 2026).
([Agents release notes](https://help.harvey.ai/release-notes/category/agents))

Apply it: paste the path and prompts from the build notes into Magic
Builder, then check the generated canvas block by block against the
"Builder checks" list in the relevant `docs/harvey/` guide: right inputs
wired, Review Table fed from the upload, Prompt fed from the table, File
creation producing the right format, Response returning both. Accept an
automatic improvement only after re-running the test set.

## Reference paths

Extraction and chronology (from `build-evidence-chronology.md`):

```text
Input (files, optional labels) -> Review Table -> Prompt -> File creation (Word) -> Response
```

Precedent-based drafting (from the estate planning guides):

```text
Input (instruction sheet) -> Prompt using embedded Vault -> File creation (Word) -> Response
```

Triage with routing:

```text
Input (files, fixed-option question) -> Branch -> Prompt A | Prompt B -> Response
```

## Review

Before publishing, confirm: the path fits on one line; every block's output
is named and @-mentioned downstream; extraction is in a Review Table;
the primary upload is required; the deliverable is a File creation block;
the checkpoint is a run boundary, not an imagined pause; web and Deep
Analysis are off unless the method needs them. Record the path and the
Harvey pages relied on, with dates, in the build notes.
