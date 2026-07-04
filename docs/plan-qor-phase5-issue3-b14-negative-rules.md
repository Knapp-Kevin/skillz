# Plan: Issue #3 (B14) — Weak-model safety rules for high-judgment skills

**change_class**: feature

**doc_tier**: minimal

**session**: 2026-07-04T0632-7cc26a

**scope**: GitHub issue #3 / BACKLOG B14. Skill-body and template-doctrine changes only; no scripts.

## Open Questions

None. The haiku eval (docs/evals/2026-07-04-handoff-writer-haiku.md) supplies the failure evidence; issue #3 supplies the rule inventory.

## Ground Truth

| Fact | Value | Evidence |
|------|-------|----------|
| Eval failures | (1) leaked token reproduced verbatim ×3 via "define every term"; (2) fabricated "hard requirement per Dana" via mandatory *because* slot | eval doc Tasks table rows 2–3 |
| Template capability floor | rules 1–7 exist; no negative-rules rule | docs/skill-template.md §Capability floor lines 75–81 |
| min-model-capability precedent | template rule 7 names the field; zero skills declare it | `grep min-model-capability skills/*/SKILL.md` → no hits |
| High-judgment targets | handoff-writer + brief-writer, decision-log, agent-postmortem, source-vetting, fact-check, deep-dive, compare — all have mandatory evidence/decision slots | section scan: each has Output Format with rationale/verdict/cause slots |
| handoff-writer examples | references/examples.md exists | `ls skills/handoff-writer/references/` |

## Phase 1: template doctrine

### Affected Files

- `docs/skill-template.md` — §Capability floor rule 8 + checklist row

### Changes

- Add rule 8 **"Ship negative rules with the scaffold"**: weak models follow explicit positive structure but infer implicit negative constraints poorly; mandatory slots pressure fabrication and define-every-term reproduces secrets (cite the haiku eval). Required prohibitions for high-judgment skills: never reproduce secret-shaped strings (refer by type + short prefix; recommend rotation on exposure); `not established` for slots with no evidence-backed value; required sections may be explicitly empty — missing evidence is a finding, not a blank to decorate; mark inference as inference.
- Add merge-checklist row: high-judgment skills (mandatory evidence/decision slots) carry negative rules (secrets, anti-fabrication, missing-evidence fallback).

## Phase 2: handoff-writer (eval subject)

### Affected Files

- `skills/handoff-writer/SKILL.md` — new §Negative rules + frontmatter `metadata.min-model-capability: sonnet`
- `skills/handoff-writer/references/examples.md` — demonstrate credential-by-prefix and `not established`

### Changes

- §Negative rules (before Notes): the four prohibitions, each mapped to the eval failure it closes; "define every term" explicitly scoped to never apply to credential values; secret exposure in inventoried work → flag + recommend rotation.
- `min-model-capability: sonnet` — eval-backed (frontier-verified only until weak-tier re-eval passes; field is data for hosts/routers per template rule 7, not self-assessment).
- Exemplar additions: a Decisions line using `not established`, a Pointers/State line referencing a credential by type + prefix only.

## Phase 3: remaining high-judgment skills

### Affected Files

- `skills/brief-writer/SKILL.md`, `skills/decision-log/SKILL.md`, `skills/agent-postmortem/SKILL.md`, `skills/source-vetting/SKILL.md`, `skills/fact-check/SKILL.md`, `skills/deep-dive/SKILL.md`, `skills/compare/SKILL.md` — compact §Negative rules each

### Changes

Per-skill 3–5 bullets tailored to that skill's mandatory slots (no generic boilerplate): brief-writer (no invented costs/figures; secrets never in briefs), decision-log (never backfill unstated rationale), agent-postmortem (undetermined root cause stays undetermined with candidates; transcript secrets by type+prefix; rotation on exposure), source-vetting (missing signal lowers confidence, never simulated), fact-check (unverifiable ≠ false; no fabricated sources/dates), deep-dive (no source → open question, not finding), compare (empty matrix cell = `no data`, excluded from weighting, never silently estimated).

## Phase 4: governance close-out

### Affected Files

- `docs/BACKLOG.md` — B14 → Done (D16)
- `docs/SYSTEM_STATE.md` — Next Actions row current

### Changes

- B14 moved to Done with closing reference; note the weak-tier re-eval is deliberately deferred: issue #5's semantic risk audit will mechanically enforce negative-rule presence (a substring test here would be presence-only per doctrine-test-functionality — the enforcing *unit* belongs to #5).

## Definition of Done

### Deliverable: negative rules shipped

- **D1**: Every high-judgment skill instructs weak models what NOT to do with secrets, empty slots, and inference; template doctrine makes the pattern mandatory for future skills.
- **D2**: 8 SKILL.md files gain §Negative rules; handoff-writer gains `min-model-capability: sonnet`; template gains rule 8 + checklist row.
- **D3**: BACKLOG B14 closed; ledger audit/seal entries; SYSTEM_STATE current.
- **D4.d**: waiver — behavioral proof is a weak-tier re-eval (a live model run, not a repo test); mechanical presence-enforcement is issue #5's risk audit. **Follow-up phase**: plan-qor-phase7-issue5-risk-audit (enforcement) + future skill-eval re-run (behavior).

## Feature Inventory Touches

None — instruction-skill prose + doctrine only; no scripts or user-facing tooling changed (FX10 row already covers instruction skills as a class).

## CI Commands

- `node --test "tests/*.test.mjs"` — 11/11 behavior tests
- `node skills/skill-audit/scripts/audit.ts` — exit 0, 48 skills (frontmatter still parses with new metadata field)
- `node scripts/build-index.ts && git diff --exit-code INDEX.md index.json` — index idempotent (descriptions unchanged)
