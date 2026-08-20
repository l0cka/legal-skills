# Context Map

## Contexts

- [Registry machinery](./CONTEXT.md) — the canonical-source and generated-surface
  vocabulary used by the repository's docs, scripts and architecture reviews
- [Estate planning document assembly](./plugins/australian-estate-planning/CONTEXT.md) —
  the instruction-sheet-to-filled-precedent vocabulary of the
  `australian-estate-planning` plugin

## Relationships

- **Registry machinery → every plugin**: each plugin's `plugin.json` and
  `catalog.json` are canonical sources; the generator emits its distribution
  surfaces. Plugin-domain contexts never redefine registry terms.
