---
name: mistral-pulse
description: >-
  Scan the latest Mistral AI developments — model releases (Mistral,
  Codestral, Devstral, Magistral), API changelog, SDK repo activity, and
  community reception — and synthesize a digest. Use when the user asks
  "what's new with Mistral", "Mistral pulse", "Codestral news", or wants
  European/open-model awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Mistral Pulse
  emoji: "📡"
  version: 1.0.2
---

# Mistral Pulse

Vendor pulse for Mistral AI. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check the listed public pages, upstream repos and queries. Substitute the window start date for `{SINCE}` search templates. Cite URLs and publication dates; treat community posts as unverified leads, and report inaccessible or rate-limited sources as gaps. Never expose user context, credentials, secrets or private project text through search queries or other outbound requests. If the host cannot fetch current sources, report an evidence-limited result, not fabricated freshness. **There is no skillz runner, crawler, script, scheduler or background worker.**

2. **Fill gaps.** Fetch mistral.ai/news and the API changelog; run the searches. Watch both the hosted API line and the open-weights line — they move independently.
3. **Synthesize.** Deprecations/pricing first; new models (note open vs API-only licensing); coding-model changes (Codestral/Devstral matter for agent workflows); community sentiment.

## Scheduling

- **Optional cadence:** Weekly, only when the user has explicitly authorized this recurring digest. Any scheduling belongs to the external host. One-off research does not authorize repeated checks or outbound notifications.

## Output Format

```
# Mistral Pulse — [range]
## Releases & API changes (deprecations FIRST; open vs API-only noted)
## Repo activity
## Community reception
## Notable patterns
## Sources
```

## Notes

- Read-only: this skill fetches and reports; it never posts, subscribes, or mutates anything.
- Official sources are authoritative; community commentary is signal, not truth.
- As an EU vendor, Mistral compliance/regulatory positioning items also feed governance-pulse — cross-reference, don't duplicate.
