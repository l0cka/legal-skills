# Adding a plugin

## 1. Define the workflow

Record the plugin name, intended users, legal task, jurisdiction, authoritative
sources, expected output, known limitations, and required human review. Decide
whether any connector or write action is necessary.

## 2. Create the canonical package

```text
plugins/<plugin-name>/
├── .claude-plugin/plugin.json    # canonical: name, version, description, keywords
├── catalog.json                  # canonical: presentation metadata
├── .codex-plugin/plugin.json     # generated - do not edit
├── README.md
└── skills/
    └── <skill-name>/
        ├── SKILL.md
        ├── agents/openai.yaml    # required
        ├── references/           # optional
        ├── scripts/              # optional
        └── assets/               # optional
```

Names must use lowercase words separated by hyphens. Each `SKILL.md` needs
frontmatter whose `name` matches its directory and a non-empty `description`
of at most 1024 characters. The description is the trigger surface that agents
use to select the skill, so state what the skill does, when to use it, and
when not to.

Each skill also needs `agents/openai.yaml`, the ChatGPT Work interface file.
Without it the skill is invisible in ChatGPT Work. It has three required keys:

```yaml
interface:
  display_name: "Check NSW Legislation"
  short_description: "Verify NSW legislation at a date"
  default_prompt: "Use $check-nsw-legislation to verify this NSW law and identify the applicable version."
```

## 3. Write the canonical sources

Two hand-edited files describe the plugin; everything else is generated.

`.claude-plugin/plugin.json` carries the plugin's `name`, `version`,
`description`, and `keywords`. Author, homepage, repository, licence, and the
`./skills/` path are stamped by the generator.

`catalog.json` carries the presentation metadata used by the ChatGPT Work
interface and the root README table:

```json
{
  "displayName": "Australian AML/CTF",
  "shortDescription": "One line shown in listings.",
  "lawCheckedOn": "2026-08-26",
  "longDescription": "Full store prose.",
  "defaultPrompt": ["One suggested prompt per workflow."],
  "whatItDoes": ["README table bullet."],
  "boundaries": ["README table bullet."]
}
```

If the plugin ships a `references/<domain>-source-and-control-method.md`
document, also declare `evidenceStates` in `catalog.json` and follow
[docs/source-and-control-method-core.md](source-and-control-method-core.md) —
the evidence-states block is stamped by the generator.

If any file in the plugin names a skill from another plugin, declare that
plugin in `catalog.json` with a one-sentence reason:

```json
"requires": {"australian-legal-research": "Verifies the legislation the workflow relies on."},
"handsOffTo": {"australian-privacy-cybersecurity": "Takes privacy depth."}
```

Use `requires` when a skill invokes the other plugin's skills as a step of
its own workflow, such as official-source verification, and `handsOffTo` when
a skill routes part of a matter to the other plugin for depth. The generator
finds every cross-plugin skill name, fails when one is undeclared or a
declaration is unused, and appends an "Other plugins" section to each affected
`SKILL.md` and a "Plugin dependencies" section to the plugin README. Plugins
install separately, so those sections tell the agent to report a missing
plugin rather than perform its step from memory.

## 4. Generate the distribution surfaces

```bash
python3 scripts/generate_registry.py
```

This regenerates both marketplace catalogs, the `.codex-plugin/plugin.json`
wrapper, the root README badges, counts, plugin table and install blocks,
`plugins/README.md`, the router's skill map, and the dependency sections. Never edit those files by hand.

## 5. Record provenance

Add one sentence per new skill to `skills.json`, under the plugin's name,
recording where the workflow came from:

```json
"<plugin-name>": {
  "<skill-name>": "Original workflow based on the official ... sources."
}
```

Validation fails until every shipped skill has a provenance sentence and
`skills.json` names no skill that does not exist.

## 6. Validate

```bash
python3 scripts/validate_repository.py
python3 scripts/generate_registry.py --check
python3 -m unittest discover -s tests
git diff --check
```

Then test a clean installation in Claude Cowork and ChatGPT Work before
describing the plugin as released.
