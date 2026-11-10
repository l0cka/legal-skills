---
name: start
description: Start work on a matter. Plans which Legal Skills to run in order with the human decision at each step, then runs one step at a time with your go-ahead. Run by typing it with the facts; never answers the legal question itself.
disable-model-invocation: true
argument-hint: "[describe the matter]"
---

# Start

## Scope

The front door for a matter. It takes the facts the user typed after the
command, has `$route-legal-fact-pattern` build the plan, and then runs the
plan one step at a time, stopping for the user before each step. It runs only
when the user types it. Use `$setup` first if the practice has no profiles
yet, and `$help` to see what the plugin covers.

This skill adds pacing, not judgment. The router's plan and each routed
skill's own scope, result contract and fail-closed rules govern; this skill
never overrides or shortens them.

## Workflow

1. Take the matter description from the text typed after the command and any
   attached documents. If there is none, ask for a short description: who is
   involved and in what role, the jurisdiction, what happened and when, and
   what the user wants produced. Do not ask for more than the router needs.
2. Run `$route-legal-fact-pattern` on the description and show its result as
   it returns it, including the status, every step, each human decision owner
   and every gap.
3. Check prerequisites. For each step that needs a profile, ask whether the
   user has one to attach. If not, say what the step does without it (per
   [../../references/profile-guide.md](../../references/profile-guide.md))
   and offer `$setup`.
4. Offer the first step. Name its skill, its inputs and the decision the user
   must make on its output. Run it only after the user says to.
5. After each step, show that skill's result as it returns it, name the human
   decision it calls for, and offer the next step. Run the next step only
   after the user says to, and only after any decision the plan puts before
   it has been recorded by the user.
6. When the plan is finished or the user stops, report using the result
   contract.

## Result contract

```text
Matter: <label from the router>
Plan status: <router status>
Steps:
  <n>. <skill> — run: <result status> | not run (<reason>) | waiting on <decision owner>
Decisions recorded: <decision; by whom, as the user stated>
Gaps: <from the router>
Next: <the next step and what it needs, or none>
```

Use the router's status for the plan and each skill's own status for its
step. This skill has no status of its own.

## Fail closed

Never answer the legal question, give a merits view or summarise a step's
result into advice. Never run a step the user has not approved, run two steps
on one approval, or skip a human decision the plan names. Never change the
router's order, drop a step or prerequisite, or replace an unavailable skill
with one that looks close. When the router returns `NOT READY` or `OUTSIDE
SCOPE`, show that result and stop. When an urgent first step is named (a
notifiable incident or a data breach), say so before anything else.
