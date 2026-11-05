# Two Cloudflare skill mirrors: exact package and rights reconciliation

Date: November 4, 2026. Issue: #624. This is a **read-only pinned identity and license analysis**, not a new quality grade, source admission, security scan, observed behavior, or approval for unchanged installation.

## Exact publisher pins and provenance

- Official source: `cloudflare/skills` at `f96bff754e428838818017f75817f0f9428acd48`. This is the existing `skills/sources/cloudflare-skills` **Git submodule** pin, not ordinary files copied into the parent repository. The source's full root `LICENSE` blob is `7a4a3ea2424c09fbe48d455aed1eaa94d9124835`, containing Apache License version 2.0 including its patent provisions. `skillz` provenance describes these skills as Apache-2.0.
- Alternate discovery source: `openai/plugins` at `0722921d5542fc593105c27bd52630babd8b8c2a`, under `plugins/cloudflare/skills/`. The plugin's `.codex-plugin/plugin.json` blob `bd6458b16d83a29231f5ef7b3f405ce090611982` states `license: MIT`. **That metadata cannot be used to infer that unchanged upstream Apache-2.0 instructions/references were relicensed or that unrelated plugin files share those exact terms.** Preserve the original upstream terms and any separate plugin-layer obligations.

## Exact bytes, not just shared skill names

| Skill | Core files compared | Cloudflare pinned package tree | OpenAI plugin package tree | Plugin-only extra |
|---|---:|---|---|---|
| Durable Objects | **4/4 identical Git blob SHAs** | `72810f48414f2e68d0aa65a8895f749c959dea91` | `cf3ced5c811c71da7d5dc546e7c526ffaf6571bc` | `agents/openai.yaml` (`d0cf1c8b80d69a3a4c0213ac9c4ee3fbb471c484`) |
| Workers Best Practices | **3/3 identical Git blob SHAs** | `7dd384e79c76d3e388dfe53e12e93642679ff1fd` | `fbf60b5122db35fa71d21ef98ce1b3539ec9d3c0` | `agents/openai.yaml` (`7c5f663cbe59ff03612c84addce3ede543ad20cb`) |

For Durable Objects, the four matching files are `SKILL.md`, `references/rules.md`, `references/testing.md`, and `references/workers.md`. For Workers Best Practices, the three are `SKILL.md`, `references/review.md`, and `references/rules.md`. Both comparisons use the complete recursively enumerated Git package trees at the exact pins; neither Git tree was truncated. There were **zero mismatched core files**, zero missing upstream files, and exactly one extra plugin-wrapper file per mirror.

Both additional `agents/openai.yaml` files were read. They contain only `interface.display_name` and `interface.short_description`. No tools, shell commands or authorization changes appeared in those two metadata files. This is a *specific static observation*, not a scanner or runtime-behavior result. A plugin-level `.mcp.json` integration or platform-installed capability is **outside** these individual skill package trees and cannot be implicitly admitted from this comparison.

## Accurate decision

1. **Equivalent core instruction/reference content, different complete packages.** Distinct package trees remain distinct source identities. Do not inflate distinct useful capabilities by counting the same mechanism twice.
2. **Keep exact-source evidence linked, not duplicated.** The existing governed Durable Objects source review is 17/20 `verified` as a Cloudflare-specific first-party-published package. It is **not** an automatic unchanged-use grade for the plugin wrapper; required authorizations and host environment remain consumer-specific. The governed Workers Best Practices review is **14/20 REJECT unchanged** for unapproved telemetry/secret-mutation advice. This rejection also applies as a warning to the byte-identical plugin core; the extra display metadata does not fix that issue.
3. **Rights follow the content.** Cloudflare's Apache-2.0 source license and notice obligations remain relevant to the identical core bytes even where the plugin manifest displays MIT. Do not claim MIT-only terms for these mixed-layer packages, silently vendor them, or replace the official license.
4. **Security and observed behavior remain independent.** Both plugin package trees need exact-tree security treatment if ever considered for unchanged use. No new scan, host behavior, execution, installation, or user-account connection took place.
5. **No numerator inflation.** The four-source raw-path count stays 4,813 and the governed-record count stays 1,039 as independently defined populations. These two mirrors add **zero** new graded independent skill methods or unchanged-use approvals; the global distinct eligible denominator remains unknown.

This narrows #624's identity/rights blocker for **two exact mirrors**, but does not establish full four-source-to-governed crosswalk completion or demonstrate measured review throughput. Historical source and candidate records are preserved.
