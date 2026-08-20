# Australian Estate Planning

Every document this plugin produces is a draft until the responsible
solicitor reviews it, and every draft says so. The plugin never composes a
legal document or requires the firm to add machine markers. It keeps each
human-designed source precedent unchanged, registers permitted fill locations
in a separate solicitor-confirmed precedent profile, and changes only those
sites in a working copy.

One onboarding workflow and two jurisdiction-specific assembly workflows use
the same governed controls. `generate-precedent-profile` creates a proposed
sidecar profile from uploaded clean firm precedents and stops for solicitor
confirmation. The assembly workflows are
`assemble-nsw-estate-documents` for New South Wales and
`assemble-vic-estate-documents` for Victoria.

1. **Profile** — each uploaded clean source precedent is inspected read-only,
   mapped to the relevant instruction schema and returned as a proposed
   sidecar profile. Executed or client-completed files are rejected, and the
   profile cannot be used until the responsible solicitor confirms it;
2. **Extract** — a completed client instruction sheet (or a direct
   interview) becomes a canonical instruction record in which every field
   carries its provenance or is marked `cannot be determined`;
3. **Confirm** — the workflow halts at an extraction gate until the
   responsible solicitor confirms the table, and confirmed fields are
   never re-asked;
4. **Register and fill** — on first use, the workflow proposes a sidecar
   profile of exact factual and clause sites and halts for solicitor
   confirmation. Later fills use working copies only after every structural
   location and exact anchor still matches. A connected drafting playbook may
   identify a registered, verbatim clause variant, but the solicitor confirms
   it before insertion; every unresolved choice or drift finding makes that
   document `NOT READY`; and
5. **Report** — each draft returns under a `DRAFT — SOLICITOR REVIEW
   REQUIRED` banner with a change manifest reconciled against the
   precedent, a gap report, and dated jurisdiction-specific execution-
   formalities references verified against the official publisher.

## Boundary

The plugin serves Australian legal practitioners only; self-represented
parties are routed to human review in every workflow. This release covers
New South Wales and Victoria. The Victorian workflow is anchored in the
Wills Act 1997 (Vic), Powers of Attorney Act 2014 (Vic), Medical Treatment
Planning and Decisions Act 2016 (Vic), and current regulations. Advance care
directives, supportive attorney appointments, superannuation death benefit
nominations, trusts, probate and administration, and all other jurisdictions
are flagged, never drafted or assessed. Testamentary
capacity, undue influence, family provision and notional estate exposure,
and tax are the responsible solicitor's calls in every workflow.

No precedent, no draft: there is no bundled generic will or instrument. A
document type without a firm precedent fails closed; a precedent without a
confirmed profile may be mapped, but cannot be filled.

## Assembly is instruction-governed, not script-governed

Unlike the repository's litigation-deadlines plugin, this plugin ships no
scripts — a deliberate decision recorded in
[ADR 0001](../../docs/adr/0001-platform-neutral-no-script-document-assembly.md).
The sidecar-profile integrity model is recorded in
[ADR 0002](../../docs/adr/0002-sidecar-precedent-profiles-for-human-designed-precedents.md).
The pack is plain markdown so it can be deployed on text-based agent
platforms that cannot execute bundled code: the skill body serves as the
agent definition and the files under `references/` attach as reference
material, with the firm's precedents and any drafting playbook connected
on the platform side. Integrity comes from the confirmed-profile, exact-anchor
and change-manifest reconciliation rules described in the
[source and control method](references/estate-planning-source-and-control-method.md).

Firm content — precedents, instruction-sheet templates, playbooks, client
information — is never committed to this repository.
