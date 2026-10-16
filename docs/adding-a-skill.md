# Adding a skill

Every skill ships in the single `legal-skills` plugin. See
[architecture.md](architecture.md) for the layout and vocabulary.

## 1. Define the workflow

Record the skill name, intended users, legal task, jurisdiction,
authoritative sources, expected output, known limitations, and required human
review. Decide whether any connector or write action is necessary; neither
ships without documented permissions and approval boundaries. Pick the
practice area it belongs to, or define a new one (step 3).

## 2. Create the skill package

```text
plugins/legal-skills/skills/<skill-name>/
├── SKILL.md
├── agents/openai.yaml    # required
├── references/           # optional, skill-specific
├── scripts/              # optional
└── assets/               # optional
```

Shared material several skills use goes in `plugins/legal-skills/references/`
and is linked as `../../references/<file>.md`. Before adding a reference,
check that another area does not already own it; link the owner rather than
copying.

Names use lowercase words separated by hyphens and must be unique across the
plugin. Each `SKILL.md` needs frontmatter whose `name` matches its directory
and a non-empty `description` of at most 1024 characters. Every skill's
description is visible to the agent at once, so state what the skill does,
when to use it, and when not to, naming the neighbouring skill to use
instead. Name another skill in the text as `` `$skill-name` ``; a test fails
when the named skill does not exist.

Each skill also needs `agents/openai.yaml`, the ChatGPT Work interface file.
Without it the skill is invisible in ChatGPT Work. It has three required keys:

```yaml
interface:
  display_name: "Check NSW Legislation"
  short_description: "Verify NSW legislation at a date"
  default_prompt: "Use $check-nsw-legislation to verify this NSW law and identify the applicable version."
```

## 3. Register the skill in its practice area

Add the skill name to its area's `skills` list in
`plugins/legal-skills/catalog.json`. A new area needs an entry with `id`,
`displayName`, `shortDescription`, `lawCheckedOn` and `skills`, and a guide
at `plugins/legal-skills/areas/<id>/README.md` covering scope and sources,
reuse of other areas, permissions and validation.

If the area ships a `references/<domain>-source-and-control-method.md`
document, declare it on the area as `methodDocument` together with
`evidenceStates`, and follow
[source-and-control-method-core.md](source-and-control-method-core.md). The
evidence-states block is stamped by the generator.

Change the plugin-level presentation metadata in `catalog.json` or the
manifest keywords only when the new skill changes what the plugin offers.

## 4. Record provenance

Add one sentence for the skill to `skills.json` `sources`, recording where
the workflow came from:

```json
"<skill-name>": "Original workflow based on the official ... sources."
```

Only a human writes this sentence. Validation fails until every shipped
skill has one, rejects `TODO` or `TBD` placeholders, and fails when
`skills.json` names a skill that does not exist.

## 5. Add evals and tests

Add synthetic evals at `plugins/legal-skills/evals/<area>-<case>/` covering
the core deliverable and decisive missing-input or unsupported-approval
cases. Never use client or matter data. Add the skill to its area's entry in
`tests/test_plugin_structure.py`, and put legal invariants in the area's test
file (`tests/test_<area>.py`, using `tests/layout.py`).

## 6. Generate and validate

```bash
python3 scripts/generate_registry.py
python3 scripts/validate_repository.py
python3 scripts/generate_registry.py --check
python3 -m unittest discover -s tests
git diff --check
```

The generator rewrites both marketplace catalogs, the Codex wrapper, the
README badges, counts, area tables and install blocks, method-document
evidence states, and the router's skill map. Never edit those by hand.

Update `CHANGELOG.md` under **Unreleased**, then test a clean installation
in Claude Cowork and ChatGPT Work before describing the change as released.

## Structural and behavioural checks

`tests/test_plugin_structure.py` pins each area's exact skill set so
directory-derived generation cannot hide an accidental deletion. Its table
also records result vocabularies, required references and shared-method
invariants. `every_skill_mentions` lists text that must occur in every skill
in that area. `statuses: ()` skips the shared result-vocabulary check because
the area uses family-specific vocabularies checked in its own test file.

Every source-and-control method must carry the invariant sentences documented
in [source-and-control-method-core.md](source-and-control-method-core.md),
with whitespace normalised by the structural check. Fixture success
demonstrates the tested package contract; live model evals and client
installation checks are separate.
