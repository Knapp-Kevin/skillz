# Skill template

Copy this into `skills/<name>/SKILL.md` and fill in. Kept in `docs/` (not `skills/`) so skill loaders never pick the template up as a real skill.

```markdown
---
name: <kebab-case-name>            # must match the directory name
description: >-
  <What it does, one sentence.> Use when the user asks
  "<trigger phrase 1>", "<trigger phrase 2>", or wants <outcome>.
metadata:
  author: frostwulf.zo.computer
  category: <Productivity|Development|Research|Ops>
  display-name: <Title Case Name>
  emoji: "<emoji>"
  version: 1.0.0
---

# <Title>

<One-paragraph summary of the outcome this skill produces.>

## What This Does

<Numbered source/step layers. Be explicit about which part the script
does and which part the model does — synthesis belongs to the model.>

## Execution Flow

1. Run the script (Bun or Node 22.18+):

   ```
   bun run scripts/<name>.ts
   node scripts/<name>.ts --flag value
   ```

2. <Fill gaps the script can't reach — fallbacks, judgment calls.>
3. <Synthesize.>
4. Present in the Output Format below.

### If no JS runtime is available

<Pure web-tool fallback: which URLs to fetch, what to search.>

## Scheduling

- **Claude Code:** `/schedule` for a recurring routine, `/loop` for in-session intervals.
- **Other agent platforms:** scheduled automation whose instruction is "Run the <name> skill and post the result."

## Output Format

```
<Exact skeleton of the deliverable.>
```

## Notes

- <Authority ordering of sources, known failure modes, safety rules
  (read-only? requires approval before sending/mutating?).>
```

Checklist before merging a new skill:

- [ ] `name` matches directory; description says **when** to use it, not just what it does
- [ ] Script runs on both `bun` and `node` with no install step
- [ ] Web-tool fallback documented for every scripted source
- [ ] Mutating actions (send/push/delete) gated behind explicit approval
- [ ] Index regenerated: `node scripts/build-index.ts` (updates INDEX.md + index.json)
