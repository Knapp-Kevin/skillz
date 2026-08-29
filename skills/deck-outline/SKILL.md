---
name: deck-outline
description: >-
  Build a narrative-first outline for a pitch, update, or launch deck: the
  one decision or feeling the deck must produce, a 10-14 beat narrative
  spine, and per-slide headline claims with evidence and visual suggestions.
  Use when the user asks "outline a deck", "help me structure my pitch",
  "plan my launch presentation", or wants slides that argue instead of list.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Deck Outline
  emoji: "🎞️"
  version: 1.1.0
---

# Deck Outline

Produce a deck outline where the story is designed before any slide exists: who the audience is and the single decision or feeling the deck must produce, a narrative spine of 10-14 one-sentence beats, and a per-slide plan where every headline is a claim the audience can agree or disagree with, not a topic label.

This skill delivers the outline. Building a slide file is a separate capability and must use the active host's supported presentation tooling or another individually eligible skill. Do not assume that a vendored presentation skill is eligible merely because it exists in the reference corpus.

## Execution Flow

1. **Pin audience and outcome.** Ask who the deck is for and the ONE decision or feeling it must produce (invest, approve, buy, feel confident in the roadmap). If the answer is several things, identify the primary outcome before continuing.
2. **Draft the narrative spine.** Write 10-14 beats, one sentence each, that carry the arc: the situation as the audience knows it, the tension that breaks it, and the shape of the resolution. Read the spine as a paragraph. If it does not hold as a story, revise before slide design.
3. **Convert beats to slides.** For each beat, write a headline sentence that is a claim, not a topic. A reader skimming only headlines should get the full argument.
4. **Attach evidence and visuals.** For each slide, list the supporting evidence (data point, quote, demo, chart source) and suggest one visual treatment. Flag any slide whose evidence is missing or asserted-but-unverified.
5. **Present** in the Output Format below.
6. **Hand off execution only after outline approval.** Detect the current host's actual presentation-generation capability. Use it when available and authorized. If no presentation-generation mechanism is established, return the complete outline and report `BLOCKED: PRESENTATION BUILD METHOD NOT ESTABLISHED` rather than routing to an arbitrary reference skill.

## Output Format

```text
# Deck Outline: [deck name]
**Audience:** [who] · **Must produce:** [the one decision/feeling]

## Narrative spine
1. [beat — one sentence]
2. [beat]
...

## Slides
| # | Headline (claim) | Supporting evidence | Visual suggestion |
|---|------------------|---------------------|-------------------|
| 1 | [claim sentence] | [evidence + source]  | [chart/photo/demo] |

## Evidence gaps
- Slide [N]: [what is missing before this claim can be shown]

## Execution handoff
- Host presentation capability: [established capability | not established]
- Build state: [ready for approved build | BLOCKED: PRESENTATION BUILD METHOD NOT ESTABLISHED]
```

## Negative rules

- Never invent evidence to complete the slide table. Missing evidence stays in `Evidence gaps`.
- Do not create a slide file before the outline is approved unless the user explicitly asked to skip the outline-review boundary.
- Do not treat reference-corpus presence as quality/eligibility evidence for a downstream presentation skill.
- Do not claim a deck file exists unless the active host actually created it.

## Notes

- Headlines are claims. If a headline could title a Wikipedia article, rewrite it until someone could disagree with it.
- Spine before slides: reordering beats is cheap, reordering finished slides is not.
- This skill is host-portable because presentation execution is resolved at runtime rather than hard-wired to one vendor's artifact implementation.