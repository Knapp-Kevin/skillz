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

## Adaptive frameworks, not bespoke tools — universal rule

Root skills must remain **environment-agnostic adaptive frameworks**. Custom interactions live in a **governance flag/document** the skill discovers and binds to at runtime — never hardcoded in SKILL.md. Unwarranted specificity invalidates a skill the moment it meets a different environment.

1. **Ship the adaptation function, not the values.** When behavior depends on local convention (formats, taxonomies, paths, org names, personal defaults), the Execution Flow's FIRST step is **Bind**: discover the governing document, in order — (a) the target repo's own convention/governance doc (README, AGENTS.md, or equivalent), (b) the operator profile / host memory, (c) elicit from the operator and offer to record the answers as a governance doc for next time.
2. **The bound document is authoritative.** If it conflicts with anything remembered or assumed, the document wins; improving the workflow means editing that document, not the skill.
3. **Forge when absent.** Skills whose whole domain is convention-shaped (task coordination, project structure, review cadences) should be able to *generate* the governance document from elicited needs — scaffold mode — then operate against what they scaffolded.
4. **No operator specifics in skill bodies.** Org names, absolute paths, business names, and personal defaults in a SKILL.md are defects, not conveniences (see BACKLOG B18 for the de-specification sweep of early violations).

## Capability floor — design for the weakest model that will run this

Skills are executed by whatever model the host provides. Do NOT write model-adaptive prose ("if you are a smaller model…") — models cannot reliably self-assess tier, and branching text bloats context for everyone. Instead, make the *structure* carry weak models while frontier models skim it:

1. **Move judgment into determinism.** Anything a script can decide, a script decides ("script collects, model synthesizes"). The skeleton the script emits is the floor no model can fall below.
2. **Encode frontier behavior as explicit procedure.** Numbered steps, mandatory output sections, and taxonomies (e.g., handoff-writer's two landmine kinds) are a distillation of what strong models do unprompted — weak models follow the recipe instead of deriving it.
3. **Ship the acceptance check, not just the instruction.** A pre-written self-check ("if a sentence only makes sense to someone who was present, rewrite it") lets a weak model *verify* to a standard it cannot *generate* to unaided; checking is easier than generating.
4. **Constrain the generation space.** Tables to fill and skeletons to complete beat open prose; every blank is a prompt.
5. **Decompose.** Many small, narrow steps outperform one big ask on weak models; if a step needs cross-step memory, write the intermediate result down.
6. **Exemplars over adjectives.** For high-judgment skills, add a `references/examples.md` with one gold-standard output; imitation transfers where instruction doesn't. Tiered loading keeps it out of context until needed.
7. **Declare the floor as data, not prose.** Optional frontmatter `metadata.min-model-capability: haiku|sonnet|opus` (Qor-logic precedent) — hosts and routers enforce it; the model never has to self-assess.
8. **Ship negative rules with the scaffold.** Weak models follow explicit positive structure well and infer implicit negative constraints poorly — mandatory slots *pressure fabrication* and "define every term" *reproduces secrets* (docs/evals/2026-07-04-handoff-writer-haiku.md: a Haiku-tier arm reproduced a leaked token verbatim and invented a stakeholder requirement to fill a *because* slot). Every high-judgment skill with mandatory evidence/decision slots ships explicit prohibitions alongside the structure: **never reproduce secret-shaped strings** (tokens, API keys, passwords, private keys, session cookies — refer by type + short prefix only; recommend rotation when exposure is possible); **write `not established` when a slot has no evidence-backed value** — never invent rationale to fill a schema; **required sections may be explicitly empty** — missing evidence is a finding, not a blank to decorate; **mark inference as inference**, never as a stated fact. Mechanically enforced by `skills/skill-audit/scripts/risk-audit.ts` (FAIL for slot-bearing skills missing any rule class).

Evidence basis: docs/evals/2026-07-03-handoff-writer.md — on a frontier model an instruction-only skill scored 0 delta (ceiling effect); the rubric behaviors it encodes are exactly what weaker tiers omit.

Checklist before merging a new skill:

- [ ] `name` matches directory; description says **when** to use it, not just what it does
- [ ] Script runs on both `bun` and `node` with no install step
- [ ] Web-tool fallback documented for every scripted source
- [ ] Mutating actions (send/push/delete) gated behind explicit approval
- [ ] No hardcoded operator/org/environment specifics; a Bind step exists wherever behavior depends on local convention (§Adaptive frameworks)
- [ ] High-judgment skills (mandatory evidence/decision slots) carry negative rules: secret handling, anti-fabrication, missing-evidence fallback (§Capability floor rule 8)
- [ ] Index regenerated: `node scripts/build-index.ts` (updates INDEX.md + index.json)
