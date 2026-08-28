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
| FX03 | First-visit bootstrap workflow | `BOOTSTRAP.md`, `engine/skills/skill-bootstrap/SKILL.md` | **STATIC PASS / BEHAVIORAL PENDING**: three isolated v2 first-visit journeys |
| FX04 | Returning-user review/refinement workflow | `README.md`, `BOOTSTRAP.md`, `AGENTS.md` | **STATIC PASS / BEHAVIORAL PENDING**: two isolated v2 returning journeys |
| FX05 | Direct library mode without forced bootstrap | `README.md`, `AGENTS.md` | **STATIC PASS** |
| FX06 | Library/engine inventory boundary | `skills/`, `engine/skills/`, `engine/README.md` | **STATIC PASS**: engine excluded from library discovery/sync |
| FX07 | Human browse-by-purpose categories | `skills/categories/`, `registry/categories.yaml` | **STATIC PASS** |
| FX08 | Recursive local skill discovery | `scripts/lib/skill-discovery.ts` | **STATIC PASS**: shared by index, audit, risk-audit, sync |
| FX09 | Schema-v2 catalog generation | `scripts/build-index.ts` | **IMPLEMENTED / RUNTIME PENDING**: materialized generation + exact counts required |
| FX10 | Semantic catalog coherence + two-pass idempotency proof | `scripts/verify-index-idempotency.ts`, `scripts/lib/catalog-invariants.mjs` | **STATIC PASS / RUNTIME PENDING ON CURRENT FULL CORPUS**: unit tests cover count/source/shape invariants; materialized second-pass proof still required |
| FX11 | Source identity, role, exact pin, and license registry | `registry/sources.yaml` | **STATIC PASS / POLICY** |
| FX12 | Per-skill third-party provenance and attribution | `registry/skills/`, `docs/third-party-provenance.md`, `THIRD_PARTY_NOTICES.md` | **STATIC PASS / POLICY** |
| FX13 | Exact-version verification and characterization state | `registry/verification/`, `scripts/lib/verification-registry.ts` | **STATIC PASS** |
| FX14 | Controlled characterization taxonomy | `registry/taxonomy.yaml` | **STATIC PASS** |
| FX15 | Fingerprint drift invalidation | `engine/skills/source-vetting/scripts/verify-characterization-integrity.ts` | **STATIC PASS / RUNTIME RECHECK IN PREFLIGHT**: strict preflight mode also fails unavailable characterized targets after source materialization |
| FX16 | Governed candidate shortlisting | `engine/skills/skill-bootstrap/scripts/select-candidates.ts` | **STATIC PASS**: selection fixtures prove eligible reuse, unverified evidence-only mode, blocked stale state, tag-aware ranking |
| FX17 | Structural skill audit | `engine/skills/skill-audit/scripts/audit.ts` | **STATIC PASS / RUNTIME RECHECK IN PREFLIGHT** |
| FX18 | Semantic risk audit | `engine/skills/skill-audit/scripts/risk-audit.ts` | **STATIC PASS / RUNTIME RECHECK IN PREFLIGHT** |
| FX19 | Portable skill synchronization/install handoff machinery | `engine/skills/skill-sync/`, `docs/installation-handoff.md` | **STATIC PASS; host-specific completion remains contextual** |
| FX20 | Custom skill scaffolding | `engine/skills/skill-forge/` | **STATIC PASS** |
| FX21 | Skill effectiveness evaluation procedure | `engine/skills/skill-eval/`, `docs/evaluation-framework.md` | **POLICY/PROCEDURE**: no result may be claimed without actual runs |
| FX22 | One-command initial-alpha preflight | `scripts/initial-alpha-preflight.ts` | **IMPLEMENTED / RUNTIME PENDING** |
| FX23 | Rotated public-only v2 alpha treatment fixtures | `docs/evals/fixtures/initial-alpha-scenarios.json` | **STATIC PASS**: neutral IDs; public tests forbid expected decisions, candidate hints, scoring criteria, or answer-key fields; retired v1 set is invalid as evidence |
| FX24 | Public treatment renderer + private evaluator-bundle binding | `scripts/render-alpha-scenario.ts`, `scripts/verify-alpha-evaluator-bundle.mjs` | **STATIC PASS**: renderer exposes only public context; private verifier binds evaluator rubric to exact public set ID, SHA-256, scenario coverage, and an evaluator-only filesystem location outside the repository |
| FX25 | Blind first-visit eligible reuse/minimal-adaptation proof | rotated v2 private evaluator mapping | **BEHAVIORAL PENDING** |
| FX26 | Blind first-visit unsafe/unproven unchanged-reuse refusal proof | rotated v2 private evaluator mapping | **BEHAVIORAL PENDING** |
| FX27 | Blind first-visit custom-creation proof | rotated v2 private evaluator mapping | **BEHAVIORAL PENDING** |
| FX28 | Blind returning-user minimal-refinement proof | rotated v2 private evaluator mapping | **BEHAVIORAL PENDING** |
| FX29 | Blind returning-user no-change proof | rotated v2 private evaluator mapping | **BEHAVIORAL PENDING** |
| FX30 | Automatic GitHub Actions budget protection | `.github/workflows/ci.yml` | **POLICY PASS**: manual-dispatch only |
| FX31 | Exact alpha source-state proof | `scripts/verify-vendor-materialization.ts` | **STATIC PASS / RUNTIME PENDING ON CURRENT FULL CORPUS**: local Git fixtures cover clean exact pin, dirty superproject, missing submodule, wrong submodule HEAD, and dirty source content; preflight executes this before catalog generation |
| FX32 | Behavioral answer-key isolation | public v2 fixture + private fingerprint-bound evaluator bundle | **STATIC PASS / BEHAVIORAL PENDING**: public Git contains no v2 outcome mapping; evaluator verifier rejects rubrics stored or resolved inside the treatment repository; host-level treatment access must still be kept separate during actual runs |

## Alpha rule

Static presence and contract tests are necessary but do not establish the complete user experience. Initial alpha remains unlocked until FX31 source-state proof and FX09/FX10/FX22 runtime proof succeed on the current fully materialized commit, the private v2 evaluator bundle verifies against the exact public fixture **from outside the treatment repository**, and FX25-FX29 have actual blind behavioral evidence.

The retired public v1 A1/A2/A3/R1/R2 mappings cannot satisfy FX25-FX29 because their answer keys remain recoverable from public Git history.

See `docs/alpha-lock.md`, `docs/initial-implementation.md`, and `docs/evals/run-initial-alpha.md`.
