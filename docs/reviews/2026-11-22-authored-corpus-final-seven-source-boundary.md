# Final authored corpus adversarial pass: optional JSON input authority boundaries

**Date:** 2026-11-22. **Scope:** seven remaining authored skills under #843.
**Baseline:** exact public `main` at
`49ca7cfa2f5f8d99f58ef2f5065642ae75b6beec`.
No private consumer project, external repository name or account is
required for these reusable first-party skill corrections.

## Threat model and triggered repair

Four independent offline Python utilities accepted user-supplied JSON
paths. Three read `args.input.stat()/open()` without checking if the
path pointed through a symlink. The Phase-3 policy lab checked that
the final manifest file was not a symlink, but overlooked a symlink
in its parent path. In both cases a user-visible path can name a
different filesystem location than intended. This is a **real
source-boundary defect**, not evidence of malicious exploitation.

Changes are narrowly scoped to the optional checker path preflight.
On the exact caller-provided absolute path, reject the file and
**every symlinked ancestor before stat or open**. No new file read,
network, write authorization, evaluator control, preference storage,
or automatic discovery is introduced.

| Skill | Baseline → corrected | Current complete package Git tree | New negative tests |
| --- | --- | --- | --- |
| Agent Failure Boundary Analysis | 1.2.0 → 1.2.1 | `0b23fbf43fb69b67523fc151a6460d8d60ba15f7` | symlinked incident JSON file + parent |
| Decision Tradeoff Workbench | 1.2.0 → 1.2.1 | `e73108630e053dacd700693dd24cc48110d70a72` | symlinked scored-comparison JSON file + parent |
| Repository Delivery Assessor | 1.4.0 → 1.4.1 | `e210b1646f679e01017283ece402395e402798fe` | symlinked authorized snapshot file + parent |
| Recursive Refinement Trace | 0.3.0 → 0.3.1 | `d46950b4d62d3eae06080b980b3ed7c8d8767014` | Phase-3 manifest symlink + linked parent |

**Positive-preservation cases:** normal regular-file input still
executes the original checks with its provenance limits; wrong
scope, missing trace receipts, failed/unknown hard gates, stale
required checks, evaluator drift, false cost savings and incomplete
heldout qualification are not reinterpreted as successful.
The input preflight is a lexical check and is **not** protection
against a hostile, concurrently replacing filesystem. That requires
a separately authorized host-enforced immutable snapshot or a
descriptor-enforced sandbox. Do not claim real source authenticity.

## Independent last-three complete-package dispositions

**Technology Change Intelligence v1.2.5:** NO_CHANGE_STATIC.
Eleven-file package, exact tree
`7aa1d44926dc7eeda91ac71f7ddebd3cf34772b7`.
Seventeen named specialist profiles plus open-topic discovery and
interest-first routing were checked for their distinct source lanes,
date-bounded provenance, opt-in adjacent exploration and no fake
persistent subscription. A one-off supplied topic must be answered
without an onboarding obstacle. An unknown existing-connector
inventory is `NOT_CHECKED`, not a fabricated capability gap.
Positive-preservation: existing named routes retain their
specialist verdicts; privacy, source dates, and corrected exclusions
stay binding. Host subscriber interviews and live media
relevance NOT_RUN.

**Skill Trial Evidence Auditor v0.1.0:** NO_CHANGE_STATIC.
Eight-file package, exact tree
`22dc96c351ffcf9c77b81c613415d9010b16984f`.
Inspected paired treatment/baseline input requirements, isolated
holdouts, source/fingerprint constraints, treatment trigger and
non-trigger controls, leakage exclusions, authority breaches,
duplicate/repeated task IDs and zero-baseline effect claims.
Optional `audit_trials.py` is read-only aggregate/internal
consistency only; it explicitly returns source and independent
host authentication FALSE even when user-supplied emulated
statistics look favorable. Positive-preservation: genuine host
comparison is neither blocked nor impersonated. Real model-host
comparative study NOT_RUN.

**Evidence-Driven Refinement Loop v0.3.4:** NO_CHANGE_STATIC.
Ten-file package, exact tree
`463c5c51e3a1c2469420cfa2fde87c39967655a1`.
Inspected source-vs-user preference separation, stop/HOLD governance,
default nonpersistent usage, POSIX private overlay authorization,
fixed schema/allowlist, readback, symlink and replaceable-directory
constraints, explicit revocation, version mismatch and absent-storage
fallback. Positive-preservation: user preference never overrides
correctness/safety/evidence or becomes a hidden task scheduler.
Real agent-host preference handling NOT_RUN.

## Acceptance evidence and limits

- All **seven** current complete standalone package file counts, Git
  trees and SKILL entrypoint blobs matched the authored index at
  baseline. Package-local relative Markdown links resolved.
- New source changes are pinned in exact updated provenance,
  verification and authored index. All four packages keep their
  original first-party MIT license file and practical core task.
- One **path-scoped** GitHub Actions workflow tests only these
  changed Python packages in a single 5-minute-capped runner, without
  matrix/bootstrap, and **skips expensive runner allocation for
  drafts**. Test run and exact HEAD must be independently verified
  before merge. Test method counts in source are not observed PASS.
- User-facing correctness, security under actively hostile
  concurrent path replacement, complete source authenticity,
  independent agent-host execution and production outcomes
  remain **NOT_RUN / NOT_VERIFIED**, not inferred from static scans.
- Do not close Phase-3 pilot and recursive improvement issues from
  source-only tests; live pilot authorization and observed
  effective-task improvements are separate gates.

**Disposition:** four narrow source ADAPT repairs; three
NO_CHANGE_STATIC findings. This review counts as source-complete
only after a merged PR and exact-source verification on live main.
