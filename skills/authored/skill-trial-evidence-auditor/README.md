# Skill Trial Evidence Auditor

Standalone, offline first-party skill for assessing **whether a skill effectiveness claim has legitimate comparative evidence**. It neither launches model evaluations nor replaces the repository's static skill review process.

Start with [SKILL.md](SKILL.md). The [receipt contract](references/trial-contract.md), [adversarial acceptance cases](examples/acceptance.md) and optional [Python standard-library checker](scripts/audit_trials.py) ship within this single package. The executable method has [local tests](tests/test_audit_trials.py) and an explicitly **synthetic** [example receipt](examples/synthetic-trial-receipt.json).

Without Python, follow the complete main procedure and clearly label calculations not executed. External benchmarking runners and vendor links are optional, not dependencies. No host access, scheduling, persistence, installation, model calls or evaluation credits are granted by reading this package.
