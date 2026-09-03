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
| **Persisted third-party review companions** | 307 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 135 / 189 |
| **Microsoft Skills current-standard gaps** | 54 |
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
- Microsoft Skills: exact denominator **189**, **135/189 companion-complete**, **54 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **25/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The registered-pin TypeScript tree contains exactly **25** first-class packages. Its upstream plugin README says 24 because it omits `applicationinsights-web-ts`, which nevertheless exists as a separate first-class package at the same pin. Tree truth controls the denominator.

Current companion-complete TypeScript packages are:

1. `applicationinsights-web-ts` — rejected unchanged, 16/20.
2. `azure-ai-contentsafety-ts` — rejected unchanged, 11/20.
3. `azure-ai-document-intelligence-ts` — rejected unchanged, 11/20.
4. `azure-ai-projects-ts` — rejected unchanged, 6/20.
5. `azure-ai-translation-ts` — rejected unchanged, 10/20.
6. `azure-ai-voicelive-ts` — rejected unchanged, 6/20.
7. `azure-appconfiguration-ts` — rejected unchanged, 7/20.
8. `azure-cosmos-ts` — rejected unchanged, 9/20.
9. `azure-eventhub-ts` — rejected unchanged, 8/20.
10. `azure-identity-ts` — rejected unchanged, 6/20.
11. `azure-keyvault-keys-ts` — rejected unchanged, 5/20.
12. `azure-keyvault-secrets-ts` — rejected unchanged, 5/20.
13. `azure-microsoft-playwright-testing-ts` — rejected unchanged, 10/20.
14. `azure-monitor-opentelemetry-ts` — rejected unchanged, 9/20.
15. `azure-postgres-ts` — rejected unchanged, 10/20.
16. `azure-search-documents-ts` — rejected unchanged, 9/20.
17. `azure-servicebus-ts` — rejected unchanged, 8/20.
18. `azure-storage-blob-ts` — rejected unchanged, 6/20.
19. `azure-storage-file-share-ts` — rejected unchanged, 6/20.
20. `azure-storage-queue-ts` — rejected unchanged, 6/20.
21. `azure-web-pubsub-ts` — rejected unchanged, 6/20.
22. `frontend-ui-dark-ts` — verified, 15/20.
23. `m365-agents-ts` — rejected unchanged, 13/20.
24. `react-flow-node-ts` — verified, 15/20.
25. `zustand-store-ts` — verified, 16/20.

`frontend-ui-dark-ts` is bound to package tree `1f15eeae63b8e03b5c10f6dbfa550095079b2409` and `SKILL.md` blob `4ff865e3c1cc60d8e5999cf950a016d7c9f019d2`. Its complete package also contains three Markdown references, four Segoe UI TTF assets, and two Foundry logo PNG assets. Skill-specific freshness is anchored to Microsoft revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. The package provides a coherent local React/Vite/Tailwind dark-UI system with theme/design tokens, reusable components, responsive shells, mobile touch-target guidance, routing, and Framer Motion patterns. Its authority is bounded to local code generation and package installation rather than consequential external-state operation. Recorded limitations include reviewed-generation stack assumptions, accessibility hardening needed for some copied patterns such as dialog focus management and reduced-motion behavior, and medium portability for bundled Segoe UI/font/logo assets whose applicable upstream terms must remain attached. Behavioral validation is `not-run`.

`m365-agents-ts` is bound to single-file package tree `0bcb6ef9c55c8f8bae331e85d40f8585844c4bc7` and `SKILL.md` blob `00169cce10c70508375fc9300513a7600c7f75f8`. Skill-specific freshness is anchored to Microsoft revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. It preserves useful AgentApplication routing, Express hosting, streaming lifecycle, sensitivity labels, invoke handling, Copilot Studio integration, API-freshness checks, and secret-hygiene advice. Unchanged adoption is rejected because ordinary user messaging, generated-content streaming, invoke acknowledgement, remote Copilot conversations/questions, WebChat sessions, Azure OpenAI/Copilot data transfer, and tenant/client secret or bearer-token use lack mandatory tenant/environment, audience, message/data-owner/classification, identity/access, model-data-transfer, production, per-action communication, and credential-custody authorization. Behavioral validation is `not-run`.

`react-flow-node-ts` is bound to package tree `ba384d63f352c5518b3dd77168e5c49af2220e8a`, `SKILL.md` blob `ab4e1a6a5a4c1bf03f4d9b49dee6285e9ce0457d`, and template blobs `8539c7b0fd5b453c9564a675b3e2fcaedeaf1c34` and `46c9e2ee44ff517693d611ad2e94388cff669adc`. Skill-specific freshness is anchored to Microsoft revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. It is verified as bounded local React Flow node-generation guidance. Portability is medium because it assumes project-local store/type/utility aliases, `updateNode`/`canvasMode` semantics, Frontier CSS variables, and a source-specific directory layout. Behavioral validation is `not-run`.

`zustand-store-ts` is bound to package tree `8dc1658099b269c1e6347b7d0ffbe38d6f7058c1`, `SKILL.md` blob `fe9aca17683b17d3c86c78cb3473f52a10b38f3d`, and template blob `3c40062ec21c5d1e875b3816516a706701a8bc03`. Skill-specific freshness is anchored to Microsoft revision `e1f9cce11758d305e6c77683fe34ccc394586291` from 2026-04-20. It is verified as bounded local Zustand state-management guidance. Its async `loadItems` body is a placeholder rather than an instruction to call an external service; portability remains medium because of project-path assumptions and an intentionally opinionated `subscribeWithSelector` rule. Behavioral validation is `not-run`.

The direct TypeScript slice is now **25/25 current-standard companion-complete**. Twenty-two packages are rejected unchanged and three are verified; all twenty-five retain `validation_status: not-run` unless representative external behavioral/adversarial evidence is actually recorded.

The non-direct Microsoft plugin frontier is now active. `airunway-aks-setup` is bound to package tree `72ec58c0a7c574dc71e14c63feb3d2aa529849ac`, `SKILL.md` blob `26bbd92815116826696fb6380d37446a285496b9`, and a complete reference tree containing GPU/model sizing, PowerShell notes, troubleshooting/rollback, and six staged step files. Skill-specific freshness is anchored to Microsoft revision `951d18d43210f0d93a931ae5d5c2a774f63d5faf` from 2026-04-21. It is **rejected unchanged, 15/20**. The package is unusually strong about positive-action safety: it reports active cluster context, stops on missing prerequisites, requires confirmation before install/deployment actions, warns about GPU cost, confirms model choice, and keeps Hugging Face token input out of conversational context and shell history. The hard fail is narrower but decisive: rollback instructs deletion of ModelDeployment resources and token secrets plus provider/controller undeploy without requiring a fresh destructive-action authorization boundary. Those rollback operations materially change persistent Kubernetes/AKS state and credential material, so unchanged promotion is blocked while the package remains valuable adaptation/reference evidence. Behavioral validation is `not-run`.

`appinsights-instrumentation` is bound to package tree `8f6b0c9b5af9ab5bbd69d25d58071c9034221eb0` and `SKILL.md` blob `ca55c310862cb95b5ebcc1f10a070f312718d1cb`, with the complete package including `LICENSE.txt`, `examples/appinsights.bicep`, `scripts/appinsights.ps1`, five platform/reference guides, and four SDK quick references. Skill-specific freshness is anchored to Microsoft revision `2d821920c717bcdd5ee4e287a41205c07e43cb0a` from 2026-05-05. It is **rejected unchanged, 12/20**. The package retains useful Application Insights/OpenTelemetry selection, SDK initialization, resource topology, tracing, secret-reference, and KQL mechanics. Unchanged adoption fails because it directly instructs creation of Log Analytics and Application Insights resources, App Service/Container App/Function App configuration mutation, application and IaC changes, telemetry export, and deployment-affecting operations without mandatory target/resource, production-change, cost, telemetry-data/disclosure, or deployment authorization. Its Container Apps reference also retrieves a Log Analytics primary shared key into a shell variable and performs secret/configuration mutation without a credential-custody authorization boundary. Behavioral validation is `not-run`.

`azure-ai` is bound to package tree `8a168336305c56e0eea0d89aced7d8a0001de3b5` and `SKILL.md` blob `6cce5b319f57f98f81772e4c8627c573d89e8571`, with bundled `references/auth-best-practices.md` and 15 SDK quick references. Skill-specific freshness is anchored to Microsoft revision `951d18d43210f0d93a931ae5d5c2a774f63d5faf` from 2026-04-21. It is **rejected unchanged, 10/20**. The package is useful as a router/reference across Search, Speech, OpenAI, Document Intelligence, Vision, Translation, Transcription, and Content Safety, and its authentication reference has strong managed-identity and least-privilege guidance. Unchanged adoption fails because bundled references instruct persistent search-index/document mutation and external processing of audio, documents, text, images, and other potentially sensitive content without mandatory data-owner/classification, disclosure/model-transfer, target-resource, mutation, production, retention, cost, or credential-custody authorization. Behavioral validation is `not-run`.

Microsoft Skills remains active with **54** gaps outside the completed direct-language slices. Continue registered-pin source order with `.github/plugins/azure-skills/skills/azure-aigateway` while preserving the complete `.NET`, Java, Python, Rust, and TypeScript slices.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches; all five direct language slices are complete. The next registered-pin gap is `.github/plugins/azure-skills/skills/azure-aigateway`.
2. Complete remaining Microsoft Skills non-direct plugin families.
3. Complete Microsoft Azure Skills.
4. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
5. Continue governed discovery/source-vetting and omission recovery.
6. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.