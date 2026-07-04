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
5. **Pair with a schedule.** Propose the weekly check-in (see Scheduling) so review is automatic rather than willpower-dependent.
6. **Write the slip protocol.** State what to do when a week slips: compress (cut optional material), shift (push everything one week), or re-scope (shrink the goal) — and which signal picks which. A slipped checkpoint means the plan adjusts; it is never silently skipped.
7. **Present** in the Output Format below.

## Scheduling

- **Claude Code:** create a weekly `/schedule` check-in that asks whether this week's checkpoint passed, and applies the slip protocol when it didn't.
- The check-in reviews against checkpoints, not hours logged — output over attendance.

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
- Read-only: this skill produces the plan document. Creating the actual `/schedule` routine or sharing the plan happens only with explicit operator approval.
