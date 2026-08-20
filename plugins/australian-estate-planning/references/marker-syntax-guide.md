# Marker syntax guide

A firm precedent is fillable only at explicit factual or clause-choice markers.
Everything outside a marker is untouchable precedent wording.

## Syntax

- A factual marker is `{{field_name}}`: two braces each side, a lowercase
  snake_case field name from the instruction record schema, no spaces.
- A clause-choice marker is `{{clause_choice:clause_point}}`, for example
  `{{clause_choice:residue_distribution}}`. The clause point is lowercase
  snake_case and must appear in the precedent's confirmed clause-choice
  register.
- Repetition is per-slot, never by loop: a precedent that accommodates two
  executors carries `{{executor_1_full_name}}` and
  `{{executor_2_full_name}}` as separate markers.
- There is no conditional, loop or block syntax (`{{#each ...}}` and
  similar are not markers and must be reported as gaps if found).
- Anything brace-wrapped that is neither a schema field nor a registered
  clause-choice marker is an
  **unrecognised marker**: reported in the gap report, left in place,
  never guessed at.

## Clause-choice register

Each clause-choice marker has a closed list of approved variants registered
with the precedent. Every variant records a stable variant identifier, the
verbatim clause text, its source in the precedent or connected firm playbook,
and its approval state. The register contains firm-approved text only: it is
not a prompt or permission to compose, adapt or combine clauses.

Before a variant is inserted, the responsible solicitor confirms the clause
point, variant identifier and verbatim text for that matter. A playbook may
identify a registered variant; it cannot add one or bypass confirmation. If
the playbook is absent or silent, no registered variant matches its position,
or confirmation is outstanding, leave the marker in place and make the
document `NOT READY`.

## Fill rules

1. Replace a factual marker only with the confirmed instruction-record value
   for that exact field. Replace a clause-choice marker only with the
   solicitor-confirmed verbatim text of a registered variant.
2. A marker whose field is `cannot be determined` or unconfirmed stays in
   place, listed in the gap report.
3. The same field appearing at several marker sites is filled identically
   at each site — the change manifest lists every site.
4. Alternative clauses are represented by one clause-choice marker, never by
   leaving several alternatives in the fillable precedent. Record the marker,
   variant identifier, verbatim text, register source and solicitor
   confirmation in the change manifest.
5. Nothing outside marker sites may change: not numbering, not
   cross-references, not formatting-significant wording. The change
   manifest must reconcile the output against the precedent; any
   difference outside a marker site makes the document `NOT READY`.

## Registering a precedent

The first time a precedent is used, propose the field map — each factual
marker paired with its schema field — and the clause-choice register for the
solicitor to confirm. A precedent containing no markers at all cannot be
filled and is reported as such, with the unrecognised-marker and clause-choice
lists as the starting point for the firm to mark it up.
