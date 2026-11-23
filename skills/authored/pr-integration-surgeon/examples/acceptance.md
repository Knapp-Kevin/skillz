# PR Integration Surgeon: fictional acceptance and false completion traps

The bundled `synthetic-backlog.json` uses six invented PRs in an invented
repository. It does not describe a real provider account, source commit,
review, CI workflow, merge queue, product release, or customer.

## Expected bounded result

| PR | Snapshot claim | Safe planner state |
| --- | --- | --- |
| #101 | Required unit/security checks and approval match exact fictional HEAD | LIVE_RECHECK_CANDIDATE, actual GitHub read still required |
| #102 | Depends on #101, shared edited file | HOLD_RECHECK until parent actually integrates and fresh HEAD tests pass |
| #103 | Draft | BLOCKED |
| #104 | Reported conflict | BLOCKED |
| #105 | Missing approval | HOLD_RECHECK |
| #106 | Required check receipts missing | HOLD_RECHECK |

Linked issues remain unclosed, even if a parent PR is marked green.
The planner reports same-path overlap as a **review advisory**, not a
confirmed conflict; its dependency edges are declared, not native-stack
proof. Under merge queue policy `required`, a candidate still needs a
real provider queue/merge-group qualification before merging. A later
merge changes the target branch, so previously green PRs must be rechecked.

## Negative controls the test suite executes

- Old HEAD checks and approvals are **not** current approval.
- Failing, cancelled, skipped, neutral and pending checks are not all
  silently treated as success; required status identity includes app.
- A draft, reported conflict or changes requested remains blocked.
- Unknown mergeability, policy, merge queue, incomplete changed paths,
  missing parent or current approval means **HOLD_RECHECK**.
- Dependency cycles, self-dependencies and duplicate PR/check/path keys
  fail closed instead of selecting a merge order.
- Same-file overlap is a *potential* collision, not a conflict verdict.
- Untrusted paths, oversized or symlinked JSON and duplicate keys fail.
- Green local simulation cannot merge anything and cannot prove product
  functionality, publisher safety, customer acceptance or issue closure.

The 49 local Python tests are structural, not an independently observed
agent-host trial. A real trial would need an approved provider principal,
complete read-only capture, current ruleset and check receipts, separately
authorized merge action, verified merged commit, and evidence that each
associated issue's acceptance criteria actually succeeded. None is
implicitly authorized by running this skill.

## Relevant provider semantics (optional external references)

GitHub REST pull requests:
https://docs.github.com/en/rest/pulls/pulls

GitHub merge queues:
https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue

Stacked PRs:
https://docs.github.com/en/pull-requests/get-started/about-stacked-prs

These are specifications for interpretation, not source files imported
into this standalone original skill.
