# Microsoft Skills freshness review tranches (2026-10-10)

**Investigation and sequencing only.** References: [issue #400](https://github.com/Knapp-Kevin/skillz/issues/400), [registered canonical crosswalk](../registry/freshness/microsoft-skills-governed-crosswalk-2026-10-10.json), [tree frontier](microsoft-skills-tree-frontier-2026-10-10.md).

Exact base `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`, candidate `d5741a1e9325adead3a28d1d203bb69283907e06`.

## Current evidence

- 186/186 previously governed Microsoft package identities have confirmed canonical source paths.
- 106 exact entire-subtree carry-forwards; 76 changed existing packages; four removed canonical packages; 22 new raw manifest paths still requiring eligibility and overlap assessment.
- Package security backfill and unchanged-reuse admission remain separate, not proven by source pins or Microsoft identity.

## Macro-first review work

### A. Replacement/deprecation reconciliation (4)
- `azure-cost`: explicitly resolve deleted/moved/replaced vs retired; preserve historical evidence
- `azure-hosted-copilot-sdk`: explicitly resolve deleted/moved/replaced vs retired; preserve historical evidence
- `azure-rbac`: explicitly resolve deleted/moved/replaced vs retired; preserve historical evidence
- `azure-servicebus-rust`: explicitly resolve deleted/moved/replaced vs retired; preserve historical evidence

### B. Initial authority/privacy-sensitive review tranche (37, heuristic shortlist)

Selected by identifiers involving identity, Key Vault, credentials, deployment, storage, telemetry, cloud resource control, messaging, or related sensitive/side-effect surfaces. This is **prioritization only**; keyword matching is not a safety verdict. Independently assess all 76 changed packages.

- `appinsights-instrumentation`
- `azure-deploy`
- `azure-eventgrid-py`
- `azure-eventhub-rust`
- `azure-identity-py`
- `azure-identity-rust`
- `azure-keyvault-certificates-rust`
- `azure-keyvault-keys-rust`
- `azure-keyvault-py`
- `azure-keyvault-secrets-rust`
- `azure-kusto`
- `azure-messaging-webpubsubservice-py`
- `azure-messaging`
- `azure-mgmt-apicenter-py`
- `azure-mgmt-apimanagement-py`
- `azure-mgmt-botservice-py`
- `azure-mgmt-fabric-py`
- `azure-monitor-ingestion-py`
- `azure-monitor-opentelemetry-exporter-py`
- `azure-monitor-opentelemetry-py`
- `azure-monitor-query-py`
- `azure-quotas`
- `azure-resource-lookup`
- `azure-resource-visualizer`
- `azure-storage-blob-py`
- `azure-storage-blob-rust`
- `azure-storage-file-datalake-py`
- `azure-storage-file-share-py`
- `azure-storage-queue-py`
- `azure-storage-queue-rust`
- `azure-storage`
- `entra-agent-id`
- `microsoft-foundry-deploy-model-capacity`
- `microsoft-foundry-deploy-model-customize`
- `microsoft-foundry-deploy-model-preset`
- `microsoft-foundry-deploy-model`
- `python-appservice-deploy`

For each: verify complete changed package tree (including scripts/references), authorization boundary, secret/sensitive data minimization, telemetry/data egress, cost/production operations, exact license and dependencies; run exact-version pinned security scan and record `passed/findings-reviewed/failed/incomplete` separately from semantic disposition.

### C. Remaining changed existing packages (39)
- `agent-framework-azure-ai-py`
- `airunway-aks-setup`
- `azure-ai-contentsafety-py`
- `azure-ai-contentunderstanding-py`
- `azure-ai-language-conversations-py`
- `azure-ai-ml-py`
- `azure-ai-projects-py`
- `azure-ai-textanalytics-py`
- `azure-ai-transcription-py`
- `azure-ai-translation-document-py`
- `azure-ai-translation-text-py`
- `azure-ai-vision-imageanalysis-py`
- `azure-ai-voicelive-py`
- `azure-ai`
- `azure-aigateway`
- `azure-appconfiguration-py`
- `azure-cloud-migrate`
- `azure-compliance`
- `azure-compute`
- `azure-containerregistry-py`
- `azure-cosmos-db-py`
- `azure-cosmos-py`
- `azure-cosmos-rust`
- `azure-data-tables-py`
- `azure-diagnostics`
- `azure-enterprise-infra-planner`
- `azure-kubernetes-automatic-readiness`
- `azure-kubernetes`
- `azure-prepare`
- `azure-reliability`
- `azure-speech-to-text-rest-py`
- `azure-upgrade`
- `azure-validate`
- `fastapi-router-py`
- `m365-agents-py`
- `microsoft-foundry-finetuning`
- `microsoft-foundry`
- `pydantic-models-py`
- `skill-creator`

Full individual exact-version semantic decisions still required; do not batch-pass. Carry forward old context only when genuinely unchanged.

### D. Newly discovered raw manifests (22)
- `.github/plugins/aks-skills/skills/aks-gpu-inference`
- `.github/plugins/aks-skills/skills/aks-known-issues`
- `.github/plugins/aks-skills/skills/aks-network-capture`
- `.github/plugins/aks-skills/skills/aks-troubleshooting`
- `.github/plugins/aks-skills/skills/azure-search-nav`
- `.github/plugins/azure-cost/skills/cost-analysis`
- `.github/plugins/azure-cost/skills/cost-estimation`
- `.github/plugins/azure-cost/skills/cost-governance`
- `.github/plugins/azure-cost/skills/cost-optimization`
- `.github/plugins/azure-kusto-graph-skills/skills/azure-kusto-graph`
- `.github/plugins/azure-kusto-graph-skills/skills/azure-kusto-irql-graph`
- `.github/plugins/azure-kusto-graph-skills/skills/azure-kusto-irql`
- `.github/plugins/azure-local-skills/skills/azure-local-multi-rack`
- `.github/plugins/azure-local-skills/skills/azure-local`
- `.github/plugins/azure-skills/skills/azure-app-onboard-prereq`
- `.github/plugins/azure-skills/skills/azure-app-onboard`
- `.github/plugins/azure-skills/skills/azure-app-onboard/deploy`
- `.github/plugins/azure-skills/skills/azure-app-onboard/prepare`
- `.github/plugins/azure-skills/skills/azure-app-onboard/scaffold`
- `.github/plugins/azure-skills/skills/azure-kubernetes/azure-kubernetes-app-deploy`
- `.github/plugins/azure-skills/skills/discover-azure-skills`
- `.github/plugins/foundry-iq-skills/skills/foundry-iq`

Evaluate nested first-class package eligibility, alias exposure, source-owned tooling, ordinary reference Markdown and repository-internal files. A raw `SKILL.md` is not automatically new governed admission. Establish a decisive candidate denominator and individual dispositions before updating the registered source pin or catalog.

## Guardrails and completion

1. The 106 unchanged whole package trees can inherit *compatible prior exact-version semantic evidence* by matched identity; no new security pass or behavioral test is inferred.
2. For the other 80 historical entries (76 changed + 4 removed), record change/deprecation review and the decisions behind any retirement/replacement.
3. Each genuinely new eligible package gets source/license, provenance, actual package dependencies, authority/privacy assessment, structured semantic review, and applicable exact-version scanner state.
4. Review candidate safety and completeness before updating all five public accounting surfaces plus the pin and gitlink atomically.
5. Do not import source-owned install hooks, telemetry or synchronization into `skillz` runtime.

This plan is intentionally not approval to advance the source revision. It also does not claim that 22 raw additions all qualify.
