# Changelog

All notable changes to this repository are recorded here.

Plugins are versioned independently. The repository does not yet have release
tags, so the current pull request remains under **Unreleased** even where its
plugin manifests already contain their intended release versions.

## Unreleased

### Added

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
