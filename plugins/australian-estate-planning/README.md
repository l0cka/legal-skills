# Australian Estate Planning

Every document this plugin produces is a draft until the responsible
solicitor reviews it, and every draft says so. The plugin never composes a
legal document: it fills factual `{{field_name}}` markers and registered
`{{clause_choice:clause_point}}` markers in the firm's own precedents, and
nothing else in a precedent may change.

One governed workflow, `assemble-nsw-estate-documents`, runs the whole
pipeline for a New South Wales private-client matter:

1. **Extract** — a completed client instruction sheet (or a direct
   interview) becomes a canonical instruction record in which every field
   carries its provenance or is marked `cannot be determined`;
2. **Confirm** — the workflow halts at an extraction gate until the
   responsible solicitor confirms the table, and confirmed fields are
   never re-asked;
3. **Fill** — the firm's will, enduring power of attorney and appointment
   of enduring guardian precedents are filled at marker sites only. A
   connected drafting playbook may identify a registered, verbatim clause
   variant, but the solicitor confirms it before insertion; every unresolved
   choice makes that document `NOT READY`; and
4. **Report** — each draft returns under a `DRAFT — SOLICITOR REVIEW
   REQUIRED` banner with a change manifest reconciled against the
   precedent, a gap report, and dated NSW execution-formalities references
   verified against the official publisher.

## Boundary

The plugin serves Australian legal practitioners only; self-represented
parties are routed to human review in every workflow. This release covers
New South Wales — the Succession Act 2006 (NSW), Powers of Attorney Act
2003 (NSW) and Guardianship Act 1987 (NSW) anchor the formalities
reference. Advance care directives, superannuation death benefit
nominations, trusts, probate and administration, and all other
jurisdictions are flagged, never drafted or assessed. Testamentary
capacity, undue influence, family provision and notional estate exposure,
and tax are the responsible solicitor's calls in every workflow.

No precedent, no draft: there is no bundled generic will or instrument,
and a document type without a registered firm precedent fails closed.

## Assembly is instruction-governed, not script-governed

Unlike the repository's litigation-deadlines plugin, this plugin ships no
scripts — a deliberate decision recorded in
[ADR 0001](../../docs/adr/0001-platform-neutral-no-script-document-assembly.md).
The pack is plain markdown so it can be deployed on text-based agent
platforms that cannot execute bundled code: the skill body serves as the
agent definition and the files under `references/` attach as reference
material, with the firm's precedents and any drafting playbook connected
on the platform side. Integrity comes from the marker-only fill rule and
the change-manifest reconciliation described in the
[source and control method](references/estate-planning-source-and-control-method.md).

Firm content — precedents, instruction-sheet templates, playbooks, client
information — is never committed to this repository.
