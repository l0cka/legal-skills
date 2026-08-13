# NSW Legislation

One provenance-first workflow for checking NSW Acts, statutory instruments and
environmental planning instruments against the official NSW legislation
website.

## Skill

`check-nsw-legislation` identifies the official title, collection, NSW website
identifier and applicable point-in-time version. It surfaces commencement,
unincorporated-amendment, update-lag and authorisation issues rather than
collapsing them into an unsupported "current" label.

The bundled `nsw_lookup.py` helper creates official status, whole-title,
legislative-history and XML URLs from a validated NSW legislation identifier.
It does not search, select a version or complete the legal check.

## Scope

Version 0.1 covers titles in the NSW legislation website's In force and
Repealed collections. It does not cover Bills, Gazettes, as-made-only material,
court deadlines, court rules, case treatment, legal interpretation or advice.
Environmental planning instrument maps and documents adopted by reference
remain outside the authorised-content assurance.
