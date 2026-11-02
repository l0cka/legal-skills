---
name: track-whs-developments
description: Check the Australian work health and safety watch register on demand — each jurisdiction's adoption of the December 2025 model WHS Act incident notification amendments, industrial and workplace manslaughter offences, psychosocial regulations and codes, new or revised codes of practice, Safe Work Australia model-law amendments, the Commonwealth WHS Act compilation and regulator priorities — verifying each item against its primary source and reporting what moved since the register snapshot. Use for periodic horizon reviews, or before advice that depends on whether a jurisdiction has enacted a model-law change. Do not use to assert a model-law amendment, Bill or draft code as law in force, to run as an unattended monitor, or to replace the duty map for a specific arrangement (use $map-whs-duties).
---

# Track WHS Developments

Check every watch item against its primary source and report movement. A
model-law amendment, Bill or draft code is never an obligation until verified
in force in the jurisdiction.

Read the [source and control method](../../references/whs-source-and-control-method.md)
and work from the [watch register](references/watch-register.json).

## Workflow

1. Fix the review context.
   - Record the review date, the last review date if known, the
     jurisdictions in scope, and any position the practitioner wants
     rechecked (for example, an incident assessment that applied the old
     notification categories).
2. Check each watch item.
   - Retrieve each item's primary source and compare it with the recorded
     status at snapshot. Record `unchanged`, `moved` (describe the movement)
     or `resolved` (commenced, made, approved or abandoned). Record `cannot be
     determined` when the source is unavailable.
   - Verify enactment and commencement of each jurisdiction's legislation
     with that jurisdiction's checker. Never infer one jurisdiction's
     adoption from another's, or from a Safe Work Australia model-law page.
3. Sweep for new items.
   - Check Safe Work Australia's model-law amendment pages and each in-scope
     regulator's legislation and codes pages for developments the register
     does not yet hold. Propose them as new watch items with primary sources.
4. Assess impact on standing positions.
   - For each moved or resolved item, state which outputs it could affect (a
     duty map, an incident assessment, a psychosocial review, an officer
     review) and flag re-running the affected workflow. Do not silently
     restate old conclusions.
5. Set the human decision gate.
   - Name the responsible lawyer or register owner who decides register
     updates and any re-assessment.
     The register file in this plugin is a published snapshot: propose
     updates, do not treat the local copy as current.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Review: <date; last review; jurisdictions; positions rechecked>
Items: <id; status at snapshot; status now; movement; source; checked date;
  evidence state>
New items proposed: <item; primary source; why it matters>
Impact: <moved item; affected outputs; re-run recommended>
Human decision gate: <register owner; decisions required>
Limitations: <snapshot register; sources unavailable; no advice>
```

## Fail closed

Return `NOT READY` when the primary sources for most items cannot be reached.
Never describe a model-law amendment, Bill or draft code as in force in a
jurisdiction, never infer a commencement date from commentary, and never
update the shipped register file in place.
