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
  version: 1.1.0
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

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/inference-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read
   `sources.json` beside this file and fetch/search those sources
   directly with web tools.

2. **Fill gaps.** Fetch the llama.cpp releases page and the Ollama/vLLM
   blogs directly if the engine's coverage is thin; run the searches,
   especially for quantization-format and NPU support news.
3. **Synthesize.** Breaking changes first (removed flags, API breaks,
   GGUF version bumps, with migration impact); then runtime releases;
   then quantization/hardware movements; end with a one-line relevance
   verdict for the bound runtime target.

## Scheduling

- **Claude Code:** `/schedule` weekly — runs alongside the other pulses
  (mcp-pulse, github-pulse); cross-reference, don't duplicate.

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
