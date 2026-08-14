---
name: track-ai-regulatory-developments
description: Check the Australian AI regulatory watch-list on demand — the proposed Australian Standards for AI, OAIC automated-decision guidance, the ASX fifth-edition consultation, facial-recognition review litigation, privacy tranche 2 and eSafety code phases — confirming each item against its named primary source and reporting what changed since the register snapshot. Use for periodic regulatory horizon reviews or before advice that depends on a pending instrument. Do not use to assert a pending instrument as law, run as an unattended monitor, or replace obligations mapping for a specific use case.
---

# Track AI Regulatory Developments

Report what has moved on the watch-list since the register snapshot, item by
item, from primary sources. A pending instrument remains a watch item until
its commencement is verified.

Read the [source and control method](../../references/ai-governance-source-and-control-method.md)
and use the [watch register](references/watch-register.json).

## Workflow

1. Fix the review scope and date.
   - Default to every register item; narrow to named items on request.
     Record the review date and the register's `as_at` snapshot date.
2. Check each item against its primary source.
   - Fetch the named primary source and compare with `status_at_snapshot`.
     Record: unchanged, moved (describe the change with the source's own
     date), or source unavailable.
   - Discovery indexes such as policai.org's developments feed may be used to
     find leads, but no change is reported unless confirmed at the primary
     source.
3. Classify every change.
   - A Bill introduced, guidance finalised or decision delivered changes the
     item's status; only a verified commencement makes anything an
     obligation. Where an instrument has commenced, state that the register
     is stale and route the obligations question to
     `$map-ai-regulatory-obligations`; verify commencement with
     `$check-commonwealth-legislation` or the relevant state skill.
4. Surface new watch candidates separately.
   - New consultations, announcements or litigation found during the review
     are proposed additions with their primary source, clearly separated
     from register items.
5. Set the human decision gate.
   - Identify which changes affect the organisation's profile overlays, who
     should be told, and any dated follow-up the reviewer should schedule.
     This skill runs on demand; users may wrap it in their own scheduler.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Review date and register snapshot: <dates>
Item status: <item; unchanged/moved/source unavailable; evidence and source URL>
Changes explained: <what moved, per the primary source, with dates>
Commenced instruments: <any item now in force, with verification route>
Proposed register additions: <new candidates with primary sources>
Human decision gate: <who to inform, affected overlays, next review date>
Limitations: <watch items are not obligations; register may be stale>
```

## Fail closed

Return `READY WITH QUALIFICATIONS` when any primary source is unavailable and
record the item as unresolved rather than assuming no change. Never report a
change on the strength of a discovery index or commentary alone, never
present a pending instrument as in force, and never silently drop a register
item that could not be checked.
