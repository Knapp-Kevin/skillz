# Plan: Issue #2 — GitHub Actions CI for tests, audit, and index freshness

**change_class**: feature

**doc_tier**: minimal

**session**: 2026-07-04T0632-7cc26a

**scope**: GitHub issue #2. One workflow file + proof-path references. No deployment, no submodule auto-refresh, no dependency installation.

## Open Questions

None. Issue #2 fully specifies checks, triggers, and non-goals.

## Ground Truth

| Fact | Value | Evidence |
|------|-------|----------|
| No CI exists | `.github/` absent | `ls .github/workflows` → no such directory |
| Validation commands | 4 (tests, audit, build-index, diff) | issue #2 Required checks; identical to plan-qor-phase3 CI Commands |
| All checks green locally | yes | cycle-1 verification run (11/11, 48/0, idempotent) |
| Node requirement | 22.18+ (native .ts type-stripping) | INDEX.md header "Bun or Node 22.18+, zero install"; local v22.22.3 |
| Submodules required by build-index | yes, 6 public GitHub repos | `git submodule status` → 6 rows, all github.com URLs |

## Phase 1: workflow file

### Affected Files

- `.github/workflows/ci.yml` — NEW

### Changes

Single job `validate` on `ubuntu-latest`; triggers `push: branches: [main]` + `pull_request`; steps: `actions/checkout@v4` with `submodules: recursive`, `actions/setup-node@v4` with `node-version: '22'` (latest 22.x ≥ 22.18 — type-stripping available), then the four declared commands as three named steps (build-index + diff combined). No package installation (zero-install contract). No Bun matrix leg (issue: only after Node leg is green).

## Phase 2: proof-path references

### Affected Files

- `docs/FEATURE_INDEX.md` — NEW row FX12
- `README.md` — one sentence in §"The repo maintains itself" bullet 4

### Changes

- FX12: "CI enforcement of declared validation commands (PR + push to main, submodules recursive) | `.github/workflows/ci.yml` | the workflow run itself; drift in INDEX.md/index.json fails `git diff --exit-code`".
- README bullet 4 gains: CI runs the same commands on every PR and push to main (`.github/workflows/ci.yml`).

## Definition of Done

### Deliverable: enforced validation on PR/push

- **D1**: Every PR and push to main mechanically re-proves tests, audit, and index freshness.
- **D2**: `.github/workflows/ci.yml` exists with recursive submodule checkout, Node 22 setup, and the four commands verbatim; no install step.
- **D3**: FEATURE_INDEX FX12 row + README reference; META_LEDGER audit/seal entries for this cycle.
- **D4.d**: waiver — an Actions run cannot execute pre-push (Review Boundary holds all pushes for user review). Local equivalent executed at substantiate: the four workflow commands verbatim + YAML parse check. **Follow-up phase**: first green Actions run after the user pushes this branch.

## Feature Inventory Touches

- entry_id: FX12 · operation: NEW · test_path: .github/workflows/ci.yml (the run itself) · test_descriptor: "a PR that breaks a behavior test, audit convention, or index freshness produces a failed check; a clean PR produces a green check"

## CI Commands

- `node --test "tests/*.test.mjs"` — 11/11 behavior tests
- `node skills/skill-audit/scripts/audit.ts` — exit 0, 48 skills
- `node scripts/build-index.ts && git diff --exit-code INDEX.md index.json` — index idempotent
- `python -c "import yaml,sys; yaml.safe_load(open('.github/workflows/ci.yml'))"` — workflow YAML parses
