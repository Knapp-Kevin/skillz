---
name: task-surface
description: >-
  Build and operate a personal task-coordination repository: a single
  command surface for responsibilities scattered across orgs, repos, PRs,
  reviews, and commitments. Scaffolds the repo and its governance document
  from elicited needs when none exists, then binds to that document to run
  intake, triage, daily views, weekly reviews, and convert-to-canonical
  flows. Use when the user asks "set up a task repo", "track this",
  "what's on my plate", "what's waiting on me", "what am I blocking",
  "run my weekly review", or "turn this into a real issue".
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Task Surface
  emoji: "🗂️"
  version: 1.0.0
---

# Task Surface

An adaptive framework per the template's universal rule: this skill carries **no user-specific values**. All customization lives in the coordination repo's own governance document (its README or equivalent) — Mode 1 generates that document from elicited needs; Mode 2 binds to it and operates. The coordination repo is a **pointer layer**: issues here reference canonical work in its home repo, never duplicate it.

## Execution Flow

1. **Locate or build.** Find the operator's coordination repo (operator profile / host memory, else ask). If none exists, offer Mode 1; otherwise proceed to Mode 2.

### Mode 1 — Forge the surface

2. **Elicit the need** (a few questions, multiple-choice where possible): which contexts/orgs the operator spans; task types beyond the defaults (review, follow-up, create, coordinate, investigate, archive); priority depth (P0–P4 default); statuses (inbox → needs-triage → active / waiting / review-needed / delegated → done / dropped default); review cadence; privacy (private repo default).
3. **Generate the governance README** from the answers: purpose (pointer layer, explicitly *not* a second source of truth), the issue format (Summary / Source / Context / My Role / Next Action / Priority / Status / Due / Notes), the full label taxonomy (`type:*`, `priority:*`, `status:*`, `org:*`, `area:*`), daily-use questions, and weekly-review questions. Present for approval.
4. **Scaffold on approval**: `gh repo create <name> --private`, push the README, seed every label from the taxonomy via `gh label create`. The generated README is now the binding contract for Mode 2.

### Mode 2 — Operate the surface (bind first)

5. **Bind.** Read the repo's governance document and treat it as authoritative for issue format, labels, statuses, and review questions. If it conflicts with anything remembered, the document wins — and workflow improvements are edits to that document (proposed, approved), never to this skill.
6. **Intake** ("track this: …"): draft an issue in the bound format — always capturing Source (canonical link) and Next Action — with the bound labels; create via `gh issue create` on approval.
7. **Daily view**: query per the bound taxonomy — top-priority actives, review-needed, items where the *operator* is the blocker, aging commitments. Action-first ordering; one screen.
8. **Weekly review**: walk the document's own review questions; propose closes, drops, escalations, and delegations (apply on approval); end with a short next-actions list, not an inventory.
9. **Convert-to-canonical**: when an item deserves a real home, create the issue in its home repository, link it in the coordination issue's Source, and transition the original per the bound statuses.

## Output Format

```
# Task surface — daily view, [date]
## Act today (bound priority order)
## Waiting on YOU (you are the blocker)
## Review queue
## Aging (oldest first, with days)

# Weekly review — [date]
[the governance doc's own questions, answered]
## Next actions (small, concrete)
## Proposed: close / drop / escalate / delegate (approval needed)
```

## Notes

- Every `gh` write (repo create, label create, issue create/edit) is approval-gated; queries are read-only.
- Enforce the pointer-layer rule at intake: an item with a clear home elsewhere gets tracked as a *responsibility to* that artifact, with its Source link — never as a copy.
- Pairs with daily-briefing (this repo is a natural task source for it) and week-in-review (which consumes this skill's weekly output); both bind the same way, via the governance document, not via hardcoded pointers.
