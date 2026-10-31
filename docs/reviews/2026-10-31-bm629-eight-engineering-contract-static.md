# Bhushan Modi: eight engineering implementation and contract packages (2026-10-31)

## Exact source and macro frontier

- Source: `bm629/agent-skills`, registered tracked-corpus, MIT, pin `f6a700ea94a16cf8e0b5e563d4d48d85503e41f6`.
- Independently enumerated pinned tree: **68 first-class `skills/<name>/SKILL.md` packages**, no nested first-class skills or duplicate package exposure paths in this source. Reference Markdown under each package is not a separate skill.
- Before: **34/68** exact-version verification/provenance pairs; **34 genuine gaps**. After: **42/68**; **26 genuine gaps**. New exact-version companions: **8 provenance + 8 verification**. Admitted-source denominator delta **0**; source is still tracked/selective, not wholesale admitted.
- Prior 34 companion identities were checked against the source package list. This tranche consists only of eight previously uncovered canonical package paths. Pinned source files and upstream revision were not modified.
- All eight package trees and SKILL.md Git blobs are individually recorded in companion YAML. Source-specific latest changes are June 8-11, 2026; current review October 31. License MIT is from registered source; preserve upstream license and reference material intact.

## Individual exact-package outcomes

| Canonical package | Files | Static decision | Authority/behavioral boundary |
|---|---:|---|---|
| `alembic` | 3 | **REJECT unchanged 13/20** | Live upgrade/downgrade/stamp and destructive schema migration lack action-specific DB/environment/backup/rollback authorization; preserve batch, rename and SQL-only review methods |
| `biome` | 6 | **REJECT unchanged 14/20** | Install, unsafe bulk write, linter migration and CI changes lack independent dependency/repository/workflow approval; `biome ci` is a read-only pattern |
| `pydantic-v2` | 6 | **VERIFIED semantic only 16/20** | Model/validation/serialization and settings reference is useful; host must not request real secrets into conversation or disclose `.env` contents/validation errors |
| `sqlalchemy` | 3 | **REJECT unchanged 14/20** | `create_all`, live queries and transaction writes lack separately approved target/data scope; preserve cross-dialect locking, upsert and session methods |
| `tanstack-router` | 7 | **REJECT unchanged 14/20** | Dependency install and auth/loader/router mutations require explicit approved application/security/data scope; preserve `beforeLoad` guard and test harness |
| `tsdoc` | 4 | **VERIFIED semantic only 18/20** | Scoped doc-comment guidance; optional ESLint/CI addition is a separate choice, not default authorization |
| `typescript-typecheck` | 6 | **REJECT unchanged 14/20** | Mandatory `tsconfig`, scripts and CI gate edits need explicit persistent workflow/repository approval; retain `tsc --noEmit` checklist |
| `rest-api-design` | 5 | **VERIFIED semantic only 18/20** | Contract-only API design; no live endpoint, security-control mutation or publication implied |

All eight records have source identity/path, license, exact pin, package tree, SKILL.md blob, source-specific upstream commit/date, bundled-reference/dependency context, portability, controlled taxonomy, rationale, score, authority and explicit `validation_status: not-run`. The verification rubric has ten scored dimensions, and no executed tests, security scan, external adversarial run, or deployment is claimed.

## Systemic findings and omissions

1. **High-value modularity.** SQLAlchemy owns ORM/session/portability, Alembic owns versioned schema evolution, and Pydantic owns validation/serialization. TSDoc and TypeScript typechecking are distinct from Biome linting. REST contract design does not pretend to implement a live service. These are differentiated mechanisms, not eight redundant wrappers.
2. **Operational authority is the main failure mode.** Useful coding instructions embed live database operations, package installation, project-wide rewrites, CI edits, and authentication-control changes. Supplied configuration, an existing connection, a working CLI, or a draft review is not approval for those effects. These five packages are rejected for unchanged reuse, not deleted; scoped adaptation/checklists remain available.
3. **Secrets and private data.** SQLAlchemy's example connection URLs contain placeholder user/password strings; they are not discovered real credentials. Pydantic settings can read environment and secrets directories in an authorized application. Neither authorizes an agent to request real values in chat, echo private data, log credential-bearing URLs, or transmit private records. API error details should not disclose internal paths or secrets.
4. **Evidence freshness.** TanStack Router's bundled research acknowledges full-page WebFetch unavailability and reliance partly on search summaries; its forge-version v1.170.x plugin details need fresh official-document confirmation before implementation. Biome v2, TypeScript 5.x, Pydantic v2 and SQLAlchemy 2.x are June-2026-era source facts, not current-version guarantees. TSDoc's research records a degraded skill-discovery sweep, not a behavioral failure. These caveats are source-specific.
5. **Capability overlap and omissions.** The Alembic↔SQLAlchemy split is coherent, but migration production approval is absent. `typescript-typecheck` and `biome` both mention CI without a reusable authorization gate. TanStack's auth guard is a code pattern, not authorization to alter identity policy or fetch private loader data. Source links to sibling skills not included in this eight-package tranche are dependencies/context, not extra eligible packages or proof.
6. **Priority.** Remaining 26 gaps should be partitioned into (a) provider-operations/external side effects, (b) prior-art/research and discovery, and (c) implementation/reference/creator methods. Deep-review provider operations separately; do not let an easy batch obscure risk.

## Governance and lifecycle

Read current README, AGENTS, Tier-1 governance index, SYSTEM_STATE, curation queue, INDEX/index.json, sources/taxonomy and historical Wayfinder #35, queue #27, structure #41, PR #42 before mutation. The historical tickets do not override current passive governance. The five pre-existing drafts (#489, #492, #496, #412, #413) remain qualification-held, with no current review/check/run/ready evidence sufficient to merge. Seven existing issues remain open; first-party 36-tree security and external adversarial qualification is a concrete blocker. This source-family tranche is disjoint from all first-party repair/admission draft manifests and the shared first-party verification registry.

**Passive architecture preserved:** no source pin, third-party package, first-party manifest, executable runtime, CI workflow, test, generator, scheduler, scanner, or service was added or run. Public accounting must be reconciled on all five surfaces before this tranche merges.
