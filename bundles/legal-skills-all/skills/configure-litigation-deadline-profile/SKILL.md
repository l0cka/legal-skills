---
name: configure-litigation-deadline-profile
description: Create or update the controlled practice profile that the Australian litigation-deadlines workflows require, recording the jurisdictions and forums practised in, the named human confirmer, the practice's actual diary system of record and the verification posture. Use before first use of the other litigation-deadlines skills or when the practice, forums or confirmer change. Do not use to compute any date, to mark a rule table verified or to approve the profile — approval is a human act.
---

# Configure Litigation Deadline Profile

Create the controlled profile the deadline workflows depend on. The profile
is a factual map of the practice, never a source of law, and only a named
human may approve it.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
and draft against the
[deadline profile schema](../../references/deadline-profile-schema.md).

## Workflow

1. Fix the practice facts.
   - Record jurisdictions, forums and civil matter types. Record whether
     the Australian Legal Research plugin is installed.
2. Fix the human controls.
   - Record the named confirmer (name and role) and the practice's actual
     diary system of record. Refuse to draft a profile without both.
   - Record the verification posture: when rule tables must be re-verified
     through `$verify-deadline-basis`.
3. Draft and hand over.
   - Draft the profile per the schema with a new version number. Present it
     for human approval and record where the practice chose to store it.
     The model never marks a profile approved.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Profile: <identifier; version; draft or approved>
Practice: <jurisdictions; forums; matter types>
Confirmation: <confirmer; diary system of record>
Verification posture: <per-matter | per-assessment; legal research plugin>
Gaps: <missing fields blocking approval>
Human decision gate: <who must approve; storage location decision>
Limitations: <profile is a factual map; every date remains provisional>
```

## Fail closed

Return `NOT READY` when the confirmer or the diary system of record is
missing — a profile without both cannot be approved. Never mark a profile
approved, never let profile content widen computed coverage or switch off a
warning, and route criminal-procedure practice areas `OUTSIDE SCOPE`.
