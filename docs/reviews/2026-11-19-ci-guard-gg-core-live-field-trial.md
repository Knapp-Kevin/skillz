# CI Guard v1.1 capability-adaptive field trial: GG-CORE

**Date:** 2026-11-19  
**Execution:** one *observed ChatGPT/GitHub-connector, read-only assessment*, with source and CI-log inspection.  
**NOT a multi-model comparison, controlled A/B study, execution of GG-CORE binaries, or full behavioral validation.**  
**Skill under test:** `skills/authored/ci-guard/SKILL.md` Git blob `29de6cb583efaca3edac1ea39fa557909b17807b`, v1.1.0; optional `components/diagnostic-paths.md` blob `f72a40c5870592daf4a3169d24c8ec10934889a5`.  
**Target:** [MythologIQ-Labs-LLC/GG-CORE](https://github.com/MythologIQ-Labs-LLC/GG-CORE), `main@f917b18b18fb042d72b92484dc38661bf73e9bf1`. All inspected workflow/code files were read at that SHA. CI run observations are bound to their respective, separately identified run SHA. No repository mutation was made to GG-CORE.

## Authorized outcome and direct route

The task was to exercise CI Guard against actual GG-CORE CI and determine whether it can distinguish trustworthy assurance, weak comparison semantics, expensive controls and inaccessible evidence without imposing a mandatory component sequence. This host used read-only GitHub repository/content, workflow, job and decoded-log APIs.

At the frozen GG-CORE SHA, inspected the [Rust workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/f917b18b18fb042d72b92484dc38661bf73e9bf1/.github/workflows/rust.yml), [CodeQL](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/f917b18b18fb042d72b92484dc38661bf73e9bf1/.github/workflows/codeql.yml), two narrowly path-triggered model-free contract workflows, and [release workflow](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/f917b18b18fb042d72b92484dc38661bf73e9bf1/.github/workflows/release.yml). The Rust workflow runs cross-platform lint/tests, MSRV, five feature jobs, cargo-deny and model-free benches on pull requests and pushes to main. Release-only packaged GGUF inference is a distinct boundary: normal PR success does **not** qualify shipped Windows/macOS/Linux archives.

The [main Rust run #44578186275](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44578186275) and [CodeQL run #44578186105](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44578186105) both reported success at that SHA. These are source/CI outcomes, **not** end-to-end inference, release publication or customer acceptance.

## Guided route: distinguish comparison evidence from a green check

The optional [CI Guard diagnostic path](../../skills/authored/ci-guard/components/diagnostic-paths.md) instructs the agent to inspect comparator, baseline, measured cases and exact-run logs, rather than assume `PASS` means a real regression comparison.

Evidence inspected:

- [`core-runtime/scripts/perf_gate.py`](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/f917b18b18fb042d72b92484dc38661bf73e9bf1/core-runtime/scripts/perf_gate.py) blob `33da54fc5f76156cab9e6e2e4e7fec966d2fce0c`: returns exit 0 after explicitly printing *skip* if no baseline is found; otherwise compares available Criterion medians. At least five eligible measurements enable median-ratio runner-shift normalization. A uniform slowdown is normalized away; values under a 1,000 ns baseline noise floor are diagnostic only.
- [`core-runtime/scripts/test_perf_gate.py`](https://github.com/MythologIQ-Labs-LLC/GG-CORE/blob/f917b18b18fb042d72b92484dc38661bf73e9bf1/core-runtime/scripts/test_perf_gate.py) blob `6c72c5a5d3d9988c5e00426fe84486f45893efa0`: explicitly tests baseline-miss skipping, missing-current-result rejection, noise-floor behavior, uniform shift normalization and outlier rejection.
- The inspected [PR Rust run #44577590997](https://github.com/MythologIQ-Labs-LLC/GG-CORE/actions/runs/44577590997) at **`40ff0697c002598fb89b837ad41639967f0bd0ec`** was globally **failure** because formatting failed on three platforms. Its **benchmark job nevertheless succeeded**, and its decoded job log shows a restored baseline cache key `criterion-baseline-Linux-183409cf7908c479475d3c8d7991d07482260bcb`, **48 gated benchmarks**, a **1.01x** normalization factor and `perf-gate: PASS -- no median regression > 2.00x`. This was an actual comparison, not a cache-miss skip.
- The main run above **skipped** the PR-only comparison step, as specified by the workflow, while it ran benchmarks and wrote the new baseline. The unit negative-control step succeeded in both inspected Rust runs. Its success is evidence those fixture tests ran, not evidence a live-model benchmark threshold was met.

**Decision:** `KEEP` the benchmark smoke and negative controls. `VERIFY` comparison coverage for each PR conclusion; a successful job with no baseline must be reported as `NO_BASELINE / NOT_COMPARED`, not `COMPARED_PASS`. `VERIFY` absolute/systemic performance separately if it is a release criterion, because the deliberate relative normalization cannot detect a uniform product slowdown by itself. Do not disable native tests or remove an expensive check merely because a comparator has this limitation.

The observation **does not establish** that any actual PR suffered an undetected regression, that its comparator skipped, or that removing/replacing its benchmark job would improve wall-clock latency. Runtime comparison confidence and the claim of actual customer performance are separate.

## Bounded fallback: inaccessible authority surface

The classic `branches/main/protection` endpoint returned HTTP 403 `Resource not accessible by integration`. This is **not** evidence that protection is absent. The separately accessible [repository ruleset #14213663](https://github.com/MythologIQ-Labs-LLC/GG-CORE/rules/14213663) was active and exposed deletion, non-fast-forward, creation, CodeQL code-scanning and code-quality rules. It did not itself demonstrate effective required check-name enforcement for every PR path. Record **classic branch-protection and any inaccessible inherited rules as `NOT_ASSESSED`**; do not approve a protection change or infer a policy bypass.

The two model-free contract workflows use path-filtered PR triggers; lack of those checks on unrelated changes does not itself prove either a failure or trustworthy required-check configuration. The relevant per-path status obligations must be checked before redesigning CI.

## Capability-adaptive observations

| Route tested on this host | What was actually observed | Interpretation |
| --- | --- | --- |
| Direct | Read live pinned workflows, active ruleset and check/job receipts without a preliminary form or mandatory module chain | **Observed:** productive, bounded analysis was possible |
| Guided | Consulted only the diagnostic branch relevant to green-but-not-compared claims; inspected comparator and actual decoded job log, correcting the naive assertion that every green benchmark run skipped comparison | **Observed:** targeted scaffolding matched the uncertainty; no controlled proof that guidance caused the decision |
| Fallback | Continued safe review after a genuine 403, distinguished visible ruleset from inaccessible classic protection and left exact unknowns | **Observed:** source/authority boundary preserved |
| Stronger equivalent method | Replaced a purely hypothetical scenario with source + job-step + decoded-log evidence at a pinned SHA | **Observed:** no artificial restriction on using stronger evidence |
| Low-context/weaker-model and cross-model | No independently observed run by a separate host/model using only the entrypoint | **NOT_ASSESSED** |

No mutation, external code execution, new scanner, scheduled task, CI rule change or altered GG-CORE workflow was performed. No performance savings, reliability uplift or 1.5x skill improvement is quantified. This is **one host-observed evidence case**, not proof of the broader model-capability claim or a reason to promote the entire skill to `validated`.

## Decisions and next discriminating work

1. **Preserve controls.** No production CI edit is justified by this field trial alone. The failing formatter was a real stop on one PR; the benchmark job was green in the same run. A whole-workflow failure must not be mislabeled a benchmark failure.
2. **Improve assurance semantics where warranted.** In an independently authorized GG-CORE change, expose distinct `COMPARED_PASS / NOT_COMPARED / INVALID` evidence states (without confusing shell exit status with comparison status); preserve missing-current-result and outlier negative tests. If systemic performance is an explicit release promise, qualify it on a comparable runner or with a separate bound, not by deleting normalized checks.
3. **Test a second, genuinely independent host/model.** Supply the same pinned GG-CORE evidence first with only the CI Guard entrypoint, then conditionally the targeted component. Compare actions and claims, not verbosity or model labels. Include one deliberate cache miss, one valid comparison, and one inaccessible protection source; record observable transcript/tool results, exact package fingerprint and permissions before claiming improvement.
4. **Review other authored entrypoints for genuine ceilings.** A coarse pass found candidate non-security output/procedure quotas in narrative and incident skills. They need context-sensitive review and targeted changes where they actually prevent authorized work; **no blanket corpus compliance pass** is claimed.

This field trial deliberately changes **review evidence only**, not source fingerprints, semantic grades, `validation_status`, or the standard adopted in [PR #771](https://github.com/Knapp-Kevin/skillz/pull/771).
