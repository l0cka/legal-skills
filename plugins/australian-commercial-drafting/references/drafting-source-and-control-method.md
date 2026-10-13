# Commercial drafting source and control method

## Scope and assumptions

Practitioner-led first drafts for Australian commercial dealings: NDAs, consumer
and small-business SaaS/subscription terms, private-sector privacy policies and
B2B services agreements. Record the governing state or territory, relevant
Commonwealth law, legal as-at date, intended use date, drafting side and qualified
lawyer responsible for review. State every assumption; do not invent an approval,
party identity, registration, operational practice or commercial choice.

Financial services, health, government procurement, construction/security of
payment, franchising, international dealings and worker-status questions can
require additional regimes. Identify the overlay, continue supported core work
and refer the affected part for specialist review. A choice of law does not
remove mandatory consumer protections or privacy overlays.

## Source hierarchy and provenance

1. Use `$check-commonwealth-legislation` for Commonwealth propositions. Verify
   the exact text, applicable compilation, amendments, commencement and
   application provisions on legislation.gov.au at the relevant date.
2. Verify state legislation with the jurisdiction's official publisher. For NSW
   use `$check-nsw-legislation` and legislation.nsw.gov.au. For other states or
   territories use the corresponding Australian Legal Research skill; never
   infer another jurisdiction's rule from NSW wording.
3. Label ACCC, OAIC, ACMA, ATO and Fair Work Ombudsman publications as regulator
   guidance. Verify their version separately from the governing statute.
4. Use user-authorised, version-identified instructions and approved profiles
   for factual and commercial inputs. Preserve any supplied precedent and
   check rights to use it privately; never copy licensed text into this plugin.
5. Treat commentary, templates, search results and model memory as discovery
   material, never authority. The original clause bank is a drafting aid, not
   legal authority or a firm-approved precedent.

For each material legal proposition record the official URL, Act title,
compilation/version, section, effective date, date checked, application analysis
and evidence state. For factual or commercial inputs record document ID,
page/clause, instruction date and confirmer. A link alone is not verification.

## Currency snapshot and verification leads

Checked on 2026-10-13: a research snapshot, not a cached rule; every live
workflow must recheck each source. These are scoped verification leads, not a
claim that all Australian contract law has been reviewed.

| Subject | Official source and provisions to verify at use | Snapshot / drafting consequence |
| --- | --- | --- |
| Consumer guarantees and unfair terms | [Competition and Consumer Act 2010](https://www.legislation.gov.au/C2004A00109/latest/text), Schedule 2 (ACL), ss 3, 23–28, 60–64A, 224 and 267–269; compilation C2026C00405, 16 September 2026 | Preserve non-excludable rights; test consumer status separately from UCT coverage; inspect limitation and remedy provisions before drafting |
| UCT transition | [Treasury Laws Amendment (More Competition, Better Prices) Act 2022](https://www.legislation.gov.au/C2022A00054/asmade/text), commencement table and Schedule 2 application rules; [ACCC contracts guidance](https://www.accc.gov.au/business/selling-products-and-services/contracts) | Penalty regime from 9 November 2023; test making, renewal and term variation dates, not just original contract date |
| Privacy coverage | [Privacy Act 1988](https://www.legislation.gov.au/C2004A03712/latest/text), ss 6C–6EA, Schedule 1 APP 1 and APP 8; compilation C2026C00227, 4 June 2026 | Verify exemption exceptions and data flows before describing coverage or overseas disclosure |
| Privacy reforms | [Privacy and Other Legislation Amendment Act 2024](https://www.legislation.gov.au/C2024A00128/asmade/text), s 2 table item 7, Schedule 1 Part 15 items 87–89 | APP 1.7–1.9 transparency commences 10 December 2026; distinguish current policy and future implementation wording and verify decision-date application |
| Marketing | [Spam Act 2003](https://www.legislation.gov.au/C2004A01214/latest/text), ss 16–18 and Schedule 2 | Verify consent, sender identification and unsubscribe rules; a policy is not marketing consent |
| Copyright | [Copyright Act 1968](https://www.legislation.gov.au/C1968A00063/latest/text), ss 196–197 and Part IX, especially ss 195AW–195AWB | Verify assignments and creator-specific moral rights consents; do not assume the service provider owns every right |
| Contractor status | [Fair Work Act 2009](https://www.legislation.gov.au/C2009A00028/latest/text), ss 15AA–15AC and 357–359 | Verify coverage and classification through the employment hand-off; labels and an ABN do not establish status |
| GST | [A New Tax System (Goods and Services Tax) Act 1999](https://www.legislation.gov.au/C2004A00446/latest/text) | Verify taxable supply, registration, tax invoice and adjustment requirements if relied on; never infer GST status from an ABN |

The privacy reform analysis must also identify relevant enacted changes to
security/retention, overseas data flows, codes and enforcement; route depth to
Australian Privacy Cybersecurity. Do not treat proposals to remove exemptions
or introduce other privacy rights as enacted law without verifying passage and
commencement. For NSW overlays verify the applicable Act on
[NSW legislation](https://legislation.nsw.gov.au/), not from model memory.

## Evidence states

<!-- generated:evidence-states -->
Assign one state to every material proposition:

- `VERIFIED` — the exact current or point-in-time official source and relevant
  text were checked in this session;
- `VERIFIED WITH QUALIFICATIONS` — the source was checked but a commencement,
  application, jurisdiction, document-status or fact qualification remains;
- `NOT VERIFIED` — the official source, applicable version, instruction or
  decisive fact could not be confirmed; or
- `OUTSIDE SCOPE` — the issue needs another legal or regulatory workflow.
<!-- end:evidence-states -->

## Profile precedence and draft controls

Read the [profile schema](drafting-profile-schema.md). The model may prepare or
validate a profile but cannot mark it approved. A human supplies approving role,
date and version. Transaction-specific authorised instructions take precedence
over standard positions, subject to verified law. If profile content conflicts
with a verified source, surface the conflict and stop the affected conclusion.
Conflicting instructions go to the qualified lawyer; never resolve them silently.
An absent approved profile does not prevent supported drafting from explicit
instructions, but every unresolved choice needs a visible marker.

Draft complete operative text, not just a checklist. Keep supported sections
when other parts are unresolved. Put `DRAFT – LAWYER REVIEW REQUIRED` inside
each draft, and `PARTIAL DRAFT – UNRESOLVED ISSUES IDENTIFIED` when necessary.
Use `[REVIEW REQUIRED – <issue ID: missing fact or decision>]` at every affected
location. Each marker has one matching issues-register entry identifying all
occurrences, source, risk and required decision. No silent blanks or guessed terms.
Separate legal research notes and assumptions from operative customer-facing text.

## Results and human control

Configuration and review lead with `READY FOR HUMAN REVIEW`, `READY WITH
QUALIFICATIONS`, `NOT READY` or `OUTSIDE SCOPE`. Drafting uses per-document
`DRAFT READY FOR SOLICITOR REVIEW`, `PARTIAL DRAFT – UNRESOLVED ISSUES`,
`BLOCKED – NO DRAFT PRODUCED` or `OUTSIDE SCOPE`. Evidence states attach to
individual propositions independently of these result statuses.

A qualified lawyer must verify legal application, commercial choices, authority,
source currency, wording, execution formalities and all unresolved items before
use. Never declare a draft enforceable, compliant, approved or ready to sign or
publish. Do not send, publish, execute, file or operate a live subscription or
marketing system. Save only to a user-authorised controlled destination; never
store profiles, matter facts, confidential data or credentials in this public
repository. Do not submit confidential names or text to public search services.
