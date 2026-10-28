# Microsoft Python service and management: eight changed-existing exact-version static reviews

**2026-10-28.** Candidate `microsoft/skills` at `61fe0305ea70389ed8705eec6026a786f57865cf`; registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` unchanged. **Static-only** external-host inspection; no cloud action, source installation, package-security scan, behavioral validation, source-pin advancement or admission.

## Macro-first frontier and identity

The canonical structural denominator remains **208**: 106 exact-tree carry-forwards, 76 changed-existing and 26 new/previously ungoverned. All **26/26 new** candidates are fully statically reviewed. This tranche comprises **eight genuine changed-existing** canonical Python packages: `30/76 → 38/76` fully reviewed, **38** remaining (**7 Python, 30 Azure operations, 1 skill-creator**). Three other Python direct-package manifests (`azure-eventhub-py`, `azure-search-documents-py`, `azure-servicebus-py`) are exact-tree carry-forwards, not additional gaps. Ordinary reference Markdown and Python templates are bundled dependency evidence, not extra first-class skills.

The eight source trees contain **29 distinct exact Git blobs** (190176 bytes of upstream tree-reported content). One package is a deep **nine-file** Cosmos service-layer package; six routine management/messaging packages contain three files each; `m365-agents-py` has two. Every source file was fetched and inspected; source trees, individual file blob identities, and prior July companions were reconciled. Source root and manifests state MIT; external SDK/service terms were not separately audited.

## Individual decisions

| Package | Exact tree | Files | Score | Disposition | Decisive defect |
|---|---|---:|---:|---|---|
| `azure-cosmos-db-py` | `1a03b83a1054d4183c58bd828db8c7997f1c38eb` | 9 | 10/20 | REJECT unchanged | Service CRUD accepts workspace_id/author_id without establishing caller authority; cross-partition queries, upsert and delete are executable without per-action authorization. Cross-partition move inserts then deletes without approved ownership/compensation. |
| `azure-containerregistry-py` | `26cbed5d43ce55fad7487f71421fb9c12f59d7b7` | 3 | 11/20 | REJECT unchanged | delete_repository, delete_manifest, delete_tag and age-based untagged-manifest cleanup can remove deployable images without registry owner approval, retention hold or rollback. |
| `azure-messaging-webpubsubservice-py` | `3d4959574cec66dc53330d47e557bf225e250e13` | 3 | 10/20 | REJECT unchanged | Token issuance, send_to_all/user/group, grant/revoke permission, group membership and close_all_connections lack recipient, tenant, audience, scope and user-communication approval. |
| `azure-mgmt-apicenter-py` | `7a985c0369d797b3aead2e8bcb3e1a15f623c1c0` | 3 | 12/20 | REJECT unchanged | Create/update service, APIs, versions, imported specifications, environments, deployments and classification schemas without owner, subscription, audience or change approval. |
| `azure-mgmt-apimanagement-py` | `e7cf59c979b611b71a2b84ce83da54edbf68fe7c` | 3 | 10/20 | REJECT unchanged | Service provisioning, API imports, published products, subscription issuance, gateway policy changes, named-value secrets, backends and user creation lack change-owner approval. |
| `azure-mgmt-botservice-py` | `cc3364a8c4e688481e68dc7b567fd95ef52259e8` | 3 | 10/20 | REJECT unchanged | Bot create/update/delete, channel creation and OAuth connection changes lack resource owner, channel recipient and identity-scope approval. |
| `azure-mgmt-fabric-py` | `26c5eecd68541a029caa2896af3df606d3a77de2` | 3 | 11/20 | REJECT unchanged | Create, resize, suspend, resume and delete operations materially affect billing and production service without cost ceiling, owner approval, dependency inventory or rollback. |
| `m365-agents-py` | `7d30932e571b05101cc0060eb2adab2195f7aec8` | 2 | 11/20 | REJECT unchanged | Message handlers send user text back into channels, Graph profile calls and Copilot Studio conversations without explicit per-recipient, tenant, scope and communication authorization. |

Every package has its own candidate-version provenance and verification companions, ten-dimension static rubric, controlled tags, source identity, exact file inventory, trigger/non-trigger boundary, dependencies, authority/privacy finding, rationale, and explicit security/behavioral `not-run`. The older registered-pin companions remain intact and do not transfer their identity or validation.

## Deep Cosmos findings

- **Tenant and destructive authority:** `assets/service_template.py` accepts `workspace_id` and `author_id` and performs read/upsert/delete without a caller-authorization contract. `references/partitioning.md` offers cross-partition queries and an insert-then-delete workspace move without a full cross-partition compensation or ownership boundary. A partition key is a data-routing value, not authorization.
- **Query construction:** `assets/cosmos_client_template.py` appends the `extra_filter` string directly to SQL. Its bundled call sites use literal parameterized filters, so this is a **potential injection sink if a future caller passes untrusted SQL fragments**, not a demonstrated exploit.
- **TLS and secrets:** `_is_emulator_endpoint` checks for substrings `localhost` or `127.0.0.1` and disables TLS certificate verification for the resulting endpoint; it does not enforce an exact loopback host and trusted emulator environment. Exception strings and tracebacks may reveal request context. The example emulator key is explicitly documented as public emulator-only material, not evidence of a leaked production secret.
- **Correctness and operational safety:** Singleton initialization and retry/error guidance need explicit client shutdown and recovery design; test fixtures can delete documents in a configured integration container without independent environment/data authorization. Source-owned Python templates remain reference material only.

## Systemic synthesis

1. **Authority hard fail, 8/8:** authenticated SDK clients and resource identifiers are not consent for database mutation, artifact deletion, broadcasts, production gateway policy, identity/channel changes, money-bearing Fabric capacity operations or user messaging.
2. **Privacy and secret custody:** Web PubSub's hero example prints a bearer-token connection URL, contradicting its non-hero guidance to avoid logging it; APIM prints a subscription primary key; Bot Service prints Direct Line keys in a hero example while the reference warns against logging them. These are output-disclosure defects even when underlying example credentials are placeholders.
3. **Cost and destructive lifecycle:** Fabric creation/resizing/suspension/deletion, ACR image cleanup and APIM gateway changes require action-scoped permits, budget/retention constraints, blast-radius review and rollback/compensation.
4. **Evidence quality:** source checklists, SDK snippets and upstream tests are not executed acceptance evidence. No package-security or behavioral state was promoted. All eight retain useful differentiated methods for ADAPT, EXTRACT and CHECKLIST, not unchanged adoption.
5. **Next frontier:** seven changed Python packages remain (agent framework, Azure AI ML/projects/voice, speech-to-text, FastAPI router, Pydantic models), followed by 30 Azure operations and one skill-creator. This tranche does not change source priority or justify July pin movement.

**Accounting:** third-party verification companions **780 → 788**, total verification YAML **824 → 832** (44 first-party + 788 third-party); candidate changed-existing **30/76 → 38/76**; remaining **46 → 38**. Registered Microsoft July **186/186**, candidate denominator **208**, first-party **44**, sources **22**, admitted-source delta **0**. No repository-owned runtime, scanner, workflow, generator or scheduler introduced.
