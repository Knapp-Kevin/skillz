# OpenClaw Agent Skills: final two exact-pin static reviews (2026-10-31)

## Macro-first source-family reconciliation

- Current source registry: `openclaw-agent-skills`, official-ecosystem, **tracked corpus** (not a wholesale admitted/installable set), root MIT, exact pin `6cd3366b10e2a8c5608265f692acf9f5da2b2448`.
- Independently enumerated pinned recursive Git tree: **8** canonical first-class `skills/<name>/SKILL.md` packages, **0** nested first-class packages, **0** duplicate/alias exposure paths. Existing companion pairs were `handoff`, `agent-transcript`, `behavior-validator`, `crabbox`, `readme-standard`, `session-viewer`: **6/8**, two genuine gaps, no prior `autoreview` or `beam` companion.
- This bounded final high-authority tranche completes **6/8 → 8/8**, gaps **2 → 0**, unchanged denominator **8**, admitted-source denominator delta **0**. Each package has its own exact-pin Git tree/manifest identity, last package-changing commit/date, dependencies, authority, taxonomy, score and explicit not-run evidence.
- Corrected a previous preliminary file-count description: the pinned recursive tree has **13 source-owned blob/symlink entries** under `autoreview` and **7** under `beam` (20 total), not the earlier provisional 16/9 that counted directory entries as files. `autoreview/CLAUDE.md` is a symlink to `AGENTS.md`, not a ninth skill. The 234 KB review helper and 251 KB test suite remain upstream-owned evidence, not repository-owned execution.

## Individual exact-version findings

| Package | Manifest blob | Package tree | Upstream last change | Decision |
|---|---|---|---|---|
| `autoreview` | `ffbcf92f4f9f6e213c3ca19d9dad990c2b131d22` | `b13bac8c660967da6b28cd32fb6bee95a3537cd8` | `b7c3d0827dfc7e66d579b171b44ac5a7354b0b49` (2026-08-30) | **REJECT unchanged 15/20** |
| `beam` | `8fac3d844bb4aadade27fdda4e50cea3b280aecd` | `e910a7830ca569d4f34b503ae674149ac7456124` | `6cd3366b10e2a8c5608265f692acf9f5da2b2448` (2026-08-30) | **REJECT unchanged 15/20** |

**Autoreview:** The manifest correctly demands explicit review invocation, a bounded target and no automatic PR/commit/merge preflight. Its helper pins Git scope, isolates model CLIs, performs pre-send TruffleHog scanning, filters sensitive paths and validates structured findings. Nevertheless, a review request is not a separate authorization to send confidential code, private diffs, prompt/dataset files, or private repository context to a selected paid external model. The default WebSearch path creates an additional disclosure surface without a specific data/recipient scope. Secret scanning does not detect all confidential business, personal or proprietary information. Source-owned CLI/tests/fixtures were inspected statically, not run. Preserve the strong target-pinning and isolation techniques as adaptation/checklist material, not an unchanged-use approval.

**Beam:** The manifest requires an explicit snapshot-sharing request, an endpoint, HTTPS, token handling, exact-session resolution, local sanitization, and separately requested persistent hooks. The bundled README confirms every `operator.read` user of the receiving Gateway can see the published catalog. A named Gateway and token do not establish the intended recipient audience, disclosure scope, retention, or downstream access policy. Regex-based redaction cannot prove no sensitive content remains; local `--dry-run` is useful but not disclosure approval. `Stop`/ `SessionEnd` hooks can persist future uploads beyond one snapshot without a bounded recurrence/revocation/data-scope contract. Preserve exact-match, size-bounding, HTTPS and safe-preview methods for adaptation; no upload or hook was performed.

## Systemic findings, omissions, and operational fit

- The source distinguishes read-only review from remote publication, but both can transmit private user/workspace content through authorized-looking helper flows. **Tool availability, review invocation, credential presence, and a named endpoint do not substitute for a complete data-disclosure boundary.**
- `autoreview` offers differentiated structured code-review isolation; `beam` offers exact-session sanitized sharing, unlike `session-viewer`'s local raw HTML. They are not duplicates of `handoff` or each other. Shared risk is provider/data egress and retention; `beam` adds persistent hook and receiver-audience risk.
- Full-package dependencies are characterized, including upstream executable tooling. No upstream source was copied, edited, installed, executed, or misclassified as `skillz` runtime. No model review, external scan, upload, hook, or behavioral acceptance was performed.
- The previously recorded 16/9 file-count estimate was an omission defect, now corrected with pinned-tree evidence. No new license ambiguity, nested first-class manifest, duplicate exposure, taxonomy addition, or admission was found. This source is **current-standard static-reviewed**, not automatically security- or behaviorally validated.

## Lifecycle and public accounting

- All **7** open issues and **5** open draft PRs were triaged against live main. Repair drafts #489 (29), #492 (5), #496 (2) remain disjoint in changed first-party manifests but share `registry/local-verification.json`. They require full pinned external SkillSpector v2.12.0 final-tree reports/digests, independent executed adversarial acceptance for **36** changed packages, and shared-registry reconciliation. Admission drafts #412/#413 require their separate exact-candidate security/behavioral qualification. All five are drafts, technically mergeable, with no review submissions, review threads, combined statuses, or PR workflow runs observed; none meets current readiness. No existing issue was evidence-complete for closure.
- Two new provenance + two new verification companions, **2 REJECT unchanged**, all security/behavioral states **not-run**. No source pin, source admission, repository-owned runtime, script, test, CI, scanner, scheduler or background process.
- Five public surfaces reconciled atomically: **44 first-party / 940 persisted third-party / 984 total** (819 registered/tracked + 121 candidate-only). OpenClaw **8/8**, zero gaps; registered/admitted denominators unchanged. Historical **44/938/982** checkpoint remains labeled historical.
- Next highest-priority action: obtain independent exact-package external qualification for the 36 changed first-party repair trees and reconcile the three shared-registry drafts before merging eligible repairs.
