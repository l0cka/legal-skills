# Portability: AI tools that run no code

How Legal Skills reaches AI tools that cannot run code, such as Harvey and
Legora. The plugin needs a host that loads skills and may run small helper
programs. The AI-tool bundle is the same content as a folder of Markdown and
data files with the code removed.

## What the bundle is

`scripts/build-ai-tool-bundle.sh` builds `dist/legal-skills-ai-<version>.zip`
from the plugin. The zip has one top-level folder, `legal-skills/`:

| Path | Content |
| --- | --- |
| `ROUTER.md` | Entry point: which skill for which task, by practice area |
| `skills/<name>/SKILL.md`, `references/`, `assets/` | Every skill and its linked material |
| `references/` | Shared source methods, schemas, rule tables, holiday data and `ai-tool-mode.md` |
| `reference/firm/README.md` | Empty slot for firm material; nothing firm-specific ships |
| `catalog.json`, `PRIVACY.md`, `LICENSE`, `VERSION` | Metadata |

Options: `--area <id>` builds one practice-area zip (`legal-skills-ai-<id>-<version>.zip`),
`--all-areas` builds the full zip and every area zip. The version defaults to
the plugin version. A rebuild of the same tree on the same machine and toolchain is
byte-identical; a different zlib version can change the compressed bytes.

The bundle leaves out `evals/`, `benchmarks/`, `tests/`, plugin manifests,
agent interface files and every `scripts/` folder. The build fails if a bundled
Markdown file mentions a script, a Python file or an excluded path, if a
relative link does not resolve inside the bundle, if a code-only marker is
left behind, or if a script-backed skill has no AI-tool section. In an area
zip, a link into a skill of another area is turned into plain text, so no
link points outside the zip, and `ROUTER.md` omits the cross-area entry
skills.

## What travels, and what does not

Travels: every workflow instruction, result contract and human-review gate,
the official-source methods, the profile schemas and starter profiles, the
computation-rule and holiday tables as reading material, and the profile
templates.

Does not travel: deterministic date computation, the Federal Register helper
calls, the NSW URL helper, the citation parser, the APP inventory comparison
and the triage profile validator. Evals and benchmarks stay in the
repository.

## Identify-only behaviour

Seven skills ship code in the plugin, `map-tribunal-review-deadlines` uses the
deadline code, and `verify-deadline-basis` needs a code-computed fingerprint.
In the bundle each of the nine has an `## AI-tool mode` section:

| Skill | In the bundle |
| --- | --- |
| `compute-procedural-deadlines`, `map-tribunal-review-deadlines` | Identify-only: the rule, its source, the inputs a person needs and `not computed`. No date is ever stated |
| `check-commonwealth-legislation`, `check-nsw-legislation`, `trace-commonwealth-legislative-change` | The official source and search steps for a person or a browsing tool; `NOT VERIFIED` when nothing was opened |
| `check-australian-privacy-principles` | The manual layer-by-layer comparison, reported as manual; no hash is computed |
| `verify-deadline-basis` | The fingerprint is `not computed`; a person with code computes it before an update is applied |
| `route-case-citation` | Manual parse with the same routing table |
| `configure-legal-triage` | Manual check against the schema; the profile is never reported as validated or approved |

The shared rules are in `references/ai-tool-mode.md`. The JSON rule tables
carry descriptive notes that mention the computation step; they are data and
are read as the rule's provenance. The build scans them only for code file names and paths, not for the word "script".

## How the source marks it

Keep Claude Code behaviour unchanged by editing one `SKILL.md`:

- Wrap code-only passages in `<!-- ai-tool:code -->` ... `<!-- /ai-tool:code -->`.
  The bundle drops them. They are invisible comments in the plugin.
- Write the replacement as a visible `## AI-tool mode` section at the end of
  the skill. In the plugin it is marked as ignorable by hosts that can run code.
- `<!-- ai-tool:bundle: ... -->` carries bundle-only wording for a passage the
  bundle replaces. Claude Code reads the raw file, so it sees that text beside
  the original wording; the original gates and commands are intact.
- Elsewhere, word prose neutrally ("the deterministic computation step").

The validator and `tests/test_ai_tool_bundle.py` fail when a skill with a
`scripts/` folder lacks the section or the markers. They also fail when any skill marks code-only
passages without the section, which covers skills that need code steps but ship
no `scripts/` folder, such as `verify-deadline-basis`.

## Research: how Harvey and Legora take custom material

Searched 2026-11-11 using public sources only, with no matter or client data
in any query.

### Harvey: unverified from public sources

All five `help.harvey.ai` pages below redirect to a Harvey login (HTTP 307 to
authentication), so none could be read publicly. Every Harvey figure here
comes from search-result summaries and is unverified. Confirm each one in a
Harvey tenant before relying on it. The URLs are kept for that check.

- **Vault limits (unverified).** Reported as 100,000 files and 100 GB per
  project, and 500 MB per file since a February 2026 release.
  [Vault project limits](https://help.harvey.ai/release-notes/increased-vault-project-limits),
  [upload limits](https://help.harvey.ai/release-notes/increased-file-upload-limits),
  [Uploading files to Harvey](https://help.harvey.ai/articles/uploading-files-to-harvey).
- **File types (unverified).** Markdown (`.md`) reported as added in a January
  2026 release.
  [Support for new file types](https://help.harvey.ai/release-notes/support-for-new-file-types).
  No source found documents zip upload: unzip first.
- **Other caps (unverified).** A per-thread Assistant upload cap (reported as
  50 files) and, for the API, at most 50 files per request:
  [upload files to project](https://developers.harvey.ai/api-reference/vault/upload-files-to-project).
  The API page was not re-read for this check.
- **Workflow Builder import (unverified).** Reported: workflows are built from
  a prompt or custom instructions and edited in steps; knowledge sources can be
  attached or embedded, with up to 50 embedded documents per workflow agent.
  [Workflow Builder](https://help.harvey.ai/articles/workflow-builder),
  [Workflows release notes](https://help.harvey.ai/release-notes/category/workflows).
- **Not found.** No documented bulk import of instruction folders or of the
  Agent Skills format.

### Legora: read 2026-11-11

- **Skills are Markdown.** [Introducing Skills](https://legora.com/blog/introducing-skills)
  (published 5 Oct 2026) says: "A Skill is a set of natural language
  instructions, saved as a Markdown file, that teaches the Agent how to
  approach a specific legal task." It says a Skill "can hold reference
  materials, templates and past examples" and that you can "read, edit, export
  and update any Skill".
- **Library.** [Artificial Lawyer, 7 Oct 2026](https://artificiallawyer.com/2026/10/07/legora-launches-250-skills-for-legal-agents)
  repeats the Markdown description and reports a library of 250+ Skills.
- **Playbooks and Workflows.** [Playbooks](https://legora.com/product/playbooks)
  and [Workflows](https://legora.com/product/workflows) say nothing about
  importing files.
- **Import is unconfirmed.** No public source read says how a custom Skill is
  imported (single file or zip), nor gives a size or file-count limit, nor says
  whether a Skill may link to other files. `support.legora.com/index.md` is the
  address a search returned; it looks like a documentation index and was not
  read for this check.

### Can one zip serve both?

Partly. Legora Skills are Markdown, which suits the bundle's content. Harvey's
accepted formats and limits are unverified. Legora's import of custom Skills is
unconfirmed publicly, so no Legora-specific export is built. A Legora export
needs, once documented: the Skill import format and name rules, size and
file-count limits, and whether a Skill can reference sibling files. If it
cannot, the export would inline each skill's references into one Markdown file
per skill. Build that only when those answers exist.

## Install

Nothing below was tested against a live tenant.

### Harvey

1. Download the release zip and unzip it.
2. Create a Vault project and upload the `legal-skills` folder's files,
   keeping the folder layout if the Vault allows it. The full bundle is about
   216 files and 0.5 MB zipped, far below the reported (unverified) Vault limits.
3. Attach the project as a knowledge source in Assistant, or embed
   `ROUTER.md` and the skills you want in a custom workflow. A workflow
   embedded-document cap (reported as 50) is smaller than the full bundle, so
   use an area zip and a subset.
4. Ask the assistant: "Follow ROUTER.md for this task."

### Legora

1. Unzip the release and read `ROUTER.md`.
2. Add the files to the workspace knowledge store, or paste a single
   `SKILL.md` as a Skill, following Legora's current help pages for the
   import step (not found in public sources).
3. Ask the Agent to follow `ROUTER.md`.

### Firm context

After upload, a firm adds its own profile, house style and precedents in the
tool's store, following `reference/firm/README.md`. Keep client and matter
material out of the bundle. The repository is public and MIT licensed.

## Release

The draft-release workflow runs on a push to `main` once `CHANGELOG.md` has a
dated section for the plugin version, and on a `v*` tag. It builds the full
zip and every area zip first, then creates the draft with them attached, so a
failed build leaves no draft without zips. Nothing is published automatically.
