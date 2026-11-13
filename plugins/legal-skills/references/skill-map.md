<!-- GENERATED FILE - do not edit. Built from each SKILL.md description by
     scripts/generate_registry.py -->

# Skill map

Every skill the router may name, grouped by practice area. The description
is the skill's own trigger text: what it does, when to use it and when not to.

## Getting Started (`getting-started`)

- **`setup`** — Set up Legal Skills for a practice. Asks role, jurisdictions and practice areas, drafts the profiles those areas need from the starter profiles, and saves them where you choose. Run by typing it; never approves a profile.
- **`start`** — Start work on a matter. Plans which Legal Skills to run in order with the human decision at each step, then runs one step at a time with your go-ahead. Run by typing it with the facts; never answers the legal question itself.
- **`check-citations`** — Check every case citation, legislation reference and quoted passage in a draft against the official publishers and return one status table. Run by typing it with the draft; never marks a reference verified itself.
- **`help`** — Show what Legal Skills covers, the practice areas, what to type for common tasks and which profiles this session has. Run by typing it; gives no legal advice.

## Australian AI Governance (`ai-governance`)

- **`assess-board-ai-oversight`** — Board and director-duty exposure from AI under the Corporations Act. Use for board AI policies and AI-assisted board packs. For general duties use `$assess-director-duties-governance`. Never concludes breach or compliance.
- **`check-ai-guidance-alignment`** — Assess AI governance documents against Australian voluntary guidance (AI Adoption, Voluntary AI Safety Standard, ISO/IEC 42001). Use for gap assessments. For binding law use `$map-ai-regulatory-obligations`. Never certifies or concludes compliance.
- **`configure-ai-governance-profile`** — Set up or update the AI-governance profile (entity type, sector, governing documents) the AI skills run against. Use for first setup or changes. For all-area setup use `$setup`. Never approves the profile.
- **`map-ai-regulatory-obligations`** — Which Australian instruments bind a described AI use case; pending ones are watch items. Use for AI adoption and procurement. For privacy depth use `$assess-ai-privacy-cybersecurity-use-case`. Not for the EU AI Act.
- **`track-ai-regulatory-developments`** — What changed on the Australian AI regulatory watch list, checked on demand against primary sources. Use for horizon reviews. For current duties use `$map-ai-regulatory-obligations`. Never treats a pending instrument as law.
- **`triage-government-ai-use-case`** — Route a government AI use case to its assurance track - Commonwealth DTA policy or a state or territory framework. Use for government AI adoption. For private-sector duties use `$map-ai-regulatory-obligations`.

## Australian AML/CTF (`aml-ctf`)

- **`configure-aml-ctf-practice-profile`** — Set up or update the tranche 2 AML/CTF practice profile for a legal practice. Use first. To test a service use `$map-designated-services`. Never decides whether a service is designated or approves the profile.
- **`map-designated-services`** — Whether an Australian legal practice's services are designated services under AML/CTF tranche 2. Use when a service line may trigger obligations. For reports use `$map-reporting-obligations`. Never decides enrolment.
- **`map-reporting-obligations`** — Which AML/CTF reports a legal practice may need, incl. suspicious matter reports, tipping-off and privilege. Use for scenarios. For coverage use `$map-designated-services`. Never decides a matter is suspicious or drafts a report.
- **`review-aml-ctf-program`** — Issue-spot a legal practice's AML/CTF program, risk assessment, policies, governance and CDD design. Use for gap reviews. For service coverage use `$map-designated-services`. Never certifies compliance.
- **`track-aml-ctf-developments`** — AML/CTF watch register checked on demand - what changed, is pending or now binds. Use for horizon reviews. For program gaps use `$review-aml-ctf-program`. Never treats a pending instrument as in force.

## Australian Commercial Drafting (`commercial-drafting`)

- **`configure-drafting-profile`** — Set up or update the profile for first-draft Australian commercial documents (party, state, house style, positions). Use before drafting. For review positions use `$configure-review-playbook`. Never approves the profile.
- **`draft-nda`** — Prepare a first-draft mutual or one-way Australian NDA for lawyer review. Use when an NDA must be drafted. To triage a received NDA use `$triage-inbound-nda`. Never approves execution.
- **`draft-privacy-policy`** — Draft a private-sector privacy policy from evidenced data practices, with an APP 1.4 map. Use for policies. For issues use `$assess-australian-privacy-issues`. Never invents data practices or publishes the policy.
- **`draft-services-agreement`** — Draft a B2B services or contractor agreement and SOW for lawyer review. Use for a first draft. For classification use `$assess-employee-vs-contractor`. Never approves execution.
- **`draft-website-terms`** — Prepare first-draft Australian SaaS or subscription website terms for consumers and small businesses. Use when drafting terms. To screen clauses use `$check-unfair-contract-terms`. Never publishes.
- **`review-draft-against-checklist`** — Review a commercial draft for missing clauses, undefined terms, broken references and UCT risk. Use for our own drafts. For a counterparty draft use `$review-commercial-agreement`. Never certifies enforceability.

## Australian Consumer & Competition (`consumer-competition`)

- **`assess-cartel-and-rpm-risk`** — Issue-spot Australian cartel, RPM, exclusive dealing and market-power risk. Use for competitor contacts, distribution restraints and pricing pressure. For mergers use `$map-merger-notification`. Never concludes an offence occurred.
- **`assess-consumer-guarantees`** — Australian Consumer Law guarantees, remedies and warranty documents. Use for defects, failed services and refund disputes. For unsafe goods use `$map-product-safety-obligations`. Never decides entitlement.
- **`configure-consumer-competition-profile`** — Set up or validate the business profile the consumer and competition skills run against. Use for scope and approval controls. For all-area setup use `$setup`. Never approves the profile.
- **`map-merger-notification`** — Mandatory merger notification thresholds, exemptions and waivers from transaction evidence. Use before signing or completion. For cartels use `$assess-cartel-and-rpm-risk`. Never lodges an application or approves closing.
- **`map-product-safety-obligations`** — Australian product safety standards, bans, recalls and mandatory reporting. Use for supply checks, injury reports and recall planning. For guarantee remedies use `$assess-consumer-guarantees`. Never executes a recall or files a report.
- **`review-marketing-claims`** — Review marketing, environmental, comparative and pricing claims, incl. drip pricing. Use before a campaign. For terms use `$check-unfair-contract-terms`. Never certifies claims or publishes advertisements.
- **`track-accc-developments`** — ACCC watch register checked on demand for changed merger, consumer, competition and safety positions. Use for horizon reviews. For current duties use `$map-merger-notification`. Not an unattended monitor.

## Australian Contract Review (`contract-review`)

- **`build-negotiation-redline-memo`** — Draft a negotiation memo - current text, proposed text, rationale and fallbacks per clause. Use after a contract review. To review use `$review-commercial-agreement`. Never sends the memo or alters a live document.
- **`check-unfair-contract-terms`** — Screen contract terms for unfair-contract-terms risk under the ACL or ASIC Act. Use for consumer and small-business standard forms. For whole contracts use `$review-commercial-agreement`. Never declares a term invalid.
- **`configure-review-playbook`** — Set up or update a contract-review playbook of positions, fallbacks and approval thresholds. Use before inbound review. For drafting use `$configure-drafting-profile`. Never invents firm positions or approves the playbook.
- **`review-commercial-agreement`** — Review an Australian MSA, SaaS, supply or services agreement against approved positions. Use for inbound contracts. For NDAs use `$triage-inbound-nda`. Never silently rewrites or approves execution.
- **`review-limitation-and-indemnity-regime`** — Review caps, exclusions, indemnities, insurance and proportionate liability in a contract. Use for risk allocation. For a full review use `$review-commercial-agreement`. Never assumes contracting out is permitted.
- **`track-contract-renewals`** — Register of contract renewal and notice dates and auto-renewal risks. Use for a portfolio or impending renewal. For litigation dates use `$maintain-deadline-register`. Never sends notices or updates live diaries.
- **`triage-inbound-nda`** — Triage a received Australian NDA as green, yellow or red against a playbook. Use for inbound NDAs. To draft an NDA use `$draft-nda`. Never clears execution or certifies enforceability.

## Australian Corporations Governance (`corporations-governance`)

- **`assess-director-duties-governance`** — Issue-spot director and officer duty risks for a company decision. Use for authority, care, reliance, conflicts and solvency. For WHS use `$assess-officer-due-diligence`. Never concludes breach, validity or solvency.
- **`configure-corporations-governance`** — Set up or update an Australian company's governance profile (entity type, documents, board authority, delegations). Use before other governance skills. For all-area setup use `$setup`. Never approves the profile.
- **`maintain-corporations-governance-calendar`** — Source-linked governance calendar for an Australian company - meetings, records, notifications and reporting. Use to create or update it. For litigation dates use `$maintain-deadline-register`. Never submits filings or sends notices.
- **`prepare-board-decision-record`** — Draft board papers, resolutions or minutes extracts from verified law and evidence. Use for a decision. For duties use `$assess-director-duties-governance`. Never invents attendance, votes or reasons, and never circulates documents.
- **`review-corporations-governance-framework`** — Review a company's governance framework against Corporations Act requirements. Use for authority, delegations, conflicts and records. For a decision use `$assess-director-duties-governance`. Never certifies compliance.

## Australian Employment & Fair Work (`employment-fair-work`)

- **`assess-discrimination-and-positive-duty`** — Map discrimination and positive-duty exposure under Commonwealth, NSW, Vic and Qld law. Use for incident reviews. For psychosocial use `$review-psychosocial-risk-controls`. Never determines liability or certifies compliance.
- **`assess-employee-vs-contractor`** — Issue-spot employee or contractor classification and sham contracting under the Fair Work Act. Use before engaging contractors. To draft use `$draft-services-agreement`. Never classifies conclusively from an ABN or label.
- **`assess-restraint-of-trade`** — Issue-spot employment restraints under common law, NSW legislation and non-compete reforms. Use for exit or clause reviews. For other terms use `$review-employment-contract`. Never certifies enforceability.
- **`assess-termination-exposure`** — Issue-spot dismissal or redundancy exposure - unfair dismissal, general protections, notice. Use before a dismissal or when a claim is threatened. For pay use `$map-fair-work-obligations`. Never concludes a dismissal was unfair.
- **`compute-underpayment-exposure-framework`** — Underpayment exposure framework from entitlements, payroll evidence and limitation leads. Use for wage reviews. For entitlements use `$map-fair-work-obligations`. Never invents award rates or computes a final liability.
- **`configure-employment-profile`** — Set up or update the employer profile the Fair Work skills run against (coverage, size, awards, agreements). Use before other employment workflows. For all-area setup use `$setup`. Never decides coverage or approves the profile.
- **`map-fair-work-obligations`** — Which Fair Work Act, NES, award and agreement provisions apply to an employment arrangement. Use for onboarding and entitlement queries. To review a contract use `$review-employment-contract`. Never concludes award coverage or calculates pay.
- **`review-employment-contract`** — Review an Australian employment contract against the NES, award coverage, set-off, IP, termination and fixed-term limits. Use for onboarding. For restraints use `$assess-restraint-of-trade`. Never certifies compliance.
- **`review-workplace-policy`** — Review workplace policies against Fair Work Act hooks - right to disconnect, flexible work, leave, delegates' rights. Use for policy refreshes. For contracts use `$review-employment-contract`. Never certifies compliance or drafts policy text.
- **`track-fair-work-developments`** — Fair Work watch register checked on demand, incl. the Annual Wage Review and indexed thresholds. Use for horizon reviews. For duties use `$map-fair-work-obligations`. Never treats a pending instrument as law.

## Australian Estate Planning (`estate-planning`)

- **`assemble-nsw-estate-documents`** — Draft a NSW will, enduring power of attorney and guardianship from approved precedents. Use for solicitor-led matters. For Queensland use `$assemble-qld-estate-documents`. Not for trusts or probate.
- **`assemble-qld-estate-documents`** — Draft a Queensland will and enduring power of attorney from approved precedents. Use for solicitor-led matters. For NSW use `$assemble-nsw-estate-documents`. Not for trusts or probate.
- **`assemble-vic-estate-documents`** — Draft a Victorian will, enduring power of attorney and medical treatment decision maker from approved precedents. Use for solicitor-led matters. For NSW use `$assemble-nsw-estate-documents`. Not for trusts or probate.

## Australian Legal Research (`legal-research`)

- **`check-act-legislation`** — Verify ACT legislation at the official ACT legislation register - in force, version on a date, citation match. Use for ACT law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-commonwealth-legislation`** — Verify Commonwealth Acts and instruments on the Federal Register of Legislation - in force, compilation on a date, citation match. Use for Commonwealth law. For changes over time use `$trace-commonwealth-legislative-change`.
- **`check-court-ai-protocol`** — Which Australian court or tribunal generative AI practice note applies to a document being filed, what it bans and what disclosure it needs. Use before filing AI-assisted evidence or submissions. For AI governance documents use `$check-ai-guidance-alignment`.
- **`check-northern-territory-legislation`** — Verify Northern Territory legislation at the official NT legislation database - in force, version on a date, citation match. Use for Northern Territory law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-nsw-legislation`** — Verify NSW legislation at the official NSW legislation website - in force, version on a date, citation match. Use for NSW law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-queensland-legislation`** — Verify Queensland legislation at the official Queensland legislation publisher - in force, version on a date, citation match. Use for Queensland law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-south-australia-legislation`** — Verify South Australian legislation at the official SA legislation publisher - in force, version on a date, citation match. Use for South Australian law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-tasmania-legislation`** — Verify Tasmanian legislation at the official Tasmanian legislation publisher - in force, version on a date, citation match. Use for Tasmanian law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-victoria-legislation`** — Verify Victorian legislation at the official Victorian legislation publisher - in force, version on a date, citation match. Use for Victorian law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`check-western-australia-legislation`** — Verify Western Australian legislation at the official WA legislation publisher - in force, version on a date, citation match. Use for Western Australian law. For Commonwealth law use `$check-commonwealth-legislation`.
- **`format-aglc4-citations`** — Draft, convert and correct Australian legal citations and bibliographies in AGLC4. Use for footnotes, pinpoints and citation audits. To verify that a source exists use `$check-citations`. Does not verify sources.
- **`route-case-citation`** — Use first to verify any Australian case citation, judgment or authority, including possibly fabricated ones. Identifies the court and routes to the verifier. For quotes use `$verify-case-quote`. Not for case treatment or foreign citations.
- **`trace-commonwealth-legislative-change`** — Trace what changed in a Commonwealth provision between two dates, which amendment and when commenced. Use for amendment history. For one date use `$check-commonwealth-legislation`. Not for Bills or State law.
- **`verify-case-quote`** — Verify a passage quoted from an Australian judgment appears in the decision at the official publisher, with its paragraph. Use after verifying the citation. For the citation use `$route-case-citation`. Not for paraphrase or interpretation.
- **`verify-federal-judgment`** — Verify a Federal Court or FCFCOA decision exists at the official publisher - FCA, FCAFC, FedCFamC, FCCA, FamCA, FCR citations. Use via `$route-case-citation`. For High Court use `$verify-hca-judgment`. Not for case treatment.
- **`verify-hca-judgment`** — Verify a High Court decision exists at the High Court website - HCA, CLR, ALJR citations. Use via `$route-case-citation` or for a known one. For Federal Court use `$verify-federal-judgment`. Not for case treatment.
- **`verify-nsw-judgment`** — Verify a NSW court or tribunal decision exists on NSW Caselaw - NSW citations and NSWLR. Use via `$route-case-citation` or for a known one. For Queensland use `$verify-qld-judgment`. Not for case treatment.
- **`verify-qld-judgment`** — Verify a Queensland court or tribunal decision exists at the Queensland Judgments website - Queensland citations and Qd R. Use via `$route-case-citation` or for a known one. For NSW use `$verify-nsw-judgment`. Not for case treatment.

## Australian Litigation Deadlines (`litigation-deadlines`)

- **`compute-procedural-deadlines`** — Compute candidate civil court deadlines from a lawyer-supplied trigger date, never by model arithmetic. Use for defences, appeals and rule-fixed steps. For limitation use `$map-limitation-periods`. Not for criminal or contested triggers.
- **`configure-litigation-deadline-profile`** — Set up or update the litigation-deadlines practice profile (forums, named confirmer, diary system). Use before first use. To compute use `$compute-procedural-deadlines`. Never computes a date or approves the profile.
- **`maintain-deadline-register`** — Deadline register for one civil litigation matter - each entry's rule, trigger and confirmation status. Use to track a matter's dates. To compute use `$compute-procedural-deadlines`. Never confirms a date.
- **`map-limitation-periods`** — Map a civil cause of action to candidate limitation periods across jurisdictions, flagging extensions. Use for time-to-sue questions. For court steps use `$compute-procedural-deadlines`. Never determines accrual or picks a binding date.
- **`map-tribunal-review-deadlines`** — Candidate merits-review and tribunal deadlines (ART, NCAT, QCAT, VCAT), never by model arithmetic. Use after a government or tribunal decision. For court steps use `$compute-procedural-deadlines`. Never concludes a period has expired.
- **`verify-deadline-basis`** — Verify the court-rule and public-holiday tables behind the deadline skills against official publishers. Use before first reliance or on rule changes. To compute use `$compute-procedural-deadlines`. Never computes dates.

## Australian Privacy & Cybersecurity (`privacy-cybersecurity`)

- **`assess-ai-privacy-cybersecurity-use-case`** — Assess an AI use case for privacy and cybersecurity suitability - data flows, harms, vendors, controls. Use for AI intake, procurement, pilots and PIAs. For AI duties use `$map-ai-regulatory-obligations`.
- **`assess-australian-data-breach`** — Triage a suspected Australian data breach or cyber incident for lawyers, mapping breach regimes, reporting clocks and an action matrix. Use for unauthorised access, ransomware and vendor incidents. Never decides whether to notify.
- **`assess-australian-privacy-issues`** — Spot and structure Australian privacy and data protection issues from facts, contracts, policies or data maps into a source-linked issue matrix. Use for privacy scoping and applicability. Not for case law or final opinions.
- **`assess-automated-decision-transparency`** — Privacy transparency duties for automated and AI-assisted decisions, incl. APP 1.7 to 1.9 from 10 December 2026 and WA PRIS. Use for decision inventories. For discrimination use `$assess-discrimination-and-positive-duty`.
- **`assess-statutory-privacy-tort`** — Screen facts against the Privacy Act statutory tort for serious privacy invasions. Use for surveillance, recording, scraping, deepfakes and intimate, health or location disclosure. For other privacy use `$assess-australian-privacy-issues`.
- **`check-australian-privacy-principles`** — Verify the Australian Privacy Principles, coverage, exemptions, codes and pending amendments from official sources. Use whenever a workflow relies on an APP or reuses an earlier APP analysis. No case law.
- **`map-australian-cyber-incident-obligations`** — Map concurrent Australian cyber incident, data breach, ransomware payment, critical infrastructure and sector reporting duties by entity, trigger, recipient and clock. For full incident triage use assess-australian-data-breach.
- **`route-australian-privacy-jurisdiction`** — Route Australian privacy, health information, data breach, surveillance and workplace monitoring issues to the Commonwealth, State and Territory regimes that may apply. Use before substantive privacy or breach analysis.

## Australian Work Health & Safety (`work-health-safety`)

- **`assess-notifiable-incident`** — Urgent preliminary assessment of an Australian workplace incident, covering candidate notifiable incident, who notifies which regulator, how fast, and site preservation. Use straight after an incident. Never decides whether to notify.
- **`assess-officer-due-diligence`** — Review evidence of officers' WHS due diligence, element by element, with gaps and board questions. Use for board WHS reviews. For a fresh incident use `$assess-notifiable-incident`. Never concludes due diligence was met.
- **`map-whs-duties`** — Who holds which WHS duties on a worksite or contractor arrangement under the model WHS Act or Victoria's OHS Act. Use for multi-party sites. For officers use `$assess-officer-due-diligence`. Never concludes a breach.
- **`review-psychosocial-risk-controls`** — Gap-check psychosocial risk management against the WHS regulations and code of practice. Use for risk-register reviews. For discrimination use `$assess-discrimination-and-positive-duty`. Never certifies compliance or investigates a complaint.
- **`track-whs-developments`** — WHS watch register checked on demand, incl. each jurisdiction's adoption of model WHS law changes. Use for horizon reviews. For duties use `$map-whs-duties`. Never treats a Bill or draft code as law in force.

## Legal Evidence Workflows (`evidence-workflows`)

- **`build-document-index`** — Source-linked, numbered document index as a Word file from matter documents, for court books. Use for litigation and disclosure. For dated events use `$build-evidence-chronology`. Never decides relevance, privilege or admissibility.
- **`build-evidence-chronology`** — Source-linked evidence chronology as a Word file, keeping exact date wording, conflicts and gaps. Use for litigation and disputes. For an index use `$build-document-index`. Never decides credibility, weight or merits.
- **`build-privilege-log`** — Draft a privilege log as a Word file, one row per document with claimed basis and waiver flags. Use for discovery, subpoenas and regulatory productions. For an index use `$build-document-index`. Never decides that privilege exists or is lost.
- **`map-evidence-inconsistencies`** — Where matter documents and accounts agree, diverge or are silent on each fact, as a Word file. Use for witness preparation and cross-examination. For the chronology use `$build-evidence-chronology`. Never decides which account is right.

## Legal Triage (`triage`)

- **`configure-legal-triage`** — Set up or update a community legal centre's triage profile (scope, urgency pathways, eligibility, referrals). Use before legal triage. To triage use `$triage-legal-enquiry`. Never invents centre policy or approves the profile.
- **`triage-legal-enquiry`** — Provisional triage record for a community legal centre enquiry under its approved profile - urgency, issue, referral. Use by authorised staff. For skill routing use `$route-legal-fact-pattern`. Not a public chatbot and never gives legal advice.

## Legal Cognitive Sparring (`cognitive-sparring`)

- **`clarify-burden-and-standard`** — Sparring for a qualified lawyer. State who bears which burden, under what standard, and what evidence would meet it on the supplied facts. Never invents a standard or decides the burden is met.
- **`drill-oral-advocacy`** — Sparring for a qualified lawyer. Run a hostile question-and-answer or opening and closing drill on a named issue and score clarity, concessions and recovery. Never invents transcript authority or predicts the ruling.
- **`find-blind-spots`** — Sparring for a qualified lawyer. List the questions, facts, parties, procedures and authorities not yet addressed, split into must-check and nice-to-have. Never invents the missing authority or decides the point.
- **`map-assumptions`** — Sparring for a qualified lawyer. Extract the explicit and hidden assumptions in an analysis, rank the ones the case turns on and propose how to test each. Never fills a gap from memory.
- **`oppose-as-counsel`** — Sparring for a qualified lawyer. Argue the other side with the strongest counters the lawyer must answer, labelling speculation. Never advises the opposing party or invents a citation.
- **`pressure-test-argument`** — Sparring for a qualified lawyer. Stress-test the lawyer's own argument for weak premises, leaps, missing authorities and adverse facts. Never gives final advice or invents a citation.
- **`pressure-test-strategy`** — Sparring for a qualified lawyer. Challenge procedural and commercial strategy, including forum, timing, settlement bands and escalation, for unstated risks. Never files or contacts a counterparty.
- **`red-team-evidence`** — Sparring for a qualified lawyer. Challenge the evidence behind a position on provenance, hearsay, weight and gaps an opponent would attack. Never decides admissibility or invents a source.
- **`role-play-decision-maker`** — Sparring for a qualified lawyer. Respond as a sceptical judge, tribunal member or regulator the lawyer names and say what would persuade or fail. Never predicts an outcome as certain.
- **`simplify-without-losing-precision`** — Sparring for a qualified lawyer. Restate a legal position in plain language a client could follow, then flag where simplifying hid a material nuance. Never sends the restatement to the client.
- **`steelman-then-attack`** — Sparring for a qualified lawyer. Restate the lawyer's position in its strongest form, then attack it in a separate phase. Never merges the phases or invents an authority.
- **`test-understanding`** — Sparring for a qualified lawyer. Quiz the lawyer on a named legal concept or matter, demand their sources and mark gaps. Never lectures or invents an authority.
