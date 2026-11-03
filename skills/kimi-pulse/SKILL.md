---
name: kimi-pulse
description: >-
  Scan the latest Moonshot AI / Kimi developments — new open weights (K2
  line), org repo activity, API changes, and r/LocalLLaMA reception — and
  synthesize a digest. Use when the user asks "what's new with Kimi",
  "Kimi pulse", "Moonshot news", "Kimi K2 update", or wants open-model
  awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Kimi Pulse
  emoji: "📡"
  version: 1.0.1
---

# Kimi Pulse

Vendor pulse for Moonshot AI's Kimi family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check the listed public pages, upstream repos and queries. Substitute the window start date for `{SINCE}` search templates. Cite URLs and publication dates; treat community posts as unverified leads, and report inaccessible or rate-limited sources as gaps. Never expose user context, credentials, secrets or private project text through search queries or other outbound requests. If the host cannot fetch current sources, report an evidence-limited result, not fabricated freshness. **There is no skillz runner, crawler, script, scheduler or background worker.**

2. **Fill gaps.** Check the MoonshotAI GitHub org and Hugging Face org page (weights land there first); run the searches. Kimi releases tend to arrive with strong agentic/tool-use claims — pull the community benchmark threads to test them.
3. **Synthesize.** New weights/licenses and agentic capabilities first; API/pricing changes; community verification of benchmark claims.

## Scheduling

- **Optional cadence:** Weekly, only when the user has explicitly authorized this recurring digest. Any scheduling belongs to the external host. One-off research does not authorize repeated checks or outbound notifications.

## Output Format

```
# Kimi Pulse — [range]
## New weights, licenses & agentic claims
## API & pricing changes
## Community reception (benchmark verification)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede announcements — treat the org page as a primary source.
- Kimi's agentic/tool-use positioning makes it directly relevant to coding-agent model choices — flag head-to-head results against Claude/GPT/GLM when the community produces them.
