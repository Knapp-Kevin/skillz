# Dependency graph, execution-plan, and qualification contract

This is a **bundled component** of CI Guard. Use when the objective is to
selectively run real verification rather than merely annotate changed files.
A classifier that only emits labels while the previous monolithic acceptance
workflow continues unconditionally is a **FAILED optimization**, even if its
classification is correct.

## Three distinct capabilities, one closed loop

1. **Classification:** compare the exact trusted base, merge-base and candidate
   HEAD; map every changed/deleted/renamed file through source-to-obligation
   bindings. An unrecognized path, source policy, CI/workflow edit, unexpected
   Git mode or ambiguity expands to all configured qualification obligations.
2. **Execution:** compute a transitive dependency closure in a validated acyclic
   obligation graph; group checks that share setup and execute the selected
   commands from a trusted-base command manifest. Every obligation must map
   to a real command. A missing, failed, timed-out or skipped command produces
   no successful obligation receipt. Grouping is not the same as skipping.
3. **Qualification:** independently recompute the plan from the exact Git
   revisions and trusted policy and executable manifest. Compare *all*
   selected and unselected groups with their actual GitHub job results, source
   SHA, merge base, run/attempt, plan/manifest digests and every individual
   obligation's execution receipt. An unselected job unexpectedly running,
   a missing selected job, or a forged/stale plan FAILS.

The bundled Python 3.9+ stdlib [planner/executor](../scripts/ci_plan.py),
[policy fixture](../examples/impact-graph.json),
[command fixture](../examples/exec-policy.json) and
[GitHub Actions reference](../examples/classified-github-pr.yml) implement
these three stages as a concrete *reference*. These files are not installed
by the skill; consumer-specific real tests and policy ownership are required.
The sample's group names and Rust/model edges are an **anonymous example**,
not hard-coded requirements for all CI providers.

## Policy adapter and graph semantics

The consumer-owned graph policy contains:

- `schema_version: 1`, `groups`: stable job IDs, `obligations`: named checks
  with `group` and prerequisite `needs` obligations, `always`: unconditional
  core obligations, and `full`: all checks for unknown/critical changes;
- `rules`: exact file or trailing-`/` directory `prefix` selectors, mapped
  to one or more obligations. No generic extension is sufficient to declare
  docs-only. Rules are trusted-base, versioned artifacts, not PR-supplied
  input. The universal selector doesn't auto-assume Markdown is passive.
- Example: `docs/passive/` -> `docs-links`; `README.md` -> `model-consumer`
  -> `rust-build`; `src/` -> `rust-tests` -> `rust-build`; `.github/` and
  unrecognized files -> full obligations. `always` retains `trust-policy`.
- Topological closure, cyclic/dangling dependency rejection, strict schema,
  exact Git/NUL diff, deleted paths and conservative nonregular mode handling.
  No silently omitted transitive dependency.

**Coverage invariants are enforced at policy load:** every advertised
execution group must own at least one registered obligation; the transitive
closure of `full` roots must contain **all** registered obligations,
including independent native, security or model checks. A declared but empty
security job, or a newly added check omitted from `full`, is an invalid
policy. Duplicate root entries are unnecessary when a dependency already
reaches the obligation. This prevents a plan from saying `full: true`
while silently omitting a required executable check.

The **separate** command manifest is a complete mapping from each obligation to
an argv-array plus bounded timeout. An interpreter invokes these commands
without a shell, from a specified workspace with untrusted PR content treated
as data. As with any CI system, running the checked-out code in an unprivileged
runner is authorized test execution, **not a license to grant it secrets or
publishing tokens**. The command manifest and executor must come from trusted
base. The example's `trusted/ci/verify_*.sh` commands are **consumer-owned
real checks**; missing files FAIL rather than returning success-shaped stubs.
Check closure by actual installed tools, not by assuming test names.

## Exact execution evidence

The `plan` command emits a single canonical JSON object with base, merge base,
HEAD, stage, policy SHA-256, command manifest SHA-256, changed paths, selected
obligation IDs, group membership, fallback reason and plan SHA-256. Job steps
must run the planner before expensive work and expose the selected group flags.

The `execute` command runs every required obligation in dependency order
**within one group** and emits a receipt *after* all its real commands exit 0.
**Exact execution checkout is now mandatory for the CLI**: pass `--repo`
pointing to the checked-out candidate. Before executing, the runner confirms
Git HEAD matches the pinned plan and no tracked source was modified. It
rechecks tracked files before issuing the successful receipt. A correct Git
object in the local repository is not sufficient proof that the working
tree being tested matches that object. Generated untracked output is allowed.

The executor also strips GitHub output/environment modification paths and
GitHub runtime/token variables from child verifier processes. This blocks
direct inheritance of common evidence-forgery channels; however, **it is not
OS-level isolation**. An adversarial same-user process may still access the
trusted checkout, runner filesystem or parent process state. For genuinely
hostile PR executable content, run it under a separate restricted OS
principal/container with no writable access to trusted source, evidence
channels, host process state, tokens or signing credentials. An untrusted
child's self-reported success is never independent attestation.
Receipt binds the group, selected obligation list, plan digest, policy and
executor digests, base, merge base, head, stage, GitHub run ID/attempt, and
per-obligation command hash + exit-code + elapsed milliseconds. Cross-group
DAG edges are represented by actual `needs`; the sample model job depends on
successful Rust qualification. If another consumer graph has different edges,
update the workflow's job `needs` accordingly; a plan graph alone cannot
make GitHub schedule correctly.

The always-emitted `CI policy gate` uses actual `needs.*.result` from each job,
NOT merely its self-reported receipt. It recomputes the plan using Git and
trusted policy. Selected jobs require SUCCESS **and** exact matching receipts
for all obligations. Unselected jobs must be SKIPPED without receipts. The
gate refuses missing docs, failed, cancelled, stale SHA, changed merge-base,
modified policy/plan, incomplete multi-group evidence, and unexpected skips.
**A passing script cannot prove GitHub branch protection requires this check.**
Check branch policies separately before reducing existing required controls.

The gate proves bounded evidence from a configured trust model, not that the
GitHub API is honest or a privileged runner cannot be compromised. Protect
workflow and command owners, forbid `pull_request_target` with untrusted code,
keep no secrets in untrusted PR jobs, pin third-party actions and retain
independent security/release/production approvals.

## Local commands, not live deployment

From a checked-out consumer repo with a pinned trusted base policy:

```sh
python3 ci/ci_plan.py plan --repo . --base "$BASE_SHA" --head "$HEAD_SHA" \
  --policy ci/impact-graph.json --executor ci/exec-policy.json \
  --stage candidate --file /tmp/ci-plan.json
python3 ci/ci_plan.py execute --plan /tmp/ci-plan.json \
  --policy ci/impact-graph.json --executor ci/exec-policy.json \
  --group docs --workdir . --repo . --run-id "local-trial" --attempt 1
```

The second command is appropriate **only** when the plan actually selects docs,
all executable commands exist and running them is authorized. Actual CI
qualification requires observed GitHub job statuses from all groups and a
fresh exact-revision recomputation. A planned receipt or mock status is never
independently observed consumer success.

## Baseline versus changed behavior

- A passive docs change: `docs-links` and always-on trust checks, no Rust/model.
- A model-consumed README: model check and prerequisite Rust build, not docs-only.
- Rust source: Rust build + test closure, sharing one runner where appropriate.
- CI/trust policy: all configured groups, still retaining separate release gates.
- Unknown/mode/graph/command ambiguity: full checks or BLOCK, never a low-risk
  guess. An unavailable changed-file diff is not a zero-change verification.

A static plan that looks correct but never controls which real jobs start is
**not complete**. Neither is a job green without obligation receipts or a
published release without its independent signer/provenance/acceptance.
