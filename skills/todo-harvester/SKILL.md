---
name: todo-harvester
description: >-
  Sweep a repository's TODO, FIXME, HACK, and XXX comments into a triaged
  list — aged via git blame, clustered by subsystem, and classified as
  quick-fix, needs-ticket, or stale-delete-candidate. Use when the user asks
  "harvest the TODOs", "what's buried in the FIXMEs", "triage the code
  comments", or wants the debt markers in a repo turned into actionable
  items.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: TODO Harvester
  emoji: "🧹"
  version: 1.0.0
---

# TODO Harvester

Turn the debt markers scattered through a repo — TODO, FIXME, HACK, XXX — into a triage table with age, cluster, and a recommended disposition for each. The harvest is honest about staleness: a five-year-old TODO next to code that has since been rewritten is a delete candidate, not a task. The skill only reports; it never edits or deletes the comments themselves.

## Execution Flow

1. **Harvest** from the repo root:

   ```
   git grep -nE "TODO|FIXME|HACK|XXX" -- ':!node_modules' ':!vendor' ':!dist' ':!build' ':!*.min.js' ':!*.lock'
   ```

   Add repo-specific exclusions if the hit list is obviously polluted (generated code, fixtures).
2. **Age each hit** with `git blame -L <line>,<line> --porcelain -- <file>` and read the `author-time` of the line. Record age in months and the original author.
3. **Cluster** by top-level directory or subsystem so related items read together, not as 80 scattered lines.
4. **Classify** each item:
   - **quick-fix** — the comment describes a small, still-valid change (rename, guard, missing case) doable in under an hour.
   - **needs-ticket** — real work: design decisions, refactors, cross-cutting changes. Draft a one-line ticket title.
   - **stale-delete-candidate** — 12+ months old and the surrounding code has changed, the referenced issue is closed, or the concern no longer applies. Verify by reading the surrounding code before assigning this class.
5. **Present** in the Output Format below, hottest cluster first (most items or oldest median age).

## Output Format

```
# TODO Harvest — [repo] — [Date]

Total: [N] markers ([T] TODO / [F] FIXME / [H] HACK / [X] XXX)

## [Cluster: subsystem/dir] ([n] items, median age [m] mo)
| Location | Marker text (trimmed) | Age | Class | Recommended disposition |
|----------|----------------------|-----|-------|------------------------|
| [file:line] | [text] | [18 mo] | needs-ticket | [ticket title / fix sketch / "delete, code rewritten"] |

## Summary
- Quick fixes: [n] — worth a single cleanup pass.
- Needs ticket: [n] — draft titles above.
- Delete candidates: [n] — confirm each before removing.
```

## Notes

- Read-only: this skill never deletes or edits comments, and never opens tickets itself. Delete candidates and ticket drafts are proposals for the operator to act on.
- All data comes from local `git` (`git grep`, `git blame`); no network access needed.
- If the harvest exceeds ~100 hits, present cluster summaries with the top 5 items each and offer the full table on request.
