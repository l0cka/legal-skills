# Australian litigation deadlines source and control method

## Scope

Use this method when mapping limitation periods or computing candidate
procedural deadlines for Australian civil litigation. Every output of every
workflow is provisional until the responsible lawyer confirms it. Nothing in
this plugin is a diary, court-list or practice-management system, and no
output may be framed as one.

Treat these as separate workflows and route to them rather than duplicating
their depth:

- point-in-time verification of Acts — Limitation Acts, Interpretation
  Acts, tribunal enabling Acts — belongs to the Australian Legal Research
  plugin (`$check-commonwealth-legislation`, `$check-nsw-legislation`,
  `$check-victoria-legislation` and the other jurisdiction checkers);
- court rules are excluded from that plugin by design, so their
  verification follows the court-rules method in this document; and
- criminal procedure, foreign limitation law and cross-border
  choice-of-law questions are flagged `OUTSIDE SCOPE`, never assessed.

## The script-only arithmetic rule

The model never performs date arithmetic. Every computed date comes from the
bundled `compute_deadline.py` script, which reads the JSON computation-rule
tables and holiday tables in `references/` and nothing else. The script
refuses to compute — returning identify-only output that names the governing
rule — whenever:

1. the period rule or any computation provision it relies on is not in the
   `verified` evidence state;
2. the computation needs a holiday table that is unverified, does not cover
   the computed range, or has an uncertain window intersecting it; or
3. the period cannot be expressed by the table — court-fixed dates,
   "as soon as practicable", backwards-counted periods and any unit the
   script does not support.

A refusal is a correct result, not an error. Never re-derive a refused date
by hand, and never present model arithmetic as a computed date.

## Snapshot of the framework

At 14 August 2026 — a research snapshot, not a cached rule; every live
workflow must recheck each source:

1. **Limitation statutes** — each jurisdiction has its own Limitation Act
   with distinct general periods, postponement regimes and special regimes
   (child-abuse no-limitation reforms, defamation single-publication rules,
   personal-injury schemes, contribution claims). The limitation registry in
   `map-limitation-periods` records candidates only.
2. **Court rules** — Federal Court Rules 2011 (Cth), High Court Rules 2004
   (Cth), Uniform Civil Procedure Rules 2005 (NSW), Supreme Court (General
   Civil Procedure) Rules 2015 (Vic) and their counterparts are statutory
   instruments published on the official legislation sites. Time-computation
   provisions also sit in each jurisdiction's Interpretation Act.
3. **Tribunals** — review periods sit in enabling Acts (Administrative
   Review Tribunal Act 2024 (Cth), Civil and Administrative Tribunal Act
   2013 (NSW), Victorian Civil and Administrative Tribunal Act 1998 (Vic))
   and in the Acts conferring the reviewable decision. Migration deadlines
   include non-extendable and jurisdictional periods.
4. **Holidays** — NSW and Victorian public-holiday tables are verified
   against the official government publications recorded in each table.
   Local public holidays, non-metropolitan arrangements and
   not-yet-declared dates are recorded as caveats or uncertain windows.

## Source hierarchy

1. Verify Acts through the Australian Legal Research plugin at the
   assessment date. A section number or period in this plugin's registries
   is a routing lead until verified.
2. Verify court rules and tribunal procedural instruments against the
   official legislation publisher for the jurisdiction; record the version
   identifier and checked date in the rule table entry.
3. Use court and tribunal websites for practice notes, registry hours and
   filing arrangements, labelled as administrative guidance.
4. Treat commentary, firm limitation tables, search results and model
   memory as discovery material, never authority.

## Evidence states

Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and
  relevant text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a
  commencement, amendment, application or coverage qualification remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.

In the JSON tables the machine states are `verified` and
`pending-verification`; the script computes only from `verified`. The
`verify-deadline-basis` workflow is the only path that moves an entry to
`verified`, and it records source URL, version identifier, checked date and
a table fingerprint when it does.

## Profile precedence

Use the approved profile only as a controlled factual map of the practice
(jurisdictions, forums, named confirmer, diary system of record). It cannot
establish that a period applies and cannot excuse a missed date. If profile
content conflicts with a verified source, surface the conflict and stop the
affected conclusion. The model may draft a profile but cannot mark it
approved.

## Human control

The workflows may organise evidence, map candidate periods, run the
computation script and prepare registers. They do not determine when a
cause of action accrued, when a fact became discoverable, whether an
extension would be granted, or which single date binds. Accrual and
discoverability are lawyer-supplied inputs recorded as assumptions. The
named confirmer must confirm every date before reliance, and every output
restates that the plugin is not the practice's diary or system of record.
