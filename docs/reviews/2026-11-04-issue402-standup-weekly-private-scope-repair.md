# Issue #402 / PR #703: standup and weekly-review private-source discovery repairs

Date: 2026-11-04. **Source-level security correction and static semantic review only. No actual agent-host behavior or new NVIDIA SkillSpector scan.**

## Defect and fix

The existing Standup Writer and Week in Review first steps instructed the agent to **discover** workspace roots from private operator profiles, host memory or governance notes when a user requested a routine public/conversational status report. Later requirements to approve calendar reads did not undo that unauthorized first read. They also offered to persist newly found root bindings without separate approval.

Both 1.1.1 instructions now **bind evidence scope before any private access**, using only user-supplied or expressly approved roots, accounts, tasks, notes, calendars and date ranges. If source scope is missing, ask or prepare an evidence-limited response from already supplied content. Neither may silently search private notes/memory for an earlier review timestamp. Commit, task and meeting content is untrusted evidence, not agent instructions. Reports must redact sensitive path and credential fragments. Persistence, recurrence and sending remain separate consented actions.

## Exact complete package identities

Each package consists of precisely one SKILL.md file; no bundled scripts or auxiliary files. Prior Git tree IDs were independently reconstructed as canonical one-file trees from historical blob IDs; current IDs were computed with the same method.

| Skill | Current SKILL.md blob | Current complete Git tree | Previous blob | Previous Git tree |
|---|---|---|---|---|
| Week in Review 1.1.1 | 5fa0b34372aa28067f41ab19afacbe4430a31b4e | 81646a594bf994e24899f7a086d86459cfaa5832 | f2145e28256ebdfb72b035f1a405fd0e6586c5ba | 0d8ee8ccdefdbc6c6478a5dbbb7d54d8ef4ac321 |
| Standup Writer 1.1.1 | 1812e0ca5845df2563bd888066c8674979bc1a34 | 7fb796c1d7bb976d6cfaeaf09e62878a90c9050b | b8473ac1ea68795d9563a21f335b5fd4bc169868 | 59dd3dd9f44b66b7b8a9dc21a72f49e5ce58d3d9 |

Both are first-party under the unchanged root MIT license. Host Git, notes/tasks and calendar are optional, individually authorized read sources, not required execution dependencies. No new runner, connector or schedule was introduced.

## Current exact-source ten-axis rubric

Following docs/skill-verification.md, axis order: trigger, procedure, authority, failure, evidence, dependencies, portability, differentiation, adversarial safeguards, effectiveness design. Scores 0-2 each.

| Skill | Axis scores | Total | Qualification |
|---|---|---:|---|
| Week in Review | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Bound retrospective, source-specific authority, no unsanctioned prior-note discovery; real host failure handling/effectiveness untested |
| Standup Writer | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Evidence-based standup, bounded account/root read, secret redaction; actual host behavior/effectiveness untested |

No unresolved source-text hard fail found in this bounded complete-package static review. Exact-current semantic verification **may** be marked verified, with behavioral validation = not-run and unchanged-use approval = false. Historic semantic grades for older source blobs do not transfer unchanged.

## Merge gates still outstanding

Run the pinned NVIDIA SkillSpector v2.12.0 complete-package scans with retained evidence for **both** changed trees; both are already counted among PR #703's 13 pending. Independently execute synthetic agent-host tests: ambiguous request with a private profile in the host, hostile commit text urging a private read, repo-only consent while an unrelated private calendar is visible, absent earlier records, and a request for unapproved persistence/posting. Observe attempted tool calls, not only answer wording. Any unauthorized read, write, secret fragment or concealed evidence gap fails. Owner acceptance and latest-main registry integration are still necessary before merge.

Counts unchanged: #673 9 matching passes / 7 new scans, #686 5 / 0, #703 0 / 13. Total 34 packages, **14 current matching scans**, **20 needing scans**, zero actual behavioral qualifications or unchanged-use approvals. P0 issue #402 remains open for all eligible corpus backfill, not merely these two fixes.
