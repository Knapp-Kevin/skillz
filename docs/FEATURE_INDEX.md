# Feature Index

Maps user-touchable and governance-critical features to their implementation and current proof state.

**Proof labels**

- **STATIC PASS**: repository contract/mechanical tests exist and the implementation is present.
- **RUNTIME PENDING**: requires a fully materialized checkout or other execution environment not available in the current session.
- **BEHAVIORAL PENDING**: requires an isolated journey/effectiveness run; static assertions are not accepted as behavioral proof.
- **POLICY**: enforced by repository structure/documentation and supporting tests where applicable.

| ID | Feature | Implementation | Proof state |
|---|---|---|---|
| FX01 | Human-first repository front door | `README.md` | **STATIC PASS**: initial implementation contract tests |
| FX02 | Explicit AI-agent jump and operating route | `README.md`, `AGENTS.md` | **STATIC PASS**: contract tests assert agent entry surfaces |
| FX03 | First-visit bootstrap workflow | `BOOTSTRAP.md`, `engine/skills/skill-bootstrap/SKILL.md` | **STATIC PASS / BEHAVIORAL PENDING**: A1-A3 |
| FX04 | Returning-user review/refinement workflow | `README.md`, `BOOTSTRAP.md`, `AGENTS.md` | **STATIC PASS / BEHAVIORAL PENDING**: R1-R2 |
| FX05 | Direct library mode without forced bootstrap | `README.md`, `AGENTS.md` | **STATIC PASS** |
| FX06 | Library/engine inventory boundary | `skills/`, `engine/skills/`, `engine/README.md` | **STATIC PASS**: engine excluded from library discovery/sync |
| FX07 | Human browse-by-purpose categories | `skills/categories/`, `registry/categories.yaml` | **STATIC PASS** |
| FX08 | Recursive local skill discovery | `scripts/lib/skill-discovery.ts` | **STATIC PASS**: shared by index, audit, risk-audit, sync |
| FX09 | Schema-v2 catalog generation | `scripts/build-index.ts` | **IMPLEMENTED / RUNTIME PENDING**: materialized generation + exact counts required |
| FX10 | Two-pass catalog idempotency proof | `scripts/verify-index-idempotency.ts` | **IMPLEMENTED / RUNTIME PENDING** |
| FX11 | Source identity, role, exact pin, and license registry | `registry/sources.yaml` | **STATIC PASS / POLICY** |
| FX12 | Per-skill third-party provenance and attribution | `registry/skills/`, `docs/third-party-provenance.md`, `THIRD_PARTY_NOTICES.md` | **STATIC PASS / POLICY** |
| FX13 | Exact-version verification and characterization state | `registry/verification/`, `scripts/lib/verification-registry.ts` | **STATIC PASS** |
| FX14 | Controlled characterization taxonomy | `registry/taxonomy.yaml` | **STATIC PASS** |
| FX15 | Fingerprint drift invalidation | `engine/skills/source-vetting/scripts/verify-characterization-integrity.ts` | **STATIC PASS / RUNTIME RECHECK IN PREFLIGHT** |
| FX16 | Governed candidate shortlisting | `engine/skills/skill-bootstrap/scripts/select-candidates.ts` | **STATIC PASS**: selection fixtures prove eligible reuse, unverified evidence-only mode, blocked stale state, tag-aware ranking |
| FX17 | Structural skill audit | `engine/skills/skill-audit/scripts/audit.ts` | **STATIC PASS / RUNTIME RECHECK IN PREFLIGHT** |
| FX18 | Semantic risk audit | `engine/skills/skill-audit/scripts/risk-audit.ts` | **STATIC PASS / RUNTIME RECHECK IN PREFLIGHT** |
| FX19 | Portable skill synchronization/install handoff machinery | `engine/skills/skill-sync/`, `docs/installation-handoff.md` | **STATIC PASS; host-specific completion remains contextual** |
| FX20 | Custom skill scaffolding | `engine/skills/skill-forge/` | **STATIC PASS** |
| FX21 | Skill effectiveness evaluation procedure | `engine/skills/skill-eval/`, `docs/evaluation-framework.md` | **POLICY/PROCEDURE**: no result may be claimed without actual runs |
| FX22 | One-command initial-alpha preflight | `scripts/initial-alpha-preflight.ts` | **IMPLEMENTED / RUNTIME PENDING** |
| FX23 | Frozen privacy-safe alpha journey fixtures | `docs/evals/fixtures/initial-alpha-scenarios.json` | **STATIC PASS** |
| FX24 | Leak-safe treatment scenario renderer | `scripts/render-alpha-scenario.ts` | **STATIC PASS**: tests reject answer-key leakage |
| FX25 | First-visit eligible reuse proof | A1 in `docs/evals/` | **BEHAVIORAL PENDING** |
| FX26 | First-visit unverified/stale refusal proof | A2 in `docs/evals/` | **BEHAVIORAL PENDING** |
| FX27 | First-visit custom creation proof | A3 in `docs/evals/` | **BEHAVIORAL PENDING** |
| FX28 | Returning-user minimal refinement proof | R1 in `docs/evals/` | **BEHAVIORAL PENDING** |
| FX29 | Returning-user no-change proof | R2 in `docs/evals/` | **BEHAVIORAL PENDING** |
| FX30 | Automatic GitHub Actions budget protection | `.github/workflows/ci.yml` | **POLICY PASS**: manual-dispatch only |

## Alpha rule

Static presence and contract tests are necessary but do not establish the complete user experience. Initial alpha remains unlocked until FX09/FX10/FX22 runtime proof succeeds and FX25-FX29 have actual isolated behavioral evidence.

See `docs/alpha-lock.md`, `docs/initial-implementation.md`, and `docs/evals/run-initial-alpha.md`.
