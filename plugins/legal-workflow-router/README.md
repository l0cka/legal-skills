# Legal Workflow Router

One skill, `route-legal-fact-pattern`, that turns a described matter into a
sequenced plan of Legal Skills plugins and skills to run. It exists because
real matters cut across the plugin boundaries: a data breach at a listed
company engages privacy, cyber incident reporting, continuous disclosure,
litigation deadlines and the legal-research verifiers at once, and the order
matters.

## How it routes

1. Extract routing facts — parties and roles, sector and regulator overlays,
   jurisdiction, events and dates, and the deliverable the user wants.
2. Match the facts to the shipped skills using
   [references/skill-map.md](references/skill-map.md), which is generated from
   the marketplace registry by `scripts/generate_registry.py` and lists every
   skill with its trigger description.
3. Check availability: each routed skill is marked installed, not installed
   or cannot be determined, and the plugins still to install, including the
   plugins a routed plugin requires, are listed under "Install first".
   `scripts/generate_registry.py` derives those dependencies from the skills
   and fails when a plugin's `catalog.json` does not declare them.
4. Sequence: configuration and profile skills first, official-source
   verification next, assessment and mapping skills after, deliverable skills
   last. Name the human decision owner at each hand-off.
5. Report gaps: a fact pattern that no shipped skill covers is reported as a
   gap, never routed to the nearest skill.

## Boundary

The router never answers the legal question, never runs the routed skills and
never treats a routing plan as advice. Each routed skill keeps its own scope,
fail-closed rules and human-review points. Install the routed plugins
separately; the router only names them and says which are missing.

## Permissions

No MCP server, app, hook or write action is bundled.
