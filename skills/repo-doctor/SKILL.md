---
name: repo-doctor
description: >-
  Run a one-shot health check of a single repository — stale branches,
  uncommitted or unpushed work, TODO/FIXME count trend, failing CI, README
  drift, missing or old LICENSE, dependency staleness — and emit a
  prioritized punch list with an exact fix command per item. Use when the
  user asks "check this repo's health", "run repo doctor", "audit this
  repo", or wants a punch list before a release or handoff.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Repo Doctor
  emoji: "🩺"
  version: 1.0.0
---

# Repo Doctor

A one-shot, on-demand health check of a single repository that turns diffuse "this repo feels neglected" unease into a prioritized punch list. Every finding carries evidence and the exact command that would fix it — but the skill fixes nothing itself; the operator runs the commands.

## Execution Flow

1. **Confirm the target repo** (path or `owner/name`); `cd` into the local checkout when one exists.
2. **Branch hygiene:** `git branch -r --sort=committerdate` — flag unmerged branches with no commits in 60+ days. Check `git status --porcelain` for uncommitted work and `git log --oneline @{u}..` for unpushed commits.
3. **TODO trend:** count now with `git grep -cE "TODO|FIXME" -- ':!node_modules' ':!vendor'`, then compare against a point ~3 months back: `git grep -cE "TODO|FIXME" $(git rev-list -1 --before="3 months ago" HEAD)`. Rising count is a finding.
4. **CI:** `gh run list --limit 5 --json displayTitle,conclusion,headBranch` — any failure on the default branch is high severity.
5. **README drift:** read the README and spot-check 3–5 concrete claims (install commands, script names, directory layout, badges) against the actual tree. Each broken claim is a finding.
6. **LICENSE:** flag a missing LICENSE file, or a copyright year 2+ years old.
7. **Dependency staleness:** inspect manifests and lockfiles (e.g. lockfile mtime, pinned major versions far behind current). Signals only — do not install or update anything.
8. **Emit the punch list** in the Output Format below, ordered high → low severity. Apply no fix without explicit approval.

## Output Format

```
# Repo Doctor — [repo] — [Date]

## Punch List
| Sev | Finding | Evidence | Fix command |
|-----|---------|----------|-------------|
| HIGH | [e.g. default-branch CI red] | [run/link or file:line] | [exact command] |
| MED  | ... | ... | ... |
| LOW  | ... | ... | ... |

## Healthy
- [Checks that passed, one line each]

Say "fix N" to have me walk through item N with you.
```

## Notes

- Read-only by default: this skill diagnoses and proposes. It never deletes branches, pushes, edits files, or bumps dependencies without the operator's explicit approval per item.
- GitHub data via the authenticated `gh` CLI; everything else via local `git` and the file tree.
- Severity rule of thumb: broken CI or data-loss risk (unpushed work) is HIGH; drift and staleness are MED; cosmetic items are LOW.
