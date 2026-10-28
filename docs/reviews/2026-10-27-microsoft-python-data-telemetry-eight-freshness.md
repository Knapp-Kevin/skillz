# Microsoft Skills: Python data, identity, telemetry, queue and four removed paths

**Observed:** 2026-10-27. **Registered source:** `microsoft/skills@32cad4ee689c95c309e61aeefcbc6af356f1e6a7`. **Latest upstream candidate:** `1a63e5f771987a9a13e9f0571823dc1e80741583` (upstream main at inspection). **Registered skillz main:** `f8807dd4aebe78108ba988f99caaf9b4f689f07c`.

This is a **bounded static candidate screen**, not new governed verification, package-security clearance, behavioral validation, or permission to advance the registered source pin. The companion JSON in [`registry/freshness/microsoft-skills-python-data-telemetry-eight-2026-10-27.json`](../../registry/freshness/microsoft-skills-python-data-telemetry-eight-2026-10-27.json) binds each candidate to its manifest Git blob, complete source package-tree Git identity, exact revision, individual controlled tags, 10-factor rubric, authority finding, dependencies, and `not-run` evidence states. All eight have frontmattered first-class identities; none duplicates an earlier screened canonical path.

## Macro-first frontier and accounting

The frozen October 10 **governed** crosswalk has 186 registered identities: **106 unchanged, 76 changed, four removed**. The prior 56/76 changed-existing screens plus this eight-package tranche yield **64/76 screened, 12 remaining**. The 22 frozen raw additions are separately **22/22 classified**, including 19 frontmattered candidates and three nested non-first-class references. Four candidate-absent governed paths are classified below, without claiming their replacements are equivalent. The latest upstream Git tree has **212 physical `SKILL.md` paths**, which is *not* a proven eligible denominator. Registered July corpus remains **186/186 current-standard**, with 721 persisted third-party verification companions and zero admission delta.

All eight candidate manifests were read at the exact upstream revision. All package files were enumerated by Git tree identity, and decisive supporting references/templates were inspected. The inspection is **not a complete semantic review of every bundled file**. No code, scanner, SDK, cloud operation, or behavioral test was executed.

## Individual dispositions

| Candidate | Static score | Decision and decisive evidence |
|---|---:|---|
| `azure-appconfiguration-py` | 12/20 | **REJECT unchanged**. Examples print configuration values and perform feature-flag, read-only, setting-delete and snapshot changes without action-specific production approval. |
| `azure-cosmos-db-py` | 13/20 | **REJECT unchanged**. Bundled `references/partitioning.md` interpolates `extra_filter` into SQL query text, permits missing-partition-key cross-partition queries, and illustrates a cross-workspace move by upsert then delete without a distinct owner check. This is a source-level pattern risk, not a demonstrated exploit. |
| `azure-cosmos-py` | 12/20 | **REJECT unchanged**. Cross-partition `SELECT *`, `read_all_items()`, item deletion and provisioned-throughput updates have no tenant-disclosure, destructive-action or spending approval boundary. |
| `azure-identity-py` | 12/20 | **REJECT unchanged**. `allow_unencrypted_storage=True` cache fallback and `additionally_allowed_tenants=["<other-tenant>", "*"]` are demonstrated without a specific security/tenant authorization decision. DEBUG auth logging also requires secret-aware redaction. The placeholder `<secret>` is not evidence of a live leaked credential. |
| `azure-monitor-ingestion-py` | 11/20 | **REJECT unchanged**. Arbitrary `logs.json` can be uploaded to a configured DCR with no sensitive-data classification/consent boundary. The example `ignore_errors` callback silently discards failure visibility. |
| `azure-monitor-opentelemetry-exporter-py` | 12/20 | **REJECT unchanged**. Root logger attachment can transmit unredacted logs; default-enabled offline retry storage can persist sensitive telemetry locally without retention/access decisions. |
| `azure-monitor-opentelemetry-py` | 12/20 | **REJECT unchanged**. Auto-instrumentation of HTTP and databases, exception-bearing log export and optional live metrics need approved signal classes, destination, minimization and consent. The source does show selective disable controls, but these are not authorization. |
| `azure-storage-queue-py` | 12/20 | **REJECT unchanged**. Queue deletion, `clear_messages()`, persistent sends and printing peeked/received payloads lack scoped destructive-action and disclosure approval. |

Each is retained as **ADAPT / EXTRACT / REFERENCE** prior art, not silently discarded. Positive patterns include credential-chain restriction, context-managed clients, Cosmos parameterization and tests, queue visibility/poison-message handling, and OpenTelemetry sampling and lifecycle control. These do not erase hard-fail findings.

## Four candidate-absent governed identities

The latest upstream tree has no canonical manifest at the registered paths below. This resolves **presence/absence classification**, not successor identity, replacement suitability, or July-pin retirement.

| Registered canonical ID | Candidate finding | Follow-up |
|---|---|---|
| `azure-cost` | Original Azure Skills manifest absent; four new Azure Cost plugin skills exist | Separate analysis/estimation/governance/optimization scope; no automatic 1:1 migration |
| `azure-hosted-copilot-sdk` | Original hosted Azure workflow manifest absent; `.github/skills/copilot-sdk` exists | SDK authoring and Azure-hosted deployment scope may differ |
| `azure-rbac` | Original RBAC role guidance manifest absent | Entra identity skills are not proven equivalents of least-privilege role assignment |
| `azure-servicebus-rust` | Original Rust Service Bus manifest absent; no same-language replacement established | Retain historical source evidence and upstream production-maturity warning |

**Macro findings:** (1) SDK credentials prove technical access, not authority to mutate, export or reveal data. (2) Configuration values, queue messages, identity caches and telemetry all need explicit sensitive-data controls. (3) Cosmos DB partition design and authorization are distinct; an optional SQL string fragment is a separate injection hazard. (4) OpenTelemetry distro and exporter are differentiated but overlap substantially, so the host should choose by user fit rather than count both as mandatory. (5) Removed paths must not be mechanically retired or mapped to successors at the registered July revision.

## Governance and next gate

- **No source pin advancement.** Registered source remains `186/186` complete at its own revision; the candidate remains unqualified.
- **No security or behavioral claims.** Pinned external SkillSpector and representative external adversarial testing are not available as qualifying evidence in this pass.
- **No new repo-owned runtime.** All upstream code and templates remain source-owned reference evidence.
- **Issue #400 remains open** until the last 12 changed-existing candidates, exact current eligible denominator, successor decisions, applicable package-security qualification and final pin/accounting decision are completed.
- PRs #412, #413 and #416 remain separate blocked first-party work; this tranche does not race their modified files.

**Next executable priority:** Screen the remaining 12 distinct changed-existing canonical packages and resolve the latest eligible denominator from the exact upstream tree. Do not turn physical manifest counts or upstream rename guesses into admission counts.
