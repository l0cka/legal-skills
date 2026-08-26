# Australian Employment & Fair Work

Five skills for practitioners advising national system employers under the
Fair Work Act 2009 (Cth). Every skill maps, issue-spots or checks; none
concludes that a dismissal was unfair, that adverse action occurred, that a
redundancy was genuine, or that an employer is compliant.

- `configure-employment-profile` records the employer's coverage basis,
  size, instruments, contracts, policies, workforce composition and
  governance as a controlled profile the other skills run against.
- `map-fair-work-obligations` lays out the Act, NES, award and agreement
  layers that a described arrangement engages, with the current National
  Minimum Wage and high income threshold and an evidence state per row.
- `assess-termination-exposure` issue-spots unfair dismissal, general
  protections, redundancy, notice and unlawful termination exposure, and
  routes the Commission's 21-day periods to the litigation-deadlines script.
- `review-workplace-policy` gap-checks a policy set against the current
  statutory hooks, labelling each hook law or guidance.
- `track-fair-work-developments` verifies a watch register of amending Acts,
  reforms, wage reviews and regulator priorities against primary sources.

## Boundary

The plugin serves Australian legal practitioners and in-house lawyers. It
covers national system employers; employers outside the national system
(for example Western Australian unincorporated businesses and state public
sectors) are identified and routed to specialist review. Contractor
characterisation, discrimination merits, work health and safety, workers
compensation, superannuation guarantee and industrial action strategy are
outside scope.

No skill computes a time limit: the governing provision is named and the
candidate date comes from `$compute-procedural-deadlines`. No skill drafts
or lodges an application, response or agreement with the Fair Work
Commission or the Fair Work Ombudsman.

## Sources

Controlling sources are the official publishers: legislation.gov.au for the
Act (Compilation No. 73, C2026C00355, 7 July 2026 at the snapshot), the
Regulations and amending Acts; fwc.gov.au for awards, agreements, the Annual
Wage Review and Commission process; and fairwork.gov.au for Ombudsman
guidance. Commission and Ombudsman pages are guidance and are recorded with
their last-updated dates. Law-firm commentary, HR platform content and model
memory are discovery material only.

The shared [source and control method](references/fair-work-source-and-control-method.md)
defines the source hierarchy, evidence states and human-review requirements.
The [employment profile schema](references/employment-profile-schema.md)
defines the controlled employer configuration. The
[framework layers](references/framework-layers.md),
[termination exposure map](references/termination-exposure.md) and
[policy statutory hooks](references/policy-statutory-hooks.md) references
carry the research snapshot of 26 August 2026 with per-row evidence states.

## Permissions

No MCP server, app, hook or write action is bundled. The plugin reads
official public sources and the documents the practitioner supplies.

## Licence

MIT. Statutory text is reproduced only by section reference; regulator
material is cited, not copied.
