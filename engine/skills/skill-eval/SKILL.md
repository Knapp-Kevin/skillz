---
name: skill-eval
description: >-
  Before/after effectiveness testing of a candidate skill: run sample tasks
  with and without the skill loaded, score both arms, and produce registry
  evidence for an adopt/reject/quarantine decision. Use when the user asks
  "evaluate this skill", "does this skill actually help", "run the eval plan
  for a candidate", or when a registry entry needs proof before a status
  change.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Eval
  emoji: "⚖️"
  version: 1.1.0
---

# Skill Eval

Operationalizes the `eval_plan` that `docs/evaluation-framework.md` declares but nothing runs today: a controlled before/after comparison that turns "this skill seems useful" into measured evidence attached to the registry entry. This skill produces a report and a recommended status change; it never edits `registry/candidates.yaml` itself.

## Execution Flow

1. Read the candidate's entry in `registry/candidates.yaml` (status, permission tier, rationale, any declared `eval_plan`) and the candidate's SKILL.md. Note the specific outcomes the skill claims to improve.
2. Design 3-5 sample tasks that exercise those claims. Each task needs a measurable success check written before any run: an exact expected output, a verifiable property of the result, or a rubric line scored 0-3 per the framework's scoring table. Reject vague checks like "output is better."
3. Run each task WITHOUT the skill loaded (baseline arm). Use an isolated context per run — a fresh subagent per task-arm when the host supports it — so no run contaminates another. Record output, success check result, and token cost.
4. Run each task WITH the skill loaded (treatment arm), same isolation, same checks. Do not reword the task prompts between arms.
5. Score both arms against the pre-written checks. Compute the per-task delta and the aggregate token-cost delta.
6. Deliver a verdict: **measurable improvement**, **no effect**, or **degradation**. Map it to a recommended registry status change (improvement supports `sandbox` → `adopted`; no effect or degradation supports `rejected` or continued `sandbox` with a revised plan), citing the framework rule that every verdict updates the registry entry.
7. Present the evidence in the Output Format below for a human to apply to the registry.

## Output Format

```
# Skill Eval: <candidate-name>

Registry entry: <status> / <permission_tier>
Claims under test: <one line>

## Tasks
| # | Task | Success check | Baseline | With skill | Delta |
|---|------|---------------|----------|------------|-------|

## Cost
Baseline tokens: <n> | With skill: <n> | Delta: <+/-n (%)>

## Verdict
<measurable improvement | no effect | degradation> — <one-sentence justification>

## Recommended registry change
status: <current> → <proposed>
evidence: <this report's task table, summarized in one line per task>
```

## Negative rules

These override the report format. An eval's only value is that its numbers happened.

- **Never fabricate a result.** A score, token count, or delta that was not actually measured reads `not established` — an arm that did not run is reported as not run, never reconstructed from expectation.
- **Never reproduce secret-shaped strings** appearing in eval transcripts or scenario material (even synthetic ones) — type + short prefix only, per the sealed exemplar rule from the 2026-07-04 haiku eval.
- **Verdicts trace to rubric rows.** A degradation or improvement claim cites the specific graded behaviors that moved; unverifiable movement is `unverifiable`, not rounded to a direction.

## Notes

- Read-only toward governance: the recommendation is applied to `registry/candidates.yaml` by a human or by skill-audit-verified tooling, never by this skill.
- Success checks are written before either arm runs; checks invented after seeing output are not evidence.
- If the host cannot isolate contexts, say so in the report — shared-context results are weaker evidence and should not alone justify adoption.
- A degradation verdict on any security-relevant task forces a quarantine recommendation regardless of the aggregate score, mirroring the framework's single-zero rule.
