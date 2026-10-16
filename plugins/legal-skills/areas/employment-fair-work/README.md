# Australian Employment & Fair Work

Ten skills for practitioners advising national system employers under the Fair
Work Act 2009 (Cth). Every skill maps, issue-spots or checks; none concludes
that a dismissal was unfair, that adverse action occurred, that a redundancy was
genuine, or that an employer is compliant.

- `configure-employment-profile` records the employer's coverage basis, size,
  instruments, contracts, policies, workforce composition and governance as a
  controlled profile the other skills run against.
- `map-fair-work-obligations` lays out the Act, NES, award and agreement layers
  that a described arrangement engages, with the current National Minimum Wage
  and high income threshold and an evidence state per row.
- `assess-termination-exposure` issue-spots unfair dismissal, general
  protections, redundancy, notice and unlawful termination exposure, and routes
  the Commission's 21-day periods to the litigation-deadlines script.
- `review-workplace-policy` gap-checks a policy set against the current
  statutory hooks, labelling each hook law or guidance.
- `track-fair-work-developments` verifies a watch register of amending Acts,
  reforms, wage reviews and regulator priorities against primary sources.

- `review-employment-contract` Review an Australian employment contract against
  the NES, instrument coverage, set-off wording, IP, confidentiality,
  termination and fixed-term limits for qualified lawyer review. Use for
  onboarding or contract refreshes; never certify compliance or approve
  execution.
- `assess-employee-vs-contractor` Issue-spot Australian worker classification
  under Fair Work Act ss 15AA–15AD and sham contracting under s 357, including
  high-income opt-out evidence. Use before contractor drafting or engagement
  review; never classify conclusively from an ABN, label or income alone.
- `assess-discrimination-and-positive-duty` Map Australian workplace
  discrimination and positive-duty exposure under Commonwealth and NSW,
  Victorian and Queensland law, AHRC powers and Fair Work general protections.
  Use for incident or preventive-control review; never determine liability,
  certify compliance or assume Queensland reforms commenced.
- `assess-restraint-of-trade` Issue-spot Australian employment restraints
  against verified common-law reasonableness, NSW restraint legislation and the
  status of proposed Commonwealth non-compete reforms. Use for exit or clause
  reviews; never certify enforceability, assume a 2027 ban is in force or send
  demands.
- `compute-underpayment-exposure-framework` Prepare an Australian underpayment
  exposure framework using verified entitlement sources, payroll evidence,
  limitation leads and intentional-underpayment offence screening. Framework
  only: never invent award rates, compute a final liability or equate every
  error with wage theft.

## Boundary

The area serves Australian legal practitioners and in-house lawyers. It covers
national system employers; employers outside the national system (for example
Western Australian unincorporated businesses and state public sectors) are
identified and routed to specialist review. Contractor characterisation and
Commonwealth, NSW, Victorian and Queensland discrimination now have dedicated
issue-spotting workflows; conclusions remain with a qualified lawyer. Work
health and safety, workers compensation, superannuation guarantee, other
statutory classification regimes and industrial action strategy require
specialist review. Underpayment work is a framework only, without invented award
rates or final monetary exposure.

Every output requires qualified lawyer review. No skill computes a time limit:
the governing provision is named and the candidate date comes from
`$compute-procedural-deadlines`. No skill drafts or lodges an application,
response or agreement with the Fair Work Commission or the Fair Work Ombudsman.

## Sources

Controlling sources are the official publishers: legislation.gov.au for the Act
(Compilation No. 73, C2026C00355, 7 July 2026 at the snapshot), the Regulations
and amending Acts; fwc.gov.au for awards, agreements, the Annual Wage Review and
Commission process; and fairwork.gov.au for Ombudsman guidance. Commission and
Ombudsman pages are guidance and are recorded with their last-updated dates.
Law-firm commentary, HR platform content and model memory are discovery material
only.

The shared [source and control
method](../../references/fair-work-source-and-control-method.md) defines the source
hierarchy, evidence states and human-review requirements. The [employment
profile schema](../../references/employment-profile-schema.md) defines the controlled
employer configuration. The [framework layers](../../references/framework-layers.md),
[termination exposure map](../../references/termination-exposure.md) and [policy
statutory hooks](../../references/policy-statutory-hooks.md) references carry the
research snapshot of 26 August 2026 with per-row evidence states.

The [extension source checklist](../../references/employment-extension-sources.md)
records the 2026-10-13 baseline and unresolved official-source checks. The
area-wide catalogue lawCheckedOn remains 2026-08-26 because the original
references were not reverified as a whole. Only the extension checklist has the
2026-10-13 baseline; item-level watch reviews do not reset the area-wide date.
Verify every relied-on proposition at use.

NSW sites block automated retrieval. The NSW Restraints of Trade Act 1976 and
NSW Anti-Discrimination Act 1977 (NSW ADA) limbs are unverified at this
snapshot: verify against legislation.nsw.gov.au before relying on their
statutory content or effect. The skills provide issue spotting with those
conclusions unresolved.

## Permissions

No MCP server, app, hook or write action is bundled. The area
reads official public sources and the documents the practitioner supplies.

## Validation

Ten synthetic eval fixtures cover the ten skills, including missing evidence,
human approval, commencement and output boundaries. Unit tests check package
structure, local links, eval coverage and existing lawyer-control,
dated-reference and watch-register contracts. Fixture success does not prove
live skill invocation or legal application; live model evals are a separate
check.

## Licence

MIT. Statutory text is reproduced only by section reference; regulator material
is cited, not copied.
