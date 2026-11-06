# Issue #402: Job Search, Blender assembly and Ink playtest

**Date:** 2026-11-05. Direct review of three complete exact-pinned Q8 packages as **static source content**. [Machine review ledger](../../registry/security/q8-three-incomplete-jobsearch-blender-ink-static-dispositions-20261105.json) records 24 package-owned material files, three root MIT license notices, the complete Git package identities, original historical scanner report fingerprints, ten-axis ratings and precise risk holds.

No external package code, browser, job search, user's résumé, Blender project, compiler, remote service, subprocess or agent-host behavior was executed. The three reviewed pinned package trees still match their latest observed upstream trees. All historical NVIDIA SkillSpector states stay **INCOMPLETE** (not promoted), and **no unchanged-use approval** was granted.

| Exact source pin | Static quality score | Disposition |
|---|---:|---|
| [Job Search](https://github.com/wexxwuther/job-hunter/tree/8c03dd4c6b7af3583c8878aa2ed66d3adc54e0e5/job-search) | **12/20** | Hold scoring without repair: wrong salary lower bound, nonfinite scores, collapsing job seniority |
| [Blender Assembly Pitfalls](https://github.com/dcc-mcp/dcc-mcp-blender/tree/8d8027fe4377b4d399d545869fc11b80e04ff785/skills/dcc-blender-assembly-pitfalls) | **12/20** | Reference only; scene deletion and unreliable mesh verification |
| [IF Playtest Review](https://github.com/bladecoder/narrative-skills/tree/c0948f7970178b72bb9561030372e75d303d37b3/skills/if/if-playtest-review) | **15/20** | Reference only; scope file writes and compiler execution separately |

## Job Search

**Complete package:** `job-search/` at Git tree `9b240990f9b56f145cca59e658ed99a72e3cc7ff`, `SKILL.md` blob `690dadeec6b579a2c43fe51717de84b4f4069fcc`. All **21** owned files were inspected: SKILL and meta/changelog, five Python scripts, four tests, six references, two evaluation JSON fixtures and the continuity reference. Root MIT copyright Greg Borden, license blob `6a562c6df2c0907740b3b817e4eabb1229474293`. Current upstream head matches the reviewed package tree.

**HIGH, salary amount unit failure.** `scripts/normalize_salary.py:127–171` lists support for `180-220k` but parses independent first and second numeric matches, `180` and `220k`, without sharing the `k` suffix. This produces a **180 to 220,000** range rather than **180,000 to 220,000**, which can undermine the compensation floor and the user's view of market rates. Resolve shared unit conventions before filtering. This is a source-derived test case, not a claimed executed acceptance run.

**HIGH, nonfinite candidate score.** `scripts/score_posting.py:112–137,150–186` coerces numbers and clamps ordinary out-of-range values but does not reject NaN or infinity. Python floating point comparisons with NaN do not trip its clamps and can yield a nonfinite `weighted_global` value and invalid recommendation. `tests/test_score_posting.py` validates regular numbers, bools and strings, not NaN/infinity. The numeric scoring receipt cannot be relied upon as fully validated input.

**MEDIUM, misleading deduplication.** `scripts/dedupe_postings.py:95–140` intentionally strips `senior`, `lead`, `staff`, `principal`, and grade tokens before matching employer, title and location. This can merge genuinely different seniority-level vacancies, concealing openings the user may prefer. Preserve seniority or distinct employer requisition IDs.

**MEDIUM, private data and untrusted HTML.** `SKILL.md:49–75,206–224` reads a candidate's profile and writes scored postings plus an HTML view, with no explicit output escaping or per-destination write gate. A listing is **untrusted** external text, and the user's résumé and private workspace notes must not be exported or silently shared. Any HTML renderer must escape values/validate link schemes, and actual access remains host-authorized. No auto-apply/send authority exists in the source; preserve that boundary.

**MEDIUM, evidence overconfidence.** `references/posting-legitimacy-rubric.md` describes direct ATS and fresh listings as 'legitimate by default'. Those are good corroborating signs, not proof of a funded vacancy. The bundled outcome evaluation fixtures mark assertions `passed: false`; these are proposed tests, not observed successes. Do not turn deterministic math over LLM-assigned inputs into an empirically verified hiring prediction.

**Strengths:** separates match from legitimacy, warns about fake jobs and sensitive prerecruitment data, supplies multiple regional/niche boards and explicit source provenance, and tests score weights and query behavior. **Remediation:** shared-suffix salary tests, finite-number validation, seniority-preserving dedupe, HTML encoding and permission/retention controls, observed source-aware legitimacy calibration.

## Blender Assembly Pitfalls

**Complete package:** single `SKILL.md`, tree `f83613f8b12120860df008b04bd4e8b1dd131d22`, blob `32bbb06a433361cc80f569b4b4d80ce8687cc63c`. Root MIT copyright Long Hao, blob `6a4b18e6e58344c3bc6e182116dd13357678c097`. Current upstream package tree unchanged.

**HIGH, scene destruction in nonisolated use.** The runnable check in `SKILL.md:324–328,360–364` executes `bpy.ops.object.select_all` followed by `bpy.ops.object.delete()`, clearing the active scene. Its supplied CLI command (`--background --factory-startup`) launches a separate factory-started Blender process and therefore mitigates the *documented* path; it does **not** make copying this script into the user's open Blender scene safe. Require a dedicated empty verification scene, not implicit scene mutation.

**HIGH, bad volume measurement.** `SKILL.md:424–435` computes signed volume from only the **first three vertices** of each Blender polygon. Quads and larger n-gons require triangulation or a trusted evaluated-mesh volume calculation; this can omit part of the geometry while still reporting a successful normals/volume check. The document's own 24/24 measurement claim was not independently reproduced here.

**MEDIUM, negative-scale accepted.** `SKILL.md:436–440` asserts all applied scale components must equal positive one, but tests `abs(abs(s) - 1)`. That condition accepts a negative unit scale and may miss a mirrored/handedness-flipped object.

**Strengths:** detailed primitive sizing, connection-map planning, joint overlap and frame orientation checks with tolerances, and a separate headless factory-startup example. **Remediation:** preserve user scenes by design, triangulate volume, check positive scales and verify before advertising a usable live-scene checker.

## Interactive Fiction Playtest Review

**Complete package:** SKILL blob `e703f3c525fd62ba10cd887686d7eafa84dde13f` plus agent YAML `568e465a11ee4bd154f20d43c0ff9cedbdc06b49`, package tree `6c6b9028d81ed25a5504052de5c541913a1b4b16`. Root MIT copyright Rafael García Moreno, blob `6218ab7ce333ac012513c331f9df84b8550982dd`. Current upstream package tree unchanged.

The source gives a focused, genuinely useful method to identify unreachable passages, soft locks, inconsistent Ink state and missing progression paths. It deliberately limits itself to **review**, not rewriting the game's source, unless asked. No bundled executable or remote service exists.

**MEDIUM, unapproved output mutation.** `SKILL.md:15–31,42–48` commands an agent to write or update `06_playtest/route_matrix.md` and `06_playtest/playability.review.md` without a separate overwrite/merge rule for existing project files. A legitimate review request should not blindly replace existing notes.

**MEDIUM, compiler authority.** The optional `inklecate` run needs a separately authorized local executable and safe output destination. Compiler availability does not by itself supply user permission.

**MEDIUM, traversal coverage.** The source requests all significant route permutations but does not limit traversal depth, state-space size or sampling budget. Reports must distinguish verified paths from unexplored frontiers and never claim exhaustive coverage solely from an agent's prose.

**Strengths:** direct file/knot evidence, prioritization by blocker severity, explicit distinction between soft locks and optional dialogue, and preservation of author ownership. **Remediation:** bounded traversal ledger, output destination/overwrite approval and no implicit executable launch.

## Separate high-risk large-source exception: BRAINS Resume

The remaining candidate `BRAINS-Certified/BRAINS-resume-skill` has a pinned **root package tree containing 373 files** (`c22ace992dc202c79c2de28fc4565d4fbd977e71`), including sizeable application sources, documentation, tests and assets. The recorded consumer review previously flagged a contradictory 'no outbound network requests' privacy statement versus a bundled `jd_url_fetch.py` utility that can access URLs, plus version/branding discrepancies. That prior evidence identifies a **focused risk priority** but **does not qualify as a fresh, complete exact-package direct static inspection** of all 373 files in this tranche. This package is **not counted reviewed**, is not copied/installed, and must be handled in a dedicated deeper source scan.

## Counts and remaining work

With these three **complete pinned-source** reviews, the Q8 historically scanner-flagged direct static corpus reaches **24/40 = 7/7 historically FAILED + 17/33 historically INCOMPLETE**, leaving **16** historically incomplete source pins for initial security-content review. A separate known newer Rerun package remains **update-available/re-review required**, not automatically fresh. Historical Q8 scanner results remain **10 PASS / 7 FAIL / 33 INCOMPLETE**. None of these statuses authorizes unchanged use, installation, account access, external sending, host execution, scene deletion or file writes.

The [README progress SVG](../../docs/assets/q8-direct-static-risk-review-progress.svg) counts only verified source-ledger identities. The independent capability-domain dashboard remains unchanged because no new method was admitted. Issue #402 stays open for the remaining 16 and the broader security/freshness review, including the 373-file BRAINS exception and the newer Rerun content.
