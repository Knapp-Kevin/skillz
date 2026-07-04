# Plan: Issue #6 — Vendored-source freshness and submodule refresh workflow

**change_class**: feature

**doc_tier**: minimal

**session**: 2026-07-04T0632-7cc26a

**scope**: GitHub issue #6. Documentation + skills-pulse spec; no automation of refreshes (non-goals: no auto-adopt, no auto-merge, vendored ≠ blanket-trusted for write tiers).

## Open Questions

None. The issue's own recommendation (CI validates pinned state only; upstream drift is scheduled/manual via skills-pulse) is adopted as the decided posture.

## Ground Truth

| Fact | Value | Evidence |
|------|-------|----------|
| Vendored sources | 6 submodules, pinned | `git submodule status` → dd091bc (kwp), 9d2f1ae (anthropic), f8a72b9 (vercel), 32cad4e (microsoft), 8f8c72b (azure), ff1481a (aws) |
| skills-pulse coverage today | refresh command + "Submodule refresh needed" output section exist; NO pinned/upstream SHA reporting, NO change classification | grep of skills/skills-pulse/SKILL.md steps 1, 4, output |
| CI touches submodules | checkout recursive; validates pinned state only (index regen against pinned trees) | .github/workflows/ci.yml |
| No freshness surface exists | — | no docs/vendor-freshness.md; SYSTEM_STATE has a one-line vendor metric only |

## Phase 1: freshness workflow + surface

### Affected Files

- `docs/vendor-freshness.md` — NEW: (a) the refresh workflow — when (weekly with skills-pulse, or when it flags activity), the command sequence (`git submodule update --remote <path>` per source → review upstream changes `git -C vendor/<x> log --oneline <pinned>..HEAD` → classify docs-only / skill-content / tooling → `node scripts/build-index.ts` → update `registry/candidates.yaml` if adoption/permission posture is affected → commit the pin bump with the classification in the message); (b) review-before-commit is mandatory — a refreshed submodule never lands unreviewed; (c) the freshness table: source | pinned SHA | last checked | last refreshed | classification of last delta; (d) CI posture stated: CI validates the pinned state only (recursive checkout + index idempotency); upstream-drift detection is scheduled/manual through skills-pulse, never a blocking PR check.

### Unit Tests

None — workflow documentation; the mechanical surfaces it references (index idempotency, recursive checkout) are already CI-proven (FX01, FX12).

## Phase 2: skills-pulse freshness reporting spec

### Affected Files

- `skills/skills-pulse/SKILL.md` — step 4 and "## Submodule refresh needed" output section gain the per-source report fields: current pinned SHA, latest upstream SHA/release where detectable (`git ls-remote <url> HEAD`, releases via `gh api` when available), refresh-needed verdict, and likely-classification (docs-only / skill-content / tooling — from upstream commit paths); pointer to docs/vendor-freshness.md as the governing workflow; version 1.0.0 → 1.1.0

## Phase 3: references + governance

### Affected Files

- `README.md` — vendored-sources section gains one line pointing at docs/vendor-freshness.md
- `docs/SYSTEM_STATE.md` — queue row final update; vendored metric row links the freshness surface
- `INDEX.md`, `index.json` — regenerated (skills-pulse version bump)

## Definition of Done

### Deliverable: freshness is a governed loop, not a hope

- **D1**: An operator can answer "how stale is each vendored source and what would refreshing cost" from one document, and the refresh path requires review before commit.
- **D2**: docs/vendor-freshness.md exists with workflow + table + CI-posture statement; skills-pulse spec carries the four report fields.
- **D3**: README references the surface; ledger entries; SYSTEM_STATE current.
- **D4.d**: waiver — the deliverable is workflow documentation; its mechanical substrate (pinned-state validation) is already proven by FX01/FX12 CI runs. **Follow-up phase**: none required; first real refresh exercises the workflow.

## Feature Inventory Touches

None — docs + instruction-skill spec only.

## CI Commands

- `node --test "tests/*.test.mjs"` — 15/15
- `node skills/skill-audit/scripts/audit.ts` — exit 0
- `node skills/skill-audit/scripts/risk-audit.ts` — exit 0
- `node scripts/build-index.ts` then commit regenerated index (skills-pulse version bump)
