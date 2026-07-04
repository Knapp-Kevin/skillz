---
name: daily-briefing
description: >-
  Build a one-screen, action-first morning brief from today's calendar,
  actionable unread email, and yesterday's loose ends across memory files,
  task lists, and MythologIQ git activity. Use when the user asks "daily
  briefing", "morning brief", "what's on today", "start my day", or wants
  a single view of what needs a decision today.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Daily Briefing
  emoji: "🌅"
  version: 1.0.0
---

# Daily Briefing

Produce a single-screen morning brief that puts today's required decisions at the top: the shape of the day from the calendar, at most five things to act on, loose ends carried over from yesterday, and a short FYI tail. Action-first — if nothing needs a decision, say so in one line.

## Execution Flow

1. **Calendar.** Pull today's events via the Google Calendar MCP tools. Note the first and last meeting, gaps long enough for focused work, and any event that implies preparation (a review, a call with an agenda, a deadline).
2. **Email.** Scan unread mail via the Gmail MCP tools. Keep only messages worth acting on: direct asks, time-sensitive items, and mail from key contacts. Ignore newsletters and notifications.
3. **Loose ends.** Gather yesterday's open threads from three sources: memory files and task lists in the current project, and recent git activity across the `G:\MythologIQ` repos via local git commands (e.g. `git log --all --since=yesterday --oneline` per repo). Uncommitted work and half-finished branches count as loose ends.
4. **Rank.** Decisions the user must make today go first, then externally imposed deadlines, then carried-over work. Cap "Act on" at five items; everything else is FYI or dropped.
5. **Present** in the Output Format below. One screen means one screen — trim, do not scroll.

## Scheduling

- **Claude Code:** use `/schedule` to create a weekday-morning routine that runs this skill and posts the brief, or `/loop` for an in-session interval.
- **Other agent platforms:** a scheduled automation whose instruction is "Run the daily-briefing skill and post the result."

## Output Format

```
# Daily Briefing — [Date]

## Today's Shape
- [First meeting → last meeting; deep-work gaps; prep needed]

## Act On (max 5)
1. [Decision or action] — [why today, one line]

## Loose Ends Carried Over
- [Open thread from yesterday] — [source: repo/task list/memory]

## FYI
- [Aware-but-no-action item]
```

## Notes

- Read-only. Calendar and Gmail are consulted through their connected MCP tools only — never raw API calls. Git data comes from local git commands.
- This skill never sends email or changes calendar events. If an "Act on" item suggests a reply, offer to draft it; drafts are shown for approval and never sent automatically.
- Authority ordering: calendar is truth for time, git is truth for work state, memory files are hints and may be stale.
