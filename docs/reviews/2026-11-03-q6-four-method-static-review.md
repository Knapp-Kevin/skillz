# Four creative methods worth studying, and four unsafe package boundaries

These are **four individually reasoned static source reviews** from three previously disjoint source families, for the November 2026 music-composition and illustration coverage drive. The purpose is to help a visitor accomplish something useful, not claim that a high score equals approval to install or run someone else's package.

| Outcome | Exact original method | Static grade | Hard-fail findings | Consumer decision |
|---|---|---:|---:|---|
| **Film scoring / timecoded cues** | [video-scoring-audio](https://github.com/grapeot/opus-video-audio-skill/blob/0abc18d22d6baf9e55d4fce9a01d29e2528ee426/skills/video-scoring-audio/SKILL.md) | 14/20 | 3 | **Valuable Reference only** |
| **Concept art / artist briefing** | [design-concept-art-brief](https://github.com/jeffreytse/grimoire-core/blob/7ff5861b00836cb0d675c00a09a26d143722579e/skills/art/illustration/skills/design-concept-art-brief/SKILL.md) | 15/20 | 2 | **Valuable Reference only** |
| **Sequential art / comics** | [scenario-storyboards](https://github.com/scenario-labs/skills/blob/7f4b801c7248d51b093ec365aceb114bd06139e6/skills/scenario-storyboards/SKILL.md) | 13/20 | 3 | **Valuable Reference only** |
| **Character consistency** | [scenario-identity-library](https://github.com/scenario-labs/skills/blob/7f4b801c7248d51b093ec365aceb114bd06139e6/skills/scenario-identity-library/SKILL.md) | 12/20 | 2 | **Valuable Reference only** |

**Separate standards:** All 4 have precise commit-pinned SKILL.md hashes, root MIT source-license text, individual 10-dimension grades and referenced dependency notes. But this environment **could not retrieve each complete upstream Git package tree**, so package-tree identities, exhaustive per-file rights and full-package validation remain **UNKNOWN**. These methods are safe *to learn from as described*, not cleared for unchanged execution or wholesale copying. All four: **security scan NOT RUN; model behavior/adversarial execution NOT RUN**. No audio was generated, image uploaded, user project read, model billed or script executed.

## Music: score directly to a picture

**Video Scoring Audio** is worth studying because it links a visual event to a precise MIDI onset and measures whether the rendered audio follows that event. Treat the listener's aesthetic decision as separate from verifiable duration, peaks, and dynamics. This is more useful than asking a music generator to guess the timing of a scene change.

**Do not run its helper unchanged.** Static source inspection of `scripts/score_cue.py` found that a JSON cue's `name` directly forms `outdir / f"{name}.wav"`, MIDI and raw WAV paths. An absolute or parent-relative name can escape the output folder; the downstream renderer calls `ffmpeg -y` and can overwrite an existing file. The sample `init` subcommand has a no-overwrite check, but `render` does not. This is a source-level **potential path-escape/overwrite defect**, not an executed exploit or scanner finding. The root MIT license does not settle each soundfont's terms, and optional online music generation requires separate user approval and cost limits. **Static grade: 14/20, reference-only.**

## Illustration: concept-art briefs

**Design Concept Art Brief** offers a useful, host-independent sequence: decide the creative direction, annotate positive references and anti-references, test the silhouette, set production constraints and agree on deliverables, changes and usage rights. It works for characters, creatures, props and environment art direction, but a *brief* is not an environment drawing workflow.

**Do not adopt its evidence claims uncritically.** It asserts that every major game studio uses the method and that clear briefs cut revisions by 40–60%, without presenting a qualifying study. Named books and existing film/game artwork have separate rights from the source's MIT text. Sending contracts, briefs or external reference images still requires action-specific approval. **Static grade: 15/20, reference-only.**

## Illustration: sequential comics and storyboards

**Scenario Storyboards** proposes a practical sequence: write a beat sheet first, approve a baseline drawing of each character, make one panel at a time, check continuity and put lettering on the art afterwards. This allows the user to replace one poor panel instead of generating an entire comic page again.

**Do not let the original skill act unattended.** It may select a model and spend credits on multiple `model_run` operations, upload character images, invoke several sibling skills and persist assets. Tool availability is not user permission. The `scenario-text-overlay` sibling calls an uninspected rendering script. The transferable method does not require Scenario. **Static grade: 13/20, reference-only.**

## Illustration: stable character identity

**Scenario Identity Library** adds a different idea: write an explicit silhouette, palette and signature-feature baseline, approve a hero image, and require each new character view to pass a consistency gate before adding it to a reference library. This supports character art; it **does not fully cover environment illustration**.

**Do not run its account workflow unchanged.** It may upload private photos/artwork, spend credits, create persistent collections and remove older assets. Those are separate write/private-egress authorizations. The source's root MIT license does not license uploaded artwork or downstream outputs. **Static grade: 12/20, reference-only.**

## Coverage: what is actually served

In the newly reviewed, positively selected method shelf, **music composition gains one specific subdomain (scoring)** and **illustration gains three (concept art, sequential art, character identity)**. None is unchanged-use approved. Other subdomains remain unserved by positive recommendations; character/environment is only partially addressed.

The dated [November 2 capability audit](../../registry/discovery/capability-coverage-audit-20261102.json) still legitimately reports **0/8 and 1/6 historical review/candidate links**. It measures a different date and stage, not the new positive method counts. [Browse all 14 creative subdomains and pending sources](../capability-creative-coverage.md).

## Evidence and next gate

- [Four exact-pinned individual 10-axis reviews](../../registry/discovery/q6-four-package-static-reviews-20261103.json) record all source revisions, SKILL.md blobs, observed helper/sibling blobs, scores, detailed reasons, root license SHA, unique method, nontriggers, hard fails, separate behavioral/security states and missing package-tree limitations.
- [Capability-level machine routes](../../registry/discovery/q6-creative-capability-routing-20261103.json) distinguish this bounded four-method shelf from unqualified leads and unfilled subdomains.
- [Specialist discovery ledger](../../registry/discovery/q6-specialized-music-illustration-pinned-leads-20261103.json) and [draft #677](https://github.com/Knapp-Kevin/skillz/pull/677) retain other pinned leads with their own owners and rights checks. Do not merge scores by filename or assume a package is identical because its SKILL.md matches.
- **Next:** establish complete package trees and per-file rights where possible, then review a full music theory/composition tranche and genuinely qualified illustration environment/scientific/editorial alternatives. User authority, installs, actions, network, scanner and model-executed behavior remain separate gates.

The globally distinct eligible-skill count is **UNKNOWN**. Q1–Q5 historical path-decision accounting is separate and unchanged.
