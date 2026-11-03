---
name: glm-pulse
description: >-
  Scan the latest z.ai / Zhipu GLM developments — new open weights, org
  repo activity (zai-org, THUDM), API and coding-plan changes, and
  r/LocalLLaMA reception — and synthesize a digest. Use when the user asks
  "what's new with GLM", "GLM pulse", "z.ai news", "Zhipu update", or wants
  open-model awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: GLM Pulse
  emoji: "📡"
  version: 1.1.1
---

# GLM Pulse

Vendor pulse for z.ai (Zhipu) and the GLM family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read the bundled `sources.json` beside this skill. For the requested time window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the start date for `{SINCE}` where present. Cite source URLs and publication dates, distinguish official reports from community leads, and report inaccessible or rate-limited sources as gaps. Never put private context, credentials or tokens in public queries. If access is unavailable, provide an evidence-limited result, not invented freshness. **skillz has no runner, crawler, script, scheduler or background job.**

2. **Fill gaps.** Check both GitHub orgs (releases have moved between THUDM and zai-org) and the Hugging Face org page — weights often land there before the blog post. Run the searches; the coding-plan/API-pricing one matters because GLM competes aggressively on price.
3. **Synthesize.** New weights/licenses first; API and coding-plan pricing moves (these shift agent-runtime economics); agent/coding tooling; community benchmarks.

## Scheduling

- **Optional cadence:** Weekly, only if the user authorizes this recurring digest. A scheduled task belongs to the external host. A one-time request never authorizes recurring checks or notifications.

## Output Format

```
# GLM Pulse — [range]
## New weights & licenses
## API & pricing moves
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede announcements — treat the org page as a primary source.
- Note anything affecting local-runtime model choices or coding-agent cost baselines (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
