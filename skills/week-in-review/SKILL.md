---
name: week-in-review
description: >-
  Run a Friday retrospective from git history, task states, and the week's
  calendar: what shipped, what stalled and why, decisions made, and what
  carries into next week as Monday's starting list. Use when the user asks
  "week in review", "weekly retro", "what shipped this week", "wrap up the
  week", or wants a carry-forward list that feeds Monday's daily-briefing.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Week in Review
  emoji: "🗓️"
  version: 1.1.0
---

# Week in Review

A Friday retrospective built from evidence: what actually shipped (git history and merged work), what stalled and honestly why, what decisions were made, and what carries forward. The carry-forward section becomes next week's starting list and feeds Monday's daily-briefing run.

## Execution Flow

1. **Bind the workspace.** Discover the bound workspace root(s) — the directory(ies) whose git repos this review sweeps — from the operator's profile, host memory, or a workspace governance note; the bound source wins over assumptions. If none is discoverable, ask once and offer to persist the answer for future runs.
2. **Set the window** — Monday morning through now, or since the last review if one exists in the project's notes or memory files.
3. **Shipped.** Sweep the bound repos with local git commands: `git log --all --since=<window> --oneline` and merged branches (`git branch --merged`) per repo. Shipped means merged, tagged, deployed, or delivered — not merely committed.
4. **Stalled.** Compare against the week's starting intentions (last review's carry-forward, task lists, memory files). Anything planned but not shipped is stalled; state the honest reason — descoped, blocked, displaced by something more urgent, or simply harder than expected. No euphemisms.
5. **Decisions.** Collect decisions made this week from memory files, the project's decisions log (see the decision-log skill), and decision-shaped commit messages or meeting outcomes pulled via the Google Calendar MCP tools.
6. **Carry-forward.** Distill stalled and unfinished items into a ranked starting list for next week. Write it so Monday's daily-briefing can consume it verbatim; save it to the project's notes or memory files if the user agrees.
7. **Present** in the Output Format below.

## Scheduling

- **Claude Code:** use `/schedule` to create a Friday-afternoon routine that runs this skill and posts the review, or `/loop` for an in-session interval.
- **Other agent platforms:** a scheduled automation whose instruction is "Run the week-in-review skill and post the retrospective."

## Output Format

```
# Week in Review — [Mon date] to [Fri date]

## Shipped
- [Deliverable] ([repo], merged/tagged [ref])

## Stalled
- [Item] — [honest reason it stalled]

## Decisions
- [Decision] — [one-line rationale]

## Carry-Forward (next week's starting list)
1. [Item] — [why it leads]
```

## Notes

- Honesty rule: the Stalled section exists to be truthful, not flattering. "I avoided it" is a valid reason and more useful than silence.
- Git data comes from local git commands; calendar context comes from the connected Google Calendar MCP tools — never raw API calls.
- Read-only by default. Writing the carry-forward list into notes or memory files happens only with the user's approval.
