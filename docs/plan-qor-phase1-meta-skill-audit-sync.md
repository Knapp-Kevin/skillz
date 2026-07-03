# Plan: Meta series completion — skill-audit + skill-sync

**change_class**: feature

**doc_tier**: standard

**boundaries**:
- limitations: audit validates structure and script health, not skill *quality* (that remains model judgment); sync targets local filesystem destinations only.
- non_goals: no gated SDLC semantics (Qor-logic's domain); no network operations; no auto-installation of third-party skills.
- exclusions: vendor/ trees are never audited for compliance with this repo's conventions and never synced.

## Open Questions

None.

## Locked Decisions

- **LD-1** Shared frontmatter parsing moves to `scripts/lib/frontmatter.ts`; `scripts/build-index.ts` is its only existing consumer and is refactored to import it. Grep-evidence: `git show HEAD:scripts/build-index.ts | grep -nE 'function parseFrontmatter'` -> `27:function parseFrontmatter(md: string): Record<string, any> | null {` (sole definition site in repo; no other file defines or imports a frontmatter parser).
- **LD-2** Meta-tooling skills declare `repo-bound: true` in frontmatter metadata; `sync.ts` excludes repo-bound skills from deployment. Rationale: their scripts import `scripts/lib/` and operate on this repo's tree, so a standalone copy in `~/.claude/skills/` would be broken by construction.
- **LD-3** `sync.ts` is dry-run by default; `--apply` performs changes. Matches ARCHITECTURE_PLAN.md load-bearing rule 3 (read-only by default).
- **LD-4** Registry lint enums mirror `docs/evaluation-framework.md`: statuses `adopted|sandbox|track|rejected|quarantined`, permission tiers `read-only|plan-only|generate|staging-write|production-write|identity|cost|destructive`. Grep-evidence: `git show HEAD:docs/evaluation-framework.md | grep -nE '^\| .adopted.'` -> `| `adopted` | Approved for use; indexed and installable. |` (status table present; tier table under "## Permission tiers").

## Phase 1: skill-audit

### Affected Files

- tests/skill-tools.test.mjs — NEW; behavior tests for audit.ts (and Phase 2 sync.ts) via child-process invocation against fixtures
- tests/fixtures/bad-skill/SKILL.md — NEW; deliberately invalid skill (name/dir mismatch, no description)
- tests/fixtures/bad-registry.yaml — NEW; registry with a `status: yolo` entry (invalid-enum fixture)
- scripts/lib/frontmatter.ts — NEW; extracted `parseFrontmatter` + `truncate` from build-index.ts (LD-1)
- scripts/build-index.ts — MODIFIED; imports from scripts/lib/frontmatter.ts, local definitions removed; preserves the prior `generated` stamp in index.json when output is otherwise unchanged (index idempotency, required for the `git diff --exit-code` CI check to be passable)
- skills/skill-audit/scripts/audit.ts — NEW; repo validator
- skills/skill-audit/SKILL.md — NEW; `repo-bound: true`

### Changes

`audit.ts` validates, in order, printing findings and exiting 1 on any FAIL (0 on clean, warnings allowed):

1. Every `skills/<dir>/SKILL.md`: frontmatter parses; `name` == directory name; `description` non-empty and contains "Use when"; `metadata.version` present.
2. Every `skills/<dir>/scripts/*.ts`: `node <file> --help` exits 0 (spawned, 30s timeout).
3. `registry/candidates.yaml`: every entry has `id`, `status` in the LD-4 status enum, `permission_tier` in the LD-4 tier enum, non-empty `rationale`; `status: adopted` entries with `resolved_path` must point to an existing path.
4. WARN-only: `INDEX.md` older (mtime) than any `skills/**/SKILL.md` → "index stale, run build-index".

Registry parsing is a purpose-built block parser for this file's regular shape (documented constraint in the file header), not a general YAML parser.

### Unit Tests

- tests/skill-tools.test.mjs::audit-fails-on-bad-skill — runs `node audit.ts --skills-dir tests/fixtures` and asserts exit code 1 AND stdout names the `bad-skill` name/dir mismatch. Fails if validation silently passes broken input.
- tests/skill-tools.test.mjs::audit-passes-on-repo — runs `node audit.ts` at repo root and asserts exit code 0. Fails if the repo itself drifts out of convention.
- tests/skill-tools.test.mjs::audit-rejects-bad-registry-status — runs audit.ts with `--registry tests/fixtures/bad-registry.yaml` (entry with `status: yolo`) and asserts exit 1 AND the finding names the invalid status value.

## Phase 2: skill-sync

### Affected Files

- tests/skill-tools.test.mjs — MODIFIED; adds sync behavior tests
- skills/skill-sync/scripts/sync.ts — NEW; deployment tool
- skills/skill-sync/SKILL.md — NEW; `repo-bound: true`

### Changes

`sync.ts` deploys **portable** local skills (frontmatter without `repo-bound: true`) to targets. Dry-run by default (LD-3): prints per-skill per-target planned action (`create`, `update`, `up-to-date`, `skip:repo-bound`). `--apply` executes.

Targets (composable flags):
- `--claude-user` — junction (`fs.symlinkSync(..., "junction")`, no admin needed on Windows) at `<claude-user-root>/<name>` pointing to the skill directory. `<claude-user-root>` defaults to `~/.claude/skills` and is overridable via `--claude-user-root <path>` so tests can exercise the junction path under a temp root.
- `--dest <path>` — recursive copy of each portable skill directory; drift = any file content differs (byte compare).
- `--coreforge <path>` — per skill, writes `<path>/<name>/manifest.json` derived from frontmatter (skillId, name, version, description, category, entryPoint: SKILL.md, runtime: typescript, permissions: []) plus a copy of SKILL.md and scripts/. Fulfils the ROADMAP `skill-sync` Synapse-manifest contract.

### Unit Tests

- tests/skill-tools.test.mjs::sync-dry-run-mutates-nothing — runs `node sync.ts --dest <tmp>` (no `--apply`) against a temp dir and asserts the temp dir remains empty AND stdout lists a `create` action per portable skill. Fails if dry-run writes.
- tests/skill-tools.test.mjs::sync-apply-copies-and-reports-drift — runs with `--apply --dest <tmp>`, asserts SKILL.md exists in tmp for a portable skill; mutates one copied file; re-runs dry-run and asserts that skill reports `update`. Fails if drift detection or copy breaks.
- tests/skill-tools.test.mjs::sync-excludes-repo-bound — asserts `skill-audit` and `skill-sync` appear only as `skip:repo-bound` in output and are absent from the tmp destination after `--apply`.
- tests/skill-tools.test.mjs::sync-coreforge-manifest-shape — runs `--apply --coreforge <tmp>`, parses the emitted manifest.json for a portable skill, asserts `skillId`, `version`, and `entryPoint === "SKILL.md"` match that skill's frontmatter. Fails if manifest derivation drifts from frontmatter.
- tests/skill-tools.test.mjs::sync-junction-under-temp-root — runs `--apply --claude-user --claude-user-root <tmp>`, asserts a junction/symlink exists at `<tmp>/claude-pulse` resolving to the skill directory AND no repo-bound skill entry exists under `<tmp>`. Fails if the junction target path derivation or repo-bound exclusion breaks.

## Phase 3: Wiring

### Affected Files

- skills/skill-audit/SKILL.md, skills/skill-sync/SKILL.md — (from phases 1–2) Execution Flow references verified
- README.md — MODIFIED; Meta tooling section (audit/sync commands), layout diagram updated
- ROADMAP.md — MODIFIED; skill-audit and skill-sync marked shipped
- INDEX.md, index.json — REGENERATED via build-index.ts (picks up the two new skills)

### Changes

Documentation currency only; no logic. Index regeneration is the LD-1 refactor's live verification: identical INDEX.md output modulo the two new skill rows proves the parser extraction preserved behavior.

### Unit Tests

- (covered by Phase 1's audit-passes-on-repo, which re-validates the finished tree, and by CI command `git diff --exit-code` freshness check below)

## Definition of Done

### Deliverable: skill-audit

- **D1**: The repo can validate its own conventions mechanically; drift is a failing exit code, not a code-review catch.
- **D2**: `skills/skill-audit/scripts/audit.ts`, zero-dep, Node 22.18+/Bun, `--skills-dir`/`--registry` overrides for testability; ≤250 lines, functions ≤40 lines, nesting ≤3.
- **D3**: Skill registered in regenerated INDEX.md; plan/audit/implement gate artifacts under `.qor/gates/2026-07-03T2023-ca9b2c/`; ledger entries in docs/META_LEDGER.md.
- **D4**: tests/skill-tools.test.mjs::audit-fails-on-bad-skill — exit 1 + named finding on fixture; ::audit-passes-on-repo — exit 0 on real tree.

### Deliverable: skill-sync

- **D1**: One command deploys portable skills to any local consumer (Claude Code user dir, arbitrary dir, COREFORGE manifest form) with visible drift.
- **D2**: `skills/skill-sync/scripts/sync.ts`, same runtime/razor constraints; dry-run default, `--apply` gate.
- **D3**: Same gate/ledger surfaces as above; ROADMAP row flipped to shipped.
- **D4**: tests/skill-tools.test.mjs::sync-dry-run-mutates-nothing, ::sync-apply-copies-and-reports-drift, ::sync-excludes-repo-bound, ::sync-coreforge-manifest-shape, ::sync-junction-under-temp-root.

## Feature Inventory Touches

None — this plan touches repo tooling, skills, tests, and docs only (no `src/`); block declared empty per plan schema allowance.

## CI Commands

- `node --test "tests/*.test.mjs"` — runs all behavior tests for audit.ts and sync.ts (glob form; the bare-directory form fails on Node 22.22 Windows builds)
- `node skills/skill-audit/scripts/audit.ts` — repo self-validation must exit 0
- `node scripts/build-index.ts` — index regeneration must succeed post-refactor
- `git diff --exit-code INDEX.md index.json` — run immediately after the previous command once the Phase-3 regeneration is staged; a second regeneration must be a no-op, proving the LD-1 parser extraction preserved generator output (determinism/freshness check)
- `node skills/skill-sync/scripts/sync.ts --dest %TEMP%\skillz-sync-check` — dry-run must exit 0 and mutate nothing
