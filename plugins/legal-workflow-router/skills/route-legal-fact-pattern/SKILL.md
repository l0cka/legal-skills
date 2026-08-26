---
name: route-legal-fact-pattern
description: Route a described Australian legal matter or fact pattern to the Legal Skills plugins and skills it engages and return a sequenced routing plan — configuration and profile skills first, official-source verification next, assessment and mapping skills after, deliverable skills last — with the human decision owner at each hand-off, using the generated skill map. Use first when a matter spans more than one practice area (a data breach at a listed company, an AI deployment by a regulated entity, a deceased estate with a limitation question) or when the user is unsure which skill to run. Do not use to answer the legal question, assess merits, run the routed skills, or route a practice area no shipped skill covers.
---

# Route Legal Fact Pattern

Turn a described matter into an ordered list of the skills to run, and say
what stays with a human at each step. The router is a map, not an adviser:
every routed skill keeps its own scope, fail-closed rules and review points.

Read [references/skill-map.md](../../references/skill-map.md) before routing. It is
generated from the marketplace registry and is the only list of skills the
router may name; never route to a skill that is not in it.

## Workflow

1. Extract the routing facts.
   - Record, with the user's wording: parties and their roles (entity type,
     listed or regulated status, individual or organisation); sector and
     regulator overlays; jurisdiction or jurisdictions; the events and their
     dates; existing profiles, registers or approved materials the user
     already holds; and the deliverable sought.
   - Record `cannot be determined` for any routing fact the description does
     not supply. Ask one bounded question only where the answer changes the
     plan; otherwise route on stated assumptions and label them.
2. Match facts to skills.
   - For each fact, list every skill in the map whose description is
     triggered by it and note which of its stated exclusions might apply.
   - Prefer the most specific skill. Where an orchestrating skill exists
     (for example a breach assessment that itself calls the APP checker and
     the legislation verifiers), route to the orchestrator and list its
     dependencies as prerequisites rather than as separate steps.
   - Where a fact engages a practice area with no skill in the map, record a
     gap. Never route it to the nearest skill.
3. Sequence the plan.
   - Order: (a) configuration and profile skills the routed skills require;
     (b) official-source verification of the legislation and case law the
     later steps rely on; (c) assessment, mapping and computation skills;
     (d) deliverable and record skills (registers, chronologies, drafts,
     board papers).
   - Mark each step with its inputs (including outputs of earlier steps), the
     plugin it belongs to, and the human decision owner who must act on its
     output before the next step runs.
   - Mark any step whose skill fails closed on a missing profile or
     unverified table, so the user runs the prerequisite first.
4. Report using the result contract.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Matter: <label; jurisdiction(s); parties and roles; deliverable sought>
Routing facts: <fact; provenance in the description; assumption flag>
Plan:
  <step>. <plugin> / <skill> — <why engaged>; inputs: <...>; human decision:
    <owner and decision before the next step>
Gaps: <fact patterns or practice areas no shipped skill covers>
Assumptions and questions: <stated assumptions; one bounded question if any>
Limitations: <the plan is a map, not advice; each skill's own scope governs>
```

Use `READY FOR HUMAN REVIEW` when every routing fact has provenance and every
step names a skill from the map. Use `READY WITH QUALIFICATIONS` when the plan
rests on labelled assumptions or contains gaps. Use `NOT READY` when the
description does not identify a jurisdiction, a party role or a deliverable
and no reasonable assumption can be stated. Use `OUTSIDE SCOPE` when the
request is for the legal answer, a merits view, or a jurisdiction outside
Australia.

## Fail closed

Never answer the legal question, assess merits, or describe the plan as
advice. Never name a skill absent from the skill map, invent a plugin, or
route an uncovered practice area to the nearest skill. Never run a routed
skill from inside the router or represent a routed skill's output. Never
drop a human decision owner from a step to make the plan shorter.
