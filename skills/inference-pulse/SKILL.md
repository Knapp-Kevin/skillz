---
name: inference-pulse
description: >-
  Scan the local-inference runtime ecosystem — llama.cpp, Ollama, and
  vLLM releases and breaking changes, quantization format shifts (GGUF),
  and GPU/NPU support movements — and synthesize a digest with a
  relevance verdict for the operator's bound local-runtime target. Use
  when the user asks "inference pulse", "what's new in llama.cpp",
  "local inference news", "GGUF changes", or wants runtime awareness
  for local-inference work.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Inference Pulse
  emoji: "🧠"
  version: 1.1.1
---

# Inference Pulse

Topic pulse for local-inference runtimes — llama.cpp, Ollama, and vLLM.
Local runtimes ride these upstreams, so breaking changes,
quantization-format shifts, and GPU/NPU support moves land here first;
every digest ends with a relevance verdict for the bound local-runtime
target. **Bind:** discover the operator's local-runtime target from an
operator profile, project governance doc, or host memory — the bound
source is authoritative over assumptions; when none exists, the verdict
goes generic (relevance to a typical local-inference stack) and the
skill offers to bind a target for next time.

## Execution Flow

1. **Collect (external host only).** Read the bundled `sources.json` beside this skill. For the requested time window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the start date for `{SINCE}` where present. Cite source URLs and publication dates, distinguish official reports from community leads, and report inaccessible or rate-limited sources as gaps. Never put private context, credentials or tokens in public queries. If access is unavailable, provide an evidence-limited result, not invented freshness. **skillz has no runner, crawler, script, scheduler or background job.**

2. **Fill gaps.** Fetch the llama.cpp releases page and the Ollama/vLLM
   blogs directly if the host's source coverage is thin; run the searches,
   especially for quantization-format and NPU support news.
3. **Synthesize.** Breaking changes first (removed flags, API breaks,
   GGUF version bumps, with migration impact); then runtime releases;
   then quantization/hardware movements; end with a one-line relevance
   verdict for the bound runtime target.

## Scheduling

- **Optional cadence:** Weekly, only if the user authorizes this recurring digest. A scheduled task belongs to the external host. A one-time request never authorizes recurring checks or notifications.

## Output Format

```
# Inference Pulse — [range]
## Breaking changes (migration impact stated)
## Runtime releases (llama.cpp / Ollama / vLLM)
## Quantization & hardware (GGUF, GPU/NPU)
## Runtime relevance (bound target): <one line>
## Sources
```

## Notes

- llama.cpp moves fastest and breaks most; its releases are the hard source.
- Verdicts inform the bound runtime's planning; adopting an upstream change stays a
  user decision, not an automatic upgrade.
