# Skill Eval: handoff-writer (vs registry candidate `handoff`)

Registry entry under decision: `handoff` — sandbox / generate
Claims under test: loading `skills/handoff-writer/SKILL.md` produces handoffs a zero-context successor can act on (state+verification, decisions+why, exact next actions, landmines) better than an unassisted "write a handoff" request.

## Method

- 3 scenario tasks (interrupted refactor; debug-found-fix-unapplied with a leaked credential; half-done vendor research), each with 5 checks (0–2) **pre-registered before any run**.
- 6 isolated fresh-context subagent runs (3 baseline / 3 treatment, identical prompts except the appended SKILL.md text), executed on the session's frontier model.
- Blind grading: independent judge, arm labels randomized per task, scenario facts + rubric only.

## Tasks

| # | Task | Success checks | Baseline | With skill | Delta |
|---|------|----------------|----------|------------|-------|
| 1 | Interrupted refactor handoff | 5 checks incl. landmine + codename | 10/10 | 10/10 | 0 |
| 2 | Debug handoff w/ leaked token | 5 checks incl. security (no token reproduction) | 10/10 | 10/10 | 0 |
| 3 | Half-done research handoff | 5 checks incl. opinion-vs-finding hygiene | 10/10 | 10/10 | 0 |

Both arms passed the security-critical check (neither reproduced the leaked token; both flagged rotation). Judge's qualitative notes: treatment showed marginally better claim hygiene and action sequencing (T2/T3); baseline was marginally more scenario-faithful (T1, where treatment hedged one item as "unverified" beyond the scenario facts). No check-level difference anywhere.

## Cost

Baseline tokens: 91,028 | With skill: 95,278 | Delta: +4,250 (+4.7%)

## Verdict

**No effect (at frontier-model tier)** — a ceiling effect: the executing model already performs every rubric behavior unaided, so the skill's checklist added cost without measurable lift. This is evidence about *this model tier*, not about the skill's value for weaker executors: the rubric dimensions the skill encodes (verification-method column, landmine taxonomy, opinion-vs-finding separation) are precisely the behaviors smaller models omit. A weak-model arm (e.g., Haiku-tier) is the required follow-up before any "no effect" generalization.

## Recommended registry change

- `handoff` (community): status `sandbox` → `rejected`, `covered_by: first-party skills/handoff-writer` — the community candidate offers nothing the first-party skill lacks, and this eval shows even the first-party version is tier-dependent; no case for a third-party dependency.
- `handoff-writer` (first-party): keep. Re-run this eval with a weak-model arm; if the delta appears there, annotate the skill as a capability-floor equalizer.
- `to-issues`, `rules-distiller` (sandbox): **eval blocked — no canonical artifact acquirable.** Recommend `sandbox` → `track` with rationale "artifact must be located and source-vetted before any eval can run."

Applied by a human per skill-eval's read-only-toward-governance rule.

## Follow-up (fed to BACKLOG)

- B11: re-run this eval with baseline/treatment arms executed on a weak model tier to test the equalizer hypothesis.
