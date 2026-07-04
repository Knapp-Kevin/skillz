---
name: handoff-writer
description: >-
  Write continuation context for cross-session or cross-agent work: current
  state, decisions with rationale, open threads with exact next actions, and
  landmines, so a successor can act without re-deriving anything. Use when
  the user asks "write a handoff", "prepare context for the next session",
  "summarize where we are for another agent", or before a context switch.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Handoff Writer
  emoji: "🤝"
  version: 1.1.0
  min-model-capability: sonnet
---

# Handoff Writer

Produces a handoff document a successor — another agent or a future session — can act on immediately, without re-deriving state, relitigating decisions, or stepping on intentional oddities. The governing rule: write for a reader with zero shared context. Every codename, shorthand, or project-internal term gets a one-line definition at first use.

## Execution Flow

1. **Inventory current state.** List what is done and, for each item, how it was verified (test run, manual check, reviewed diff) — "done" without a verification method gets marked unverified. List what is in progress and exactly where it stopped.
2. **Record decisions and their why.** For each decision that shaped the current state, capture what was chosen, what was rejected, and the reason — one or two sentences each. The point is that the successor does not relitigate settled questions.
3. **List open threads with exact next actions.** Each thread gets a concrete first step ("run X, expect Y, then edit Z"), not a topic label. If the next action depends on an unresolved question, state the question and who or what can answer it.
4. **Mark the landmines.** Two kinds: things that look wrong but are intentional (workarounds, deliberate duplication, disabled checks — say why), and things that look done but are not (stubs, untested paths, hardcoded values pending real ones).
5. **Add pointers.** Reference every relevant file and artifact by full path; never "the config file" or "the script we discussed."
6. Define every codename or shorthand in one line at first use, then assemble the document in the Output Format below.

## Output Format

```
# Handoff: <task/project> — <date>

## Definitions
- <term>: <one-line definition>

## State
| Item | Status | Verified by |
|------|--------|-------------|

## Decisions
- <chosen> over <rejected> because <reason>.

## Open threads
1. <thread> — next action: <exact step>. Blocked on: <nothing | question>.

## Landmines
- Looks wrong, is intentional: <item> — <why>.
- Looks done, is not: <item> — <what remains>.

## Pointers
- <full path> — <what it is>
```

## Negative rules

These override every section rule above, including "define every term." An honest blank beats a filled fabrication in every case.

- **Never reproduce secret-shaped strings** — tokens, API keys, passwords, private keys, session cookies, connection strings (`sk-…`, `key=`, `token=`, `Bearer …`, `-----BEGIN`). Refer to a credential by type and short prefix only: "the OpenAI key (`sk-pr…`)". "Define every term" does **not** apply to credential values — a handoff that quotes a secret becomes a new leak vector. If a secret appears anywhere in the work being inventoried, flag probable exposure and recommend rotation in Landmines.
- **Never invent a fact to fill a slot.** If a Decisions line has no evidence for its *because*, or a State row has no verification method, write `not established` — do not manufacture a rationale, a rejected alternative, or a verifier to satisfy the format.
- **Mark inference as inference.** Anything not directly observed in the session gets "(inferred: <basis>)". Never promote an inferred requirement or risk to a stated one.
- **Sections may be empty.** An empty section with `none established` is a valid, complete answer; missing evidence is itself handoff content — report it as an open thread.

## Notes

- Test the document against the zero-context standard: if a sentence only makes sense to someone who was present, rewrite it.
- Verification method matters more than the done/not-done label; successors get burned by unverified "done" items, not by honest "in progress" ones.
- Landmines are the highest-value section — they prevent the successor's two most expensive mistakes: fixing what is not broken and trusting what is not finished.
- This skill writes the handoff document only; it never modifies the work itself or any configuration while inventorying it.
