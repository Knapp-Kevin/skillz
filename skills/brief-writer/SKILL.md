---
name: brief-writer
description: >-
  Write a one-page decision brief for a human decision-maker: the decision
  and deadline, situation, 2-4 options with costs, risks, and reversibility,
  a recommendation with reasoning, and what would change it. Use when the
  user asks "write a decision brief", "help me pitch this decision", "options
  memo", "one-pager for a decision", or needs to ask someone to decide.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Brief Writer
  emoji: "📄"
  version: 1.1.0
---

# Brief Writer

Produce a one-page brief that lets a human make a decision without a meeting: what is being decided and by when, the situation in a few sentences, real options with their costs and reversibility, a recommendation with reasoning, and the information that would change that recommendation. One page is a hard limit, not a style preference.

## Execution Flow

1. **Pin the decision.** State the decision needed as a single question and the deadline for deciding. If either is missing, ask the user before writing anything — a brief without a decision is a status report.
2. **Situation.** Summarize the relevant context in 3-5 complete sentences. Only facts the decision-maker needs; no history tour.
3. **Options.** Lay out 2-4 genuine options (including "do nothing" when it is genuine). For each: cost, key risks, and reversibility — can this be undone cheaply, expensively, or not at all?
4. **Recommendation.** Pick one option and give the reasoning in plain language. A brief that refuses to recommend pushes the work back onto the reader.
5. **What would change it.** List the specific pieces of information that would flip the recommendation. This is what makes the brief trustworthy.
6. **Enforce the page.** If the draft does not fit on one page, the decision is underscoped — say so explicitly and propose splitting it into smaller decisions rather than shrinking the font.
7. **Present** in the Output Format below.

## Output Format

```
# Decision Brief: [decision as a question]
**Decide by:** [date] · **Decider:** [name/role] · **Prepared:** [date]

## Situation
[3-5 sentences of only-what-matters context.]

## Options
| # | Option | Cost | Key risks | Reversibility |
|---|--------|------|-----------|---------------|
| 1 | [option] | [cost] | [risks] | [easy/hard/one-way] |
| 2 | [option] | [cost] | [risks] | [easy/hard/one-way] |

## Recommendation
[Option N], because [reasoning in 2-3 sentences].

## What Would Change This
- [Specific fact or measurement that would flip the recommendation]
```

## Negative rules

These override the format above. An honest gap beats a confident invention on every axis a decision-maker cares about.

- **Never invent a number.** Costs, dates, and figures without a source get `not established` — do not decorate the options table to make it look complete.
- **Unknown risk is stated as unknown**, with what would establish it; reversibility is never guessed.
- **Never reproduce secret-shaped strings** (tokens, keys, passwords) in a brief — type + short prefix only; if one surfaced in source material, recommend rotation.
- **Mark inference as inference** — "(inferred: <basis>)" — never as a stakeholder statement.

## Notes

- One page means one page. If it doesn't fit, the decision is underscoped — split it and say so; never compress by omitting risks.
- Ground claims in evidence the user provides or that lives in the project (local git data, existing docs). If supporting context is needed from email or calendar, use the connected Gmail MCP or Google Calendar MCP tools — never raw API calls.
- Read-only: this skill produces a document. Sending it to anyone (email, Slack) is draft-only — prepare, show, and send nothing without explicit approval.
