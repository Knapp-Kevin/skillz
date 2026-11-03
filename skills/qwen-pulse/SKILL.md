---
name: qwen-pulse
description: >-
  Scan the latest Qwen (Alibaba) developments — new open weights, QwenLM
  org repo activity, blog posts, and r/LocalLLaMA reception — and
  synthesize a digest. Use when the user asks "what's new with Qwen",
  "Qwen pulse", "new Qwen model", or wants open-model awareness alongside
  the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Qwen Pulse
  emoji: "📡"
  version: 1.1.1
---

# Qwen Pulse

Vendor pulse for Alibaba's Qwen family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the date for `{SINCE}` in search templates. Cite exact URLs and publication dates; treat community posts as leads to verify and report inaccessible or rate-limited sources as gaps. Never send secrets, user memory or private project data in public queries. If live sources cannot be checked, disclose missing evidence rather than claiming freshness. **skillz provides no runner, crawler, script, scheduler or background service.**

2. **Fill gaps.** Fetch the Qwen blog and Hugging Face org page (weights often land there first); run the searches. QwenLM org activity is broad — filter to model releases, agent tooling (qwen-code), and inference kernels.
3. **Synthesize.** New weights/licenses first; agent-tooling changes; community benchmarks and quantization results.

## Scheduling

- **Optional cadence:** Weekly only with explicit user authorization for this specific recurring digest; external host scheduling only. A one-time request does not authorize repeated checks or notifications.

## Output Format

```
# Qwen Pulse — [range]
## New weights & licenses
## Tooling / repo activity (qwen-code, kernels)
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede blog posts — treat the org page as a primary source.
- Note anything affecting local-runtime model choices (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
