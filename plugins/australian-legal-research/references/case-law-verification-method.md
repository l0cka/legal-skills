# Case law verification method

This reference defines the shared method for every case-law skill in the
`australian-legal-research` plugin: the official-source hierarchy, the citation
grammar, the five-outcome result semantics, the access rules and the
restriction handling. Each skill supplies only its court-specific facts.

## Purpose and boundary

The plugin verifies that a cited Australian judgment exists at the official
publisher for the issuing court, and that quoted passages appear in the
verified text. It does not summarise judgments, assess precedential weight,
report subsequent treatment (overruled, followed, distinguished), or give
legal advice. No free official citator exists for treatment analysis, so the
plugin ships nothing rather than an inference.

## Official-source hierarchy

Verification must use the publisher operated by or for the issuing court.
Aggregators are not verification sources for this plugin, whatever their
quality, because their terms restrict automated use (AustLII), require
subscriptions (Westlaw, Lexis, Jade professional tiers), or both.

| Court group | Official publisher | Access posture |
| --- | --- | --- |
| High Court of Australia | `hcourt.gov.au` (incorporating the former eresources collection) | Direct requests permitted |
| NSW courts and tribunals | `caselaw.nsw.gov.au` | Direct requests permitted; see NSW conditions below |
| Federal Circuit and Family Court | `fcfcoa.gov.au` | Direct requests permitted |
| Federal Court of Australia | `fedcourt.gov.au` (Federal Law Search) | Bot-challenge WAF; human-operated browser only |
| Queensland courts | Supreme Court Library Queensland | Bot-challenge WAF; human-operated browser only |
| Other State and Territory courts | Each court's own website | Not yet mapped by this plugin |

## Citation grammar

A medium-neutral citation has the form `[YEAR] COURT NUMBER`, for example
`[2023] HCA 12`. The court identifier names the issuing court, which makes
routing deterministic without an aggregator. A reported citation has the form
`(YEAR) VOLUME SERIES PAGE`, for example `(2020) 94 ALJR 1`. Report series
are proprietary publications; the official publishers index judgments by
medium-neutral citation, so a reported citation must first be resolved to a
medium-neutral citation through the issuing court's search before it can be
verified. Most Australian superior-court decisions from about 1998 onward
carry both forms. High Court decisions are the exception: `hcourt.gov.au`
includes Commonwealth Law Reports volumes 1–100, so many older reported HCA
citations are directly verifiable.

## Result semantics

Every verification ends in exactly one of five outcomes. Never collapse
`UNVERIFIABLE` and `NOT FOUND` into each other: one is missing evidence, the
other is affirmative evidence of absence.

- `VERIFIED` — the citation resolved at the official publisher; the case
  name, court, date and official URL were recorded from the publisher's
  page.
- `VERIFIED WITH QUALIFICATIONS` — the judgment was located but something
  material is qualified: the case name differs from the one supplied, a
  restriction notation applies, or identity rests on a near rather than
  exact match.
- `UNVERIFIABLE` — the authoritative source could not be consulted (WAF
  challenge, outage, unsupported jurisdiction) or the citation is a
  proprietary report series that could not be resolved to a medium-neutral
  form. This is not evidence of fabrication and must never be reported as
  such.
- `NOT FOUND` — the issuing court's own database was searched and contains
  no matching decision. This is a strong fabrication signal. Report it as a
  flag for human confirmation, never as an accusation.
- `OUTSIDE SCOPE` — the request asks for treatment analysis, interpretation,
  advice, a non-Australian citation, or anything else outside the plugin's
  boundary.

## Access rules

- Perform targeted, user-directed lookups only: one citation, one lookup.
  Never crawl, bulk-download, mirror or index a publisher.
- Never solve, automate around or otherwise bypass a bot challenge or WAF.
  Where a publisher challenges automated clients, either guide a
  human-operated browser session or return `UNVERIFIABLE` with the exact
  manual search URL.
- Space repeated requests; do not retry an unavailable publisher more than
  once.
- Respect each publisher's stated conditions. For NSW Caselaw: the Copyright
  in Judicial Decisions Notice 1995 (NSW) permits reproduction of decisions
  conditioned on accuracy, proper context and compliance with restriction
  notations, and the site's robots directives target search-engine indexing
  of party names — reproduce decisions accurately, never republish party
  names into indexable contexts, and preserve every restriction notation.

## Restrictions and suppression

Before quoting or reproducing any part of a judgment, check the publisher's
page for restriction, suppression or non-publication notations, and for
pseudonymised party names. If a restriction notation is present, report its
existence, do not reproduce restricted content, and mark the result
`VERIFIED WITH QUALIFICATIONS` at best. Federal Circuit and Family Court
family-law decisions are published under statutory anonymisation
(Family Law Act 1975 (Cth) s 121); treat the published pseudonym as the
official case name.

## Quote verification

A quote check runs only against text obtained from the official publisher in
the same session. Search for the exact passage first; if absent, search for a
normalised form (straight quotes, collapsed whitespace, ellipses expanded).
Report the paragraph number or page marker where the passage appears. An
exact match is `VERIFIED`; a near match (minor punctuation or spelling
divergence) is `VERIFIED WITH QUALIFICATIONS` with the divergence itemised; no
match in a verified judgment is `NOT FOUND` for the quote even though the
case itself is verified.

## Provenance record

Every outcome, including failures, records: the exact official URLs
inspected, the date and Australian timezone of the check, and what remains
unverified. Cite only pages that resolved and were read. Never present a
constructed URL as an inspected source.
