# Seven useful skill ideas, with their limits

**These are seven positive recommendations across seven different capability areas.** They are ideas worth learning from, **not** skills we recommend installing or running unchanged. We picked each for a different practical benefit and checked the original pinned files, supporting material, license and known risks.

| If you need to… | Study this method | Why it's worth your time |
|---|---|---|
| Build 3D models that fit together | **[Blender Assembly Pitfalls](https://github.com/dcc-mcp/dcc-mcp-blender/blob/8d8027fe4377b4d399d545869fc11b80e04ff785/skills/dcc-blender-assembly-pitfalls/SKILL.md)** | Make a connection map before building; verify sizes, axes and joint overlap afterwards |
| Test an interactive game story | **[IF Playtest Review](https://github.com/bladecoder/narrative-skills/blob/c0948f7970178b72bb9561030372e75d303d37b3/skills/if/if-playtest-review/SKILL.md)** | Catch impossible paths, stuck players, unreachable endings and states that never match |
| Fix audio CPU spikes and dropouts | **[Audio Performance Debug](https://github.com/kunitoki/sonic-skills/blob/8b6dcfe89030d7de9ba9d6afcc2d927fb11fe7fa/skills/audio-performance-debug/SKILL.md)** | Measure a real symptom, isolate the audio-thread hotspot, then verify a fix instead of guessing |

| Make government forms work for everyone | **[Singapore DSS Accessibility](https://github.com/kyleoliveiro/sg-gov-skills/blob/16892fc613263c3f835457cd23ae092d404979ca/skills/sg-gov-dss-accessibility/SKILL.md)** | Check keyboard use, screen-reader labels, forms, and contrast before launch |
| Troubleshoot blocked Kubernetes traffic | **[NetworkPolicy Debug](https://github.com/scitix/siclaw/blob/ceee3f49f8bdc9223c0a2b0afec33253f95616f9/skills/core/networkpolicy-debug/SKILL.md)** | Narrow down network rules before considering any change to a live cluster |
| Explain your service clearly | **[Singular Positioning Clarity](https://github.com/peterod99/consultant-skills/blob/ee82a9dfe327a734e815a590aaaf92327d111d85/singular-positioning-clarity/SKILL.md)** | State who you help and what changes in one sentence people can repeat |
| Organize a long voice note | **[Split Transcript by Intent](https://github.com/danielrosehill/Claude-Transcription-Plugin/blob/d19d6df5792490b477d9ea6fd4f7eebb0434dc9d/skills/split-transcript/SKILL.md)** | Separate decisions, tasks, background and instructions without losing words |

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

### UX / UI: Singapore DSS Accessibility

**Unique idea:** Check accessibility while building the page, not only when it is finished. Link each finding to a specific control and use three kinds of testing: automated checks, keyboard navigation and assistive technology.

**Important warning:** Singapore's official requirements can change, and the mapping to WCAG is partly the author's inference. The original package includes government-published control text whose reuse rights are **not** covered by the source's MIT license. One evaluation expects a different control family. Do not use this package unchanged to certify legal or policy compliance.

**Evidence:** Q2 static review **18/20**; `kyleoliveiro/sg-gov-skills@16892fc6`, SKILL.md `ec0e8e20`; source-authored content **MIT**, official control text has separate rights. [Individual review](../registry/discovery/q2-kyleoliveiro-sg-gov-skills-static-20261103.json).

### Cloud / DevOps: NetworkPolicy Debug

**Unique idea:** Follow the blocked connection in both directions. Check which policies select each pod, how allow rules combine, whether DNS can leave the pod, and whether the network provider adds special rules.

**Important warning:** Some details about host-network pods and Cilium/Calico rule order are too broad. Reading a real cluster requires the user's permission and live checks must not create pods or change firewall rules without separate approval. The source is **Apache-2.0**, not MIT. We corrected this mislabeled license in all **28** source-family review records.

**Evidence:** Q4 static review **17/20**; `scitix/siclaw@ceee3f49`, SKILL.md `4a80dcb3`, original root LICENSE `7c9ea9eb`; **Apache-2.0** with license and modification-notice requirements. [Individual review](../registry/discovery/q4-scitix-siclaw-static-20261103.json).

### Marketing: Singular Positioning Clarity

**Unique idea:** Make a one-sentence description of who you serve and the result they get. Check whether someone can repeat it, it clearly excludes the wrong work, and you can defend the claim.

**Important warning:** Some impressive sales results in its example are unverified. The original draws on named third-party books and courses; the source author's MIT license does not relicense their protected language. Borrow the simple questions, not the anecdotal success claims.

**Evidence:** Q4 static review **16/20**; `peterod99/consultant-skills@ee82a9df`, SKILL.md `31e85f5f`; root **MIT** with separate third-party rights. [Individual review](../registry/discovery/q4-peterod99-consultant-skills-static-20261103.json).

### Technical writing: Split Transcript by Intent

**Unique idea:** Sort a mixed voice transcript into context, prompts, decisions, action items, questions and notes, while keeping every original sentence and speaker attribution.

**Important warning:** The original writes files and suggests passing spoken instructions directly to AI development tools. Recorded speech may contain private data or untrusted directions. Review the extracted content and approve any downstream use before an agent runs instructions or writes to a new destination. The original does not prove every sentence was retained.

**Evidence:** Q3 static review **16/20**; `danielrosehill/Claude-Transcription-Plugin@d19d6df5`, SKILL.md `71edb736`; root **MIT**. [Individual review](../registry/discovery/q3-danielrosehill-claude-transcription-plugin-static-20261103.json).

## What this does and doesn't count

Seven **distinct, positively endorsed Valuable Reference examples** from seven different domains. **Zero Recommended for Use entries in this starter set.** We have **not** established global counts, or that the other 26 domains lack useful skills. Each package has static source-vetting evidence, but **security scanning and hands-on behavioral validation were not run**.

The source-neutral [structured reference catalog](../registry/consumer-positive-references-20261103.json) includes exact pins, file hashes, supported mechanisms, limits, licensing and evidence. Other candidates, rejected packages and historical decisions stay in the broader research archive.
