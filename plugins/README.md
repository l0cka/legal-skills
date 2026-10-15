<!-- GENERATED FILE - do not edit. Edit plugin.json/catalog.json and
     run: python3 scripts/generate_registry.py -->

# Plugins

Canonical plugin packages live in this directory.

- [**Australian AI Governance**](australian-ai-governance/README.md) — Maps
  the AI rules and guidance that apply to an Australian organisation. Shows
  which items are law and which are only guidance. (requires
  `australian-legal-research`; hands off to
  `australian-corporations-governance`, `australian-privacy-cybersecurity`;
  law checked 2026-08-26)
- [**Australian AML/CTF**](australian-aml-ctf/README.md) — Finds the AML/CTF
  obligations of an Australian legal practice under the tranche 2 reforms. A
  person must approve each report and decision. (requires
  `australian-legal-research`; hands off to
  `australian-privacy-cybersecurity`; law checked 2026-08-26)
- [**Australian Commercial
  Drafting**](australian-commercial-drafting/README.md) — Drafts Australian
  NDAs, subscription terms, privacy policies and services agreements for
  lawyer review. (requires `australian-legal-research`; hands off to
  `australian-employment-fair-work`, `australian-privacy-cybersecurity`; law
  checked 2026-10-13)
- [**Australian Consumer &
  Competition**](australian-consumer-competition/README.md) — Maps consumer
  guarantees, marketing, merger notification, competition conduct and product
  safety for lawyer review. (requires `australian-legal-research`; hands off
  to `australian-commercial-drafting`, `australian-employment-fair-work`,
  `australian-privacy-cybersecurity`; law checked 2026-10-13)
- [**Australian Contract Review**](australian-contract-review/README.md) —
  Reviews inbound Australian contracts against standard positions, fallbacks
  and approval thresholds. (requires `australian-commercial-drafting`,
  `australian-legal-research`; hands off to `australian-employment-fair-work`,
  `australian-privacy-cybersecurity`; law checked 2026-10-13)
- [**Australian Corporations
  Governance**](australian-corporations-governance/README.md) — Helps govern
  an Australian company under the Corporations Act. Prepares board records and
  reviews for human approval. (requires `australian-legal-research`; law
  checked 2026-08-26)
- [**Australian Employment & Fair
  Work**](australian-employment-fair-work/README.md) — Maps Fair Work
  obligations and reviews contracts, classification, discrimination,
  restraints and underpayment frameworks for lawyers. (requires
  `australian-legal-research`, `australian-litigation-deadlines`; hands off to
  `australian-commercial-drafting`, `australian-privacy-cybersecurity`; law
  checked 2026-08-26)
- [**Australian Estate Planning**](australian-estate-planning/README.md) —
  Prepares solicitor-review drafts from approved NSW, Victorian and Queensland
  estate planning precedents. (law checked 2026-08-26)
- [**Australian Legal Research**](australian-legal-research/README.md) —
  Checks Australian legislation and case citations against the official
  publishers. Writes and reviews AGLC4 citations. (law checked 2026-08-26)
- [**Australian Litigation
  Deadlines**](australian-litigation-deadlines/README.md) — Maps limitation
  periods and computes candidate court deadlines. A lawyer must confirm each
  date. (requires `australian-legal-research`; law checked 2026-08-26)
- [**Australian Privacy &
  Cybersecurity**](australian-privacy-cybersecurity/README.md) — Maps the
  Australian privacy and cyber rules that can apply to a set of facts, a data
  breach or an AI use case. (requires `australian-legal-research`; law checked
  2026-08-26)
- [**Legal Cognitive Sparring**](legal-cognitive-sparring/README.md) — Spars
  with a qualified lawyer on reasoning, gaps, and strategy. Jurisdiction is
  lawyer-supplied. It does not give final advice or invent citations. (law
  checked 2026-10-15)
- [**Legal Evidence Workflows**](legal-evidence-workflows/README.md) — Builds
  source-linked Word document indexes, chronologies, privilege logs and
  inconsistency maps from supplied matter documents without deciding
  credibility, privilege or merits. (law checked 2026-08-26)
- [**Legal Triage**](legal-triage/README.md) — Helps community legal centre
  staff record and triage legal enquiries under an approved profile. (law
  checked 2026-08-26)
- [**Legal Workflow Router**](legal-workflow-router/README.md) — Maps a fact
  pattern to the Legal Skills plugins and skills it engages, in order, with
  the human decision points named. (law checked 2026-08-26)

See [Adding a plugin](../docs/adding-a-plugin.md).
