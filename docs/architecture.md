# Architecture

Legal Skills uses one canonical implementation with thin provider-specific
distribution wrappers.

## Portability model

```text
        canonical sources (hand-edited)
   plugins/<name>/.claude-plugin/plugin.json     plugins/<name>/catalog.json
   plugins/<name>/skills/                        skills.json (provenance)
                                  |
                    scripts/generate_registry.py
                                  |
        +----------------+--------+--------+----------------+
        |                |                 |                |
 .codex-plugin/   marketplace.json   marketplace.json   README table,
  plugin.json      (.claude-plugin)  (.agents/plugins)  badges, install
                        |                 |             blocks, plugins/
                  Claude Cowork      ChatGPT Work       README.md
```

The shared skill package is authoritative. Each plugin's
`.claude-plugin/plugin.json` and `catalog.json` are the only hand-edited
plugin sources; `scripts/generate_registry.py` emits every distribution
surface from them, so a plugin fact exists in exactly one place. Provider
manifests describe the same package using each provider's schema; they must
not fork the legal logic.

## Vocabulary

Use these terms exactly in docs, scripts and reviews.

- **Canonical source** — a hand-edited file that owns a fact. Per plugin:
  `.claude-plugin/plugin.json` (name, version, description, keywords) and
  `catalog.json` (presentation metadata, plus the optional `evidenceStates`
  qualification lists and the optional `requires` and `handsOffTo`
  dependency declarations). Per skill: the skill package itself and its
  provenance sentence in `skills.json`.
- **Distribution surface** — a machine-owned file emitted by
  `scripts/generate_registry.py`: the `.codex-plugin/plugin.json` wrapper,
  both marketplace catalogs, `plugins/README.md`, the router's
  `skill-map.md`, and the generated regions of hand-written Markdown. Never
  hand-edited; CI fails when one is stale.
- **Presentation metadata** — the editorial prose in `catalog.json`
  (`displayName`, `shortDescription`, `longDescription`, `defaultPrompt`,
  `whatItDoes`, `boundaries`), rendered into the ChatGPT Work interface and
  the root README table.
- **Provenance sentence** — the per-skill entry in `skills.json` recording
  where the workflow came from. Only a human can write it, so validation fails
  closed until every shipped skill has one.
- **Generated region** — a span of a hand-written Markdown file between
  `<!-- generated:x -->` and `<!-- end:x -->` markers that the generator
  owns: the README badges, counts, table and install blocks, each method
  document's evidence-states block, and the trailing `plugin-dependencies`
  section of a plugin README or `SKILL.md` that names another plugin's skills.
- **Plugin dependency** — a declared cross-plugin link in `catalog.json`:
  `requires` when a skill invokes another plugin's skills as a workflow step,
  `handsOffTo` when it routes part of a matter there for depth. Plugins
  install separately; the generator derives the links from the skill text and
  fails when the declarations drift. The router is exempt because it names
  every skill by design.
- **Method core** — the shared convention for `*-source-and-control-method.md`
  documents, recorded in
  [source-and-control-method-core.md](source-and-control-method-core.md).

Plugin-specific vocabularies live beside their plugins and never redefine
these terms:
[estate planning](../plugins/australian-estate-planning/CONTEXT.md) and
[evidence workflows](../plugins/legal-evidence-workflows/CONTEXT.md).

## Checks

- `generate_registry.py` loads and shape-checks the canonical plugin sources;
  with `--check` (run in CI) it fails when any distribution surface is stale.
- `validate_repository.py` covers what generation cannot: law-check currency,
  plugin READMEs, skill frontmatter, relative links, `agents/openai.yaml`, and
  a provenance sentence for exactly the shipped skills.
- `tests/test_plugin_structure.py` pins each plugin's skill set and result
  vocabulary; each plugin's own test file holds its legal invariants.

## Provider boundaries

- Shared instructions, references, scripts, and redistributable assets belong
  inside the owning plugin.
- Provider-specific display metadata belongs in the matching plugin manifest.
- Provider-specific apps, connectors, hooks, and sub-agents must remain
  optional unless the workflow genuinely requires them.
- Credentials and authentication configuration remain with the user or
  workspace. They are never stored in this repository.

## Release model

A plugin version is written once, in the plugin's
`.claude-plugin/plugin.json`, and propagated by the generator to the Codex
wrapper and both catalogs. A release bumps that one field, regenerates, passes
offline validation, and is then tested from each consumer surface.
