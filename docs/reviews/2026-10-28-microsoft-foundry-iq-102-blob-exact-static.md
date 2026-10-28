# Microsoft Foundry IQ: exact-version 102-blob static review

**Date:** 2026-10-28. **Disposition:** REJECT unchanged (15/20) because the distributed plugin enables session/tool telemetry and reporter installation by default without a distinct informed opt-in. Preserve EXTRACT / ADAPT / CHECKLIST value. **Review type:** complete exact-source static semantic, dependency, authority and privacy inspection; package-security scanner **not-run**; representative external behavioral/adversarial validation **not-run**. No upstream helper, hook, Azure command, model, installer or telemetry binary was executed.

## Identity and package closure

- Source: [microsoft/skills](https://github.com/microsoft/skills) candidate `61fe0305ea70389ed8705eec6026a786f57865cf`. Registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` remains unchanged; no source admission or vendoring.
- Canonical first-class manifest: `.github/plugins/foundry-iq-skills/skills/foundry-iq/SKILL.md`, blob `d81ed5fc5840955acae9d14f022828a580621327`, frontmatter `name: foundry-iq`, version `0.2.1`, MIT. Last manifest change in this source at `2eb9ecea0f823d3967ffa3800794a200086d5c9e` (2026-10-14 11:05:43 UTC); this does not establish every dependency's freshness.
- Exact skill tree `c45f2a12dcffa1929705b1523cb1645a03de134e`: **85/85** source blobs, **1,276,121 bytes**, consisting of 1 SKILL.md, 5 agent procedures, 55 helper files, 2 KB guides, 2 source guides, 1 cleanup guide, 17 references, 1 Search guide, 1 troubleshooting guide. Includes 40 Python helpers and optional `pypdf==6.16.1` / `defusedxml==0.7.1` assessment requirements.
- Plugin distribution tree `d6d3a76b22e461c34ecf9c902e04745159038af5`: **102/102** blobs, **1,367,855 bytes**, including all 85 skill blobs and **17/17** plugin-level manifest, license, changelog, README, hook and telemetry-installer blobs. Plugin LICENSE blob `356b112bcc4f07e03b6e57569eedf9d79978d2d5` is MIT. These source-owned scripts/hooks remain upstream evidence, never `skillz`-owned execution machinery.
- External dependencies: Azure AI Search, Azure Blob/ADLS, Azure CLI/SDK/REST, Azure identities/RBAC, Foundry agents/models, Python 3.12+, selected parsers, network access and optional plugin host. None was installed or exercised.

## Positive systemic findings

The 85-file skill is unusually rigorous about routing by actual user intent; separating resource selection from approval; fingerprinted immutable plans; fresh scoped readback; no inferred ownership; explicit approval for billable provisioning, file ingestion, model queries, identity grants and deletion; separate destructive cleanup; no silent retries after ambiguous writes; pagination/ETag bounds; secrets redaction; and no claims of success from an HTTP acknowledgement alone. File and Blob content boundaries require explicit scope; document inspection is separately authorized; retrieval audits do not fabricate grounding. These mechanisms have strong adaptation value.

Examples: `SKILL.md` lines 12–16, 22–29 and 59–61; `knowledge-bases/retrieve.md` lines 20–25 and 60–64; `knowledge-sources/create-file.md` lines 11–30; `lifecycle/cleanup.md` lines 24–55; `agents/create-missing-agent.md` lines 23–25 and 58–81. Helper scripts were inspected statically, not executed. The policy's `approval.confirmed` field is a concrete plan gate in context, not automatic permission.

## Decisive unchanged-use privacy/authority failure

1. **Telemetry is opt-out, not consent-first.** `hooks/claude-hooks.json` (`47c9976d66a6b1b16c3d203d43acf9671eda1fa5`), `hooks/copilot-hooks.json` (`bac46f27aa874e2b8e53dbaba07da3e3ad8f1dcb`) and `hooks/cursor-hooks.json` (`b0da804111d720860891e0e217f04cdf3f19d436`) invoke `track-telemetry` at session start and after tool use (Cursor also after MCP execution). The hook skips only when `AZURE_MCP_COLLECT_TELEMETRY=false`; the README describes setting this opt-out. No separate user authorization is required before collecting and publishing session/skill/tool/reference-file metadata. This crosses the privacy-sensitive telemetry boundary even though the core skill's Azure write approvals are substantially better.
2. **The hook installs and runs a native reporter as a side effect of ordinary events.** `hooks/scripts/track-telemetry.sh` (`1e47853e26494f07ea58b44a1d515862a1f1dbad`, lines 537–582) and PowerShell equivalent (`7f010ec7c2dfbeb705d488758831134a54a5a8f5`, lines 559–631) call their installers, then execute `ghcfa-telem` with plugin/client/version, timestamp, event, session ID, skill/tool name and relative reference path. The installer downloads a pinned release and checks SHA-256 in the normal network path. Pinning reduces supply-chain risk but does not authorize a download, installation or telemetry transmission.
3. **Optional raw-input logging can retain sensitive material.** If `AZURE_SKILLS_TELEMETRY_LOG_DIR` is configured, the Bash hook (lines 163–175) and PowerShell hook (lines 150–163) persist raw hook JSON, which can include tool input. The default telemetry reporter arguments do **not** demonstrate transmission of raw prompts or credentials; the risk is metadata transmission and optional unredacted local logging, not a claimed observed secret exfiltration.
4. **Local reporter ZIP override lacks the normal archive digest gate.** `hooks/scripts/install-telemetry.sh` (`80316e11104a8fb05d871cfdc1842cb7a3f3e758`, lines 345–374) and `install-telemetry.ps1` (`d647f3aa497ca8a2c79669c58767805387879fef`, lines 193–222) copy an `AZURE_SKILLS_TELEMETRY_ZIP_PATH` override without the release SHA-256 comparison used in the download branch. This requires an explicitly configured local override; it is a conditional integrity weakness, not proof of exploitation. Cached reporter binaries also return without rehashing.

## Rubric and disposition

| Dimension | /2 |
|---|---:|
| Trigger precision | 2 |
| Procedural clarity | 2 |
| Authority and safety | 0 |
| Failure handling | 2 |
| Evidence discipline | 2 |
| Dependency coherence | 1 |
| Portability honesty | 1 |
| Differentiated usefulness | 2 |
| Adversarial resilience | 1 |
| Effectiveness design | 2 |
| **Total** | **15/20** |

**REJECT unchanged** despite the passing numerical score: the authority hard fail is independent of the rubric threshold. Preserve consented document-assessment contracts, scoped readback, receipt-backed cleanup, source/KB/agent separation and exact-plan approval as EXTRACT/ADAPT/CHECKLIST prior art. For unchanged eligibility, require a genuine pre-telemetry opt-in and authorization for native reporter installation, bounded retention and debug logging, plus complete exact-package security evidence and independent acceptance. Disabling the hook in a user-specific adaptation changes the package and does not inherit this exact-version review.

**Limitations:** All 85 skill files and 17 plugin-level files were fetched by exact Git blob identity, risk-screened and high-consequence paths read deeply. This was not a full Python program verification, supply-chain binary audit, security scan, Azure deployment, or observed host behavioral test. The candidate is reference evidence only, not an admitted/pin-advanced version.

## Macro and lifecycle

Microsoft latest structural denominator **208** = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned. New-candidate exact static review **25/26 → 26/26** (4 semantic VERIFIED only / 22 REJECT unchanged). Remaining **76 changed-existing** full current-version requalifications; 76/76 screening is not that review. Four removed paths have candidate-only retirement decisions. Registered July remains **186/186** at unchanged pin. Third-party companions **749 → 750**; first-party **44** unchanged. No candidate security scan, behavioral validation, source admission, repository-owned runtime, CI or scheduler. Issue #400 remains open; #402 and #415 and draft PRs #412/#413/#416 retain separate blockers.
