# Three useful skill ideas, with their limits

**This is our first small set of positive recommendations.** They are ideas worth learning from, **not** skills we recommend installing or running unchanged. We picked each for a different practical benefit and checked the original pinned files, supporting material, license and known risks.

| If you need to… | Study this method | Why it's worth your time |
|---|---|---|
| Build 3D models that fit together | **[Blender Assembly Pitfalls](https://github.com/dcc-mcp/dcc-mcp-blender/blob/8d8027fe4377b4d399d545869fc11b80e04ff785/skills/dcc-blender-assembly-pitfalls/SKILL.md)** | Make a connection map before building; verify sizes, axes and joint overlap afterwards |
| Test an interactive game story | **[IF Playtest Review](https://github.com/bladecoder/narrative-skills/blob/c0948f7970178b72bb9561030372e75d303d37b3/skills/if/if-playtest-review/SKILL.md)** | Catch impossible paths, stuck players, unreachable endings and states that never match |
| Fix audio CPU spikes and dropouts | **[Audio Performance Debug](https://github.com/kunitoki/sonic-skills/blob/8b6dcfe89030d7de9ba9d6afcc2d927fb11fe7fa/skills/audio-performance-debug/SKILL.md)** | Measure a real symptom, isolate the audio-thread hotspot, then verify a fix instead of guessing |

## Why each is a valuable reference, not ready for unchanged use

### 3D modeling: Blender Assembly Pitfalls

**Unique idea:** Record which faces must meet, their expected overlap and the direction of each part *before* generating geometry. Then check actual world-space boundaries and axes, rather than trusting parameters or a screenshot.

**Important warning:** The example script clears all objects in its Blender scene. Running it in a live project could erase work, and its volume calculation is only suitable as a basic sign check. The upstream author reports Blender 4.5.13 measurements, but we did not execute that example. Use the connection-map concept, not the raw script.

**Evidence:** Q4 static review **18/20**; pinned `dcc-mcp/dcc-mcp-blender@8d8027fe`; exact SKILL.md blob `32bbb06a`; root **MIT**, with copyright/notice obligations. [Individual review](../registry/discovery/q4-dcc-mcp-dcc-mcp-blender-static-20261103.json).

### Game design: IF Playtest Review

**Unique idea:** Check both directions of the game-state contract. A clue must exist where it is needed, and every state named in the game should have a matching definition. Record routes, circular locks and failed paths, then classify severity.

**Important warning:** The original expects a specific Ink project layout and writes review files; its route search is not bounded for large branching stories. A compiler run and file writes require the user's actual project and approval. Borrow the method or adapt it to another game system.

**Evidence:** Q1 static review **16/20**; pinned `bladecoder/narrative-skills@c0948f79`; SKILL.md `e703f3c5`; root **MIT**, with notice preservation. [Individual review](../registry/discovery/q1-bladecoder-narrative-skills-static-20261103.json).

### Testing: Audio Performance Debug

**Unique idea:** First classify the glitch, then measure a reproducible optimized build and the specific audio thread. Compare CPU spikes, voice counts and buffer deadlines before changing code, and re-measure after changes.

**Important warning:** Some bundled SIMD examples fail to handle leftover samples and may overrun buffers. Other example logging and processor details need platform-specific checks. Treat the measurement approach as valuable; do **not** transplant its code examples unchanged.

**Evidence:** Q5 static review **16/20**; pinned `kunitoki/sonic-skills@8b6dcfe8`; SKILL.md `15c46481`; root **Unlicense** dedication. Check third-party rights before copying snippets. [Individual review](../registry/discovery/q5-kunitoki-sonic-skills-static-20261103.json).

## What this does and doesn't count

Three **distinct, positively endorsed Valuable Reference examples** from three different domains. **Zero Recommended for Use entries in this starter set.** We have **not** established global counts, or that the other 30 domains lack useful skills. Each package has static source-vetting evidence, but **security scanning and hands-on behavioral validation were not run**.

The source-neutral [structured reference catalog](../registry/consumer-positive-references-20261103.json) includes exact pins, file hashes, supported mechanisms, limits, licensing and evidence. Other candidates, rejected packages and historical decisions stay in the broader research archive.
