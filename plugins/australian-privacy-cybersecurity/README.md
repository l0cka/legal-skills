# Australian Privacy & Cybersecurity

This plugin helps lawyers identify Australian privacy and cybersecurity legal
issues and assess suspected data breaches. It produces preliminary,
source-linked work for human review; it does not provide a final legal opinion,
make notifications, or determine facts.

## Skills

- `assess-australian-privacy-issues` maps facts, entities, data, conduct and
  jurisdictions to potentially applicable Australian legislation.
- `assess-australian-data-breach` prepares an urgent assessment and action
  matrix for a suspected breach without making external reports.
- `assess-ai-privacy-cybersecurity-use-case` assesses a defined AI-system use
  case and recommends suitable, suitable with controls, pilot only, not
  suitable on current information, or insufficient information for human
  approval.

## Authority and scope

Install `commonwealth-legislation` and `nsw-legislation` from this marketplace
alongside this plugin. The skills use them to verify Commonwealth and NSW
legislation at the requested date. Other State and Territory propositions must
be checked against the relevant official legislation publisher and reported as
not verified if that check cannot be completed.

Case law is expressly outside scope. Regulator guidance and standards may be
used only when identified as non-legislative material. Every output states its
jurisdiction, as-at date, sources, assumptions, gaps and human-review points.

Do not provide unnecessary personal information, credentials, secrets,
malicious payloads, privileged material or confidential client documents.
Use de-identified extracts wherever possible.

## Provenance

The workflow is original and Australia-specific. Its issue-matrix and
evaluation design is informed by the MIT-licensed Harvey AI `harvey-labs`
data-privacy-cybersecurity task corpus. No task facts, client artefacts or legal
answers are bundled here.
