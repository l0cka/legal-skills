# Deadline profile schema

The minimum practice-controlled configuration for the litigation-deadlines
workflows. The model may draft a profile; only a named human may approve it.
Store the approved profile where the practice chooses — the plugin never
writes anywhere on its own.

## Required fields

```yaml
profile:
  identifier: <practice-chosen id>
  version: <integer, increments on every change>
  approved_by: <name and role of the approving human>
  approved_date: <ISO date>

practice:
  jurisdictions: [<NSW | VIC | QLD | WA | SA | TAS | ACT | NT | Cth>]
  forums: [<courts and tribunals the practice appears in>]
  matter_types: [<civil matter types run>]

confirmation:
  confirmer: <name and role of the person who confirms every date>
  diary_system: <the practice's actual system of record for dates>
  confirmation_note: >
    Statement that computed dates are provisional until entered and
    confirmed in the diary system by the confirmer.

verification:
  posture: <when tables must be re-verified: per-matter | per-assessment>
  legal_research_plugin: <installed | not installed>
```

## Rules

1. `confirmer` and `diary_system` are mandatory — a profile without a named
   human confirmer and a named system of record cannot be approved.
2. The profile cannot switch off any warning, widen computed coverage, or
   mark a rule table verified — only `verify-deadline-basis` does that.
3. Record every change as a new version with its approver.
