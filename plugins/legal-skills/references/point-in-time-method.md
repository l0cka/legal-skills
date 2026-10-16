# Shared point-in-time verification method

This method governs every State and Territory legislation checker in this
plugin. Each skill supplies only its jurisdiction-specific facts: the official
publisher, the local timezone, and the local name for a consolidated version.
Everything else — the workflow, the result contract and the fail-closed rule —
is identical across jurisdictions and must stay identical.

## Jurisdiction vocabulary

Each publisher names its consolidated point-in-time text differently. Use the
local term and treat them as equivalent artefacts:

| Jurisdiction       | Publisher                  | Consolidated text term |
| ------------------ | -------------------------- | ---------------------- |
| ACT                | `legislation.act.gov.au`   | republication          |
| New South Wales    | `legislation.nsw.gov.au`   | version                |
| Northern Territory | `legislation.nt.gov.au`    | reprint                |
| Queensland         | `legislation.qld.gov.au`   | reprint                |
| South Australia    | `legislation.sa.gov.au`    | version                |
| Tasmania           | `legislation.tas.gov.au`   | version                |
| Victoria           | `legislation.vic.gov.au`   | authorised version     |
| Western Australia  | `legislation.wa.gov.au`    | compilation            |

## Official-source rules

- The jurisdiction's official publisher is the controlling source. Do not
  substitute a secondary source, an aggregator, or another jurisdiction's
  publisher, silently or otherwise.
- Produce a provenance record, not a bare assertion that legislation is
  "current". Every field in the result contract must be supported by an
  official page that was actually opened and inspected.
- Cite only pages that resolved and were inspected. A constructed or predicted
  URL is not a source.

## Identity resolution

- Resolve exactly one official title and instrument type before anything else.
- Treat multiple plausible titles, an unclear type, or a mismatch between the
  supplied citation and the official record as ambiguity, and fail closed.

## Point-in-time selection

- Select the consolidated text (republication, reprint, version or
  compilation) whose effective date range covers the requested date.
- Record the identifier, the effective date range, the present status of the
  title and the exact URL of the selected text.
- Keep the title's present in-force or repealed status separate from whether
  the selected version operated on the requested date.
- Do not infer that a date embedded in a URL, a registration date or an
  as-made publication date is the version's effective start date. Confirm the
  displayed effective information.

## Commencement and currency

- Inspect commencement material, amendment history and currency notes relevant
  to the requested provision, not only title-level metadata.
- Treat uncommenced or partially commenced provisions, unincorporated
  amendments, and publisher update-lag warnings as qualifications that must be
  itemised in the result.
- Treat future commencements as future law, not present operation.
- A Bill, an as-made document or a registration record is not proof of later
  operation.

## Fail closed

Return `NOT VERIFIED` instead of guessing when the title or type is ambiguous,
the requested date cannot be tied to a displayed consolidated text, the
official publisher is unavailable, or a relevant commencement, amendment or
currency issue cannot be resolved from official evidence. Case law is outside
scope for every checker.
