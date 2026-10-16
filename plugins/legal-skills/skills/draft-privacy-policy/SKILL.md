---
name: draft-privacy-policy
description: Draft an Australian private-sector privacy policy from evidenced data practices, with an APP 1.4 map, exemption analysis, overseas disclosure and marketing controls, and separate future automated-decision transparency. Use with the Australian Privacy Cybersecurity workflows; do not invent data practices or publish a policy.
---

# Draft Privacy Policy

Jurisdiction: Australian Commonwealth law and the identified governing state or
territory. Record the legal as-at and intended use dates. The 2026-10-13 source
snapshot is a currency limit, not live verification. Verify every applicable
statutory provision on legislation.gov.au (NSW overlays on legislation.nsw.gov.au)
using `$check-commonwealth-legislation` and, for NSW, `$check-nsw-legislation`;
use the corresponding official-source workflow for other states or territories.
Never rely on model memory. Record assumptions and input provenance. A qualified
lawyer must review every output before use.

Read the [source and control method](../../references/drafting-source-and-control-method.md)
first. Use the [profile schema](../../references/drafting-profile-schema.md)
for standing positions and transaction instructions.

## Workflow

1. Identify the policy entity, Australian jurisdictions, audience, legal as-at
   date and intended publication/use date. Build an evidenced data inventory:
   categories including sensitive information, collection channels/cookies,
   holding/security and retention, purposes, recipients, processors, countries,
   access/correction, complaint contacts, marketing and automated decisions.
   Separate actual practices from proposed changes; never promise universal
   security, deletion, consent or a right the business has not established.
2. Route coverage to
   `$route-australian-privacy-jurisdiction`
   and depth to
   `$assess-australian-privacy-issues`.
   Verify Privacy Act 1988 ss 6C–6EA on legislation.gov.au with
   `$check-commonwealth-legislation`. A turnover of $3 million or less is only
   a starting point: assess related entities, health services/data, personal
   information trading and exceptions, Commonwealth contracted services,
   opt-in and other statutory coverage. Do not infer exemption from turnover
   alone or conflate it with the ACL small-business threshold. Record uncertain
   coverage and specialist state/health overlays. For NSW health information,
   use `$check-nsw-legislation` to verify the *Health Records and Information
   Privacy Act 2002* (NSW), including coverage and Schedule 1 Health Privacy
   Principles, on legislation.nsw.gov.au at the relevant date. Treat this as a
   verification lead; do not assume the overlay applies or rely on model memory.
   An exempt business may request
   a voluntary factual policy; do not imply that every APP legally applies.
3. Use
   `$check-australian-privacy-principles`
   to verify the current Privacy Act Schedule 1 APP 1.3–1.6, APP 8 and relevant
   amendments on legislation.gov.au. Return a checklist mapping APP 1.4(a)–(g)
   to policy clauses and evidence: information kinds; collection and holding;
   collection/holding/use/disclosure purposes; access and correction; complaints
   and their handling; likely overseas disclosure; and recipient countries
   where practicable. Include entity/contact, policy date and accessible free
   availability. A policy does not replace APP 5 collection notices.
4. List overseas recipients/categories, functions and countries from the data
   inventory. Distinguish use/storage from disclosure through the specialist
   workflow. Identify APP 8 safeguards or relied-on exceptions and unresolved
   processor arrangements for lawyer review. Never invent a country list or
   describe publication of a list as fulfilling APP 8. Verify APP 8.2(aa),
   8.3 and s 100(1A)–(1B) before relying on a prescribed country/binding scheme;
   verify actual regulations and conditions, not merely the enabling power.
   Mark unknown locations;
   an unexplained worldwide disclosure clause is not a substitute for inquiries.
5. Verify Spam Act 2003 ss 16–18 and Schedule 2 on legislation.gov.au. Describe
   actual consent collection, sender identification and functional unsubscribe
   practices separately from APP 7. A privacy policy or acceptance of website
   terms does not itself establish valid marketing consent.
6. Route automated decisions to
   `$assess-automated-decision-transparency`.
   Verify the Privacy and Other Legislation Amendment Act 2024, s 2 table item 7,
   Schedule 1 Part 15 items 87–89 on legislation.gov.au. APP 1.7–1.9 commence
   on 10 December 2026: separate currently required wording from future wording.
   Inventory personal-information kinds, solely automated decision kinds and
   kinds where a computer performs a substantially/directly related step, with
   the significant-rights/interests test and item 89 decision-date application.
   Human involvement alone does not remove the latter category. If use is after
   commencement, verify and apply the then-operative law; before commencement,
   label preparation or voluntary transparency accurately. Do not duplicate the
   specialist legal assessment in this drafting workflow.
7. Map relevant 2024 enacted reforms and current regulations/codes through the
   privacy workflows, including security/retention, overseas data flows and
   enforcement. Verify the current Schedule 2 serious-invasion tort (commenced
   10 June 2025), its distinct elements/defences/exemptions and exposure even
   where APP coverage is exempt. Check the 2024 Act's s 2 table item 8 for the
   tort, separately from item 7 for automated decisions. Check s 26GC's Children's
   Online Privacy Code development/registration requirement, the actual code's
   registration, commencement and application, and civil penalty tiers under
   ss 13G, 13H and 13K. Verify APP 11.3 technical/organisational measures.
   Enacted mechanisms do not prove an operative code or prescribed-country list.
   If these instruments cannot be confirmed, write "verify against legislation.gov.au"
   and mark the affected claims not verified. Keep proposals separate from law.
   Draft the full factual policy
   with the APP checklist and a current/future change ledger for the lawyer.
   Run `review-draft-against-checklist`; do not insert contract liability caps
   into a privacy policy or use policy wording as blanket processing consent.

## Result contract

Use one status per requested document: `DRAFT READY FOR SOLICITOR REVIEW`,
`PARTIAL DRAFT – UNRESOLVED ISSUES`, `BLOCKED – NO DRAFT PRODUCED` or
`OUTSIDE SCOPE`. A review-ready draft has no unresolved markers; it still requires
qualified lawyer approval and is never ready to sign or publish.

Return the full working draft labelled `DRAFT – LAWYER REVIEW REQUIRED`, the
instruction table, assumptions, source ledger (official URL, provision, version,
effective date, checked date and evidence state), selected positions and departures,
and an issues register. Each `[REVIEW REQUIRED – <issue ID: missing fact or decision>]`
marker must match an entry listing every affected location, source, consequence,
options and required lawyer decision. Add `PARTIAL DRAFT – UNRESOLVED ISSUES
IDENTIFIED` inside any marked draft. Give a bounded list of next decisions and
specialist hand-offs. Save only to a user-authorised controlled destination.

## Fail closed

Block when the entity or Australian policy perimeter cannot be identified.
Unknown data practices produce visible partial-draft markers and targeted
questions, never invented assurances. Unavailable privacy and cybersecurity
skills mean the assessment has not been performed; record the affected
propositions as not verified. Exemption, APP 8 exceptions, future commencement
and material coverage uncertainty remain for the qualified lawyer. Foreign-law
policies and final compliance certification are `OUTSIDE SCOPE`. Never publish
or update live policy.
