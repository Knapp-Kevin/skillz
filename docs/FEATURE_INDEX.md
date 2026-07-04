# Feature Index

Maps every user-touchable feature to its implementation and its proof. Rows are stable IDs; the SG-035 acceptance question governs each test descriptor: "if the feature were silently broken but the artifact still existed, would this assertion fail?"

| ID | Feature | Implementation | Proof |
|----|---------|----------------|-------|
| FX01 | Skill index generation (local + 6 vendor trees, deduped) | `scripts/build-index.ts` | CI: regeneration succeeds + `git diff --exit-code INDEX.md index.json` (idempotency) |
| FX02 | Repo self-validation (frontmatter, script health, registry enums, index freshness) | `skills/skill-audit/scripts/audit.ts` | `tests/skill-tools.test.mjs::audit-fails-on-bad-skill`, `::audit-passes-on-repo`, `::audit-rejects-bad-registry-status` |
| FX03 | Skill deployment: dry-run default, `--dest` copy with drift | `skills/skill-sync/scripts/sync.ts` | `::sync-dry-run-mutates-nothing`, `::sync-apply-copies-and-reports-drift` |
| FX04 | Repo-bound exclusion from deployment | `sync.ts` (LD-2) | `::sync-excludes-repo-bound` |
| FX05 | Claude Code junction target with testable root | `sync.ts --claude-user[-root]` | `::sync-junction-under-temp-root` |
| FX06 | COREFORGE Synapse manifest emission (exact 8-key shape) | `sync.ts --coreforge` | `::sync-coreforge-manifest-shape` (full key-set assertion) |
| FX07 | Generic pulse collection (repos, orgs, search, changelogs, reddit) | `scripts/pulse-run.ts` + per-skill `sources.json` | `--help` contract enforced by FX02 (audit.ts covers repo-level `scripts/*.ts` since 2026-07-04); sources.json parse + fallback-marker checks enforced by FX02; live smoke qwen-pulse 2026-07-03 |
| FX08 | Watchlist intake scan | `skills/skills-pulse/scripts/scout.ts` | Manual smoke (live run 2026-07-03); `--help` contract enforced by FX02 |
| FX09 | Claude release digest | `skills/claude-pulse/scripts/pulse.ts` | Manual smoke (live run 2026-07-03); `--help` contract enforced by FX02 |
| FX10 | 44 instruction skills — 48 first-party minus 4 scripted (pulses, research, agent-ops, daily-ops, comms, life-ops, hygiene, meta) | `skills/*/SKILL.md` (no scripts) | FX02 convention checks + `tests/skill-tools.test.mjs::audit-reports-skill-count` (asserts validated count >= 46; intentional floor, not exact — index churn must not break the test) |
| FX11 | Multi-host deployment (`--hosts`: .claude/.kilo/.codex skill dirs of a target repo) | `skills/skill-sync/scripts/sync.ts` | `tests/skill-tools.test.mjs::sync-hosts-writes-three-host-dirs` (three paths + repo-bound exclusion) |
| FX12 | CI enforcement of declared validation commands (PR + push to main, submodules recursive) | `.github/workflows/ci.yml` | the workflow run itself; a PR that breaks a behavior test, audit convention, or index freshness fails the check (`git diff --exit-code INDEX.md index.json`) |

Rows FX08–FX09 carry script smoke-tests rather than automated behavior tests; upgrading them to fixture-based tests is acceptable future work but not currently required (network-dependent collectors).
