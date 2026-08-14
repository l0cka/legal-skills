# Australian Case Law

This plugin verifies Australian case citations against the official
publishers operated by or for the issuing courts. It exists because
AI-fabricated citations are a live professional risk, and because the free
aggregators either prohibit automated use or sit behind subscriptions. A
medium-neutral citation names its issuing court, so every check can go
straight to that court's own publisher.

The skills route citations, verify High Court, NSW and federal court
decisions, and confirm that quoted passages appear in the officially
published text. Every check follows the same outcome semantics, defined once
in
[references/case-law-verification-method.md](references/case-law-verification-method.md):
`VERIFIED`, `VERIFIED WITH QUALIFICATIONS`, `UNVERIFIABLE` and `NOT FOUND`
are distinct results, and a citation that cannot be checked is never
reported as fabricated.

## Skills

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

## Access posture

Every skill performs targeted, user-directed lookups only — one citation,
one lookup — and never crawls, bulk-downloads or indexes a publisher. Bot
challenges are never solved or bypassed; where a publisher challenges
automated clients the skills degrade to a guided browser session or an
explicit manual check. Suppression and non-publication notations are
preserved, and family-law statutory anonymisation is respected.

## Limitations

Victoria, Queensland, Western Australia, South Australia, Tasmania, the ACT
and the Northern Territory are not yet supported; citations for those courts
return `UNVERIFIABLE` with a manual path. Subsequent treatment (overruled,
followed, distinguished) is out of scope because no free official citator
exists. Verification confirms existence and text, never precedential weight,
interpretation or legal advice.
