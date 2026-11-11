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
| `skills/<name>/no-code.md` | The no-code replacement for each skill that needs code |
| `references/` | Shared source methods, schemas, rule tables, holiday data and `ai-tool-mode.md` |
| `references/deadline-calculator.xlsx` | Deadline calculator workbook, generated at build time |
| `reference/firm/README.md` | Empty slot for firm material; nothing firm-specific ships |
| `catalog.json`, `PRIVACY.md`, `LICENSE`, `VERSION` | Metadata |

Building needs openpyxl (`requirements-build.txt`). Options: `--area <id>` builds one practice-area zip (`legal-skills-ai-<id>-<version>.zip`),
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
skills. The build also fails if a skill with an `AI-tool mode` section has no
`no-code.md`, or its section does not link it.

## What travels, and what does not

Travels: every workflow instruction, result contract and human-review gate,
the official-source methods, the profile schemas and starter profiles, the
computation-rule and holiday tables, the profile templates, and the
candidate-date computation as a spreadsheet a person fills.

Does not travel: the Federal Register helper calls, the NSW URL helper, the
citation parser, the APP inventory comparison, the triage profile validator
and every hash or fingerprint. Their no-code procedures give the manual
steps. Evals and benchmarks stay in the repository.

## No-code replacements

Seven skills ship code in the plugin, `map-tribunal-review-deadlines` uses the
deadline code, and `verify-deadline-basis` needs a code-computed fingerprint.
In the bundle each of the nine has an `## AI-tool mode` section and a
`no-code.md` procedure beside its `SKILL.md`. A procedure is a spreadsheet
where a calculation is needed, and a checklist or record table where
judgement or a manual lookup is enough. Where neither can do the job
honestly, the procedure says so and keeps `not computed` or `NOT VERIFIED`.

| Skill | Replacement | What stays out |
| --- | --- | --- |
| `compute-procedural-deadlines` | Deadline calculator workbook and the steps to fill and read it | The model never states a date; a person reads it |
| `map-tribunal-review-deadlines` | The same workbook for the ART, NCAT and QCAT general periods; conferring-Act periods and VCAT stay identify-only | Expiry or extension conclusions |
| `verify-deadline-basis` | Field-by-field change table | The table fingerprint: `not computed` |
| `check-commonwealth-legislation`, `check-nsw-legislation` | Official-source steps and a record table filled only from pages opened | Live status without browsing: `NOT VERIFIED` |
| `trace-commonwealth-legislative-change` | Compilation-by-compilation comparison table | Live compilations without browsing: `NOT VERIFIED` |
| `check-australian-privacy-principles` | Layer-by-layer comparison table | Every digest: `hash not computed` |
| `route-case-citation` | Manual parse worksheet and the skill's routing table | Proof the decision exists |
| `configure-legal-triage` | Checklist of the validator's field, control and date checks, including review dates against today's date | `VALIDATED APPROVED PROFILE` |

## Deadline calculator workbook

`scripts/ai_tool_workbooks.py` generates `references/deadline-calculator.xlsx`
with openpyxl at build time from the computation-rule and holiday tables of
the same tree. It is not committed: the generator is the reviewable source.
Workbook metadata and zip entry times are fixed, so the bundle stays
byte-identical across rebuilds.

Sheets: Calculator (yellow inputs and the result), Rules (one row per period
rule, with provision evidence and excluded ranges resolved), HolidayTables
and Holidays (one column per registry, plus a `custom` column a person fills
and marks verified), Windows (uncertain holiday windows), Scope (what the
workbook does not cover), and Engine and Working (the formulas, open for
review).

Safeguards in the sheet itself:

- No date shows unless the profile is marked approved, the profile, confirmer
  and diary system are named, the trigger event and date are entered, the
  date is not contested and the matter type is a civil step fixed by a rule.
  Otherwise the status is `NOT READY` or `OUTSIDE SCOPE`.
- Every refusal of the deterministic computation is reproduced, in the same
  order: unverified rule, provision or holiday table, unsupported unit or
  rollover, excluded ranges on months or years, short calendar-day periods
  that count only business days, a missing registry table for federal courts
  and the ART, dates outside coverage or in an uncertain window, and a
  rollover into an excluded range. The status is then
  `IDENTIFY-ONLY - NOT COMPUTED` with the reason.
- A computed result is labelled `CANDIDATE DATE - NOT BINDING UNTIL CONFIRMED`
  and carries the human decision gate.
- The custom holiday table computes only when its row is marked `verified`
  (exact lower case) and names its source and the person who verified it.
- The Engine and Working sheets carry a note that their dates are working
  values with no gate applied. Every sheet is protected without a password
  against accidental edits; only the Calculator inputs, the custom holiday
  column, the custom HolidayTables row and the blank Windows rows are
  unlocked. Protection is not a security control.
- Known limits: the custom column takes 100 dates and the Windows sheet 40
  added windows, and rows typed below them are ignored. `TEXT` date formats
  in reason and day text follow the spreadsheet's locale; the dates do not.

The formulas scan day by day (WEEKDAY, COUNTIF, MATCH, EDATE) rather than
using WORKDAY.INTL. The scan follows the deterministic computation's walk
exactly, a reviewer can read it row by row, and it does not depend on how a
spreadsheet treats a non-business start day in WORKDAY.INTL. Trade-off: the
count scan covers 120 days after the trigger and a rollover 15 days; longer
periods are refused. Raise those limits in the generator if a rule needs
them.

`tests/test_deadline_workbook.py` proves the formulas. It evaluates the
generated workbook with the formulas package against every case of the
deadline engine's own tests (hand-derived fixtures, refusals, excluded-range
cases, unverified tables and every 2026 NSW holiday), against every shipped
rule for several triggers and registries, and against the gates and the
custom holiday column, and edge refusals (unsupported rollover, a zero or
fractional length, a missing provision, missing evidence and an uncertain
window met during rollover, and a business-day count that ends on the first
weekday past coverage or inside a window). A test fails if a status, date or refusal
reason text differs from the engine. Separate tests prove that the 120-day
scan and 15-day rollover limits refuse where the engine would compute, and
the Provisions, Warnings and Holiday caveats cells are compared with the
engine for every shipped rule. LibreOffice and Excel were not run; a live
check in the spreadsheet a firm uses is still worth doing before first
reliance, because blank-cell handling can differ (a rule with no period
length reads `got 0` rather than `got None`; it still refuses).

A table verified after a release reaches the workbook only in the next
release. Build a new bundle when a table changes.

The shared rules are in `references/ai-tool-mode.md`. The JSON rule tables
carry descriptive notes that mention the computation step; they are data and
are read as the rule's provenance. The build scans them only for code file names and paths, not for the word "script".

## How the source marks it

Keep Claude Code behaviour unchanged by editing one `SKILL.md`:

- Wrap code-only passages in `<!-- ai-tool:code -->` ... `<!-- /ai-tool:code -->`.
  The bundle drops them. They are invisible comments in the plugin.
- Write the replacement as a visible `## AI-tool mode` section at the end of
  the skill. In the plugin it is marked as ignorable by hosts that can run code.
- Write the no-code procedure in `plugins/legal-skills/ai-tool/no-code/<skill>.md`.
  It ships only in the bundle, as `skills/<skill>/no-code.md`, and the build
  adds a link to it at the top of the skill's `AI-tool mode` section. Links in
  it resolve against the bundle layout, not the plugin.
- `<!-- ai-tool:bundle: ... -->` carries bundle-only wording for a passage the
  bundle replaces. Claude Code reads the raw file, so it sees that text beside
  the original wording; the original gates and commands are intact.
- Elsewhere, word prose neutrally ("the deterministic computation step").

The validator and `tests/test_ai_tool_bundle.py` fail when a skill with a
`scripts/` folder lacks the section or the markers, when a skill with the
section has no no-code procedure, or when a procedure names no such skill. They also fail when any skill marks code-only
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
   226 files and 0.6 MB zipped, far below the reported (unverified) Vault limits.
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
