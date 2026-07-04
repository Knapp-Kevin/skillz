# Plan: Issue #1 — Align repo state metadata and generated counts

**change_class**: feature

**doc_tier**: minimal

**session**: 2026-07-04T0632-7cc26a

**scope**: GitHub issue #1 (Knapp-Kevin/skillz). Docs-only reconciliation; no code or skill-body changes.

## Open Questions

None. All counts below are grep/run-verified ground truth (evidence inline).

## Ground Truth (verified 2026-07-04, session 7cc26a)

| Fact | Value | Evidence |
|------|-------|----------|
| First-party skills | 48 | `ls skills/ \| wc -l` → 48; `audit.ts` → "48 skill(s), 0 failure(s)" |
| Repo-bound | 3 (skill-audit, skill-forge, skill-sync) | `grep -l "repo-bound" skills/*/SKILL.md` → 3 files |
| Portable | 45 (= 48 − 3) | derived |
| Scripted skills | 4 (claude-pulse, skill-audit, skills-pulse, skill-sync) | `ls -d skills/*/scripts` → 4 dirs |
| Vendored sources | 6 submodules | `git submodule status` → 6 rows |
| Indexed vendor skills | 524 | index.json walk: kwp 185 + anthropic 17 + vercel 9 + microsoft 186 + azure 34 + aws 93 |
| Behavior tests | 11, all passing | `node --test "tests/*.test.mjs"` → `# tests 11 / # pass 11 / # fail 0` |
| Index freshness | clean | `node scripts/build-index.ts` then `git diff` → empty |
| Latest ledger entry | #8, chain head 6744f93e | docs/META_LEDGER.md Validation History 2026-07-04 |

Stale surfaces found: `docs/SYSTEM_STATE.md` (35 skills / 33+2 split / 8 tests / seal f1150ab7 / 3 completed Next Actions), `docs/FEATURE_INDEX.md` FX10 ("42 instruction skills"; actual = 44 = 48 − 4 scripted), `ROADMAP.md` §Suggested build order (all seven "Next" items shipped per its own ✅ lines and BACKLOG D03–D08; evidence: ROADMAP.md line 78 "Shipped so far: the pulse fleet (16), skill-audit, skill-sync, skills-pulse" undercounts by 29). `README.md`, `INDEX.md`, `index.json`, `docs/BACKLOG.md` verified current — no edits needed there.

## Phase 1: SYSTEM_STATE.md refresh

### Affected Files

- `docs/SYSTEM_STATE.md` — full snapshot refresh to ground-truth table above

### Changes

- Snapshot Metadata: Last Updated → 2026-07-04, Iteration → 2, Session Seal → Entry #8 chain head 6744f93e.
- File Tree: 35 → 48 first-party skills; add missing series lines (comms/life-ops full list, hygiene/meta additions incl. agent-home-doctor, task-surface, skill-forge); gates dir line covers both sessions.
- Metrics: Local skills 48 (45 portable, 3 repo-bound); Scripted 4 (unchanged list); Behavior tests 11; Vendored 6 sources / 524 indexed skills (drop "+60 partner plugins" — plugins are containers, their 185 skills are already inside the 524; labeling both was double-describing).
- Health Indicators: Test Status 11/11; dates refreshed.
- Next Actions: remove the three completed items (skill-eval first run = BACKLOG D04; comms/life-ops shipped = D05/D06); replace with current opens: issues #2–#6 queue, B13/B15/B17 remainders.

## Phase 2: FEATURE_INDEX.md count fix

### Affected Files

- `docs/FEATURE_INDEX.md` — FX10 row only

### Changes

- FX10: "42 instruction skills" → "44 instruction skills (48 first-party − 4 scripted)" so the arithmetic is self-explaining; proof column unchanged (the `>= 46` floor assertion remains valid and intentionally approximate — it is a floor, not an exact count, so index churn doesn't break tests; label stands as-is in test comment).

## Phase 3: ROADMAP.md build-order refresh

### Affected Files

- `ROADMAP.md` — §Suggested build order only

### Changes

- Replace the stale "Shipped so far … Next: 1–7" block with a current statement: all seven build-order items shipped (close-out reference: BACKLOG D03–D08, sessions ca9b2c + 927a53); current open work now tracked in docs/BACKLOG.md §Open and GitHub issues #2–#6. Retitle section "Build order (complete — 2026-07-04)" so future readers see it as a historical record, not a queue.
- No other ROADMAP sections touched (series Shipped ✅ lines, design rules, portability contract are current).

## Definition of Done

### Deliverable: reconciled state surfaces

- **D1**: Every repo-state surface (README, ROADMAP, INDEX.md, index.json, SYSTEM_STATE, FEATURE_INDEX, BACKLOG) reports the same current repo state.
- **D2**: Edits confined to `docs/SYSTEM_STATE.md`, `docs/FEATURE_INDEX.md`, and `ROADMAP.md` §Suggested build order; all other surfaces verified-current with evidence above.
- **D3**: META_LEDGER gains audit + substantiate entries for this cycle; issue #1 acceptance boxes all satisfiable.
- **D4.d**: waiver — docs-only change; no unit invokes these prose surfaces. Enforcement of ongoing agreement arrives as CI in cycle 2 (issue #2), which is this waiver's **Follow-up phase**: plan-qor-phase4-issue2-ci.

## Feature Inventory Touches

None — plan touches only docs/governance (block declared empty per plan schema).

## CI Commands

- `node --test "tests/*.test.mjs"` — 11/11 behavior tests
- `node skills/skill-audit/scripts/audit.ts` — exit 0, 48 skills
- `node scripts/build-index.ts && git diff --exit-code INDEX.md index.json` — index idempotent
