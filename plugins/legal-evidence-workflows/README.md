# Legal Evidence Workflows

This plugin supplies four controlled workflows for organising evidence supplied
by a legal practitioner. Each delivers a `.docx` file for human review and none
decides what the evidence proves:

- `build-document-index` numbers every supplied document into a source-linked
  index with descriptions taken from the documents themselves and duplicate,
  version and attachment links — the front of a bundle and the source register
  for the other workflows;
- `build-evidence-chronology` inventories the documents, extracts source-linked
  event candidates through a structured review table, and creates an event-level
  chronology as a `.docx` file without smoothing over conflicts or uncertainty;
- `build-privilege-log` records, per document, the author and recipient roles,
  purpose on the face, circulation and waiver flags a practitioner needs to
  decide privilege, with every basis labelled candidate; and
- `map-evidence-inconsistencies` builds a fact-by-source matrix with a
  divergence register that quotes each competing passage and a corroboration
  register, without ranking the accounts.

## Boundary

The workflows organise supplied material. They do not collect evidence, decide
relevance, privilege or waiver, decide credibility, assess evidentiary weight or
admissibility, determine legal effect, or express a view on merits. Every
deliverable is complete only against the supplied and readable source set. A
human reviewer must verify every material row, pinpoint and candidate claim
before relying on the output.

Source documents remain unchanged. The workflow does not infer missing events,
silently normalise ambiguous dates, or combine inconsistent accounts into a
single narrative.

Every deliverable is a Word document. The chronology includes the review scope,
status and limitations, a source-linked chronology table, a conflict register,
evidence gaps and a source register. If the runtime cannot create a valid
`.docx`, each workflow returns `NOT READY` rather than substituting another file
format or prose-only output.

## Structured review

The skill requires the runtime's native structured document-review table when
one is available. The review layer remains source-oriented; the final Word
chronology is event-oriented. If no native table is available, the same schema
is used as an internal structured extraction with the reduced-verifiability
limitation stated in the `.docx`.

For a manually configured Harvey Workflow agent, use the
[Review Table import guide](../../docs/harvey/build-evidence-chronology.md).
That guide is a platform adapter; the canonical skill remains provider-neutral.

## Permissions

No MCP server, app, hook or write action is bundled. Users choose the documents
to provide and where to save or share any reviewed output. The workflow does
not send, file, publish or modify source documents.

## Licence

MIT. This is an original, jurisdiction-neutral evidence-organisation workflow.
