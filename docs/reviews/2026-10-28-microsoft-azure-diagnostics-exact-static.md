# Microsoft Azure Diagnostics: complete exact-version static review

**2026-10-28.** Candidate `microsoft/skills@61fe0305ea70389ed8705eec6026a786f57865cf`, registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. Full `azure-diagnostics` package tree `17d064bfbddf07fc8882ecc864b99994921936e2`, manifest blob `35a21659518211925117404cdd9622aa2eb91380`. **54/54 files, 54 distinct Git blobs, 229,051 bytes** read at the exact candidate revision, including the root, service references, 12 upstream-owned Bash/PowerShell scripts and AKS/VM/messaging troubleshooting material. Static review only: no Azure access, script execution, security scan or behavioral validation.

## Macro map and accounting

Candidate structural denominator **208 = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned**. The new candidate tranche remains **26/26**. Changed-existing **71/76 → 72/76**, Azure operations **24/30 → 25/30**; remaining **4** genuine gaps: `azure-kubernetes` parent, `azure-prepare`, `azure-upgrade`, and `microsoft-foundry` root. Existing separately reviewed AKS/Foundry children are not counted again. The `auth-best-practices.md` content also appears in other source packages; shared reference exposure is not a new skill.

## Individual decision

| Package | Tree | Files | Score | Disposition |
|---|---|---:|---:|---|
| `azure-diagnostics` | `17d064bfbddf07fc8882ecc864b99994921936e2` | 54 | **12/20** | **REJECT unchanged; extract/adapt/checklist/reference** |

The root provides systematic symptom/resource-health/log/metric/recent-change triage and an explicit **evidence-only** mode when live access is forbidden. AKS routing includes read-only baseline commands and says not to restart, delete, cordon, drain, scale, upgrade or reconfigure without an explicit remediation request. The VM parent has extension preflight checks. These are genuine strengths, but they do not consistently authorize the following separate operations:

- **Production mutation:** `references/app-service/README.md` suggests plan scale-up, failed-request tracing, auto-heal recycling, redeployment, app-setting changes, TLS upload/binding and domain repair as fixes. `references/container-apps/README.md` changes registry identity and minimum replicas. Neither establishes a distinct target, cost, availability and rollback approval for each effect.
- **Destructive lifecycle / identity:** `references/functions/durable.md` presents `func durable purge-history` (and warns that an unscoped purge can remove active instances). VM troubleshooting references include password/key reset via `az vm user update`, `az vm repair reset-nic --yes`, firewall/NLA changes, VM repair creation and boot diagnostics changes. Preflight health checks are not action authorization.
- **Privileged diagnostics and privacy:** `scripts/run-ig.sh` and `.ps1` use `kubectl debug --profile=sysadmin` to create a privileged node debug pod, including packet capture, process and DNS traces. Comments call for explicit approval, but the script does not enforce it; scope, traffic privacy, retention and data-owner consent remain external. AKS guidance can select a sole cluster and establish credentials after discovery, which changes local kubeconfig without a separate context-mutation checkpoint.
- **Credentials and sensitive output:** `references/functions/README.md` projects App Insights `instrumentationKey` and `connectionString`, and lists Function App settings. VM repair examples accept passwords as CLI arguments. Log streams, telemetry, network captures and messaging debug output may contain secrets/PII and require scoped collection, minimization, redaction and retention.
- **Messaging state:** Event Hubs SDK references recommend disabling checkpoint storage soft delete/versioning for performance without a separate storage-owner and recovery/retention approval.

## Shared findings and preserved value

**Authorization fragmentation** persists across service-specific subguides even when the root offers evidence-only analysis. Read-only health-first triage, KQL/ARG query patterns, symptom-specific escalation, scoped AKS baseline collection, pod evidence, connectivity probes and SDK failure taxonomies are useful adaptation material. Source-owned scripts remain intact upstream reference evidence, not `skillz` runtime. The review does not assert a vulnerability was exploited, that any live command was run, or that behavioral effectiveness was established.

Two candidate-version provenance/verification companions record each exact blob, the 10-dimension rubric, tags, dependency/authority/privacy findings and explicit package-security/behavioral `not-run`. Third-party records **821 → 822**, total verification YAML **865 → 866** (44 first-party + 822 third-party). No candidate admission or source-pin movement. Draft PRs #412/#413/#416 retain independent external-security/acceptance blockers; issue #400 remains open for the four remaining packages and source-pin decision.
