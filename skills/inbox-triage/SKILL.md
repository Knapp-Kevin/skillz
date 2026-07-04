---
name: inbox-triage
description: >-
  Classify the Gmail inbox into act / delegate / read-later / archive piles,
  draft (never send) replies for the act pile, and flag time-sensitive mail
  or messages from key contacts. Use when the user asks "triage my inbox",
  "sort my email", "what needs a reply", "clear my inbox", or wants drafted
  responses ready for review.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Inbox Triage
  emoji: "📥"
  version: 1.0.0
---

# Inbox Triage

Turn an unread inbox into four decided piles — act, delegate, read-later, archive — with a one-line reason per message and ready-to-review reply drafts for everything in the act pile. Nothing is sent, moved, or archived without explicit approval.

## Execution Flow

1. **Fetch.** Pull unread and recent inbox messages via the Gmail MCP tools. Default window: since the last triage or 48 hours, whichever is longer.
2. **Classify** each message into exactly one pile:
   - **Act** — needs a reply or action from the user personally.
   - **Delegate** — someone else should handle it; name who, if obvious.
   - **Read-later** — informative, no deadline; batch for later reading.
   - **Archive** — no action, no future value; safe to file.
3. **Flag urgency.** Independently of pile, mark anything time-sensitive (explicit deadlines, same-day meetings) or from key contacts, and surface those at the top of the report.
4. **Draft replies** for every act-pile message. Drafts only: write them inline in the report for review. Never send a reply, and only create a Gmail draft object if the user explicitly asks for that after reviewing the text.
5. **Present** in the Output Format below, then ask which drafts to keep, edit, or discard.

## Scheduling

- **Claude Code:** use `/schedule` to run this as a recurring routine (e.g. late morning and end of day), or `/loop` for an in-session interval.
- **Other agent platforms:** a scheduled automation whose instruction is "Run the inbox-triage skill and post the piles."

## Output Format

```
# Inbox Triage — [Date, window]

## Flagged (time-sensitive / key contacts)
- [Sender — subject] — [why it can't wait]

## Act (drafts below)
- [Sender — subject] — [what they need, one line]

## Delegate
- [Sender — subject] — [suggested owner]

## Read-later
- [Sender — subject] — [one-line gist]

## Archive
- [Sender — subject] — [reason it's safe to file]

## Drafted Replies (review before anything is sent)
### Re: [subject]
[Full draft text]
```

## Notes

- Gmail is accessed through the connected Gmail MCP tools only — never raw API calls.
- Strictly draft-only: this skill never sends mail, archives, labels, or deletes anything. Every mutation requires the user's explicit approval after seeing the exact change.
- When a message is ambiguous between piles, prefer act over archive and say why — a false "act" costs seconds; a false "archive" loses a thread.
