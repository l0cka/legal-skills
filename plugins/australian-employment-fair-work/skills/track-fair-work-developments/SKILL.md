---
name: track-fair-work-developments
description: Check the Australian Fair Work watch register on demand — new Fair Work Act compilations and amending Acts, the Building Cooperative Workplaces reforms, Closing Loopholes transitional issues, the Annual Wage Review and threshold indexation, proposed non-compete reforms, gender-undervaluation award reviews, employee-like minimum standards orders and Fair Work Ombudsman priorities — verifying each item against its primary source and reporting what moved since the register snapshot. Use for periodic horizon reviews or before advice that depends on a pending instrument or a figure that indexes on 1 July. Do not use to assert a pending instrument as law, to run as an unattended monitor, or to replace the obligations map for a specific arrangement.
---

# Track Fair Work Developments

Check every watch item against its primary source and report movement.
A pending instrument is never an obligation until verified in force.

Read the [source and control method](../../references/fair-work-source-and-control-method.md)
and work from the [watch register](references/watch-register.json).

## Workflow

1. Fix the review context.
   - Record the review date, the last review date if known and any specific
     position the practitioner wants rechecked (for example, an obligations
     map prepared before 1 July).
2. Check each watch item.
   - Retrieve each item's primary source and compare it with the recorded
     status-at-snapshot. Record: unchanged, moved (describe the movement) or
     resolved (commenced, made, decided, published or abandoned). Record
     `cannot be determined` when the source is unavailable.
   - For legislative items, verify commencement and current text through
     `$check-commonwealth-legislation` and trace amendments with
     `$trace-commonwealth-legislative-change`.
3. Sweep for new items.
   - Check the Federal Register for new Fair Work Act compilations and
     amending Acts, the Fair Work Commission's major cases and legislation
     pages, and the Fair Work Ombudsman's legislation-changes page for
     developments the register does not yet hold. Propose them as new watch
     items with primary sources.
4. Assess impact on standing positions.
   - For each moved or resolved item, state which plugin outputs it could
     affect — an obligations map, a termination assessment, a policy review
     — and flag re-running the affected workflow. Do not silently restate
     old conclusions.
5. Set the human decision gate.
   - Name the reviewer who decides register updates and any re-assessment.
     The register file in this plugin is a published snapshot: propose
     updates, do not treat the local copy as current.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Review: <date; last review; positions rechecked>
Items: <id; status at snapshot; status now; movement; source; checked date;
  evidence state>
New items proposed: <item; primary source; why it matters>
Impact: <moved item; affected workflow outputs; re-run recommended>
Human decision gate: <register owner; decisions required>
Limitations: <snapshot register; sources unavailable; no advice>
```

## Fail closed

Return `NOT READY` when the primary sources for most items cannot be
reached. Never describe a pending instrument, Bill, exposure draft or
proposed reform as in force, never infer a commencement date from
commentary, and never update the shipped register file in place.
