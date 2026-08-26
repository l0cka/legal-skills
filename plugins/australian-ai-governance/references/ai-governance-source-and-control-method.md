# Australian AI governance source and control method

## Scope

Use this method for Australian organisations and government agencies adopting,
governing or monitoring artificial intelligence. Australia has no economy-wide
AI Act. The obligations that bind an organisation come from existing law
(privacy, corporations, consumer, online-safety, sector regulation), from
government-use policies where the organisation is a public entity, and from
voluntary guidance that regulators increasingly treat as the benchmark of
reasonable practice. Never present voluntary guidance, a proposal or a draft as
binding law.

Treat these as separate workflows and route to them rather than duplicating
their depth:

- privacy, automated-decision transparency and AI use-case privacy assessment
  belong to the Australian Privacy Cybersecurity plugin
  (`$assess-ai-privacy-cybersecurity-use-case`,
  `$assess-automated-decision-transparency`);
- general director-duty and board-process assessment belongs to the Australian
  Corporations Governance plugin (`$assess-director-duties-governance`); and
- court generative-AI practice directions belong to a litigation workflow and
  are outside this plugin.

## The current-versus-superseded framework map

Label the layer of every framework proposition. At 14 August 2026 — a research
snapshot, not a cached rule; every live workflow must recheck each source:

1. **Guidance for AI Adoption ("AI6")** — National AI Centre / DISR, published
   21 October 2025 and restructured into *foundations* and *implementation*
   tiers (implementation PDF dated 5 May 2026). The primary voluntary
   guidance: six essential practices
   (accountability; stakeholder engagement and redress; risk management;
   transparency, including an AI register; testing and monitoring; human
   oversight and decommissioning). Verify the current text at
   <https://www.ai.gov.au/staying-safe-and-responsible/essential-ai-practices/guidance-ai-adoption-implementation-guidance>
   and
   <https://www.ai.gov.au/staying-safe-and-responsible/essential-ai-practices/guidance-ai-adoption-foundations>.
2. **Voluntary AI Safety Standard (VAISS)** — DISR, September 2024, updated
   December 2025. Superseded as primary guidance by AI6 but still published as
   the detailed 10-guardrail control catalogue at
   <https://www.industry.gov.au/publications/voluntary-ai-safety-standard>.
   Any reference to "the 10 guardrails" must state this layering.
3. **AS ISO/IEC 42001:2023** — the certifiable AI management-system standard,
   published by Standards Australia on 16 February 2024 as an identical
   adoption of ISO/IEC 42001:2023
   (<https://store.standards.org.au/product/as-iso-iec-42001-2023>); AI6 and
   VAISS are designed
   to interoperate with it. ISO/IEC 23894:2023 (AI risk management) exists
   internationally; its adoption as an AS-badged standard is unconfirmed.
4. **National AI Plan** — DISR, 2 December 2025: existing law plus sector
   regulators plus an AI Safety Institute; no standalone AI Act.
   <https://www.industry.gov.au/publications/national-ai-plan>.
5. **Proposed "Australian Standards for AI"** — announced by the Prime
   Minister on 15 July 2026 with an Office of AI in PM&C; legislation targeted
   for early 2027. Confirmed scope so far is limited: mandatory requirements
   for large AI data centres (energy, water, siting) and creator-consent
   copyright protections. National Cabinet's August 2026 consideration was
   unresolved at the snapshot date. This is a proposal, never current law.
   <https://www.pmc.gov.au/domestic-policy/office-ai>.
6. **Mandatory guardrails for high-risk AI proposals paper** — DISR, September
   2024. Consulted on but not proceeded with; historical context only.

## Source hierarchy

1. Verify Commonwealth legislation and commencement with
   `$check-commonwealth-legislation`; verify state and territory legislation
   with the corresponding `$check-*-legislation` skill. A section number or a
   date in this plugin is a routing lead until verified.
2. Verify case law through `$route-case-citation` and the official-court
   verifiers. Citation existence does not establish treatment or application.
3. Use regulator publications (OAIC, ASIC, APRA, ACCC, eSafety, TGA, AHRC) as
   regulator expectations, labelled as guidance and never restated as statute.
4. Use government AI policy documents (DTA, state and territory frameworks)
   as binding administrative policy only for the entities they cover.
5. Use organisation-supplied, version-identified AI policies, registers,
   assessments and board records for internal controls.
6. Treat commentary, law-firm insights, trackers such as policai.org, search
   results and model memory as discovery material, never authority.

## Regulator and instrument starting points

Currency and application must be checked at use time:

- OAIC AI guidance (developing and training generative AI models; commercial
  AI products): <https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies>;
- automated-decision transparency (APP 1.7–1.8, commencing 10 December 2026)
  is asserted, with its verify-at-use instruction, in the Australian Privacy
  Cybersecurity plugin's automated-decision method reference — defer to it;
- ASIC REP 798 (October 2024) governance-gap review:
  <https://www.asic.gov.au/regulatory-resources/find-a-document/reports/rep-798-beware-the-gap-governance-arrangements-in-the-face-of-ai-innovation/>;
- APRA letter to industry on AI (April 2026), layered on CPS 220/230/234:
  <https://www.apra.gov.au/apra-letter-to-industry-on-artificial-intelligence-ai>;
- eSafety Online Safety Codes and Standards — Phase 2 Age-Restricted Material
  Codes: three in effect from 27 December 2025, six from 9 March 2026;
  Regulatory Guidance updated April 2026: <https://www.esafety.gov.au/industry/codes>;
- DTA Policy for the Responsible Use of AI in Government v2.0 (mandatory for
  non-corporate Commonwealth entities; v2.0 effective 15 December 2025 with
  staged per-requirement deadlines — verify the specific deadline at use):
  <https://www.digital.gov.au/ai/ai-in-government-policy>;
- Australia's AI Ethics Principles (2019):
  <https://www.industry.gov.au/publications/australias-ai-ethics-principles>; and
- EU AI Act extraterritorial exposure for outputs affecting EU persons — flag
  for specialist review; this plugin does not assess EU law.

## Board and case-law leads

- *ASIC v Bekier (Liability Judgment)* [2026] FCA 196 (5 March 2026) is the
  first Australian judgment treating directors' use of AI: use should be
  controlled and transparent, governed by formally adopted board policies, and
  cannot displace the director's own judgment. It is a first-instance Federal
  Court judgment; verify status and any appeal before relying on it.
- The facial-recognition line — *Clearview AI* [2021] AICmr 54 (14 October
  2021); *Bunnings* (OAIC determination 29 October 2024, varied on review by
  the Administrative Review Tribunal on 4 February 2026, which affirmed the
  APP 1 and APP 5 findings but set aside the APP 3.3 finding under the s 16A
  "permitted general situation"; locate the neutral citation on AustLII before
  formal citation); *Kmart* [2025] AICmr 155 (18 September 2025, under ART
  review) — is unsettled. Present it as live doctrine, never as final.
- AICD/Human Technology Institute *Director's Guide to AI Governance* V2
  (2026) and the Governance Institute's agentic-AI paper (May 2026) are
  professional-body guidance, not law.
- ss 180–190 of the *Corporations Act 2001* (Cth) are routing leads for board
  AI oversight (s 189 permits reliance on "persons", not AI systems); verify
  through `$check-commonwealth-legislation` and route board-process depth to
  `$assess-director-duties-governance`.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  supersession, application or document-status qualification remains;
- `NOT VERIFIED` — the official source, applicable version or decisive fact
  could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

Give each finding its source URL or document identifier, version or effective
date, relevant provision or practice, checked date and evidence state. Record
every pending instrument as a watch item with its expected trigger, never as
an obligation.

## AI governance profile precedence

Use the approved profile only as a controlled factual map of the organisation
(sector, overlays, government track, EU footprint, AI inventory maturity,
governing documents). It cannot establish that an instrument applies or excuse
non-compliance. If profile content conflicts with a verified source, surface
the conflict and stop the affected conclusion. The model may draft a profile
but cannot mark it approved.

## Human control

The workflows may organise evidence, map obligations, identify gaps and
prepare drafts. They do not determine legal compliance, breach, board
effectiveness or certification against any standard. A responsible lawyer,
company secretary, privacy officer or other authorised reviewer must confirm
entity classification, source application, material facts and next action.
