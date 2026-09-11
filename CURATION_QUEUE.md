# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **20** unique registered source identities.
- **582** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **44/44** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

## Admitted-source curation

### Anthropic Skills — CURRENT-STANDARD COMPLETE
- Pin: `9d2f1ae187231d8199c64b5b762e1bdf2244733d`; **17/17**, gaps **0**, **10 verified / 7 rejected unchanged**.

### Anthropic Knowledge Work Plugins — CURRENT-STANDARD COMPLETE
- Pin: `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8`; **74/74**, gaps **0**, historical **36 verified / 38 rejected unchanged**.

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE
- Pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`; **72/72**, gaps **0**.

### Microsoft Skills — CURRENT-STANDARD COMPLETE
- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; **186/186**, gaps **0**. Direct `.NET` **29/29**; Java **26/26**; Python **40/40**; Rust **9/9**; TypeScript **25/25**.

### Microsoft Azure Skills — CURRENT-STANDARD COMPLETE
- Pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`; **34/34**, gaps **0**.

### Cole Medin Skills — CURRENT-STANDARD COMPLETE
- Pin: `fb2e876f057c5356d6603ba0c52d6b4418d893ba`; **33/33**, gaps **0**.

### David Ondrej Skills — TRACKED / PARTIALLY CURATED
- Pin: `7d0ef87dad1f638cab58995eead9e0e6e3fae237`.
- Exact eligible denominator: **55** first-class packages across agent orchestration **17**, ops/setup **11**, research/web **10**, skill authoring **4**, thinking/docs **13**.
- Current provenance/verification companions: **45/55**; gaps **10**.
- Current decisive states: **17 verified / 28 rejected unchanged**; behavioral validation remains `not-run` for all reviewed units.
- **Skill authoring: 4/4 current-standard complete.**
- **Agent orchestration: 17/17 current-standard complete.**
- **Ops-and-setup: 11/11 current-standard complete.**
- **Research-and-web: 10/10 current-standard complete.** `browser-harness` is rejected unchanged **14/20** because its bundled install/update and troubleshooting paths lack distinct authorization for software mutation, broad process termination, and billable remote sessions. `deep-research` is rejected unchanged **16/20** because its normal workflow defaults to a paid DeepAPI call capped at $0.70 and its larger-report path can issue multiple separately billable calls without distinct authorization for aggregate spend. `deepapi` is rejected unchanged **14/20** because ordinary search/research can spend money without distinct authorization, open-web search mandates 5+ separate paid-capable calls, failed-work/product-friction feedback can be transmitted without separate communication authority, and first daily use automatically launches the installed updater. `fireflies-transcript` is rejected unchanged **15/20** because invalid-key recovery instructs the agent to ask the user for a replacement credential and update local credential state without secure external credential entry or distinct credential-store mutation authority. `online-shopping` is rejected unchanged **15/20** because ordinary mid-range and expensive shopping research can trigger one or more paid DeepAPI requests without a distinct spend-authorization checkpoint; per-request cost caps and configured credentials do not grant spend authority. `pi-web-search` is rejected unchanged **15/20** because failure of its nominal zero-config Exa/Perplexity/Gemini search chain directs the agent to a paid-capable DeepAPI fallback without distinct spend authorization. `research-prompt` is rejected unchanged **16/20** because its execution section directs a fully contextualized prompt to the paid-capable DeepAPI deep-research workflow without distinct spend authorization or separate authorization to transmit embedded project/context details. `twitter-alpha` is rejected unchanged **15/20** because ordinary execution mandates numerous paid-capable DeepAPI Twitter, LinkedIn, and web requests across a seven-person cohort without a distinct spend-authorization checkpoint. `who-is-this` is rejected unchanged **15/20** because ordinary execution mandates multiple paid-capable DeepAPI GitHub, LinkedIn, Twitter/X, and deep-research calls and routes person-specific profile/social data through that external service without distinct spend and disclosure authorization. `youtube-transcript` is rejected unchanged **14/20** because the normal DeepAPI path can spend money without distinct spend authorization, the workflow always persists a transcript file even for non-persistence requests, and first yt-dlp failure directs `yt-dlp -U` without distinct software-mutation authorization. All retain useful adaptation/extraction evidence; behavioral validation is `not-run`.
- **Thinking-and-docs: 3/13 reviewed.** `ask-then-build` is rejected unchanged **16/20** because the ordinary scoping loop directs immediate repository-document mutation after each user answer, including superseding prior decisions, without a distinct repository-mutation authorization checkpoint. Its question sequencing, option framing, decision capture, and implementation-handoff structure remain useful adaptation/extraction evidence. `before-building` is verified **16/20** as a narrow read-only pre-build framing checkpoint; its explicit no-files/no-tools rule keeps the recommendation preliminary when project-specific facts matter. `brain-to-docs` is rejected unchanged **15/20** because ordinary execution mandates updating repository documentation after every user answer with no distinct file-mutation authorization checkpoint; its five-angle questioning, README-versus-ADR partitioning, and concise decision-capture format remain useful adaptation/extraction evidence. Behavioral validation is `not-run`.
- Historical issue #47 / PR #50 accounting of **44** skills for this same public pin is superseded by direct pinned-tree evidence. No state is inferred for the remaining 10.

### Corey Haines Marketing Skills — TRACKED / ADMITTED
- Pin: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` (upstream v2.11.1 state).
- Admitted through issue #297 as a **tracked corpus**, not blanket trusted inventory.
- Root license: **MIT**, copyright Corey Haines (2025).
- Exact eligible denominator: **50** top-level first-class `skills/<name>/SKILL.md` packages. Source guidance defines `SKILL.md` as required for each skill directory, and the pinned source tree exposes 50 top-level skill directories.
- Current provenance/verification companions: **0/50**; gaps **50**. No individual unchanged-reuse eligibility is implied by source admission.
- Out of denominator: partner/integration guides, `tools/` CLI/integration material, source-owned scripts/workflows, generated partner surfaces, and ordinary reference Markdown nested beneath skill packages.
- High-value first review candidates include `customer-research`, `product-marketing`, `pricing`, `attribution`, `content-strategy`, `marketing-plan`, `offers`, `free-tools`, `launch`, and `ai-seo`.
- Authority focus for individual review: ad spend/bids/budgets, outbound communications, CRM/analytics mutations, production publishing, pricing/revenue configuration, credentials/webhooks/tokens, PII/customer-research handling, and commercially sponsored integrations.

### Matt Pocock Skills — CURRENT-STANDARD COMPLETE
- Pin: `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`; **29/29**, gaps **0** after source-policy exclusions.

### Cloudflare Skills — CURRENT-STANDARD COMPLETE
- Pin: `f96bff754e428838818017f75817f0f9428acd48`; **13/13**, gaps **0**, **11 verified / 2 rejected unchanged**.

### Addy Osmani Agent Skills — CURRENT-STANDARD COMPLETE
- Pin: `f63ec56a3cc936408d792956ae583c3c96a825bd`; **24/24**, gaps **0**.

### Vercel Agent Skills — CURRENT-STANDARD COMPLETE
- Pin: `f8a72b9603728bb92a217a879b7e62e43ad76c81`; **9/9**, gaps **0**, **6 verified / 3 rejected unchanged**.

### OpenHands Extensions — CURRENT-STANDARD COMPLETE
- Pin: `87959a7da3e75445647e77b2fbf5bf5b66fb037b`; **1/1**, gaps **0**; `theme-factory` rejected unchanged 14/20.

### Google Agents CLI — CURRENT-STANDARD COMPLETE
- Pin: `ef7808f33fc3038112b69d4ad488ce33b72699b1`; **7/7**, gaps **0**, all verified.

### Cline Skills — CURRENT-STANDARD COMPLETE
- Pin: `26378461e978f2b4e2e6d67b57121b86b2a79ba5`; published **36/36**, gaps **0**; internal/unlisted `review-team` remains outside the denominator.

## Governed discovery / source-vetting

Discovery proceeds in parallel without displacing current-standard source maintenance. Current governed surfaces and candidates include the Creator Technical Resource Catalog, Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator-methodology sources, and bounded candidate work surfaced through current issues. Discovery intelligence never substitutes for canonical source identity, terms, exact-version evidence, or individual quality review.

Issue #297 completed source-level vetting for `coreyhaines31/marketingskills` and moved it from candidate to tracked-corpus admission at an exact snapshot. Individual skills remain unreviewed until companion evidence exists.

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue issue #66 with the David Ondrej frontier now at **45/55 current-standard companion pairs, 10 genuine gaps**. Skill authoring, agent orchestration, ops-and-setup, and research-and-web are current-standard complete at **4/4**, **17/17**, **11/11**, and **10/10**. Continue thinking-and-docs, now **3/13**, after checking current companions and recoverable repository history for each genuine gap; next candidate is `decisions`. Corey Haines Marketing Skills is an admitted tracked corpus at **0/50** and should receive selective exact-version review after the higher-priority David frontier, beginning with differentiated marketing mechanisms rather than wholesale approval.
