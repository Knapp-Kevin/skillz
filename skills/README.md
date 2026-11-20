# Local Skill Library

This directory contains Skillz's first-party user-facing packages and capability navigation. Start from a task, then inspect the relevant complete `SKILL.md` package and its exact-version evidence.

## Browse by purpose

- [Planning & Productivity](categories/planning-productivity/)
- [File & Information Management](categories/file-information-management/)
- [Writing & Communication](categories/writing-communication/)
- [Research & Analysis](categories/research-analysis/)
- [Software & Repositories](categories/software-repositories/)
- [Agent Operations & Security](categories/agent-operations-security/)
- [Monitoring & Intelligence](categories/monitoring-intelligence/)
- [Business & Career](categories/business-career/)

The category shelves are navigation aids, not approval lists. Search the [full capability directory](../registry/capability-directory.json) and [governed review index](../registry/governed-review-name-index.json) when a task is not represented here.

## Active original skills

Canonical authored packages live under [`authored/`](authored/) and have an exact-version [authored index](../registry/authored-skills-index.json). Downloaded packages should be independently understandable offline, including the references they actually require.

Examples include [Technology Change Intelligence](authored/technology-change-intelligence/SKILL.md), [Repository Delivery Assessor](authored/repository-delivery-assessor/SKILL.md), [Context Continuation Contract](authored/context-continuation-contract/SKILL.md), and [Healthcare Contract Forensics](authored/healthcare-contract-forensics/SKILL.md). These links show available methods, **not** verified outcomes on every model or permission to inspect sensitive accounts.

## What was retired

All **44 historical Frostwulf-attributed root skill entrypoints** were retired from active selection, with complete original Git package-tree identities retained. Their functions were crosswalked to **21 original authored replacement packages**. Retirements used owner-accepted controlled procedures; the [migration ledger](../registry/migration/frostwulf-independent-replacement-ledger-20261118.json) records original and replacement paths. Independently executed host parity, the target 1.5× improvement and historical rights remain unproven. Historical packages are not reinstalled just because their source still exists in immutable Git history.

## Evidence to check before use

First-party provenance lives in [`../registry/skills/local-skills/`](../registry/skills/local-skills/), review companions in [`../registry/verification/local-skills/`](../registry/verification/local-skills/), and the local selection state in [`../registry/local-verification.json`](../registry/local-verification.json). Third-party reference sources and verified or rejected exact-version companions retain separate rights and reuse conditions.

- A **static review** rates source quality and documented boundaries, not observed host behavior.
- A **security scan**, if present, applies only to its pinned package and stated procedure.
- A **behavioral test** must provide actual, scoped host observations before its outcome can be claimed.
- **Discovery, adoption and execution** have distinct permissions. No repository file grants connector access, private reads or writes.

For contributors, see the [review rubric](../docs/skill-verification.md), [capability-adaptive standard](../docs/capability-adaptive-skill-execution.md), [provenance policy](../docs/third-party-provenance.md) and [consumer contract](../docs/consumer-discovery-and-installation.md).

## Maintainer checks

Skillz remains a **passive library** for consumers. It also contains explicitly invoked, offline maintainer QA scripts. Those scripts are not background agents and do not install or execute referenced third-party skills.

From the repository root, maintainers can check canonical capability links and retirement-route integrity:

```bash
node scripts/qa/check-authored-capability-links.mjs
node --test scripts/qa/test-retired-skill-routes.mjs
```

The [retirement audit](../scripts/qa/check-retired-skill-routes.mjs) refuses retired source reactivation, stale selectors, missing replacements, mismatched historical ledgers and broken active navigation. These are structural checks, **not** proof of skill effectiveness.

For system-wide orientation, return to the [project README](../README.md) or [agent start guide](../AGENT_START_HERE.md).
