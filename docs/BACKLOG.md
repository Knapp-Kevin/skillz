# Backlog

Current work is ordered by the initial-alpha finish line. Broad skill acquisition and refinement are intentionally post-alpha unless they expose a blocker in the first-visit or returning-user experience.

## Active: required before initial alpha lock

| ID | Item | State | Completion evidence |
|---|---|---|---|
| A01 | Materialize all 12 pinned vendor submodules and run `node scripts/initial-alpha-preflight.ts` | BLOCKED BY CURRENT EXECUTION ENVIRONMENT | Clean exact source-state proof passes; schema-v2 semantic invariants pass; exact counts recorded; second catalog pass byte-identical; preflight ends `READY FOR JOURNEY EVALUATION` |
| A02 | Verify the separately held private v2 evaluator bundle against the exact committed public treatment fixture | READY AFTER ISOLATION REPAIR MERGES | `verify-alpha-evaluator-bundle.mjs` passes set ID, public SHA-256, complete neutral scenario coverage, and frozen criteria structure |
| A03 | Execute all three rotated v2 first-visit treatment scenarios in fresh contexts | READY AFTER A01-A02 | Collectively proves eligible reuse/minimal adaptation, unsafe/unproven unchanged-reuse refusal, and custom creation; each treatment output frozen before private rubric entry is opened |
| A04 | Execute both rotated v2 returning-user treatment scenarios in fresh contexts | READY AFTER A01-A02 | Collectively proves minimal justified refinement and a correct no-change outcome while preserving valid existing behavior |
| A05 | Privately score the five frozen treatment outputs and write public evidence records | READY AFTER A03-A04 | All five satisfy frozen private criteria with no hard fail; public result files record set ID, scenario ID, public fixture hash, scores/outcome, evidence, and truthful install/handoff state without republishing the active answer key |
| A06 | Reconcile generated counts, README, alpha checklist, system state, and Issue #15 | READY AFTER A01-A05 | Generated index/README agree; five blind evidence records linked; current docs agree |
| A07 | Declare initial implementation alpha locked | BLOCKED UNTIL A01-A06 | Every remaining alpha gate supported by actual materialized and blind behavioral evidence |

## Invalid / retired alpha work

| Item | State | Reason |
|---|---|---|
| Original public A1/A2/A3/R1/R2 behavioral set | RETIRED / INVALID AS BLIND EVIDENCE | Expected decisions, candidate hints, and scoring criteria were committed publicly and remain recoverable from Git history. The renderer hid them from stdout but not from a repository-reading treatment agent. |

Do not execute the retired set for alpha closure. The current v2 public treatment fixture uses neutral scenario IDs, while evaluator-only mappings live in a private fingerprint-bound bundle outside the repository.

## Post-alpha enrichment

These are useful but **not blockers** for the initial implementation.

| ID | Item | Area | Notes |
|---|---|---|---|
| P01 | Continue source discovery and corpus expansion | curation | Add sources only with correct source role, pin/freshness, license, and attribution |
| P02 | Characterize more existing corpus skills | curation | Fingerprint + controlled tags + provenance before treating as fully characterized |
| P03 | Structured verification of additional third-party skills | quality | Unverified remains design evidence until it earns stronger status |
| P04 | Behavioral validation of high-value skills | evaluation | Use representative before/after evidence where practical |
| P05 | Improve category navigation and direct-library browsing | human UX | Let categories evolve from real corpus growth without destabilizing skill IDs |
| P06 | Refine selection taxonomy and weights from real usage | selection | Tags inform shortlisting; final user-fit judgment remains required |
| P07 | Expand returning-user drift/overlap heuristics | refinement | Prefer smallest justified change; preserve `NO CHANGE NEEDED` outcome |
| P08 | Add additional supported host installation adapters | portability | Only when host packaging/install behavior is established |
| P09 | Revisit minimum-model/capability metadata where evidence supports it | quality | Historical B13; do not block alpha |
| P10 | Consider additional host format conversion in skill-sync | portability | Historical B15; do not block alpha |
| P11 | Revisit historical sandbox candidates when they are relevant | curation | Historical B17 and similar items; source reputation is not proof |

## Completed foundational work

| ID | Item | Evidence |
|---|---|---|
| D01 | Separate user-facing library from repository engine machinery | `skills/`, `engine/skills/`, README/AGENTS boundary |
| D02 | Human-first README with explicit AI-agent jump | `README.md` |
| D03 | First-visit bootstrap route | `BOOTSTRAP.md`, `AGENTS.md`, `engine/skills/skill-bootstrap/` |
| D04 | Returning-user refinement route | README/BOOTSTRAP/AGENTS contracts |
| D05 | Human browse-by-purpose categories | `skills/categories/`, `registry/categories.yaml` |
| D06 | Third-party provenance/attribution companion model | `registry/skills/`, `docs/third-party-provenance.md`, `THIRD_PARTY_NOTICES.md` |
| D07 | Exact-version verification/fingerprint model | `registry/verification/`, `docs/skill-verification.md` |
| D08 | Controlled characterization taxonomy | `registry/taxonomy.yaml` |
| D09 | Source role + source pin/license registry | `registry/sources.yaml` |
| D10 | Governed candidate selector | `engine/skills/skill-bootstrap/scripts/select-candidates.ts`, selection tests |
| D11 | Recursive skill discovery across catalog/audit/risk/sync | `scripts/lib/skill-discovery.ts` and consumers |
| D12 | Schema-v2 generated-catalog implementation | `scripts/build-index.ts` |
| D13 | Semantic catalog invariants + two-pass idempotency verifier | `scripts/lib/catalog-invariants.mjs`, `scripts/verify-index-idempotency.ts` |
| D14 | Exact vendored-source materialization proof in one-command alpha preflight | `scripts/verify-vendor-materialization.ts`, `scripts/initial-alpha-preflight.ts` |
| D15 | Rotated public-only v2 treatment fixture | `docs/evals/fixtures/initial-alpha-scenarios.json` |
| D16 | Public treatment renderer with neutral v2 IDs | `scripts/render-alpha-scenario.ts` + tests |
| D17 | Private evaluator-bundle fingerprint verifier | `scripts/verify-alpha-evaluator-bundle.mjs` + tests |
| D18 | Actions budget protection | `.github/workflows/ci.yml` manual-dispatch only |

## Historical records

The July 2026 build series and its B/D identifiers remain available in git history, historical plan documents, evaluation reports, and governance ledger artifacts. They are not the current implementation queue.

For the authoritative finish line, use `docs/alpha-lock.md`, `docs/initial-implementation.md`, `docs/evals/run-initial-alpha.md`, and GitHub Issue #15.
