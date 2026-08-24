# Legal Evidence Workflows

This plugin supplies one controlled workflow for organising evidence supplied
by a legal practitioner:

- `build-evidence-chronology` inventories the documents, extracts source-linked
  event candidates through a structured review table, and creates an event-level
  chronology as a `.docx` file without smoothing over conflicts or uncertainty.

## Boundary

The workflow organises supplied material. It does not collect evidence, decide
credibility, assess evidentiary weight or admissibility, determine legal effect,
or express a view on merits. A chronology is complete only against the supplied
and readable source set. A human reviewer must verify every material event and
pinpoint before relying on the output.

Source documents remain unchanged. The workflow does not infer missing events,
silently normalise ambiguous dates, or combine inconsistent accounts into a
single narrative.

The chronology deliverable is a Word document. It includes the review scope,
status and limitations, a source-linked chronology table, a conflict register,
evidence gaps and a source register. If the runtime cannot create a valid
`.docx`, the workflow returns `NOT READY` rather than substituting another file
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
