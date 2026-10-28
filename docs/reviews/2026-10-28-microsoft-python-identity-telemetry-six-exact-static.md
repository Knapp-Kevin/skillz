# Microsoft Python identity and telemetry: six changed-existing exact-version static reviews

**2026-10-28.** Candidate `microsoft/skills` at `61fe0305ea70389ed8705eec6026a786f57865cf`; registered July `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. No cloud execution, scanner, behavioral validation, admission or pin change.

## Macro-first identity and denominator

The canonical candidate denominator remains **208** (106 exact-tree carry-forwards, 76 changed-existing, 26 new). All **26/26** new candidates have complete static reviews. Six genuine changed-existing Python packages advance **24/76 → 30/76**, leaving **46** (15 Python, 30 Azure operations, one skill-creator). The Python `azure-eventhub-py`, `azure-search-documents-py` and `azure-servicebus-py` manifests are exact carry-forwards, not new gaps. Each reviewed package contains one front-mattered SKILL.md and two supporting reference Markdown files. Six package trees and 18 source Git blob identities were inspected at the candidate revision. The supporting Markdown is not first-class skill content. The source root and manifests state MIT; external SDK/service terms were not separately audited.

## Individual dispositions

| Package | Score | State | Decisive defect |
|---|---:|---|---|
| `azure-identity-py` | 12/20 | REJECT unchanged | Wildcard additionally_allowed_tenants=['*'], direct token acquisition and OnBehalfOfCredential lack tenant, principal and scope approval. |
| `azure-keyvault-py` | 10/20 | REJECT unchanged | set_secret, key/certificate creation, deletion and irreversible purge lack owner/object/action authorization. |
| `azure-monitor-ingestion-py` | 10/20 | REJECT unchanged | logs.json upload and retry of failed logs lack dataset, destination, cost, retention and idempotency approval. |
| `azure-monitor-opentelemetry-exporter-py` | 10/20 | REJECT unchanged | Root logger handler and span processors export signals without approved signal/destination boundary; offline storage enabled by default. |
| `azure-monitor-opentelemetry-py` | 10/20 | REJECT unchanged | Broad automatic instrumentation starts without collection/recipient approval; documented default sampling_ratio is 1.0. |
| `azure-monitor-query-py` | 12/20 | REJECT unchanged | Workspace RBAC does not authorize arbitrary dataset, tenant, subject or disclosure; raw log rows and DataFrame heads are printed. |

## Systemic findings

- **Authority hard fail 6/6:** credentials and configured Azure destinations do not authorize cross-tenant token acquisition, vault mutations, private data disclosure, telemetry export or log reads.
- **Identity and secrets:** wildcard tenants and optional unencrypted token cache require approval/custody. Key Vault prints `secret.value` and offers irreversible purge without a separate permit. Example secret strings are placeholders, not proven leaked credentials.
- **Telemetry privacy:** Logs Ingestion uploads local JSON and retries records without explicit recipient/data consent; exporter attaches root logger and stores retries offline; distro auto-instruments web/database frameworks with documented default sampling 1.0.
- **Read-only is not privacy-safe:** Monitor Query prints raw workspace rows and DataFrame heads; RBAC does not authorize output disclosure.
- **Evidence:** repeated capability checklists and unpinned package installs do not establish behavioral results. Each skill has its own exact provenance, ten-dimension score, controlled tags, dependency and privacy characterization, and explicit security/behavioral `not-run`.
- **Value:** preserve credential-chain controls, Key Vault recovery/versioning, DCR batching, OTel filters/sampling and Kusto bounded queries for authorized adaptation. The nine-file `azure-cosmos-db-py` service layer deserves separate deep review.

All six are REJECT unchanged, retained as adaptation/extraction/checklist prior art. Third-party companions **774 → 780**; total verification YAML **818 → 824** (44 first-party). Registered July remains **186/186**; no repository-owned execution machinery introduced.
