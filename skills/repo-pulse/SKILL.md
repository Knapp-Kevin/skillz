---
name: repo-pulse
description: >-
  Produce a weekly cross-repo digest of the operator's own GitHub repos via
  the gh CLI — PRs waiting on you, red CI runs, stale branches, and repos
  with uncommitted local work under the bound workspace root(s) — ranked
  action-first.
  Use when the user asks "repo pulse", "what needs my attention on my repos",
  "weekly repo digest", or wants a sweep of everything waiting on them.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Repo Pulse
  emoji: "📡"
  version: 1.1.0
---

# Repo Pulse

A weekly digest across all of the operator's GitHub repos, assembled from the authenticated `gh` CLI and local git checkouts. It surfaces the four things that rot silently — PRs waiting on the operator, failing CI, stale branches, and uncommitted local work — and puts the needs-you items on top so the digest reads as a to-do list, not a report.

## Execution Flow

1. **Bind the workspace.** Discover the bound workspace root(s) — the directory(ies) whose git repos this skill sweeps — from the operator's profile, host memory, or a workspace governance note; the bound source wins over assumptions. If none is discoverable, ask once and offer to persist the answer for future runs.
2. **Enumerate repos:** `gh repo list --limit 50 --json name,owner,pushedAt`. Mark repos pushed within the last 30 days as active; the rest get one line in the digest at most.
3. **Collect PRs per active repo:** `gh pr list --repo <owner>/<name> --json number,title,isDraft,reviewRequests,updatedAt`. A PR "waits on the operator" if it requests their review or is their own PR with changes requested.
4. **Check CI per active repo:** `gh run list --repo <owner>/<name> --limit 5 --json displayTitle,conclusion,headBranch,updatedAt`. Collect runs with `conclusion: failure` on default or PR branches.
5. **Check local checkouts** under the bound workspace root(s): for each repo directory found there, run `git status --porcelain` (uncommitted work) and `git log --oneline @{u}..` (unpushed commits). Stale branches: `git branch -r --sort=committerdate` and flag branches with no commits in 60+ days that are not merged.
6. **Rank:** needs-you items (review requests, red CI, unpushed work) first, ordered by age; informational notes after.
7. **Present** in the Output Format below. Propose actions; take none.

## Scheduling

- **Claude Code:** use `/schedule` to create a weekly routine (e.g. Monday morning) whose instruction is "Run the repo-pulse skill and post the digest."
- **Other agent platforms:** a weekly scheduled automation with the same instruction.

## Output Format

```
# Repo Pulse — [Date]

## Needs You
| # | Item | Repo | Why | Suggested action |
|---|------|------|-----|------------------|
| 1 | [PR/run/branch] | [repo] | [review requested / red CI / unpushed] | [exact command or link] |

## Per-Repo Notes
### [repo] (last push [date])
- CI: [green / N failing runs on <branch>]
- PRs: [open count, oldest waiting]
- Branches: [stale branches, if any]
- Local: [clean / uncommitted files / unpushed commits]

## Quiet Repos
- [repo] — no activity in [N] days.
```

## Notes

- Read-only: this skill reports and proposes. It never pushes, merges, closes PRs, or deletes branches; every suggested action is a command for the operator to run.
- All GitHub data comes from the authenticated `gh` CLI; local state comes from `git` in the known checkouts — never raw API calls or scraping.
- If `gh` is unauthenticated or rate-limited, say so and produce a local-only digest rather than a partial one that looks complete.
