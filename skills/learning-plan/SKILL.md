---
name: learning-plan
description: >-
  Build a structured skill-acquisition plan: a curriculum from real, named
  sources verified to exist, a weekly cadence with concrete checkpoints,
  and a progress-review protocol for when weeks slip. Use when the user
  asks "make me a learning plan", "help me learn X", "build a study
  schedule", or wants a curriculum with checkpoints instead of a link pile.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Learning Plan
  emoji: "🎓"
  version: 1.0.0
---

# Learning Plan

Produce a learning plan a real week can survive: a goal pinned to the operator's current level and time budget, a curriculum built only from sources verified to exist, a week-by-week cadence where every week ends in something demonstrable, and a protocol for what to adjust when a week slips — because one will.

## Execution Flow

1. **Pin the inputs.** Ask for anything missing: the goal (what "done" looks like), current level (honest, not aspirational), and weekly time budget in hours. Do not draft a plan around guessed inputs.
2. **Build the curriculum from real sources.** Select named docs, books, and courses. Verify each exists via web search before including it — confirm title, author/publisher, and that it covers what the plan claims. Never invent a title, and drop anything that cannot be confirmed.
3. **Set the weekly cadence.** Map sources to weeks sized to the time budget. Every week gets a concrete checkpoint: build X, or explain Y without notes. "Read chapter 3" is an activity, not a checkpoint.
4. **Define checkpoint pass criteria.** For each checkpoint, state what passing looks like specifically enough that the operator can self-grade (the thing runs; the explanation covers these three ideas).
5. **Offer an optional check-in.** Propose a weekly checkpoint review, but do not create a recurring host schedule from a request for a learning plan. Recurrence, future context access, and delivery are separate actions requiring specific authorization.
6. **Write the slip protocol.** State what to do when a week slips: compress (cut optional material), shift (push everything one week), or re-scope (shrink the goal) — and which signal picks which. A slipped checkpoint means the plan adjusts; it is never silently skipped.
7. **Present** in the Output Format below.

## Optional host-managed scheduling

- Default to a one-time learning plan and a manually reusable check-in prompt. No scheduling capability is required to use this skill.
- Before creating a recurring check-in in an authorized external host, obtain separate explicit approval of frequency, timezone, start/end or cancellation terms, exact future information sources and private-data scope, report destination/recipients, retention, and any cost. Confirm how the user can inspect, pause, or revoke it.
- If the host lacks an authorized scheduling capability, provide the check-in prompt as a handoff; never claim that a schedule was created.
- The check-in evaluates demonstrated checkpoints, not hours logged.

## Output Format

```
# Learning Plan: [goal]
**Current level:** [level] · **Budget:** [N hrs/week] · **Horizon:** [N weeks]

## Goal statement
[One sentence: what the operator can do at the end that they cannot do now.]

## Sources
- [Title — author/publisher, link] — why: [what this source uniquely covers]

## Week by week
| Week | Material | Checkpoint | Passes when |
|------|----------|------------|-------------|
| 1 | [source, sections] | [build X / explain Y without notes] | [criteria] |

## Slip protocol
- [signal] → compress / shift / re-scope: [specific adjustment]
```

## Notes

- Sources must be real and verified via web search; a plan citing an invented book is worse than no plan.
- Checkpoints are demonstrable artifacts or from-memory explanations — never "finished reading".
- The one-shot plan is read-only. Scheduling, sharing, future private-data access, and persistent storage are separate host actions; a request for a plan is not permission for them.
- For build-from-scratch goals, draw candidate tutorials from codecrafters-io/build-your-own-x (curated, CC0-claimed link index) - still verify each linked source individually before inclusion.
