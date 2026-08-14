---
name: configure-aml-ctf-practice-profile
description: Create or update a controlled AML/CTF practice profile for an Australian legal practice regulated, or potentially regulated, under the tranche 2 reforms to the Anti-Money Laundering and Counter-Terrorism Financing Act 2006 (Cth) — practice structure, service lines, enrolment status, claimed exemptions, reporting-group membership, governance roles and program document inventory. Use before any other AML/CTF workflow so mapping and review run against approved practice facts. Do not use to decide whether a service is designated, to enrol with AUSTRAC or to approve the profile — approval is a human act.
---

# Configure AML/CTF Practice Profile

Build the controlled factual map of the practice that every other skill in
this plugin requires. The model drafts; an authorised human approves.

Read the [source and control method](../../references/aml-ctf-source-and-control-method.md)
and follow the [practice profile schema](../../references/aml-ctf-practice-profile-schema.md).

## Workflow

1. Establish the profile context.
   - Determine whether a profile exists. If one exists, load it, record its
     version, status and as-at date, and treat this run as an update.
   - Record who requested the profile and which authorised role will approve
     it. The model may only ever set status `draft`.
2. Collect the practice facts.
   - Complete every required field in the schema: structure, jurisdictions
     of practice, as-at date and review date.
   - Record the regulatory position fields as `yes`, `no` or `unknown` —
     never default a missing answer to `no`. Capture service lines the
     practice believes may be designated, enrolment status, reporting-group
     membership, trust-account operation, claimed exemptions and any
     foreign-branch or funds-transfer dimension.
   - Record governance roles (governing body, approving senior manager,
     AML/CTF compliance officer) by position title, and the document
     inventory for the program, risk assessment, CDD policies and training
     arrangements with versions and effective dates.
3. Verify what is checkable.
   - Claimed statutory bases (an exemption, a designated-service belief, an
     enrolment obligation) are recorded as claims with their source; route
     any statutory proposition the practice relies on to
     `$check-commonwealth-legislation` and record the evidence state.
   - Flag internal contradictions — for example, a claimed incidental
     trust-money exemption alongside a conveyancing service line.
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
Practice: <structure, jurisdictions>
Regulatory position: <field: value with source or claim basis per entry>
Governance and documents: <roles and inventory with versions>
Verified: <proposition; source; evidence state; checked date>
Gaps: <unknown fields and unverified claims, with resolver>
Contradictions: <conflicts between claims and facts>
Human decision gate: <approving role; approval and review fields to complete>
Limitations: <draft only; no designated-service or exemption conclusion>
```

## Fail closed

Return `NOT READY` when the practice structure, the service lines or the
governance roles cannot be established. Never mark a profile `approved`,
never default a regulatory-position answer to `no`, never conclude that an
exemption applies, and never record client information, matter information
or privileged material in the profile.
