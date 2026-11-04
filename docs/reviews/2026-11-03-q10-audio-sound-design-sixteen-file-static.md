# Q10 supplement: sound design, sixteen-file executable package

**Date:** 2026-11-03 · **Route:** REPOSITORY_MAINTENANCE · **Q9 discovery:** #697 · **Q10 review:** #698

## Outcome

The pinned [Sound Design package](https://github.com/salomonMuriel/media-production-skills/tree/6ba42845c9d355776fb10091e47ee32e035509fc/skills/sound-design) has a valuable production method: use measurements to align music and sound effects, perform blind comparisons of edits with untouched controls, and test loudness and peaks on the **finished** recording. It earned **13/20** on the ten-axis static rubric.

**Do not execute unchanged.** The blind-splice program has an unguarded directory-deletion path that could destroy unrelated files. The 16 source files were inspected; the finding is grounded in the code, **not** a hypothetical behavioral run or a scanner alarm.

| Useful mechanism | Why it matters |
|---|---|
| Blind splice tests against an untouched original | A splice that looks perfect on a waveform may still sound abrupt |
| Measured transient alignment | The sound lands when the impact occurs, not just when the file starts |
| Speech-aware music ducking | The voice stays audible while the soundtrack remains intentional |
| Final-file LUFS and true-peak checks | The exported file, not just the editor project, must meet the target |

## Concrete unsafe behavior

The file [`scripts/music_splice.py`](https://github.com/salomonMuriel/media-production-skills/blob/6ba42845c9d355776fb10091e47ee32e035509fc/skills/sound-design/scripts/music_splice.py#L182-L211) defines a command with a user-selectable `--out-dir`. Within `run_blind`, **an existing target directory is recursively removed** with `shutil.rmtree(arguments.out_dir)`, without checking whether its contents belong to that command, whether the folder is inside a disposable workspace, or whether the user approved deletion. The default is `out/review/splice-blind`, but `--out-dir` can point elsewhere. This is a **confirmed static source-code deletion hazard**, not proof that an actual user directory was erased.

Other output paths also lack no-clobber guards: `music_splice.py` writes edit WAVs and joins JSON; `mix.py` writes named stems, master and report; `foley.py` replaces predictable SFX files; and `audio_qa.py` gives reports filenames from a file's *stem*, meaning two input files with the same base name can replace each other's report. The [structured review](../../registry/discovery/q10-audio-sound-design-sixteen-file-static-20261103.json) records exact file/blob identities and code locations.

## Package, licensing and missing tests

Every file in the **16-file owned subtree** was opened and read without executing scripts. The package Git tree is `23f68eb57f4a0e93032e9108ae0de3f2684713e5`; the root MIT license blob is `44a666fb7b15bb3f52a1d88f06ba46f8992df423`. The package depends on Python 3.11+, `uv`, NumPy/SciPy, FFmpeg and related audio libraries. Optional judging refers to a separate `video-director` skill and hosted model. No binary, package, network request, audio analysis, model judging or file write was executed during this review.

Upstream MIT licenses its own code/text with the required notices. It does **not** grant use of someone else's music, performance recordings or samples. Commercial/music content rights and disclosure to any hosted judge remain separate.

Before use, require a scratch directory, explicit output path ownership, no-clobber checks, safe removal of only command-created files, source-music rights, action-scoped permission for installs/network/cost, a pinned scanner pass and observed representative/adversarial behavior. Then test audio correctness with human listening. Passing a scanner would not itself resolve the file-loss defect.

**Disposition:** REJECT UNCHANGED / KEEP CONCEPTUAL METHODS · **Security:** NOT RUN · **Behavior:** NOT RUN · **Featured shelf:** unchanged. The protected information is the engineering lesson and evidence, not a recommendation to install this package.

