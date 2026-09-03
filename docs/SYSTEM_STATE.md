# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-03 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 304 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 132 / 189 |
| **Microsoft Skills current-standard gaps** | 57 |
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
- Microsoft Skills: exact denominator **189**, **132/189 companion-complete**, **57 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Microsoft TypeScript closure

The registered-pin TypeScript tree contains exactly **25** first-class packages. Its upstream plugin README says 24 because it omits `applicationinsights-web-ts`, which nevertheless exists as a separate first-class package at the same pin. Tree truth controls the denominator.

The direct TypeScript slice is now **25/25 current-standard companion-complete**. Its decisive states are twenty-two rejected unchanged and three verified local implementation packages. The final three units are:

- `m365-agents-ts` — **rejected unchanged, 13/20**. Exact package tree `0bcb6ef9c55c8f8bae331e85d40f8585844c4bc7`, `SKILL.md` blob `00169cce10c70508375fc9300513a7600c7f75f8`, skill-specific freshness revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. It preserves useful AgentApplication, Express hosting, streaming, sensitivity-label, invoke, Copilot Studio, API-freshness, and secret-hygiene mechanics. Unchanged adoption fails because ordinary user messaging, generated-content streaming, invoke acknowledgement, remote Copilot conversations/questions, WebChat connections, Azure OpenAI data transfer, and tenant/client secret or bearer-token use lack mandatory tenant/environment, audience, message/data-owner/classification, identity/access, model-data-transfer, production, per-action communication, and credential-custody authorization.
- `react-flow-node-ts` — **verified, 15/20**. Exact package tree `ba384d63f352c5518b3dd77168e5c49af2220e8a`, `SKILL.md` blob `ab4e1a6a5a4c1bf03f4d9b49dee6285e9ce0457d`, plus template blobs `8539c7b0fd5b453c9564a675b3e2fcaedeaf1c34` and `46c9e2ee44ff517693d611ad2e94388cff669adc`; freshness revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. It is bounded local React Flow node-generation guidance. Portability is medium because it assumes project-local store/type/utility aliases, updateNode/canvasMode semantics, Frontier CSS variables, and a specific directory layout.
- `zustand-store-ts` — **verified, 16/20**. Exact package tree `8dc1658099b269c1e6347b7d0ffbe38d6f7058c1`, `SKILL.md` blob `fe9aca17683b17d3c86c78cb3473f52a10b38f3d`, template blob `3c40062ec21c5d1e875b3816516a706701a8bc03`; freshness revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. It is bounded local Zustand state-management guidance. Its async load example is a placeholder rather than an instruction to call an external service; portability remains medium because of project-path assumptions and an intentionally opinionated subscribeWithSelector rule.

All twenty-five TypeScript packages retain `validation_status: not-run`; no behavioral evidence was invented.

Microsoft Skills remains active with **57** gaps outside the completed direct-language slices. The next registered-pin source-ordered gap is `.github/plugins/azure-skills/skills/airunway-aks-setup`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills at the registered pin; all five direct language slices are now complete. Enter `.github/plugins/azure-skills/skills/airunway-aks-setup` next.
2. Complete remaining Microsoft Skills non-direct plugin families before moving to Microsoft Azure Skills.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.