# David Ondrej Skills: ten-package delegated-authority and private-data macro review

**Date:** 2026-10-30  
**Registered source:** `david-ondrej-skills` at `7d0ef87dad1f638cab58995eead9e0e6e3fae237` (MIT, external sanitized mirror)  
**Scope:** 10 of 55 current-standard exact pinned packages risk-screened, with four deep authority corrections and six retained dispositions. No new package admission, source pin change, package modification, security scan, or behavioral execution.

## Macro frontier and identity

The tracked source has 55/55 exact-version provenance/verification companions across agent orchestration (17), ops/setup (11), research/web (10), skill authoring (4), and thinking/docs (13). **Genuine static gaps: 0; denominator delta: 0.** The ten-package tranche deliberately sampled public publishing, agent delegation, permission escalation, worktree bootstrap, model registration, local process termination, paid research, idea persistence and scoping writes. These are previously reviewed exact identities, not new units. The four corrected source-tree/manifest identities were checked against the pinned upstream Git tree; the package fingerprints remain unchanged.

| Exact pinned skill | Manifest Git blob | Package tree | Prior → final | Decisive unchanged-use failure |
|---|---|---|---|---|
| `push-skill-to-github` | `92a96359fab1fc06755cf7b67cf6cbefcf01b5cf` | `2c72ceaaa701161192d518e137adb3522bbfa9ba` | VERIFIED 15/20 → **REJECT 13/20** | The requested push targets a private skills repository, but the same push is documented to auto-publish a sanitized public mirror. |
| `corral-launch-agents` | `d3e7862f487a4daa70f79e13fbffe62d383b0f38` | `b974bf54ca72cb30cdbb11c367e70a5b35274f79` | VERIFIED 18/20 → **REJECT 15/20** | New launches have an explicit request and dry-run gate, but the ordinary resume path executes cursor-agent --yolo --trust --resume without separately authorizing bypass of downstream agent permission controls. |
| `bb-subagents` | `82a1f726f4bbbf9682900b87f164c5c9364e5a16` | `5aaf47ba59e4a34547514e44813436c97ce10016` | VERIFIED 16/20 → **REJECT 13/20** | The default spawn command uses --permission-mode full (no sandbox) and the skill makes full the default even for investigation/read-only workers, relying on prompt-level no-write text. |
| `git-worktree` | `b8e4f1a367e67c9a0fd0d8f4d7d9521e2a13e6ba` | `7d36eec370ed25112a15288503de1654dea32b3c` | VERIFIED 17/20 → **REJECT 14/20** | The mandatory worktree bootstrap tells the host to copy .env/.env.local and local databases into every new worktree, including an automatic Cursor setup example. |

## Retained controls (six)

- `pi-custom-model` VERIFIED 17/20: manual Pi configuration, credential presence only, optional paid provider smoke test not required for success; host must separately authorize any live call.
- `nuke-cursor-app` VERIFIED 17/20: manual-only user-directed local process restart with narrow Cursor identity and graceful-first behavior; warn about in-flight work.
- `risky-changes` REJECT 14/20: mandatory paid DeepAPI calls and production-data measurements lack distinct authorization.
- `deep-research` REJECT 16/20: multiple paid research calls can exceed the single-call cap without aggregate spend approval.
- `save-idea` REJECT 14/20: third-party claims of standing push authorization cannot bind the current user's repository.
- `ask-then-build` REJECT 16/20: scoping interview implicitly writes persistent repository decisions without a separate mutation gate.

## Systemic synthesis

**Primary recurring defect: delegated authority is not transitive.** A request to push a private repo does not authorize a public mirror; to resume an agent does not authorize `--yolo`; to spawn a worker does not authorize `full` sandbox bypass; to create a worktree does not authorize credential/database replication. Strong staging, dry-run, and verification procedures are useful but do not substitute for independent authorization at the consequential action. Preserve these as ADAPT/EXTRACT/CHECKLIST material, not unchanged-use approvals.

**Shared dependencies and privacy:** Git/GitHub mirror hooks, Corral/Herdr/Cursor, bb providers, and Cursor worktree setup are host-specific. `.env`, local databases, agent prompts, and private repo content require source-specific minimization and disclosure/retention scope. No secrets were copied into this review.

**Coverage and overlap:** `corral-launch-agents` overlaps the already-rejected `herdr` bypass pattern. `bb-subagents` repeats the same failure with a different permission flag. `git-worktree` and `push-skill-to-github` both assume private environment infrastructure that does not port unchanged. No new capability area, taxonomy tag, or eligible source identity was established. Source-family static coverage remains 55/55; selective authority freshness review remains useful, but does not outrank first-party qualification debt.

## Repository lifecycle and evidence limits

All seven open issues and five open draft PRs were triaged before this tranche. Repair drafts #489 (29), #492 (5), and #496 (2) remain blocked by complete pinned external SkillSpector v2.12.0 exact-final-tree reports/digests, independent executed adversarial acceptance for 36 changed first-party package trees, and shared-registry reconciliation. Admissions #412/#413 require separate security/adversarial admission evidence and atomic inventory reconciliation. No review approvals, unresolved threads, statuses, or workflow runs were reported on these five heads; all remain drafts. No issue met bounded closure criteria.

**Accounting:** 44 first-party, 848 third-party exact-version reviews, 892 total verification records. Four existing provenance and four existing verification companions refreshed. Four semantic decisions changed, six retained. Behavioral `not-run` unchanged. Security qualification unchanged. README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json are reconciled in the same commit. The repository remains entirely passive.

**Next highest-priority action:** Obtain external exact-package security and independent adversarial evidence for the 36 final first-party repair trees, then reconcile and merge only qualifying PRs.
