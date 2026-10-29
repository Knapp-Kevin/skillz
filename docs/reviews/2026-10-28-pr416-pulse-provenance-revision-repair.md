# PR #416: 16 pulse provenance revision and eligibility repair

**Observed:** 2026-10-28 UTC. **Base candidate head:** `1ae6f0698ca1b970dfea51683fedd34977d9548f`. **Scope:** first-party provenance records on draft PR #416 only. **Disposition:** evidence repair, **not** package-security approval or merge acceptance.

## Reproduced defect

The 16 changed pulse manifests each had a correct current `registry/verification/local-skills/<name>.yaml` `content_blob_sha`, but the corresponding provenance companion's `source_snapshot_revision` still pointed to `906b229172b9e81f0338048c50522df6439bf63c`. Independent `fetch_file` readback at that old revision returned **16/16 different SKILL.md blob identities** from the candidate head. A prior 21-package identity audit checked manifest/verification/consolidated consistency but did not check whether the provenance source revision actually resolved to the claimed current manifest.

Nine of those 16 provenance records also still advertised `import_eligibility: eligible-with-complete-skill-folder`, despite no qualifying final-version package-security evidence. Seven already used `conditional-on-security-and-user-fit`.

## Corrective change

For all 16 pulse provenance companions, set `source_snapshot_revision` to the observed candidate commit `1ae6f0698ca1b970dfea51683fedd34977d9548f`, which contains the exact SKILL.md blobs below. Refresh `last_checked_at` to 2026-10-28 after direct exact-version readback. Set the nine stale eligibility labels to `conditional-on-security-and-user-fit`; preserve the seven already-conditional labels. No skill manifest, source list, semantic verification record, package-security status, or behavioral state is changed.

| Package | Exact candidate SKILL.md Git blob | Resolvable source revision |
|---|---|---|
| `deepseek-pulse` | `2aadd8f5d190e3b4ae91cf5877a09ef25ee33304` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `gemini-pulse` | `36b460f40471134da8e13c16d707b6d17f3004a1` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `github-pulse` | `587313bab488dc27411f9e52c1c43516dc8f26f4` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `glm-pulse` | `5a0414e6d8bda0433d5fbedbde734b8369a25f6c` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `governance-pulse` | `0709d2f3392b5e63f1e91b98e805cb0e13a95d14` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `hf-pulse` | `38387fea604b6eb7d9e81b1e449b36f8ca1fc30c` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `inference-pulse` | `6c676b7e9e45e82504d84fa4bbd56682830660b8` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `kimi-pulse` | `4c953878c4c02183d819e94a89462c151bef2f44` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `llama-pulse` | `818a0d1d9a2225a6ae311eba6b4f19955558a1af` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `mcp-pulse` | `23e62f52dbfdf657106c9f8212a3be3ce312849f` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `memory-pulse` | `7d0404768a982758ce3bbbf80aadb561b41957e2` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `mistral-pulse` | `81e2d64d29af4fa3ac1fc6aeeda38166ec5bed11` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `openai-pulse` | `cfb234de2003eb1024b8e4d7dd7c3172c80e1718` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `perplexity-pulse` | `4426e6744badf1f77c552fb50aa807a464b8ab8b` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `qwen-pulse` | `9b78f2c0a4dc3197eb61ec8bafbe8141d15138ad` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |
| `xai-pulse` | `fd78686d64ff02b2e730b3839ff7c980c275b7ed` | `1ae6f0698ca1b970dfea51683fedd34977d9548f` |

The five other changed first-party skills (`decision-log`, `devlog-draft`, `handoff-writer`, `mcp-vetting`, `permissions-review`) were checked separately: their existing `source_snapshot_revision` resolves to the same exact SKILL.md blob as PR head, so those revision fields were not changed.

## Macro findings and remaining gates

- **Systemic defect:** provenance revision can silently become stale even when per-manifest verification and consolidated local registry SHA agree. A review must resolve the claimed source revision, not merely compare two recorded fingerprints.
- **Eligibility drift:** nine older pulse records implied standalone import eligibility without explicitly conditioning on security and user fit. Corrected conservatively.
- **Security/behavioral state:** all 21 changed packages remain **not qualified by a complete final-version pinned SkillSpector report**; external behavioral validation remains `not-run`. Historical scanner success, status checks, or static semantic `verified` cannot clear these gates.
- **Independent acceptance:** inspect untrusted source/tool-output handling, private context reads, credential-bearing URLs, authorization for notifications and host scheduling, missing source coverage, and representative adversarial scenarios. The manifest review is static only.
- **Integration:** PR #416 still needs current-main conflict reconciliation and atomic five-surface public accounting before a qualified merge. The 16 provenance edits alone do not change any counts or the public inventory, so no five-surface count update is warranted here.
- **Passive boundary:** no repository runner, script, scanner, CI workflow, scheduler, or background service was added.

**Flow:** 16 provenance files refreshed; nine eligibility labels narrowed; five other source-revision records verified unchanged; zero admissions, zero source-pin moves, zero package-security/behavioral passes. **Merge recommendation:** HOLD until the external security, independent acceptance, and current-main reconciliation gates are satisfied.
