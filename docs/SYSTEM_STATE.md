# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-11 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | 579 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 20 |
| **Anthropic Skills current-standard companions** | 17 / 17 |
| **Anthropic Knowledge Work Plugins current-standard companions** | 74 / 74 |
| **Anthropic Knowledge Work Plugins current-standard gaps** | 0 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Cole Medin Skills current-standard companions** | 33 / 33 |
| **David Ondrej Skills current-standard companions** | 42 / 55 |
| **David Ondrej Skills current-standard gaps** | 13 |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | 0 / 50 |
| **Matt Pocock Skills current-standard companions** | 29 / 29 |
| **Cloudflare Skills current-standard companions** | 13 / 13 |
| **Addy Osmani Agent Skills current-standard companions** | 24 / 24 |
| **Vercel Agent Skills current-standard companions** | 9 / 9 |
| **OpenHands Extensions current-standard companions** | 1 / 1 |
| **Google Agents CLI current-standard companions** | 7 / 7 |
| **Cline Skills published current-standard companions** | 36 / 36 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Microsoft TypeScript direct-package companions** | 25 / 25 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **44/44 provenance-complete**.
- Anthropic Skills: **17/17**, gaps **0**, **10 verified / 7 rejected unchanged**.
- Anthropic Knowledge Work Plugins: **74/74**, gaps **0**, historical states **36 verified / 38 rejected unchanged**.
- AWS Agent Toolkit: **72/72**, gaps **0**.
- Microsoft Skills: **186/186**, gaps **0**.
- Microsoft Azure Skills: **34/34**, gaps **0**.
- Cole Medin Skills: **33/33**, gaps **0**.
- David Ondrej Skills: exact registered-pin denominator **55**, **42/55** provenance/verification companion complete, gaps **13**; current decisive states **16 verified / 26 rejected unchanged**. Skill authoring is **4/4** complete; agent orchestration is **17/17** complete; ops-and-setup is **11/11** complete; research-and-web is **10/10** current-standard complete; thinking-and-docs remains **0/13**.
- Corey Haines Marketing Skills: tracked at exact snapshot `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`; exact eligible denominator **50** top-level first-class `skills/<name>/SKILL.md` packages; **0/50** individually current-standard reviewed. Root license is MIT. Partner/integration guides, source-owned CLI/tooling, generated partner surfaces, and ordinary reference Markdown do not count toward the skill denominator.
- Matt Pocock Skills: **29/29**, gaps **0** after source-policy exclusions.
- Cloudflare Skills: **13/13**, gaps **0**, **11 verified / 2 rejected unchanged**.
- Addy Osmani Agent Skills: **24/24**, gaps **0**.
- Vercel Agent Skills: **9/9**, gaps **0**, **6 verified / 3 rejected unchanged**.
- OpenHands Extensions: **1/1**, gaps **0**; `theme-factory` remains **rejected unchanged 14/20**.
- Google Agents CLI: **7/7**, gaps **0**, all seven verified.
- Cline Skills: **36/36 published**, gaps **0**; internal/unlisted `review-team` remains outside the denominator.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## David Ondrej denominator reconciliation

The registered public snapshot is `7d0ef87dad1f638cab58995eead9e0e6e3fae237`. Direct inspection establishes five category folders with **17 + 11 + 10 + 4 + 13 = 55** first-class skill packages. Current repository evidence contains forty-two exact-version companion pairs. Skill authoring is **4/4** current-standard complete, agent orchestration is **17/17** current-standard complete, ops-and-setup is **11/11** current-standard complete, research-and-web is **10/10** current-standard complete, and thinking-and-docs remains **0/13**.

`browser-harness` is **rejected unchanged 14/20** because bundled installation guidance instructs automatic software update without asking the user, troubleshooting may escalate to broad Chrome/daemon termination, and remote Browser Use sessions can create cost-bearing cloud resources without a distinct authorization boundary. Its screenshot-first interaction, explicit authentication-wall stopping behavior, local/remote routing, and visible-state verification remain useful adaptation/extraction evidence.

`deep-research` is **rejected unchanged 16/20**. It is manual-only, handles its API key through external environment/local credential state without printing it, uses idempotency keys, bounds retries, and produces source-backed reports. It nevertheless defaults to a paid DeepAPI request with `maxCostUsd` 0.70 and can fan larger reports into multiple separately billable calls without a distinct aggregate-spend authorization boundary. Approval only for raising one call above $0.70 does not authorize several default-priced calls. Behavioral validation is `not-run`.

`deepapi` is **rejected unchanged 14/20**. Its exact package has strong secret non-disclosure, idempotency, dry-run previews, endpoint routing, polling/error recovery, and sound local approvals in some high-risk subflows. Unchanged use nevertheless fails the authority hard fail because ordinary search/research can spend money without distinct authorization, open-web search requires 5+ separately paid-capable calls, failed work and product-friction reports can be transmitted externally without separate communication authority, and first daily use automatically launches the installed updater. Behavioral validation is `not-run`.

`fireflies-transcript` is **rejected unchanged 15/20**. It is a focused read-only Fireflies.ai transcript retriever with good local-secret non-disclosure, recent-meeting listing, pagination, speaker/topic verification, and large-output handling. Its invalid-key recovery path nevertheless tells the agent to ask the user for a replacement API key and update a local environment file without requiring secure external credential entry or distinct authorization for credential-store mutation. Behavioral validation is `not-run`.

`online-shopping` is **rejected unchanged 15/20**. It is explicitly research-only, forbids orders/payment/address/account creation, keeps its DeepAPI credential external and undisclosed, scales effort by purchase price, verifies unknown shops, and requires found-price evidence. Unchanged use nevertheless fails the money-bearing authority hard fail because normal mid-range and expensive shopping research directs one or more paid DeepAPI calls with per-request cost caps but no distinct spend-authorization checkpoint. Behavioral validation is `not-run`.

`pi-web-search` is **rejected unchanged 15/20**. It is tightly scoped to Pi Agents and provides useful routing across web search, code search, URL/PDF/video/GitHub retrieval, and large-content continuation, with explicit query-depth minimums. Unchanged use nevertheless fails the money-bearing authority hard fail because failure of the nominal zero-config Exa/Perplexity/Gemini chain directs the agent to a DeepAPI fallback capable of paid external requests without a distinct spend-authorization checkpoint. Behavioral validation is `not-run`.

`research-prompt` is **rejected unchanged 16/20**. It provides strong research-question decomposition, source hierarchy, contradiction handling, corroboration requirements, completion criteria, and iterative gap-closing. Unchanged use nevertheless fails the authority hard fail because its execution section directs a fully contextualized prompt to the paid-capable DeepAPI deep-research workflow without a distinct spend-authorization checkpoint or separate authorization for transmitting embedded project/context details to that external service. Behavioral validation is `not-run`.

`twitter-alpha` is **rejected unchanged 15/20**. It provides a differentiated method for constructing a seven-person insider/outsider cohort from observed X engagement, verifying handles, retaining sparse posters via LinkedIn fallback, ranking concrete non-obvious signals, and returning concise source-linked findings. Unchanged use nevertheless fails the money-bearing authority hard fail because ordinary execution mandates numerous DeepAPI Twitter, LinkedIn, and web requests across the cohort without a distinct spend-authorization checkpoint. Behavioral validation is `not-run`.

`who-is-this` is **rejected unchanged 15/20**. It is manual-only and has strong identity-disambiguation, cross-platform evidence gathering, claim-versus-evidence labeling, missing/private-profile handling, and concise verdict discipline. Unchanged use nevertheless fails the authority hard fail because ordinary execution mandates multiple paid-capable DeepAPI GitHub, LinkedIn, Twitter/X, and deep-research calls without distinct spend authorization and routes person-specific profile/social data through that external service without a separate disclosure boundary. Behavioral validation is `not-run`.

`youtube-transcript` is **rejected unchanged 14/20**. It has a useful transcript extraction flow with DeepAPI idempotency, caption-only yt-dlp fallback, language handling, json3 duplicate-caption avoidance, bounded retry, explicit bot-detection stop behavior, and deterministic naming. Unchanged use nevertheless fails the authority hard fail because the normal DeepAPI path can spend money without distinct spend authorization, the skill always persists a transcript file even for requests that only ask what a video says, and first yt-dlp failure instructs `yt-dlp -U` without distinct software-mutation authorization. Behavioral validation is `not-run`.

Together the David Ondrej family is **42/55**, with **13** gaps and **16 verified / 26 rejected unchanged**.

## Corey Haines source admission

Issue #297 established the exact source identity `coreyhaines31/marketingskills` and admitted it as a **tracked corpus**, not as a blanket trusted or pinned-reference corpus. The registered snapshot is `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` (upstream v2.11.1 state). Direct tree inspection shows **50** top-level skill directories under `skills/`, and source guidance defines each `skills/<name>/SKILL.md` as the required first-class skill entry point. Root terms are MIT. Commercial partner/integration material and source-maintained tooling remain source context and are excluded from the 50-skill denominator. Individual unchanged reuse still requires exact-version review.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue corpus-wide provenance audit #66. David Ondrej Skills is now **42/55**, with **13** exact-version companion gaps; skill authoring, agent orchestration, ops-and-setup, and research-and-web are complete at **4/4**, **17/17**, **11/11**, and **10/10**.
2. Reconcile David Ondrej thinking-and-docs history before fresh review; thinking-and-docs remains **0/13**.
3. Begin selective exact-version curation of the newly admitted Corey Haines Marketing Skills **50-skill** tracked corpus after higher-priority admitted-source gaps, starting with high-differentiation user-fit candidates rather than wholesale approval.
4. Continue recomputing remaining admitted and tracked families for genuine provenance, fingerprint, exact-pin, or canonical-path gaps.
5. Continue governed discovery/source-vetting and omission recovery.
6. Resolve bounded candidate issues when evidence supports a decisive outcome.
7. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.