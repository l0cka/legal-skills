---
status: accepted
date: 2026-08-20
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

Integrity comes instead from instruction-level contracts enforced by the agent
definition: precedents are filled at explicit `{{field_name}}` markers only
(per-slot repetition, no block or conditional syntax); every fill produces a
change manifest (each location changed, marker removed, value inserted,
reconciled against the precedent) and a gap report; extraction from an
instruction sheet cites provenance per field and halts at a lawyer confirmation
gate; missing precedent, missing required field, or silent playbook all fail
closed to the responsible solicitor. This is self-attestation, not the proof a
deterministic script gives — the trade was accepted to keep one canonical,
platform-neutral markdown pack instead of per-platform forks.

Consequences: no file in the plugin may name or depend on any specific target
platform; firm content (precedents, playbooks, house style) is connected on the
platform side and never committed to this public repository; execution
formalities ship as a dated, provision-cited reference verified against
legislation.nsw.gov.au at each release, with a standing instruction to
re-verify live against the official publisher when the platform allows web
access.

Considered and rejected: a bundled stdlib fill/diff script (breaks direct
upload to script-less platforms); per-platform export surfaces from the
registry generator (maintenance cost, content drift); a bundled generic will
template as fallback (liability in a public MIT repo, contradicts the
fill-don't-draft model).
