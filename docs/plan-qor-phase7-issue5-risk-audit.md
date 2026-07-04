# Plan: Issue #5 — Semantic skill-risk audit beyond structural validation

**change_class**: feature

**doc_tier**: standard

**terms_introduced**:
- term: risk-audit
  home: skills/skill-audit/SKILL.md

**boundaries**:
- limitations: [deterministic pattern checks — no semantic proof; regex heuristics with documented false-positive posture]
- non_goals: [replacing skill-eval outcome evaluation, blocking vendored official skills, full NLP understanding of skill prose]
- exclusions: [vendor/ trees, repo-bound meta-skills for the portability check]

**session**: 2026-07-04T0632-7cc26a

## Open Questions

None. Implementation form decided: separate `skills/skill-audit/scripts/risk-audit.ts` (audit.ts is at 164 lines; folding five new check families in would crowd the 250-line razor; a sibling script under the same repo-bound skill is the simplest maintainable option offered by the issue).

## Ground Truth

| Fact | Value | Evidence |
|------|-------|----------|
| audit.ts idioms | findings[] {FAIL/WARN}, parseArgs, --skills-dir override, exit 1 on FAIL | read of audit.ts (164 lines) |
| Test harness | run() spawns process.execPath; fixtures under tests/fixtures/ | tests/skill-tools.test.mjs lines 8–30 |
| Fixture isolation constraint | audit tests scan `tests/fixtures/` whole; risk fixtures must live elsewhere | audit-fails-on-bad-skill runs `--skills-dir tests/fixtures` |
| Secret-rule coverage today | handoff-writer, brief-writer, decision-log, agent-postmortem carry secret bullets; source-vetting, fact-check, deep-dive, compare do NOT | grep of §Negative rules bodies |
| B14 status | closed (D16) → issue #5's "FAIL for high-judgment missing negative rules after B14" clause is active | docs/BACKLOG.md |

## Phase 1: uniform secret rule (issue #3 completion enabling a uniform FAIL)

### Affected Files

- `skills/source-vetting/SKILL.md`, `skills/fact-check/SKILL.md`, `skills/deep-dive/SKILL.md`, `skills/compare/SKILL.md` — one secret-handling bullet each in §Negative rules (issue #3 listed all four under its rule additions; cycle 3 shipped their fabrication/evidence rules but not the secret bullet); version +0.0.1

### Changes

Shared bullet, per-skill voiced: never reproduce secret-shaped strings encountered in sources or scanned material (tokens, keys, credentials) — type + short prefix only; flag probable exposure.

## Phase 2: risk-audit.ts + fixtures + tests

### Affected Files

- `tests/skill-tools.test.mjs` — four new tests (listed first per TDD)
- `tests/fixtures-risk/failing/mutating-no-approval/SKILL.md` — NEW fixture: send/publish verbs, no approval language
- `tests/fixtures-risk/failing/judgment-no-negative-rules/SKILL.md` — NEW fixture: `because <reason>` slot, no §Negative rules
- `tests/fixtures-risk/warn-only/portable-specific/SKILL.md` — NEW fixture: `C:\Users\` path + org term in body
- `skills/skill-audit/scripts/risk-audit.ts` — NEW (≤ 250 lines, functions ≤ 40)

### Changes

Deterministic checks over `skills/*/SKILL.md` bodies (frontmatter excluded from term scans; `--skills-dir` override for fixtures):

1. **High-judgment negative rules (FAIL)** — high-judgment = fenced Output Format contains an evidence/decision slot (`because`, `[reason]`, `rationale`, `root cause`, `verdict`, `confidence`). Such a skill must carry `## Negative rules` covering all three classes: secrets (`secret|token|credential|key`), anti-fabrication (`not established|never invent|fabricat`), evidence-gap (`not established|none recorded|unknown|undetermined|no data|unverifiable|empty`). Missing section or missing class → FAIL naming the class.
2. **Schema pressure (WARN)** — non-high-judgment skill whose Output Format has rationale-shaped slots but whose body lacks any evidence-gap vocabulary.
3. **Mutating-action ambiguity (FAIL/WARN)** — FAIL verbs: `send|push|delete|publish|deploy|create issue|archive|enroll|pay|buy` present with NO approval/read-only language anywhere (`approval|approve|confirm|draft-only|read-only|dry-run|propose|never (sends|posts|publishes|edits|applies|mutates|contacts)|operator to (apply|publish)`). `move|update` are WARN-class only (noise posture documented in script header).
4. **Portable specificity (WARN)** — skipped for bodies containing `repo-bound`; absolute paths (`X:\`, `/home/`, `/Users/`) and an embedded operator/org term list (repo-bound tool ⇒ local list intentional; documented). Absorbed from issue #4 per posted transfer comment.
5. **External-service ambiguity (WARN)** — direct vendor API host (`api.<vendor>.<tld>`) or env-key requirement without an MCP/web-tool-fallback mention.

Exit contract identical to audit.ts: any FAIL → exit 1; WARN-only → exit 0. `--help` exits 0 (audit.ts's script-health check will pick it up automatically).

### Unit Tests

- `risk-audit-fails-on-mutating-without-approval` — invokes risk-audit on `fixtures-risk/failing`, asserts exit 1 + finding names the verb and the missing-approval ground
- `risk-audit-fails-on-missing-negative-rules` — same dir, asserts finding names the missing rule class
- `risk-audit-warns-on-portable-specificity` — invokes on `fixtures-risk/warn-only`, asserts exit 0 AND warn text names the path/term (behavioral: proves WARN ≠ FAIL)
- `risk-audit-passes-on-repo` — invokes on `skills/`, asserts exit 0 (proves current first-party set is risk-clean)

## Phase 3: wiring + governance

### Affected Files

- `.github/workflows/ci.yml` — risk-audit step after skill-audit
- `docs/FEATURE_INDEX.md` — FX13 row
- `skills/skill-audit/SKILL.md` — document the second script + version bump
- `docs/skill-template.md` — rule 8 gains "(mechanically enforced by risk-audit)" pointer
- `docs/SYSTEM_STATE.md` — test count, queue row
- `INDEX.md`, `index.json` — regenerated (version bumps)

## Definition of Done

### Deliverable: static risk filter

- **D1**: A structurally valid skill that induces dangerous behavior patterns (secret reproduction pressure, schema-slot fabrication pressure, unapproved mutation, operator lock-in, vendor lock-in) is caught pre-merge.
- **D2**: `risk-audit.ts` per Phase 2 signature; razor-compliant; zero-install Node 22.18+.
- **D3**: FX13 row maps feature → implementation → proof; CI runs it; ledger entries; SYSTEM_STATE current.
- **D4**: the four named tests, green in `node --test "tests/*.test.mjs"` — each invokes the unit and asserts on its output/exit code (no presence-only assertions).

## Feature Inventory Touches

- entry_id: FX13 · operation: NEW · test_path: tests/skill-tools.test.mjs · test_descriptor: "risk-audit exits 1 naming the finding for a mutating-verb skill without approval language and for a high-judgment skill missing negative rules; exits 0 with named WARN for portable-specificity; exits 0 over skills/"

## CI Commands

- `node --test "tests/*.test.mjs"` — 15 tests green
- `node skills/skill-audit/scripts/audit.ts` — exit 0
- `node skills/skill-audit/scripts/risk-audit.ts` — exit 0 over skills/
- `node scripts/build-index.ts` then commit regenerated index (version bumps)
