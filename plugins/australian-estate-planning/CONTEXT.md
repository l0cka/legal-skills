# Estate planning document assembly

Vocabulary for the `australian-estate-planning` plugin: turning a client's
completed instruction sheet into filled drafts of the firm's own precedents.

## Language

**Precedent**:
A firm's own template document containing `{{field_name}}` markers, connected
on the deployment platform and never committed to this repository.
_Avoid_: template, form, sample

**Instruction sheet**:
The completed client-facing questionnaire (PDF, Word or scan) a practitioner
uploads as the factual source for a matter.
_Avoid_: intake form, questionnaire

**Instruction record**:
The canonical structured set of fields extracted from an instruction sheet or
gathered by interview; the only input the fill step is allowed to read.
_Avoid_: intake data, client data

**Field map**:
The correspondence between instruction-record fields and a precedent's
markers, confirmed by the solicitor the first time a precedent is used.

**Extraction gate**:
The mandatory halt at which the solicitor confirms the extraction table —
every field with its provenance — before any document work begins.

**Change manifest**:
The per-fill reconciliation listing every location changed, the marker
removed and the value inserted, proving nothing outside markers moved.

**Gap report**:
The per-fill list of unfilled markers, unused record fields and clause
choices awaiting the solicitor.
