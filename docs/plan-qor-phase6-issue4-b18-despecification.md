# Plan: Issue #4 (B18) — De-specify portable skills; require Bind steps

**change_class**: feature

**doc_tier**: minimal

**session**: 2026-07-04T0632-7cc26a

**scope**: GitHub issue #4 / BACKLOG B18. Portable skill bodies only. The audit-heuristic acceptance box is transferred to issue #5 (comment posted on #4, 2026-07-04). Non-goals honored: README first-party positioning untouched; repo-bound meta-skills untouched; specifics replaced with binding logic, never with vagueness.

## Open Questions

None. The sweep inventory below is grep-derived; task-surface Mode 2 step 5 is the binding-authority reference pattern ("the document wins" over memory).

## Ground Truth (sweep of portable skill bodies, 2026-07-04)

| Cluster | Files | Specifics found |
|---------|-------|-----------------|
| Business/profile | smallbiz-ops, career-radar | 3 family-business names hardcoded in description+body+output table; default career profile hardcoded |
| Workspace paths | repo-pulse, standup-writer, week-in-review, daily-briefing, devlog-draft | `G:\MythologIQ` literal paths; "MythologIQ repos/git activity" |
| Product relevance | inference-pulse (7 refs), llama/qwen/glm/deepseek-pulse (1 line each), memory-pulse (3), mcp-pulse (1), paper-digest (2), governance-pulse (2) | GG-CORE, COREFORGE Vault/Synapse, "MythologIQ stack/workspace" |

Evidence: `grep -rniE "MythologIQ|GG-CORE|COREFORGE|G:\\\\" skills/*/SKILL.md` excluding repo-bound (skill-audit/sync/forge) → 30 hits across exactly these 16 files. `frostwulf.zo.computer` in `metadata.author` is provenance attribution, not behavior — retained.

## Required pattern (uniform across all 16)

A **Bind** line/step early in Execution Flow: (1) discover the governing source — operator profile, governance doc, or host memory; (2) the bound source is authoritative — it wins over memory and assumptions; (3) if none exists, ask the operator, then offer to persist the answers as a governance doc for future runs; (4) concrete examples stay as clearly-labeled examples ("e.g.").

## Phase 1: deep rewrites

### Affected Files

- `skills/smallbiz-ops/SKILL.md` — description + body + output generalized to a bound business portfolio (names, sites, localities, seasonal cadence from the bound doc; elicit + offer-to-create when absent); output table rows become `[Business]` placeholders; seasonal examples generic
- `skills/career-radar/SKILL.md` — hardcoded default profile removed; profile bound from career notes/operator profile, elicited when absent and offered for persistence; query examples labeled as examples for an example profile

## Phase 2: workspace-root binds

### Affected Files

- `skills/repo-pulse/SKILL.md`, `skills/standup-writer/SKILL.md`, `skills/week-in-review/SKILL.md` — `G:\MythologIQ` → bound workspace root(s)
- `skills/daily-briefing/SKILL.md`, `skills/devlog-draft/SKILL.md` — "MythologIQ" → the bound workspace/repos

## Phase 3: product-relevance binds

### Affected Files

- `skills/inference-pulse/SKILL.md` — GG-CORE removed entirely → bound local-runtime target (verdict section renamed generically; the bound doc supplies the runtime's name at report time, keeping the sweep grep at zero hits)
- `skills/llama-pulse/SKILL.md`, `skills/qwen-pulse/SKILL.md`, `skills/glm-pulse/SKILL.md`, `skills/deepseek-pulse/SKILL.md` — one notes line each → bound runtime target phrasing
- `skills/memory-pulse/SKILL.md` — COREFORGE Vault → bound memory-layer project
- `skills/mcp-pulse/SKILL.md` — COREFORGE Synapse → bound platform's MCP integration
- `skills/paper-digest/SKILL.md` — MythologIQ stack → bound stack/interest profile
- `skills/governance-pulse/SKILL.md` — "MythologIQ workspace" → any workspace with `.qor/` governance state (capability-based, not org-based)

## Phase 4: governance close-out

### Affected Files

- `docs/BACKLOG.md` — B18 → Done (D17), audit-heuristic remainder noted as moved to #5
- `docs/SYSTEM_STATE.md` — queue row updated
- `INDEX.md`, `index.json` — regenerated (descriptions + versions change)

All 16 skills bump `metadata.version` 1.x.0 → +0.1.0.

## Definition of Done

### Deliverable: portable skills are adaptive frameworks

- **D1**: No portable skill body carries operator/org/business/product specifics; every convention-dependent skill binds at runtime and declares the bound source authoritative.
- **D2**: 16 SKILL.md files edited per phases 1–3; re-running the sweep grep over portable skill bodies returns zero behavioral hits (metadata.author excluded; "e.g." examples excluded by review).
- **D3**: B18 → Done D17; ledger audit/seal entries; SYSTEM_STATE current; index regenerated.
- **D4.d**: waiver — the enforcing unit (portable-specificity WARN heuristic) is issue #5 scope by explicit transfer. **Follow-up phase**: plan-qor-phase7-issue5-risk-audit.

## Feature Inventory Touches

None — instruction-skill prose only (FX10 class row covers these).

## CI Commands

- `node --test "tests/*.test.mjs"` — 11/11
- `node skills/skill-audit/scripts/audit.ts` — exit 0, 48 skills
- `node scripts/build-index.ts` then commit regenerated INDEX.md + index.json — descriptions/versions changed by design
- `grep -rniE "MythologIQ|GG-CORE|COREFORGE|G:\\\\" skills/*/SKILL.md | grep -v "skill-audit\|skill-sync\|skill-forge"` — zero behavioral hits post-sweep
