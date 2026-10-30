# AWS pinned final-two closure and CDK authority correction (2026-10-30)

## Source-family macro map and denominator

Live registered source: `aws/agent-toolkit-for-aws@ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546` (root Apache-2.0); pinned intact under `skills/sources/aws-agent-toolkit/`. Prior recursive pinned-tree census: **115** front-mattered `SKILL.md` exposure paths, **93** distinct skill names, **94** distinct package-tree identities. Exact-tree mirrors collapse; the two `aws-cdk` exposures are **not** mirrors. At the start of this tranche, **92/94** had current-standard provenance and verification companions, leaving exactly two genuine gaps: `signing-in-to-aws` and `plugins/aws-core/skills/aws-cdk`. The core `aws-cdk` was already companion-complete but had a false unchanged-use approval. The final tranche resolves **92/94 → 94/94**, **2 → 0 gaps**; the eligible denominator remains **94**. This is static semantic completeness, not a claim of security or behavioral approval.

| Canonical package / exposure | Package tree SHA | SKILL.md blob SHA | Individual decision | Score |
|---|---|---|---|---|
| `skills/core-skills/signing-in-to-aws` (exact mirror at `plugins/aws-core/skills/signing-in-to-aws`) | `ee531e3e75bc80420fa93a7cec433cc3cdb3340f` | `3f56dd7330dc9ff8ade816425d5d1d5b4a79c5f7` | REJECT unchanged (new) | 14/20 |
| `plugins/aws-core/skills/aws-cdk` | `1c69221e639f1e6efe81befa51d3b5cdb064f737` | `bf47a52741f9b7c97c1dd5189676f6c44397559f` | REJECT unchanged (new variant) | 14/20 |
| `skills/core-skills/aws-cdk` | `6ed8c50838438d4a6f4746fb9d90c4e8ae63b288` | `27d488115c9fb60ed7a5dc68ff44a7b6e44acab9` | VERIFIED 19/20 → REJECT unchanged 15/20 | 15/20 |

The `signing-in-to-aws` package has no bundled references; the two CDK packages each contain nine source-owned references. Five CDK references have identical blob SHAs across variants, while the manifest, bootstrap, construct, deployment and synth references differ. In particular, the canonical core offers a three-deploy weak-reference migration and newer CloudFormation diagnostics; the plugin variant uses a two-deploy export workaround and older event diagnosis. These are materially different behavior/evidence paths, not duplicate names to count once.

## Individual static review and authority findings

### signing-in-to-aws: REJECT unchanged 14/20

**Use / non-use:** Local AWS CLI/SDK authentication recovery when credentials are missing or expired. Not CI/CD, not an established IAM Identity Center SSO flow, not an excuse to overwrite existing profiles. Requires local shell, AWS CLI >=2.32.0, browser/remote login and AWS STS/IAM; portability **low**. Last package-specific manifest change at the registered pin: **2026-06-16 09:55 UTC**, commit `62cc3a66c3958271cdf29cdce573a5521b51bc8d`; AWS CLI behavior, availability and policy guidance remain time-sensitive.

**Strength:** Explicit approval before `aws login`, preservation of existing SSO workflows, short-lived credentials and profile isolation.

**Hard fail:** The precondition flow orders `aws sts get-caller-identity` and conditional `aws configure list` **silently before asking permission**, prints account/ARN and inspects access-key prefix metadata. That is private identity/credential metadata access, not merely local version checking. The later approval covers `aws login` only, not the earlier identity read or output disclosure. A host must independently authorize exact account/profile, private fields and display scope before these reads, and must not solicit or echo secret fragments. Login may also persist credential/profile state. Retain secure-credential and SSO distinctions as ADAPT/EXTRACT/CHECKLIST, not unchanged instructions.

**Rubric:** trigger 2, clarity 2, authority 0, failure 2, evidence 1, dependencies 2, portability 1, differentiation 2, adversarial 0, effectiveness 2 = **14/20**. Authority hard fail independently prevents promotion.

### plugin aws-cdk: REJECT unchanged 14/20

**Use / non-use:** CDK TypeScript/Python infrastructure authoring, bootstrap, deploy, import, refactor, drift and rollback; not SAM, raw CloudFormation, Terraform or Pulumi. Requires CDK/AWS CLI, CloudFormation, IAM, AWS account credentials and nine bundled references; portability **medium**. Plugin manifest last changed **2026-05-13 09:01 UTC** at commit `803cbf47025e5f98cc52e4597614ca9bf94205d1`.

**Strength:** Source-intact reference depth, diff-before-deploy, resource replacement cautions, cross-stack export migration and troubleshooting.

**Hard fail:** The main workflow and references prescribe `cdk bootstrap` (including `--trust` role grants), `cdk deploy`, `cdk import`, `cdk rollback --force`, `cdk destroy` and persistent CloudFormation/IAM changes. There is no action-specific gate for account/region, stack/resource, target environment, spend, data-loss/destruction or deployment window. Diff inspection, warnings, command parameters and CLI prompts are not authorization. The plugin's older two-deploy workaround does not inherit the core variant's newer review. Preserve migration and diff safeguards as adaptation/reference only.

**Rubric:** trigger 2, clarity 2, authority 0, failure 1, evidence 2, dependencies 2, portability 1, differentiation 2, adversarial 0, effectiveness 2 = **14/20**.

### canonical core aws-cdk: VERIFIED 19/20 → REJECT unchanged 15/20

**Use / non-use:** Same broad CDK domain but a different package and reference tree. Core manifest last changed **2026-06-11 07:51 UTC**, commit `e089489e33747df19abf0f3548dcfb8d1f4ee6b8`; nine bundled references, CDK/CloudFormation/IAM and project tooling, portability **medium**.

**Hard fail:** Its stronger three-deploy cross-stack migration and replacement safeguards still direct consequential `cdk bootstrap`, deploy, import, rollback, drift remediation, destroy and possible trust/IAM/data-lifecycle changes without independently scoped user authority. Production `cdk diff` is a review step, not consent. Its previous 19/20 VERIFIED state incorrectly treated strong safety guidance as sufficient permission. Retain staged migration, least-privilege and stateful-resource safeguards as ADAPT/EXTRACT/CHECKLIST.

**Rubric:** trigger 2, clarity 2, authority 0, failure 2, evidence 2, dependencies 2, portability 1, differentiation 2, adversarial 0, effectiveness 2 = **15/20**. Authority hard fail overrides numeric threshold.

## Systemic synthesis and omissions

- **Delegated authority:** A sign-in or infrastructure-design request must not silently expand into private identity reads, persistent credentials, IAM trust changes, paid cloud provisioning or destructive resource lifecycle operations.
- **Variant-aware identity:** Canonical skill name is insufficient for exact-version deduplication. The identical `signing-in-to-aws` mirrors collapse, but CDK core and plugin differ in their bundled migration/diagnostics guidance and require separate records.
- **Privacy and secrets:** Account/ARN and access-key-prefix metadata should be minimized; no real credential value, signed URL or token should be collected in conversation. AWS account/profile reads require scoped authority.
- **Evidence/freshness:** All decisions bind to pinned source trees and manifest Git blob SHAs. Package-specific last-change commits are recorded where established; AWS CLI/CDK/API behavior and prices remain volatile. **No SkillSpector run, package-security approval, representative external behavioral test or adversarial execution** occurred. `validation_status: not-run` remains explicit.
- **Value/overlap:** CDK variants offer differentiated reference methods but both fail unchanged-use authority. Keep intact upstream packages as rejected prior art; do not create duplicate first-party wrappers merely to inflate inventory.
- **Source priority:** AWS is now **94/94 current-standard static complete**. Shift from gap closure to selective freshness and omission detection. New source discovery/admission delta **0**.

## Repository flow and accounting

Two new exact-version provenance/verification pairs, one corrected core pair, this macro review, source registry and all five public accounting surfaces are reconciled in one tranche. Published inventory **44 first-party / 848 third-party exact-version reviews / 892 total verification**; denominator delta **0**; AWS **92/94 → 94/94**; gaps **2 → 0**. Source pin and source-owned package trees unchanged. No repository-owned runtime, script, test, CI, scheduler, generator, scanner or background service introduced. The five pre-existing draft PRs #489/#492/#496/#412/#413 are separately blocked by external exact-package security and independent adversarial acceptance; none is made ready by this static review.
