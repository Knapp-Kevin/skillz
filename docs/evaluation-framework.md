# Skill evaluation framework

How a skill gets from *discovered* to *allowed to influence an agent*. Distilled from the [longlist research](agent-skills-longlist.md) §17; decisions are recorded in [`registry/candidates.yaml`](../registry/candidates.yaml).

The governing principle: **a skill is an untrusted dependency until reviewed, scoped, tested, and versioned.** The opportunity is not collecting skills — it is deciding which skills may influence an agent, under which conditions, with which permissions, and with what proof they improve outcomes.

## Intake flow

```
discovered (skills-pulse / longlist / ad-hoc)
  → registry entry (status: track)
  → scored (rubric below)
  → sandbox evaluation (isolated worktree or scratch project, before/after task comparison)
  → adopted | rejected | quarantined
```

Every transition updates the registry entry. No skill is symlinked into `~/.claude/skills/`, referenced by an agent, or compiled to a host without an `adopted` entry (vendored official repos count as adopted-at-source; individual write-tier skills inside them still need their own review).

## Scoring rubric (0–3 per criterion)

| Criterion | 0 | 3 |
|---|---|---|
| Relevance | No clear workflow | Critical recurring workflow |
| Source trust | Unknown/random | Official/vendor/internal |
| Scope clarity | Vague | Clear trigger AND non-trigger conditions |
| Version compatibility | Unknown | Explicitly compatible |
| Determinism | Vague advice | Reproducible tests/checks |
| Security posture | Unsafe/unknown | Sandboxed/read-only/safe |
| Token efficiency | Bloated | Strong progressive disclosure |
| Verifiability | No test path | Clear before/after eval |
| Composability | Conflicts likely | Explicitly compatible with repo governance |
| Drift risk | High | Actively reduces drift |

Rough bar: **< 15 reject, 15–21 sandbox, ≥ 22 adopt-track** — but any single 0 on Security posture or Composability forces quarantine/reject regardless of total.

## Statuses

| Status | Meaning |
|---|---|
| `adopted` | Approved for use; indexed and installable. |
| `sandbox` | Promising; being tested in isolation before a decision. |
| `track` | Market/product signal worth watching; not adoption-ready. |
| `rejected` | Vague, risky, obsolete, or **redundant** — redundancy with Qor-logic or a built-in is a rejection reason on its own. |
| `quarantined` | Useful but dangerous without strict permissioning; never auto-loaded. |

## Permission tiers

Every candidate is classified by the highest-impact action it can trigger. Only the first two tiers may run without explicit human approval.

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

## Security review checklist (before any adoption)

- Inspect all scripts and bundled resources.
- Check for external network calls, secret handling, destructive file operations, and dependency installs.
- Verify version compatibility; run in a sandbox first.
- Record expected tool permissions in the registry entry.
- Confirm the skill declares when it should be used AND when it must not be used.
- Check for conflicts with repo-level rules (CLAUDE.md, AGENTS.md, Qor-logic doctrines, MCP policies).

## Redundancy guard

Before adopting, check in order:

1. **Qor-logic** (`../Qor-logic/qor/skills/`) — anything gated/SDLC. If covered, reject with `covered_by`.
2. **Claude Code built-ins** (`/code-review`, `/security-review`, `/verify`, etc.).
3. **Vendored official repos** (see INDEX.md) — prefer the official implementation over a community clone.
4. **This repo's local skills and ROADMAP** — if it's planned here, track it against the roadmap item instead of adopting a third-party version.

Two skills that answer the same trigger are worse than one: they create conflicting process authority and bloat context. When in doubt, reject the duplicate and link the survivor.
