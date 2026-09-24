# Currency audit — 24 September 2026

Scope: all eleven plugins and sixty-one skills, 29 days after the 26 August
2026 sweep (`lawCheckedOn` 2026-08-26 everywhere).

## Method and limits

- The completion gate passes: `validate_repository.py`,
  `generate_registry.py --check`, 171 unit tests and `git diff --check`. No
  plugin is near the 183-day law-check limit.
- The audit environment's egress proxy blocked the official publishers
  (legislation.gov.au, AustLII, AUSTRAC, OAIC, APH, FWC, Home Affairs, state
  legislation sites). Every finding below rests on web-search results. Where
  a result came from an official domain it is marked *official (via search)*,
  but the page itself was not read.
- **Every finding is a lead to confirm against the primary source.** None of
  them justifies moving `lawCheckedOn`, which asserts a check against the
  official publishers.
- Nothing in the plugins was changed by this audit.

## Priority 1 — the law or its status has moved

| # | Plugin | Location | What moved | Confidence |
| --- | --- | --- | --- | --- |
| 1 | privacy-cybersecurity, ai-governance | `assess-australian-privacy-issues/references/current-commonwealth-privacy-map.md:33-39`; ai-gov `watch-register.json:55` | AGD released an exposure draft Privacy Amendment (Personal Data Protection) Bill 2026 on 31 Aug 2026 (consultation closed 18 Sep). Proposals include a fair-and-reasonable test, a broader definition of personal information and **72-hour** NDB notification to the Commissioner. The register still says "no Bill introduced, no timetable". This is an exposure draft only; current law is unchanged. | High (existence), medium (content) |
| 2 | aml-ctf | `track-aml-ctf-developments/references/watch-register.json`; `references/lpp-carve-outs.md:27-35` | The AML/CTF Amendment Bill 2026 (introduced 12 Mar 2026, PJCIS reported, House debate in Sep 2026) is not on the register. It would redirect LPP forms to the agency that issued the notice, not the AUSTRAC CEO, which changes the two-form mechanics described. Passage and assent status were inconclusive. | High (bill exists), low (status) |
| 3 | aml-ctf | `references/aml-ctf-source-and-control-method.md:54-55`; `lpp-carve-outs.md:66-71`; `watch-register.json:9` | The s 242A LPP guidelines are described as "announced but unreleased". Home Affairs published the Draft Legal Professional Privilege Guidelines 2026, and consultation closed 24 Jun 2026. The final version is still pending. | High |
| 4 | aml-ctf | `watch-register.json:40` | The annual compliance report is described as a calendar-2026 cycle. AUSTRAC has moved to financial years, so the first tranche 2 report appears to cover FY2026-27 and be due by 30 Sep 2027. | Medium-high |
| 5 | estate-planning | `references/nsw-execution-formalities.md:97-120`; `references/nsw-instruction-record-schema.md:74` | The NSW Guardianship Regulation 2026 (SL 2026 No 437) commenced 1 Sep 2026. It remakes Forms 1–3, adds a fifth standard function (restrictive practices consent), removes Service NSW employees as eligible witnesses and changes "major treatment". The s 6E functions checklist is now incomplete. | High (commenced), medium (detail) |
| 6 | employment-fair-work | `track-fair-work-developments/references/watch-register.json:88` | The non-compete ban exposure draft (Competition and Fair Work Legislation Amendment (Banning Unfair Non-Competes) Bill 2026) was published 7 Sep 2026, and consultation closes 2 Oct 2026. The register says "no exposure draft or Bill located", and the item id presumes a 2027 start. | High |
| 7 | employment-fair-work | `watch-register.json` (no entry) | The Clerks Award working-from-home Full Bench decision of 27 Aug 2026 proposes a right-to-request term, and the final determination is pending. It is relevant to `review-workplace-policy`. | High |
| 8 | employment-fair-work | `watch-register.json:16-17` | The Closing Loopholes statutory review final report was tabled 20 Aug 2026 but is not recorded. The next trigger is the government response. | High |
| 9 | employment-fair-work | `watch-register.json:95` | Gender-undervaluation (HPSS): Expert Panel decisions of 7 and 11 Sep 2026; Health Services Award changes apply from 1 Oct 2026. | Medium-high |
| 10 | ai-governance | `watch-register.json:9`; `references/ai-governance-source-and-control-method.md:58-61` | National Cabinet met 26 Aug 2026 and endorsed mandatory data-centre standards (the Commonwealth will legislate in early 2027). The PM&C AI-infrastructure consultation closes 9 Oct 2026. The register says the outcome is unpublished. Separately, "creator-consent" copyright is now contested by reported opt-out proposals. | High / medium |
| 11 | corporations-governance | `references/governance-source-and-control-method.md:41-43` | The Corporations Act compilation cited (C2026C00339, No 147) appears superseded from 27 Aug 2026. The replacement ID was inconclusive. | Medium |
| 12 | ai-governance, privacy-cybersecurity | ai-gov `watch-register.json:44-50`; `ai-governance-source-and-control-method.md:110-120` | Bunnings (ART, [2026] ARTA 130): no appeal, and the OAIC issued retail facial-recognition guidance on 29 Jul 2026, so the watch item can close. Bekier: the executives filed appeals on 14 Jul 2026, so the status should read appeal pending. | Medium-high |

## Priority 2 — past dates still written as future or pending

These are high-confidence and need no external source. The text only has to
be rewritten.

- privacy-cybersecurity `map-australian-cyber-incident-obligations/references/cyber-regime-registry.json:31`:
  "auto-repealed on 8 September 2026" should be past tense.
- corporations-governance `governance-source-and-control-method.md:44-50`:
  the ASX 5th edition consultation closed on 14 Sep 2026, and the APRA CPS 510
  consultation closed on 28 Aug 2026. ASX materials point to a
  recommendation to the ASX board by December 2026, while the plugin says
  "response Q1 2027". Reconcile the two.
- ai-governance `watch-register.json:28` and `track-ai-regulatory-developments/SKILL.md:3`:
  the ASX 5th edition consultation has closed.
- aml-ctf `watch-register.json:28`: the fixed 29 Jul 2026 compliance-officer
  date has passed. Only the "14 days after enrolment" limb still matters.
- aml-ctf `catalog.json:4,18` and `README.md:14`: "pending AUSTRAC guidance"
  framing now that tranche 2 is in force.
- litigation-deadlines `README.md:36,50-52` and
  `references/litigation-deadlines-source-and-control-method.md:44`: these
  still describe the 14 Aug snapshot and NSW/Vic/Qld-only holiday tables. All
  eight jurisdictions now ship, so the README contradicts itself.
- litigation-deadlines: the NSW, Vic and Qld holiday tables and seven
  court-rule tables carry `checked` 2026-08-14, older than the catalog's
  `lawCheckedOn`.

## Priority 3 — accuracy and watch-list gaps

- ai-governance `ai-governance-source-and-control-method.md:89` and
  `watch-register.json:19` say APP 1.7–1.8. The privacy plugin says
  APP 1.7–1.9, which matches the 2024 amending Act. Make the two consistent.
- litigation-deadlines `holidays/wa.json:23`: the "review under way" caveat
  should name the Public and Bank Holidays Amendment Bill 2025. Its changes
  start 1 Jan 2028; the 2026–27 dates are unaffected.
- litigation-deadlines `map-limitation-periods/references/limitation-registry.json:16`:
  the single-publication defamation rule is not in force in WA or NT.
- corporations-governance: director ID reporting through ASIC annual reviews
  starts 1 Jul 2027 (Business Registries Act 2026). The AASB, AUASB and FRC
  merge into External Reporting Australia (Financial Reporting System Reform
  Act 2026). Both are future changes the calendar skill should flag.
- privacy-cybersecurity: add SOCI tranche 2 (Home Affairs consultation closed
  31 Jul 2026) and the Children's Online Privacy Code registration deadline of
  10 Dec 2026.
- ai-governance: add the Joint Select Committee on AI (report due
  30 Nov 2026) and the Sep 2026 revision of the eSafety codes regulatory
  guidance (medium-low confidence).
- aml-ctf: the legal profession starter kit appears to have been revised
  after v1.1 (Aug–Sep 2026); content not confirmed.
- employment-fair-work `references/termination-exposure.md:42`: unlawful
  termination (s 772) is not limited to non-national-system employees.
  `framework-layers.md:25` and `policy-statutory-hooks.md:11` cite different
  section ranges for flexible work requests.
- estate-planning `assemble-qld-estate-documents/SKILL.md:67,99`: the
  "remote execution" wording, carried over from Victoria, implies an option
  Queensland does not have.

## Checked and apparently current

- AGLC4 is still the current edition; AGLC5 is unpublished.
- All eight holiday tables cover 2026–27 and match the weekday rules and
  announced dates (including NSW Anzac Day Mondays and the 2026 AFL Grand
  Final Friday). No new 2027 holidays have been gazetted.
- Vic Supreme Court Civil Procedure Rules 2025, NSW UCPR (Amendment No 107),
  FCR (11 Jun 2026 compilation) and the general limitation periods.
- 2026 Annual Wage Review figures, high income threshold ($190,100),
  compensation cap ($95,050), FWC fee ($92.70), payday super, right to
  disconnect and casual conversion.
- ADM transparency commencement (10 Dec 2026), statutory privacy tort, Cyber
  Security Act ransomware and smart-device rules, WA PRIS dates, DTA AI
  policy v2.0, mandatory AI guardrails not proceeding.
- AML/CTF tranche 2 commencement (1 Jul 2026), Rules 2025, Transitional Rules
  2026, tipping-off commencement.
- NSW, Victorian and Queensland wills and powers-of-attorney statutes, apart
  from the NSW Guardianship Regulation above.

## Recommended next steps

1. Re-run the priority 1 items against the official publishers from an
   environment that can reach them. Correct the plugins, patch-bump each
   affected plugin, and only then move `lawCheckedOn`.
2. Apply the priority 2 wording fixes. They need no external verification.
3. Triage the priority 3 gaps into watch-register additions.
