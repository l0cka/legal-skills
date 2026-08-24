---
status: superseded
date: 2026-08-20
superseded_by: 0002-sidecar-precedent-profiles-for-human-designed-precedents.md
---

# Platform-neutral, no-script document assembly for australian-estate-planning

The `australian-estate-planning` plugin must be deployable by uploading its
markdown files directly into text-based enterprise agent platforms (an agent
definition plus attached reference files, an optionally connected firm drafting
playbook, and optional web access), as well as running as a normal plugin in
this repository. Those platforms cannot execute bundled scripts, so the plugin
ships none — a deliberate departure from the repository's script-only pattern
for operations that could silently change legal meaning (see
`australian-litigation-deadlines`, whose date arithmetic is script-only).

The original integrity mechanism required factual and clause-choice machine
markers in the firm's precedent, a closed register of firm-approved clause
variants, a change manifest and a gap report. This mechanism was superseded by
[ADR 0002](0002-sidecar-precedent-profiles-for-human-designed-precedents.md)
because ordinary firm precedents are designed for humans and do not contain
machine markers.

The platform-neutral, no-script decision remains in force through
[ADR 0003](0003-private-deployment-estate-drafting.md).
Firm content stays connected on the platform side and is never committed to
this public repository. Execution formalities remain dated,
jurisdiction-specific references with a standing instruction to re-verify
against the official publisher.

Originally considered and rejected: a bundled stdlib fill/diff script (breaks
direct upload to script-less platforms); per-platform export surfaces from the
registry generator (maintenance cost, content drift); a bundled generic will
template as fallback (liability in a public MIT repo, contradicts the
fill-don't-draft model).
