# Domain vocabulary

Terms used by the repository's docs, scripts, and architecture reviews. Use
them exactly; do not coin synonyms.

- **Canonical source** — a hand-edited file that owns a fact. Per plugin:
  `.claude-plugin/plugin.json` (name, version, description, keywords) and
  `catalog.json` (presentation metadata). Per skill: the skill package itself
  and the `source` provenance sentence in `skills.json`. Every fact has
  exactly one canonical source.
- **Distribution surface** — a machine-owned file emitted by
  `scripts/generate_registry.py`: the `.codex-plugin/plugin.json` wrapper,
  both marketplace catalogs, `plugins/README.md`, the generated regions of
  `README.md`, and the derived fields of `skills.json`. Never hand-edited;
  CI fails when one is stale.
- **Presentation metadata** — the editorial prose in `catalog.json`
  (`displayName`, `shortDescription`, `longDescription`, `defaultPrompt`,
  `whatItDoes`, `boundaries`). Written by a human, rendered by the generator
  into the ChatGPT Work interface and the root README table.
- **Provenance sentence** — the per-skill `source` field in `skills.json`,
  the one registry fact only a human can write. New skills are scaffolded
  with an empty one and validation fails closed until it is filled.
- **Generated region** — a span of `README.md` between
  `<!-- generated:x -->` and `<!-- end:x -->` markers that the generator
  owns. Prose outside the markers is hand-written.
