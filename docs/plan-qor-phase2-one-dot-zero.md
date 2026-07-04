# Plan: skillz 1.0 completion — backlog close-out

**change_class**: feature

**doc_tier**: standard

**boundaries**:
- limitations: instruction-skill quality is convention+eval verified, not per-use verified; gh-based hygiene skills require an authenticated `gh` CLI; the weak-model eval measures one skill (handoff-writer), not the whole library.
- non_goals: gated SDLC semantics; Gemini TOML host compilation (format conversion, deferred); vendoring additional third-party skills; network mutations.
- exclusions: vendor/ trees untouched; no automated registry edits beyond the human-directed application of the 2026-07-03 eval recommendations (operator commanded this cycle; recorded in decision log).

## Open Questions

None.

## Locked Decisions

- **LD-1** New `--hosts <targetRepo>` sync target copies each portable skill to `<targetRepo>/.claude/skills/<name>`, `<targetRepo>/.kilo/skills/<name>`, and `<targetRepo>/.codex/skills/<name>` (markdown hosts share the copy mechanism; Gemini excluded per boundaries). Host-dir names follow Qor-logic's host resolver convention. Grep-evidence: `git show HEAD:skills/skill-sync/scripts/sync.ts | grep -nE 'const targets'` -> `154:const targets: Array<{ label: string; fn: (s: Skill) => string }> = [];` (composable-target array the new target plugs into; repo-bound exclusion applies at line 166 dispatch, unchanged).
- **LD-2** B09 (migrate claude-pulse onto the pulse engine) is REJECTED: the bespoke `pulse.ts` undated-changelog cap has no engine equivalent (engine's changelog handler extracts dated lines or falls back to headers), and complecting the engine with per-source caps violates Simple-Made-Easy. claude-pulse keeps its script; BACKLOG B09 closes as rejected-with-reason.
- **LD-3** The 10 new instruction skills and inference-pulse follow the existing conventions enforced by audit.ts (name==dir, "Use when" description, metadata.version); none carry scripts; gh-based skills embed `gh`/git commands in Execution Flow prose (model runs them), consistent with zero-install. **skill-forge declares `repo-bound: true`** — it scaffolds skills in this repo's tree and regenerates this repo's index, so a deployed copy would be broken by construction (same rationale as skill-audit/skill-sync).
- **LD-4** B11 weak-model eval reuses the 2026-07-03 pre-registered rubric and scenarios verbatim (docs/evals/2026-07-03-handoff-writer.md) with both arms executed on the haiku model tier; same blind-judging protocol. New checks are NOT invented; tier is the only variable.
- **LD-5** Engine-consuming pulse skills are a deliberate third deployment class: **portable-with-fallback**. Every skill carrying a `sources.json` ships a standalone web-tool fallback in its SKILL.md ("engine is unavailable" marker), so deployed copies (sources.json travels with the directory) are degradedly functional without the repo engine. Grep-evidence: 14 of 15 sources.json skills already contain the literal marker `engine is unavailable` in SKILL.md (verified via Select-String this session); hf-pulse uses variant wording ("neither MCP nor the engine is available") and is standardized in Phase 1. The class becomes mechanically enforced: audit.ts gains a check that every skill with sources.json contains the marker — prose conventions that a reasonable grep cannot find are treated as absent (audit-iteration-1 F1 lesson).

## Phase 1: sync.ts --hosts target + audit.ts scope extension

### Affected Files

- tests/skill-tools.test.mjs — MODIFIED; adds `sync-hosts-writes-three-host-dirs`, `audit-reports-skill-count`, and `audit-fails-on-bad-sources` tests
- tests/fixtures/bad-skill/sources.json — NEW; deliberately malformed JSON (fixture for the sources check)
- skills/skill-sync/scripts/sync.ts — MODIFIED; adds `--hosts <path>` composable target (copy per host dir, drift via existing copyDrift; no nested ternaries)
- skills/skill-sync/SKILL.md — MODIFIED; target table gains the hosts row
- skills/skill-audit/scripts/audit.ts — MODIFIED; three scope extensions (below) + summary line reports validated-skill count
- skills/skill-audit/SKILL.md — MODIFIED; What This Does gains the new checks
- skills/hf-pulse/SKILL.md — MODIFIED; fallback phrasing standardized to include the `engine is unavailable` marker (keeps its MCP-first nuance)
- .gitattributes — NEW; pins governance artifacts (`docs/*.md`, `.qor/**`) and skill sources to `eol=lf` so working-tree bytes stay seal-stable. Applied at gate time under the audit-iteration-1 chain ruling (Judge-directed governance repair, precedes implementation); listed for inventory completeness.
- docs/FEATURE_INDEX.md — MODIFIED; FX07's coverage claim becomes true (repo scripts enter the --help check); FX11 row added

### Changes

`--hosts <targetRepo>`: for each portable skill and each host dir in `[".claude/skills", ".kilo/skills", ".codex/skills"]`, compute the copy action via the existing `copyDrift` and, under `--apply`, `cpSync` recursively. Output lines use the existing `[mode] label skill: action` shape with label `hosts(<path>)`; per-host detail appears as `action` values joined only when they differ (e.g., `create`), else the shared action.

audit.ts scope extensions (all razor-compliant additions):
1. Every `skills/<dir>/sources.json` must `JSON.parse` (FAIL naming the skill on parse error).
2. The `--help` health check also covers repo-level `scripts/*.ts` (build-index, pulse-run) — makes FEATURE_INDEX FX07's enforcement claim factually true.
3. Every skill carrying a `sources.json` must contain the `engine is unavailable` fallback marker in SKILL.md (LD-5 mechanical enforcement).
4. The summary line reports the validated-skill count (`skill-audit: N skill(s), F failure(s), W warning(s)`).

### Unit Tests

- tests/skill-tools.test.mjs::sync-hosts-writes-three-host-dirs — runs `--apply --hosts <tmp>`; asserts `<tmp>/.claude/skills/claude-pulse/SKILL.md`, `<tmp>/.kilo/skills/claude-pulse/SKILL.md`, and `<tmp>/.codex/skills/claude-pulse/SKILL.md` all exist AND no `skill-audit` directory exists under any of the three host dirs. Fails if host-dir derivation, copy, or repo-bound exclusion silently breaks.
- tests/skill-tools.test.mjs::audit-reports-skill-count — runs audit.ts at repo root; asserts exit 0 AND the summary line reports a validated-skill count >= 46. Fails if any planned skill is missing or the count reporting breaks (closes the iteration-1 F4 overstatement).
- tests/skill-tools.test.mjs::audit-fails-on-bad-sources — runs audit.ts with `--skills-dir tests/fixtures`; asserts exit 1 AND output names `bad-skill` for its malformed sources.json. Fails if the JSON validation silently passes broken specs.

## Phase 2: eleven skills (authoring)

### Affected Files

- skills/devlog-draft/SKILL.md — NEW; founder devlog from git history, voice-preserving, registry marketing constraints
- skills/deck-outline/SKILL.md — NEW; narrative-first deck outlines, hands execution to vendored pptx
- skills/finance-review/SKILL.md — NEW; monthly money digest from exports, read-only, vendored xlsx does mechanics
- skills/smallbiz-ops/SKILL.md — NEW; upkeep cadence for the family business sites
- skills/career-radar/SKILL.md — NEW; periodic role/rate market scan
- skills/learning-plan/SKILL.md — NEW; structured skill acquisition with /schedule cadence
- skills/repo-pulse/SKILL.md — NEW; weekly own-repo digest via gh (PRs needing review, stale branches, CI failures)
- skills/repo-doctor/SKILL.md — NEW; one-shot repo health punch list, fixes nothing without approval
- skills/todo-harvester/SKILL.md — NEW; TODO/FIXME sweep with file:line + git-blame age
- skills/skill-forge/SKILL.md — NEW; scaffold a new skill in this repo from docs/skill-template.md, regenerate index
- skills/inference-pulse/SKILL.md — NEW; local-inference runtime pulse (llama.cpp, Ollama, vLLM)
- skills/inference-pulse/sources.json — NEW; engine spec (github repos/orgs + searches)

### Unit Tests

- (covered by the existing behavior test `audit-passes-on-repo`, which re-validates every new SKILL.md against the enforced conventions, and by CI command `node skills/skill-audit/scripts/audit.ts`)

## Phase 3: evidence (B11 weak-model eval + B12 exemplars)

### Affected Files

- docs/evals/2026-07-04-handoff-writer-haiku.md — NEW; weak-model arm results per LD-4
- skills/handoff-writer/references/examples.md — NEW; one gold-standard handoff exemplar
- skills/brief-writer/references/examples.md — NEW; one gold-standard brief exemplar

### Changes

Run the LD-4 eval (6 haiku-tier isolated arms + blind judge), write the report with verdict and registry implications. Author one exemplar per skill, written to satisfy the skill's own Output Format and the template's §Capability floor rule 6.

### Unit Tests

- (evidence artifacts, not code; the eval report itself carries the pre-registered checks and blind scores)

## Phase 4: wiring and close-out

### Affected Files

- docs/proposals/qor-versioned-gate-artifacts.md — NEW; B10 upstream proposal (one seal, one immutable file) for the operator to carry to Qor-logic
- registry/candidates.yaml — MODIFIED; apply the 2026-07-03 eval recommendations (handoff -> rejected/covered_by; to-issues, rules-distiller -> track with eval-blocked rationale)
- docs/BACKLOG.md — MODIFIED; B02–B12 rows moved to Done (B09 as rejected-with-reason per LD-2)
- docs/FEATURE_INDEX.md — MODIFIED; FX11 NEW row for the hosts target; FX10 count updated
- ROADMAP.md — MODIFIED; shipped markers for series 1/2/3/7/8 additions
- README.md — MODIFIED; series table counts updated (46 skills)
- INDEX.md, index.json — REGENERATED

## Definition of Done

### Deliverable: sync --hosts target

- **D1**: One command deploys portable skills to all markdown-host directories of any target repo.
- **D2**: `--hosts <path>` flag in sync.ts; reuses copyDrift/cpSync; razor-compliant (no nested ternaries, functions ≤40 lines, file ≤250).
- **D3**: FEATURE_INDEX FX11 row; SKILL.md target table updated; gate artifacts under `.qor/gates/2026-07-04T0405-927a53/`.
- **D4**: tests/skill-tools.test.mjs::sync-hosts-writes-three-host-dirs.

### Deliverable: eleven skills

- **D1**: Comms, life-ops, repo-hygiene, meta-forge, and inference-pulse series gaps closed; backlog B02–B07 done.
- **D2**: `skills/<name>/SKILL.md` each, conventions per LD-3 (skill-forge repo-bound); inference-pulse adds sources.json consumable by scripts/pulse-run.ts and carries the LD-5 fallback marker.
- **D3**: Indexed in regenerated INDEX.md; BACKLOG rows closed.
- **D4**: tests/skill-tools.test.mjs::audit-reports-skill-count — exit 0 AND validated-skill count >= 46 asserted from audit.ts's summary line.

### Deliverable: weak-model evidence

- **D1**: The capability-equalizer hypothesis has data: same rubric, haiku-tier arms.
- **D2**: docs/evals/2026-07-04-handoff-writer-haiku.md in the 2026-07-03 report's format.
- **D3**: BACKLOG B11 closed; evaluation-framework model-tier rule gains its cited second data point.
- **D4**: Report contains per-check blind scores for all 6 arms and an explicit verdict; exemplar files satisfy their skills' Output Formats.

## Feature Inventory Touches

- entry_id: FX11 — operation: NEW — test_path: tests/skill-tools.test.mjs — test_descriptor: `--apply --hosts <tmp>` creates SKILL.md under .claude/.kilo/.codex skills dirs for a portable skill and excludes repo-bound skills.
- entry_id: FX10 — operation: MODIFIED — test_path: (convention checks via FX02) — test_descriptor: instruction-skill count rises to 41; audit exit 0 proves conventions hold.

## CI Commands

- `node --test "tests/*.test.mjs"` — all behavior tests including the new hosts test
- `node skills/skill-audit/scripts/audit.ts` — repo self-validation must exit 0 over 46 skills
- `node scripts/build-index.ts` — index regeneration must succeed
- `git diff --exit-code INDEX.md index.json` — run after the regenerated index is staged; second regeneration must be a no-op (determinism)
- `node skills/skill-sync/scripts/sync.ts --hosts %TEMP%\skillz-hosts-check` — dry-run must exit 0 and mutate nothing
