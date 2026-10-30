# AWS DevSecOps final five exact-version static reviews (2026-10-30)

## Pin, denominator and macro frontier

Registered AWS Agent Toolkit gitlink: `skills/sources/aws-agent-toolkit` → `aws/agent-toolkit-for-aws@ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`, Apache-2.0 (root LICENSE and plugin manifest). No upstream source, package or pin is changed. The pinned recursive tree has **115** front-mattered SKILL.md exposure paths, **93** distinct skill names, and **94** distinct package-tree identities. Duplicate mirrors collapse by exact package-tree SHA; the divergent `aws-cdk` plugin exposure remains distinct. This tranche covers five genuine missing records, not duplicate paths.

The 13 first-class `plugins/aws-agents-for-devsecops/skills/` packages are now **13/13 current-standard statically reviewed**: eight in [the preceding tranche](2026-10-30-aws-pinned-plugin-denominator-and-eight-static.md) and these five. All 13 are REJECT unchanged under the strict action-authorization rule; this is not a finding that their designs lack useful components. AWS family progress: **80/94 → 85/94**, gaps **14 → 9**. Remaining exact gaps: **seven** `plugins/aws-agents/skills/` AgentCore identities, **one** `signing-in-to-aws`, and **one** materially divergent `plugins/aws-core/skills/aws-cdk` variant.

## Five exact-pin decisions

| Skill | Package tree | SKILL.md blob | Score | Disposition |
|---|---|---|---:|---|
| `investigating-incidents-with-aws-devops-agent` | `46093040d5302e6a586fceeab7279d0ea5b35b04` | `ea0a40bf690019426992e3288cd93b8e56579d83` | 13/20 | REJECT unchanged |
| `setup-devops-agent` | `4b3d53ccc19d5664f349a2f5c1e53aec35e26c90` | `afea862a61c3ae081253cc566220e55398fb4cda` | 15/20 | REJECT unchanged |
| `setup-security-agent` | `0b27efd53c0ca29a3d8882147a402dbcb6db4993` | `187ac78daedc92d028530a16fa0f8e77b687a380` | 11/20 | REJECT unchanged |
| `setup` | `f60a821d6b1e8fd380cc68526199a2be314f71f2` | `f855a5727278411904e4ba6a835691ef77069fef` | 12/20 | REJECT unchanged |
| `threat-modeling-with-aws-security-agent` | `a6783b1f796bdf737b096ee6230053eaac819d55` | `07b7681c61fb6eb00aa20a68606c116b6697464f` | 12/20 | REJECT unchanged |

### investigating-incidents-with-aws-devops-agent

**Use/non-use boundary:** Deep asynchronous incident/root-cause analysis; not a generic cost or architecture chat.

**Dependencies:** AWS DevOps Agent remote MCP or aws-mcp/AWS CLI fallback, AgentSpace routing, Git, local incident logs and IaC, bundled REFERENCE.md, remote journal/recommendation APIs.

**Authority and decision:** The default pre-flight packs full stack traces, local Git history and IaC into a remote managed investigation title without bounded private-data disclosure approval. It starts persistent remote investigations and may incur cost without a separate authorization boundary. Bundled REFERENCE.md additionally offers mitigation task state changes only after approval, which does not cure the earlier unauthorized disclosure and job creation. Preserve pagination, status reporting and no-auto-execute recommendations for ADAPT/CHECKLIST.

**Review state:** exact-version structured static semantic review only; `validation_status: not-run`, no full package-security scanner report and no behavioral/adversarial execution evidence.

### setup-devops-agent

**Use/non-use boundary:** Configure a missing or broken AWS DevOps Agent MCP connection; not routine use of an already healthy connection.

**Dependencies:** Claude MCP configuration, DEVOPS_AGENT_TOKEN or AWS SigV4 credentials, curl, uvx mcp-proxy-for-aws@latest, AWS CLI, remote AWS DevOps Agent MCP.

**Authority and decision:** The procedure usefully asks for an auth-mode choice and confirms the main MCP config write, but SigV4 verification executes unpinned uvx mcp-proxy-for-aws@latest before separate installation authority, reads account identity, and later lists private AgentSpaces and writes a routing guide without a separate scoped private-read and durable-file authorization. Token guidance keeps values in environment variables rather than asking for chat disclosure, but project-scoped config and remote tool scope still need host governance. Reject unchanged; retain choice and connectivity checks for adaptation.

**Review state:** exact-version structured static semantic review only; `validation_status: not-run`, no full package-security scanner report and no behavioral/adversarial execution evidence.

### setup-security-agent

**Use/non-use boundary:** Set up or inspect AWS Security Agent resources; not permission to create or overwrite production IAM, storage or retention policy.

**Dependencies:** AWS Security Agent APIs, AWS CLI, IAM roles/trust/inline policies, S3 bucket and lifecycle, local .security-agent config/scans, AWS credentials.

**Authority and decision:** Even an 'is security agent configured' read-only trigger can create an AgentSpace, IAM role/policy and S3 bucket. The workflow unconditionally reapplies IAM inline policy, public access block and a whole-bucket 30-day lifecycle without distinct account, resource, cost, access-control and destructive-retention authorization. Reuse selection and confused-deputy protection are positives but do not authorize these writes. Reject unchanged; extract least-privilege checklist and explicit pre-write gate.

**Review state:** exact-version structured static semantic review only; `validation_status: not-run`, no full package-security scanner report and no behavioral/adversarial execution evidence.

### setup

**Use/non-use boundary:** Orchestrate setup of one or both AWS agents; not a safe general-purpose 'connect' command absent scoped authorization.

**Dependencies:** Delegates to setup-devops-agent and setup-security-agent, Claude plugin/MCP host, AWS account credentials and mutable cloud resources.

**Authority and decision:** This thin dispatcher invokes both setup workflows by default on broad 'set up/configure/connect' triggers. Its DevOps child has unapproved unpinned installation and private-read steps; its Security child can create or overwrite IAM, S3 lifecycle and persistent AgentSpace resources. The 'only one if needed' branch is useful, but there is no independent action-specific authority boundary before delegation. Reject unchanged; retain dependency routing as CHECKLIST/COMPOSE input.

**Review state:** exact-version structured static semantic review only; `validation_status: not-run`, no full package-security scanner report and no behavioral/adversarial execution evidence.

### threat-modeling-with-aws-security-agent

**Use/non-use boundary:** STRIDE review of requirements/design documents; not a license to upload an entire private repository or create paid persistent AWS jobs.

**Dependencies:** AWS Security Agent threat-model APIs, AWS CLI, S3, IAM service role, local zip/openssl/md5sum, .security-agent state and report files, setup-security-agent fallback.

**Authority and decision:** A request to review a spec immediately triggers a full-workspace archive, S3 uploads of source and specs, persistent threat-model/job creation, polling and report writes. The archive excludes common directories but not arbitrary secrets or sensitive documents. Missing setup silently delegates to resource-provisioning setup. There is no independent approval of exact source disclosure, account/bucket, retention, cost or workspace writes. Reject unchanged; retain STRIDE categorization and findings format for ADAPT/CHECKLIST.

**Review state:** exact-version structured static semantic review only; `validation_status: not-run`, no full package-security scanner report and no behavioral/adversarial execution evidence.


## Cross-package synthesis

- **Shared authority defect:** broad user intent such as "investigate", "set up", or "review a design" expands into persistent cloud jobs, account-wide reads, local configuration writes, IAM/security controls, S3 object retention, or third-party disclosure without separate, scoped authorization. Input confirmation, available credentials and safety-oriented settings are not permission.
- **Private information and secrets:** the incident title can include logs, stack traces, Git history and IaC. Threat-model uploads package whole workspaces; directory exclusions are not a guarantee against embedded secrets. DevOps setup uses environment-token references rather than soliciting token values into chat, but live connectivity probes and private AgentSpace enumeration still need scoped authority.
- **Dependency cascade:** `setup` delegates to both setup skills; `threat-modeling-with-aws-security-agent` can invoke setup-security-agent implicitly. A caller's narrow task cannot inherit unlimited provisioning authority from a child procedure. The incident skill's bundled `REFERENCE.md` documents mitigation task mutation, while the top-level procedure's no-auto-execute warning covers only recommendations, not prior data transmission or remote task creation.
- **Strengths worth extracting:** explicit auth-mode selection and config confirmation, IAM confused-deputy protection, public-access blocking, AgentSpace choice, STRIDE findings, paginated incident journals, failure reporting and no-auto-execute recommendations. Preserve as ADAPT/EXTRACT/CHECKLIST inputs with new independent gates, not as unchanged-use approvals.
- **Freshness and portability:** source identity and exact package fingerprints are pinned. Package-specific last-modified dates were not established. AWS API availability, regional support, cost, MCP proxy version and token scopes are volatile; the host must recheck before adaptation. Claude-specific configuration, AWS permissions and CLI tooling reduce portability.
- **No quota-driven inference:** all five received individual records, scores, dependencies, controlled tags, authority profiles and decisive rationale. No behavioral or scanner evidence was invented.

## Public accounting and lifecycle

This bounded tranche adds five provenance records and five exact-version verification records, plus this macro review. The five public accounting surfaces are reconciled together: README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json. `registry/sources.yaml` is updated to match. Public inventory: **44 first-party**, **834 → 839 third-party**, **878 → 883 total verification records**. Admitted-source denominator **94 → 94**; AWS progress **80 → 85** and gaps **14 → 9**.

Open first-party repair PRs #489/#492/#496 remain separately blocked on pinned SkillSpector v2.12.0 exact-package reports and independently executed adversarial acceptance for 36 changed package identities. Admission drafts #412/#413 require their own external qualification. This AWS source-review tranche does not qualify or merge those PRs. No repository-owned runtime, CI, script, scheduler, scanner or background process was added.

**Next highest-priority admitted-source action:** map the seven AgentCore packages and review a bounded group with full reference/dependency and authority inspection, then resolve the login and divergent CDK identities.
