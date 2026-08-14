---
name: track-aml-ctf-developments
description: Check the Australian AML/CTF watch register for developments affecting legal practices — pending ministerial LPP guidelines, AUSTRAC guidance waves, amendments to the AML/CTF Rules 2025 and transitional rules — verifying each item against its primary source and reporting what changed, what remains pending and what has become binding since the last review. Use for periodic monitoring or before relying on a previously mapped position. Do not use to assert a pending instrument as in force, to conclude new obligations apply without verification or to give final legal advice.
---

# Track AML/CTF Developments

Check every watch item against its primary source and report movement.
A pending instrument is never an obligation until verified in force.

Read the [source and control method](../../references/aml-ctf-source-and-control-method.md)
and work from the [watch register](references/watch-register.json).

## Workflow

1. Fix the review context.
   - Record the review date, the last review date if known and any specific
     position the practice wants rechecked (for example, a mapping done
     before a guidance update).
2. Check each watch item.
   - Retrieve each item's primary source and compare against the recorded
     status-at-snapshot. Record: unchanged, moved (describe the movement),
     or resolved (the item commenced, was released, was made or was
     abandoned).
   - For legislative items, verify commencement and current text through
     `$check-commonwealth-legislation` and trace amendments with
     `$trace-commonwealth-legislative-change`.
3. Sweep for new items.
   - Check the AUSTRAC reform hub and the AML/CTF Rules page for new
     guidance, amendment instruments or consultations affecting legal
     practices that the register does not yet hold. Propose them as new
     watch items with primary sources.
4. Assess impact on standing positions.
   - For each moved or resolved item, state which plugin outputs it could
     affect — a designated-services mapping, a program review, a reporting
     map — and flag re-running the affected workflow. Do not silently
     restate old conclusions.
5. Set the human decision gate.
   - Name the reviewer who decides register updates and any re-assessment.
     The register file in this plugin is a published snapshot: propose
     updates, do not treat the local copy as current.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Review: <date; last review; positions to recheck>
Item status: <item; unchanged | moved | resolved; evidence; source URL;
  checked date; evidence state>
New items proposed: <item; primary source; expected trigger>
Impact: <affected workflow outputs and recommended re-runs>
Human decision gate: <reviewer; register updates and re-assessments>
Limitations: <pending items are not obligations; snapshot register>
```

## Fail closed

Return `NOT READY` when a primary source cannot be reached or a decisive
status cannot be established — an unreachable source is `NOT VERIFIED`,
never assumed unchanged. Never assert a pending instrument as in force,
never drop a watch item without evidence it resolved, and never present the
bundled register as current without checking.
