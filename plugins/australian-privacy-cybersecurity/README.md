# Australian Privacy & Cybersecurity

This plugin helps lawyers identify Australian privacy and cybersecurity legal
issues, assess suspected data breaches and evaluate AI-system use cases. It
produces preliminary, source-linked work for human review; it does not provide
a final legal opinion, make notifications, approve deployments or determine
facts.

## Skills

- `check-australian-privacy-principles` verifies the applicable official APP
  framework, fingerprints complete principle text and blocks stale analysis
  when a change is detected or cannot be ruled out.
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

The APP workflow does not assume a fixed number, numbering or text. It
enumerates official Schedule 1 at the relevant date, compares full-text
fingerprints across the decision horizon and requires legal-content review
before an earlier APP analysis is reused after change.

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
