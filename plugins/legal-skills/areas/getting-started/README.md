# Getting Started

Four commands for finding your way in. Every other skill in the plugin starts
on its own when a request matches it; these four start only when you type
them.

| Command | What it does |
| --- | --- |
| `setup` | Asks your role, jurisdictions and practice areas, drafts the profiles those areas need from the [starter profiles](../../references/starter-profiles.md) and offers to save them in a folder you name |
| `start` | Takes a matter description, has `route-legal-fact-pattern` plan the skills to run, and runs the plan one step at a time with your go-ahead |
| `check-citations` | Finds every case citation, legislation reference and quoted passage in a draft, sends each to its verifier and returns one table |
| `help` | Lists the practice areas and commands, and the profiles this session can see |

## How to type them

| Host | Form |
| --- | --- |
| Claude Code and Claude Cowork | `/legal-skills:setup` |
| ChatGPT Work and Codex | `$setup`, or pick it from the skills list |
| Cursor | `/setup` |

Text typed after the command is passed to it, for example
`/legal-skills:start A shop worker in Brisbane was injured yesterday`.

## Why they only start when typed

Each is marked `disable-model-invocation: true` in its `SKILL.md` and
`allow_implicit_invocation: false` in its `agents/openai.yaml`. That keeps
the assistant from starting a setup or a multi-step plan unasked. On hosts
that honour the flag, the description is also left out of the skill listing
the assistant reads, so the commands do not use up the listing budget.

## Boundary

The commands add no legal method of their own. `start` adds pacing to the
router, `check-citations` adds collection to the verifiers and `setup`
sequences the `configure-*` skills. Each underlying skill's scope, result
contract and fail-closed rules govern. None gives legal advice or approves a
profile.

## Permissions

No MCP server, app or hook is bundled. `setup` may write files, and only
this way: it lists the profile file names it proposes, writes nothing until
you confirm them, writes only inside the folder you named, never overwrites
an existing file and never writes client or matter information. If the host
cannot write files, it shows each draft for you to save.
