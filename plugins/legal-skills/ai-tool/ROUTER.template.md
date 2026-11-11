# Legal Skills: router

Start here. This bundle is a folder of legal workflow instructions for AI
tools that run no code. Version: {{version}}. Mostly Australian law; each
skill states its own jurisdiction.

## How to use it

1. {{entry}}
2. Open that skill's `SKILL.md` and follow it. Read the files it links
   (its `references/` folder and the shared `references/` folder) when it tells
   you to.
   A dollar-prefixed skill name inside a skill means "open `skills/<name>/SKILL.md`". The Getting
   Started skills (`setup`, `start`, `check-citations`, `help`) are typed
   commands in some tools; here, ask for them by name.
3. Follow the skill's result contract and its human-review gate. Every output
   is a draft for a qualified lawyer.
4. If the tool has firm material (a profile, house style, precedents), read
   `reference/firm/README.md`, then use what the firm added.

## What this bundle cannot do

No code runs here. Deadlines are identify-only: the rule, its source, the
inputs a person needs and `not computed`. Legislation checks give the
official source and search steps unless the tool can browse. Read
`references/ai-tool-mode.md` once before the first task.

## Skills by practice area

{{areas}}

## Files

- `skills/<name>/SKILL.md`: one workflow per skill, with its `references/`.
- `references/`: shared source methods, schemas, rule tables and holiday data.
- `catalog.json`: practice areas and their skills.
- `PRIVACY.md`, `LICENSE`, `VERSION`.
