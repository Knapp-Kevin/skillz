# Skill evaluation framework

How a skill gets from *discovered* to *allowed to influence an agent*. Decisions are recorded in [`registry/candidates.yaml`](../registry/candidates.yaml); source trust/provenance is recorded separately in [`registry/sources.yaml`](../registry/sources.yaml).

The governing principle: **a skill is an untrusted dependency until reviewed, scoped, tested, and versioned.** The opportunity is not collecting skills. It is deciding which skills may influence an agent, under which conditions, with which permissions, and with what proof they improve outcomes.

## Source class is not adoption status

Reference repositories may be:

- `official`: first-party source for the platform/vendor it describes
- `community-vetted`: intentionally centralized because it provides strong comparative or supplemental value
- `tracked`: useful discovery source not included as an active vendored corpus
- `quarantined`: source or content unsuitable for normal influence without explicit review

Source class answers **where the skill came from and how much authority that source deserves**.

Candidate status answers **whether this particular skill has earned influence in this system**.

Do not confuse the two.

An official skill can still be unsafe for an operation or redundant with local governance. A community-vetted skill can be excellent comparative evidence without becoming platform authority.

## Intake flow

```
discovered (skill-bootstrap / skills-pulse / longlist / ad-hoc)
  → source classification (if source is new)
  → registry entry (status: track)
  → scored (rubric below)
  → sandbox evaluation (isolated worktree or scratch project, before/after task comparison)
  → adopted | rejected | quarantined
```

Every transition updates the registry entry. No skill is symlinked into a host, referenced as an authoritative operational dependency, or compiled for deployment without an `adopted` decision appropriate to that use.

Vendored reference repositories are available for comparison. **Vendored does not mean automatically adopted.** Official repositories may be trusted as authoritative documentation/examples for their own platform, but individual high-impact skills still require permission and behavior review before operational use.

### Model-tier rule for evals

A "no effect" verdict measured only on a frontier model may be a ceiling effect, not a rejection ground. Instruction skills often encode behaviors weaker tiers omit. Sandbox evaluations of instruction-only skills should include a weaker-model arm when the intended deployment includes weaker models.

## Comparative disposition vs adoption status

During bootstrap or design, a reference skill may receive a comparative disposition before any adoption decision:

- **ADOPT**: existing skill appears to fit and should proceed through normal evaluation/adoption.
- **ADAPT**: use the source as the basis for a locally modified skill; preserve provenance.
- **SUPPLEMENT**: borrow a specific proven pattern while keeping the target skill/process authoritative.
- **COMPOSE**: keep skills separate and combine responsibilities explicitly.
- **BENCHMARK**: use the reference only as a quality/evaluation comparator.
- **REJECT**: do not incorporate it.

These are design decisions, not registry statuses. An `ADAPT` recommendation still requires the resulting local skill to be evaluated.

## Scoring rubric (0–3 per criterion)

| Criterion | 0 | 3 |
|---|---|---|
| Relevance | No clear workflow | Critical recurring workflow |
| Source trust | Unknown/random | Official or intentionally vetted with provenance |
| Scope clarity | Vague | Clear trigger AND non-trigger conditions |
| Version compatibility | Unknown | Explicitly compatible |
| Determinism | Vague advice | Reproducible tests/checks |
| Security posture | Unsafe/unknown | Sandboxed/read-only/safe |
| Token efficiency | Bloated | Strong progressive disclosure |
| Verifiability | No test path | Clear before/after eval |
| Composability | Conflicts likely | Explicitly compatible with repo governance |
| Drift risk | High | Actively reduces drift |

Rough bar: **< 15 reject, 15–21 sandbox, ≥ 22 adopt-track**. Any single 0 on Security posture or Composability forces quarantine/reject regardless of total.

## Statuses

| Status | Meaning |
|---|---|
| `adopted` | Approved for the documented use; indexed/installable where applicable. |
| `sandbox` | Promising; being tested in isolation before a decision. |
| `track` | Signal worth watching; not adoption-ready. |
| `rejected` | Vague, risky, obsolete, redundant, or behaviorally inferior. |
| `quarantined` | Useful but dangerous without strict permissioning; never auto-loaded. |

## Permission tiers

Every candidate is classified by the highest-impact action it can trigger. Only the first two tiers may run without explicit human approval unless a more authoritative environment policy says otherwise.

| Tier | Examples |
|---|---|
| `read-only` | Inventory, diagnostics, digests, scans |
| `plan-only` | Recommendations, architecture plans, drafts |
| `generate` | Code/config/doc generation into the working tree |
| `staging-write` | Issues, PRs, staging deploys, scheduled drafts |
| `production-write` | Production deploys, published releases, sent messages |
| `identity` | RBAC, app registrations, credentials, agent identity |
| `cost` | Spend-affecting changes |
| `destructive` | Deletes, payments, irreversible external actions |

## Security review checklist (before any adoption or material adaptation)

- Inspect all scripts and bundled resources.
- Check for external network calls, secret handling, destructive file operations, and dependency installs.
- Verify version compatibility; run in a sandbox first.
- Record expected tool permissions in the registry entry.
- Confirm the skill declares when it should be used AND when it must not be used.
- Check for conflicts with repo-level rules (CLAUDE.md, AGENTS.md, Qor-logic doctrines, MCP policies).
- Check `registry/sources.yaml` for source class and provenance.
- If copied or materially adapted, preserve attribution/license requirements per `docs/third-party-provenance.md`.
- If behavior came from a community-vetted source, ask whether it changes user-facing process or imports unnecessary author-specific assumptions.

## Redundancy guard

Before adopting, adapting, or creating, check in order:

1. **Qor-logic** (`../Qor-logic/qor/skills/`) for anything gated/SDLC. If covered, reject with `covered_by` unless the proposed skill is clearly outside that authority.
2. **Host built-ins** such as code review, security review, verification, or equivalent native capabilities.
3. **Vendored official sources** in `INDEX.md`. Prefer the official implementation for platform-specific behavior unless evidence supports a local adaptation.
4. **Vendored community-vetted sources** in `INDEX.md`. Use them as comparative/adaptation/supplemental evidence, not automatic authority.
5. **This repo's local skills and ROADMAP**. If covered or planned here, refine/compose rather than adding a competing copy.
6. **Tracked community sources** only when the previous layers do not adequately cover the need.

Two skills that answer the same trigger without an explicit composition relationship are worse than one. They create conflicting process authority and bloat context.

## Behavioral evaluation

Use [`skills/skill-eval/SKILL.md`](../skills/skill-eval/SKILL.md) for controlled baseline-versus-treatment testing.

When evaluating an adaptation or supplement, prefer three arms when practical:

1. target skill/process baseline
2. reference skill or reference pattern alone when meaningful
3. target skill/process plus the proposed adaptation/supplement

Write success checks before seeing the outputs. A more elaborate result that does not measurably improve the target behavior is not an improvement.
