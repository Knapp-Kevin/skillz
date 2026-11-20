# CI Guard v1.3: classification-first and budget-aware CI qualification

**Date:** 2026-11-20. **Decision:** Exact-version first-party source package is **static VERIFIED**, 19/20 under the [ten-axis rubric](../skill-verification.md). The original classifier's 16 executable tests and offline package closure pass. **Behavioral validation of generated workflows, cross-model effectiveness, monetary savings and portability beyond GitHub Actions are NOT RUN / NOT PROVEN.** This is not a release/deployment pass.

## Product requirement corrected

Earlier v1.2 referred to class-dependent risk and placement, but did **not** require classifying a change set before constructing generated CI workflows. An agent could generate an identical expensive matrix for a `README.md` patch and a runtime security patch. v1.3 now **requires a trustworthy change-classification decision before expensive dispatch** (or a verified reason every change requires identical checks), independent of model tier.

This is **one** budget-saving method. The 10-file package also includes affected-test selection, early failure ordering, cache and build-artifact reuse with trust constraints, matrix pruning, safe per-PR cancellation, bounded infrastructure retry and runner/setup cost accounting. Each is governed by failure detection, branch protection and true acceptance, not appearance or runner count.

## Exact source and complete package

Maintainer source: `skills/authored/ci-guard/`; original first-party MIT, no third-party skill text imported. Complete **ten files**: LICENSE, SKILL.md, four component Markdown files, two example files (adversarial Markdown + GitHub workflow), one executable Python classifier and one Python test file.

- **v1.3 SKILL.md Git blob:** `f314ca9afe746af8f154447987ee59d29e7198fb`
- **v1.3 complete package Git tree:** `77450795ccb8a1cda65414406232f9a579596947`
- **Prior v1.2 SKILL.md blob:** `a98f04ad42fedec08d316605ba7d390c7de3b5f1`
- **Prior v1.2 tree:** `950bf5db6b9740bdd3fa92721ffb5a8a0fb9c258`; historic original review 2026-11-19 remains in [v1.2 closure review](2026-11-19-ci-guard-offline-package-closure.md).

No dependency on central Skillz governance files, sibling skills, network, paid services, provider API or new permanent workflow. The new GitHub workflow is a **bundled template only**, not an installed or live workflow. Its unconfigured full-qualification script fails instead of falsely passing; consumers must bind it to their actual repository tests. Python 3 and Git are optional tools **only** to run the bundled classifier, not prerequisites for the skill's textual analysis.

## What was actually executed

[Bounded one-shot qualification run #44784919638](https://github.com/Knapp-Kevin/skillz/actions/runs/44784919638) on a GitHub Linux runner:

- `python3 -m unittest discover -s examples -p test_change_classification.py -v`: **16/16 PASSED**; includes a real disposable Git diff across docs edit, a renamed docs→Python path, and a Git symlink replacement.
- Whole package closure: **10/10 tracked source files** assessed, Python syntax parsed, all local Markdown links resolved inside the package. Generated `__pycache__` from the test runner is **not** considered a distributed file. The first one-shot runs failed precisely because this byproduct was mistakenly counted; the corrected check passed and the temporary workflow was deleted.
- Original real CLI fixture: `README.md` + `docs/usage.md` -> `docs` route; `run_python=false`, `run_full=false`.
- Negative routing: workflow/security/release/dependency changes, unknown files and symlinked docs fail to the `full` route; Python-only changes select Python; mixed docs/Python selects both. Exact Git commit refs are required for production mode. Missing source control evidence prevents a reduced-check decision.

[Source classifier](../../skills/authored/ci-guard/scripts/classify_change.py) · [Test fixtures](../../skills/authored/ci-guard/examples/test_change_classification.py) · [Bounded GitHub example](../../skills/authored/ci-guard/examples/classified-github-pr.yml)

## Controls and known limits

- **Skip semantics:** GitHub documents that skipped jobs may report success and workflow-level path-filter skips can leave required checks pending. The bundled example uses a stable, `always()`-emitting aggregation job that checks whether selected jobs *actually* succeeded, and retains independent required checks. See [GitHub required checks documentation](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks).
- **Trust:** The example reads a PR's changed tree as data but executes classifier code from the trusted base revision, with read-only checkout and no PR secrets. Do not use privileged `pull_request_target` to run untrusted fork code.
- **Conservative scope:** This is a portable *example* selector only for ordinary documentation and Python code changes; unknown languages, dependency/build/policy changes, symlinks/modes and unknown paths select FULL. It is **not** a universal dependency graph; a real repository may require even README changes to run more checks when README is a material release/contract input.
- **Required baseline:** The template does not replace security, branch protection, platform and release tests. Existing protected checks cannot be removed merely because the new gate emits success; actual repo owners must qualify and explicitly authorize a migration.
- **Unmeasured:** No real third-party PR pipeline was installed; no end-to-end `pull_request` run of the example template was observed. **No measured saved minutes, saved actions budget, reduced CI bills or faster production outcome.** The positive outcome so far is executable routing logic plus static source/package verification.

## Static rubric (19/20)

| Dimension | Score | Basis / limitation |
| --- | ---: | --- |
| Trigger precision | 2 | Explicit CI review/generation; no assumption of write authority |
| Procedural clarity | 2 | Mandatory pre-dispatch classification with concrete 10-step procedure |
| Authority and safety | 2 | Trusted base, minimal token, no secrets, no implicit write permission |
| Failure handling | 2 | Missing/ambiguous diff and selected skip fail closed |
| Evidence discipline | 2 | Pin, actual negative tests, observed versus modeled budget separation |
| Dependency coherence | 2 | 10 files and local references verified, optional Python 3/Git only for CLI |
| Portability honesty | 1 | Full executable template supports GitHub Actions/Python; other providers require adaptation |
| Usefulness/differentiation | 2 | Original class-based dispatcher and seven additional cost levers |
| Adversarial resilience | 2 | Renames/symlinks, unknown files and trust-boundary tests |
| Effectiveness design | 2 | Expected to skip irrelevant tests while preserving core checks; savings unmeasured |

**Next independent qualification:** With a separately authorized consuming repository, run the template with its real tests and existing branch protections; compare docs-only and code/security change classes, inspect stable final check results, verify a seeded failure cannot bypass a required gate, and measure runner minutes and critical-path latency before accepting real budget savings. Do not upgrade to `validated` from the existing synthetic or unit tests.
