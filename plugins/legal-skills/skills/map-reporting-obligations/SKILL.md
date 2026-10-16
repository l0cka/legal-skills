---
name: map-reporting-obligations
description: Map which AML/CTF reporting obligations — suspicious matter reports, threshold transaction reports, annual compliance reports, AUSTRAC notices — are potentially triggered for a described scenario in an Australian legal practice, including the reformed tipping-off offence and the legal-professional-privilege carve-outs and LPP-form mechanics, using verified official sources. Use when a practice needs to understand what a scenario may require it to report and how privilege interacts. Do not use to decide that a matter is suspicious, to draft or lodge any report or LPP form, to conclude that privilege applies, or for IFTI obligations — those route to human or specialist review.
---

# Map Reporting Obligations

Map the reporting triggers a described scenario may engage and how legal
professional privilege interacts with each. The suspicion judgment, the
privilege judgment and every lodgement are human acts.

Read the [source and control method](../../references/aml-ctf-source-and-control-method.md),
the [LPP carve-outs reference](../../references/lpp-carve-outs.md) and use an
approved profile per the
[practice profile schema](../../references/aml-ctf-practice-profile-schema.md).

## Workflow

1. Fix the scenario and time.
   - Record the scenario as described — the designated service context, the
     transaction or information involved, what has been observed and when —
     without adding facts. Record the date of assessment.
   - Require an approved, current practice profile and a designated-service
     context; route an unmapped service to `$map-designated-services`.
2. Map potentially engaged report types.
   - Suspicious matter reports: state the statutory trigger as verified from
     the Act (section 41 is the routing lead) and AUSTRAC's timing guidance
     — 24 hours for terrorism-financing suspicions, 3 business days
     otherwise — as guidance. Map whether the described facts could engage
     the trigger; the suspicion itself is a human judgment, so express the
     result as "for human suspicion assessment", never as a conclusion.
   - Threshold transaction reports: physical currency of $10,000 or more,
     10-business-day lodgement, verified against the Act and Rules.
   - Annual compliance reports and AUSTRAC notices or requests
     (sections 26Q, 49, 49B, 167 and 202 are routing leads) that the
     scenario or profile indicates.
   - Verify every statutory proposition through
     `$check-commonwealth-legislation` at the assessment date.
3. Map the privilege interaction.
   - Apply the LPP carve-outs reference: whether each potentially engaged
     obligation carries an LPP-form requirement, the all-privileged and
     partly-privileged SMR positions, the extended 5-business-day
     SMR-with-LPP-form timeframe for non-terrorism suspicions, and the
     TTR-with-LPP-form position.
   - Record every privilege question as a flag for the responsible lawyer.
     Never assess whether a communication is privileged.
4. Map the tipping-off position.
   - State the reformed tipping-off offence (section 123 is the routing
     lead; the reformed offence commenced 31 March 2025) as verified, and
     flag disclosure decisions around the scenario — including to the
     client — for the responsible lawyer before anyone communicates.
5. Set the human decision gate.
   - Name the AML/CTF compliance officer and responsible lawyer who must
     assess suspicion, privilege and any lodgement, with the verified
     timeframes they would face. Flag any IFTI or cross-border dimension for
     specialist review without mapping it.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Scenario: <described facts, service context, assessment date>
Profile: <approved identifier and version>
Potentially engaged: <report or notice type; verified trigger; source;
  evidence state; timeframe as verified>
Privilege interaction: <per obligation: LPP-form requirement and position;
  privilege questions flagged to responsible lawyer>
Tipping-off: <verified position; communications flagged before disclosure>
Out of scope: <IFTI or cross-border dimensions for specialist review>
Human decision gate: <compliance officer and responsible lawyer;
  suspicion, privilege and lodgement decisions with timeframes>
Limitations: <no suspicion conclusion, no privilege conclusion, no lodgement>
```

## Fail closed

Return `NOT READY` when the scenario facts, the designated-service context
or a decisive statutory trigger cannot be established. Never conclude that a
matter is or is not suspicious, never conclude that privilege applies or is
waived, never draft SMR narrative content, never advise delaying or shaping
a report, and never map IFTI obligations.
