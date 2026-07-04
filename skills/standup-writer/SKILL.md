---
name: standup-writer
description: >-
  Generate an evidence-backed standup or worklog entry in did / doing /
  blocked format from git commits across the MythologIQ repos, task-state
  changes, and calendar events since yesterday or the last standup. Use when
  the user asks "write my standup", "what did I do yesterday", "generate a
  worklog", "standup notes", or needs a status update grounded in real work.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Standup Writer
  emoji: "📋"
  version: 1.0.0
---

# Standup Writer

Write a standup entry — did, doing, blocked — assembled entirely from evidence: git history across the MythologIQ repos, task-state changes, and calendar events. The output claims only what the trail shows; when the trail is ambiguous, it asks instead of inventing.

## Execution Flow

1. **Set the window.** Default is since yesterday's workday start; if a previous standup exists in the project's notes or memory files, use its timestamp instead.
2. **Collect git evidence** with local git commands across the repos under `G:\MythologIQ`: `git log --all --since=<window> --author=<user> --oneline` per repo, plus `git status` for uncommitted work in progress. Group commits by repo and by theme, not one bullet per commit.
3. **Collect task and calendar evidence.** Diff task lists or memory files for state changes (done, started, dropped). Pull the window's meetings from the Google Calendar MCP tools — meetings attended are legitimate "did" items.
4. **Draft did / doing / blocked.** "Did" comes from commits, closed tasks, and meetings. "Doing" comes from open branches, uncommitted changes, and in-progress tasks. "Blocked" only from explicit evidence (a task marked blocked, a commit message saying so) or the user's own words.
5. **Verify against the evidence rule.** Every line must trace to a commit, task change, or event. If the git trail is ambiguous — e.g. commits on a branch whose purpose is unclear — ask the user rather than guessing a narrative.
6. **Present** in the Output Format below.

## Scheduling

- **Claude Code:** use `/schedule` to create a weekday-morning routine that drafts the standup before the meeting, or `/loop` for an in-session interval.
- **Other agent platforms:** a scheduled automation whose instruction is "Run the standup-writer skill and post the entry."

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
- Git data comes from local git commands; calendar comes from the connected Google Calendar MCP tools — never raw API calls.
- Read-only: this skill produces text for the user to post. If posting to Slack is requested, prepare the message via the Slack MCP tools as a draft and send only with explicit approval.
