# Prompt and Instruction Design

How to write the text inside a Harvey Workflow agent: Prompt blocks, Review
Table column prompts and persistent table instructions. Labels follow the
[source policy](README.md#source-policy).

Harvey's own prompt guidance is written for Assistant. It transfers to Prompt
blocks because a Prompt block is an Assistant-style request with fixed context
wiring. Where the two differ, the principle says so.

## 1. Structure every prompt as Request, Context, Output

**Documented.** Harvey states that "a successful prompt includes three key
components": the request, the context, and the output. Its worked example
uses the headings `### Context`, `### Task`, `### Guidelines`, `### Checklist`
and `### Format`.
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))

Apply it:

1. Open with the task in one sentence, then the audience and tone
   ("Summarize for a senior in-house counsel"; "Draft in a neutral, formal
   tone"). **Documented** in
   [Getting Started](https://help.harvey.ai/articles/getting-started-with-harvey).
2. Name every input the block should use and what to use it for. In
   multi-source prompts "give Harvey clear instructions on how to use each
   one". **Documented.**
3. Close with the output shape. Name sections, columns and the status
   vocabulary. Do not name a page or word count: "Harvey cannot generate a
   specified number of pages"; use "brief", "detailed" or "in 10 bullet
   points". **Documented.**

## 2. Wire context with @-mentions, not prose descriptions

**Documented.** Workflow Builder lets you "tag the contents of previous input
blocks in your prompts with an @-mention, directing Harvey to focus on the
right context at each step".
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))

Apply it: refer to an uploaded file, text input or earlier Prompt block by its
@-mention every time the prompt relies on it. Do not write "the document the
user uploaded"; the agent has no other way to know which one.

**Inference.** When a Prompt block consumes a Review Table, @-mention the
table and say "use the table, not the raw files" so the block does not
re-extract from source.

## 3. Refer to sections and document names, never pages

**Documented.** "Harvey may not interpret documents and pages as you do.
Instead, refer to sections or document names." Pinpoint the clause where you
can ("pursuant to Section 8.3(d) of the agreement").
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))

Apply it to the *output* as well: when the agent must record where something
came from, ask for the document name and the section, clause or sentence, not
a page number. This is why the repo's per-skill guides ask for "supporting
passage and pinpoint" rather than page references.

## 4. Let Harvey cite; specify only what a citation must not be

**Documented.** "Avoid requesting citations explicitly ... Requesting specific
citation formats or asking for references unnecessarily may reduce output
quality."
([Getting Started](https://help.harvey.ai/articles/getting-started-with-harvey))
Citations may be omitted when many sources are referenced or a point is
"inferred as a general concept from the document".
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))

Apply it:

- Do not prescribe a citation format (AGLC4, Bluebook) inside the agent.
  Format citations downstream, by a human or a separate step.
- Do state the prohibition: "Do not invent a pinpoint. If no passage supports
  the value, enter `Not found`." That is a fallback rule (principle 6), not a
  citation request.
- **Indexed.** Review Table cells carry "sentence-level citations" and
  "transparent reasoning" (Review Table Cell Improvements, 1 April 2026,
  [Review Tables index](https://help.harvey.ai/release-notes/category/review-tables)).
  Rely on the table for provenance rather than asking a Prompt block to
  reproduce it.

## 5. One question per sentence; one job per block

**Documented.** "Ask one specific question per sentence for best results";
"Open-ended questions increase the risk of hallucinations".
([Getting Started](https://help.harvey.ai/articles/getting-started-with-harvey))
"Consider breaking up complex prompts ... Use follow-up questions instead of
multi-part prompts."
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))

In a workflow the follow-up question is the next Prompt block. Harvey
describes "prompt chaining": "The output of the first block is passed
internally to the second, so users only see the final, polished result".
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))

Apply it: a block that extracts, then classifies, then drafts is three blocks.
Split when a prompt needs a second `### Task` heading.

## 6. Give a fallback rule for every value that might be absent

**Documented.** Harvey's table guidance: "If a value is not found, enter N/A"
prevents "made-up content".
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))
Review Table models are trained to "abstain from answering when not
applicable".
([Applied Compute blog](https://www.harvey.ai/blog/training-frontier-review-table-models-with-applied-compute))

Apply it: every column and every required output field names its empty
value. Use one token across the agent (`Not found`, `Unclear`, `Not
applicable`) and define each once in the persistent instructions. Never let
"leave blank" be the rule; a blank cannot be distinguished from a skipped
cell.

## 7. Add structure only when the simple prompt fails

**Documented.** Harvey's table technique is an ordered escalation: establish
context, define the task, pre-specify rows, add fallback rules, add a
checklist, show a positive example, repeat critical rules. "Start simple, then
add more structure only if needed." And: "Don't overload prompts with too many
examples or rules at once. Conflicting instructions often cause poor quality
outputs."
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques))

**Documented.** Agent Builder agents "can now accomplish more with less
detailed instructions"; "Instead of writing exhaustive instructions to cover
every possible scenario, lawyers can shift their time towards setting the
objective."
([Introducing Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder))

Apply it: draft the objective and output shape first; run it; add a rule only
against an observed failure and keep the failing test. Before adding a rule,
check it does not contradict one already there.

## 8. Embed the precedent instead of describing the style

**Documented.** Grounding on a precedent lets Harvey "pick up on subtle
stylistic cues and preferences without requiring the builder or the end-user
to enumerate them".
([Workflow Builder blog](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend))
Teams "embed templates to provide additional context".
([Introducing Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder))

Apply it: embed the approved precedent or template and instruct "follow the
embedded precedent where the playbook is silent". Do not write paragraphs of
house-style rules that a precedent already shows. The per-skill estate
planning guides in `docs/harvey/` use this pattern with an embedded Vault.

## 9. Put run-wide rules in persistent table instructions, not in each column

**Indexed.** "Table Instructions for Review Tables" (27 May 2026): "add
persistent instructions to a review table that automatically apply to every
new column you generate."
([Review Tables index](https://help.harvey.ai/release-notes/category/review-tables))

Apply it: the persistent instructions hold the empty-value tokens (principle
6), the no-invention rule (principle 4), any controlled vocabulary (for
example evidence-character labels) and the statement that labels are
provenance, not findings. Column prompts then hold only what that column
extracts.

**Indexed.** Column prompts can be short ("change-of-control provisions");
column types are verbatim, free response and classification; a column can
carry a reference file as context; a column can reference an earlier column's
answers (Conditional Columns, 15 April 2026). Same index and
[Collaborative Review Tables blog](https://www.harvey.ai/blog/collaborative-review-tables).
Use classification columns for anything that must be a fixed value.

## 10. Do not ask Harvey to calculate or to diff

**Documented.** "Harvey does not perform calculations ... ask for the
components of the calculation first." "Assistant does not detect document
inconsistencies"; version comparison belongs to the Redline Workflow agent.
Harvey "does not have real-time internet access" by default.
([Getting Started](https://help.harvey.ai/articles/getting-started-with-harvey))

Apply it: deadline arithmetic, sums and date offsets are extracted as
components and computed outside the agent or by a human. This is consistent
with the repo's litigation-deadlines rule that arithmetic is script-only.
State any web access the agent relies on explicitly; the "Web in Custom
Workflows" feature is **indexed** only (21 October 2025,
[Agents index](https://help.harvey.ai/release-notes/category/agents)).

## 11. Bound the agent in the prompt, not only in the sharing settings

**Inference.** Every Prompt block that produces a deliverable ends with the
boundary the repo's skills already carry: what the agent must not do (assess
merits, send, file, disclose), what it must not claim (completeness beyond
supplied readable documents), and the status vocabulary it must return
(`READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`,
`OUTSIDE SCOPE`). Sharing and approval controls (**indexed**: "Updated
Workflow Builder Permissions", "Simplified Sharing in Agent Builder",
[Agents index](https://help.harvey.ai/release-notes/category/agents)) decide
who can run the agent; the prompt decides what a run may claim.

## Prompt block template

```text
### Task
<one sentence: verb, object, audience, tone>

### Context
Use @<input> for <purpose>. Use @<table> for <purpose>; do not re-extract
from the raw files.

### Guidelines
- Refer to documents by name and section; never by page number.
- If a value is not supported by a passage, enter `Not found`.
- <one rule per observed failure>

### Output
<sections or columns in order>. End with one of: READY FOR HUMAN REVIEW,
READY WITH QUALIFICATIONS, NOT READY, OUTSIDE SCOPE.
Do not assess merits, completeness beyond the supplied documents, or
admissibility. Do not send, file or disclose anything.
```

## Review

Before publishing, read each Prompt block against the eleven principles.
Any block that fails 1, 2, 5 or 6 is not ready; the others are judgement
calls to record in the build notes with the date and the Harvey page relied
on.
