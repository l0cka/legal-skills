# Harvey Agents: Markdown Spec Agents

How to write an agent as a single markdown specification file, where the
spec replaces the block canvas. Labels follow the
[source policy](README.md#source-policy). Checked 25 August 2026.

## What is verified and what is not

**Documented.** "Harvey Agents" is the product name for Harvey's agent
platform; Agent Builder is its authoring tool.
([Harvey Agents product page](https://www.harvey.ai/agents))
The 5 May 2026 launch put "500 agents and Agent Builder" into early access
and promised "greater flexibility in developing their own text-based agents".
([Press release, 5 May 2026](https://www.prnewswire.com/news-releases/built-by-lawyers-tailored-by-you-harvey-launches-purpose-built-legal-agents-across-every-major-practice-area-302762519.html))
Custom agents are tailored "in plain english by adjusting scope, refining
steps, and adding your organization's specific context, precedents, and
expertise".
([Agentic platform blog](https://www.harvey.ai/blog/agentic-platform-updates))

**Gated (paraphrased, 25 August 2026).** A builder with workspace access
reports that Harvey Agents can be built from a markdown spec file, and that
the file is the whole agent: instructions, inputs, knowledge sources and
outputs, with no block canvas. No public page confirms the file format,
required sections, frontmatter, size limits or how a spec agent is shared,
versioned or approved. Treat everything in this file below the next heading
as **Inference** until a workspace document is read and recorded here with
its title and date.

The block-based path remains fully supported ("existing workflows remain
fully supported with no changes",
[Introducing Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder)),
so nothing in the other principle sets is superseded.

## 1. The spec is a prompt; every prompt principle applies

The spec body is read by the same model that reads a Prompt block. Apply all
eleven principles in
[prompt-and-instruction-design.md](prompt-and-instruction-design.md)
directly: Request, Context, Output structure; sections not pages; no
citation-format demands; fallback tokens; add structure only after a failure;
embed the precedent rather than describe it; state the boundary and status
vocabulary in the spec itself.

## 2. One spec, one deliverable, one jurisdiction

A block agent enforces one job per block. A spec has no such seam, so the
author must draw it. A spec describes one deliverable for one jurisdiction.
When the method has distinct extract, classify and draft stages, the spec
lists them as numbered steps with the output of each named, so the agent can
be tested stage by stage. If a second deliverable appears, write a second
spec.

## 3. Structure the file the way Harvey structures a prompt

Until Harvey publishes a schema, use the headings Harvey's own example prompt
uses, in this order, so a reader can map the spec to a block design if the
agent is ever rebuilt:

```markdown
# <Agent name>

## Purpose
One sentence: verb, object, audience, tone. Jurisdiction named.

## Inputs
- Required: <file upload or text input>, what it must contain.
- Optional: <input>, and what the agent uses instead when it is absent.

## Knowledge sources
- Vault: <exact Vault name>; files selected by exact name.
- Regional knowledge sources: <bundle>, or "none".
- Precedence: Vault over upload; state it (vaults principle 6).

## Method
1. <step> -> <named intermediate output>
2. ...

## Guidelines
- Refer to documents by name and section, never page.
- If a value is unsupported, enter `Not found`.
- <one rule per observed failure>

## Output
<deliverable shape>. End with READY FOR HUMAN REVIEW, READY WITH
QUALIFICATIONS, NOT READY or OUTSIDE SCOPE.

## Boundary
Must not assess merits, claim completeness beyond supplied documents, or
send, file or disclose anything. Human review required.
```

Keep it under what a reviewer can read in one sitting. Harvey warns that
overloaded prompts with conflicting rules degrade output
([Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques));
a long spec is the same failure in one file.

## 4. Keep the spec in version control, but never in this repository

A markdown spec is text, so it can be diffed, reviewed and rolled back like
code. Hold each firm's specs in a private repository with the same review
gate the workspace applies to publishing. Do not commit a working spec to
this public repository: it names Vaults, file names and playbooks that are
firm property, and it may reproduce gated Harvey documentation. This
repository holds only the provider-neutral skill and this framework.

## 5. Map from the repo skill, do not copy it

A `SKILL.md` in `plugins/` is written for an agent that has tools, scripts
and a file system. A Harvey spec agent has documents, Vaults, knowledge
sources and Harvey's own file creation. When converting:

- Keep: the method steps, output schema, status vocabulary, boundary
  statements, controlled vocabularies and human-review requirements.
- Drop: script invocations, file-path references, tool names and any step
  that computes (Harvey "does not perform calculations",
  [Getting Started](https://help.harvey.ai/articles/getting-started-with-harvey)).
- Replace: "read references/x.md" with an embedded Vault file named exactly;
  "return JSON" with a Review Table or a Word deliverable.

Record the mapping in the spec's build notes so a change to the skill can be
traced into the spec.

## 6. Test a spec agent the way you would test blocks

There is no block boundary to inspect, so the tests carry the whole burden.
Before seeking approval, run the agent against: a complete input, an input
with a required field missing, an upload that imitates a Vault precedent, a
document with an ambiguous date or clause, and an unreadable file. Confirm
each returns the right status token and no invented pinpoint. Keep the test
set with the spec and re-run it after every edit.

## Review

Record in the build notes the spec file name and version, the workspace
article or release note that documents the spec format (title and date
read), the Vault and file names, the sharing level, and the test set. When
the format is documented publicly, replace the Gated label above with
Documented and link the page.
