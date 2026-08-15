# Changelog

This changelog records all notable repository changes.

Each plugin has an independent version. The repository does not have release
tags. The current pull request remains under **Unreleased**, even when its
plugin manifests contain their intended release versions.

## Unreleased

### Changed

- Made the evidence-states block of the four `*-source-and-control-method.md`
  documents a generated region: canonical bullet text lives in
  `scripts/generate_registry.py`, per-plugin qualification lists are declared
  as `evidenceStates` in `catalog.json`, and the migration preserved the
  current wording of every document word for word. The shared convention —
  the two status vocabularies, the generated block, the invariant sentences
  now asserted by `tests/test_plugin_structure.py` — is recorded in
  `docs/source-and-control-method-core.md`.
- Consolidated the four per-plugin copies of the structural test suite
  (expected skills, workflow/result-contract/fail-closed headings, READY
  status vocabulary, shared-method references) into one parametrized
  `tests/test_plugin_structure.py`; the per-plugin test files now carry only
  their plugin-specific legal invariants. The pinned skill sets moved with
  it: they are the guard against accidental skill-directory deletion now
  that `skills.json` is generated from the directories.
- Merged the six topic-named test files covering `australian-legal-research`
  (a fossil of the pre-merge plugin boundaries) into one
  `tests/test_australian_legal_research.py` with unchanged test classes.
- Made each plugin's `.claude-plugin/plugin.json` and a new hand-owned
  `catalog.json` the canonical registry sources, generated every other
  distribution surface from them with the new
  `scripts/generate_registry.py` (both marketplace catalogs, the
  `.codex-plugin/plugin.json` wrappers, `plugins/README.md`, the root
  README badges, counts, plugin table and install blocks, and the derived
  fields of `skills.json`), and added a `--check` drift gate to CI. New
  skills are now scaffolded into `skills.json` with an empty `source` that
  fails validation until the provenance sentence is written. Catalogs and
  the README table are now ordered alphabetically, and `plugins/README.md`
  again lists all seven plugins.
- Gave `australian-litigation-deadlines` (0.2.0) its previously missing
  ChatGPT Work interface metadata (display name, descriptions and default
  prompts) via its new `catalog.json`.

- Extended `australian-litigation-deadlines` (0.2.0) computed coverage to
  Queensland: new `qld-courts` and `qcat` computation-rule tables and a
  `qld` holiday table, all verified against legislation.qld.gov.au and the
  official Queensland Government holiday pages (checked 2026-08-14).
  Verified and computing: UCPR 1999 (Qld) r 137(1) notice of intention to
  defend (the defence attaches to it under r 139(1)(b), with SEPA and
  42-day outside-Australia displacement warnings) and r 748(a) notice of
  appeal, reckoned under the Acts Interpretation Act 1954 (Qld) s 38 —
  the UCPR has no time-reckoning rule of its own; the note to r 7 confirms
  s 38 governs through the Statutory Instruments Act 1992 s 14(1) and
  sch 1 bridge — and the QCAT Act 2009 s 33(3) general review period with
  relevant-day branches, enabling-Act displacement (s 6(7)) and the s 61(3)
  extension bar recorded as warnings. The Queensland holiday table is
  Brisbane-area based: the Royal Queensland Show day is included because
  appeals are filed at Brisbane (r 746(1)), the 96 other district show
  holidays are a caveat, and the Christmas Eve part-day holiday (6pm to
  midnight) is not counted as a non-business day. Shipped-table tests
  cover the Brisbane show-day rollover, the Christmas Eve business-day
  decision and the QCAT enabling-Act warning.

- Extended the `australian-litigation-deadlines` computation script with
  table-driven excluded-range support so Federal Court time reckoning is
  now expressible: a computation provision may declare recurring month-day
  excluded ranges (FCR r 1.61(5), 24 December to 14 January not counted)
  and a short-period threshold (r 1.61(3), periods of 5 days or less count
  business days only, so calendar-day rules at or under the threshold fail
  closed). Both FCR period rules (`fcr-defence-after-service`,
  `fcr-notice-of-appeal`) flipped to verified and now compute. Where
  rolling a last day under r 1.61(4) would enter the excluded range, the
  interaction with r 1.61(5) is legally unsettled, so the script refuses
  and refers the call to the responsible lawyer rather than choosing a
  reading. Excluded ranges combine only with calendar-day and business-day
  periods; months and years fail closed. Eight new fixtures cover periods
  spanning, inside and clear of the December-January window, the
  business-day interaction, both refusal gates and the roll-into-window
  refusal.

- Completed the initial publisher-verification pass over the
  `australian-litigation-deadlines` computation-rule tables against
  legislation.gov.au, legislation.nsw.gov.au and legislation.vic.gov.au
  (checked 2026-08-14). Verified and activated for computation: Acts
  Interpretation Act 1901 (Cth) s 36, FCR 2011 r 1.61, Interpretation Act
  1987 (NSW) s 36, UCPR r 1.11, UCPR rr 14.3(1) and 51.16(1)(c), the ART
  Rules 2024 r 5 general review period (citation corrected from the ART
  Act), Migration Act ss 477/477A, NCAT r 25(4)(c) (trigger corrected to
  the later of notification and first giving of reasons), Interpretation of
  Legislation Act 1984 (Vic) s 44 and the Victorian defence rule.
  Corrections from verification: the Supreme Court (General Civil
  Procedure) Rules 2015 (Vic) were replaced by the 2025 Rules
  (S.R. No. 85/2025) and all Victorian citations now reference the 2025
  instrument; the Victorian appearance rule stays pending because r 8.04
  fixes only minimum periods and the operative time is stated in the writ;
  the Federal Court period rules stay pending because FCR r 1.61(5)
  excludes 24 December to 14 January from the reckoning, which the script
  cannot yet express; NSW Interpretation Act s 36 is disapplied to the
  UCPR by r 1.11(5), so UCPR rules now rely on r 1.11 alone with a
  registry-closure warning; and the VCAT general 28-day review period was
  removed entirely — verification found no such period exists in the VCAT
  Act or Rules, so the enabling enactment always fixes it. Tests updated:
  verified entries must carry checked/method/version metadata, a shipped
  verified rule must compute, and shipped pending rules must still refuse.

### Added

- Added `australian-litigation-deadlines` 0.1.0 with six skills:
  `configure-litigation-deadline-profile`, `map-limitation-periods`,
  `compute-procedural-deadlines`, `map-tribunal-review-deadlines`,
  `maintain-deadline-register` and `verify-deadline-basis`. The plugin
  serves Australian legal practitioners running civil litigation. Every
  date it produces is provisional until the responsible lawyer confirms
  it, and the model never performs date arithmetic: a bundled
  deterministic script computes candidate dates from evidence-gated JSON
  computation-rule tables and refuses — returning identify-only output
  naming the governing rule — whenever an entry is unverified, a holiday
  table does not cover the computed range or intersects an uncertain
  window, or a period cannot be expressed. Rule tables ship as
  pending-verification routing leads that `verify-deadline-basis`
  activates against official publishers; NSW and Victorian holiday tables
  ship verified against the official government publications, including
  an uncertain window for the undeclared 2027 Grand Final Friday holiday.
  Limitation mapping covers all nine jurisdictions with special-regime
  flags and a conservative earliest-candidate marker; computed procedural
  coverage is staged to the federal courts, NSW, Victoria, the ART, NCAT
  and VCAT; migration outputs always carry a non-extendable and
  jurisdictional warning with a specialist-review flag. Accrual,
  discoverability and extension prospects stay with the lawyer; criminal
  procedure and foreign limitation law are excluded. Act verification
  routes to `australian-legal-research`; court rules carry their own
  source method because that plugin excludes them by design. The engine
  ships with 46 hand-derived and property fixtures covering weekend and
  holiday rollover, business-day counting across holiday clusters,
  month-end and leap-year arithmetic and every fail-closed gate.

- Added `australian-aml-ctf` 0.1.0 with five skills:
  `configure-aml-ctf-practice-profile`, `map-designated-services`,
  `review-aml-ctf-program`, `map-reporting-obligations` and
  `track-aml-ctf-developments`. The plugin serves Australian legal practices
  regulated under the tranche 2 AML/CTF reforms that commenced on
  1 July 2026. It creates a controlled practice profile, maps described
  legal services to the table 6 designated services in subsection 6(5B) of
  the amended AML/CTF Act using AUSTRAC's sufficiently-linked principles and
  the exemption carve-outs, issue-spots AML/CTF programs and
  customer-due-diligence frameworks against the Act, the AML/CTF Rules 2025
  and AUSTRAC's legal profession program starter kit, maps SMR, TTR and
  compliance-report triggers with the tipping-off offence and the
  legal-professional-privilege carve-outs and LPP-form mechanics, and checks
  a primary-source watch register on demand. Legislation verification stays
  with `australian-legal-research` and CDD-data privacy depth with
  `australian-privacy-cybersecurity` via `$skill` routing. The plugin covers
  legal practices only — other tranche 2 sectors fail closed to human
  review — and never enrols, lodges or submits anything to AUSTRAC, never
  performs customer due diligence, never concludes a matter is suspicious
  and never concludes that privilege applies.

- Added `australian-ai-governance` 0.1.0 with six skills:
  `configure-ai-governance-profile`, `map-ai-regulatory-obligations`,
  `assess-board-ai-oversight`, `check-ai-guidance-alignment`,
  `triage-government-ai-use-case` and `track-ai-regulatory-developments`. The
  plugin creates a controlled AI-governance profile, maps which Australian
  instruments currently bind an AI use case while flagging pending
  instruments — including the proposed Australian Standards for AI — as watch
  items only, issue-spots board and director-duty AI exposure, checks
  governance documentation against the AI6 guidance with the superseded
  Voluntary AI Safety Standard as detail catalogue and AS ISO/IEC 42001 as
  crosswalk, routes government AI use cases to the Commonwealth DTA policy or
  the eight state and territory assurance frameworks, and checks a
  primary-source watch register on demand. AI-privacy depth stays with
  `australian-privacy-cybersecurity` and board-process depth with
  `australian-corporations-governance` via `$skill` routing. The plugin never
  asserts pending law as in force, never certifies compliance with any
  standard and treats trackers such as policai.org as discovery indexes only.

- Added `australian-legal-research` 0.1.0, merging the `australian-legislation`
  0.2.0, `australian-case-law` 0.1.0 and `australian-legal-citation` 0.1.0
  plugins into a single research plugin with all sixteen skills unchanged.
  The three source plugins covered one workflow — verify legislation, verify
  case citations and quoted passages, cite under AGLC4 — and every skill keeps
  its name, so `$skill` cross-references from other plugins are unaffected.
  Users of the three superseded plugins should uninstall them and install
  `australian-legal-research@legal-skills` instead.

- Added `australian-corporations-governance` 0.1.0 with five skills:
  `configure-corporations-governance`, `assess-director-duties-governance`,
  `prepare-board-decision-record`, `review-corporations-governance-framework`
  and `maintain-corporations-governance-calendar`. The plugin configures a
  controlled governance profile, issue-spots decision-process risks, drafts
  board records, reviews governance frameworks and creates source-linked
  calendars for companies governed by the *Corporations Act 2001* (Cth). It
  separates ASX, APRA, ACNC and CATSI overlays, treats consultation drafts as
  non-operative, and never approves, files, executes or invents corporate action.

- Added `australian-legal-citation` 0.1.0 with one skill,
  `format-aglc4-citations`, ported from the author's private gt-skills
  workbench with firm-specific branding removed. The skill drafts, converts,
  reviews and corrects citations and bibliographies under the Australian
  Guide to Legal Citation, 4th edition, covering footnotes, pinpoints,
  subsequent references, cases, legislation, secondary sources, treaties,
  international and foreign materials, quotation treatment and citation
  audits. It ships an operational distillation with a source map recording
  provenance, chapter routing and missing appendices; it never invents a
  missing citation field and keeps formatting separate from source
  verification.

- Added `australian-case-law` 0.1.0 with five skills: `route-case-citation`,
  `verify-hca-judgment`, `verify-nsw-judgment`, `verify-federal-judgment` and
  `verify-case-quote`. The plugin verifies Australian case citations and
  quoted passages against the official court publishers, routes each citation
  by its medium-neutral court identifier, distinguishes `UNVERIFIABLE` from
  `NOT FOUND`, and never bypasses publisher bot challenges. Includes a shared
  case-law verification method reference, an offline citation parser and a
  structural and parser test suite.

- Added a shared point-in-time method reference to `australian-legislation`
  0.2.0 and gave every State and Territory checker the same full workflow,
  result contract and fail-closed sections that the Commonwealth and NSW
  checkers already had.
- Added worked examples, including a `VERIFIED WITH QUALIFICATIONS` result, to
  the Commonwealth legislation, data breach and triage skills.
- Extended repository validation to check skill descriptions, frontmatter
  form, relative links, `agents/openai.yaml` interface files, per-skill
  registry versions, plugin READMEs, and description, tag and keyword parity
  between manifests and both marketplace catalogs.
- Added a validator unit-test suite and structural tests for every
  jurisdiction checker's headings and result-contract fields.
- Added a CI Python version matrix, a ruff lint job with a pinned repository
  ruff configuration, a README badge-count check and compilation of all
  plugin helper scripts.
- Added `SECURITY.md` with a private vulnerability reporting path.

- Added `australian-legislation` 0.1.0, combining the existing Commonwealth and
  New South Wales workflows with official-source legislation checks for the
  Australian Capital Territory, Northern Territory, Queensland, South
  Australia, Tasmania, Victoria and Western Australia.
- Expanded `australian-privacy-cybersecurity` 0.3.0 with jurisdiction routing,
  a legislation-only statutory privacy tort assessment, date-gated automated
  decision transparency analysis and a Commonwealth cyber incident obligations
  matrix.
- Added current-law privacy and cybersecurity registries covering State and
  Territory privacy, health, surveillance, workplace and data breach overlays,
  together with Commonwealth sectoral cyber regimes.
- Added regression coverage for the combined legislation plugin, privacy and
  cyber registries, APP provenance controls and future-law transitions.

### Changed

- Simplified the README language and added a paste-ready Agent request for
  plugin installation.
- Recorded plugin descriptions, versions and keywords in the ChatGPT Work
  marketplace catalog so both catalogs carry the same discovery metadata.
- Documented the required `agents/openai.yaml` interface file, aligned the
  three pre-submission command checklists, and expanded the README plugin
  layout diagram.
- Documented each bundled helper script as optional and read-only, including
  which official publisher it contacts and how the skill degrades without
  command execution (`legal-triage` 0.1.1, `australian-privacy-cybersecurity`
  0.3.1).
- Restored Australian English spelling in the README.
- Strengthened APP verification so schema-valid user-supplied text cannot be
  described as authoritative without verified source provenance.
- Split APP analysis into statutory text, application perimeter, codes and
  instruments, known future amendments and OAIC guidance currency.
- Updated AI-system and data breach workflows to route concurrent privacy,
  cyber, sectoral and contractual obligations without treating case law as in
  scope.

### Removed

- Removed `scripts/check_readme_counts.py` and its CI step: the README
  badges are a generated region, so `generate_registry.py --check` already
  fails the build when they drift, and the satellite script re-ran the full
  validation a second time per CI job.
- Removed two vestigial tests (the superseded-plugin-directory tombstone and
  a single-skill duplicate of the validator's registry checks) and made the
  shipped computation-rule table count assertion derive from the shipped
  files instead of a hard-coded 8, so adding a jurisdiction no longer breaks
  an unrelated test.
- Removed the unused per-skill `version` field from `skills.json` and its
  validator check; plugin versions remain the only versioned surface.
- Removed the `australian-legislation`, `australian-case-law` and
  `australian-legal-citation` plugins, superseded by `australian-legal-research`
  0.1.0 above.

### Fixed

- Made the legal triage test fixture independent of the caller's home directory
  so repository validation is deterministic in CI.

## 2026-08-14 - Initial repository

### Added

- Created the provider-neutral Legal Skills marketplace for Claude Cowork and
  ChatGPT Work, with paired plugin manifests, a portable skill registry and
  offline repository validation.
- Added Commonwealth legislation verification and legislative change tracing.
- Added New South Wales legislation verification.
- Added governed community legal centre triage workflows.
- Added the initial Australian privacy, APP, data breach and AI use-case
  assessment workflows.
