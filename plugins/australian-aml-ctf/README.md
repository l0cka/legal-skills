# Australian AML/CTF

This plugin supplies five governed workflows for Australian legal practices
regulated under the tranche 2 AML/CTF reforms:

- `configure-aml-ctf-practice-profile` creates a controlled practice profile;
- `map-designated-services` maps described legal services to the designated
  services in table 6 of the amended AML/CTF Act;
- `review-aml-ctf-program` issue-spots a practice's AML/CTF program and
  customer-due-diligence framework against the Act and the AML/CTF Rules 2025;
- `map-reporting-obligations` maps SMR, TTR and compliance-report triggers,
  the tipping-off offence and the legal-professional-privilege carve-outs for
  a described scenario; and
- `track-aml-ctf-developments` monitors the pending-guidance watch-list.

## Boundary

The plugin serves Australian legal practices — law firms, sole practitioners
and incorporated legal practices — that provide or may provide designated
services under table 6 of subsection 6(5B) of the *Anti-Money Laundering and
Counter-Terrorism Financing Act 2006* (Cth), as amended by the tranche 2
reforms that commenced on 1 July 2026. Other tranche 2 sectors (real estate,
accounting, trust and company service providers, dealers) and tranche 1
reporting entities are outside scope: services those sectors provide are
flagged for human review, never mapped.

The plugin never enrols a practice with AUSTRAC, never lodges a suspicious
matter report, threshold transaction report, compliance report or LPP form,
and never submits anything to any regulator — those are human-only acts
performed through AUSTRAC Online. It never performs or certifies customer due
diligence, never screens a person against sanctions lists, never concludes
that a matter is or is not suspicious, and never concludes that legal
professional privilege applies or is lost — privilege calls always go to the
responsible lawyer. IFTI obligations are not mapped: if a practice believes it
acts as an ordering or beneficiary institution, the workflows flag specialist
review. State and territory trust-accounting regimes under legal profession
legislation are a separate regulatory interface, flagged but not assessed.

Point-in-time verification of legislation routes to the separately installed
Australian Legal Research plugin. Privacy depth for customer-due-diligence
data handling routes to the Australian Privacy Cybersecurity plugin.

## Sources

Controlling sources are the official publishers: legislation.gov.au for the
Act, the Amendment Act 2024 and the Anti-Money Laundering and
Counter-Terrorism Financing Rules 2025 (F2025L01026), and austrac.gov.au for
regulator guidance including the reform hub, the professional
designated-services guidance, the legal profession program starter kit and
the legal-professional-privilege guidance. Law society implementation guides
and commentary are discovery material only — every proposition is confirmed
against the named primary source before use.

The shared [source and control method](references/aml-ctf-source-and-control-method.md)
defines the source hierarchy, evidence states and human-review requirements.
The [practice profile schema](references/aml-ctf-practice-profile-schema.md)
defines the minimum practice-controlled configuration. The
[LPP carve-outs reference](references/lpp-carve-outs.md) maps the statutory
privilege protections and LPP-form mechanics.

## Permissions

No MCP server, app, hook or write action is bundled. The workflows may use
the separately installed Australian Legal Research plugin for read-only
verification of legislation and case citations. Users decide what documents
to provide and where to save any approved output.

## Licence

MIT. This is an original Australian workflow based on public official sources.
