# Changelog

This changelog records all notable repository changes.

Each plugin has an independent version. The repository does not have release
tags. The current pull request remains under **Unreleased**, even when its
plugin manifests contain their intended release versions.

## Unreleased

### Added

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
