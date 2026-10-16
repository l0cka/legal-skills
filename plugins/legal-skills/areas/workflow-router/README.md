# Legal Workflow Router

One skill, `route-legal-fact-pattern`, that turns a described matter into a
sequenced plan of Legal Skills skills to run, grouped by practice area. It
exists because real matters cut across practice areas: a data breach at a
listed company engages privacy, cyber incident reporting, continuous
disclosure, litigation deadlines and the legal-research verifiers at once, and
the order matters.

## How it routes

1. Extract routing facts — parties and roles, sector and regulator overlays,
   jurisdiction, events and dates, and the deliverable the user wants.
2. Match the facts to the shipped skills using
   [references/skill-map.md](../../references/skill-map.md), which is generated from
   the marketplace registry by `scripts/generate_registry.py` and lists every
   skill, grouped by practice area, with its trigger description. The profile
   and verification skills a routed skill relies on are added as
   prerequisites.
3. Sequence: configuration and profile skills first, official-source
   verification next, assessment and mapping skills after, deliverable skills
   last. Name the human decision owner at each hand-off.
4. Report gaps: a fact pattern that no shipped skill covers is reported as a
   gap, never routed to the nearest skill.

## Boundary

The router never answers the legal question, never runs the routed skills and
never treats a routing plan as advice. Each routed skill keeps its own scope,
fail-closed rules and human-review points.

## Permissions

No MCP server, app, hook or write action is bundled.
