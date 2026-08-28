# Backlog

Current work is ordered by the initial-alpha finish line. Broad skill acquisition and refinement are intentionally post-alpha unless they expose a blocker in the first-visit or returning-user experience.

## Active: required before initial alpha lock

| ID | Item | State | Completion evidence |
|---|---|---|---|
| A01 | Materialize all 12 pinned vendor submodules and run `node scripts/initial-alpha-preflight.ts` | BLOCKED BY CURRENT EXECUTION ENVIRONMENT | Preflight ends `READY FOR JOURNEY EVALUATION`; schema-v2 counts recorded; second catalog pass byte-identical |
| A02 | Run first-visit scenario A1: eligible reuse/minimal adaptation | READY AFTER A01 | Actual isolated result under `docs/evals/results/`, no hard fail, fixture pass |
| A03 | Run first-visit scenario A2: refuse unverified/stale trusted unchanged reuse | READY AFTER A01 | Actual isolated result, no quality-state escalation without evidence |
| A04 | Run first-visit scenario A3: custom creation when library fit is materially worse | READY AFTER A01 | Actual isolated result showing comparison before creation and truthful validation/install state |
| A05 | Run returning-user scenario R1: minimal justified refinement | READY AFTER A01 | Existing set inventoried, drift surfaced, valid custom behavior preserved, changed capability re-evaluated |
| A06 | Run returning-user scenario R2: no-change decision | READY AFTER A01 | Actual isolated result concludes `NO CHANGE NEEDED` without inventing a gap |
| A07 | Reconcile generated counts, README, alpha checklist, and Issue #15 | READY AFTER A01-A06 | Generated index/README agree; evidence linked; `docs/alpha-lock.md` updated |
| A08 | Declare initial implementation alpha locked | BLOCKED UNTIL A01-A07 | Every remaining alpha gate supported by actual evidence |

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
| D13 | Catalog two-pass idempotency verifier | `scripts/verify-index-idempotency.ts` |
| D14 | One-command initial-alpha preflight | `scripts/initial-alpha-preflight.ts` |
| D15 | Frozen five-scenario journey proof matrix | `docs/evals/fixtures/initial-alpha-scenarios.json` |
| D16 | Leak-safe journey scenario renderer | `scripts/render-alpha-scenario.ts` + tests |
| D17 | Actions budget protection | `.github/workflows/ci.yml` manual-dispatch only |

## Historical records

The July 2026 build series and its B/D identifiers remain available in git history, historical plan documents, evaluation reports, and governance ledger artifacts. They are not the current implementation queue.

For the authoritative finish line, use `docs/alpha-lock.md`, `docs/initial-implementation.md`, `docs/evals/run-initial-alpha.md`, and GitHub Issue #15.
