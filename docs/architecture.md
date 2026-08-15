# Architecture

Legal Skills uses one canonical implementation with thin provider-specific
distribution wrappers.

## Portability model

```text
        canonical sources (hand-edited)
   plugins/<name>/.claude-plugin/plugin.json     plugins/<name>/catalog.json
   plugins/<name>/skills/                        skills.json `source` fields
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
registry sources; `scripts/generate_registry.py` emits every distribution
surface from them, so a plugin fact exists in exactly one place. Provider
manifests describe the same package using each provider's schema; they must
not fork the legal logic.

## Canonical registry

`skills.json` records each skill, owning plugin, plugin version, supported
targets, and source provenance. The generator derives every field except the
per-skill `source` sentence, which is hand-written provenance: a new skill is
scaffolded with an empty `source` and validation fails until a human records
where the workflow came from. CI runs `generate_registry.py --check`, so a
stale generated file fails the build instead of drifting.

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
wrapper, both catalogs, and the skill registry. A release bumps that one
field, regenerates, passes offline validation, and is then tested from each
consumer surface.

The legislation packages demonstrate the model with provider-neutral skills,
paired manifests and optional helpers for official-source navigation or
metadata retrieval.
