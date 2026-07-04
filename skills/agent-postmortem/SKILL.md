---
name: agent-postmortem
description: >-
  Extract durable lessons from a failed, wrong, or unexpectedly expensive
  agent session: reconstruct the timeline, find the earliest determining
  point, classify the failure, and propose where each lesson should live.
  Use when the user asks "postmortem that session", "why did the agent fail",
  "what went wrong with that run", or "that run cost way too much".
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Agent Postmortem
  emoji: "🩻"
  version: 1.1.1
---

# Agent Postmortem

Turns a bad agent session into 1-3 durable lessons with a proposed home for each, so the same failure is not paid for twice. The unit of analysis is the earliest point where the outcome was determined — not the visible error at the end. This skill produces a report and proposals only; it never writes memory files, governance ledgers, or config changes itself.

## Execution Flow

1. Reconstruct the timeline from whatever survives: the transcript, tool-call logs, produced artifacts, git history, and cost data. Anchor each event to what the agent knew at that moment, not what is known now.
2. Identify the earliest point where the outcome was determined. Walk back from the visible failure past each proximate cause until removing one more step would have changed the outcome — that step is the root cause. A wrong final answer usually traces to a wrong assumption accepted many steps earlier.
3. Classify the root cause as one or more of: **bad context** (wrong or stale information loaded), **bad tool result** (a tool returned garbage that was trusted), **bad plan** (correct inputs, flawed strategy), **drift from instructions** (the plan was fine and abandoned), **missing skill/knowledge** (no procedure existed for the situation), **cost runaway** (correct work, unbounded loop or scope).
4. Extract 1-3 durable lessons. A durable lesson changes behavior in future sessions and is falsifiable; "be more careful" is not a lesson.
5. Propose a home for each lesson: a memory file, a SKILL.md amendment to a specific skill, a CLAUDE.md rule, or a Qor shadow-genome entry. Propose only — governance artifacts are written by their own gated processes, never directly by this skill.
6. Present the result in the Output Format below.

## Output Format

```
# Postmortem: <session identifier / date>

## Timeline
1. <timestamp/step> — <event> (<what the agent knew>)
...

## Root cause
Earliest determining point: step <n> — <one sentence>
Proximate causes ruled out: <list>

## Classification
<bad context | bad tool result | bad plan | drift | missing skill | cost runaway>

## Lessons
| # | Lesson | Proposed home |
|---|--------|---------------|
| 1 | <falsifiable behavioral change> | <memory file / SKILL.md <name> / CLAUDE.md / shadow-genome> |
```

## Negative rules

These override the format above. A wrong-but-confident root cause is the most expensive output this skill can produce.

- **Every timeline entry cites evidence** (transcript line, log, diff). No evidence → open question, not timeline.
- **Undetermined stays undetermined.** If evidence does not settle the root cause, write `undetermined — candidates: <list>` with what would discriminate between them.
- **Never reproduce secrets encountered in transcripts** — tokens, keys, cookies by type + short prefix only; if one was exposed, rotation is the first lesson.
- **Mark inference as inference**; never invent or promote a suspected cause to an established one to fill the Classification slot — an unfillable slot reads `not established`.

## Notes

- Blame the earliest determining point, not the loudest error. Most postmortems that stop at the proximate cause produce lessons that fix nothing.
- One session yields at most three lessons; more than that means the analysis has not found what mattered.
- Cost runaways deserve the same rigor as wrong answers — identify the step where the loop or scope should have been bounded.
- All proposed homes require their owner's normal review process before anything is written; this report is the input to that process, not a bypass of it.
