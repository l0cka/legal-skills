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
| [block-design-and-data-flow.md](block-design-and-data-flow.md) | Choosing and ordering blocks, @-mention wiring, Review Table vs Prompt, chaining, branching, optional inputs, file creation, checkpoints |
| [prompt-and-instruction-design.md](prompt-and-instruction-design.md) | Writing Prompt block text, Review Table column prompts and persistent table instructions |
| [vaults-and-knowledge-sources.md](vaults-and-knowledge-sources.md) | Vault scope, folder structure, file naming, limits, embedding, precedence, Regional Knowledge Sources, permissions |
| [harvey-agents-markdown-spec.md](harvey-agents-markdown-spec.md) | Agents authored as a single markdown spec instead of blocks; spec layout, skill-to-spec mapping, testing |
| [testing-and-governance.md](testing-and-governance.md) | Test sets, synthetic fixtures, deliverable verification, cell lock, roles, publication approval, build records, data scope, retirement |

Read them in table order when building a new agent; the files
cross-reference each other where one principle relies on another.

## Source policy

Every principle carries one of three labels:

- **Documented** - stated on a public Harvey page. The page is linked.
- **Indexed** - the feature appears in a public release-note index by title
  and one-line summary only; the full note requires a Harvey Support Hub
  login. Treat the summary as accurate and the detail as unverified.
- **Gated (paraphrased, date)** - reported by a builder who read a
  login-gated Harvey page, restated in their own words. No verbatim text from
  a gated page is reproduced here; check your firm's Harvey terms before
  quoting one.
- **Inference** - this repo's design judgement applied to documented
  behaviour. Test it in the target workspace before relying on it.

Do not promote an *indexed*, *gated* or *inference* claim to *documented*
without a public URL. If you hold a Harvey login, the gated article most likely to
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
- [Release notes: Vault](https://help.harvey.ai/release-notes/category/vault) (index only)
- [Release notes: Knowledge](https://help.harvey.ai/release-notes/category/knowledge) (index only)
- [Getting Started with Workflow Builder: 5 Workflows We Recommend](https://www.harvey.ai/blog/getting-started-with-workflow-builder-5-workflows-we-recommend)
- [Introducing Agent Builder](https://www.harvey.ai/blog/introducing-agent-builder)
- [Create and Edit Files in Harvey](https://www.harvey.ai/blog/create-and-edit-files-in-harvey)
- [Agent Builder, formerly Workflow Builder](https://www.harvey.ai/blog/introducing-workflow-builder)
- [Introducing Harvey II](https://www.harvey.ai/blog/introducing-harvey-ii)
- [Harvey Agents product page](https://www.harvey.ai/agents) and [launch press release, 5 May 2026](https://www.prnewswire.com/news-releases/built-by-lawyers-tailored-by-you-harvey-launches-purpose-built-legal-agents-across-every-major-practice-area-302762519.html)
- [Vault product page](https://www.harvey.ai/platform/vault), [file ingestion blog](https://www.harvey.ai/blog/building-new-file-ingestion-system-to-scale-firm-knowledge), [100+ Knowledge Sources blog](https://www.harvey.ai/blog/100-knowledge-sources-available-in-harvey)
