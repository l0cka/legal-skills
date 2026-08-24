---
status: superseded
date: 2026-08-21
supersedes: 0001-platform-neutral-no-script-document-assembly.md
superseded_by: 0003-private-deployment-estate-drafting.md
---

# Sidecar precedent profiles for human-designed estate precedents

## Context

Firm estate-planning precedents are authored for lawyers, not machines. They
may use ordinary headings, clauses, tables, blank cells, content controls and
formatting without containing dedicated machine markers. Requiring the firm to
rewrite those precedents before using the workflow would make the plugin
impractical and create a separate template-maintenance burden.

The plugin must still prevent an agent from guessing where to insert content,
rewriting uncontrolled precedent text or silently carrying a cached mapping
across a changed precedent. It must also retain the platform-neutral,
no-bundled-script constraint adopted in ADR 0001.

## Decision

Keep every human-designed source precedent unchanged. Register its permitted
factual and clause sites in a separate, solicitor-confirmed precedent profile.
The profile records:

- precedent identity, version or approval date, and a content fingerprint
  where available;
- a stable identifier, structural location, exact surrounding text, target,
  operation and expected occurrence count for every permitted site;
- the field map and closed register of firm-approved verbatim clause variants;
  and
- the responsible solicitor's confirmation and date.

First use produces a proposed profile and stops. It cannot fill the precedent
until the solicitor confirms the profile. Later use makes a working copy only
after the source identity and every registered site still match. A fingerprint
mismatch, missing or duplicate anchor, changed target, ambiguous location or
unexpected occurrence count is precedent drift and requires a newly confirmed
profile.

Every fill reconciles the complete working copy against the unchanged source
precedent and returns a site-level change manifest and gap report. Any change
outside a registered site, unresolved clause choice, unconfirmed or missing
fact, or drift finding makes the affected document `NOT READY`.

## Consequences

- Firms may use their existing human precedents without adding machine syntax.
- The source precedent and the sidecar profile have separate lifecycles and
  approval records.
- Integrity remains instruction-governed rather than script-proven, so the
  pack stays portable to text-based platforms that cannot execute bundled
  code.
- Firm precedents, profiles, playbooks, instruction sheets and client data
  remain connected firm material and are never committed to this public
  repository.
- No precedent or confirmed profile means no fill; there is no generic
  fallback document.

## Considered and rejected

- Editing machine markers into every firm precedent: incompatible with the
  firm's existing human drafting assets and creates duplicate maintenance.
- Approximate or semantic-only location matching: permits silent changes at
  the wrong location after precedent drift.
- Filling during the same step that proposes a profile: bypasses the
  solicitor's registration gate.
- A bundled deterministic document editor: unavailable on supported
  script-less deployment surfaces and would require platform-specific forks.
