# CI Guard v1.0: live GG-CORE repository application (2026-11-19)

## Scope and outcome

- **Skill:** `skills/authored/ci-guard/SKILL.md`, exact Git blob `80d9cc0eec15dae1d23c0e0bb24ff6b69c9fd698`, package tree `05b7339ef03657a74d675cf795650434513083f1`.
- **Target:** [MythologIQ-Labs-LLC/GG-CORE](https://github.com/MythologIQ-Labs-LLC/GG-CORE), `main@183409cf7908c479475d3c8d7991d07482260bcb`; public GitHub Actions YAML and actual GitHub run/job logs.
- **Mode:** Authorized, read-only in an external ChatGPT agent host. Real repository source inspection, real observed CI runs/logs, and separate controlled counterexample emulation. **No target repository edits, CI triggers, test execution in native Windows, release publication, secrets access, or independent host/model A/B.**
- **Outcome:** Actionable CI-control assessment produced. It retained relevant security/native coverage and exposed a performance-gate claim/evidence mismatch. **Neither measured improvement nor user outcome delivery has occurred.** Do not upgrade `ci-guard` to behavioral `validated` from this single assisted review.

## Observed checks and evidence

| Check | Actual workflow trigger/coverage | Observed evidence at frozen target | Decision and qualification |
| --- | --- | --- | --- |
| `CodeQL / Analyze` | Push to main, PR to main, Rust static analysis; job scoped `security-events: write` | [CodeQL workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/183409cf7908c479475d3c8d7991d07482260bcb/.github/workflows/codeql.yml); [run 44568256644](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44568256644) PASS; active [ruleset Basic](https://github.com/MythologIQ-Labs-LLC/GG-CORE/rules/14213663) has high-or-higher security-alert and error code-quality gates | KEEP. Rule configuration exists; the unique detection of every suppressed/queried class was not independently seeded or verified. |
| `cargo-deny` | Rust push/PR, locked dependency graph, advisories, dependency bans, licenses, sources | [Rust workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/183409cf7908c479475d3c8d7991d07482260bcb/.github/workflows/rust.yml); job PASS on run 44568256590 | KEEP. Explicit independent supply-chain checks; do not delete due overlap with CodeQL. |
| `fmt + clippy` | Linux/macOS/Windows, three jobs | PASS on run 44568256590; earlier PR run 44565701714 failed formatting on all three platforms | KEEP / possible minor SIMPLIFY. Formatting is repeated across OS but is short; platform-specific Clippy still has value. Actual detection of format violations observed. |
| `test` | Linux/macOS/Windows default workspace tests | PASS on run 44568256590 | KEEP. This does not establish separate installed/native stream and cancellation behavior. |
| `features` | Linux GGUF, ONNX, FFI, Python and advanced feature suites | All five PASS on run 44568256590 | KEEP. Distinct feature compilation/tests, not redundant by naming alone. |
| `bench` | Ten model-free bench targets on every Rust PR and main push; PR baseline comparison, cache from main | [run 44568256590](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44568256590) green; 9m18s benchmark job on that run; PR run 44566019508 restored main baseline and passed comparator | REPAIR comparator evidence before deciding on RELOCATE/SIMPLIFY. Missing baseline is an intentional zero exit; uniform slowdown is normalized out. |
| `ONNX packaged readiness` | Path-scoped PR model-free unit contract | [Workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/183409cf7908c479475d3c8d7991d07482260bcb/.github/workflows/onnx-readiness-contract.yml), run 44562474823 PASS on specified head | KEEP narrowly; cannot substitute for actual ONNX IPC serving. |
| `packaged IPC probe` | Path-scoped PR model-free contract | [Workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/183409cf7908c479475d3c8d7991d07482260bcb/.github/workflows/packaged-ipc-perf-contract.yml), run 44561286909 PASS | KEEP; model-free tests are not real installed throughput qualification. |
| `Release` | Manual or version-tagged; package Linux/macOS/Windows and test real pinned GGUF fixture; only version tag publishes | [Release workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/183409cf7908c479475d3c8d7991d07482260bcb/.github/workflows/release.yml) source inspected, but **no release-run execution inspected** | KEEP / VERIFY required native acceptance and release owner GO. |

The active repository ruleset was directly read. The separate branch protection API returned 403 to this GitHub App; do not infer no branch protection or that any named check is formally required from the workflow alone.

## Measured historical comparison, selection limits

From **nine recent successful Rust and nine recent successful CodeQL GitHub runs**:
- Rust workflow total wall time (created→updated): p50 **9.72 min**, p90 **19.95 min**.
- CodeQL workflow wall time: p50 **11.18 min**, p90 **11.80 min**.
- Rust benchmark job p50 **9.65 min**, p90 **10.05 min**.
- GGUF feature job p50 **7.95 min**, p90 **9.30 min**.
- Windows default test job p50 **2.88 min**, p90 **3.05 min**.

The sample is deliberately bounded, success-selected and includes PR attempts/queue effects. It does **not** measure the full repository failure rate or flakiness and is not enough to establish billed runner costs. Removing benchmarks would avoid their own job time but is not proof of equivalent detection or a major pipeline latency reduction with CodeQL still on the critical path.

## Performance comparator adversarial tests

[Actual source `core-runtime/scripts/perf_gate.py`](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/183409cf7908c479475d3c8d7991d07482260bcb/core-runtime/scripts/perf_gate.py) includes: a missing/empty baseline returning exit 0; new unmatched benchmarks being reported, not failed; and normalization by the median run-wide ratio across gated benchmarks. A controlled **decision-rule reimplementation** of those read instructions, not an execution of the source Python script, produced:

| Synthetic input | Comparator-equivalent verdict | CI Guard disposition |
| --- | --- | --- |
| Three comparable benchmarks all slow to 3x the baseline, threshold 2x | PASS (global shift=3, each normalized ratio=1) | REPAIR/VERIFY systemic-slowdown reporting |
| One of three comparables slows to 3x, other two unchanged | FAIL | KEEP this useful outlier detector |
| No usable baseline | PASS without comparison | REPAIR truthful evidence state (not necessarily block first-run by policy) |
| Baseline exists but all current benchmarks are new/unmatched | PASS without comparisons | REPAIR explicit NOT_COMPARED result |

Two actual benchmark job logs, including [PR run 44566019508](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44566019508) and [main run 44568256590](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44568256590), each contained **88** Criterion messages referencing missing `base/sample.json`, although the jobs completed successfully. This may represent Criterion's normal baseline mechanics rather than invalid results. Investigate without relabeling all performance runs failed.

## Three priority decisions and acceptance

1. **REPAIR (high): Improve comparator truthfulness without removing its meaningful detection.** Preserve the ability to detect local per-benchmark regressions; add distinct `COMPARED`, `NO_BASELINE` and `NO_MATCHED_BENCHMARKS` reporting. An explicit systemic-shift signal or comparison against a genuinely comparable runner is needed before interpreting a uniform slowdown as healthy. **Acceptance:** seeded 3x local and uniform regressions are distinguished from genuine runner-wide class changes, cache misses never masquerade as compared PASS, and a controlled negative test proves the classification. **Rollback:** restore previous comparator+workflow from exact reviewed commit if false positives block normal commits.
2. **VERIFY then SIMPLIFY (medium): Measure targeted benchmark placement and avoid unconditional repetition only if release assurance survives.** The Rust workflow has 14 jobs, with the benchmark dominating its own runner time. Preserve CodeQL, locked dependency policy, Windows/macOS tests and GPU/native release qualification. **Acceptance:** relevant benchmark-sensitive changes still run appropriate detection; docs-only/low-risk changes produce truthful visible outcomes; compare job-minutes and exact-head wall times on representative PR classes. **Rollback:** restore current unfiltered benchmark trigger/check immediately if a seeded relevant failure is missed.
3. **KEEP + VERIFY (P0): Do not mistake green PR CI for installed Windows release acceptance.** [Issue #219](https://github.com/MythologIQ-Labs-LLC/GG-CORE/issues/219) and [draft PR #226](https://github.com/MythologIQ-Labs-LLC/GG-CORE/pull/226) explicitly require independent native Windows streamed-task/cancellation/memory-safety proof. [Issue #161](https://github.com/MythologIQ-Labs-LLC/GG-CORE/issues/161) owns integrated v1.0.0 GO/NO-GO. **Acceptance:** original Windows crash reproducer and native installed acceptance tied to exact candidate, then owner release decision; no inference from successful Linux/hosted jobs.

## Evaluation of CI Guard itself

The v1.0 skill correctly routed supply-chain security and platform checks to KEEP, resisted cosmetic CI optimization, distinguished measured critical-path impact from runner cost, and maintained `UNKNOWN` where branch protection/runtime acceptance were inaccessible. It also surfaced the `baseline missing = green` and uniform normalization counterexamples.

Potential refinement of the skill: explicitly require a *truthfulness classification for a quality gate whose successful exit means no evidence was compared*. No extra top-level skill is needed. This report is one host-executed application with real read-only GitHub evidence and synthetic counterexample math; it is **not** a blind original-versus-new A/B, actual target CI modification, measured benefit, or full production qualification. Status: REVIEWED / FINDINGS_VERIFIED_FROM_SOURCE / NO_CHANGES_APPLIED.
