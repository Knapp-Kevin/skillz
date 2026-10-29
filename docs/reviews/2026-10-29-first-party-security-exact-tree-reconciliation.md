# First-party historical security exact-tree reconciliation

**Date:** 2026-10-29. **Main:** `713c98fa55d5c7fa27552f567b4bd73e9f0f7a18`. **Scope:** all 44 first-party packages. **No scanner or behavioral test executed.**

## Macro accounting

- 44/44 current `SKILL.md` blobs match `registry/local-verification.json`; 44/44 package trees match the historical baseline scan targets.
- Retained baseline (`registry/security/first-party-baseline-2026-10-10.json`): **23 PASSED** with complete coverage, zero active findings, SHA-256 report digests and pinned scanner identity; **20 INCOMPLETE**; **1 FAILED** (`handoff-writer`). This is historical evidence for identical current-main package trees, not 23 new scans.
- Candidate (`registry/security/first-party-candidate-2026-10-10.json`): 44 PASSED at a different source commit, but **only 23** candidate package trees equal current main. The **21 nonmatching candidate passes are not transferable**.
- All 21 baseline nonpasses are revised in unmerged **#416**. Eight baseline passes have pending manifest changes in **#480** (five) and **#482** (three). `permissions-review` and `mcp-vetting` additionally overlap #482/#485. If those drafts merge, the eight previously passing package identities become stale; **15** matching-pass packages currently have no manifest changes in those drafts.
- Exact-tree matching preserves the meaning of an existing scan report, but it does not cure the known P1 authority defects or establish semantic/behavioral approval, package freshness, user fit or merge readiness. The scanner was NVIDIA SkillSpector v2.12.0 at `c7958a3268d9498644b22edb75d0f051bbc8cbfc`, static-only, `--no-llm --fail-on-findings --fail-on-incomplete`.

## Exact package matrix

| Skill | Main package Git tree SHA-1 | Baseline state | Candidate tree matches? | Unmerged repair |
|---|---|---|---|---|
| `agent-home-doctor` | `715150a85cf47b6f68e08735996f5fe394deac72` | PASSED | yes | none |
| `agent-postmortem` | `2859a7ce0b9424e52c4c044cef7074bcd924af8a` | PASSED | yes | none |
| `automation-receipts` | `cdf9aa3df667e2b1156b310d924b0559716c7d6a` | PASSED | yes | none |
| `brief-writer` | `c6d40fbd06c310a0259548c37c2d5338bfc42903` | PASSED | yes | none |
| `career-radar` | `cfcbff6d7d3b1d6300e3287a3e01caebd8855104` | PASSED | yes | #480 |
| `claude-pulse` | `690a0c7ed7a9666ef71d9a607bccfa28833eae02` | PASSED | yes | none |
| `compare` | `6d67ced9cf7a588ad35774918ed07b9a2a6d7f71` | PASSED | yes | none |
| `daily-briefing` | `a43d8314e09a10227eac37c710261160b0a887d2` | PASSED | yes | #480 |
| `decision-log` | `286f2aac12926ba8fba0836c35dce3daf2d83965` | INCOMPLETE | no | none |
| `deck-outline` | `8ef15cae96adcf8289c3c844847f026b97f8cfc6` | PASSED | yes | none |
| `deep-dive` | `aca9a5ead634fa4e7bf986ab11c38da228890e56` | PASSED | yes | none |
| `deepseek-pulse` | `10aa4e6d8b2cf89ac9c27b538684de75581653e0` | INCOMPLETE | no | none |
| `devlog-draft` | `867a94024356cc4545c4fc712b247c9fc0cd0244` | INCOMPLETE | no | none |
| `fact-check` | `a922bd0405fe1779b43349ac2336f71a86e8e099` | PASSED | yes | none |
| `finance-review` | `65edb7c6acd6b6ac808bd4f55ecd5b0248b774c3` | PASSED | yes | none |
| `gemini-pulse` | `b08a023ebe015ef072b1c3acfb566c218c494508` | INCOMPLETE | no | none |
| `github-pulse` | `3e914c97c76ec2e5ef9f861ee434516dfbd70455` | INCOMPLETE | no | none |
| `glm-pulse` | `32584b50b6a82a5186a6133539c33ed702f6f3a9` | INCOMPLETE | no | none |
| `governance-pulse` | `af3a1710ea1c187956bd6034e52327e2f257b8d5` | INCOMPLETE | no | none |
| `handoff-writer` | `430f96ac8b01b0ade5ffbe680131d1e2d575af2d` | FAILED | no | none |
| `hf-pulse` | `5bc8e3c60139688e4fc9ff0a7e2d10685701ca7a` | INCOMPLETE | no | none |
| `inbox-triage` | `b00a0c36f604147b4665e34a62aaffc608b8f246` | PASSED | yes | #480 |
| `inference-pulse` | `7c7b0b48bba555f4e989d78a1d4463af933bdc05` | INCOMPLETE | no | none |
| `kimi-pulse` | `0b6d6d9d339448fe9baaea566ee28c2a2b8583ad` | INCOMPLETE | no | none |
| `learning-plan` | `706728f600246427b77609ff3cd9904c1490218a` | PASSED | yes | #482 |
| `llama-pulse` | `221db05d2638e6407eb608ba1225e17fdf0abb95` | INCOMPLETE | no | none |
| `mcp-pulse` | `fe568a39ebd18f11353f74ae4d567b785c07afa0` | INCOMPLETE | no | none |
| `mcp-vetting` | `d06472b10125e598253ca82564a43242433f58f7` | INCOMPLETE | no | #416/#485 |
| `memory-pulse` | `da8047567efa064415e0945542835c444fbe1b01` | INCOMPLETE | no | none |
| `mistral-pulse` | `cb9b3571e69a60d4f2fd76c52704202331f0efa3` | INCOMPLETE | no | none |
| `openai-pulse` | `aabca083ed4bef6e520089d39dba36fc545b892b` | INCOMPLETE | no | none |
| `paper-digest` | `6820240e263bafbf832742f47310cab4958573a4` | PASSED | yes | none |
| `permissions-review` | `71246bf93839c94885d43acd21ee3a4dc5704ef3` | INCOMPLETE | no | #416/#482 |
| `perplexity-pulse` | `819d6aadafdfb37887efda8bb7ed5aa42e8befea` | INCOMPLETE | no | none |
| `qwen-pulse` | `0103e9d55e6c7e804dc765386644605b4ac2c072` | INCOMPLETE | no | none |
| `repo-doctor` | `c2529253b35b5f90d58500091a0d1efbb1c14c2b` | PASSED | yes | none |
| `repo-pulse` | `bb8e4cac90acfadabf235a0b09435e7e2f8fa50d` | PASSED | yes | #480 |
| `session-continuity` | `35aa83bd4823be99babe9015b629071cb3ed5cb5` | PASSED | yes | none |
| `smallbiz-ops` | `979bf89b0a3d3ec2b8858462560b1a05ef100cdc` | PASSED | yes | #480 |
| `standup-writer` | `ff5aef8e22cad85d0423cc3ce50b857316b2dbdc` | PASSED | yes | #482 |
| `task-surface` | `084c416caea0bf8413859dff06cbc23370019168` | PASSED | yes | none |
| `todo-harvester` | `8e718ecafbf601557cf5ca44fb681affdac1f4a9` | PASSED | yes | none |
| `week-in-review` | `36c5b72bdba27b46118b5745032ea066ecf8cdb9` | PASSED | yes | #482 |
| `xai-pulse` | `68a3a03703847cf32d71f74f33068be360315d25` | INCOMPLETE | no | none |

## Lifecycle disposition

Issue #402 remains OPEN. No new security pass was granted and no report was rewritten. Prioritize fresh complete pinned external scans for final changed identities, beginning with #480's five, followed by #482's four and #416's 21; #485 overlaps `mcp-vetting`. Independently execute representative adversarial acceptance and reconcile shared first-party registry before merging. Preserve passive architecture; no repository-owned scanner, CI, runtime, scheduler or test runner.
