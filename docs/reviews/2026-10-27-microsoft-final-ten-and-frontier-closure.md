# Microsoft Skills: final ten changed-existing screenings

**Date:** 2026-10-27. **Registered pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`. **Candidate revision:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Method:** exact Git tree + ten manifests + selected decisive package references; static-only, no execution.

## Macro reconciliation

Registered July remains **186/186** current-standard at its own pin. Frozen governed crosswalk is **106 exact-tree carry-forward / 76 changed-existing / four removed**. Six earlier duplicate review exposures were corrected before this pass. This tranche screened the **ten remaining distinct IDs**, advancing **66/76 → 76/76** frozen changed-existing candidates. This does **not** complete source refresh, security, admission or behavioral qualification.

The upstream candidate tree has **212 physical `SKILL.md` paths**, not an established canonical eligible denominator. Three nested Azure App Onboard phase files lack first-class frontmatter. Six July physical manifests were not in the governed 186, including two name collisions: the `.github/skills/applicationinsights-web-ts` and Azure SDK TypeScript plugin paths have identical complete four-blob package trees, while `.github/skills/entra-agent-id` and the Azure plugin path have different manifests and four- versus seven-blob trees. Neither should be counted twice without canonical routing. See the [exact duplicate-exposure crosswalk](../../registry/freshness/microsoft-skills-duplicate-exposure-crosswalk-2026-10-27.json) for tree and manifest fingerprints. The `azure-kubernetes` parent tree includes separately first-class nested AKS skills, so physical exposure is not a new package by itself. Four removed paths still need successor/retirement decisions. The latest upstream also changes plugin-owned telemetry hooks and previously screened `azure-diagnostics`/`azure-prepare`; these ten package trees themselves are unchanged from `1a63e5f7`.

## Individual exact-version candidate findings

| ID | Manifest blob | Score | Candidate disposition | Decisive observation |
|---|---|---:|---|---|
| `airunway-aks-setup` | `b073a851e1f9` | 14/20 | REFERENCE_ONLY_PENDING_FULL_PACKAGE | Per-step installation confirmation and GPU cost awareness exist, but no scoped cluster/namespace/image digest/budget authorization. |
| `azure-cloud-migrate` | `8daa1b9e40e4` | 14/20 | REFERENCE_ONLY_PENDING_FULL_PACKAGE | Global rules require ask_user before subscription/region selection, deployment, destructive operations and source overwrites; not all 31 blobs were checked. |
| `azure-kubernetes-automatic-readiness` | `c5618c53ef11` | 17/20 | REFERENCE_ONLY_PENDING_FULL_PACKAGE | Strong read-only cluster rule and explicit approval before YAML edits; cluster-connected reads still require approved target scope; constraint spec not fully qualifi |
| `azure-kubernetes` | `34a04d801024` | 11/20 | REJECT_UNCHANGED_EXTRACT | Manifest and CLI reference include cluster creation and add-on changes without action-specific subscription/resource/budget approval; requirements collection is not  |
| `entra-agent-id` | `ec3318657c97` | 12/20 | REJECT_UNCHANGED_EXTRACT | Examples POST identities, grant User.Read.All and AllPrincipals delegated User.Read/Tasks.ReadWrite/Mail.Send with ten-year expiry without owner-approved role/scope/ |
| `fastapi-router-py` | `be9b22a94a16` | 13/20 | REJECT_UNCHANGED_EXTRACT | PATCH ownership check is commented out and DELETE lacks owner check; GET/list use optional auth without tenant scoping. Authentication is not object authorization. |
| `m365-agents-py` | `3d583a89a369` | 14/20 | REFERENCE_ONLY_PENDING_OPERATIONAL_AUTHORITY | Samples build message handlers and send activities, but do not establish operational tenant/channel owner approval for a live deployment. |
| `pydantic-models-py` | `15bd46d5df97` | 19/20 | REFERENCE_ONLY_STATIC_REVIEWED | Local model generation has no direct external side effect; workspace/author identifiers in schema are not an access-control boundary. |
| `python-appservice-deploy` | `ca5cc00ee360` | 10/20 | REJECT_UNCHANGED_EXTRACT | create-app.md says do not ask for confirmation and proceed with defaults before creating RG, paid P0v3 plan, web app and deploying. --track-status false proves ZIP a |
| `skill-creator` | `6429efa08396` | 14/20 | REFERENCE_ONLY_PENDING_FULL_PACKAGE | Skill guides local creation, packaging and optional eval commands without a scoped host target/execution authorization; upstream scripts are reference evidence, not  |

**Four REJECT unchanged:** `azure-kubernetes` has no action-specific billable cluster/network approval; `entra-agent-id` shows Graph `User.Read.All` and `AllPrincipals` delegated scopes including `Mail.Send` with ten-year expiry without distinct authorization; `fastapi-router-py` comments out PATCH ownership and omits DELETE ownership while allowing unscoped optional-auth reads; `python-appservice-deploy` explicitly skips confirmation before creating a paid P0v3 plan and deploying. ZIP acceptance with `--track-status false` is not runtime readiness.

**Six REFERENCE ONLY:** `airunway-aks-setup` has per-step confirmation but lacks full target/image/cost binding; `azure-cloud-migrate` has real `ask_user` gates yet 31-blob scenario coverage is incomplete; `azure-kubernetes-automatic-readiness` offers sanitized read-only assessment and approved YAML diffs but needs constraint-spec/sanitizer qualification; `m365-agents-py` needs tenant/channel and sensitive-chat send authority before deployment; `pydantic-models-py` has all three blobs statically inspected but schema fields are not access control; `skill-creator` is a large source-owned script/evaluation package without host execution authority.

**Systemic findings:** Separate conceptual advice from actual cloud operations; authentication and tool availability are not authorization. Protect Hugging Face tokens, Entra credentials, Kubernetes context, private Teams chat and cross-cloud code. Preserve useful patterns from rejected packages for governed adaptation. Upstream scripts and hooks remain source-owned reference material, not `skillz` runtime.

The [individual structured ledger](../../registry/freshness/microsoft-skills-final-ten-2026-10-27.json) records each exact source/package/manifest identity, license, dependency, tags, rubric, authority/privacy rationale, supporting blob fingerprints, disposition and explicit security/behavioral `not-run`. Some large packages were selectively inspected and **not** declared fully verified.

## Repository flow and next gate

No new `registry/verification` companion, source pin, source admission or security/behavioral result. Public counts remain **44 first-party / 22 sources / 12 pinned corpora / 721 third-party reviews**. All five public accounting surfaces report the frozen screening result together.

**Next:** establish latest canonical eligible denominator and alias/successor mapping, then qualify changed/new packages with complete exact-version semantic and external security evidence before any pin advancement. PR #416 separately requires pinned SkillSpector evidence and independent acceptance for 21 changed first-party packages.
