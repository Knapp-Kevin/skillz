# CI Guard v1.6.1: source-derived workflow and oracle reconciliation

**Tracking:** #861. **Date:** 2026-11-22. **Scope:** one standalone authored CI Guard package; no consuming project, organization or identifiable external workflow touched.

## Defect and scope

The v1.6.0 normalized v3 simulator can correctly analyze a caller-supplied
event→job graph and reconcile declared scheduled jobs to host attempts.
But it cannot establish that those declarations match actual checkout
workflow YAML or the local acceptance tests that police those workflows.
A stale validator's closed `if` allowlist, forgotten workflow file or
wrong `needs` can invalidate the planned change while the JSON simulator
still passes.

## Implemented source milestone

Added `scripts/ci_source_reconcile.py`, a read-only, bounded standard-library
reconciler. It reads an explicit source map and a normalized v3 scenario
input from a specified root, reuses the existing simulator's source-level
manifest validation, requires complete `.github/workflows/*.yml|*.yaml`
inventory, exact SHA-256 binding for every referenced workflow and oracle
file, one-to-one normalized/source job mapping, declared literal job-level
`if`, `needs`, `runs-on`, and detects source-vs-model dependency drift.

Static Python AST inspection requires one explicit `test_*` checker per
job, with literal workflow path and job-header assertions, plus `if`
and `needs` assertions when present. It never executes these test
functions; the consuming host must run its real compiled/Rust/shell/Python
checkers separately. This AST subset is deliberately narrow to avoid
falsely interpreting arbitrary runtime test logic.

Unsupported reusable jobs, dynamic matrices, job-level multiline guards,
event filters, aliases in guards, ambiguous YAML duplicate keys, symlinked
paths and unknown source structures HOLD. Rejected inputs are not declared
a GitHub semantics violation; they simply need a trusted host parser.
No second competing assurance or overlap engine was introduced.

27 synthetic planted unit/CLI tests create and inspect ephemeral source
files, including stale checker guard, renamed/missing verifiers, missing
or duplicated conditions, unexpected workflows, source/manifest mismatch,
unsafe paths, and an oracle that raises if executed (proving AST-only use
does not run consumer code). The CI Guard QA workflow invokes all 27 tests
in addition to the prior 211. Target source-suite size: **238** methods,
subject to actual hosted receipts.

The method and fixture tests remain entirely independent of any specific
consumer. No provider job billing, actual workflow run, release side effect,
branch rule, source Git tree authentication or compiled conformance-test
outcome is asserted.

## Completion criteria and outstanding provider acceptance

Source qualification requires a passing exact-head PR and successful
repository checks, merged source and independently reconciled full
package tree + SKILL Git blob pins. First source integration [GitHub Actions #45084658182](https://github.com/Knapp-Kevin/skillz/actions/runs/45084658182) at PR #872 source HEAD `7be957a52399daa6b9ca1ed35c7e4bdb7f8253cb` passed **238/238 Python methods**: 12 overlap +16 cutover +23 self-repair +55 scenario +28 classifier +26 plan +8 comparator +16 results proof +27 host +27 source. Socket Security Project Report and PR Alerts both SUCCESS; offline-contracts SUCCESS. The 46-file package tree `d4183718fee3db5b9eef1fa7ef553f1afa0e9c6b` and SKILL blob `2dd814681292e44d9acf97b3a51b9df5b20bc03c` are pinned. The final evidence-only reconciliation HEAD must still pass exact-head checks before merge.

Even after source QA and merge, #861 must remain OPEN until an authorized
consumer can validate actual Git-hosted event/dispatch, active branch
required contexts, complete conformance execution, artifact/runtime
guard paths, provider run lineage and real cutover. Real cost and latency
benefits remain in #840 and **NOT_MEASURED**.
