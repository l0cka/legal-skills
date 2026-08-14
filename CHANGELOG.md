# Changelog

This changelog records all notable repository changes.

Each plugin has an independent version. The repository does not have release
tags. The current pull request remains under **Unreleased**, even when its
plugin manifests contain their intended release versions.

## Unreleased

### Added

- Added `australian-ai-governance` 0.1.0 with six skills:
  `configure-ai-governance-profile`, `map-ai-regulatory-obligations`,
  `assess-board-ai-oversight`, `check-ai-guidance-alignment`,
  `triage-government-ai-use-case` and `track-ai-regulatory-developments`. The
  plugin creates a controlled AI-governance profile, maps which Australian
  instruments currently bind an AI use case while flagging pending
  instruments — including the proposed Australian Standards for AI — as watch
  items only, issue-spots board and director-duty AI exposure, checks
  governance documentation against the AI6 guidance with the superseded
  Voluntary AI Safety Standard as detail catalogue and AS ISO/IEC 42001 as
  crosswalk, routes government AI use cases to the Commonwealth DTA policy or
  the eight state and territory assurance frameworks, and checks a
  primary-source watch register on demand. AI-privacy depth stays with
  `australian-privacy-cybersecurity` and board-process depth with
  `australian-corporations-governance` via `$skill` routing. The plugin never
  asserts pending law as in force, never certifies compliance with any
  standard and treats trackers such as policai.org as discovery indexes only.

- Added `australian-legal-research` 0.1.0, merging the `australian-legislation`
  0.2.0, `australian-case-law` 0.1.0 and `australian-legal-citation` 0.1.0
  plugins into a single research plugin with all sixteen skills unchanged.
  The three source plugins covered one workflow — verify legislation, verify
  case citations and quoted passages, cite under AGLC4 — and every skill keeps
  its name, so `$skill` cross-references from other plugins are unaffected.
  Users of the three superseded plugins should uninstall them and install
  `australian-legal-research@legal-skills` instead.

- Added `australian-corporations-governance` 0.1.0 with five skills:
  `configure-corporations-governance`, `assess-director-duties-governance`,
  `prepare-board-decision-record`, `review-corporations-governance-framework`
  and `maintain-corporations-governance-calendar`. The plugin configures a
  controlled governance profile, issue-spots decision-process risks, drafts
  board records, reviews governance frameworks and creates source-linked
  calendars for companies governed by the *Corporations Act 2001* (Cth). It
  separates ASX, APRA, ACNC and CATSI overlays, treats consultation drafts as
  non-operative, and never approves, files, executes or invents corporate action.

- Added `australian-legal-citation` 0.1.0 with one skill,
  `format-aglc4-citations`, ported from the author's private gt-skills
  workbench with firm-specific branding removed. The skill drafts, converts,
  reviews and corrects citations and bibliographies under the Australian
  Guide to Legal Citation, 4th edition, covering footnotes, pinpoints,
  subsequent references, cases, legislation, secondary sources, treaties,
  international and foreign materials, quotation treatment and citation
  audits. It ships an operational distillation with a source map recording
  provenance, chapter routing and missing appendices; it never invents a
  missing citation field and keeps formatting separate from source
  verification.

- Added `australian-case-law` 0.1.0 with five skills: `route-case-citation`,
  `verify-hca-judgment`, `verify-nsw-judgment`, `verify-federal-judgment` and
  `verify-case-quote`. The plugin verifies Australian case citations and
  quoted passages against the official court publishers, routes each citation
  by its medium-neutral court identifier, distinguishes `UNVERIFIABLE` from
  `NOT FOUND`, and never bypasses publisher bot challenges. Includes a shared
  case-law verification method reference, an offline citation parser and a
  structural and parser test suite.

- Added a shared point-in-time method reference to `australian-legislation`
  0.2.0 and gave every State and Territory checker the same full workflow,
  result contract and fail-closed sections that the Commonwealth and NSW
  checkers already had.
- Added worked examples, including a `VERIFIED WITH QUALIFICATIONS` result, to
  the Commonwealth legislation, data breach and triage skills.
- Extended repository validation to check skill descriptions, frontmatter
  form, relative links, `agents/openai.yaml` interface files, per-skill
  registry versions, plugin READMEs, and description, tag and keyword parity
  between manifests and both marketplace catalogs.
- Added a validator unit-test suite and structural tests for every
  jurisdiction checker's headings and result-contract fields.
- Added a CI Python version matrix, a ruff lint job with a pinned repository
  ruff configuration, a README badge-count check and compilation of all
  plugin helper scripts.
- Added `SECURITY.md` with a private vulnerability reporting path.

- Added `australian-legislation` 0.1.0, combining the existing Commonwealth and
  New South Wales workflows with official-source legislation checks for the
  Australian Capital Territory, Northern Territory, Queensland, South
  Australia, Tasmania, Victoria and Western Australia.
- Expanded `australian-privacy-cybersecurity` 0.3.0 with jurisdiction routing,
  a legislation-only statutory privacy tort assessment, date-gated automated
  decision transparency analysis and a Commonwealth cyber incident obligations
  matrix.
- Added current-law privacy and cybersecurity registries covering State and
  Territory privacy, health, surveillance, workplace and data breach overlays,
  together with Commonwealth sectoral cyber regimes.
- Added regression coverage for the combined legislation plugin, privacy and
  cyber registries, APP provenance controls and future-law transitions.

### Changed

- Simplified the README language and added a paste-ready Agent request for
  plugin installation.
- Recorded plugin descriptions, versions and keywords in the ChatGPT Work
  marketplace catalog so both catalogs carry the same discovery metadata.
- Documented the required `agents/openai.yaml` interface file, aligned the
  three pre-submission command checklists, and expanded the README plugin
  layout diagram.
- Documented each bundled helper script as optional and read-only, including
  which official publisher it contacts and how the skill degrades without
  command execution (`legal-triage` 0.1.1, `australian-privacy-cybersecurity`
  0.3.1).
- Restored Australian English spelling in the README.
- Strengthened APP verification so schema-valid user-supplied text cannot be
  described as authoritative without verified source provenance.
- Split APP analysis into statutory text, application perimeter, codes and
  instruments, known future amendments and OAIC guidance currency.
- Updated AI-system and data breach workflows to route concurrent privacy,
  cyber, sectoral and contractual obligations without treating case law as in
  scope.

### Removed

- Removed the `australian-legislation`, `australian-case-law` and
  `australian-legal-citation` plugins, superseded by `australian-legal-research`
  0.1.0 above.

### Fixed

- Made the legal triage test fixture independent of the caller's home directory
  so repository validation is deterministic in CI.

## 2026-08-14 - Initial repository

### Added

- Created the provider-neutral Legal Skills marketplace for Claude Cowork and
  ChatGPT Work, with paired plugin manifests, a portable skill registry and
  offline repository validation.
- Added Commonwealth legislation verification and legislative change tracing.
- Added New South Wales legislation verification.
- Added governed community legal centre triage workflows.
- Added the initial Australian privacy, APP, data breach and AI use-case
  assessment workflows.
