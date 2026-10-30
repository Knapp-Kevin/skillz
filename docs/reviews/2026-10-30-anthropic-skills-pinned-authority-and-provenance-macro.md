# Anthropic Skills: pinned authority and provenance macro review (2026-10-30)

## Exact source and denominator

Registered source: `anthropic-skills`, `https://github.com/anthropics/skills`, gitlink and `registry/sources.yaml` pin `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4`. The pinned upstream tree contains **19 first-class `skills/*/SKILL.md` packages** and one `template/SKILL.md` example, excluded from the eligible denominator. No alias, mirror, nested first-class duplicate, or new admission changes the 19 eligible identities. Source material remains an intact upstream gitlink under `skills/sources/anthropic-skills`.

The 19 exact-version provenance and verification pairs already existed, so **static gaps 0 → 0** and **denominator 19/19 → 19/19**. This tranche fixes semantic misclassification and source-identity wording, not missing records. All 19 provenance files and 19 verification files were read and reconciled against the registered pin. Candidate-only language remained after pin advancement; the records now describe current pinned evidence, without silently granting package-security or behavioral acceptance.

## Ten-package bounded authority tranche

| Pinned skill | Before | Current decision | Evidence |
|---|---|---|---|
| `skill-creator` | VERIFIED 18/20 | **REJECT unchanged 15/20** | Default paired subagent runs and grading, background reviewer, persisted eval outputs, and iterative model-trigger optimization lack independent cost, private-input, scope, retention, and side-effect authorization |
| `webapp-testing` | VERIFIED 16/20 | **REJECT unchanged 14/20** | Starts local application servers and directs browser interactions without a gate for authenticated writes, connected backend mutations, notifications, or private browser state |
| `internal-comms` | VERIFIED 15/20 | Retain VERIFIED semantic only | Generates communication drafts and routes to bundled formats; does not itself direct sending |
| `mcp-builder` | VERIFIED 16/20 | Retain VERIFIED semantic only | Source and SDK freshness matter; evaluation examples explicitly favor read-only questions; host-local build work is distinguishable from production deployment |
| `doc-coauthoring` | REJECT 13/20 | Retain REJECT unchanged | Unresolved package terms and broad private organizational context; staged drafting and reader-testing remain adaptation evidence |
| `web-artifacts-builder` | REJECT 13/20 | Retain REJECT unchanged | Mutable, unpinned executable dependency/scaffold graph |
| `pdf` | REJECT 17/20 | Retain REJECT unchanged | Proprietary package terms restrict unchanged reuse |
| `docx` | REJECT 17/20 | Retain REJECT unchanged | Proprietary package terms restrict unchanged reuse |
| `pptx` | REJECT 17/20 | Retain REJECT unchanged | Proprietary package terms restrict unchanged reuse |
| `xlsx` | REJECT 17/20 | Retain REJECT unchanged | Proprietary package terms restrict unchanged reuse |

`skill-creator` exact `SKILL.md` blob `65b3a402dbd09b8e83f9d637c6b553875189085c`, package tree `3cf9a8db32597ba3e24b584a3d696f4e11c7d7b6`. Source steps 143–171 ask for test prompts and then launch paired subagents; steps 221–251 grade and launch a background viewer; steps 375–395 run an optimization loop that can call models repeatedly. These are useful design methods, but creating a skill is not blanket permission for paid multi-agent evaluation, sensitive prompts in test runs, persistent workspaces, or a background server. The prompt examples even encourage realistic personal context and file paths. No observed execution or exploitation is claimed.

`webapp-testing` exact `SKILL.md` blob `4726215301db64a0cc4d41fc3219c61f37a30f4a`, package tree `5ffb7dc66b9fd4c25c3e400a4c00da99a349b714`. The source directs `scripts/with_server.py` to launch a dev server and browser scripts to execute discovered actions. It does not require explicit approval for state-changing controls or separate private/authenticated context. The helper is source-owned, retained as upstream evidence, not a repository-owned runner.

Both packages retain valuable ADAPT/EXTRACT/CHECKLIST methods: holdout and baseline evaluation, assertion design, reviewer feedback, selector discovery, screenshot evidence, and cleanup. Neither is suitable for unmodified use under the current authority hard fail. Their behavioral state remains `not-run`; no external SkillSpector evidence was created.

## Macro synthesis

- **Authority:** benign labels such as skill creation or UI testing do not authorize paid background agents, local server lifecycles, connected-app writes, notifications, or private-data disclosure. Read-only evidence, local generation, persistent mutation, and external effects need distinct boundaries.
- **Privacy and freshness:** realistic eval prompts can contain private file paths and personal context. Browser sessions may expose authentication or live backend state. Mutable SDK documentation remains a freshness dependency for `mcp-builder`; proprietary document-package licenses remain hard restrictions.
- **Capability overlap:** skill authoring and web testing overlap existing first-party methods but provide useful evaluation/selector techniques, not a quota-based reason for unchanged adoption.
- **Accounting and omission:** stale candidate-only wording appeared in all 19 provenance and 19 verification companions even though the current gitlink already matches their `source_snapshot_revision`. Corrected that lifecycle drift without changing source identity, content fingerprints, package trees, licenses, source admission, or the controlled taxonomy.
- **Family result:** **12 VERIFIED / 7 REJECT unchanged → 10 VERIFIED semantic only / 9 REJECT unchanged**; **19/19** current-standard, **0** static gaps. First-party 44, third-party reviews 826, total 870 unchanged. No scanner or behavioral pass inferred.

## Lifecycle

Five public accounting surfaces were reconciled together: `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json`. No existing first-party repair or admission PR was modified. Those drafts remain separately held for exact-package security and independent adversarial acceptance. No repository-owned runtime, scripts, CI, scheduler, scanner, or background machinery was added.
