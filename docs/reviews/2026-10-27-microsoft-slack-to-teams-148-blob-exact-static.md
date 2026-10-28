# Microsoft Slack-to-Teams: exact-version shared-boundary review

**Date:** 2026-10-27. **Disposition:** REJECT unchanged (11/20); retain EXTRACT / ADAPT / CHECKLIST reference value. **Review type:** exact-revision static semantic and authority review; package security **not-run**, representative behavioral/adversarial validation **not-run**. No external operation was executed.

## Identity, denominator and dependency closure

- Source: [microsoft/skills](https://github.com/microsoft/skills) at candidate `61fe0305ea70389ed8705eec6026a786f57865cf`; registered July pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` remains unchanged. Upstream root license MIT (blob `79656060de00aa4659ad2c276d5be8830664d544`); no package-specific conflicting terms found in inspected Markdown. No candidate material vendored.
- Canonical nested first-class manifest: `.github/plugins/microsoft-365-agents-toolkit/skills/teams-app-developer/slack-to-teams/SKILL.md`, blob `11dfd2b3b069b8ae77d835c7317c3698d94346f0`; **one** local blob (9,109 bytes), tree `41f03fb5bb8791de6d0c2d1c76764372d906bc3c`.
- Parent `teams-app-developer/SKILL.md` blob `04d194383e9863d8167d8005747cf6a3933ddc26`; manifest last changed 2026-06-15 at `a43d2c6a69fac2298ac0f301419931b39d996c6b` (this is skill-manifest freshness, not a shared-expert freshness guarantee).
- Shared expert subtree `teams-app-developer/experts/` has exact tree `39ecbc21af77c72859ec9e32dc7e88fb7052ded9`, **120/120** source-owned Markdown blobs, **1,469,504** bytes, seven expert domains plus root utility/router files. The non-truncated Git tree was enumerated; all 120 exact blobs were fetched and screened for scope, authority, sensitive data and relevant behavior. Consequential examples were read in depth.
- **27/27** additional parent/sibling files were fetched and screened: parent manifest (1), create-project (1), docs (11), provision-deploy (1), test-playground (3), test-teams (1), toolkit (8), troubleshoot (1). Together with the local manifest, **148 distinct source blobs** were examined across the dependency closure. Sibling subskills and shared experts are dependencies, not extra canonical admissions of `slack-to-teams`.
- External dependencies: Slack API/Bolt and workspace permissions; Teams SDK/Bot Framework; Microsoft Graph, Entra ID, Agents Toolkit, Azure/AWS, storage and model providers. No dependency or cloud command was executed. Upstream reference code and examples are not repository-owned execution machinery.

## Exact-source findings

1. **Credential solicitation:** parent `SKILL.md` line 14 says to ask users for real environment-variable values, including secrets. This invites conversational secret disclosure instead of secure host credential handling. Parent source blob `04d194383e9863d8167d8005747cf6a3933ddc26`.
2. **Identity and cross-platform disclosure:** `experts/bridge/identity-oauth-bridge-ts.md` line 16 maps Slack users to Entra identities by email; later code queries user profiles and builds an identity map. No distinct tenant/workspace-owner authorization, transfer scope, consent, retention or sensitive-data boundary precedes cross-platform correlation. Blob `a8f45f15533be3ff9ac134f20954dbe2cd3ae7f2`.
3. **File exposure:** `experts/bridge/files-upload-download-ts.md` discusses preauthenticated URLs, Graph `createLink` sharing (including anonymous scope), and direct Graph channel upload outside the personal-chat consent-card path. Authentication scopes and technical file consent do not grant authorization for wider file disclosure. Blob `6f5bb460724bfebb9b7724fd56fbbf1c0d8edbe2`.
4. **Design defaults treated as action choice:** `experts/bridge/cross-platform-advisor-ts.md` lines 154-157 allow "You Decide Everything" to accept all YELLOW/RED defaults. This may be a valid planning shortcut, but must not authorize migrations, cloud deployment, messaging, access grants or data sharing. Blob `5330e68f51d64de73e2272bf574a519b50c5ba9f`.
5. **Infrastructure, identity and cost effects:** `experts/deploy/azure-bot-deploy-ts.md` creates resource groups, Entra applications, resets credentials and configures app settings; `experts/deploy/aws-bot-deploy-ts.md` describes IAM creation, credentials and billable cloud deployment. No action-specific, tenant/subscription/role/cost-bound approval gate controls the entire path. Blobs `0a7de69f9eaddb067e21648044cc16e960b0436a` and `c665d944b8165229853f544dd87e1ce5fbf45ade`.
6. **Destructive lifecycle:** `experts/convert/bulk-conversion-strategy-ts.md` line 20 directs deleting original source files after conversion, without an explicit separate destructive-change approval. Blob `f25f305ee28d1c8bd19d7f26d6e1addaa9c64b2a`.
7. **Communications and external exposure:** `experts/slack/web-api-proactive-ts.md` and `experts/teams/runtime.proactive-messaging-ts.md` describe proactive messages and stored conversation IDs without an overarching sender/recipient/notification authorization gate. `test-teams/test-teams.md` line 19 instructs an anonymous public devtunnel. These require explicit target, environment, audience and exposure approval. Blobs `077c845059470b6ef33c7b08f0b8d0c91e8408c3`, `27955ae4ee806862e0566dcd2dcd99af071ac06b`, `438650757373814632498496273b844e7765ec8b`.
8. **Positive safeguards:** `experts/security/secrets-ts.md` advocates managed identity, Key Vault, least privilege, and secret-log redaction; `experts/security/input-validation-ts.md` supplies validation patterns; `toolkit/publish.md` explicitly distinguishes submission from Teams Admin Center approval. These are useful prior art, but do not supply missing authorization for the separate operations above.

## Rubric and synthesis

| Dimension | /2 |
|---|---:|
| Trigger precision | 2 |
| Procedural clarity | 2 |
| Authority and safety | 0 |
| Failure handling | 1 |
| Evidence discipline | 1 |
| Dependency coherence | 1 |
| Portability honesty | 1 |
| Differentiated usefulness | 2 |
| Adversarial resilience | 0 |
| Effectiveness design | 1 |
| **Total** | **11/20** |

**Macro:** Strong differentiated bridge, UI-conversion, SDK-language and routing prior art. The shared tree is materially larger than the one-file local package, so manifest-only reviews would undercount risk. Across bridge, deployment, messaging and lifecycle experts, technical permissions and implementation choices repeatedly substitute for action authorization. The parent secret-request instruction is an independent privacy hard fail. Preserve the expert taxonomy, identity-map design cautions, file-consent distinctions, SDK migration patterns and Key Vault practices for scoped adaptation. Do **not** select the unchanged package.

**Scope limits:** This was source-text inspection and risk triage of all 148 exact blobs, with deep review of consequential paths; no static security scanner, external package installation, runtime execution, live credential, tenant operation or representative behavioral test was performed. Shared-expert freshness may differ from the manifest's last-change date. The candidate source pin was not advanced.

## Accounting and lifecycle

Candidate structural denominator remains **208** = 106 exact-tree carry-forwards + 76 changed-existing + 26 new/ungoverned. New-candidate complete static reviews **24/26 → 25/26** (4 semantic VERIFIED only / 21 REJECT unchanged). Remaining **1 new (Foundry IQ) + 76 changed = 77** full current-version reviews. Registered July remains **186/186** at the existing pin. Third-party verification companions **748 → 749**, first-party **44** unchanged. No new admission, package-security pass, behavioral validation or repository-owned execution surface. Issue #400 remains open; PRs #412/#413/#416 remain blocked on independent and exact-package security acceptance.
