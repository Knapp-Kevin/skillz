# Security evidence registry

This directory stores persisted exact-version skill-package security evidence.

Security evidence is intentionally separate from provenance under `registry/skills/` and semantic quality evidence under `registry/verification/`.

**First-party per-skill lookup:** [`first-party-package-lookup.json`](first-party-package-lookup.json) provides a compact keyed pointer for all 44 first-party package names, the historically recorded baseline state and whether baseline/candidate scans match the package tree at the recorded source snapshot. For deeper evidence inspect [the baseline](first-party-baseline-2026-10-10.json) or [the separate candidate scans](first-party-candidate-2026-10-10.json). A historical pass transfers **only to an identical exact package tree**. Do not use 21 nonmatching candidate passes for unchanged current packages; do not turn this index into a fresh security certificate.

**Current external-host receipts (2026-11-03):** [first-party, engine and draft-PR exact trees](external-host-skillspector-first-party-20261103.json) (72 records: main 25 passed / 1 failed / 25 incomplete; PR #686 5/5 passed; PR #673 10 passed / 3 failed / 3 incomplete) and [featured Valuable References](external-host-skillspector-featured-20261103.json) (20 records: 5 passed / 3 failed / 12 incomplete; all 20 package-tree identities verified). Pinned SkillSpector v2.12.0, `--no-llm --fail-on-findings --fail-on-incomplete`, run by an authorized external host. States are the fail-closed gate; proposed false-positive dispositions await maintainer acceptance. [Plain-English receipt](../../docs/reviews/2026-11-03-q8-external-skillspector-exact-tree-receipts.md).

**Direct static adjudication (2026-11-05):** [Three previously FAILED third-party Q8 package reviews](third-party-three-failed-static-dispositions-20261105.json) inspected nine material source files and three upstream root LICENSE files at independently checked pinned Git trees. [Review rationale](../../docs/reviews/2026-11-05-issue402-three-third-party-failed-static-review.md) distinguishes scanner-text false-positive hypotheses from concrete unremediated finance, DSP and compliance risks. This supplementary content record **does not change historical SkillSpector failure states** or authorize unchanged installation, execution or external-system operations.

Each persisted record must bind to an exact package identity and follow `docs/security-scanning.md`. A semantic `verified` or `validated` state never implies a security pass.

Do not commit secrets, model credentials, unrestricted raw external content, or reports whose licensing/terms prohibit redistribution. Normalize evidence when necessary while preserving the scanner identity, exact scanner revision, target identity, completeness/coverage, findings, dispositions, and final security state.
