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
3. **Shipped.** Sweep the bound repos through the host's authorized repository capability (local git when available): `git log --all --since=<window> --oneline` and merged branches (`git branch --merged`) per repo. Shipped means merged, tagged, deployed, or delivered — not merely committed.
4. **Stalled.** Compare against the week's starting intentions (last review's carry-forward, task lists, memory files). Anything planned but not shipped is stalled; state the honest reason — descoped, blocked, displaced by something more urgent, or simply harder than expected. No euphemisms.
5. **Decisions.** Collect decisions made this week from authorized memory files, the project's decisions log (see the decision-log skill), and decision-shaped commits. Include calendar meeting outcomes only when the user has authorized the relevant calendar scope and the host has a suitable connector; do not infer meeting decisions from attendance alone.
6. **Carry-forward.** Distill stalled and unfinished items into a ranked starting list for next week. Write it so Monday's daily-briefing can consume it verbatim; save it to the project's notes or memory files if the user agrees.
7. **Present** in the Output Format below.

## Optional host-managed scheduling

- Default to a one-time retrospective and a proposed reusable Friday prompt. Do not create recurrence or send the report as a consequence of one review request.
- Before an authorized external host creates a recurring review, obtain separate explicit approval of cadence/timezone, continuing repo/task/calendar and private-data scope, recipients/delivery, retention, applicable costs, and pause/revocation controls. Saving carry-forward notes and posting the retrospective are distinct actions requiring approval.
- If a host scheduler or future access is unavailable or unauthorized, report scheduling `not configured` and keep the reusable prompt as a manual handoff.

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
- Use only the authorized repository/calendar capabilities actually available in the host. Do not assume local git or a specific calendar MCP tool; missing source coverage must be reported.
- Read-only by default. Writing the carry-forward list into notes or memory files happens only with the user's approval.
