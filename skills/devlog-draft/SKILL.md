---
name: devlog-draft
description: >-
  Draft a founder-led devlog or blog post from real work evidence — git
  history across the bound workspace repos plus logged decisions — telling one
  narrative in the operator's own voice. Use when the user asks "draft a
  devlog", "write a blog post about this week's work", "turn my commits
  into a post", or wants a build-in-public update grounded in what actually
  shipped.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Devlog Draft
  emoji: "📝"
  version: 1.1.0
---

# Devlog Draft

Produce a devlog draft built from evidence, not vibes: commits and decisions from a chosen window, distilled into one narrative worth telling, written in the operator's voice. The deliverable is three title options, a draft where every factual claim points at its evidence, and an explicit list of claims the operator must verify before publishing.

## Execution Flow

1. **Pin and authorize the evidence scope.** Identify the operator-designated repositories and time window from the request or approved workspace context. If either is unclear, ask rather than guessing. A repository path remembered by the host is not permission to inspect it; obtain authorization for any private repository or decision ledger before reading. Persisting workspace preferences is a separate opt-in host action.
2. **Gather bounded evidence.** Use authorized host Git/repository tools to inspect commits within the approved scope and window; `git log --since=<window> --oneline --stat` is an optional host command, not a repository runner. Read only authorized decision entries. Keep commit identities and source pointers, but exclude credentials, credential-bearing URLs, private personal details, and confidential or unreleased content unless its inclusion and intended audience are expressly approved.
3. **Pick ONE narrative.** Scan the evidence for the single story worth telling: a problem wrestled with, a bet placed, a reversal, a thing learned. A devlog is not a changelog; if the evidence only supports a list of changes, say so and ask the operator which thread matters to them.
4. **Draft in the operator's voice.** Quote approved, non-sensitive phrasing from commits and decisions where useful rather than inventing a voice. Redact secrets, PII and private customer or organizational information; never paste raw private logs into a publication draft. Tag factual claims with minimal safe evidence references (commit hash, decision entry, file).
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
- Read-only evidence gathering and generate-only output: this skill produces a draft. Sharing it with other people, posting it, or scheduling publication are separate external actions requiring explicit approval of audience, destination and exact content.
