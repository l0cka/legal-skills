# Australian AML/CTF source and control method

## Scope

Use this method for Australian legal practices assessing their position under
the *Anti-Money Laundering and Counter-Terrorism Financing Act 2006* (Cth) as
amended by the *Anti-Money Laundering and Counter-Terrorism Financing
Amendment Act 2024* (Cth). The tranche 2 reforms made certain professional
services provided by legal practices designated services from 1 July 2026,
with enrolment obligations arising within 28 days of first providing a
designated service. The detail sits in the *Anti-Money Laundering and
Counter-Terrorism Financing Rules 2025* (F2025L01026) and transitional rules.

Treat these as separate workflows and route to them rather than duplicating
their depth:

- point-in-time verification of the Act, the Amendment Act and the Rules
  belongs to `$check-commonwealth-legislation` and
  `$trace-commonwealth-legislative-change`;
- privacy handling of customer-due-diligence data belongs to the Australian
  Privacy Cybersecurity plugin (`$assess-australian-privacy-issues`,
  `$check-australian-privacy-principles`); and
- state and territory trust-accounting obligations under legal profession
  legislation are a separate regulatory interface — flag them, never assess
  them here.

## Snapshot of the framework

At 14 August 2026 — a research snapshot, not a cached rule; every live
workflow must recheck each source:

1. **The Act** — designated services for professional services are in
   table 6 of subsection 6(5B); AUSTRAC's overview of the nine items is at
   <https://www.austrac.gov.au/new-austrac/designated-services-newly-regulated-entities/professional-designated-services>.
   Exemptions exist, including for legal aid commissions, community legal
   centres and barristers acting for Australian government bodies, and the
   incidental trust-money exemption in subsection 6(5C); AUSTRAC's
   exemptions guidance is the starting point and the Act text controls.
2. **The Rules** — the AML/CTF Rules 2025 (F2025L01026; commenced 31 March
   2026, replacing the AML/CTF Rules 2007; latest compilation F2026C00274 as
   at 31 March 2026), as amended, carry the program, CDD and reporting
   detail:
   <https://www.austrac.gov.au/about-us/legislation/amlctf-rules>. Check for
   amendment instruments and transitional rules at use time.
3. **AUSTRAC guidance** — the reform hub
   (<https://www.austrac.gov.au/industry-and-business/about-amlctf-reforms/about-reforms>),
   the tranche 2 obligations summary
   (<https://www.austrac.gov.au/amlctf-reform/reforms-guidance/before-you-start/summary-obligations-reform>),
   the legal profession program starter kit
   (<https://www.austrac.gov.au/industry-and-business/obligations-and-guidance/program-starter-kits/legal-profession-program-starter-kit>)
   and the LPP guidance
   (<https://www.austrac.gov.au/industry-and-business/obligations-and-guidance/your-amlctf-program/reporting-us/legal-professional-privilege>)
   are regulator interpretation, never statute.
4. **Pending layer** — the ministerial LPP guidelines under section 242A are
   announced but unreleased, and AUSTRAC continues to publish sector guidance
   in waves. Record pending items in the watch register, never as
   obligations.

## Source hierarchy

1. Verify the Act, the Amendment Act, the Rules and their commencement with
   `$check-commonwealth-legislation`; trace amendment history with
   `$trace-commonwealth-legislative-change`. A section number or a date in
   this plugin is a routing lead until verified.
2. Use AUSTRAC publications as regulator expectations and interpretation,
   labelled as guidance and never restated as statute. AUSTRAC's own pages
   carry a last-updated date — record it.
3. Use practice-supplied, version-identified documents (AML/CTF program,
   risk assessment, CDD policies, training records, governance documents)
   for internal controls.
4. Treat law society implementation guides, law-firm commentary, search
   results and model memory as discovery material, never authority.

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
effective date, relevant provision or guidance section, checked date and
evidence state.

## Practice profile precedence

Use the approved profile only as a controlled factual map of the practice
(structure, services, enrolment status, reporting-group membership,
governance roles, governing documents). It cannot establish that a service
is or is not designated and cannot excuse non-compliance. If profile content
conflicts with a verified source, surface the conflict and stop the affected
conclusion. The model may draft a profile but cannot mark it approved.

## Human control

The workflows may organise evidence, map services and obligations, identify
gaps and prepare drafts. They do not determine that a service is designated,
that a program complies, that a matter is suspicious, that privilege applies
or that any lodgement is due. Enrolment, every report, every LPP form and
every program approval is a human act: a principal, senior manager, AML/CTF
compliance officer or other authorised reviewer must confirm entity
classification, source application, material facts and next action.
