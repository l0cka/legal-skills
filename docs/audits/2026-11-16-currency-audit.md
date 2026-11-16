# Currency audit — 16 November 2026

Scope: every watch-register item, the dated statements in each practice
area's skills and shared references, the deadline computation and holiday
tables, and the court AI protocol register, as at 16 November 2026
(Australia/Sydney).

## Method and limits

- Nine read-only verification passes ran in two rounds, split by practice
  area. Each opened the official publisher and reported findings; the
  coordinator applied the edits. Disputed or surprising findings were re-opened
  at the official source before any edit: the AML/CTF Amendment Bill page, the
  Fair Work Commission generative AI news item, the Financial Reporting System
  Reform Act and the Interactive Gambling Amendment (Gambling Reform) Act.
- The maintainer downloaded, from the official sites on 16 November 2026, the
  sources that block automated access, and they were read from those copies:
  the Home Affairs pages on the draft LPP guidelines and the 2026 AML/CTF
  reforms, the PM&C consultation insights page, the merger threshold
  determination (F2026C00002), Act No. 19 of 2026, the Queensland
  Anti-Discrimination Act 1991 reprint, and the NSW Uniform Civil Procedure
  Rules 2005, Interpretation Act 1987 and Civil and Administrative Tribunal
  Rules 2014. The maintainer also ran the Parliament all-bills keyword search
  for "non-compete". The downloaded copies are not kept in the repository.
- Watch registers keep their snapshot date and text. A reviewed item gains
  `reviewed_on`, `status_at_review` and `review_basis`. Only items actually
  checked were given the review date.
- None of this moves `lawCheckedOn`, which is an area-wide assertion. Every
  area still has unverified items, listed below.

## Results

| Area | Item | Finding | Status |
| --- | --- | --- | --- |
| aml-ctf | `amlctf-amendment-bill-2026`; source-and-control method; `lpp-carve-outs.md` | Passed both Houses on 16 Nov 2026 (Senate second and third readings that day, no Senate amendment recorded). No Royal Assent and no registered Act. As passed, Schedule 3 Part 3 keeps the LPP-form change (items 14–16 and 20–22) and adds s 176(1A) | Verified on aph.gov.au and the ParlInfo as-passed text |
| aml-ctf | `lpp-ministerial-guidelines` | Still a draft; Home Affairs says work to finalise is in progress (page updated 8 Jul 2026). No s 242A instrument on the Federal Register; AUSTRAC still says the Minister "will issue" guidelines | Verified on homeaffairs.gov.au (downloaded copy), legislation.gov.au and austrac.gov.au |
| aml-ctf | `amlctf-rules-amendments` | Transitional Rules now compiled as F2026C00452 (14 May 2026) after F2026L00556, which changes only s 10(5) and adds s 21. Rules 2025 still F2026C00274 | Verified on legislation.gov.au |
| aml-ctf | `austrac-professional-services-guidance-waves`; designated-services registry | Starter kit still release 1.1 (10 Jun 2026). Professional designated services guidance page last updated 25 Sep 2026; the registry items were not re-compared | Dates verified on austrac.gov.au; content comparison outstanding |
| corporations-governance | governance source-and-control method | Corporations Act latest compilation is C2026C00432, compilation 149 (19 Sep 2026). ASIC's RG 280 page flags a consultation on raising the large proprietary thresholds, not in effect | Verified on legislation.gov.au and asic.gov.au |
| corporations-governance | Financial Reporting System Reform Act 2026 | The assent line reads 7 July 2026 and the commencement table gives 6 July 2026 for ss 1–3. The method already records the conflict | No change; conflict confirmed in the as-made text |
| consumer-competition | `cca-compilation`; UCT checklist; product safety skill; `merger-pathways.md`; source register | Latest CCA compilation is 168 (C2026C00486, 27 Oct 2026); its only new amendment is to s 151BC(2)(c), outside the ACL. ACL s 23 unchanged | Verified on legislation.gov.au (Act No. 100 of 2026 and compilation 168) |
| consumer-competition, contract-review | UCT checklist | Act No. 19 of 2026 raised the s 224(3A)(a) fixed amount from $50,000,000 to $100,000,000 from 28 Mar 2026. The checklist had only the 9 Nov 2023 regime | Added; verified in the Act (downloaded copy) and compilation 168 |
| consumer-competition | `merger-instruments`; `merger-pathways.md` | Every screening figure matches F2026C00002. Indexation under s 7-1 begins with calendar years starting on or after 1 Jan 2027 | Verified in the determination (downloaded copy and register text) |
| consumer-competition | `merger-forms`, `merger-guidance`, `environmental-claims`, `general-safety`, `utpa-2026` | Forms instrument in force from 18 Dec 2025; new ACCC merger guidance items; environmental guide flagged as not reflecting the 28 Mar 2026 penalties; Treasury release of 19 Sep 2026 now readable, general safety still proposed; UTPA unchanged | Verified on legislation.gov.au, accc.gov.au and ministers.treasury.gov.au |
| ai-governance | `pmc-ai-infrastructure-consultation`; `standards-for-ai-bill`; source-and-control method | Insights published 13 Nov 2026 (1,533 submissions; no date, draft or Bill). PM&C's consultation page puts copyright policy outside scope, with the Attorney-General leading | Verified on pmc.gov.au (insights from a downloaded copy) |
| ai-governance | `joint-select-committee-ai`, `asx-cgc-5th-edition`, `esafety-code-phases` | Reporting date 30 Nov 2026 confirmed; ASX recommendation expected early Dec 2026; eSafety guidance updated Sep 2026 after a Federal Court judgment it links as [2026] FCA 1123 | Verified on aph.gov.au, asx.com.au and esafety.gov.au (judgment not read) |
| ai-governance | DTA AI in government policy | Now version 2.1 (minor updates 21 Oct 2026). The remaining requirements are stated as "within 12 months" of 15 Dec 2025, with no calendar date | Verified on digital.gov.au; v2.1 changes not compared |
| privacy-cybersecurity | `privacy-tranche-2`; Commonwealth privacy map | Exposure draft dates confirmed on the Attorney-General's Department page. Privacy Act compilation C2026C00227 still latest. New row: Act No. 72 of 2026 amends s 33C and APP 7.8 from 1 Jan 2027 | Verified on consultations.ag.gov.au and legislation.gov.au |
| privacy-cybersecurity | WA PRIS breach scheme; Children's Online Privacy Code; OAIC ADM guidance | 1 Jan 2027 commencement confirmed by Commencement Proclamation (No. 2) 2026 (SL 2026/203); the Code is not yet registered; APP Guidelines chapter 1 unchanged | No change; verified on legislation.wa.gov.au and oaic.gov.au |
| employment-fair-work | `fwo-priorities-2026-27` | The FWO priorities page lists different sectors from the snapshot and says aged care and universities are deprioritised; the Criminal Investigations Branch is not mentioned on it | Corrected from fairwork.gov.au |
| employment-fair-work | `non-compete-ban` | Treasury consultation on draft legislation ran 7 Sep to 2 Oct 2026. Parliament all-bills search for "non-compete" returned nothing | No Bill located (search-limited) |
| employment-fair-work | `rtd-fwc-guidelines`, `closing-loopholes-tranches`, `policy-statutory-hooks.md` | The Commission will not issue right to disconnect guidelines until there is case law ([2025] FWCFB 266). Closing Loopholes report tabling on 20 Aug 2026 confirmed. FWO flexible working page now dated 11 Nov 2026 | Verified on fwc.gov.au and dewr.gov.au; FWO page changes not compared |
| employment-fair-work | `exclusion-state-laws-regs-2026`, `state-declaration-endorsement-2026`, `framework-layers.md` | F2026L00766 commenced 20 Jun 2026 and was repealed 10 Sep 2026 after inserting reg 1.13(d). F2026L00414 is made under s 14(4)(a), not s 14(5), and names Northern Parklands Trust (SA) | Corrected from legislation.gov.au |
| employment-fair-work | `annual-wage-review-2026-27`, `on-demand-delivery-mso`, `qld-positive-duty-commencement` | Wage review figures, high income threshold ($190,100) and compensation cap ($95,050) confirmed; interim on-demand order [2026] FWCFB 211; Queensland positive duty still not commenced | Verified on fwc.gov.au and legislation.qld.gov.au (reprint from a downloaded copy) |
| work-health-safety | `model-whs-amendments-other`, `vic-psychological-health-regulations`, `whs-framework.md` | Model Workplace Exposure Limits amendment takes effect 1 Dec 2026. Victorian S.R. No. 103/2025 in operation 1 Dec 2025, sunsetting 30 Sep 2035 | Verified on safeworkaustralia.gov.au and the authorised regulations |
| litigation-deadlines | `nsw-courts.json`, `ncat.json` | UCPR rr 1.11, 14.3 and 51.16, Interpretation Act s 36 and NCAT Rules r 25 match the current in-force versions | Verified from downloaded official PDFs |
| litigation-deadlines | `art.json` | Migration Act now compilation 172 (C2026C00461, 8 Oct 2026); ss 477 and 477A unchanged | Verified on legislation.gov.au |
| litigation-deadlines | Holiday tables | All eight tables match the official pages for 16 Nov 2026 to the end of 2027. SA, WA and Tasmanian page-modified dates had moved | Verified on each government page |
| legal-research | Court AI protocol register | The Fair Work Commission's guidance note is final and applies from 20 Oct 2026; the register had the March exposure draft | Corrected from the fwc.gov.au news item (guidance note not read) |

## Found but not applied

- `tas-courts.json`, `tas-aia-s29` (pending verification): a pass reports that
  s 29 of the Acts Interpretation Act 1931 (Tas) names Sunday, a statutory
  holiday and a public holiday, and not Saturday. The entry stays pending
  until the authorised text is read; changing it would turn on Tasmanian date
  computation.
- `qld-courts.json` and `qcat.json`: a pass reports newer reprints (QCAT Act
  current as at 22 Oct 2026; UCPR current as at 29 Oct 2026) with the cited
  text unchanged. The recorded versions were not updated.
- `sa-courts.json`: an unofficial consolidation shows amending rules "No 17,
  15 Sep 2026". The gazette was not opened.
- Court AI protocol register: instruments exist for VCAT (PNVCAT 11) and the
  District Court of Queensland (PD 12 of 2025), and Supreme Court of Tasmania
  guidelines were reported. None has been read into the register. The ART
  practice direction's own heading reads "(Use of Generative AI)". The
  Queensland non-lawyer guidelines news page blocks automated access.
- Supreme Court of Queensland Practice Direction 2 of 2026 designates
  25 December 2026 to 1 January 2027 as court holidays for UCPR r 976. The
  Queensland table carries only a general caveat.

## Not verified

- aml-ctf: Royal Assent to the Amendment Act; what AUSTRAC changed in its
  professional designated services guidance after 10 July 2026.
- corporations-governance: APRA's draft CPS 510 dates (the consultation page
  was not found); the ASX fifth edition's first reporting periods; the Group 1
  and Group 2 sustainability reporting dates.
- consumer-competition: merger fees, waivers and form text; whether
  compilation 168's ACL contains a general safety provision (only the amending
  Act was read).
- ai-governance and privacy-cybersecurity: the Kmart tribunal review and
  whether a Bunnings appeal was filed; the National AI Plan page; the cyber
  regime registry (ransomware reporting, security of critical infrastructure);
  whether any privacy, online safety or AI Bill was introduced after
  28 October 2026; the statutory privacy tort, data breach, board oversight
  and guidance-alignment skills, which were only keyword-scanned.
- employment-fair-work: a Bill search under terms other than "non-compete";
  the content of the FWO flexible working page after its 11 November update;
  the Building Cooperative Workplaces detail.
- work-health-safety: industrial manslaughter, psychosocial codes of practice
  and adoption of the incident notification amendments, by jurisdiction.
- litigation-deadlines and estate-planning: Victorian, Western Australian,
  Tasmanian, Northern Territory and ACT rule versions were reported current
  by one pass and not re-opened; the NSW Succession Act 2006, Powers of
  Attorney Act 2003, Guardianship Act 1987 and the reported Guardianship
  Regulation 2026 (the NSW register blocks automated access).
- legal-research: ten court AI register entries were not re-read for a newer
  instrument; the VCAT half of the Victorian judgments statement.

## Next steps

- Confirm Royal Assent and the Act number for the AML/CTF Amendment Act, then
  move the LPP-form change from pending to enacted with its commencement.
- Read the 30 November 2026 Joint Select Committee report and the ASX Board's
  December decision on the fifth edition.
- Recheck on or after 1 December 2026 (Financial Reporting System Reform Act
  Schedule 1 Parts 1 and 3; model Workplace Exposure Limits), 10 December 2026
  (APP 1.7–1.9; Children's Online Privacy Code registration) and
  1 January 2027 (WA breach scheme; merger threshold indexation; Privacy Act
  s 33C and APP 7.8).
- Read the Tasmanian s 29 text, the Queensland reprints and the three new
  court AI instruments, and update the tables and register.
