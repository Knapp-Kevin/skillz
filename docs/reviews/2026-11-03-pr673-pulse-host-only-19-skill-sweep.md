# First-party pulse host-only repair: complete 19-skill sweep (2026-11-03)

**Status: substantive implementation on draft PR #673, HOLD for qualification.** The repository itself remains passive. This receipt describes a real candidate patch, not an accepted release or completed external security check.

## Source and scope

- Starting `main`: `389d2f93ec0cee309039c0c0a4ad164dbd85c7db`. Draft PR #673 branch `fix/pulse-host-native-source-collection-20261103-no-ci`, initially changed only `governance-pulse` and `memory-pulse` from its first head `66cd7630aea4aad70ed02bfbcd45e2d9616bb4e1`.
- Inspected **19** live first-party pulse/monitoring SKILL.md manifests from current first-party inventory: **16** had a concrete `node scripts/pulse-run.ts` instruction; **three did not** (`career-radar`, `claude-pulse`, `repo-pulse`). The old runner is removed and cannot be reinstated.
- Checked all 16 bundled `skills/<name>/sources.json` files; all exist, parse as JSON, and were retained byte-for-byte. Source lists include 228 listed source/search elements in total (sum of array lengths, not distinct URLs or approved sources). No new service, account, credential or network action was created.
- Replaced the removed-runner step for the **14 previously unfixed** manifests with host-only read/search behavior, verification of dates and source URLs, safe handling of unavailable providers and secret-free queries; retained the two earlier PR fixes and made their patch versions explicit. All 16 now require explicit per-task authorization for recurring scheduling; one-off requests remain one-off.
- Applied **patch SemVer bumps** to all 16; retained non-target step content and `sources.json` inputs.
- Checked ten mainline live entry documents: `README.md`, `AGENTS.md`, `AGENT_START_HERE.md`, `docs/agent-value-discovery.md`, `docs/consumer-discovery-and-installation.md`, `docs/capability-quickstart.md`, `engine/skills/skill-bootstrap/SKILL.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`. No active `scripts/pulse-run.ts` commands found. Historical archived documents were not altered.

## Full-package exact-identity checks

All **16 final candidate manifest SHA values** below were re-read on the draft branch and at their resolvable pinned source revision: **14 unchanged-since-guard snapshots** at `4ff16d78e6414fd1637026062e57e18c821440b9`, and **two separately protected local-private-read variants** (`governance-pulse`, `mcp-pulse`) at `c75566e7470c5c6072a405e8c4a5526d2cb7c94f`. Each `registry/verification/local-skills/<name>.yaml` and consolidated `registry/local-verification.json` uses the final exact SKILL.md blob SHA; the individual provenance entry references the corresponding source revision. All 16 final source-revision SHA checks passed. Earlier `81f476...` is a historical intermediate version and does not apply to this final candidate.

| First-party skill | New SemVer | Prior reviewed SKILL.md blob | Current candidate SKILL.md blob | New qualification state |
|---|---|---|---|---|
| `deepseek-pulse` | 1.1.2 | `e5778521bac5459432731814755dd2c4d60ff705` | `63be9ffb787e29e7c9d53a4111c817f660d0c943` | stale / not-run |
| `gemini-pulse` | 1.0.2 | `8bf2cc64aaaaa60dd3a15e94464a17d475f9bc80` | `9dbae1510d0fb3c65056fc53f0050ce0ed6ede59` | stale / not-run |
| `github-pulse` | 1.0.2 | `03e135f4e916115040af63271de71b23277e36f7` | `b0c3784a53ef3ad15fda0a7678239b8bec86c42a` | stale / not-run |
| `glm-pulse` | 1.1.2 | `3bfbb84c43a76413897b30ad675d1ba5d8b8a1de` | `79e2e3b384ee707871122fa70d5fb3651c0511e6` | stale / not-run |
| `governance-pulse` | 1.1.2 | `aa2157650140bf0820b6d6b1921c5f0881d8c627` | `a444566237940b43944bc1f5e0afb55708d84123` | stale / not-run |
| `hf-pulse` | 1.0.2 | `de2d55b632e88deaa71aa145cf83293f5877381a` | `3250a7c3ed49783329220536e8ef4a1f7b9bb286` | stale / not-run |
| `inference-pulse` | 1.1.2 | `bc90e5248c04c408c8c5a44bea62b1d66a7fb143` | `7f152bc910bf5a225170f7ab16c0c47c641613da` | stale / not-run |
| `kimi-pulse` | 1.0.2 | `4d8935ea2d8006ea277ab1371f419c723a867643` | `3e2e6cc836ddb05e0da6a7dafb7048a30fd9921e` | stale / not-run |
| `llama-pulse` | 1.1.2 | `d5141bcfebcc4e9ccbba4cbfc9cf57564010b5dc` | `c0c38b0dd182f1f588d1800b832b331c8572080e` | stale / not-run |
| `mcp-pulse` | 1.1.2 | `41451ac34a4a660ec82cae2c4356d3afe4b49334` | `d59296c2fcc6d287a1cc38a890bde34d0fcf43fa` | stale / not-run |
| `memory-pulse` | 1.1.2 | `659441df0952f7db302835606068c812ed81d22f` | `d0b57c1da47b800cf0003149ef08a869068d5944` | stale / not-run |
| `mistral-pulse` | 1.0.3 | `4d2e092ee1cfdbd7127145926d48d6cf78b46ce1` | `5695a01a8d7927f87be7da76ec353d12ef56ddb9` | stale / not-run |
| `openai-pulse` | 1.0.2 | `d6b98630525e16d392b3f50e67ae674332316310` | `1285b1226733e93b0db4b230a6fb0021e5220fd0` | stale / not-run |
| `perplexity-pulse` | 1.0.2 | `ef8b1cfd50f464f91d02855eaad7d05032475493` | `06906792509a41a3a9cbb641e02f47e9fb458a69` | stale / not-run |
| `qwen-pulse` | 1.1.2 | `e22ff1879ce563a76e733bc576bed80cf4cc5f12` | `03d3015bbfe571ddaf4fa9448de66f74bb62ce69` | stale / not-run |
| `xai-pulse` | 1.0.2 | `ec172826db6d811dbea1985c8962ad342c310412` | `58dcef43210c4ddb09f4a7ad7273d99516e42813` | stale / not-run |

**No inherited approval:** These are new exact-version manifests. Their earlier `rubric_score` values are preserved **as historical evidence only**, with `rubric_score_current_fingerprint: false`; each individual YAML record and consolidated entry is `verification_status: stale`, and each provenance record has `review_status: stale` and `import_eligibility: conditional-on-security-and-user-fit`. Source snapshot pin, source path, original license, user-facing purpose and consent boundaries are retained. In the 44-record first-party consolidated surface: **16 stale candidate manifests**, **28 previously verified unchanged records**. These are branch-local *proposed* status changes, not mainline count changes.

## Validation actually performed

- Static source readback: **16/16** exact manifesto / pinned snapshot / per-skill verification / provenance consistency checks passed; no former runner command remains in the sixteen changed SKILL.md files.
- All 16 JSON source lists parsed and were not edited. Scope scan: 19 relevant SKILL.md files (16 changed, three untouched).
- Verified that the 10 named live entry docs contain no former runner invocation.
- Did **not** execute any third-party skill, external search, behavioral model session, attack simulation, SkillSpector scan or scanner package.
- **Security:** not-run for the 16 new exact package versions; pinned SkillSpector unavailable in this execution host. Earlier scanner receipts do not apply to changed package bytes. **Behavioral/adversarial execution:** not-run. **Static risk review:** source strings and authority wording reviewed, not an external executable acceptance result.
- No repository runtime, script, CI, scheduler, crawler, daemon or monitor added; all commits use `[skip ci]`.

## Independent static authority and adversarial-case review (2026-11-03)

**Static text inspection, NOT executed behavioral/adversarial acceptance.** Read the full 16 final SKILL.md manifests and checked the following attack/failure cases against their published instructions:

| Case | Checked safeguard | Static result / limit |
|---|---|---|
| User requests one news digest; agent attempts to schedule itself | One-time, read-only default and separate approval requirement | **16/16** contain the boundary. No scheduled action was attempted. |
| Recurring request lacks frequency, timezone, source/data-access scope, delivery, retention, budget, expiry or cancellation | Missing terms cannot be assumed; require action-specific approval | **16/16** have explicit consent scope. No scheduler was invoked. |
| Search result, README or forum post instructs an agent to install tools, change policy, send a message, upload files or disclose credentials | Retrieved material is untrusted evidence, never authority | **16/16** contain source-trust guard language. No agent was exposed to an actual hostile payload in a representative run. |
| Host has no browser, MCP tool, GitHub token or access to a cited source | Report unavailable evidence and source/date; never invent freshness or request secrets | **16/16** have missing-source fallback. No live model run. |
| A digest includes sensitive memory, credentials or private code in public search strings | Prevent sensitive data in queries, URLs, and public provider requests | **16/16** prohibit private-data egress. No outbound search or DLP test executed. |
| Governance digest tries to read `.qor/` or `docs/META_LEDGER.md` without local-file authorization | Separate permission for named local file and exact read scope | **governance-pulse explicitly hardened**, other skills unaffected; no local file read executed. |
| MCP digest opens `.mcp.json` or private integration settings just because they exist | Require explicit approval of local path/read scope; never print secrets | **mcp-pulse explicitly hardened**, no local config read executed. |
| Referenced peer skill or deprecated permission tier is absent | No implicit `skills-pulse` runtime; describe suggested intake without writes or old tier assumptions | Updated **github-pulse** and **mcp-pulse** source text only. |

**No automated package security pass was produced.** The authorized host did not have NVIDIA SkillSpector installed; its network could not resolve GitHub to retrieve v2.12.0. This is an environment limitation, not a scanner finding and not a waiver of the external security gate. Scanner pin and execution requirements remain in [the repository's security policy](../../docs/security-scanning.md). No LLM security provider was called and no private package contents were sent to a third party.

**SemVer and provenance:** final manifests have package-local patch-version bumps. Every change to a SKILL.md fingerprint was reflected in individual verification YAML, local-skills provenance YAML and the 44-record consolidated registry. Prior scores are historical, not reverified current-package grades. Source-list files remain unmodified.

## Remaining release gates

1. Run the separately pinned and approved **external** SkillSpector v2.12.0 final-package review with complete-file evidence on all 16 exact package trees, including bundled sources.json, then reconcile findings.
2. Execute independent representative host/adversarial tests for missing browser/permissions, rate limits, injected search results, unauthorized recurring action, secrets and private context, and ensure no private data leaves the host through a search query.
3. Complete controlled per-skill 10-dimension semantic requalification on the new exact fingerprints. Prior scores remain historical.
4. Before merging, reconcile current main/head and the five public catalog/accounting surfaces **if** changed verification states affect displayed totals. No source identity or positive-endorsement inflation is permitted.

**Disposition:** KEEP PR #673 DRAFT/HOLD until these gates are met; KEEP issue #415 OPEN, because this branch is not on main and current-final-package acceptance is not established. The candidate does eliminate the concrete removed-runner instructions without discarding the sibling evidence.
