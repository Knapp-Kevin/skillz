# Addy Osmani Agent Skills: ten-package pinned authority macro review

**Review date:** 2026-10-29  
**Source:** https://github.com/addyosmani/agent-skills  
**Registered pin:** `f63ec56a3cc936408d792956ae583c3c96a825bd`  
**License:** MIT, with upstream package/references retained intact  
**Eligible denominator:** 24 first-class `skills/<name>/SKILL.md` packages; 24/24 already have exact-version provenance and semantic review companions; 0 current-standard static gaps.  
**Selected high-authority tranche:** 10 existing packages; 2 dispositions corrected, 8 preserved. This is a **recheck**, not ten new admissions or new behavioral validation.

## Macro map and selection

The pinned source tree contains 24 first-class manifests. All are already covered at the exact pin; ordinary Markdown and the shared `references/` tree are bundled dependencies rather than new first-class packages. No aliases, duplicate exposure paths, or newly admitted skills were identified in this bounded review. The selected ten were `ci-cd-and-automation`, `git-workflow-and-versioning`, `deprecation-and-migration`, `shipping-and-launch`, `security-and-hardening`, `browser-testing-with-devtools`, `observability-and-instrumentation`, `performance-optimization`, `source-driven-development`, and `using-agent-skills`.

The high-risk cluster is not repository-owned automation: these are **intact upstream instructions** retained as reference. The risk arises when an external host treats them as permission to install tools, change persistent host configuration, interact with authenticated pages, emit telemetry, page humans, deploy or alter infrastructure. The shared source is strong on engineering checklists, measurements, evidence, privacy warnings, rollback thinking and explicit untrusted-content handling. However, useful safety advice does not automatically bind each external action to the user's specific approval.

## Corrected exact-version decisions

| Package | Exact pinned `SKILL.md` blob | Before | After | Authority hard fail |
|---|---|---|---|---|
| `observability-and-instrumentation` | `7d56593ec599cce0bae12aa46862884d0208cc59` | VERIFIED semantic only 18/20 | **REJECT unchanged 15/20** | Steps 3–5 introduce production telemetry, including payment identifiers and OpenTelemetry export, without explicit destination/field/retention/data-transfer authorization. Steps 6–7 create page/ticket alerts, temporarily lower thresholds and test-fire notification channels without separate approval for live policy changes and sends. |
| `browser-testing-with-devtools` | `9864d2724e273e1164d62ab10b73590ae00fd6a8` | VERIFIED semantic only 19/20 | **REJECT unchanged 14/20** | Lines 26–41 install/execute unpinned `npx -y chrome-devtools-mcp@latest` and persist host MCP configuration. The browser workflows can trigger actions including PATCH writes, while the confirmation gate in line 90 only covers JavaScript execution, not all browser interactions or authenticated accounts. |

Both retain individual exact-version provenance, fingerprints, controlled tags, dependencies, individual rubric and rationale, and `validation_status: not-run`. No new security scan, behavioral execution, or vulnerability exploit was observed. These are static instruction/authority findings.

**Safe extraction:** keep question-first telemetry, RED/USE and cardinality, structured allowlisted logs, trace design, alert runbooks, browser-profile isolation, untrusted DOM/network boundaries, credential restrictions, and visual/network/accessibility verification. An adapting host must obtain specific authorization for target project/account, tool installation and host configuration, telemetry export destination and retention, monitoring policy/recipient changes, and browser actions with real side effects. Prefer pinned reviewed tool versions and isolated test accounts.

## Eight reviewed, unchanged

- `ci-cd-and-automation`: REJECT unchanged 13/20; unapproved CI/deployment/rollback/branch-protection writes.
- `git-workflow-and-versioning`: REJECT unchanged 14/20; recovery/release operations and workflow prescriptions need host-specific authorization.
- `deprecation-and-migration`: REJECT unchanged 14/20; production traffic, data migrations and destructive lifecycle changes require explicit authority.
- `shipping-and-launch`: REJECT unchanged 12/20; operational rollout assumptions and unsafe generic rollback command.
- `security-and-hardening`: VERIFIED semantic only 18/20; explicit ask-first sensitive-change boundary, useful threat model and SSRF/supply-chain caveats.
- `performance-optimization`: VERIFIED semantic only 19/20; measure-first and revert discipline; deployment/database changes remain subject to host task authorization.
- `source-driven-development`: VERIFIED semantic only 19/20; exact-version official-source and untrusted-document safeguards.
- `using-agent-skills`: REJECT unchanged 13/20; source-specific compulsory routing is not portable governing policy.

The remaining 14 of the 24 pinned packages were not deeply re-reviewed in this tranche. Their existing records remain intact; **24/24 current-standard complete** describes static companion coverage, not a fresh 24-package security or behavioral pass.

## Systemic disposition and accounting

The two newly rejected packages demonstrate a recurring pattern: a procedure may correctly warn about privacy and still authorize too much by default. Testing a pager is a communication; lowering a live threshold is a security/operations policy mutation; installing `@latest` is a supply-chain and persistent host-configuration action; a browser click may be a money-bearing or data-changing operation. Technical capability, test intent, isolated profiles, and warnings are not action authorization.

**Tranche delta:** 10 existing reviewed / 2 VERIFIED → REJECT unchanged / 8 retained. Admitted-source denominator 24/24 → 24/24; static gaps 0 → 0; first-party inventory 44 unchanged; third-party review records 826 unchanged; total verification YAML 870 unchanged; registered source pins unchanged; package-security and behavioral acceptance unchanged. Discovery/source-vetting delta 0. Preserve the upstream gitlink and its reference/tooling files unchanged. This repository gains no runtime, scanner, CI, script, monitor, installer or automation.

**Next gate:** complete the externally blocked 36-final-package first-party SkillSpector v2.12.0 and adversarial acceptance frontier before merging #489/#492/#496. Continue disjoint pinned-source authority rechecks only where they yield consequential truthful corrections.
