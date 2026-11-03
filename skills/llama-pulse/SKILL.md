---
name: llama-pulse
description: >-
  Scan the latest Meta AI / Llama developments — new open weights, llama-stack
  and cookbook repo activity, research announcements, and r/LocalLLaMA
  reception — and synthesize a digest. Use when the user asks "what's new
  with Llama", "llama pulse", "Meta AI news", "new open weights from Meta",
  or wants open-model awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Llama Pulse
  emoji: "📡"
  version: 1.1.1
---

# Llama Pulse

Vendor pulse for Meta AI's Llama family and its open-weights ecosystem. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check the listed public pages, upstream repos and queries. Substitute the window start date for `{SINCE}` search templates. Cite URLs and publication dates; treat community posts as unverified leads, and report inaccessible or rate-limited sources as gaps. Never expose user context, credentials, secrets or private project text through search queries or other outbound requests. If the host cannot fetch current sources, report an evidence-limited result, not fabricated freshness. **There is no skillz runner, crawler, script, scheduler or background worker.**

2. **Fill gaps.** Fetch the Meta AI blog; run the searches. r/LocalLLaMA is the highest-signal community source for open-weights news — if the Reddit API was blocked, the site-scoped search is mandatory, not optional.
3. **Synthesize.** New weights and licenses first (license terms matter for local deployment); llama-stack/tooling changes; benchmark and quantization chatter.

## Scheduling

- **Optional cadence:** Weekly, only when the user has explicitly authorized this recurring digest. Any scheduling belongs to the external host. One-off research does not authorize repeated checks or outbound notifications.

## Output Format

```
# Llama Pulse — [range]
## New weights & licenses
## Tooling / repo activity (llama-stack, cookbook)
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- License changes on open weights are the deprecation-equivalent here — flag them first.
- Note anything affecting local-runtime model choices (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
