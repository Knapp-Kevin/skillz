# Microsoft Azure AI, gateway, AKS, App Service and reliability: five exact-version reviews

**2026-10-28.** Exact candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`; July registered `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Static host review only, no Azure operation, security scan, behavioral test, admission or source-pin advancement.

## Macro map

208 structural candidate packages = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned. Before this tranche, 53/76 changed-existing had complete current-version reviews. Five genuine gaps share AI cloud-service, API gateway, inference and PaaS deployment/reliability authority. **63 complete upstream package blobs (238198 Git-tree-reported bytes)** were inspected, including bundled references and upstream-owned scripts. Root exposure aliases are not independent packages. High-authority, credential and production-state risks justified a smaller-than-usual tranche.

| Package | Exact package tree | Blobs | Score | Static disposition |
|---|---|---:|---:|---|
| `azure-ai` | `34c27c0761f1a2f730d45ddc1f395c6036723754` | 16 | 11/20 | REJECT unchanged |
| `azure-aigateway` | `8529348e07a31f48a46f0345a34fcaae9b27e7d0` | 9 | 10/20 | REJECT unchanged |
| `airunway-aks-setup` | `f1188c99d276aada84992b4e60387f2ad5814dd8` | 12 | 12/20 | REJECT unchanged |
| `python-appservice-deploy` | `3003f4d14f1e1a63ec94afd28f958560aab4b273` | 13 | 9/20 | REJECT unchanged |
| `azure-reliability` | `9330ac7bb6e8dbe5748219ac467ed066d8baa476` | 13 | 13/20 | REJECT unchanged |

## Individual findings and retained value

### azure-ai

**Decisive authority/privacy finding:** Private search documents, audio, images and transcripts may be transmitted to Azure AI without data-owner consent or retention/disclosure scope; bundled SDK references also mutate search indexes.

**Preserve for adaptation:** Cross-SDK routing, managed identity, bounded search, confidence thresholds and SDK patterns.

### azure-aigateway

**Decisive authority/privacy finding:** APIM subscription keys are retrieved; backend creation, API import, RBAC role grants, traffic policies and safety-threshold changes lack scoped approval. Prompt caching and token telemetry lack privacy isolation.

**Preserve for adaptation:** Managed identity, policy order, rate limits and cost controls as approval-gated design prior art.

### airunway-aks-setup

**Decisive authority/privacy finding:** Install confirmations exist, but skip-to-step assumes prior state; rollback deletes shared cluster resources without separate approval. Hugging Face tokens are written to plaintext TEMP files before Kubernetes secret creation.

**Preserve for adaptation:** GPU compatibility, VRAM sizing, provider selection and staged status checks.

### python-appservice-deploy

**Decisive authority/privacy finding:** Creates billable P0v3 plan and resource group in derived default subscription and deploys code; explicitly says not to ask for confirmation. Quiet post-deploy stop forbids independent startup acceptance; wildcard Django ALLOWED_HOSTS guidance.

**Preserve for adaptation:** Framework detection, safe runtime quoting, bounded retries and warm-up caveats.

### azure-reliability

**Decisive authority/privacy finding:** Useful staged deployment confirmations do not prevent bundled storage assessment from querying AzureWebJobsStorage app-setting .value, which may reveal a credential-bearing connection string. Storage migration and multi-region traffic changes require scoped authorization.

**Preserve for adaptation:** Four-feature reliability matrix, staged consent, compute-before-storage sequencing and IaC/CLI options.

## Systemic synthesis

- Azure credentials and tools are not action authorization. APIM RBAC/policy mutation, billable P0v3 creation, AKS deployment, storage migration and production traffic changes need scoped consent. A chance to say 'stop' after the host has decided to provision is not consent.
- Secret handling is a hard fail in three distinct paths: APIM subscription-key retrieval, Hugging Face token plaintext TEMP-file handling, and the `AzureWebJobsStorage` app-setting `.value` query in reliability assessment. Preserve read-only metadata methods without raw secrets.
- AI Search, transcription, OCR, image analysis and translation can disclose private content externally. Gateway semantic caching/telemetry adds tenant-isolation and retention concerns.
- Partial safeguards are not full safety: AI Runway and Reliability contain useful confirmation checkpoints but also bypasses, rollback/deletion exposure or sensitive read-side leaks. Adapt the positive mechanisms, reject unchanged operational authority.
- Remaining Azure operations packages are increasingly dependency-heavy. Separate `azure-prepare`, `azure-diagnostics`, `azure-kubernetes`, `azure-upgrade` and `microsoft-foundry` for deep inspection. No taxonomy drift detected in this tranche.

## Flow and evidence

Five complete static reviews, five provenance and five verification companions, 63 exact blobs, **5 REJECT unchanged**. Changed-existing **53/76 → 58/76**, remaining **23 → 18** (17 Azure operations and one skill-creator). Third-party verification **803 → 808**; total YAML **847 → 852** (44 first-party + 808 third-party). New candidate frontier **26/26** unchanged, denominator **208**, July **186/186** unchanged. Security scans **0**, behavioral validations **0**, cloud actions **0**, source admissions **0**. Public accounting reconciled atomically.
