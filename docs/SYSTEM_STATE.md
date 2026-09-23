# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-24 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | **633** |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 20 |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | **41 / 50** |
| **Corey Haines Marketing Skills current-standard gaps** | **9** |
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
| **Corey Haines Marketing Skills** | **41 / 50** | **9** |
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

Forty-one packages now have current-standard provenance and exact-version verification companions. Macro tranche 03 adds eight packages: `paywalls` **17/20 VERIFIED**, `popups` **15/20 REJECTED unchanged**, `pricing` **14/20 REJECTED unchanged**, `product-marketing` **13/20 REJECTED unchanged**, `programmatic-seo` **15/20 REJECTED unchanged**, `prospecting` **17/20 VERIFIED**, `public-relations` **14/20 REJECTED unchanged**, and `referrals` **13/20 REJECTED unchanged**. `VERIFIED` here means the exact version passed structured static semantic review; it does not itself assert behavioral validation or automatic unchanged-use eligibility. Behavioral validation is `not-run` for all forty-one reviewed units.

`product-marketing` fails the authority hard rule because its ordinary workflow creates/updates and may move persistent files without a distinct mutation authorization checkpoint. `referrals` fails because its normal launch procedure crosses into external tool/tracking mutation, customer communications, and money-bearing rewards/commissions without distinct authorization checkpoints. `paywalls` has explicit anti-dark-pattern, dismissal, and escape-hatch safeguards; `prospecting` has strong evidence-lineage, anti-scraping, privacy, sensitive-trait, contact-provenance, and downstream-outreach separation safeguards.

**Macro synthesis:** Corey Haines remains substantially stronger as a planning/checklist/design corpus than as unchanged operational authority, but tranche 03 confirms the family is not uniformly reject-only. Recurring defects remain fragmented action authorization, weak privacy/minimization/consent/retention boundaries, unsupported or volatile quantitative marketing/platform claims, and incomplete safeguards around persuasive or dark-pattern-adjacent tactics. Upstream evals are intended-behavior evidence, never behavioral validation. The remaining nine should be treated as one final macro frontier if their actual complexity permits, with deeper review for high-authority, privacy-sensitive, evidence-heavy, or ambiguous packages.

Exact fingerprints, package boundaries, dependencies, controlled tags, freshness evidence, authority findings, scores, and detailed rationale live in the canonical companions under `registry/skills/corey-haines-marketing-skills/` and `registry/verification/corey-haines-marketing-skills/` rather than being duplicated here.

## Provenance and quality state

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44 provenance-complete**. Every governed third-party unit must retain truthful provenance and exact-version verification evidence; unknown facts remain unknown rather than inferred.

Static verification is not behavioral validation. `verified` means the exact bound material passed structured semantic review. `validated` requires representative external behavioral/adversarial evidence that actually exists. `rejected` and `retired` remain prior art but are excluded from normal unchanged selection.

The authority hard fail remains controlling: procedures that can mutate or materially affect infrastructure, external state, production traffic, money-bearing resources, credentials, subscriptions, DNS/routing, security controls, user communications, notifications, identity/access, persistent cloud resources, destructive lifecycle state, or sensitive-data disclosure require a real authorization boundary appropriate to the action.

A corpus-hygiene defect is tracked under #66: some older Corey verification companions use tag values outside the current controlled vocabulary in `registry/taxonomy.yaml`. New reviews use only current controlled values; historical tag drift should be normalized without inventing new behavioral evidence.

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

After every material corpus tranche, reconcile these five public surfaces atomically: `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json`. Recompute counts from live evidence. Do not increment stale counters. Do not merge a material tranche while these surfaces disagree.

## Next action

Complete and merge Corey macro tranche 03 at **41/50 reviewed and 9 gaps**, then recompute the remaining nine as a whole and finish them as one final macro tranche if evidence and complexity permit.
