---
name: assess-discrimination-and-positive-duty
description: Map Australian workplace discrimination and positive-duty exposure under Commonwealth and NSW, Victorian and Queensland law, AHRC powers and Fair Work general protections. Use for incident or preventive-control review; never determine liability, certify compliance or assume Queensland reforms commenced.
---

# Assess Discrimination and Positive Duty

Jurisdiction: Australia; Fair Work application requires a verified national
system basis. State overlays are separately identified. Snapshot: 2026-10-13;
this is a research baseline, not a current-law assurance. Verify every relied-on
provision, threshold and commencement at its official publisher for the relevant
date, using `$check-commonwealth-legislation` for Commonwealth law.

Read the [source and control method](../../references/fair-work-source-and-control-method.md),
reuse the [employment profile schema](../../references/employment-profile-schema.md)
and consult the [extension source checklist](../../references/employment-extension-sources.md).
Assume only evidenced instructions and documents; unknown facts stay unknown.
Every output requires review by a qualified lawyer before reliance.

## Workflow

1. Reuse `$configure-employment-profile` and the employment profile schema. Record work and conduct locations, employer/PCBU basis, worker status, protected attributes alleged, conduct/dates, decision-maker reasons, witnesses and preventive measures. Keep allegations separate from findings and minimise personal information. Urgent protection, support and evidence preservation go to the responsible human owner; do not contact parties.
2. Build separate Commonwealth tracks from the extension reference. Verify Sex Discrimination Act 1984 s 47C and its precise conduct/person scope at legislation.gov.au. Assess reasonable and proportionate preventive measures against risks, resourcing, training, leadership, reporting, response and monitoring; a policy alone does not establish discharge. Label AHRC guidance as guidance, record its version and do not turn every guideline into a statutory rule.
3. Separately map Disability Discrimination Act 1992, Racial Discrimination Act 1975 and Age Discrimination Act 2004 employment provisions, direct/indirect discrimination, adjustments, exceptions and vicarious liability where relevant. Verify each relied-on section and version on legislation.gov.au. Do not generalise the SDA positive duty into an identical duty under every Act or decide an inherent-requirements/exception defence without evidence.
4. Verify AHRC Act 1986 Part II Division 4A, including inquiry, compliance-notice, enforcement and undertaking powers at legislation.gov.au. Separate positive-duty oversight from individual complaint/conciliation and court routes. Identify forum, remedy and time-limit questions for `$compute-procedural-deadlines`; unresolved jurisdiction tables are identify-only. Never lodge, respond to a notice or promise an outcome.
5. Map Anti-Discrimination Act 1977 (NSW), Equal Opportunity Act 2010 (Vic) and Anti-Discrimination Act 1991 (Qld) separately using `$check-nsw-legislation`, `$check-victoria-legislation` and `$check-queensland-legislation`. Verify at legislation.nsw.gov.au, legislation.vic.gov.au and legislation.qld.gov.au. Victorian s 15 has a preventive duty; do not equate its scope or enforcement with SDA s 47C. NSW detailed provisions remain verify-against-source leads in this snapshot. Queensland's Respect at Work and Other Matters Amendment Act 2024 contains reforms enacted but not yet in force, including the new positive duty: commencement awaits proclamation, with no date confirmed. Check individual amendment/proclamation status; some provisions already commenced. Do not assert blanket commencement on 1 July 2025.
6. Map the same facts separately to Fair Work Act Part 3-1, including s 351 and workplace-right issues, with `$check-commonwealth-legislation`. Use `$assess-termination-exposure` for dismissal overlap. Record distinct tests, exceptions, forum/election and duplicate-proceeding questions without assuming that success under one Act establishes another claim. Route sensitive personnel data through `$assess-australian-privacy-issues`.
7. Return a jurisdiction/claim/control matrix and prioritised gaps. A qualified lawyer must review application, forum choices and preventive-control recommendations; no merits finding or duty-compliance certification.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

Return: Conduct chronology and allegation states; jurisdiction/Act/provision/source matrix; positive-duty controls and gaps; AHRC oversight vs complaint routes; Queensland amendment/commencement table; general-protections overlap; forum/time-limit hand-off. Include scope/date/assumptions, evidence state for each
proposition, official source URL/identifier, version, provision or clause,
actual checked date, unresolved issue/resolver and qualified lawyer decisions.
Snapshot dates never substitute for the date a source was actually accessed.
An unavailable named skill means its step was not done; name the plugin to install.

## Fail closed

No conduct or preventive-control facts: `NOT READY`. Unverified commencement blocks the affected statutory claim. Other states/territories: `OUTSIDE SCOPE` for their detailed law, with named specialist review. Never certify the duty is met, determine discrimination liability or make a complaint.
Unverified law is labelled `NOT VERIFIED` with “verify against <official source>”;
stop the affected conclusion while completing supported issue spotting.
No saving outside the approved matter system, sending, filing, signing or payment
is authorised by invocation of this skill.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`, `check-queensland-legislation`,
  `check-victoria-legislation`. Verifies the Fair Work Act and related
  legislation and case-law leads against the official sources.
- `australian-litigation-deadlines` (required):
  `compute-procedural-deadlines`. Computes the Fair Work Commission time
  limits the termination assessment flags.
- `australian-privacy-cybersecurity` (hand-off):
  `assess-australian-privacy-issues`. Assesses personnel-data, confidentiality
  and privacy application questions.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
