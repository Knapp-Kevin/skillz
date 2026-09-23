# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-23 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | **625** |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 20 |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | **33 / 50** |
| **Corey Haines Marketing Skills current-standard gaps** | **17** |
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
| **Corey Haines Marketing Skills** | **33 / 50** | **17** |
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

Thirty-three packages now have current-standard provenance and exact-version verification companions. The first twenty-five dispositions remain as recorded in their canonical companions. Macro tranche 02 adds eight rejected-unchanged packages: `lead-magnets`, `marketing-council`, `marketing-ideas`, `marketing-loops`, `marketing-plan`, `marketing-psychology`, `offers`, and `onboarding`. Behavioral validation is `not-run` for all thirty-three.

`marketing-plan` fails the authority hard rule because ordinary procedure includes persistent file creation and optional external API/data pulls without a distinct authorization boundary. The other seven tranche-02 packages are primarily advisory/planning artifacts and do not establish an authority hard fail, but unchanged adoption is rejected for combinations of unsupported or volatile claims, privacy/consent/minimization gaps, simulated-authority concerns, planning-to-execution boundary blur, and insufficient non-deception safeguards around persuasion, scarcity, urgency, profiling, or behavioral instrumentation.

**Macro synthesis:** Corey Haines is substantially stronger as a planning/checklist/design corpus than as unchanged operational authority. Across the first thirty-three reviews, recurring defects cluster around fragmented action authorization, weak privacy/minimization/consent/retention boundaries, unsupported or volatile quantitative marketing/platform claims, and incomplete safeguards around persuasive or dark-pattern-adjacent tactics. Upstream evals are treated as intended-behavior evidence, never behavioral validation. The remaining seventeen should therefore continue under macro mapping and coherent tranches while preserving individual exact-version decisions and deeper review for high-authority, privacy-sensitive, evidence-heavy, or ambiguous packages.

Exact fingerprints, package boundaries, dependencies, controlled tags, freshness evidence, authority findings, scores, and detailed rationale live in the canonical companions under `registry/skills/corey-haines-marketing-skills/` and `registry/verification/corey-haines-marketing-skills/` rather than being duplicated here.

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

After every material corpus tranche, reconcile these five public surfaces atomically:

1. `README.md`
2. `docs/SYSTEM_STATE.md`
3. `CURATION_QUEUE.md`
4. `INDEX.md`
5. `index.json`

Recompute counts from live evidence. Do not increment stale counters. At minimum keep persisted exact-version review count, active source-family completion, denominator, gaps, completed sub-family denominators, and active frontier consistent. Do not perform five-surface ceremony after every individual record when a coherent tranche is still in progress, but do not merge a material tranche while these surfaces disagree.

## Next action

Continue the Corey Haines Marketing Skills frontier from **33/50 reviewed and 17 gaps** using the macro-first cycle shape: recompute the remaining frontier, select a coherent bounded tranche, deep-review ambiguous/high-authority/privacy/evidence-sensitive packages, batch shared source facts without weakening individual evidence, synthesize family-level findings, and reconcile all five public accounting surfaces before merge.
