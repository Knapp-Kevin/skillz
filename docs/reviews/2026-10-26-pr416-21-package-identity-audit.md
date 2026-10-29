# PR #416: current 21-package exact-manifest identity audit

**Observed UTC date:** 2026-10-27 (session local date 2026-10-26). **PR head checked before writing:** `5b1b83c459358f0be90a03ed66b19cd06006e9f3`. **Target:** PR #416 (`fix/415-passive-pulse-collection`). **Method:** read-only GitHub file retrieval and comparison of each changed first-party `SKILL.md` Git blob SHA, its `registry/verification/local-skills/<name>.yaml` `content_blob_sha`, and the corresponding `registry/local-verification.json` entry. Individual provenance companion `review_status` was inspected as a fourth status surface. This is not a complete package-tree hash or security scan.

## Results

**21 / 21 exact SKILL.md blob identities agree across all three evidence locations.** All 21 individual records and the consolidated registry report semantic `verified`; all 21 provenance companions report `verified-structured`. These are *record-consistency observations*, not a new semantic qualification, a package security pass, or evidence that the review's rubric findings were independently repeated. The branch's recorded external behavioral state remains `not-run`.

| First-party skill | Git blob SHA from live branch | Manifest ↔ individual ↔ consolidated |
|---|---|---|
| `decision-log` | `3e1ceeb3a20e2d933e5ade631e82d54dd582a44b` | Match |
| `deepseek-pulse` | `2aadd8f5d190e3b4ae91cf5877a09ef25ee33304` | Match |
| `devlog-draft` | `e7f6456fafbe4b432270696d64e3685a8ca8725a` | Match |
| `gemini-pulse` | `36b460f40471134da8e13c16d707b6d17f3004a1` | Match |
| `github-pulse` | `587313bab488dc27411f9e52c1c43516dc8f26f4` | Match |
| `glm-pulse` | `5a0414e6d8bda0433d5fbedbde734b8369a25f6c` | Match |
| `governance-pulse` | `0709d2f3392b5e63f1e91b98e805cb0e13a95d14` | Match |
| `handoff-writer` | `b60a41bc26348370eb61a60b9c1287f29044e92c` | Match |
| `hf-pulse` | `38387fea604b6eb7d9e81b1e449b36f8ca1fc30c` | Match |
| `inference-pulse` | `6c676b7e9e45e82504d84fa4bbd56682830660b8` | Match |
| `kimi-pulse` | `4c953878c4c02183d819e94a89462c151bef2f44` | Match |
| `llama-pulse` | `818a0d1d9a2225a6ae311eba6b4f19955558a1af` | Match |
| `mcp-pulse` | `23e62f52dbfdf657106c9f8212a3be3ce312849f` | Match |
| `mcp-vetting` | `aa79354448d800c97c577a74b1bc13f97c4c550c` | Match |
| `memory-pulse` | `7d0404768a982758ce3bbbf80aadb561b41957e2` | Match |
| `mistral-pulse` | `81e2d64d29af4fa3ac1fc6aeeda38166ec5bed11` | Match |
| `openai-pulse` | `cfb234de2003eb1024b8e4d7dd7c3172c80e1718` | Match |
| `permissions-review` | `8e7719b68f4c125fb256d72203841dd4064a9fd0` | Match |
| `perplexity-pulse` | `4426e6744badf1f77c552fb50aa807a464b8ab8b` | Match |
| `qwen-pulse` | `9b78f2c0a4dc3197eb61ec8bafbe8141d15138ad` | Match |
| `xai-pulse` | `fd78686d64ff02b2e730b3839ff7c980c275b7ed` | Match |

## Macro risk and integration boundaries

- Sixteen pulse manifests replace a removed repository runner with **host-operated** source retrieval; the other five amended skills concern logging, drafting, handoff, MCP vetting, and permissions review.
- `sources.json` remains untrusted data and cannot provide tool/action authorization; private project context, host configuration, credentials, logs, and scheduled/report-delivery operations require specific host-side approval where applicable.
- `registry/local-verification.json` reports semantic review state only. Do **not** infer scanner coverage or success from a matching SHA, absence of reported findings, a prior scanner receipt, or zero GitHub workflow checks.
- The registered security policy requires NVIDIA SkillSpector **v2.12.0**, exact commit `c7958a3268d9498644b22edb75d0f051bbc8cbfc`, in an authorized external host with appropriate static-only settings and complete, fail-closed package coverage. This session's local environment has no installed `skillspector` and cannot resolve `github.com`, so no qualifying run was attempted or claimed.
- When the external scanner becomes available, assess **the final exact *complete package*** for each of these 21 files, including bundled source lists and references, with receipts and content/report digests under `registry/security/`. Recheck identities if PR head changes before accepting evidence.
- The PR remains **draft and merge blocked** until complete current-version package-security evidence plus independent acceptance are established. Mergeability does not imply readiness.

## Accounting and effect

This audit modifies no skill or package content, source pin, score, admission disposition, or public catalog totals. Count delta: 0 first-party, 0 third-party review companions, 0 registered sources, 0 pinned corpora. Five public accounting surfaces remain unchanged. No repository runtime, CI, script, scanner, scheduler, or execution mechanism is introduced.
