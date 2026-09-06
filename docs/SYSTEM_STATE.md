# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-05 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 361 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 3 / 131 |
| **Microsoft Azure Skills current-standard gaps** | 128 |
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

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **186**, **186/186 companion-complete**, **0 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft Azure Skills: exact registered-pin denominator **131**, **3/131 companion-complete**, **128 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Microsoft Skills closure

Microsoft Skills closes at **186/186** with **0** gaps after exact-pin denominator reconciliation removed ordinary Foundry Markdown and dangling duplicate symlink exposures from the eligible count.

## Microsoft Azure Skills frontier

The registered source pin is `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`, with **131** eligible skill packages.

`airunway-aks-setup` is verified **17/20** by structured static review at exact tree `72ec58c0a7c574dc71e14c63feb3d2aa529849ac` and `SKILL.md` blob `26bbd92815116826696fb6380d37446a285496b9`; behavioral validation remains `not-run`. Mutating controller, provider, secret, and model-deployment operations are gated by explicit user-confirmation rules immediately before install/deployment actions.

`appinsights-instrumentation` is rejected unchanged **13/20** at exact tree `8f6b0c9b5af9ab5bbd69d25d58071c9034221eb0` and `SKILL.md` blob `ca55c310862cb95b5ebcc1f10a070f312718d1cb`; freshness is bound to upstream revision `a98eb86dc2a7b2bc57bdc0c346421576782bf3e5` on 2026-05-05 and behavioral validation remains `not-run`. Its guidance, context collection, auto-instrumentation preference, and SDK/platform references are useful, but the manual path directs Azure resource creation and app-setting mutation without a distinct action-specific authorization checkpoint immediately before those operations.

`azure-ai` is rejected unchanged **13/20** at exact tree `8a168336305c56e0eea0d89aced7d8a0001de3b5` and `SKILL.md` blob `6cce5b319f57f98f81772e4c8627c573d89e8571`; freshness is bound to upstream revision `317a8e7b879c0ed6a1890378eafd939bdd9bc749` on 2026-04-22 and behavioral validation remains `not-run`. Preserve its service-routing matrix, MCP-first tool map, SDK quick-reference map, and managed-identity authentication guidance. Reject unchanged because ordinary triggered use can transmit search queries, audio, synthesized-text inputs, documents/OCR payloads, prompts, or other user data to external Azure AI services and may incur paid usage without a distinct action-specific authorization checkpoint immediately before transmission or invocation.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Azure Skills from **3/131**, checking canonical companion paths and repository history before each unit.
2. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
3. Continue governed discovery/source-vetting and omission recovery.
4. Resolve bounded candidate issues when evidence supports a decisive outcome.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.