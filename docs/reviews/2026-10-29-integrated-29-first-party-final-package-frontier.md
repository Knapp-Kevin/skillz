# Integrated first-party authority repairs: final exact-package qualification frontier

**Date:** 2026-10-29. **Candidate manifest commit:** `dd82725a191c264e46437270d2559efb5b165feb`. **Base main:** `f19e78107b91a1897ed04eae53c1cb7d09aaed60`. **PR:** #489 (draft). **Scope:** 29 existing first-party packages. **No scanner or behavioral test executed.**

## Macro reconciliation

- Four superseded source PRs (#416, #480, #482, #485) covered **31 PR-package slots**, but only **29 distinct skills**. `mcp-vetting` and `permissions-review` each appeared twice. Their selected final versions are #485 and #482 respectively; the older #416 variants contain obsolete permission-tier/source-trust contracts.
- **29/29** final `SKILL.md` blobs match the consolidated first-party registry and **29/29** individual verification companions; **29/29** individual provenance companions contain a source revision, canonical local path, and structured-review state. The entire 44-entry registry matches **44/44** integrated manifests. These are **static identity checks**, not security or behavioral validation.
- Historical October 10 baseline status for the 29 changed packages: **8 PASSED**, **20 INCOMPLETE**, **1 FAILED**. All 29 integrated package trees differ from their historical scanned baseline trees, so **none of those old security results can qualify the new final package identity**. The other **15** unchanged first-party historical matching-pass packages remain outside this tranche.
- No source admission, source-pin movement, inventory increase, or new repository-owned execution machinery. Current public counts remain **44 first-party, 826 third-party reviews, 870 verification records**. Microsoft candidate remains **102/102 static review and NO-GO pin promotion**.


- **2026-10-29 independent pulse recurrence macro review:** 16 of 17 pulse-named skills in this PR had an optional schedule instruction but lacked a complete durable-authority scope contract. Their 16 final manifests now default to one-time reporting and require separately approved cadence/timezone/expiry, future source and private access scope, recipients/delivery, retention, costs and revocation before any external-host recurrence. The seventeenth, `repo-pulse`, already had this boundary; `claude-pulse` outside this PR remains one-time only. The same tranche removes an obsolete `permission-tier` reference from `mcp-pulse` and a nonexistent `skills-pulse` reference from `github-pulse`. See [targeted review](2026-10-29-pr489-sixteen-pulse-recurrence-authority-macro.md). No external execution occurred.

## Exact final package identities

| Skill | Origin PR | Integrated package tree SHA-1 | Final SKILL.md Git blob SHA-1 | Historical baseline |
|---|---:|---|---|---|
| `decision-log` | #416 | `8eb548e7e3f0ea832b6d7f29093caa69b2ec4ff4` | `3e1ceeb3a20e2d933e5ade631e82d54dd582a44b` | INCOMPLETE |
| `deepseek-pulse` | #416 | `302a655c2ecd1c40cf720063705edb7e5fec5855` | `00e0977fa32c82172ad35cd3fb9344e86d79bfe0` | INCOMPLETE |
| `devlog-draft` | #416 | `a5c4e1bbb5e33b93d6df01a6ebd0f1f99ea94e76` | `e7f6456fafbe4b432270696d64e3685a8ca8725a` | INCOMPLETE |
| `gemini-pulse` | #416 | `c1a7ac283b563d7a6f38c5f4f8895ba25510f864` | `2656c2ab5615324432502619411fb75210e7b1bf` | INCOMPLETE |
| `github-pulse` | #416 | `2085adff634cdead09f57446a2e4b07ede0cd80b` | `b0ee1fa9d065527c840ee9f3a6e5a9dc693fc032` | INCOMPLETE |
| `glm-pulse` | #416 | `7d281f05871cc7f0ca5147c788d1df5a24ae6b06` | `bee05faf21b9ae30cc704e8c77b1a7cf41b6eb06` | INCOMPLETE |
| `governance-pulse` | #416 | `61080b0db5550b2c8a20119f5d61d29ef6b44cb6` | `69755799a3560771a4bf21cbae39dec341f60b36` | INCOMPLETE |
| `handoff-writer` | #416 | `0706a8de5d49106d136c1c6c4029ba4ea947e8fd` | `b60a41bc26348370eb61a60b9c1287f29044e92c` | FAILED |
| `hf-pulse` | #416 | `f2ae9b7b51b8b2a8a112979921907573bd46db5a` | `2862f7f9c0e8d07bae7e68bb64f1edfb9f8a3044` | INCOMPLETE |
| `inference-pulse` | #416 | `79ac17e06a79d480bee52f682261c8285ab7252b` | `c7d7679e6cdfbfb271964e6b9f7e47a8d1c08b60` | INCOMPLETE |
| `kimi-pulse` | #416 | `cd210595372709162895da9d93b10edaf98e992c` | `6f9780f934fecbb9d1e949da8b4b93b1f6482d52` | INCOMPLETE |
| `llama-pulse` | #416 | `ce57a74006d59e11696fa4a4596616b0bea39a64` | `eca89a1a66b51de87e4b7c26f9f449d646e191b6` | INCOMPLETE |
| `mcp-pulse` | #416 | `f18864b57a0e88daaea486ca877879f1bec4bd26` | `6d8a859704952a7e88488b91c4eb4ab2ff0c52ca` | INCOMPLETE |
| `memory-pulse` | #416 | `17f9dc8ab0eade44d589646d94f55737eb4d23fd` | `f5acde9edb65db529ef4b1e029d534428f557a2d` | INCOMPLETE |
| `mistral-pulse` | #416 | `d2fbd53e666548a4d90540cf2f79cdc2ad23df03` | `e47dc0143a7898532cddb94eb0391e7785dfdd1d` | INCOMPLETE |
| `openai-pulse` | #416 | `1ca3acd6648883f178fd828a0af74958b2e477ee` | `954a1fc98e9c71c59afe034eef2e553cfed63011` | INCOMPLETE |
| `perplexity-pulse` | #416 | `ac324ead5e31cc366b7d449e92fae6fef8dd221b` | `cdc6506a16c5e7a87029783cdcad8f078a009d80` | INCOMPLETE |
| `qwen-pulse` | #416 | `02ad927ef67e5a212e52d8ed19928545cf5764d4` | `77dc93a39022008c45f386871a2c94c83fb04146` | INCOMPLETE |
| `xai-pulse` | #416 | `35c3e5a18faf620db37f92582152365cfcea8eb9` | `c95b9e4e8b8dc37aaa3c7d3d7b27371e84212e18` | INCOMPLETE |
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
