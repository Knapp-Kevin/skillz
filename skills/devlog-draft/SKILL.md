---
name: devlog-draft
description: >-
  Draft a founder-led devlog or blog post from real work evidence — git
  history across the MythologIQ repos plus logged decisions — telling one
  narrative in the operator's own voice. Use when the user asks "draft a
  devlog", "write a blog post about this week's work", "turn my commits
  into a post", or wants a build-in-public update grounded in what actually
  shipped.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Devlog Draft
  emoji: "📝"
  version: 1.0.0
---

# Devlog Draft

Produce a devlog draft built from evidence, not vibes: commits and decisions from a chosen window, distilled into one narrative worth telling, written in the operator's voice. The deliverable is three title options, a draft where every factual claim points at its evidence, and an explicit list of claims the operator must verify before publishing.

## Execution Flow

1. **Pin the window.** Ask the operator for the time window (e.g. "last two weeks") and, if ambiguous, which MythologIQ repos are in scope. Do not guess a window.
2. **Gather evidence.** Run `git log --since=<window> --oneline --stat` across each in-scope repo. Read decision entries for the window from `docs/DECISIONS.md` or the project's ledgers. Collect exact commit messages and decision phrasing — this is the quote pool.
3. **Pick ONE narrative.** Scan the evidence for the single story worth telling: a problem wrestled with, a bet placed, a reversal, a thing learned. A devlog is not a changelog; if the evidence only supports a list of changes, say so and ask the operator which thread matters to them.
4. **Draft in the operator's voice.** Quote their actual phrasing — commit messages, decision-log sentences — wherever possible rather than paraphrasing it into marketing prose. Tag each factual claim inline with its evidence (commit hash, decision entry, file).
5. **Separate hypothesis from proof.** Anything not directly backed by the evidence pool gets phrased as a hypothesis ("we think", "the bet is") or moved to the verification list. No synthetic authority, no invented traction or usage numbers, no "users love" without a source.
6. **Present** in the Output Format below.

## Output Format

```
# Devlog Draft — [window] · [repos covered]

## Title options
1. [title]
2. [title]
3. [title]

## Draft
[Narrative draft. Factual claims carry inline evidence markers:
(evidence: abc1234, repo) or (evidence: DECISIONS.md 2026-06-14).]

## Claims needing your verification
- [claim as written] — [why it is unverified and how to check it]
```

## Notes

- Registry marketing rules are hard constraints: no synthetic authority, no fake traction claims, hypothesis and proof stay visibly separate, and the operator's voice is preserved — quote them, don't ventriloquize them.
- One narrative per draft. Cut side-threads rather than braiding three weak stories together.
- Read-only: this skill produces a draft document. Publishing or posting it anywhere is draft-only — never send, post, or schedule publication without explicit approval.
