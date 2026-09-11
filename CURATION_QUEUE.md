# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority. Detailed exact-version evidence belongs in canonical companions under `registry/`.

## Current governed depth

- **44** first-party user-facing skills, **44/44** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **574** persisted exact-version third-party verification companions.
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
- Current provenance/verification companions: **37/55**; gaps **18**.
- Current decisive states: **16 verified / 21 rejected unchanged**; behavioral validation remains `not-run` for all reviewed units.
- **Skill authoring: 4/4 current-standard complete.**
- **Agent orchestration: 17/17 current-standard complete.**
- **Ops-and-setup: 11/11 current-standard complete.**
- **Research-and-web: 5/10 reviewed.** `browser-harness` is rejected unchanged **14/20** because its bundled install/update and troubleshooting paths lack distinct authorization for software mutation, broad process termination, and billable remote sessions. `deep-research` is rejected unchanged **16/20** because its normal workflow defaults to a paid DeepAPI call capped at $0.70 and its larger-report path can issue multiple separately billable calls without distinct authorization for aggregate spend. `deepapi` is rejected unchanged **14/20** because ordinary search/research can spend money without distinct authorization, open-web search mandates 5+ separate paid-capable calls, failed-work/product-friction feedback can be transmitted without separate communication authority, and first daily use automatically launches the installed updater. `fireflies-transcript` is rejected unchanged **15/20** because invalid-key recovery instructs the agent to ask the user for a replacement credential and update local credential state without secure external credential entry or distinct credential-store mutation authority. `online-shopping` is rejected unchanged **15/20** because ordinary mid-range and expensive shopping research can trigger one or more paid DeepAPI requests without a distinct spend-authorization checkpoint; per-request cost caps and configured credentials do not grant spend authority. All retain useful adaptation/extraction evidence; behavioral validation is `not-run`.
- **Thinking-and-docs: 0/13 current-standard companions.** Reconcile companions/history before fresh review.
- Historical issue #47 / PR #50 accounting of **44** skills for this same public pin is superseded by direct pinned-tree evidence. No state is inferred for the remaining 18.

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

## Lifecycle hygiene

At each run: inspect every open PR and issue; merge a current authorized ready PR; close evidence-complete/duplicate/superseded bounded issues; state concrete blockers; reconcile README, `docs/SYSTEM_STATE.md`, this ledger, `INDEX.md`, and `index.json` atomically after material corpus changes; preserve the passive architecture.

## Historical authority boundary

Wayfinder #35 remains canonical destination/scope evidence, but stale frontier text is historical. Source queue #27, structure ticket #41, and PR #42 are closed historical evidence. Current README and Tier-1 governance control live execution.

## Next action

Continue issue #66 with the David Ondrej frontier now at **37/55 current-standard companion pairs, 18 genuine gaps**. Skill authoring, agent orchestration, and ops-and-setup are current-standard complete at **4/4**, **17/17**, and **11/11**. Continue the bounded research-and-web category, now **5/10**, after checking current companions and recoverable repository history for each genuine gap; keep discovery/source-vetting and omission detection parallel and secondary.