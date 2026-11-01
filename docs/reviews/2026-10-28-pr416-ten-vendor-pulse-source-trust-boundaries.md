# PR #416: Ten vendor-pulse untrusted-source boundary repairs (2026-10-28)

## Scope and macro map

Independent read of the ten vendor pulse manifests and their ten bundled `sources.json` files at draft PR head `13de44fad71c3a906e0b8fba441e11488a5c5569` established one shared omission: the manifests directed hosts to fetch untrusted third-party pages, Reddit discussions, repositories, and search output without consistently saying that retrieved instructions have no authority. The source lists were all parseable JSON and remain unchanged. This is a coherent existing-first-party revision tranche, not ten new skills or a source admission.

The previous PR had already removed the nonexistent repository runner. This tranche retains its host-only retrieval, public source lists, use cases, output formats, optional user-authorized scheduling, and existing individual static scores. It adds a common explicit untrusted-source and private-data boundary after the `Execution Flow` heading in each of the ten complete manifests.

## Individual exact-version static decisions

All ten have **VERIFIED semantic-only**, **16/20** (unchanged score after complete-manifest read), `validation_status: not-run`, and no qualifying final-package security evidence. The exact content identities below were read back from the detached manifest commit `014b61b9da005d4665b391c45258f911faf39c51`. The provenance source revision for each is that manifest commit, not this evidence commit.

| Package | Exact new SKILL.md Git blob | Specific source/risk context | Disposition |
|---|---|---|---|
| deepseek-pulse | `1fc968fb94bfcd3618fda085b08cf0cd21d4c23e` | Model weights, arXiv and Reddit claims; reject embedded instructions | VERIFIED semantic only |
| gemini-pulse | `69b1b4dd1ba164308f755629510b2043eb358e61` | API changelog, DeepMind blogs and community content; no Qor host assumption | VERIFIED semantic only |
| glm-pulse | `7c7f92832f42e7cfdafe36da087b1e634ab060b6` | Vendor price/coding-plan claims and Hugging Face weights; corroborate primary sources | VERIFIED semantic only |
| kimi-pulse | `eefd3337a2875fef8251a4478b391a75318fa694` | Agentic benchmark claims, public model repositories and Reddit | VERIFIED semantic only |
| llama-pulse | `3f0bd40adde01d1855b557c0f62f5e0eb28b0a7e` | Weight-license conditions and community performance claims | VERIFIED semantic only |
| mistral-pulse | `23bbc1a8f7f8ecd5af2db7d5cf5ebea3488640ce` | API-only versus open-weight licensing and release claims | VERIFIED semantic only |
| openai-pulse | `7344d2e431afad9e0fde6e179ed14517ec00b8a0` | Public API/release notes and community sentiment; incidental Warp repo in source list is not evidence of OpenAI ownership | VERIFIED semantic only |
| perplexity-pulse | `38eeae61d87c292aeffc4f32bd038b7862d9b6b6` | API/product announcements; Sonar is only an optional external-host capability | VERIFIED semantic only |
| qwen-pulse | `f56496f4ca0bcd7969d5e5d3fe308d8a45ba251e` | Hugging Face weights, model releases and Reddit discussions | VERIFIED semantic only |
| xai-pulse | `ad904ae0b35fd605780c0ffaa856a2da3606394c` | Official API news versus noisy public/community claims | VERIFIED semantic only |

## Authorization, dependencies and validation

- **Authority:** read-only public information retrieval and synthesis. The new boundary refuses source-supplied commands, installation, settings changes, credential requests, private-context disclosure, messaging and scheduling. Reading private/gated material or transmitting workspace context requires distinct, source-specific authorization. Subsequent user-facing actions require their own authority.
- **Dependencies:** each unchanged bundled `sources.json` plus whatever approved public browsing/search capability the external host actually has. No repository-owned runtime, fetcher, runner, scheduler, scanner, monitor, tests, or CI.
- **Provenance:** ten individual first-party companions bind `source_snapshot_revision` to the manifest commit. Ten verification companions and the 44-entry consolidated registry bind to the exact ten new Git blob SHA values. Existing controlled tags and source identity are unchanged.
- **Evidence:** ten complete manifests and ten JSON source lists were read; JSON parse passed for 10/10. Static semantic review only. No external pages were fetched for this tranche, no scanner executed, no behavioral/adversarial host scenario executed, no package-security pass inferred, no score inflation, and no adoption claim.

## Macro findings and gates

This closes the specific missing instruction-boundary pattern across the ten vendor pulses. It does not resolve the independent final-package SkillSpector and adversarial/integration acceptance gates for **all 21** changed packages in PR #416. The new ten blob identities invalidate any prior scan on earlier package versions. First-party inventory remains **44**, third-party review companions **826**, total YAML **870**, registered source identities **22**, and admitted-source denominators unchanged; therefore the five public accounting surfaces require no count change. Keep PR #416 draft until full final-version qualification and independent acceptance.
