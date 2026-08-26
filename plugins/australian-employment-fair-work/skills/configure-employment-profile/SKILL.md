---
name: configure-employment-profile
description: Create or update a controlled employment profile for an Australian employer under the Fair Work Act 2009 (Cth) — national system coverage basis, small business status and headcount bands, modern awards and enterprise agreements believed to apply, contract and policy inventory, workforce composition and governance roles — so the other Fair Work skills run against approved employer facts. Use before any other employment workflow or when the employer's instruments, size or policies change. Do not use to decide award or national system coverage, to characterise workers as employees or contractors, or to approve the profile — approval is a human act.
---

# Configure Employment Profile

Build the factual map the other skills depend on, and stop there. The
profile records what the employer believes and holds; it never decides
coverage, thresholds or characterisation.

Read the [source and control method](../../references/fair-work-source-and-control-method.md)
first, then complete the [employment profile schema](../../references/employment-profile-schema.md).

## Workflow

1. Establish the profile context.
   - Determine whether a profile exists. If one exists, load it, record its
     version, status and as-at date, and treat this run as an update.
   - Record who requested the profile and which authorised role will approve
     it. The model may only ever set status `draft`.
2. Collect the employer facts.
   - Complete every required field in the schema: entity type, jurisdictions
     of operation, as-at date and review date.
   - Record coverage and size fields as `yes`, `no` or `unknown` — never
     default a missing answer to `no`. Capture the claimed basis for national
     system coverage, the small-business headcount and its date, and any
     labour hire, group or franchise arrangement.
   - Record instruments by identifier: awards believed to cover employees,
     enterprise agreements with FWC approval references and nominal expiry
     dates, contract templates and policies with versions.
   - Record workforce composition as the employer classifies it, in counts,
     never re-characterising a casual, fixed-term or contractor arrangement.
   - Record governance roles by position title.
3. Verify what is checkable.
   - A claimed statutory basis (national system coverage, small-business
     status, an award's existence and coverage clause, a threshold figure) is
     recorded as a claim with its source; route any statutory proposition
     the employer relies on to `$check-commonwealth-legislation` and record
     the evidence state. Confirm award and agreement identifiers against the
     Fair Work Commission's published instruments.
   - Flag internal contradictions — for example, a claimed small-business
     status alongside a headcount above 15, or a casual classification with a
     regular roster the employer describes as permanent.
4. Assemble the draft and the gaps.
   - Produce the draft profile in the schema's structure with status
     `draft`, listing every `unknown` and every unverified claim as a gap
     with the person best placed to resolve it.
5. Set the human decision gate.
   - Name the approving role, the approval fields they must complete and the
     review-due date. Do not mark the profile approved.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Profile: <ID, version, status draft, as-at date>
Employer: <entity type, jurisdictions, coverage basis claimed, size band>
Instruments: <awards, agreements, contracts, policies with identifiers and versions>
Workforce: <composition counts as classified by the employer>
Governance: <roles by position title; systems>
Verified: <proposition; source; evidence state; checked date>
Gaps: <unknown fields and unverified claims, with resolver>
Contradictions: <conflicts between claims and facts>
Human decision gate: <approving role; approval and review fields to complete>
Limitations: <draft only; no coverage, threshold or characterisation conclusion>
```

## Fail closed

Return `NOT READY` when the employer cannot be identified or the requester
is not an authorised role. Never fill an `unknown` with a plausible value,
never decide award or national system coverage, never characterise a worker,
and never set a status other than `draft`. Route state-system employers and
contractor characterisation to `OUTSIDE SCOPE` with the specialist review
named.
