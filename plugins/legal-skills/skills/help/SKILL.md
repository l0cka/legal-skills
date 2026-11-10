---
name: help
description: Show what Legal Skills covers, the practice areas, what to type for common tasks and which profiles this session has. Run by typing it; gives no legal advice.
disable-model-invocation: true
---

# Help

## Scope

A short orientation to the plugin. It runs only when the user types it. It
lists the practice areas and their skills from the generated skill map,
shows the commands, and says which profiles the session can see. It does no
legal work.

## Workflow

1. Read [../../references/skill-map.md](../../references/skill-map.md). It is
   generated from the shipped skills and is the only list this skill may
   show; never name a skill that is not in it.
2. If the user typed a topic after the command (for example `deadlines` or
   `privacy`), show only the matching practice areas and their skills, with
   each skill's one-line description.
3. Otherwise show:
   - the four commands: `$setup`, `$start`, `$check-citations` and `$help`,
     one line each, written the way this host types them:
     `/legal-skills:setup` in Claude Code and Cowork, `$setup` in ChatGPT
     Work and Codex, `/setup` in Cursor. If the host is unclear, show all
     three forms once;
   - each practice area with one line on what it does and the number of
     skills;
   - that the other skills start on their own when a request matches them,
     and can also be named directly.
4. List the profiles attached to or readable in this session, with each
   one's identifier, version and status as recorded in it. If none can be
   seen, say so and point to `$setup` and
   [../../references/profile-guide.md](../../references/profile-guide.md).
   Do not search outside the session's files to find one.
5. End with the plugin's limits in two lines: every result is for a qualified
   lawyer to review, and research is checked against official sources at the
   time of use.

## Result contract

```text
Commands: <four lines>
Practice areas: <area — one line; skill count> | <matching skills for the topic>
Profiles in this session: <identifier, version, status> | none found
Limits: <two lines>
```

## Fail closed

Never answer a legal question asked alongside the command; offer `$start`
for it. Never list a skill absent from the skill map, describe a profile as
approved unless the profile itself records an approval, or claim the plugin
remembers anything between sessions.
