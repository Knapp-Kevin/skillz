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
| **Persisted third-party review companions** | **617** |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 20 |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | **25 / 50** |
| **Corey Haines Marketing Skills current-standard gaps** | **25** |
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
| **Corey Haines Marketing Skills** | **25 / 50** | **25** |
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

Twenty-five packages now have current-standard provenance and exact-version verification companions:

- `ab-testing`: **rejected unchanged 13/20**, behavioral validation `not-run`. Useful experiment-planning mechanisms remain adaptation/extraction evidence, but unchanged adoption is rejected for materially inconsistent sample-size guidance and misleading frequentist p-value/confidence semantics.
- `ad-creative`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful grounding, source-traceability, creative-format, performance-learning, review-template, and human-review mechanisms remain adaptation/extraction evidence, but unchanged adoption lacks distinct authorization boundaries for persistent file mutation and client-facing publication/communication.
- `ads`: **rejected unchanged 15/20**, behavioral validation `not-run`. Strong evidence, budgeting, read-only audit, and reversible-change mechanisms remain adaptation/extraction evidence, but operational paths do not consistently inherit explicit authorization for spend, launches, customer-data operations, persistence, integrations, and recurring communication.
- `ai-seo`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful AI-search/content mechanisms remain adaptation/extraction evidence, but unchanged adoption contains materially incorrect crawler-control semantics and insufficient explicit authorization boundaries around website mutation/publication and identity-bearing external activity.
- `analytics`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful decision-first measurement, event taxonomy, debugging, data-quality, consent, and minimization mechanisms remain adaptation/extraction evidence, but normal implementation paths prescribe GA4/GTM/site/configuration mutation and privacy-sensitive telemetry activation without distinct explicit authorization boundaries.
- `aso`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful read-only ASO audit structure, Apple/Google differentiation, evidence-gap handling, visual review, competitor comparison, and prompt-injection boundaries remain adaptation/extraction evidence, but unchanged adoption presents volatile platform and benchmark claims too confidently, including prescriptive Google Play keyword-density targets and asserted Apple screenshot-caption indexing, while several bundled benchmark statistics lack claim-level traceability.
- `attribution`: **rejected unchanged 15/20**, behavioral validation `not-run`. Strong source-of-truth discipline, model caveats, incrementality, self-reported attribution, fail-closed identity handling, webhook verification, PII-aware logging, confidence labeling, and conservative backfill remain useful adaptation/extraction evidence. Unchanged adoption fails because normal implementation paths prescribe persistent analytics/CRM/identity mutation and privacy-sensitive identifier transmission without distinct explicit authorization checkpoints.
- `churn-prevention`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful voluntary/involuntary churn separation, intervention mapping, visible cancellation paths, dark-pattern avoidance, payment-failure classification, dunning/grace-period structure, and cohort measurement remain adaptation/extraction evidence. Unchanged adoption fails because normal procedures prescribe billing/account mutations, integrations, data processing, and customer communications without distinct explicit authorization checkpoints; volatile benchmark and legal/regulatory claims also lack claim-level sourcing.
- `co-marketing`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful partner identification, scoring, campaign ideation, agreement, measurement, routing, and partnership taxonomy remain adaptation/extraction evidence. Unchanged adoption fails because normal procedures prescribe partner communications, lead/data sharing, publication, commercial offers, brand use, and external actions without distinct explicit authorization checkpoints; volatile quantitative claims also lack claim-level primary sourcing.
- `cold-email`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful brevity, problem-linked personalization, framework selection, low-friction CTAs, follow-up rotation, breakup-email finality, critique, and routing remain adaptation/extraction evidence. No authority hard fail applies because the package itself is generate-only, but evidence, privacy/compliance, anti-deception, and separate send-authorization boundaries remain insufficient.
- `community-marketing`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful shared-identity, member-first value, community flywheel, journey design, rituals, ambassador, support, platform-selection, health, and scaling mechanisms remain adaptation/extraction evidence. Unchanged adoption fails because normal procedures prescribe communications, access/role changes, incentives, member tracking/data processing, and publication without distinct authorization checkpoints; volatile health/growth benchmarks also lack claim-level sourcing.
- `competitor-profiling`: **rejected unchanged 16/20**, behavioral validation `not-run`. Strong read-only classification, evidence tiers, source triangulation, freshness/confidence labels, unknown-field handling, profiles, matrices, battlecards, win/loss synthesis, and prompt-injection safeguards remain useful. No authority hard fail applies; unchanged adoption needs stronger privacy/data-minimization/source-terms boundaries and current verification for volatile vendor capability/pricing guidance.
- `competitors`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful comparison-page structures, honest positioning, centralized competitor data, templates, research/update cadence, internal linking, and sales-enablement routing remain useful. Unchanged adoption fails because normal procedures prescribe persistent data/page creation, sitewide changes, and publication of comparative claims/CTAs without distinct mutation/publication authorization; research also needs stronger privacy/source-terms and current claim verification.
- `content-strategy`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful research inputs, buyer-stage mapping, pillars/clusters, weighted prioritization, content-as-product, distribution, atomization, and content-model/CMS guidance remain useful. Unchanged adoption fails because ordinary procedures prescribe identity-bearing distribution and persistent CMS/site/configuration/permissions/webhook/migration/publication actions without distinct authorization; research/privacy/source terms and volatile evidence also need strengthening.
- `copy-editing`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful multi-pass editing, final checklist, plain-language, specificity/voice, and refresh-vs-rewrite remain useful. No authority hard fail applies. Unchanged adoption is rejected for unsupported volatile AI-search/SEO and cadence claims plus insufficient source-verification and data-handling boundaries.
- `copywriting`: **rejected unchanged 14/20**, behavioral validation `not-run`. Strong generate-only routing, context gathering, clarity/specificity/customer language, page structures, CTA, voice/tone, annotated alternatives, Now-you-can test, Human Action Model, and Perception Gap remain useful. No authority hard fail applies; unchanged adoption is rejected for unsupported quantitative performance claims and insufficient customer-data safeguards.
- `cro`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful read-only CRO audit, page-specific frameworks, experiment hypotheses, and form UX remain useful. No authority hard fail applies. Unchanged adoption is rejected for unsupported quantitative form/UX claims, inadequate enrichment/profiling privacy boundaries, and missing current-claim verification for proof/security/review/case-study/ROI/guarantee content.
- `customer-research`: **rejected unchanged 15/20**, behavioral validation `not-run`. Strong read-only extraction, source weighting, confidence labels, and disconfirmation remain useful; active primary research fails the authority hard fail because CRM segmentation, outreach, interviews/surveys, and incentives lack distinct communication, customer-data, and money-bearing authorization checkpoints. Public-source/support-ticket research also needs stronger privacy/source-terms boundaries and several PMF/sample/incentive heuristics lack claim-level evidence.
- `directory-submissions`: **rejected unchanged 12/20**, behavioral validation `not-run`. Useful readiness, tiering, positioning-variant, tracker, and destination-before-distribution mechanisms remain useful; external submission/publication/community/review-incentive/outreach workflows fail the authority hard fail and volatile Product Hunt/G2/backlink/AI-ranking claims lack adequate primary evidence.
- `emails`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful generate-only sequence routing, one-email-one-job, value-before-ask, structured metadata, and lifecycle templates remain useful. No authority hard fail applies because ordinary behavior drafts/plans, but cadence/engagement claims lack evidence, personalization/segmentation needs explicit data safeguards, and live send/automation requires separate authorization.
- `events`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful portfolio selection, ICP-overlap economics, lifecycle decomposition, follow-up tiering, qualified-conversation focus, and metric discipline remain useful. Unchanged adoption fails the authority hard fail through spend, negotiation, outreach, attendee data, CRM routing, hosting, recording, publication, and follow-up without universal distinct authorization.
- `free-tools`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful ideation, adjacency, build-vs-buy, MVP scope, maintenance/security-debt, and scorecard mechanisms remain useful. No authority hard fail applies because ordinary behavior is strategy/evaluation; unchanged adoption is rejected because benchmark claims lack claim-level primary evidence and lead capture lacks explicit data-governance boundaries.
- `image`: **rejected unchanged 13/20**, behavioral validation `not-run`. Useful tool/model routing, prompt structure, real-screenshot integrity, brand consistency, asset-type distinctions, and optimization remain useful. Unchanged adoption fails the authority hard fail through paid external generation/API use, asset upload/disclosure, and file mutation without distinct authorization; rights/likeness/provenance/credential safeguards are incomplete and model/platform guidance is volatile.
- `influencer-marketing`: **rejected unchanged 15/20**, behavioral validation `not-run`. Useful creator-fit vetting, compensation-model comparison, disclosure/compliance, creative briefs, agreement dimensions, measurement, and a compliance-rewritten UGC playbook remain useful. Unchanged adoption fails the authority hard fail through outreach, compensation, commercial terms/rights, account operation, publication, tracking, and whitelisting without distinct authorization; legal/platform/compensation guidance also requires current verification.
- `launch`: **rejected unchanged 14/20**, behavioral validation `not-run`. Useful SLC readiness, channel framing, phased progression, touchpoint checklist, announcement sizing, and post-launch momentum remain useful. Unchanged adoption fails the authority hard fail through site/signup mutation, public announcements, user invitations, communications, Product Hunt activity, publication, access-state changes, and charging without distinct authorization; case/channel claims also need current evidence.

**Macro synthesis:** the first concerted tranche confirms that Corey Haines is substantially more valuable as a planning/checklist/design corpus than as unchanged operational authority. Recurring defects are fragmented action authorization, weak privacy/minimization/consent/retention boundaries around audience/customer/attendee/creator/reference data, and volatile quantitative marketing/platform claims that upstream evals often encode as expected behavior rather than independently prove. The curation model therefore uses macro mapping and coherent tranches for shared source facts while preserving individual exact-version dispositions and deeper review for high-authority, privacy-sensitive, evidence-heavy, or ambiguous packages.

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

After every material corpus tranche, reconcile these five public surfaces atomically:

1. `README.md`
2. `docs/SYSTEM_STATE.md`
3. `CURATION_QUEUE.md`
4. `INDEX.md`
5. `index.json`

Recompute counts from live evidence. Do not increment stale counters. At minimum keep persisted exact-version review count, active source-family completion, denominator, gaps, completed sub-family denominators, and active frontier consistent. Do not perform five-surface ceremony after every individual record when a coherent tranche is still in progress, but do not merge a material tranche while these surfaces disagree.

## Next action

Continue the Corey Haines Marketing Skills frontier from **25/50 reviewed and 25 gaps** using the macro-first cycle shape: recompute the remaining frontier, select a coherent bounded tranche, deep-review ambiguous/high-authority/privacy/evidence-sensitive packages, batch shared source facts without weakening individual evidence, synthesize family-level findings, and reconcile all five public accounting surfaces before merge.
