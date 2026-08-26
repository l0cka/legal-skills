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

## 4. Generate the distribution surfaces

```bash
python3 scripts/generate_registry.py
```

This regenerates both marketplace catalogs, the `.codex-plugin/plugin.json`
wrapper, the root README badges, counts, plugin table and install blocks,
`plugins/README.md`, and `skills.json`. Never edit those files by hand.

A new skill is scaffolded into `skills.json` with an empty `source`. Fill in
the provenance sentence — it is the one registry field only a human can write,
and validation fails until it is present.

## 5. Validate

```bash
python3 scripts/validate_repository.py
python3 scripts/generate_registry.py --check
python3 -m unittest discover -s tests
git diff --check
```

Then test a clean installation in Claude Cowork and ChatGPT Work before
describing the plugin as released.
