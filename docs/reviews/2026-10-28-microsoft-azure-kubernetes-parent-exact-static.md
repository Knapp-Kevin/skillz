# Microsoft Azure Kubernetes parent: complete exact-version static review

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`; registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Parent tree `563d312d0625f6c6f815abc147a10375b8ec8ff9`, root manifest blob `34a04d8010249f24147c0ce66982c8cfa7eedc87`, upstream v1.2.4. The non-truncated tree contains **55 blob exposures (238,467 bytes)**. **Seven direct parent-owned files were read at the candidate revision**; 42 nested app-deploy and 6 nested Automatic-readiness files have compatible, separately persisted exact-tree reviews. The latter 48 were not newly re-read. No Azure access, script execution, scanner or behavioral validation.

## Macro frontier

Candidate structural denominator **208 = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned**. New candidates **26/26** complete; changed-existing **72/76 → 73/76**, Azure operations **25/30 → 26/30**. Three gaps remain: `azure-prepare` (166 blobs), `azure-upgrade` (50 blobs), and `microsoft-foundry` root (220 parent/nested/shared blob exposures). Nested app-deploy tree `580e5d0cffde99b0b4e571721570f282d5930d9a` (42, REJECT unchanged) and Automatic-readiness tree `c8ffe7bbfd195951701a5514cbdad6263c817e7a` (6, VERIFIED semantic only) are independently counted; no double admission.

## Individual decision

| Package | Score | Decision |
|---|---:|---|
| `azure-kubernetes` parent | **12/20** | **REJECT unchanged; extract/adapt/checklist/reference** |

The root offers useful Day-0/Day-1 decisions, AKS Automatic/Standard choice, CNI/egress, Entra/Key Vault/Policy guidance, zones, PDBs and monitoring. Six direct references cover metrics-aware rightsizing, autoscaler profiles, Spot eviction, VPA, CLI and optional skill routing. Unchanged adoption fails:

- **Persistent/billable cluster and security effects:** `references/cli-reference.md` gives `az aks create`, `az aks enable-addons`, and `az aks get-credentials` without a mandatory target/tenant/cost/production/security approval. Configuration questions are not authorization.
- **Node pool and availability:** `references/azure-aks-autoscaler.md` updates autoscaling and profiles before its aggressive-tuning confirmation. `references/azure-aks-spot.md` provisions interruptible Spot pools and updates existing pools without separate owner/eviction/cost approval.
- **VPA and local context:** `references/azure-aks-vpa.md` calls `az aks update --enable-vpa` and `kubectl apply` even for recommendation-only mode; its warning about Auto mode does not authorize those earlier effects. `az aks get-credentials` can mutate kubeconfig.
- **Sensitive reads:** Subscription discovery and all-namespace pod/metrics inspection lack a mandatory resource/data-owner scope and minimization boundary. The root correctly forbids printing secrets, but workload topology and private telemetry still require authority.
- **Independent nested gates:** App-deploy remains REJECT unchanged; Automatic-readiness has genuine read-only sanitization and local-write approval, but VERIFIED semantic-only is not a parent approval or package-security pass.

**Macro finding:** approval fragmentation recurs across parent, references and nested procedures. Preserve the differentiated architecture matrix, metrics freshness distinctions, conservative cost/eviction guidance and optional installation consent for adaptation. Upstream templates and scripts remain source-owned reference evidence, never `skillz` runtime.

One candidate provenance/verification pair advances third-party records **822 → 823**, total YAML **866 → 867** (44 first-party + 823 third-party). No source admission, July pin change, security evidence or behavioral validation.
