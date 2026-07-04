---
name: decision-log
description: >-
  Capture personal and business decisions as lightweight ADR entries — date,
  context, options considered, choice and why, revisit-by date — appended to
  a designated decisions log, and list decisions due for revisit. Use when
  the user says "log this decision", "record that we decided", "add to the
  decision log", "what decisions are due for revisit", or wants a paper
  trail for non-code choices.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Decision Log
  emoji: "🧭"
  version: 1.0.0
---

# Decision Log

Keep a durable record of life and business decisions in ADR style: what was decided, when, in what context, what else was considered, why the chosen option won, and when to revisit it. This is the life-side sibling of the code-side qor-meta-log-decision skill, but fully independent — no Qor gates, no code required.

## Execution Flow

1. **Locate the log.** Use the log file the user has designated; default is `docs/DECISIONS.md` in the current project. If it does not exist, propose creating it and create it only after the user approves.
2. **Capture the decision.** From the conversation, extract: the decision in one sentence, today's date, the context that forced a choice, the options considered (including the one chosen), why the chosen option won, and a revisit-by date. Ask for anything missing rather than inventing it — especially the revisit-by date, which the user must own.
3. **Draft the entry** in the entry format below and show it to the user for confirmation.
4. **Append on approval.** Add the confirmed entry to the end of the log file. Never rewrite or delete existing entries; the log is append-only, and superseding an old decision is a new entry that references it.
5. **Revisit listing (on request).** When asked "what's due for revisit", read the log, compare each entry's revisit-by date against today, and present overdue and upcoming decisions in the revisit-list format below.

## Output Format

```
## [YYYY-MM-DD] — [Decision in one sentence]
- **Context:** [what situation forced a choice]
- **Options considered:** [option A]; [option B]; [option C]
- **Chosen:** [option] — [why it won, 1-2 sentences]
- **Revisit by:** [YYYY-MM-DD]
- **Status:** active | superseded by [date/decision]
```

```
# Decisions Due for Revisit — as of [date]

## Overdue
- [YYYY-MM-DD] [Decision] — revisit was due [date]

## Coming up (next 30 days)
- [YYYY-MM-DD] [Decision] — revisit due [date]
```

## Notes

- Independent of Qor: shares the ADR spirit of qor-meta-log-decision but touches none of its gates, genome files, or process machinery.
- File mutations are gated: creating the log and appending an entry both require the user to see and approve the exact text first. Entries are append-only.
- If external context is needed to reconstruct a decision (an email thread, a meeting), pull it via the connected Gmail MCP or Google Calendar MCP tools — never raw API calls.
- Every entry needs a revisit-by date; decisions without expiry silently become dogma.
