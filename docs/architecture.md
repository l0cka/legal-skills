# Architecture

Legal Skills ships as one plugin, `legal-skills`, with one canonical
implementation and thin provider-specific distribution wrappers.

## Why one plugin

Every skill installs together. A user runs one install command and every
cross-area hand-off (contract review to the drafting checklist, a breach
assessment to the legislation verifiers) resolves in the session. Fourteen
separately installed plugins forced each skill to report a missing
dependency plugin and the generator to police declarations between them;
that machinery is gone.

The cost is a larger trigger surface: the agent sees all skill descriptions
at once, so each description must say when not to use the skill, and the
router (`route-legal-fact-pattern`) sequences multi-area matters. Revisit the
split if a consumer surface caps skills per plugin or if a practice area
needs a separate release cadence or licence.

## Portability model

```text
           canonical sources (hand-edited)
   plugins/legal-skills/.claude-plugin/plugin.json
   plugins/legal-skills/catalog.json   (presentation + practice areas)
   plugins/legal-skills/skills/        skills.json (provenance)
                         |
              scripts/generate_registry.py
                         |
   +-------------+-------+--------+--------------+---------------+
   |             |                |              |               |
 .codex-plugin/  marketplace.json marketplace.json README regions, router
  plugin.json   (.claude-plugin) (.agents/plugins) plugin README  skill-map.md
                      |                |           area table
                Claude Cowork     ChatGPT Work
```

The shared skill package is authoritative. Provider manifests describe the
same package using each provider's schema; they must not fork the legal
logic.

## Layout

```text
plugins/legal-skills/
├── .claude-plugin/plugin.json   canonical: name, version, description, keywords
├── .codex-plugin/plugin.json    generated
├── catalog.json                 canonical: presentation metadata and areas
├── README.md                    hand-written, with a generated area table
├── areas/<area>/README.md       practice-area guide
├── areas/<area>/CONTEXT.md      optional area vocabulary
├── references/                  shared method documents, schemas, registers
├── skills/<skill>/              skill packages
└── evals/<area>-<case>/         synthetic behavioural evals
```

## Vocabulary

Use these terms exactly in docs, scripts and reviews.

- **Practice area**: a named group of skills declared in `catalog.json`
  `areas`, with its own `lawCheckedOn` date, guide and optional method
  document. Every skill belongs to exactly one area. Areas replaced the
  former per-area plugins; an area id is the old plugin name without its
  `australian-` or `legal-` prefix.
- **Canonical source**: a hand-edited file that owns a fact.
  `.claude-plugin/plugin.json` owns name, version, description and keywords.
  `catalog.json` owns presentation metadata (`displayName`,
  `shortDescription`, `longDescription`, `defaultPrompt`, `whatItDoes`,
  `boundaries`) and the `areas` list. Each skill owns its package and its
  provenance sentence in `skills.json`.
- **Distribution surface**: a machine-owned file emitted by
  `scripts/generate_registry.py`: the `.codex-plugin/plugin.json` wrapper,
  both marketplace catalogs, the router's `skill-map.md`, and the generated
  regions of hand-written Markdown. Never hand-edited; CI fails when one is
  stale.
- **Provenance sentence**: the per-skill entry in `skills.json` recording
  where the workflow came from. Only a human can write it, so validation
  fails closed until every shipped skill has one, and rejects `TODO` or
  `TBD` placeholders.
- **Generated region**: a span of a hand-written Markdown file between
  `<!-- generated:x -->` and `<!-- end:x -->` markers that the generator
  owns: the root README badges, counts, area table and install blocks, the
  plugin README area table, and each method document's evidence-states
  block.
- **Method core**: the shared convention for `*-source-and-control-method.md`
  documents, recorded in
  [source-and-control-method-core.md](source-and-control-method-core.md).
  An area with a method document names it in `methodDocument` beside its
  `evidenceStates`; the two fields go together.

Area vocabularies live beside their areas and never redefine these terms,
for example [estate planning](../plugins/legal-skills/areas/estate-planning/CONTEXT.md)
and [evidence workflows](../plugins/legal-skills/areas/evidence-workflows/CONTEXT.md).

## Checks

- `generate_registry.py` loads and shape-checks the canonical sources: each
  skill in exactly one area, no area naming an unknown skill, method
  documents present. With `--check` (run in CI) it fails when any
  distribution surface is stale.
- `validate_repository.py` covers what generation cannot: skill
  frontmatter, relative links, `agents/openai.yaml`, area guides, provenance
  for exactly the shipped skills, and law-check currency. An area whose
  `lawCheckedOn` is more than 183 days old fails: re-verify the area against
  the official sources, fix anything stale, then set the date.
  Within 30 days of that limit it prints a warning (a GitHub annotation in
  CI) naming each area due, so the re-check happens before CI goes red.
- `tests/test_plugin_structure.py` pins each area's skill set, result
  vocabulary and method invariants, and checks that every `$skill-name` a
  document names exists. Each area's own test file holds its legal
  invariants; `tests/layout.py` gives tests the area's skills and evals.

## Provider boundaries

- Shared instructions, references, scripts, and redistributable assets belong
  inside the plugin.
- Provider-specific display metadata belongs in the matching plugin manifest.
- Provider-specific apps, connectors, hooks, and sub-agents must remain
  optional unless the workflow genuinely requires them.
- Credentials and authentication configuration remain with the user or
  workspace. They are never stored in this repository.

## Release model

The plugin version is written once, in `.claude-plugin/plugin.json`, and
propagated by the generator to the Codex wrapper and both catalogs. A release
bumps that one field, regenerates, passes offline validation, and is then
tested from each consumer surface.
