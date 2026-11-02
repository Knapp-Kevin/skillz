# Awesome Copilot: all 313 remaining packages (2026-11-02)

**Source:** `github/awesome-copilot` at `f11a4e441c5ff061b4f8ae37952be8c602e4034e`. Root MIT, GitHub, Inc.; package-local licenses recorded per record.
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers every remaining direct-shape skill package: 177 single-file and 136 multi-file. Exact package records are in the [ledger](../../registry/discovery/github-awesome-copilot-remaining-313-static-20261102.json), and the [capability index](../../registry/discovery/github-awesome-copilot-capability-index-20261102.json) lists them by domain and subdomain.

| Measure | Before | After |
|---|---:|---:|
| Awesome Copilot terminal exact-path decisions | 119 / 432 | **432 / 432** |
| Four-source current-standard exact-path decisions | 3,405 | **3,718 / 4,813** |
| Raw paths without a current-standard decision | 1,408 | **1,095** |

Results: **194 REFERENCE-ONLY / 119 REJECT unchanged**, 0 DEFER. Hard-fail flag counts:

| Flag | Packages |
|---|---:|
| `unauthorized-consequential-action` | 47 |
| `self-update-or-remote-code` | 10 |
| `private-data-egress` | 6 |
| `capability-content-mismatch` | 4 |
| `license-conflict` | 4 |
| `embedded-agent-instruction` | 4 |
| `secret-logging` | 3 |
| `solicits-secret-in-chat` | 2 |
| `literal-credential` | 2 |
| `credential-in-url` | 1 |

Main capability domains: software-engineering (99), agent-mcp-development (58), cloud-devops (37), technical-writing (15), security (14), testing (13), memory-context (12), marketing (8).

## Method

- **Review:** 19 parallel read-only reviewers worked disjoint package lists, balanced by text weight and kept in name order so related families stayed together.
- **Integration checks:** the integration owner validated exact blob/tree identity, controlled taxonomy and rubric-rationale agreement, and computed the static threshold signal itself.
- **Second pass:** 97 REFERENCE-ONLY records whose notes mentioned ungated actions, privacy, missing files or rights issues were re-adjudicated by three independent reviewers. Each decision cites a quote from the package.
- **Overrides:** 28 are recorded in the ledger:
  - 19 REFERENCE-ONLY records below the 10/20 floor were demoted;
  - 7 hard fails were added;
  - 3 static-threshold signals were withdrawn for missing required files.

## Static threshold signal

**73** packages score at least 15/20, have no hard fail, and score at least 1 on trigger precision, authority and dependency coherence. This flags candidates for a future governed review. It is **not** verification, admission or approval.

The top-scoring examples:

| Package | Score | Capability |
|---|---:|---|
| `mcp-implementation-security-review` | 18 | security/application-security |
| `mcp-release-qa` | 18 | testing/end-to-end |
| `resx-source-generator-migration` | 18 | software-engineering/build-tooling |
| `shopify-review-triage` | 18 | product/prioritization |
| `verify-agent-action` | 18 | agent-mcp-development/permissions |
| `codebase-memory-mcp` | 18 | software-engineering/developer-experience |
| `d365-solution-blueprint` | 18 | software-engineering/architecture |
| `agent-skill-stack` | 17 | agent-mcp-development/orchestration |
| `gitmoji` | 17 | software-engineering/developer-experience |
| `harness-engineering` | 17 | agent-mcp-development/agent-architecture |
| `impediment-prioritization` | 17 | planning/decision-frameworks |
| `incident-postmortem` | 17 | cloud-devops/sre |

## Macro findings

- Every remaining pinned Awesome Copilot skill package (313 direct-shape, 177 single-file and 136 multi-file including scripts, references, templates and assets) was read as a complete package by 19 parallel read-only reviewers; binary assets were recorded by type and a handful of >60 KB generated data files were characterised rather than read line by line (noted per record).
- 47 packages fail the authority hard gate: pushes, PR creation and thread resolution without per-action confirmation (copilot-pr-autopilot, github-release, make-repo-contribution, workshop-create, repo-standardizer), live cloud/tenant/Store changes (azure-devops-cli with --yes, azure-static-web-apps production deploys, entra-agent-user, msstore-cli, foundry-agent-sync, powerbi-modeling, snowflake-semanticview), DNS changes (namecheap), destructive file operations (document converters that rmtree output folders) and persistent agent-memory writes without approval (audit-integrity).
- Privacy: six packages read or send private data without consent (clipboard, colleague email and meetings, calendar/chat pre-fill, production LLM traces to third-party judges, vendor usage telemetry); secret handling defects include printed deploy tokens, plaintext DB passwords echoed back, passwords solicited in chat, API keys in query strings and hard-coded weak passwords.
- Ten packages fetch-and-follow remote content or install unpinned code at runtime (unpinned npx -y github:..., suggest-* skills overwriting local files from main, remote PROMPT.md declared trusted).
- Rights: package-local licenses override root MIT for several packages (Microsoft MIT, Apache-2.0 quality-playbook and resemble-detect); four license conflicts (unattributed datasheet and MDN/tutorial copies, LGPL-like ISO data, unattributed Azure icons). GitHub Docs CC-BY material inside this GitHub-owned repository was not treated as a third-party conflict.
- Accuracy: many packages carry stale or wrong version-specific claims (MCP SDK templates that do not compile, renamed PostgreSQL views, wrong React 19 statements, outdated App Store rules); these lower scores but are not hard fails.
- Quality controls: 28 integration overrides recorded (19 REFERENCE-ONLY records below the 10/20 floor demoted; 7 hard fails added by a three-way second-pass adjudication of 97 REFERENCE-ONLY records whose notes mentioned ungated actions, privacy or rights; 3 static-threshold withdrawals for missing required files).
- 73 packages meet the computed static threshold signal (>=15/20, no hard fail, trigger/authority/dependency >=1); this marks candidates for a future governed review and is NOT verification, admission or approval.

## Next

The four-source frontier now holds j4flmao (555) and OpenAI Plugins (536). OpenAI plugins mostly declare licenses in `plugin.json` without shipping license text, and 8 declare Proprietary terms; those rights caveats will be recorded per package.
