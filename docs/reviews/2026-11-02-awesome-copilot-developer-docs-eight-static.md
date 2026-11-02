# GitHub Awesome Copilot: eight developer documentation and workflow packages (static source vetting)

**Date:** 2026-11-02. **Source:** `github/awesome-copilot@f11a4e441c5ff061b4f8ae37952be8c602e4034e`. **Evidence:** [individual exact-version ledger](../../registry/discovery/github-awesome-copilot-developer-docs-eight-static-20261102.json). **Program:** #599, process improvement #624.

## Macro-first selection and package completeness

From the 337 unresolved direct-shape paths in this pinned 432-path source, selected eight previously unreviewed developer documentation, repository workflow and agent-support packages. These share root MIT source terms but differ materially in privacy, authority and output reliability. All eight exact `SKILL.md` files were read; the pinned upstream `docs/README.skills.md` asset index reports no bundled assets for seven and one `references/conventional-commits-guide.md` for `commit-message-storyteller`, which was also read. The source manifest records each skill blob and containing package-tree SHA. No host tools, package scripts, tests, CI, security scanners or behavioral evaluations were executed. The asset index is evidence of declared package contents, not a separate recursive tree API proof; this limitation is retained in individual records.

The root [MIT LICENSE](https://github.com/github/awesome-copilot/blob/f11a4e441c5ff061b4f8ae37952be8c602e4034e/LICENSE) was read at the same pin (blob `89bc5e962c9944cdb050887062afdaaf89be504a`). Individual frontmatter, package assets and third-party tool/dependency rights remain separately relevant. No material was vendored or admitted.

## Individual decisions

| Pinned package | Grade | Terminal candidate disposition | Decisive static finding |
| --- | ---: | --- | --- |
| `ai-prompt-engineering-safety-review` | 13/20 | REFERENCE-ONLY | Useful prompt safety checklist, but overbroad mandatory report, unvalidated scoring and unredacted reproduction of potentially sensitive prompts |
| `brag-sheet` | 13/20 | REJECT unchanged | Private Copilot session logs, Git history and cross-repo PR mining require distinct account/data-access authority; optional extension installation is not authorized by availability |
| `chrome-devtools` | 11/20 | REJECT unchanged | Live click/fill/upload/JavaScript and network payload reads lack explicit page/session, data and action boundaries |
| `convert-plaintext-to-md` | 11/20 | REJECT unchanged | Creates or reuses a same-name Markdown file and can overwrite content without an existing-file/target authorization gate |
| `create-agentsmd` | 11/20 | REJECT unchanged | Unconditional root `AGENTS.md` creation and test commands lack write/execution authority and existing-governance preservation |
| `conventional-branch` | 12/20 | REJECT unchanged | `git pull`, checkout and branch creation proceed without remote/network authorization, dirty-tree guard or user-approved mutation |
| `create-architectural-decision-record` | 12/20 | REJECT unchanged | Automatically writes numbered ADR under `docs/adr`; no file-write approval, collision check or decision-authority proof |
| `commit-message-storyteller` | 15/20 | REFERENCE-ONLY | Good intent-first drafting and bundled Conventional Commits reference; private diff reads and asserted impact need explicit evidence/authorization |

Each exact record includes source pin, Git blob, package tree, package-file evidence, source license, trigger/non-trigger, dependencies, privacy/authority, ten-dimension score and rationale, controlled capability tags, terminal candidate disposition and explicit `not-run` security/behavioral states. `REJECT` and `REFERENCE-ONLY` retain useful prior art, not approval to install or execute.

## Family-level synthesis

The principal defect is **action conflation**: a request to draft documentation or discuss a branch is treated as permission to overwrite files, access private histories or run networked Git commands. Read-only prompt/commit methods are safer but still require source privacy and claim verification. A single source-level MIT check reduced repeated provenance work without relaxing per-package rights or individual scoring.

The tranche also reveals **capability overlap** with previously reviewed commit-message, browser-testing and documentation guidance. Source-vetted examples must not be promoted into the governed 1,039-record population or presented as preferred because of their publisher. No new first-party inventory or source admission.

## Accounting and remaining work

GitHub Awesome Copilot: **95/432 → 103/432** exact-path candidate decisions; direct **78/415 → 86/415**, other-shape **17/17 unchanged**; **329 raw paths** remain. Four-source pinned path decisions: **185/4,813 → 193/4,813**, leaving **4,620 raw paths** without terminal path-matched decisions. These are raw-path counts, not the deduplicated eligible-package denominator, which remains **unknown**. Governed review population **1,039 unchanged**. New security scans **0**, behavioral validations **0**, admissions **0**.

Next: use the verified identity preflight to reconcile complete-package overlap and process a further bounded, risk-tiered source-family tranche. Preserve the passive architecture and do not invent execution evidence.
