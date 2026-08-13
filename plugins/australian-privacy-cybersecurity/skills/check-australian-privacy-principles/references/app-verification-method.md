# APP verification method

## Authority boundary

Use the applicable point-in-time compilation of Schedule 1 to the *Privacy Act
1988* (Cth) on the Federal Register of Legislation as the controlling source.
Use `$check-commonwealth-legislation` to establish identity and version. Use
`$trace-commonwealth-legislative-change` when the decision horizon crosses a
version boundary or a potentially relevant amendment or commencement.

The OAIC's [APP text](https://www.oaic.gov.au/privacy/australian-privacy-principles/read-the-australian-privacy-principles)
and [APP Guidelines](https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines)
are regulator materials. They can assist navigation and application, but they
do not replace verification of the current official Act. Record their page
title, URL and update or access date when used.

Case law is outside scope.

## Inventory schema

Create one JSON object for each official compilation inspected:

```json
{
  "title_id": "<verified Federal Register Title ID>",
  "compilation_id": "<verified compilation Register ID>",
  "as_at": "YYYY-MM-DD",
  "source_url": "https://www.legislation.gov.au/<official path>",
  "coverage": {
    "schedule": "Schedule 1",
    "complete": true,
    "method": "Inspected the complete official Schedule 1 text"
  },
  "principles": [
    {
      "identifier": "<displayed identifier>",
      "heading": "<complete displayed heading>",
      "clause_range": "<displayed range or empty string>",
      "text": "<complete text of this principle from the official compilation>"
    }
  ]
}
```

Do not populate an inventory from memory or an earlier checklist. Preserve the
official order. Include every provision presented as an Australian Privacy
Principle, even if it is new, renumbered, transitional or outside the expected
range. Set `coverage.complete` to `true` only after inspecting the whole
Schedule.

The comparison script validates an HTTPS `legislation.gov.au` source, dates,
non-empty identifiers, headings and text, unique identifiers and complete
Schedule coverage. It emits normalized text fingerprints and never emits the
full statutory text.

## Comparison logic

Compare full normalized text as well as structure:

- an identifier in only the later inventory is `added`;
- an identifier in only the earlier inventory is `removed`;
- a changed heading, clause range or full-text fingerprint is `modified`;
- changed order of a common identifier set is `reordered`; and
- a new compilation with no structural or text difference is recorded as a
  compilation change but not an APP framework change.

Renumbering will normally appear as a removal and addition. Review those rows
together rather than assuming equivalence.

The script detects differences; it does not establish commencement, legal
effect, transitional operation, APP-entity coverage or interpretation.

## Decision horizon

Use a horizon that matches the decision. Examples include the planned pilot
end, deployment date, contract term, data-retention period or next mandatory
review. If no horizon is supplied, report that future-period verification was
not performed.

When the horizon crosses a compilation boundary:

1. establish each applicable or potentially applicable compilation;
2. inspect and inventory Schedule 1 in each version;
3. compare consecutive inventories;
4. trace the amending and commencement material; and
5. separate current law, future law and transition work.

## Downstream rule

`APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED` blocks reuse of
earlier APP mappings and blocks a final AI-use-case suitability recommendation.
It does not prevent urgent incident containment or other independently verified
breach duties from proceeding.

`APP FRAMEWORK NOT VERIFIED – DO NOT RELY` blocks APP conclusions. State the
missing source or comparison and the shortest follow-up action.

A verified inventory establishes only that the framework text was checked. A
lawyer must still verify coverage, definitions, exemptions, registered APP
codes, regulations, other relevant provisions and application to the facts.
