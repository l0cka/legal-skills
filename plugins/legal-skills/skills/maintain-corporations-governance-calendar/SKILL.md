---
name: maintain-corporations-governance-calendar
description: Create, validate or update a source-linked governance calendar for an Australian company using verified statutory triggers, an approved governance profile and controlled organisation documents. Use for recurring reviews, meetings, records, appointments, notifications and reporting checkpoints with owners and evidence. Do not calculate dates from cached rules, submit filings, send notices, create regulator reminders without verified application, or cover tax, employment, licensing or sector calendars unless separately scoped.
---

# Maintain Corporations Governance Calendar

Build a reviewable calendar, not an autonomous compliance system. A date is
exact only when both its controlling trigger and the entity-specific event are
verified.

Read the [source and control method](../../references/governance-source-and-control-method.md)
and use the approved [profile schema](../../references/governance-profile-schema.md).

## Workflow

1. Confirm scope and horizon.
   - Record the company, profile version, covered governance functions, start
     and end dates and excluded calendars.
   - Identify listed, APRA, ACNC, CATSI and sector overlays. Do not blend their
     deadlines into the core calendar without a separately verified source map.
2. Build a source register.
   - Use `$check-commonwealth-legislation` for each statutory trigger at the
     relevant date. Check application, commencement, modification and any known
     future change separately.
   - Record internal review triggers from approved constitutions, delegations,
     charters and policies by document ID, clause, version and effective date.
   - ASIC pages or forms may explain process but do not replace controlling law.
3. Derive each calendar item.
   - Record event, source, trigger, entity-specific anchor date, calculation,
     due date or `TBC`, accountable owner role, reviewer, lead time, evidence of
     completion and escalation path.
   - Use `TBC – SOURCE REVIEW REQUIRED` if the source or anchor date is missing.
     Never guess a business-day adjustment, extension or notification period.
4. Separate current and future requirements.
   - Keep enacted but uncommenced law and consultation drafts in a future-change
     register with their status and monitoring owner. Do not place them in the
     current calendar as operative obligations.
5. Hand off without acting.
   - Give the authorised owner an import-neutral table plus an exception list.
   - Do not create external calendar events, send reminders, lodge forms, notify
     ASIC or any other regulator, or mark completion without supplied evidence.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY` or
`OUTSIDE SCOPE`.

```text
Calendar perimeter and horizon: <entity, functions, dates and exclusions>
Profile version: <approved identifier>
Applicable overlays: <checked status and separate calendar needs>
Source register: <source; version; trigger; evidence state; checked date>
Calendar items: <event; trigger; anchor; calculation; due date/TBC; owner; reviewer; lead time; completion evidence>
Future-change register: <change; legal status; possible effect; monitoring owner>
Exceptions: <missing source, anchor, owner or unresolved conflict>
Verified legal sources: <official URLs and provisions>
Human activation gate: <reviewer and import/notification decision>
Limitations: <no filing, notice, reminder or completion action>
```

## Fail closed

Return `NOT READY` when the entity perimeter, applicable regime, controlling
source, anchor date or accountable owner is missing for a material item. Use
`TBC`, not an estimated deadline. Never rely on a cached deadline, silently
apply a draft or future rule, create a regulator filing, send a notice or mark
an obligation complete without human-supplied evidence.
