# Australian Legal Research

This plugin covers the research workflow behind Australian legal writing:
verify legislation against the official Commonwealth, State and Territory
publishers, verify case citations and quoted passages against the official
court publishers, and draft citations under the *Australian Guide to Legal
Citation*, 4th edition (AGLC4). The three capabilities share one posture —
every check fails closed when official evidence is unavailable or
incomplete, and no citation field is ever invented.

## Legislation

The legislation skills establish title identity, point-in-time version,
commencement, currency and official-source provenance. The Commonwealth
change-tracing skill also follows compilations, amendments and commencement
across a date range.

Every State and Territory checker follows the same workflow, result contract
and fail-closed rule, defined once in
[references/point-in-time-method.md](references/point-in-time-method.md). Each
checker supplies only its jurisdiction-specific facts: the official publisher,
the local timezone and the local name for a consolidated version.

- `check-commonwealth-legislation` — Federal Register of Legislation,
  point-in-time compilations and commencement.
- `trace-commonwealth-legislative-change` — compilations, amendments and
  commencement across a date range.
- `check-nsw-legislation`, `check-victoria-legislation`,
  `check-queensland-legislation`, `check-western-australia-legislation`,
  `check-south-australia-legislation`, `check-tasmania-legislation`,
  `check-act-legislation`, `check-northern-territory-legislation` — each
  jurisdiction's official publisher.

## Case law

The case-law skills exist because AI-fabricated citations are a live
professional risk, and because the free aggregators either prohibit
automated use or sit behind subscriptions. A medium-neutral citation names
its issuing court, so every check can go straight to that court's own
publisher. Every check follows the same outcome semantics, defined once in
[references/case-law-verification-method.md](references/case-law-verification-method.md):
`VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `UNVERIFIABLE` and `NOT FOUND`
are distinct results, and a citation that cannot be checked is never
reported as fabricated.

- `route-case-citation` parses medium-neutral, reported and case-name
  citations and routes each to its verification path. A bundled offline
  parser handles the citation grammar.
- `verify-hca-judgment` checks High Court citations at `hcourt.gov.au`,
  including Commonwealth Law Reports volumes 1–100.
- `verify-nsw-judgment` checks NSW court and tribunal citations on NSW
  Caselaw, preserving restriction notations and the Copyright in Judicial
  Decisions Notice 1995 conditions.
- `verify-federal-judgment` checks FCFCOA citations directly and Federal
  Court citations through a human-operated browser or an explicit manual
  path, because the Federal Court website challenges automated clients.
- `verify-case-quote` confirms a quoted passage appears in the verified
  official text and reports its paragraph location and any divergence.

## AGLC4 citation

- `format-aglc4-citations` applies AGLC4 to Australian cases and
  legislative materials, secondary sources, treaties and international
  materials, and foreign domestic sources. It builds first citations in
  full, applies `Ibid`, `(n X)` and short titles only after checking the
  citation sequence, transforms footnotes into bibliography entries under
  rule 1.13, and audits documents for element order, italics, pinpoints and
  punctuation.

The skill is an operational distillation of the published AGLC4. It
summarises rules and supplies field templates; it does not bundle or
reproduce the publication, whose copyright the Melbourne University Law
Review Association Inc and Melbourne Journal of International Law Inc
retain. Rule numbers and chapter boundaries are documented in a source map
so any answer can be checked against an authorised copy.

Formatting is not verification: a perfectly formatted citation can still
identify the wrong source, so pair the citation skill with the legislation
and case-law checks above. When AGLC4 has no rule, the skill states the
analogy it used rather than silently substituting another citation system.

## Access posture

Every skill performs targeted, user-directed lookups only — one citation,
one lookup — and never crawls, bulk-downloads or indexes a publisher. Bot
challenges are never solved or bypassed; where a publisher challenges
automated clients the skills degrade to a guided browser session or an
explicit manual check. Suppression and non-publication notations are
preserved, and family-law statutory anonymisation is respected.

## Limitations

Case-law verification covers the High Court, NSW and the federal courts;
citations for other jurisdictions return `UNVERIFIABLE` with a manual path.
Subsequent treatment (overruled, followed, distinguished) is out of scope
because no free official citator exists. The AGLC4 distillation omits
appendices A–C (law report abbreviations, medium-neutral court identifiers
and pinpoint abbreviations), so uncommon abbreviations must be verified
against an authorised complete AGLC4 copy; if the distillation conflicts
with the publication, the publication prevails. Verification confirms
existence and text, never precedential weight, interpretation or legal
advice. Bills, and final legal advice, are outside scope unless a skill
expressly states otherwise.
