# Pinned Awesome Copilot AWS/Azure eight: complete-package static source vetting (2026-11-02)

**Scope:** `github/awesome-copilot` pinned at `f11a4e441c5ff061b4f8ae37952be8c602e4034e`. Source family has 432 raw `SKILL.md` paths (415 direct-shape, 17 other-shape). Eight genuine previously unreviewed direct-shape package trees, 15 source-owned files (eight `SKILL.md`, seven required references) were read at the exact pin and reconciled against manifest blobs/trees. Root MIT LICENSE blob `89bc5e962c9944cdb050887062afdaaf89be504a`; external cloud tools and dependencies retain independent terms.

[Individual 10-dimension scores, blobs, trees, dependency/authority/rights findings and terminal decisions](../../registry/discovery/github-awesome-copilot-aws-azure-eight-complete-static-20261102.json). This is **candidate source-vetting**, not governed verification or unchanged-use approval.

| Exact package | Static grade | Source-vetting disposition | Decisive boundary |
|---|---:|---|---|
| aws-cdk-python-setup | 11/20 | REJECT unchanged | Global install, credentials, bootstrap and deployment without separate authorization |
| aws-cloudwatch-investigation | 13/20 | REFERENCE-ONLY | Production logs, CloudTrail identities and request parameters read without approved scope |
| aws-cost-optimize | 11/20 | REJECT unchanged | Issue-write approval does not authorize AWS cost/inventory reads |
| aws-resource-health-diagnose | 11/20 | REJECT unchanged | Sensitive telemetry and remediation examples lack execute/propose boundary |
| aws-well-architected-review | 11/20 | REJECT unchanged | Cloud/security inventory access unscoped before issue-write approval |
| az-cost-optimize | 11/20 | REJECT unchanged | Azure subscription enumeration and private cost data lack read authority |
| azure-container-registry-cli | 12/20 | REJECT unchanged | Credential, RBAC, purge, task, network and resource mutation commands unbounded |
| azure-deployment-preflight | 12/20 | REJECT unchanged | Cloud what-if and report writes unscoped; pass cannot authorize deployment |

## Macro findings

1. **Authorization is the systemic hard fail.** All eight assume that host tools or cloud credentials imply permission. An explicit GitHub issue-creation confirmation in the cost workflows is useful but insufficient for preceding private cloud reads. Even nominally read-only queries require bounded account, resource, time and data scope.
2. **Sensitive data and money-bearing side effects cluster.** CloudWatch logs/CloudTrail can disclose identity and request payloads; ACR examples expose credential-bearing commands, create persistent cloud tasks, purge images, change RBAC and network access; CDK bootstraps and deploys billable infrastructure.
3. **Useful reusable methods remain.** Incident blast-radius reasoning, cost-evidence comparison, architecture pillar review, ACR least-privilege roles and Bicep what-if categorization are valuable reference methods. None is licensed to execute or approved unchanged by this record.
4. **Technical caveats.** Hardcoded AWS concurrency 1000, some cloud metric math, Azure CLI/version assumptions and the preflight template's claim that passing checks means safe deployment need independent verification.
5. **No double counting.** Source-vetting grades do not create governed semantic pairs, scanner results, behavioral validation or a deduplicated eligible population.

## Accounting and continuation

Awesome Copilot exact-path terminal decisions: **87/432 → 95/432**; direct-shape **70/415 → 78/415**, other-shape **17/17** unchanged; raw path leads without terminal decisions **345 → 337**. Four-source path-matched decisions **166/4,813 → 174/4,813**. Governed exact-version review population remains **1,039**. Distinct eligible denominator remains **unknown** pending package and mirror reconciliation.

The next disjoint source-family tranche should target unreviewed, structurally first-class Awesome Copilot packages with meaningful capability differentiation, checking overlap with the 995 governed third-party records before assigning any unchanged-use status. No security scan or behavioral execution was performed. The repository remains passive.
