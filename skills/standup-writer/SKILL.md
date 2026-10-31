---
name: standup-writer
description: >-
  Generate an evidence-backed standup or worklog entry in did / doing /
  blocked format from git commits across the bound workspace repos,
  task-state changes, and calendar events since yesterday or the last
  standup. Use when
  the user asks "write my standup", "what did I do yesterday", "generate a
  worklog", "standup notes", or needs a status update grounded in real work.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Standup Writer
  emoji: "📋"
  version: 1.1.0
---

# Standup Writer

Write a standup entry — did, doing, blocked — assembled entirely from evidence: git history across the bound workspace repos, task-state changes, and calendar events. The output claims only what the trail shows; when the trail is ambiguous, it asks instead of inventing.

## Execution Flow

1. **Bind the workspace.** Discover the bound workspace root(s) — the directory(ies) whose git repos supply the evidence — from the operator's profile, host memory, or a workspace governance note; the bound source wins over assumptions. If none is discoverable, ask once and offer to persist the answer for future runs.
2. **Set the window.** Default is since yesterday's workday start; if a previous standup exists in the project's notes or memory files, use its timestamp instead.
3. **Collect git evidence** through the authorized host's repository tools or local git when available across the bound repos: `git log --all --since=<window> --author=<user> --oneline` per repo, plus `git status` for uncommitted work in progress. Group commits by repo and by theme, not one bullet per commit.
4. **Collect authorized task and calendar evidence.** Read only the task lists, memory files, and meeting metadata the operator has allowed for this report. Use a connected calendar tool when available and authorized, without assuming a particular MCP integration. A scheduled future run needs its own continuing access grant. Missing or inaccessible sources become disclosed coverage gaps, not inferred meetings or accomplishments.
5. **Draft did / doing / blocked.** "Did" comes from commits, closed tasks, and meetings. "Doing" comes from open branches, uncommitted changes, and in-progress tasks. "Blocked" only from explicit evidence (a task marked blocked, a commit message saying so) or the user's own words.
6. **Verify against the evidence rule.** Every line must trace to a commit, task change, or event. If the git trail is ambiguous — e.g. commits on a branch whose purpose is unclear — ask the user rather than guessing a narrative.
7. **Present** in the Output Format below.

## Optional host-managed scheduling

- Default to a one-time draft. A weekday routine or report delivery is not implied by asking for a standup.
- Before an authorized external host creates recurrence, obtain separate explicit approval of frequency/timezone, future repo/task/calendar access scope, delivery destination and recipients, retention, applicable cost, and pause/revocation method. Posting or notifying recipients requires its own authorization.
- Without an approved scheduler or continuing data-access grant, provide a reusable standup prompt and mark scheduling `not configured`.

## Output Format

```
# Standup — [Date]

## Did
- [Accomplishment] ([repo/branch or task/meeting evidence])

## Doing
- [In-progress item] ([evidence: open branch, uncommitted work, task])

## Blocked
- [Blocker] — [what would unblock it]
(or: Nothing blocked.)

## Unclear (needs your word before I include it)
- [Ambiguous trail item] — [question]
```

## Notes

- Evidence-only rule: never pad the standup with plausible-sounding work the trail does not show. An honest short standup beats an embellished one.
- Use the host's legitimately available git/repository and calendar capabilities, not mandatory local CLI or Google Calendar MCP assumptions. State missing evidence explicitly.
- Read-only: this skill produces text for the user to post. If posting to Slack is requested, prepare the message via the Slack MCP tools as a draft and send only with explicit approval.
