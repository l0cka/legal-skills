---
name: review-aml-ctf-program
description: Issue-spot an Australian legal practice's AML/CTF program — the ML/TF risk assessment, AML/CTF policies, governance roles, personnel due diligence and training, record keeping and the design of initial, ongoing, enhanced and simplified customer due diligence — against the amended AML/CTF Act, the AML/CTF Rules 2025 and AUSTRAC's legal profession program starter kit, using verified official sources. Use for gap reviews of draft or approved programs and CDD frameworks. Do not use to certify compliance, approve a program, perform customer due diligence on a real person or conclude that governance is adequate — approval belongs to senior management.
---

# Review AML/CTF Program

Issue-spot a practice's AML/CTF program and CDD framework design against the
Act, the Rules and AUSTRAC's published expectations. Find gaps; never
certify.

Read the [source and control method](../../references/aml-ctf-source-and-control-method.md)
and use an approved profile per the
[practice profile schema](../../references/aml-ctf-practice-profile-schema.md).

## Workflow

1. Fix the documents and time.
   - Record each document supplied for review with its identifier, version,
     effective date and status, and the date of review.
   - Require an approved, current practice profile and the designated
     services the program must cover — route an unmapped service line to
     `$map-designated-services` first.
2. Review the program core.
   - ML/TF risk assessment: does it identify and assess money laundering,
     terrorism financing and proliferation financing risks for the
     practice's designated services, customers, delivery channels and
     jurisdictions?
   - AML/CTF policies: do policies, procedures, systems and controls address
     each identified risk and each obligation the practice has?
   - Verify each obligation proposition against the Act and the AML/CTF
     Rules 2025 through `$check-commonwealth-legislation` and record
     AUSTRAC's legal profession program starter kit sections used, as
     guidance.
3. Review governance and personnel.
   - Test the three governance roles AUSTRAC expects — governing body,
     approving senior manager or managers, AML/CTF compliance officer —
     against the profile's recorded role holders, noting that one person may
     hold multiple roles in a small practice.
   - Check personnel due diligence and AML/CTF training arrangements exist
     and cover the people performing AML/CTF functions.
4. Review CDD framework design.
   - Check the design of initial and ongoing CDD, enhanced CDD for high-risk
     scenarios and any use of simplified CDD for low-risk scenarios, and how
     the framework identifies the customer of each designated service.
   - Check record-keeping design: program records, CDD records and
     transaction records, with the retention period stated in the practice's
     policy verified against the Rules.
   - Route privacy handling of CDD data to
     `$assess-australian-privacy-issues`. Record only the routing result.
5. Assemble gaps and set the human decision gate.
   - List each gap with the document, the obligation or expectation it
     fails, the source and evidence state. Name the senior manager or
     governing body who must decide remediation and approve any change.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Documents reviewed: <ID; version; effective date; status>
Profile: <approved identifier and version>
Designated services covered: <from mapping; gaps routed>
Program findings: <risk assessment and policy gaps with source per finding>
Governance findings: <roles, personnel due diligence, training>
CDD framework findings: <initial, ongoing, enhanced, simplified, records>
Routed depth: <privacy or other skill routings and results>
Verified: <provision or guidance; source URL; evidence state; checked date>
Human decision gate: <approver; remediation decisions required>
Limitations: <issue-spotting only; no certification or approval>
```

## Fail closed

Return `NOT READY` when the supplied documents, the profile or the
designated-service coverage cannot be established. Never mark a program
compliant or adequate, never perform CDD on a real customer, never draft
findings that conclude a matter is suspicious, and never treat starter-kit
or guidance content as the statute or Rules it interprets.
