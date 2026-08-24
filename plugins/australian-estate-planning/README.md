# Australian Estate Planning

This plugin provides one practitioner-facing drafting skill per supported
jurisdiction:

- `assemble-nsw-estate-documents` prepares NSW wills, enduring powers of
  attorney and appointments of enduring guardian; and
- `assemble-vic-estate-documents` prepares Victorian wills, enduring powers of
  attorney and appointments of medical treatment decision maker.

Each run concerns one client. The skill extracts a provenance-cited instruction
table and prepares working copies from the centrally maintained approved
precedent library. The source precedents remain unchanged. The workflow applies
the approved drafting playbook and never substitutes a generic or uploaded
document.

Drafting continues where the instructions and approved materials support it. Every missing
fact or unresolved decision is marked inside the document and recorded in a
matching drafting-issues register. Each document is reported as `DRAFT READY
FOR SOLICITOR REVIEW`, `PARTIAL DRAFT – UNRESOLVED ISSUES`, `BLOCKED – NO DRAFT
PRODUCED` or `OUTSIDE SCOPE`.

## Boundary

The plugin serves Australian legal practitioners only. It covers New South
Wales and Victoria. Self-represented parties and other jurisdictions are
outside scope. Advance care directives, supportive attorney appointments,
superannuation death benefit nominations, trusts, probate and administration
are not drafted. Testamentary capacity, undue influence, family provision,
notional estate exposure and tax remain matters for the responsible solicitor.

Every draft carries `DRAFT – SOLICITOR REVIEW REQUIRED`. The workflow never
states that a document is approved, final or ready to sign.

## Deployment model

The plugin ships provider-neutral markdown only. Its two skill definitions are
the portable public interfaces. A private deployment connects the relevant
skill to one senior-lawyer-maintained jurisdiction library containing the
approved precedents, instruction sheet and playbook. The embedded library and
exact file-name references are the deployment's source of truth. Private
materials are never committed to this repository.

See [ADR 0001](../../docs/adr/0001-platform-neutral-no-script-document-assembly.md)
for the text-only design and
[ADR 0003](../../docs/adr/0003-private-deployment-estate-drafting.md) for the
simplified private-deployment boundary.
