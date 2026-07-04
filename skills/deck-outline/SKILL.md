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
  version: 1.0.0
---

# Deck Outline

Produce a deck outline where the story is designed before any slide exists: who the audience is and the single decision or feeling the deck must produce, a narrative spine of 10-14 one-sentence beats, and a per-slide plan where every headline is a claim the audience can agree or disagree with — not a topic label. This skill delivers the outline only; building the actual file is handed off to the vendored pptx skill.

## Execution Flow

1. **Pin audience and outcome.** Ask who the deck is for and the ONE decision or feeling it must produce (invest, approve, buy, feel confident in the roadmap). If the answer is "several things", push back — a deck with two goals achieves neither.
2. **Draft the narrative spine.** Write 10-14 beats, one sentence each, that carry the arc: the situation as the audience knows it, the tension that breaks it, and the shape of the resolution. Read the spine aloud as a paragraph — if it doesn't hold as a story, no slide design will save it.
3. **Convert beats to slides.** For each beat, write a headline sentence that is a claim, not a topic ("Churn is concentrated in month two", never "Churn overview"). A reader skimming only headlines should get the full argument.
4. **Attach evidence and visuals.** For each slide, list the supporting evidence (data point, quote, demo, chart source) and suggest one visual treatment. Flag any slide whose evidence is missing or asserted-but-unverified.
5. **Present** in the Output Format below.
6. **Hand off execution.** When the operator approves the outline, direct deck production to the vendored pptx skill (vendor/anthropic-skills) — do not build slides in this skill.

## Output Format

```
# Deck Outline: [deck name]
**Audience:** [who] · **Must produce:** [the one decision/feeling]

## Narrative spine
1. [beat — one sentence]
2. [beat]
...
[10-14 beats: situation → tension → resolution shape]

## Slides
| # | Headline (claim) | Supporting evidence | Visual suggestion |
|---|------------------|---------------------|-------------------|
| 1 | [claim sentence] | [evidence + source]  | [chart/photo/demo] |

## Evidence gaps
- Slide [N]: [what is missing before this claim can be shown]
```

## Notes

- Headlines are claims. If a headline could title a Wikipedia article, rewrite it until someone could disagree with it.
- Spine before slides, always — reordering beats is cheap, reordering finished slides is not.
- Outline only: this skill never generates the .pptx. Execution belongs to the vendored pptx skill after explicit operator approval of the outline.
