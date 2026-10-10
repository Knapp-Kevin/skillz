# Microsoft Skills freshness: exact raw-tree frontier (2026-10-10)

**Status: reconnaissance only. No pin advancement, admission, quality promotion, or public-count mutation.** Supports [issue #400](https://github.com/Knapp-Kevin/skillz/issues/400).

## Exact snapshots
- Source: [microsoft/skills](https://github.com/microsoft/skills).
- Currently registered: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` (July 2).
- Latest upstream main observed October 10: `d5741a1e9325adead3a28d1d203bb69283907e06` (October 9 commit).
- Both recursive trees resolved fully (`truncated=false`). Each manifest-bearing directory is compared using its complete Git tree SHA, not only its SKILL.md blob.
- [Machine-readable per-package evidence](../registry/freshness/microsoft-skills-tree-frontier-2026-10-10.json) records the complete paths, tree hashes and manifest blob hashes from both snapshots.

## Raw, not governed, denominator
| Partition | Manifest-bearing directories |
| --- | ---: |
| At registered revision | 192 |
| At candidate revision | 210 |
| Exact identical package trees | 111 |
| Existing paths with changed subtree | 77 |
| Added manifest paths | 22 |
| Removed manifest paths | 4 |

**Do not replace the existing governed Microsoft 186/186 count with the raw 192/210 counts.** The governed identity set has 186 companion pairs and may exclude editorial/internal manifests, collapse aliases, or explicitly account for first-class nested packages. The classification above is an exact raw-tree *frontier*, not a curation denominator.

## New manifest paths (22)
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
- `.github/plugins/azure-kusto-graph-skills/skills/azure-kusto-irql`
- `.github/plugins/azure-kusto-graph-skills/skills/azure-kusto-irql-graph`
- `.github/plugins/azure-local-skills/skills/azure-local`
- `.github/plugins/azure-local-skills/skills/azure-local-multi-rack`
- `.github/plugins/azure-skills/skills/azure-app-onboard`
- `.github/plugins/azure-skills/skills/azure-app-onboard-prereq`
- `.github/plugins/azure-skills/skills/azure-app-onboard/deploy`
- `.github/plugins/azure-skills/skills/azure-app-onboard/prepare`
- `.github/plugins/azure-skills/skills/azure-app-onboard/scaffold`
- `.github/plugins/azure-skills/skills/azure-kubernetes/azure-kubernetes-app-deploy`
- `.github/plugins/azure-skills/skills/discover-azure-skills`
- `.github/plugins/foundry-iq-skills/skills/foundry-iq`

## Removed manifest paths (4)
- `.github/plugins/azure-sdk-rust/skills/azure-servicebus-rust`
- `.github/plugins/azure-skills/skills/azure-cost`
- `.github/plugins/azure-skills/skills/azure-hosted-copilot-sdk`
- `.github/plugins/azure-skills/skills/azure-rbac`

## Decisions and remaining gates
1. Join each existing `registry/skills/microsoft-skills/*.yaml` record by its **canonical `source_path`**, not by filename, against the registered and candidate tree records. Preserve separately reviewed nested package identities.
2. Label any extra root/editorial manifest as not-in-governed-denominator **with a reason**, and reconcile moves, renames, replacements or deprecations of removed packages. No silent count changes.
3. For genuine previously governed packages in `unchanged`, recover matching exact subtree evidence without rerunning static review. For `changed` or new eligible packages, prioritize authority/privacy-sensitive Azure deploy, identity, Key Vault, cost, Kusto, monitoring, resource control, storage, and messaging instructions. Do not infer safety from Microsoft's branding.
4. Run pinned package-security scanning on compatible changed/new packages and retain reports with exact identity and coverage. Security and behavioral validation do not inherit semantic results.
5. Only after the complete eligible candidate denominator has decisive provenance, verification, security and disposition: update the pinned gitlink, `registry/sources.yaml`, `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md` and `index.json` atomically. Otherwise leave current pinned corpus and historical 721 reviews untouched.

This evidence file supports subsequent reconciliation and is not an approval to execute any source-owned tooling, deployment, sync, telemetry, or other external mutation.


## Governed canonical-path reconciliation (186 of 186 confirmed)

The original **192** manifest-bearing directories at the registered pin include **186** canonical individually governed entries and **six** additional manifests that are not their own governed package identity. The registry's `source_path` for **all 186** existing companions was read and matched to the exact July source tree, allowing for `source_path` values that identify the package directory rather than a `SKILL.md` path.

The seven non-unique/nested identifiers were explicitly resolved using canonical provenance: `applicationinsights-web-ts`, `entra-agent-id`, and five `microsoft-foundry-*` nested entries. The other 179 source paths were checked directly against their unique old source packages. See [full governed crosswalk](../registry/freshness/microsoft-skills-governed-crosswalk-2026-10-10.json).

| Governed exact-tree partition | Count |
|---|---:|
| Canonical current entries | **186** |
| Unchanged entire package subtree | **106** |
| Changed entire package subtree, same canonical path | **76** |
| Removed canonical package subtree | **4** |
| Raw new candidate manifest paths requiring eligibility review | **22** |

The **six** historical raw manifests outside the governed 186 are `.github/plugins/azure-sdk-typescript/skills/applicationinsights-web-ts`, `.github/plugins/azure-skills/skills/entra-app-registration`, `.github/plugins/microsoft-365-agents-toolkit/skills/teams-app-developer/slack-to-teams`, `.github/skills/continual-learning`, `.github/skills/debugview`, and `.github/skills/entra-agent-id`. Their existence as nested/alias/editorial or additional upstream surfaces does not license automatic exclusion forever; each retains an explicitly visible, ungoverned status.

**This completes the existing 186 canonical identity join only.** The candidate eligible denominator still needs judgment on 22 raw additions, four removals/renames, overlap and nested first-class classification. The 76 changed packages need individual semantic/security/authority disposition, while 106 unchanged package trees can reuse genuinely compatible exact-version semantic evidence without being re-reviewed ceremonially. No source pin, public review count or unchanged-use security claim has changed.
