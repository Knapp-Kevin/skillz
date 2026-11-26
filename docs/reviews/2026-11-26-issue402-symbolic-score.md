# Issue 402: Symbolic score pinned source disposition

2026-11-26. Reference-only; unchanged use held. Historical scanner INCOMPLETE (16 missing-reference indications); not a new scan or host test.

## Exact scope

Repository: jtydhr88/music-composition-skills; pin `e283141babb8806f2798d5fd2d9e833e75c1bd26`; package `plugins/music-composition/skills/mc-symbolic-score`; complete tree `4e2500d61b989b399c45ba70df795f7c5d820459`. Both owned files were read in full and returned blob IDs match the untruncated pinned recursive tree inventory: `SKILL.md` `d84cd65170744219c64a46387e6ff675bc1fabbd`; `reference.md` `4c5183b6d7f0c15ef5e0df59f73139e5faeb522d`. Root LICENSE and NOTICE reviewed. Default branch head matches pin. Selected external-to-package reference paths exist, but no claim is made that all historical missing-reference indications were resolved.

## Findings (12/20 static rubric)

- **contradictory-backend-capability (MEDIUM)** — SKILL.md §§6b, 7.2 and source appendix; reference.md §§1.6, 5. The entrypoint reports tested two-voice support and says the dialect is known; its appendix and companion reference still classify dialect and multi-voice support as unconfirmed. No backend version, exact fixture or reproducibility receipt is supplied. Require a versioned capability probe and conservative fallback.
- **unsupported-deterministic-render-claim (MEDIUM)** — SKILL.md §§2.2, 5.3, 8. Identical symbolic input alone does not establish identical audio or isolate a single variable. Renderer, soundfont, plugins, timing resolution, settings and environment must also be pinned; no emitter executable is owned by this two-file package. The described author experiment is not an independent host test.
- **unescaped-format-and-private-metadata (MEDIUM)** — SKILL.md §§3.1, 9. Raw title, motif ABC and lyrics insertion, and wholesale export of intent/mix/vocal text into comments or metadata, lack escaping, field allowlists and privacy controls. Embedded line breaks or target-format delimiters can alter output structure; internal notes may be carried into shared files. Require format-aware serialization, validated motifs, minimization and separately approved destinations.
- **insufficient-semantic-validation (MEDIUM)** — SKILL.md §§6, 8, 9; reference.md §1.2–1.3. Aggregate bar count and chord-degree checks do not establish per-voice measure durations, note/lyric alignment, effective accidentals, supported target features or lossless conversion. The source acknowledges that the named parser drops lyric lines and chord playback. Require per-format semantic round-trip and explicit loss reporting.
- **external-dependencies-and-authority (MEDIUM)** — SKILL.md §§7–9; root NOTICE. Neighboring schema, backend configuration, render and orchestration skills and external parsers/synths are dependencies. Their presence is not authorization to execute, upload lyrics, install software, spend credits or distribute protected material. Preserve MIT notice for original content; model weights and protected material have separate rights.

## Disposition

Version and test backend capability, pin renderer dependencies, serialize and minimize metadata, require per-voice and per-target semantic checks, separate external execution and publication authorization. No third-party code executed or copied into Skillz; no private project data, paid backend calls, audio rendering, scanner run, or unchanged-use approval. Original 10 PASS / 7 FAIL / 33 INCOMPLETE unchanged. Targeted source-review progress 33/40 (7/7 failed + 26/33 incomplete), seven initial reviews remain. #402 remains open.
