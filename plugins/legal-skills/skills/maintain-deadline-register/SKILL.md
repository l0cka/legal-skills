---
name: maintain-deadline-register
description: Build and update a source-linked deadline register for one Australian civil litigation matter, where every entry carries its governing rule citation, trigger assumption, script or mapping provenance, evidence state and confirmation status, and unconfirmed entries stay visibly provisional. Use to assemble computed and mapped candidates into a reviewable register, to record the confirmer's confirmations or to update entries after a trigger changes. Do not use as the practice's diary or system of record, to confirm a date, or to recompute dates outside the bundled script — the register mirrors decisions made elsewhere and confirmation is a human act.
---

# Maintain Deadline Register

Assemble candidate dates into one register per matter. The register mirrors
the outputs of the other workflows and the confirmer's decisions — it never
creates a date and it is not the practice's diary.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
and use an approved profile per the
[deadline profile schema](../../references/deadline-profile-schema.md).

## Workflow

1. Fix the matter and collect entries.
   - Record the matter identifier and gather candidates only from
     `$map-limitation-periods`, `$compute-procedural-deadlines` and
     `$map-tribunal-review-deadlines` outputs. A date with no workflow
     provenance does not enter the register.
2. Build the register.
   - One row per candidate: date, governing citation, trigger assumption,
     provenance (which workflow and script result), evidence state,
     warnings, and confirmation status starting at `provisional`.
   - Keep the conservative marker and every unresolved characterisation
     visible; never collapse candidates into a single date.
3. Record confirmations and changes.
   - Record a confirmation only as reported by the named confirmer, with
     name and date, and note that the date must also be entered in the
     diary system of record. When a trigger changes, mark dependent entries
     `stale` and route recomputation to the owning workflow.
4. Hand over.
   - Present the register for review and record where the practice chose to
     store it. The plugin writes nowhere on its own.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Matter: <identifier; profile used>
Register: <per entry: date; citation; trigger assumption; provenance;
  evidence state; status provisional | confirmed (by, date) | stale>
Unresolved: <candidates awaiting characterisation or verification>
Human decision gate: <confirmer; entries awaiting confirmation; diary
  entries pending>
Limitations: <register is not the diary or system of record; every
  unconfirmed entry is provisional>
```

## Fail closed

Return `NOT READY` when an entry lacks provenance, a citation or a trigger
assumption — never register a bare date. Never mark an entry confirmed
without the named confirmer's reported confirmation, never drop a stale
entry silently, and route criminal-procedure steps `OUTSIDE SCOPE`.
