# First-party pulse host-only repair: complete 19-skill sweep (2026-11-03)

**Status: substantive implementation on draft PR #673, HOLD for qualification.** The repository itself remains passive. This receipt describes a real candidate patch, not an accepted release or completed external security check.

## Source and scope

- Starting `main`: `389d2f93ec0cee309039c0c0a4ad164dbd85c7db`. Draft PR #673 branch `fix/pulse-host-native-source-collection-20261103-no-ci`, initially changed only `governance-pulse` and `memory-pulse` from its first head `66cd7630aea4aad70ed02bfbcd45e2d9616bb4e1`.
- Inspected **19** live first-party pulse/monitoring SKILL.md manifests from current first-party inventory: **16** had a concrete `node scripts/pulse-run.ts` instruction; **three did not** (`career-radar`, `claude-pulse`, `repo-pulse`). The old runner is removed and cannot be reinstated.
- Checked all 16 bundled `skills/<name>/sources.json` files; all exist, parse as JSON, and were retained byte-for-byte. Source lists include 216 listed source/search elements in total (sum of array lengths, not distinct URLs or approved sources). No new service, account, credential or network action was created.
- Replaced the removed-runner step for the **14 previously unfixed** manifests with host-only read/search behavior, verification of dates and source URLs, safe handling of unavailable providers and secret-free queries; retained the two earlier PR fixes and made their patch versions explicit. All 16 now require explicit per-task authorization for recurring scheduling; one-off requests remain one-off.
- Applied **patch SemVer bumps** to all 16; retained non-target step content and `sources.json` inputs.
- Checked ten mainline live entry documents: `README.md`, `AGENTS.md`, `AGENT_START_HERE.md`, `docs/agent-value-discovery.md`, `docs/consumer-discovery-and-installation.md`, `docs/capability-quickstart.md`, `engine/skills/skill-bootstrap/SKILL.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`. No active `scripts/pulse-run.ts` commands found. Historical archived documents were not altered.

## Full-package exact-identity checks

All sixteen candidate manifest SHA values below were read from the branch and again at **resolvable source revision `81f476885d8741343077f91faf60b4972485af21`**, which contains every patched SKILL.md. For each skill, the current `registry/verification/local-skills/<name>.yaml` and `registry/local-verification.json` store the same new blob fingerprint, and the first-party `registry/skills/local-skills/<name>.yaml` record points to that source revision.

| First-party skill | New SemVer | Prior reviewed SKILL.md blob | Current candidate SKILL.md blob | New qualification state |
|---|---|---|---|---|
| `deepseek-pulse` | 1.1.1 | `e5778521bac5459432731814755dd2c4d60ff705` | `eb5ee9d97e7efe9f38cff89958396dfd9ec82457` | stale / not-run |
| `gemini-pulse` | 1.0.1 | `8bf2cc64aaaaa60dd3a15e94464a17d475f9bc80` | `437f1a0c71015898bbf4bd90ca1156791a137536` | stale / not-run |
| `github-pulse` | 1.0.1 | `03e135f4e916115040af63271de71b23277e36f7` | `24addb7d68087c21f99330830977920d77fd3269` | stale / not-run |
| `glm-pulse` | 1.1.1 | `3bfbb84c43a76413897b30ad675d1ba5d8b8a1de` | `82da67c37302abd77dac002014c82602527f5981` | stale / not-run |
| `governance-pulse` | 1.1.1 | `aa2157650140bf0820b6d6b1921c5f0881d8c627` | `e2c69537b86becb9293b5237dc0ec3f96a5f7b28` | stale / not-run |
| `hf-pulse` | 1.0.1 | `de2d55b632e88deaa71aa145cf83293f5877381a` | `65465396c75537c6cd28036c6487ff68ec17b057` | stale / not-run |
| `inference-pulse` | 1.1.1 | `bc90e5248c04c408c8c5a44bea62b1d66a7fb143` | `e8bc23828371be651bf8cfe449f1a0257a24a841` | stale / not-run |
| `kimi-pulse` | 1.0.1 | `4d8935ea2d8006ea277ab1371f419c723a867643` | `831a77f1d8250f6fd23db9a20a07570a63bf8d19` | stale / not-run |
| `llama-pulse` | 1.1.1 | `d5141bcfebcc4e9ccbba4cbfc9cf57564010b5dc` | `d90c47b7ac39122bd9ef26bfa88ac3c6af707b1b` | stale / not-run |
| `mcp-pulse` | 1.1.1 | `41451ac34a4a660ec82cae2c4356d3afe4b49334` | `46c878d52188f658cce1389294bc5aa6b13082f6` | stale / not-run |
| `memory-pulse` | 1.1.1 | `659441df0952f7db302835606068c812ed81d22f` | `b030f35f52c66b13892a3ad8f1e362f15ff9be5e` | stale / not-run |
| `mistral-pulse` | 1.0.2 | `4d2e092ee1cfdbd7127145926d48d6cf78b46ce1` | `a04a39981d17c4f2b237e387e4464b18f6d333f5` | stale / not-run |
| `openai-pulse` | 1.0.1 | `d6b98630525e16d392b3f50e67ae674332316310` | `bd16ca6f71c76c7c9dcfabf36a34752b9df408f3` | stale / not-run |
| `perplexity-pulse` | 1.0.1 | `ef8b1cfd50f464f91d02855eaad7d05032475493` | `26c79e2b73172810b1ff9342528b3a7c15b2de42` | stale / not-run |
| `qwen-pulse` | 1.1.1 | `e22ff1879ce563a76e733bc576bed80cf4cc5f12` | `8c1a9821f38fe09ccf275084ec2ebda029fe2d16` | stale / not-run |
| `xai-pulse` | 1.0.1 | `ec172826db6d811dbea1985c8962ad342c310412` | `7b1a9cf2c21e36f05d0b2ee9507e90b78c67e924` | stale / not-run |

**No inherited approval:** These are new exact-version manifests. Their earlier `rubric_score` values are preserved **as historical evidence only**, with `rubric_score_current_fingerprint: false`; each individual YAML record and consolidated entry is `verification_status: stale`, and each provenance record has `review_status: stale` and `import_eligibility: conditional-on-security-and-user-fit`. Source snapshot pin, source path, original license, user-facing purpose and consent boundaries are retained. In the 44-record first-party consolidated surface: **16 stale candidate manifests**, **28 previously verified unchanged records**. These are branch-local *proposed* status changes, not mainline count changes.

## Validation actually performed

- Static source readback: **16/16** exact manifesto / pinned snapshot / per-skill verification / provenance consistency checks passed; no former runner command remains in the sixteen changed SKILL.md files.
- All 16 JSON source lists parsed and were not edited. Scope scan: 19 relevant SKILL.md files (16 changed, three untouched).
- Verified that the 10 named live entry docs contain no former runner invocation.
- Did **not** execute any third-party skill, external search, behavioral model session, attack simulation, SkillSpector scan or scanner package.
- **Security:** not-run for the 16 new exact package versions; earlier scanner receipts do not apply to changed package bytes. **Behavioral/adversarial execution:** not-run. **Static risk review:** source strings and authority wording reviewed, not an external executable acceptance result.
- No repository runtime, script, CI, scheduler, crawler, daemon or monitor added; all commits use `[skip ci]`.

## Remaining release gates

1. Run the separately pinned and approved **external** SkillSpector v2.12.0 final-package review with complete-file evidence on all 16 exact package trees, including bundled sources.json, then reconcile findings.
2. Execute independent representative host/adversarial tests for missing browser/permissions, rate limits, injected search results, unauthorized recurring action, secrets and private context, and ensure no private data leaves the host through a search query.
3. Complete controlled per-skill 10-dimension semantic requalification on the new exact fingerprints. Prior scores remain historical.
4. Before merging, reconcile current main/head and the five public catalog/accounting surfaces **if** changed verification states affect displayed totals. No source identity or positive-endorsement inflation is permitted.

**Disposition:** KEEP PR #673 DRAFT/HOLD until these gates are met; KEEP issue #415 OPEN, because this branch is not on main and current-final-package acceptance is not established. The candidate does eliminate the concrete removed-runner instructions without discarding the sibling evidence.
