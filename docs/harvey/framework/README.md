# Harvey Agentic Framework

Design principles for building Workflow agents in Harvey Agent Builder
(formerly Workflow Builder). The framework is provider-specific guidance that
sits beside the provider-neutral skills in `plugins/`; the per-skill guides in
`docs/harvey/` apply it to one skill each.

Checked against Harvey's public documentation on 25 August 2026. Confirm the
current controls in your workspace before publishing an agent: product
capabilities, limits and permissions change.

## Principle sets

| File | Covers |
| --- | --- |
| [prompt-and-instruction-design.md](prompt-and-instruction-design.md) | Writing Prompt block text, Review Table column prompts and persistent table instructions |

Planned, not yet written: block design and data flow; mapping a repo skill to
a Harvey agent; testing and governance.

## Source policy

Every principle carries one of three labels:

- **Documented** - stated on a public Harvey page. The page is linked.
- **Indexed** - the feature appears in a public release-note index by title
  and one-line summary only; the full note requires a Harvey Support Hub
  login. Treat the summary as accurate and the detail as unverified.
- **Inference** - this repo's design judgement applied to documented
  behaviour. Test it in the target workspace before relying on it.

Do not promote an *indexed* or *inference* claim to *documented* without a
public URL. If you hold a Harvey login, the gated article most likely to
change these principles is
`https://help.harvey.ai/articles/workflow-builder`; record what it says in
the relevant principle file with the date read.

The US (`help.harvey.ai`) and EU (`eu.help.harvey.ai`) Help Centers carry the
same articles. Cite one host consistently; this framework cites the US host.

## Public sources used

- [Prompt Writing Techniques](https://help.harvey.ai/articles/prompt-writing-techniques)
- [Getting Started with Harvey](https://help.harvey.ai/articles/getting-started-with-harvey)
- [Release notes: Agents](https://help.harvey.ai/release-notes/category/agents) (index only)
- [Release notes: Review Tables](https://help.harvey.ai/release-notes/category/review-tables) (index only)
- [Getting Started with Workflow Builder: 5 Workflows We Recommend](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend)
- [Introducing Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder)
