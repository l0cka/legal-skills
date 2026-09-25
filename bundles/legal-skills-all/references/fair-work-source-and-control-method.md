# Australian employment and Fair Work source and control method

## Scope

This method governs every skill in the `australian-employment-fair-work`
plugin. The plugin serves Australian legal practitioners and in-house
lawyers advising national system employers under the Fair Work Act 2009
(Cth). It maps and issue-spots; it never concludes that a dismissal was
unfair, that adverse action occurred, that a redundancy was genuine, or
that an employer is compliant. Contractor characterisation, state-system
employers, discrimination merits, workers compensation, work health and
safety, superannuation guarantee and industrial action strategy are
identified and routed to human or specialist review.

Section numbers, thresholds, dollar figures and dates in this plugin are
a research snapshot, not a cached rule. Each is a routing lead until the
official source is checked in the session that relies on it.

## Snapshot of the framework

At 26 August 2026 the framework has these layers, verified against
legislation.gov.au and the Fair Work Commission and Fair Work Ombudsman
sites on that date (see the plugin README for compilation identifiers):

1. **The Act** — the Fair Work Act 2009 (Cth), including the National
   Employment Standards in Part 2-2, unfair dismissal in Part 3-2, general
   protections in Part 3-1, and the Closing Loopholes amendments of 2023 and
   2024 as commenced.
2. **Modern awards and enterprise agreements** — instruments made by the
   Fair Work Commission under Parts 2-3 and 2-4, read with the Annual Wage
   Review decision in force.
3. **Regulations and legislative instruments** — the Fair Work Regulations
   2009 and instruments such as the high income threshold indexation and the
   Small Business Fair Dismissal Code.
4. **Regulator material** — Fair Work Commission benchbooks, guidelines and
   forms, and Fair Work Ombudsman guidance, labelled as guidance.
5. **Employer-supplied documents** — the employment profile, contracts,
   policies, enterprise agreements and payroll records, version-identified.

## Source hierarchy

1. Verify the Act, the Regulations and every commencement with
   `$check-commonwealth-legislation`; trace amendment history with
   `$trace-commonwealth-legislative-change`. A section number, threshold or
   date in this plugin is a routing lead until verified.
2. Use modern awards and enterprise agreements as published by the Fair
   Work Commission, recording the award code, clause and the version in
   force on the relevant date.
3. Use Fair Work Commission and Fair Work Ombudsman publications as
   regulator expectations and interpretation, labelled as guidance and never
   restated as statute. Record each page's last-updated date.
4. Use employer-supplied, version-identified documents for the employer's
   own position.
5. Treat law-firm commentary, HR platform content, search results and model
   memory as discovery material, never authority.
6. Route case law to `$route-case-citation`; do not rely on a decision that
   has not been verified at its official publisher.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  amendment, application or document-status qualification remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

Give each finding its source URL or document identifier, version or
effective date, relevant provision, clause or guidance section, checked date
and evidence state.

## Employment profile precedence

Use the approved profile only as a controlled factual map of the employer
(coverage, size, instruments, governance, policies). It cannot establish
that an instrument applies, that a threshold is met or that a dismissal is
protected from a claim. If profile content conflicts with a verified source,
surface the conflict and stop the affected conclusion. The model may draft a
profile but cannot mark it approved.

## Time limits

Fair Work Commission application periods are never computed by the model.
Name the governing provision and route the candidate date to
`$compute-procedural-deadlines`; where that plugin has no verified table for
the step, report the period as identify-only with the provision cited.

## Human control

Every output names the responsible lawyer or decision owner and the
decision they must make. The plugin never lodges, files or sends anything
to the Commission, the Ombudsman, an employee or a union, and never
represents that a termination, policy or payment is lawful.
