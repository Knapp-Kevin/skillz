# PR #673: nine unchanged-tree pulse packages, current exact-version semantic review

Date: 2026-11-04. **Static reviewer assessment, not host-executed behavior, not a new SkillSpector scan, and not approval to use unchanged.** The nine source procedures were changed from old runner-based instructions to host-native public source collection. Their historical 2026-08-30 rubric scores were previously correctly marked `stale`; this review evaluates their **current** complete packages rather than copying old grades.

## Package and rights scope

All nine packages are first-party, under the complete root MIT license (`LICENSE` blob `023abdb34298b27580d1d303084aca942050585e`). Each package consists of precisely `SKILL.md` plus a bundled `sources.json`, both read directly from PR #673's exact source revision. Each JSON source file parsed and contained public URLs, provider GitHub repositories/orgs and generic searches; no executable sidecars, repository-owned jobs, scripts or credentials were bundled. Current **two-file Git package trees** were independently recalculated from the two Git blob SHAs using Git's canonical tree hashing and matched the existing 9/9 pinned external-scan package identities exactly.

| Skill | SKILL.md Git blob SHA | sources.json Git blob SHA | Exact Git package tree SHA |
|---|---|---|---|
| deepseek-pulse | `63be9ffb787e29e7c9d53a4111c817f660d0c943` | `0acf86aa545c6c519ee95e364226badca5f32bda` | `8984411410ccae81474a93e53c28a180ff61ec25` |
| gemini-pulse | `9dbae1510d0fb3c65056fc53f0050ce0ed6ede59` | `02a7017d93b20f13392bdb0343d22ad3d5ebf440` | `ff5d73b1208b6faafe7eecdc7d0b67daa3c78a29` |
| glm-pulse | `79e2e3b384ee707871122fa70d5fb3651c0511e6` | `741b61992356dc6a7ee2063fe54765b93fc3c039` | `7974b0f1957fec72a823e43b5c6985abfb9a937c` |
| llama-pulse | `c0c38b0dd182f1f588d1800b832b331c8572080e` | `14b89191a00a7e1ffccb28ab47c32b1a5a84acdb` | `53dbd090ce88c406296ff84fce4faa61534044cd` |
| mistral-pulse | `5695a01a8d7927f87be7da76ec353d12ef56ddb9` | `760e8d731d00ff99ac8eb7405ab7da9390745c43` | `0460d0ae30d98e8013eb41f5f86668af6acec2d1` |
| openai-pulse | `1285b1226733e93b0db4b230a6fb0021e5220fd0` | `7453e54b0fd67f2fbf6ca8bad4e6f0e569b59a3b` | `e7d287f0f6f280b45196205cbd0d71e9c69274ed` |
| perplexity-pulse | `06906792509a41a3a9cbb641e02f47e9fb458a69` | `a7dc203a87bbb6eab1ccbbe40583c5f90eb74d46` | `2929295240f02db18afc52eeb44a8d3c30ec8346` |
| qwen-pulse | `03d3015bbfe571ddaf4fa9448de66f74bb62ce69` | `304be9866f211cec086f5479af9d872cac7d84b4` | `e328cb591e98f994d2646bae448cb779c6adee06` |
| xai-pulse | `58dcef43210c4ddb09f4a7ad7273d99516e42813` | `f3608fb81efd181a91ecf2c72b73930e073ab67f` | `b389f8de77dc95b207e650e4a5ca2ff5caf3cc41` |

## Ten-axis current-source rubric

Scores follow `docs/skill-verification.md`, with 0 deficient, 1 constrained, 2 strong. Axis order: **trigger, procedure, authority, failure, evidence, dependencies, portability, differentiation, adversarial resilience, effectiveness design**.

| Skill | Ten individual axis scores | Score | Individual evidence and limits |
|---|---|---:|---|
| deepseek-pulse | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Clear DeepSeek model/weight, paper, pricing and license focus; checked public HF and docs search templates; lacks observed rate-limit/freshness behavior |
| gemini-pulse | 2,2,1,1,2,2,2,2,2,1 | **17/20** | API deprecations, Google/DeepMind releases and SDK changes are well scoped. Final host-specific Qor reference must never imply permission to inspect private host configuration; cross-project relevance stays constrained |
| glm-pulse | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Explicit public z.ai, THUDM and HF source families; prioritizes weights, coding-plan pricing and verified community claims; no observed failure handling |
| llama-pulse | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Distinguishes license changes and API/tool releases; source includes a site-search fallback for blocked Reddit API, but actual host reachability is untested |
| mistral-pulse | 2,2,2,1,2,2,2,1,2,1 | **17/20** | Legitimate distinct API-only vs open-weight and EU vendor angle; much of the step sequence overlaps the generic vendor digest and remains effectiveness-unmeasured |
| openai-pulse | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Strong source/date boundaries and explicit deprecations, API changes and Codex-related repo coverage; no assertion that unread JS-rendered changelog pages were fetched |
| perplexity-pulse | 2,2,2,1,2,2,2,1,2,1 | **17/20** | Distinguishes Sonar model/API and Comet product news, but mostly follows generic public vendor-research procedure; no model-tested advantage |
| qwen-pulse | 2,2,2,1,2,2,2,2,2,1 | **18/20** | Specific QwenLM/HF open weights, licenses, coding tools and inference kernels; vendor community evidence kept separate from official release claims |
| xai-pulse | 2,2,2,1,2,2,2,1,2,1 | **17/20** | Separates vendor official releases from noisy community commentary; relatively narrow reusable method, with no observed proof of improved outcomes |

### Shared boundary analysis, not behavioral evidence

For each package, source text explicitly disallows secret/private-context egress, unauthorized schedules, installs, writes and external notifications; a public digest remains read-only and one-time. Each calls external source content untrusted evidence, not commands. The optional scheduling section requests separate user approval for exact scope, time, recipient, cost, retention and revocation. When connectors/search fail, instructions require reporting evidence gaps instead of fabricating freshness. No unresolved **source-text** hard fail was found within these nine complete current package trees. The current rubrics meet >=15/20 and trigger/authority/dependency >=1.

This is **not** a successful agent-host test: no agent consumed the skills under malicious fixtures; no unapproved tool attempt was observed or ruled out. The existing **9 exact-tree external NVIDIA SkillSpector PASS receipts** may remain associated with these same unmodified two-file trees, but do **not** establish behavioral validation or unconditional import. The separate Memory Pulse 1.1.3 privacy repair is reviewed in `docs/reviews/2026-11-04-issue402-memory-pulse-113-authority-review.md` and explicitly **lost** its old exact-tree scanner PASS.

## Qualification disposition

Mark these nine **semantic `verified`** at their listed exact current source blobs with their new per-source rubric reasons. Preserve behavior `not-run`, prior external scanner receipt identity without relabeling the scan date, and conditional unchanged-use status. The six earlier changed/failed-or-incomplete pulse packages have their own current semantic review; Memory Pulse 1.1.3 has a separate 18/20 current review. None of the 16 is behaviorally accepted. PR #673 remains DRAFT until seven unmatched package-tree scans, all independent host adversarial runs, owner acceptance, and shared-registry integration are done. Issues #415/#402 stay OPEN.
