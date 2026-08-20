# Marker syntax guide

A firm precedent is fillable only at explicit markers. Everything outside a
marker is untouchable precedent wording.

## Syntax

- A marker is `{{field_name}}`: two braces each side, a lowercase
  snake_case field name from the instruction record schema, no spaces.
- Repetition is per-slot, never by loop: a precedent that accommodates two
  executors carries `{{executor_1_full_name}}` and
  `{{executor_2_full_name}}` as separate markers.
- There is no conditional, loop or block syntax (`{{#each ...}}` and
  similar are not markers and must be reported as gaps if found).
- Anything brace-wrapped that does not match a schema field is an
  **unrecognised marker**: reported in the gap report, left in place,
  never guessed at.

## Fill rules

1. Replace a marker only with the confirmed instruction-record value for
   that exact field.
2. A marker whose field is `cannot be determined` or unconfirmed stays in
   place, listed in the gap report.
3. The same field appearing at several marker sites is filled identically
   at each site — the change manifest lists every site.
4. Alternative clauses in a precedent (for example three residue options)
   are a clause choice: presented to the solicitor in the gap report,
   never selected — unless a connected drafting playbook covers the point,
   in which case the playbook position is adopted and noted in the change
   manifest.
5. Nothing outside marker sites may change: not numbering, not
   cross-references, not formatting-significant wording. The change
   manifest must reconcile the output against the precedent; any
   difference outside a marker site makes the document `NOT READY`.

## Registering a precedent

The first time a precedent is used, propose the field map — each marker
paired with its schema field — for the solicitor to confirm. A precedent
containing no markers at all cannot be filled and is reported as such,
with the unrecognised-marker and clause-choice lists as the starting point
for the firm to mark it up.
