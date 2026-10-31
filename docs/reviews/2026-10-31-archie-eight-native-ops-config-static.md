# Archie Indian Superpowers: eight native operations/configuration exact-pin static reviews (2026-10-31)

## Live source-family macro map

Starting main `55d807d2ceabbed0f06ef269e832bcb204a84571`. The registered tracked source `a95a59d221d44b89d4fc27a52934e24fb2060ddb` has **56 canonical first-class front-mattered SKILL.md packages**: 17 core, 38 OpenClaw-native, one community. The `community/.gitkeep` marker is not a skill. At the starting tree there are **42/56** matching individual provenance/verification pairs (17 core, 25 native, 0 community) and **14 genuine gaps**; the selected eight have no prior companion paths and contain **32 source-owned files** (eight four-file packages). All upstream tools are preserved only as external reference evidence. Source license terms are incomplete (#544); no vendoring or new admission.

Remaining after this tranche: **six genuine gaps**, namely five native (`community-skill-radar`, `morning-briefing`, `skill-compatibility-checker`, `skill-doctor`, `tool-description-optimizer`) and one community (`obsidian-sync`). The current source's recurring audit, configuration, agent orchestration, skill-selection and credential-handling mechanisms overlap substantially; repeated safety vocabulary does not establish real enforcement. The entire family remains tracked and reference-only pending independent per-package qualification and source terms.

## Individual pinned package decisions

| Package | SKILL.md Git blob | Package-tree SHA | Pinned package last commit (UTC) | Static decision |
|---|---|---|---|---|
| `cron-hygiene` | `d659403c13369c4bb18d678fc2de9bb711617ec1` | `b5edf43e98b7787bc37e677884aa6a016170d99f` | `712cec3bcbdd78b253b8b0577669494e3d6b234a` / 2026-03-15T05:42:12Z | REJECT unchanged 10/20 |
| `heartbeat-governor` | `5d5dc52ffb0c4ef4967fefff4e5c0b4bf4122bfe` | `8bb52374ea77f7a1c2e6aa7f777def3833f2277f` | `6da45d4a3ed05a2448fb556229d2ec80c9b4e2f3` / 2026-03-15T18:26:56Z | REJECT unchanged 8/20 |
| `multi-agent-coordinator` | `6ec460fb2b02a9b1917d3fe59715f85982d98ba1` | `e97b0860f84a623195ac54c2c613e73429675d35` | `21a77e409ce93465b71e4ef1fd8b641d147ad386` / 2026-03-15T05:30:11Z | REJECT unchanged 11/20 |
| `workflow-orchestration` | `e4518490336b0678ef58433d61bae3823b2e2743` | `3dcbc48327a0775daccfcd5bd43e082e7759e208` | `c3d0b3ea2dba5f97624099531e03b1855bec53bc` / 2026-03-15T03:20:07Z | REJECT unchanged 11/20 |
| `openclaw-config-advisor` | `46a5b44845aa524c1e3a242edcdca0386f9dd364` | `c721b46d355b54d03382b2c2d9725de4ebc73511` | `18d87bc942313f756a81367caedb62aafcfc5ac7` / 2026-04-17T03:22:49Z | REJECT unchanged 14/20 |
| `config-encryption-auditor` | `7ee599453a3c47c31a5f1681112c238b473a6842` | `adcfabdb9dcdc08d71fd1fcbd909af4a3b500308` | `020bb9a4d88b454d5b07ea07f60587fc98d48a19` / 2026-03-15T19:19:43Z | REJECT unchanged 10/20 |
| `skill-loadout-manager` | `1d0045502d0e6cb77881a271a04e7d3124d23233` | `5e1b046ed05e991648ff10afc597466c41abc44c` | `e669a049a4ecde23c45af2081ac78d865762803e` / 2026-03-15T18:09:26Z | REJECT unchanged 10/20 |
| `installed-skill-auditor` | `b2a4f54bd8511fa431b0386446c86a58f6e8a021` | `a86d22311baaf4f678b597cc293a5ecab18e8ea0` | `757aa655cff44b2c0f2fc17cf1bb5f1d248b0e2b` / 2026-03-15T18:00:49Z | REJECT unchanged 11/20 |

Each companion preserves exact source identity, canonical manifest path, full four-file package tree SHA, manifest blob SHA, last source commit/date, bundled script/schema/example dependencies, use-case/trigger/non-trigger, side-effect/authority profile, controlled tags, score and rationale. **No package was executed, scanned or behaviorally validated.** Source-owned scripts are not repository-owned runtime.

## Systemic findings

1. **False enforcement and savings assurance.** `cron-hygiene/audit.py` iterates a hard-coded `CRON_SKILLS` table, not the live OpenClaw schedule, and `--fix-session` prints advice instead of changing configuration. `heartbeat-governor/governor.py` sets a local `paused` flag and prints notices; it neither pauses a scheduler nor aborts an already-running job or delivers alerts. Its per-run and wall-clock checks occur after the run is recorded. Advertised budget savings and safety cannot be inferred from these logs.
2. **Orchestration as bookkeeping.** `workflow-orchestration/run.py` tracks step status and accepts `--step-done` or `--complete` without executing or verifying the named skill. `multi-agent-coordinator/run.py` treats string inequality as a contradiction and retains raw output/handoff context in persistent state; timestamps depend on manually recorded heartbeats. Neither creates trustworthy independent agent authorization or semantic agreement.
3. **Sensitive config scope.** `openclaw-config-advisor/advise.py` recursively reads credential-bearing config including `.env`, persists file paths and findings, and detects keyword hints rather than validating provider routing. `config-encryption-auditor/audit.py` recursively reads private credentials, permits unapproved `chmod 600`, and its guidance models shell export of a literal secret. A global gitignore substring check is not proof that a particular repository excludes the files.
4. **Misleading skill assurance.** `skill-loadout-manager/loadout.py` changes only its own YAML state without demonstrated integration with the OpenClaw loader, despite claiming loadout activation. `installed-skill-auditor/audit.py` uses heuristic regexes, allows a self-declared new baseline for arbitrary installed code, and does not implement the advertised ORPHAN check in its audit routine. Neither is a security or runtime guarantee.
5. **Authority and privacy pattern.** All eight expose persistent state, broad private-file reads, scheduling, possible external effects, or configuration mutations without the action-specific host/user authorization required by current governance. Retain bounded, owner-supplied checklists and design ideas; reject unchanged operational use. No extra source, category or passive infrastructure is needed.

## Accounting and lifecycle

- Archie **42/56 → 50/56**; core **17/17**, native **25/38 → 33/38**, community **0/1**; genuine gaps **14 → 6**. Eligible/source denominator delta **0**.
- New companions **8 provenance + 8 verification**. **0 VERIFIED / 8 REJECT unchanged**, all scanner/behavioral states `not-run`.
- Total corpus **44 first-party / 981 → 989 third-party / 1025 → 1033 total**; registered/tracked **860 → 868**, candidate-only **121** unchanged.
- Five public surfaces reconciled atomically with this tranche. No source pin, upstream package, runtime, script, CI, scanner, test, scheduler, crawler or generator was added or changed.
- Existing first-party repair drafts #489/#492/#496 remain held for complete pinned external SkillSpector v2.12.0 evidence and independent adversarial acceptance of 36 final trees; #412/#413 are separate admission holds. License issue #544 remains externally blocked.
