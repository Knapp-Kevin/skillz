# Awesome Copilot cross-domain nine-package candidate review (2026-11-02)

**Source:** github/awesome-copilot at `f11a4e441c5ff061b4f8ae37952be8c602e4034e`; root GitHub MIT license blob `89bc5e962c9944cdb050887062afdaaf89be504a`. [Individual exact-package grades](../../registry/discovery/github-awesome-copilot-nine-breadth-static-20261102.json). Nine pinned trees, **10/10 package-owned files inspected**, including Azure role selector's package-local Microsoft MIT license. No execution, installation, security scan or behavioral validation.

| Skill | Static score | Candidate disposition | Decisive limitation |
|---|---:|---|---|
| ai-ready | 6/20 | REJECT | Unpinned external skill install; review only first 20 lines |
| arch-linux-triage | 8/20 | REJECT | Copy-paste pacman/service remediation without action approval |
| aspnet-minimal-api-openapi | 10/20 | REFERENCE-ONLY | Code edits and deployment need explicit target and write authorization |
| boost-prompt | 7/20 | REJECT | Unconditional clipboard write and project exploration |
| centos-linux-triage | 8/20 | REJECT | Remediation commands without firewall/SELinux/package mutation gate |
| comment-code-generate-a-tutorial | 7/20 | REJECT | Automatically refactors Python and overwrites README without approval |
| conventional-commit | 6/20 | REJECT | Explicit automatic git add and git commit without confirmation |
| azure-role-selector | 10/20 | REFERENCE-ONLY | Role assignments require separate tenant/principal/scope approval; generation alone is not assignment authority |
| acreadiness-policy | 9/20 | REJECT | Unpinned npx -y github:microsoft/agentrc; policy/CI writes not authorized |

## Macro synthesis

The Arch/CentOS support pair is a near-duplicate thin diagnostic template; it does not separate read-only diagnosis from authorized package/service changes. Conventional-commit explicitly bypasses commit confirmation, and the Python tutorial wrapper changes code and README without scoped authorization. Prompt improvement assumes an authorized clipboard write; AI-ready directs an unpinned skill installation; AgentRC policy applies unpinned `npx -y` and potentially modifies CI. ASP.NET typed endpoint patterns and Azure least-privilege role drafting are useful **reference-only** approaches, not deployment or assignment approval. The latter has its own Microsoft MIT notice. Numeric scores never override hard-fail authority gates.

## Flow accounting

Awesome Copilot exact-path candidate decisions **78 → 87/432** (**70/415 direct**, **17/17 nested**, **345 direct pending**); four-source exact-path decisions **119 → 128/4,813 raw paths**. The next unreviewed direct cursor stays `skills/acquire-codebase-knowledge/SKILL.md` because this tranche was deliberately non-contiguous. Distinct eligible denominator **unknown**. **2 REFERENCE-ONLY / 7 REJECT unchanged**; zero admissions, governed verification pairs, scans and behavioral tests. Governed population **1,039**, registered sources **25**, admitted-source denominator delta **0**. Existing draft PRs remain separately owned and blocked by their documented pre-merge gates.
