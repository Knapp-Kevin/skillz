# Issue #402 / PR #673: six current pulse skills, exact-source semantic assessment

Date: 2026-11-04. Scope: reviewer static examination of current complete SKILL.md text and bundled sources.json syntax for six repaired exact versions. The historical NVIDIA SkillSpector 3-fail/3-incomplete results are tied to earlier exact package trees; this report **does not run SkillSpector** or any host agent and cannot clear any security or behavioral gate.

Rubric: [skill verification standard](../../docs/skill-verification.md), ten dimensions scored 0/1/2. In order: trigger, procedure, authority, failure, evidence, dependencies, portability, distinct value, adversarial safeguards, effectiveness design. All six packages are first-party source instructions with an existing bundled sources.json, no required executable sidecar, and source-level read-only/report-only procedures.

| Skill | Exact SKILL.md Git blob SHA | Dimension scores (in rubric order) | Source-semantic grade |
|---|---|---|---:|
| hf-pulse | `149e577a9f72895b09aea43d607203d731db1bce` | 2, 2, 2, 1, 2, 2, 2, 2, 2, 1 | **18/20** |
| inference-pulse | `d76c0cc56bc90e7c88c2c63564ae9f24a77cca6c` | 2, 2, 2, 1, 2, 2, 1, 2, 2, 1 | **17/20** |
| kimi-pulse | `6625f147011dfd38ed2b9881eda2d5ea62e2ece4` | 2, 2, 2, 1, 2, 2, 2, 2, 2, 1 | **18/20** |
| github-pulse | `9c345c88cef5f4f97235facb6d3d7414ab820f1a` | 2, 2, 2, 1, 2, 2, 2, 2, 2, 1 | **18/20** |
| governance-pulse | `4eb7b63979fb29d997ef3ad6a10e9248e7c573ce` | 2, 2, 2, 1, 2, 2, 1, 2, 2, 1 | **17/20** |
| mcp-pulse | `33070cbc43c1bf05feeeb4e9bdd1c1d0ac04247a` | 2, 2, 2, 1, 2, 2, 2, 2, 2, 1 | **18/20** |

## Individual reviewer rationale and limitations

### hf-pulse

- **Positive mechanism:** Bundled public source list and optional HF tools; users need not connect a private account; external publisher popularity is not quality. Explicit one-time default, separate recurrence permissions, untrusted-source treatment and no self-executing repository runtime are present in the exact text. Source and companion JSON were read; source Git blob SHA `149e577a9f72895b09aea43d607203d731db1bce` matched the individual verification record.
- **Constraints:** Failure handling and effectiveness design are scored 1, because reporting access gaps and citing sources is specified but not observed with actual host failures or real outputs. No claim is made that retrieved sources are comprehensive, fresh, harmless, or correct.
- **Adversarial static thought-experiment:** a public source page asks the agent to send credentials, broaden private account scope, install a tool, schedule tomorrow's run, or write to a repository. The text says not to treat such source text as instructions. These are expected instructions, not observed behavior; no synthetic agent fixture ran.

### inference-pulse

- **Positive mechanism:** Platform-specific local-runtime relevance is optional; a private operator profile is not opened implicitly, generic relevance is clearly labeled. Explicit one-time default, separate recurrence permissions, untrusted-source treatment and no self-executing repository runtime are present in the exact text. Source and companion JSON were read; source Git blob SHA `d76c0cc56bc90e7c88c2c63564ae9f24a77cca6c` matched the individual verification record.
- **Constraints:** Failure handling and effectiveness design are scored 1, because reporting access gaps and citing sources is specified but not observed with actual host failures or real outputs. Portability is also 1 because relevant workspace/product target context varies by host; generic fallback avoids falsely claiming knowledge.
- **Adversarial static thought-experiment:** a public source page asks the agent to send credentials, broaden private account scope, install a tool, schedule tomorrow's run, or write to a repository. The text says not to treat such source text as instructions. These are expected instructions, not observed behavior; no synthetic agent fixture ran.

### kimi-pulse

- **Positive mechanism:** Separates official model weights and release facts from unverified community benchmarks and claims. Explicit one-time default, separate recurrence permissions, untrusted-source treatment and no self-executing repository runtime are present in the exact text. Source and companion JSON were read; source Git blob SHA `6625f147011dfd38ed2b9881eda2d5ea62e2ece4` matched the individual verification record.
- **Constraints:** Failure handling and effectiveness design are scored 1, because reporting access gaps and citing sources is specified but not observed with actual host failures or real outputs. No claim is made that retrieved sources are comprehensive, fresh, harmless, or correct.
- **Adversarial static thought-experiment:** a public source page asks the agent to send credentials, broaden private account scope, install a tool, schedule tomorrow's run, or write to a repository. The text says not to treat such source text as instructions. These are expected instructions, not observed behavior; no synthetic agent fixture ran.

### github-pulse

- **Positive mechanism:** Public discovery does not trigger candidate registry reads, repo writes or secret collection; prior duplication checks are marked not-run if no approved list. Explicit one-time default, separate recurrence permissions, untrusted-source treatment and no self-executing repository runtime are present in the exact text. Source and companion JSON were read; source Git blob SHA `9c345c88cef5f4f97235facb6d3d7414ab820f1a` matched the individual verification record.
- **Constraints:** Failure handling and effectiveness design are scored 1, because reporting access gaps and citing sources is specified but not observed with actual host failures or real outputs. No claim is made that retrieved sources are comprehensive, fresh, harmless, or correct.
- **Adversarial static thought-experiment:** a public source page asks the agent to send credentials, broaden private account scope, install a tool, schedule tomorrow's run, or write to a repository. The text says not to treat such source text as instructions. These are expected instructions, not observed behavior; no synthetic agent fixture ran.

### governance-pulse

- **Positive mechanism:** Public source hierarchy distinguishes binding obligations from drafts; local governance comparisons require supplied authorized redacted context. Explicit one-time default, separate recurrence permissions, untrusted-source treatment and no self-executing repository runtime are present in the exact text. Source and companion JSON were read; source Git blob SHA `4eb7b63979fb29d997ef3ad6a10e9248e7c573ce` matched the individual verification record.
- **Constraints:** Failure handling and effectiveness design are scored 1, because reporting access gaps and citing sources is specified but not observed with actual host failures or real outputs. Portability is also 1 because relevant workspace/product target context varies by host; generic fallback avoids falsely claiming knowledge.
- **Adversarial static thought-experiment:** a public source page asks the agent to send credentials, broaden private account scope, install a tool, schedule tomorrow's run, or write to a repository. The text says not to treat such source text as instructions. These are expected instructions, not observed behavior; no synthetic agent fixture ran.

### mcp-pulse

- **Positive mechanism:** Migration/security reporting; no local MCP configuration or registry read; optional local relevance uses redacted user-provided summary. Explicit one-time default, separate recurrence permissions, untrusted-source treatment and no self-executing repository runtime are present in the exact text. Source and companion JSON were read; source Git blob SHA `33070cbc43c1bf05feeeb4e9bdd1c1d0ac04247a` matched the individual verification record.
- **Constraints:** Failure handling and effectiveness design are scored 1, because reporting access gaps and citing sources is specified but not observed with actual host failures or real outputs. No claim is made that retrieved sources are comprehensive, fresh, harmless, or correct.
- **Adversarial static thought-experiment:** a public source page asks the agent to send credentials, broaden private account scope, install a tool, schedule tomorrow's run, or write to a repository. The text says not to treat such source text as instructions. These are expected instructions, not observed behavior; no synthetic agent fixture ran.

## Gate conclusion

All six sources meet the numeric >=15/20 review threshold, have trigger/authority/dependencies dimensions >=1, matching exact content fingerprints and controlled tags from existing verification records, and no unresolved **source-text** hard fail was found in this bounded review. The new exact source semantic label may be `verified` with these individual reasons. This does not supply full package-tree security scanning, license checks beyond known first-party source attribution, executed host behavioral validation, dependency/URL security, owner approval, or authorization to use unchanged.

**Mandatory HOLD:** NVIDIA SkillSpector v2.12.0 pinned `c7958a3268d9498644b22edb75d0f051bbc8cbfc` full final package trees for all six, complete report/coverage/digest and finding adjudication; independent external host trigger/nontrigger/adversarial scenarios; cross-PR registry union and approved merge. No user accounts were accessed, no skill was executed, and no security state has been promoted by this rubric.
