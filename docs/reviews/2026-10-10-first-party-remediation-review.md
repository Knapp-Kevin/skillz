# SkillSpector first-party remediation: exact-version review handoff

Date: 2026-10-10. Branch: `security/402-first-party-scan-remediation`. Related [#402](https://github.com/Knapp-Kevin/skillz/issues/402), [#410](https://github.com/Knapp-Kevin/skillz/pull/410).

**State: individual semantic/adversarial reviews pending.** A successful scanner run is not proof that new skill instructions satisfy the prior semantic rubric, and historical verification fingerprints do not automatically transfer.

The prior [21-package scan](https://github.com/Knapp-Kevin/skillz/actions/runs/38061878414) passed 21/21 changed packages without SkillSpector failures. The main-branch full-corpus attempt had 21 fail-closed coverage results (not proven malicious content), documented under #402.

## Exact content changes

| Skill | Prior Git blob (main) | Proposed Git blob (PR #410) | Semantic review |
|---|---|---|---|
| `decision-log` | `56e5c574c295546c9e654a9e6a14a9814136f2f4` | `d16c7982c869bb95bb9d0120f0b4526ed58e5426` | pending |
| `deepseek-pulse` | `e5778521bac5459432731814755dd2c4d60ff705` | `371d463fd4b226c86f528fcfd1db5b0a7cde8660` | pending |
| `devlog-draft` | `073f18ba2c2f7de21015cd072741c395335e9f2e` | `4b15319435e77d6ad89b9882351f8c5fa7773b03` | pending |
| `gemini-pulse` | `8bf2cc64aaaaa60dd3a15e94464a17d475f9bc80` | `29593f4c61a2826d17186c01f8820e05bbeced0a` | pending |
| `github-pulse` | `03e135f4e916115040af63271de71b23277e36f7` | `4e2cfc4e3d93508c50cc4c066c6883ef8ea1a446` | pending |
| `glm-pulse` | `3bfbb84c43a76413897b30ad675d1ba5d8b8a1de` | `39363b6628911d6f9c6a784667f831aaf5a8c0f7` | pending |
| `governance-pulse` | `aa2157650140bf0820b6d6b1921c5f0881d8c627` | `972f3a8bdd9e58eacc389afae9b0f742b4ecf4e3` | pending |
| `handoff-writer` | `8a789ea0dd3b1c89ccac9d50727b06007abcf5c1` | `2a7a1265db9f335c537643dff3b5e7e234e8e8b4` | pending |
| `hf-pulse` | `de2d55b632e88deaa71aa145cf83293f5877381a` | `f2f6446408241a0498d26e094fc74190191bb03a` | pending |
| `inference-pulse` | `bc90e5248c04c408c8c5a44bea62b1d66a7fb143` | `5ce06c1b813e1dc85ad653cf79f0f78bd8e4300c` | pending |
| `kimi-pulse` | `4d8935ea2d8006ea277ab1371f419c723a867643` | `becc18f469bc16ce65218a6ef98f03024f4870f7` | pending |
| `llama-pulse` | `d5141bcfebcc4e9ccbba4cbfc9cf57564010b5dc` | `d46b389147819690da2f3f6814061d211aa01803` | pending |
| `mcp-pulse` | `41451ac34a4a660ec82cae2c4356d3afe4b49334` | `0912feff2503d0369fcd7c8998da8a800b30f6ac` | pending |
| `mcp-vetting` | `806e79f593446ad15938249898e15230208f2d81` | `3d0145a95b0b353c0983d117c0fd84c71a86d8a0` | pending |
| `memory-pulse` | `659441df0952f7db302835606068c812ed81d22f` | `ad7de59f767a5f2f6948a5d3e651c58491ea92ee` | pending |
| `mistral-pulse` | `4d2e092ee1cfdbd7127145926d48d6cf78b46ce1` | `da89e053c7074b9d14274b23766dbe88ffee3a29` | pending |
| `openai-pulse` | `d6b98630525e16d392b3f50e67ae674332316310` | `d9d163b7717d7d3b15eef4788519296b86140555` | pending |
| `permissions-review` | `60e1d546e713cfa5b289def082dd73e8b326f029` | `306d5f6abf561370ee5083e1d70d9deefe2f040c` | pending |
| `perplexity-pulse` | `ef8b1cfd50f464f91d02855eaad7d05032475493` | `5fd9db6162fa01cd294b53c65e82600bcaf919d4` | pending |
| `qwen-pulse` | `e22ff1879ce563a76e733bc576bed80cf4cc5f12` | `e27177ddb112e0cc2427a86b023374b54b9322a1` | pending |
| `xai-pulse` | `ec172826db6d811dbea1985c8962ad342c310412` | `7337cf51dda4491f9c1584fd4f42217fc688ff97` | pending |

## Review by change group

- **Vendor and topic pulses:** Replacing `node scripts/pulse-run.ts` with host-available tools removes unsupported repository runtime assumptions. Check that sources, time windows, attribution, side-effect restrictions, and unavailable-host handling remain functional; no automatic scheduling.
- **Decision log and devlog:** Removing assumed `docs/DECISIONS.md` paths must preserve the operator's nominated log, read-only/default behavior, and approval-gated append.
- **MCP vetting and permissions:** Make impact-tier definitions self-contained without weakening identity, cost, destructive, or data-exfiltration protections. Keep vetting and permission review report-only.
- **Governance pulse:** Host-dependent metadata inspection must remain optional, read-only and explicitly unavailable when absent.
- **Handoff:** Redaction stays mandatory; credential rotation is recommendation-only, never performed by this writing skill.

## Acceptance before merge

- [ ] Inspect all **21** proposed instruction changes for actual semantics and host portability, not merely scanner acceptance.
- [ ] Run trigger/non-trigger and adverse instruction-pressure scenarios for consequential skills.
- [ ] Independently rereview and update each affected `registry/verification/local-skills/<name>.yaml` with the **new exact blob** and an evidence-backed semantic state/rubric result. Until then, old verified evidence binds only to old blobs. Do not copy prior score by fiat.
- [ ] Record any relevant first-party provenance changes and require per-package security evidence under `registry/security/`.
- [ ] Re-run full **44 first-party** SkillSpector gate against the final candidate and retain its exact-version reports through #408.
- [ ] Keep behavioral validation `not-run` absent actual execution, verify final diff, and obtain independent review.

This document is a review ledger, not a `verified` or security-`passed` assertion.
