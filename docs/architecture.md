# Architecture

Legal Skills uses one canonical implementation with thin provider-specific
distribution wrappers.

## Portability model

```text
                        plugins/<name>/skills/
                                  |
                 shared SKILL.md, references and scripts
                                  |
                +-----------------+-----------------+
                |                                   |
    .claude-plugin/plugin.json          .codex-plugin/plugin.json
                |                                   |
 .claude-plugin/marketplace.json   .agents/plugins/marketplace.json
                |                                   |
          Claude Cowork                       ChatGPT Work
```

The shared skill package is authoritative. Provider manifests describe the
same package using each provider's schema; they must not fork the legal logic.

## Canonical registry

`skills.json` records each skill, owning plugin, plugin version, supported
targets, and source provenance. It exists to make drift detectable without
depending on either provider's installed cache.

## Provider boundaries

- Shared instructions, references, scripts, and redistributable assets belong
  inside the owning plugin.
- Provider-specific display metadata belongs in the matching plugin manifest.
- Provider-specific apps, connectors, hooks, and sub-agents must remain
  optional unless the workflow genuinely requires them.
- Credentials and authentication configuration remain with the user or
  workspace. They are never stored in this repository.

## Release model

A plugin version is identical across its two manifests and the Claude catalog.
A release changes the canonical plugin, updates both wrappers and catalogs,
passes offline validation, and is then tested from each consumer surface.

The empty initial marketplace is intentional. No plugin will be registered
until its purpose, scope, sources, and risk controls have been decided.
