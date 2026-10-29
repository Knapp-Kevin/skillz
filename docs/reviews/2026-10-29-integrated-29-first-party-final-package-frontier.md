# Integrated first-party authority repairs: final exact-package qualification frontier

**Date:** 2026-10-29. **Candidate commit:** `7c05bb6826d4382326a03aa4691107d10cd1f79c`. **Base main:** `f19e78107b91a1897ed04eae53c1cb7d09aaed60`. **PR:** #489 (draft). **Scope:** 29 existing first-party packages. **No scanner or behavioral test executed.**

## Macro reconciliation

- Four superseded source PRs (#416, #480, #482, #485) covered **31 PR-package slots**, but only **29 distinct skills**. `mcp-vetting` and `permissions-review` each appeared twice. Their selected final versions are #485 and #482 respectively; the older #416 variants contain obsolete permission-tier/source-trust contracts.
- **29/29** final `SKILL.md` blobs match the consolidated first-party registry and **29/29** individual verification companions; **29/29** individual provenance companions contain a source revision, canonical local path, and structured-review state. The entire 44-entry registry matches **44/44** integrated manifests. These are **static identity checks**, not security or behavioral validation.
- Historical October 10 baseline status for the 29 changed packages: **8 PASSED**, **20 INCOMPLETE**, **1 FAILED**. All 29 integrated package trees differ from their historical scanned baseline trees, so **none of those old security results can qualify the new final package identity**. The other **15** unchanged first-party historical matching-pass packages remain outside this tranche.
- No source admission, source-pin movement, inventory increase, or new repository-owned execution machinery. Current public counts remain **44 first-party, 826 third-party reviews, 870 verification records**. Microsoft candidate remains **102/102 static review and NO-GO pin promotion**.

## Exact final package identities

| Skill | Origin PR | Integrated package tree SHA-1 | Final SKILL.md Git blob SHA-1 | Historical baseline |
|---|---:|---|---|---|
| `decision-log` | #416 | `8eb548e7e3f0ea832b6d7f29093caa69b2ec4ff4` | `3e1ceeb3a20e2d933e5ade631e82d54dd582a44b` | INCOMPLETE |
| `deepseek-pulse` | #416 | `3c575fe6269d4c8db60bb6fc344847aff6ddf84e` | `1fc968fb94bfcd3618fda085b08cf0cd21d4c23e` | INCOMPLETE |
| `devlog-draft` | #416 | `a5c4e1bbb5e33b93d6df01a6ebd0f1f99ea94e76` | `e7f6456fafbe4b432270696d64e3685a8ca8725a` | INCOMPLETE |
| `gemini-pulse` | #416 | `9d1a2554c59fe899c9dea62832700a1f12406618` | `69b1b4dd1ba164308f755629510b2043eb358e61` | INCOMPLETE |
| `github-pulse` | #416 | `acfac6174affa184ca9f26ddc403f36352e83d43` | `587313bab488dc27411f9e52c1c43516dc8f26f4` | INCOMPLETE |
| `glm-pulse` | #416 | `add0ce74321fe264675c05ad32a4c160501a933a` | `7c7f92832f42e7cfdafe36da087b1e634ab060b6` | INCOMPLETE |
| `governance-pulse` | #416 | `d5252bdc3d6df4e322c9b8da11261ad18153d36b` | `0709d2f3392b5e63f1e91b98e805cb0e13a95d14` | INCOMPLETE |
| `handoff-writer` | #416 | `0706a8de5d49106d136c1c6c4029ba4ea947e8fd` | `b60a41bc26348370eb61a60b9c1287f29044e92c` | FAILED |
| `hf-pulse` | #416 | `a4c77c12ada126088ed1e21f177811567bb49daa` | `38387fea604b6eb7d9e81b1e449b36f8ca1fc30c` | INCOMPLETE |
| `inference-pulse` | #416 | `04e5aa1dc2b6f7af8868db8587d6dfb89d20f6e5` | `6c676b7e9e45e82504d84fa4bbd56682830660b8` | INCOMPLETE |
| `kimi-pulse` | #416 | `be320e5329997231128e1d452c968192977a47ef` | `eefd3337a2875fef8251a4478b391a75318fa694` | INCOMPLETE |
| `llama-pulse` | #416 | `133ed88743d5e6f7bb39b93c97e53afda058c7de` | `3f0bd40adde01d1855b557c0f62f5e0eb28b0a7e` | INCOMPLETE |
| `mcp-pulse` | #416 | `6c54d0a1f5fcb0076ceb6fee92a945f4dc5458a4` | `d1a2d62b9f4ffa90a1c13480ca00034ddffd52ee` | INCOMPLETE |
| `memory-pulse` | #416 | `70fa836f96636eca978cf1e6b3966653b16b7e99` | `7d0404768a982758ce3bbbf80aadb561b41957e2` | INCOMPLETE |
| `mistral-pulse` | #416 | `7e1167a5694bc893a28002c0c82c37cb7f9279a8` | `23bbc1a8f7f8ecd5af2db7d5cf5ebea3488640ce` | INCOMPLETE |
| `openai-pulse` | #416 | `30d85cec0dc9949c677ff13fc98a5e08bd121848` | `7344d2e431afad9e0fde6e179ed14517ec00b8a0` | INCOMPLETE |
| `perplexity-pulse` | #416 | `25a4fd99f813abab55b4c427ce213243f7d3aca1` | `38eeae61d87c292aeffc4f32bd038b7862d9b6b6` | INCOMPLETE |
| `qwen-pulse` | #416 | `d1465bae43b301d39213fc02e2f65e40aa370670` | `f56496f4ca0bcd7969d5e5d3fe308d8a45ba251e` | INCOMPLETE |
| `xai-pulse` | #416 | `6718db3e8fc919504dbf0d4a03b354038ef43c70` | `ad904ae0b35fd605780c0ffaa856a2da3606394c` | INCOMPLETE |
| `career-radar` | #480 | `23aea5706cb130078f1ec01b8cf937a8f9d37305` | `35e211d098f4497568beca3999ecf250a46183c5` | PASSED |
| `daily-briefing` | #480 | `eeec1cc5332edf5014150215b215aacd4c429e8d` | `86353382996c2ce73b7981d341ef0bea93b7b6c2` | PASSED |
| `inbox-triage` | #480 | `65e68d2c50737b4a408b495fe1c1fac5e9209481` | `c1566f6ccfd15cb92094c256c7295234368c4b27` | PASSED |
| `repo-pulse` | #480 | `4cf41fc603927e329aa19172682fd5ea5fcb7c74` | `91631c593f9923b86b19ec6a4c8e6f0643af7e78` | PASSED |
| `smallbiz-ops` | #480 | `5d4a8dcc47ab9c61510ec298f9d0b9c7558da65c` | `83439d9422c5a7bdc57f0ad15ebf4378faf43265` | PASSED |
| `learning-plan` | #482 | `931fb2192a3cb1212643fe1df51d5e4bc3c70af4` | `7941b70fc971bf7c16c1201b7c8876f35db4ab29` | PASSED |
| `permissions-review` | #482 | `8b8cbd95cbcb4f053c1070fdb4400c823593863f` | `dcaf7ff96c832c69bb5be1c7cd8f4c3ed418b707` | INCOMPLETE |
| `standup-writer` | #482 | `59dd3dd9f44b66b7b8a9dc21a72f49e5ce58d3d9` | `b8473ac1ea68795d9563a21f335b5fd4bc169868` | PASSED |
| `week-in-review` | #482 | `0d8ee8ccdefdbc6c6478a5dbbb7d54d8ef4ac321` | `f2145e28256ebdfb72b035f1a405fd0e6586c5ba` | PASSED |
| `mcp-vetting` | #485 | `a8824fff4a3d0ed5b7a82603b48f1aefbccb9666` | `37a13d7296c7d3d87dc360988bc6aca1f873c4db` | INCOMPLETE |

## External qualification boundary

An authorized **external host** must scan the exact **29 final package trees above**, not the 31 intermediate PR versions. Use registered NVIDIA SkillSpector **v2.12.0**, commit `c7958a3268d9498644b22edb75d0f051bbc8cbfc`, static-only mode `--no-llm --fail-on-findings --fail-on-incomplete`. Preserve full scanner output, completeness proof, scan timestamp, target package identity, report digest, findings and individual dispositions. A package changed after scanning is stale and must be requalified. Scanner network/OSV behavior must respect approved egress and data boundaries.

Separate independent **executed** external-host adversarial/behavioral evidence is still required for the final manifests: explicit approval before scheduling or future private reads, safe handling of untrusted source/tool output, no secret disclosure, authorization before external sends or consequential changes, honest incomplete-source reporting, and correct refusal/abstention behavior. Written scenarios and this matrix are not executed evidence.

**Status: DRAFT / HOLD.** The package-security state of all 29 final identities is **not established** and behavioral validation is **not-run**. Do not merge #489 until these gates and any review findings are resolved, final head/main drift is checked, and expected-head protection is used. Preserve the passive repository boundary.
