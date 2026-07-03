# Architecture Plan

## Risk Grade

**Selected Grade**: [ ] L1  [x] L2  [ ] L3

L2: repo tooling that writes to the local working tree and (behind an explicit
apply flag) to the operator's `~/.claude/skills`. No production systems,
credentials, or third-party state are touched. No L3 surfaces (security,
financial, compliance, fundamental rights).

## System Shape

```
INDEX.md / index.json          generated registry surface (never hand-edited)
        ▲
scripts/build-index.ts         generator: scans skills/ + vendor/
scripts/lib/                   shared zero-dep helpers (frontmatter parsing)
        ▲
skills/<name>/                 first-party skills: SKILL.md + scripts/
registry/candidates.yaml       third-party intake decisions
vendor/<source>/               official skill repos (git submodules, read-only)
docs/                          governance artifacts + evaluation framework
```

## Load-Bearing Rules

1. **SKILL.md is the single source of truth** per skill; the index is derived, never authored.
2. **Scripts collect, the model synthesizes.** All scripts run zero-install on Bun or Node 22.18+.
3. **Read-only by default.** Anything that mutates beyond the working tree is dry-run by default and requires an explicit apply flag or human approval.
4. **vendor/ is immutable** from this repo's perspective — refreshed only via `git submodule update --remote`, never edited.
5. **Repo-bound vs portable skills**: skills whose scripts depend on this repo's tree (meta-tooling) declare `repo-bound: true` in frontmatter metadata and are excluded from deployment sync.

## Module Boundaries

- `scripts/` — repo tooling (index generation, shared lib). May read the whole tree.
- `skills/<name>/scripts/` — skill payloads. Portable skills are self-contained; repo-bound skills may import `scripts/lib/`.
- `registry/` — data only, no code.
- `.qor/`, `docs/META_LEDGER.md` — Qor-logic governance artifacts; written by gates, read by audits.
