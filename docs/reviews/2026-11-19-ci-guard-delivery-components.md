# CI Guard and delivery components: exact-package static review (2026-11-19)

## Decision and nonduplication

- **New top-level CI Guard**, `skills/authored/ci-guard/`, owns check-level assurance, actual detection, skip/status trust, conditional placement, CI metrics and experiment/rollback decisions. Exact SKILL Git blob `80d9cc0eec15dae1d23c0e0bb24ff6b69c9fd698`; complete five-file package tree `05b7339ef03657a74d675cf795650434513083f1`.
- **Extend rather than clone Repository Delivery Assessor** at `skills/authored/repository-delivery-assessor/` v1.3 with three selectively invoked components: issue-resolution stewardship, delivery-momentum triage, and delivery-evidence validation. Exact SKILL blob `75c09e83d13a388e591f384f8029090edbe0bc50`; six-file package tree `58662de287377f9b479d80cfa92e454413f9dc0e`.
- Existing source-debt triage remains the owner of TODO/FIXME annotations, Claim Evidence Adjudicator remains the owner of general factual assertion review, and Agent Failure Boundary Analysis remains incident-root-cause focused. No historical skills retired. No new universal state store, scheduled task or automatic governance gate.

## Structured semantic review

Using `docs/skill-verification.md` 10 dimensions, static rubric estimate: 18/20 each (both packages). Trigger 2; procedure 2; authority 2; failure handling 2; evidence 2; dependencies 2; portability 1 (provider semantics and host API availability vary); differentiation 2; adversarial resistance 2; effectiveness design 1 (no observed production delta). No hard fail found in the reviewed instruction package. This is reviewer static characterization, **not host validation**.

CI Guard fixture contracts C1-C10 cover positive optimization, unique security detector, Windows flake, self-blocked gate, release matrix, ignored scanner alerts, illusory integration, privileged fork, missing required check, and docs-vs-runtime risk. Negative controls cover absent metrics, stale SHA, speculative scanner, no write authority, unknown branch rules and loss of unique detection. All case contracts are present in the exact package.

`docs/evals/receipts/2026-11-19-ci-guard-decision-emulation.json` records **13/13 deterministic decision-function emulations** (ten named cases and three negative controls), with mutation disabled unless separately authorized. The emulator is deliberately narrower than the prose skill; it does **not** show an agent would obey the instructions, that prior skills have parity, or that runtime/cost improves. Component assertions and Git SHA fingerprints were verified against newly created blobs, not an external host.

## Real repo observational exercise (read-only)

Inspected `MythologIQ-Labs-LLC/qortara-logic` at commit `d0f8143e7b7ed48779b1376b9bc6ba15337a9934`, GitHub Actions `.github/workflows/ci.yml` blob `7e15dce2f5be229da4ef10ccc53a87806dcee1ff`. The `test` job has OS and Python matrix axes, uses `timeout-minutes: 90`, and runs `python scripts/verified_test_run.py` twice for stated determinism. It deliberately limits usual PR legs to Linux and broadens on main/`ci:full`; this is an existing evidence-backed placement mechanism, not a request to remove release/security tests. `permissions: contents: read` is explicitly configured.

**Actionable measured-gap recommendation:** compare second-pass independent failure detection with the first pass and its additional critical-path time on comparable exact-head runs. Only if a seeded nondeterministic failure remains detectably covered should the second pass be reduced or relocated. No durations, job history distribution, branch protection, installed runtime or outcome were qualified, so speedup and safe reduction remain **UNKNOWN**. No external repository config was modified.

## Index repair and limitations

The pinned baseline capability directory still contained **18** old skill-blob/tree pairs inconsistent with the canonical authored index. This PR synchronizes those metadata pointers to canonical index fingerprints while retaining their current reviews and historical predecessor review notes. This is pointer reconciliation, **not** a claim of new content review of those packages.

The repository remains passive. New CI Guard and updated assessor are static-reviewed with `validation_status: not-run`; neither new skill's independent model-host behavior, 1.5x lift, measured CI cost reduction, or production safety is established. No original/historical skills are retired by this PR.
