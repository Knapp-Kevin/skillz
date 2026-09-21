# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-21 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | **598** |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 20 |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | **6 / 50** |
| **Corey Haines Marketing Skills current-standard gaps** | **44** |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

Normal DIRECT_LIBRARY, FIRST_VISIT, and RETURNING_USER work treats this repository as read-only reference material. User-derived skills target the user's active host/environment or a portable handoff. Only explicit REPOSITORY_MAINTENANCE authority permits repository mutation.

## Current admitted-source accounting

| Source family | Reviewed / denominator | Gaps |
|---|---:|---:|
| Anthropic Skills | 17 / 17 | 0 |
| Anthropic Knowledge Work Plugins | 74 / 74 | 0 |
| AWS Agent Toolkit | 72 / 72 | 0 |
| Microsoft Skills | 186 / 186 | 0 |
| Microsoft Azure Skills | 34 / 34 | 0 |
| Cole Medin Skills | 33 / 33 | 0 |
| David Ondrej Skills | 55 / 55 | 0 |
| **Corey Haines Marketing Skills** | **6 / 50** | **44** |
| Matt Pocock Skills | 29 / 29 | 0 |
| Cloudflare Skills | 13 / 13 | 0 |
| Addy Osmani Agent Skills | 24 / 24 | 0 |
| Vercel Agent Skills | 9 / 9 | 0 |
| OpenHands Extensions | 1 / 1 | 0 |
| Google Agents CLI | 7 / 7 | 0 |
| Cline Skills (published) | 36 / 36 | 0 |

Microsoft direct-package accounting remains `.NET` **29/29**, Java **26/26**, Python **40/40**, Rust **9/9**, and TypeScript **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected and retired material remains useful bounded prior art.

## Active curation frontier: Corey Haines Marketing Skills

Registered snapshot: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`. Root license: MIT. Exact eligible denominator: **50** top-level first-class `skills/<name>/SKILL.md` packages. Partner/integration guides, source-owned tooling, generated partner surfaces, and ordinary reference Markdown are outside the denominator.

Six packages now have current-standard provenance and exact-version verification companions:

- `ab-testing`: **rejected unchanged 13/20**, behavioral validation `not-run`. Useful experiment-planning mechanisms remain adaptation/extraction evidence, but unchanged adoption is rejected for materially inconsistent sample-size guidance and misleading frequentist p-value/confidence semantics.
- `ad-creative`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful grounding, source-traceability, creative-format, performance-learning, review-template, and human-review mechanisms remain adaptation/extraction evidence, but unchanged adoption lacks distinct authorization boundaries for persistent file mutation and client-facing publication/communication.
- `ads`: **rejected unchanged 15/20**, behavioral validation `not-run`. Strong evidence, budgeting, read-only audit, and reversible-change mechanisms remain adaptation/extraction evidence, but operational paths do not consistently inherit explicit authorization for spend, launches, customer-data operations, persistence, integrations, and recurring communication.
- `ai-seo`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful AI-search/content mechanisms remain adaptation/extraction evidence, but unchanged adoption contains materially incorrect crawler-control semantics and insufficient explicit authorization boundaries around website mutation/publication and identity-bearing external activity.
- `analytics`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful decision-first measurement, event taxonomy, debugging, data-quality, consent, and minimization mechanisms remain adaptation/extraction evidence, but normal implementation paths prescribe GA4/GTM/site/configuration mutation and privacy-sensitive telemetry activation without distinct explicit authorization boundaries.
- `aso`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful read-only ASO audit structure, Apple/Google differentiation, evidence-gap handling, visual review, competitor comparison, and prompt-injection boundaries remain adaptation/extraction evidence, but unchanged adoption presents volatile platform and benchmark claims too confidently, including prescriptive Google Play keyword-density targets and asserted Apple screenshot-caption indexing, while several bundled benchmark statistics lack claim-level traceability.

Exact fingerprints, package boundaries, dependencies, controlled tags, freshness evidence, authority findings, and detailed rationale live in the canonical companions under `registry/skills/corey-haines-marketing-skills/` and `registry/verification/corey-haines-marketing-skills/`.

## Provenance and quality state

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44 provenance-complete**. Every governed third-party unit must retain truthful provenance and exact-version verification evidence; unknown facts remain unknown rather than inferred.

Static verification is not behavioral validation. `verified` means the exact bound material passed structured semantic review. `validated` requires representative external behavioral/adversarial evidence that actually exists. `rejected` and `retired` remain prior art but are excluded from normal unchanged selection.

The authority hard fail remains controlling: procedures that can mutate or materially affect infrastructure, external state, production traffic, money-bearing resources, credentials, subscriptions, DNS/routing, security controls, user communications, notifications, identity/access, persistent cloud resources, destructive lifecycle state, or sensitive-data disclosure require a real authorization boundary appropriate to the action.

## Discovery and source vetting

Discovery runs in parallel with admitted-source curation but never grants quality, trust, installation authority, redistribution rights, or automatic admission. New third-party discoveries use the issue-first lifecycle in `docs/candidate-intake.md`.

Current governed discovery surfaces include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, canonical creator/source repositories, and candidate work recorded in the living curation ledger. Restricted or unclear-license material remains reference-only unless terms justify another role.

`ConsultingFuture4200/unusual-thoughts` (#307) and `ConsultingFuture4200/repo-readme` (#308) are closed REFERENCE-ONLY candidates because canonical redistribution terms sufficient for governed corpus inclusion were not established.

## Current authority and lifecycle surfaces

- Wayfinder #35 remains canonical destination/scope evidence. Its stale frontier text is historical.
- Source queue #27, structure ticket #41, and PR #42 are closed historical evidence, not live execution authority.
- Current README, AGENTS, Governance Index, this file, CURATION_QUEUE, INDEX, index.json, source registry, and taxonomy control live repository truth.
- Open PRs and issues must be triaged before new curation. Ready authorized work should move through merge/closure rather than becoming permanent lifecycle furniture.

## Accounting contract

After every material corpus change, reconcile these five public surfaces atomically:

1. `README.md`
2. `docs/SYSTEM_STATE.md`
3. `CURATION_QUEUE.md`
4. `INDEX.md`
5. `index.json`

Recompute counts from live evidence. Do not increment stale counters. At minimum keep persisted exact-version review count, active source-family completion, denominator, gaps, completed sub-family denominators, and active frontier consistent.

## Next action

Continue the Corey Haines Marketing Skills frontier from **6/50 reviewed and 44 gaps**. Before each new unit, confirm it is a genuine gap, inspect existing provenance/verification paths and compatible history, review the exact pinned package and bundled references, apply authority and sensitive-data hard fails, persist decisive evidence, and reconcile all five public accounting surfaces atomically.