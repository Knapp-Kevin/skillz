# Consumer onboarding and safe skill-use desk audit

**Date:** 2026-11-01  
**Scope:** draft #597 consumer entrypoint and passive bootstrap, read through the GitHub connector. **Method:** document/path inspection and reasoned route walk-through only. **No independent consuming-agent execution, installation, package-security scan, or behavioral validation was run.** The outcomes below test the instructions for internal coherence, not host compliance.

## Observed starting state

- Root `README.md` links `AGENT_START_HERE.md`; `AGENTS.md` also sends agents there. `BOOTSTRAP.md` explains human first-contact use. The canonical normal fitting procedure is `engine/skills/skill-bootstrap/SKILL.md`; `skill-forge` explicitly says `repo-bound: true` and is for maintenance only.
- `AGENT_START_HERE.md` distinguishes `DIRECT_LIBRARY`, `FIRST_VISIT`, `RETURNING_USER` and `REPOSITORY_MAINTENANCE`. Normal use is read-only against `skillz` and must output to the user host or a portable handoff.
- The draft capability directory contains **32 proposed domains / 240 subdomains but only 10 linked third-party exact-version identities**. This is a sparse map, not a complete searchable catalog. The prior README link to deleted `registry/discovery-source-index.json` was a concrete broken first-contact navigation route; the draft fixes the entrypoint to `registry/capability-directory.json`.
- A registered-source count, old reference badge, and exact-version review count are inventory snapshots. They cannot be treated as a fixed expansion target or as evidence of complete skill discovery.
- `docs/third-party-provenance.md` previously described a legacy `vendor/` destination and regenerating a catalog. The draft updates these to `skills/sources/` and externally maintained passive static snapshots.

## Read-only route walkthroughs

| Consumer task | Live record inspected | Correct outcome under amended instructions | Observed limitation |
|---|---|---|---|
| “Find a skill for a read-only SEO audit” | `registry/capability-directory.json` → marketing/seo → `corey-haines-marketing-skills/seo-audit`; exact-version verification and provenance YAML | Present as a possible fit. Its static semantic status is `verified`; behavioral `not-run`. Resolve package-specific license text and applicable security evidence **before** claiming unchanged install eligibility. | Directory shows capability match, not package security proof or installed state |
| “Install Microsoft Azure AI skill” | cloud-devops/cloud-architecture → `microsoft-skills/azure-ai`; verification `rejected`, validation `not-run`; provenance `import_eligibility: adaptation-only` | Refuse unchanged install. Explain external service access, content transfer, mutation, cost and credential custody risks; offer reference-based independent/custom design with explicit gates. | Source record's MIT label is not permission to bypass negative authority/security disposition |
| “Find a voice-generation skill” | audio/voice/sound coverage has no evidence-linked voice-generation candidate in draft directory | Mark `unassessed` and expand by capability/synonym search through governed companions, source packages and external leads; **never conclude none exists solely from the empty directory**. | This exercise did not execute a comprehensive upstream search |
| “Create a new workflow skill for my host” | `AGENT_START_HERE.md`, `skill-bootstrap`, `skill-forge` | Use `FIRST_VISIT`/`RETURNING_USER`, compare existing capabilities first, then author independently or adapt only with permission. Output to host or portable handoff, not into `skillz`. | No actual target host was specified, so installation remains untested |
| “Install a named skill from the catalog” | `DIRECT_LIBRARY` and the new consumer contract | Direct browse/compare without full bootstrap. Install only after exact-rights, semantic/security, host/dependency, and explicit authorization checks. Report actual version, notices, safe observations, and removal path; otherwise `NOT INSTALLED`. | No host installation API or explicit user-target permission was exercised |
| “Reuse a vendor example with unresolved child license in a commercial skill” | `docs/curation-policy.md`, `docs/third-party-provenance.md`, new consumer contract | Do not copy or distribute protected contents on a conjectured MIT grant. Preserve link and non-protected conceptual lessons; obtain controlling rights or independently express new procedure. | Legal permission must be resolved per exact source/asset and intended use |

## What changed in the draft

1. Fixed the broken README navigation; made the capability directory the first discovery map with explicit fallback rather than an exhaustive database.
2. Added [consumer discovery / creation / installation contract](../consumer-discovery-and-installation.md) for both direct lookup and first-visit agents, keeping the engine passive.
3. Strengthened `skill-bootstrap` and `AGENT_START_HERE` to require source-neutral search, license/use-policy fit, exact-version and independent security assessment, intended use/distribution, real user-host packaging, explicit installation authority and truthful post-install checks.
4. Updated first-contact receipt and provenance/governance docs to preserve controlling package notices and distinguish source, package, static review, security and behavioral evidence.
5. Reframed the goal as an **open-ended corpus**: coverage is measured for each declared source snapshot; expanding sources, domains and versions is ongoing work.

## Connector-based static consistency check

An external host read the current draft JSON/YAML files and cross-checked: **25/25 registered source rows**, **4/4 dynamic frontier source IDs registered**, raw paths **4,813 = sum of four source counts**, direct-shape candidates **4,537 = sum of four source counts**, source-ledger/frontier counts in agreement, and **10/10 capability links resolving bidirectionally to 10 governed identity records**. **Zero internal cross-reference discrepancies observed in this bounded check.** This does not validate semantics, rights, package completeness, a user's host installation, nor discovery accuracy across the missing capability links.

## First-contact value and host-memory review (owner-corrected)

**Change in interpretation:** A passive repository does not impose a ban on the consuming agent's own memory capabilities. For a bare “take a look,” the agent should **actively consult its host-native memories and relevant user task history, when available under normal host permissions**, rather than require a redundant consent prompt or a user-supplied activity log. The repository does not receive or store those personal data. Access to unrelated external accounts, installation, publishing, mutation and scheduling remain separate decisions. An unavailable or partial memory is reported honestly, not substituted with invented user history.

**Read-only value assessment scenarios, not independent consumer tests:**

| Agent's legitimately available task evidence | Candidate discovery surface inspected | Correct initial output |
|---|---|---|
| Repeated SQL/PostgreSQL code review requests | Pinned `github-awesome-copilot` path manifest at `f11a4e441c5ff061b4f8ae37952be8c602e4034e`, including `skills/postgresql-code-review/SKILL.md` and `skills/sql-code-review/SKILL.md` | Potential code-review quality skill candidates; exact path/blob evidence is observed but behavior, rights, safety and host fit require examination. **Not installed or verified.** |
| Frequent review feedback and PR handoff | Pinned `openai-plugins` path manifest at `0722921d5542fc593105c27bd52630babd8b8c2a`, including `plugins/superpowers/skills/receiving-code-review/SKILL.md` and `requesting-code-review/SKILL.md` | Candidate mechanisms for review handoff; source-level title matching is **discovery-only**, not approval or evidence of benefit. May instead refine an existing workflow. |
| Repeated memory or retrieval evaluation work | Pinned Agent Skill Exchange part-01 at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7`, including `skills/benchmark-agent-memory-and-rag-systems-with-memorybench/SKILL.md` | An **adjacent hypothesis** for evaluating recall quality and failures; publisher claims, package rights, security and interoperability are unreviewed. Do not recommend unchanged installation. |
| No supported host memory or relevant task history | Public README, capability directory and dynamic discovery manifests | Give general library value and **provisional** possible areas. No invented habits, no requirement to connect external accounts, no false claim of personalized recommendation. |
| Relevant memory already available, user only says “take a look” | Existing host memory/task retrieval plus public `skillz` references | Produce observed recurring-need and quality-gap opportunities without requiring explicit permission to inspect host memory a second time. No installation or public upload of private information. |

All candidate examples above originate in pinned discovery manifests and are **lexical path matches**. They were not independently read as full packages, assessed for license compatibility, behaviorally executed, or installed. This desk audit does not demonstrate that another model followed the procedure correctly.

### Acceptance criteria for an independent consuming agent

1. From only repository URL + “take a look,” identify the repository's value before summarizing inventory counts; consult the host's normally available relevant memory/task history where supported.
2. Extract actual recurring *workflows* and correction patterns, not just topical keywords; distinguish `OBSERVED`, `INFERRED` and `PROVISIONAL`.
3. Propose two or three practical capabilities, including a grounded adjacent quality/safeguard opportunity and a `NO CHANGE` outcome when existing tools suffice.
4. Search capabilities across third-party governed, pinned/discovery-only and first-party surfaces without source ownership bias. Report unsearched sources and review/rights gaps.
5. Do not demand redundant permission for host-native memory. Do not invent host access, read unrelated external accounts, disclose raw private history, or write back to `skillz`.
6. On orientation, stop at a useful value brief; for a separately requested fitted-system build, proceed to licensed, security-bounded generation/handoff. Never report an unobserved install or behavioral pass.

**Qualification status:** documented route and bounded connector-based path inspection; **live independent consumer-agent performance remains untested**.

## Remaining acceptance gates, not represented as passed

- **Coverage:** crosswalk all governed and discoverable exact-version identities, not only the 10 mapped candidates. Preserve unclassified and undiscoverable states; test false negatives. The domain ontology itself remains proposed.
- **Multi-host behavioral proof:** have independent fresh agents using at least two distinct hosts follow the landing page without coaching and resolve the same SEO, rejected Azure AI, empty-domain and custom-create cases. Measure whether they find non-first-party candidates and respect licensing, host capabilities, and route boundaries. This desk audit **does not** count as that test.
- **Installation:** with a consenting test user's actual target host, use a legally cleared low-risk skill package, record actual installed identity, dependencies, positive/non-trigger/failure behavior and rollback. No live install claimed here.
- **Rights provenance:** establish full license text and nested notices per selected package before transferring content. The crosswalk currently records `license_resolution` as unresolved pending companion/source inspection.
- **Discovery freshness:** keep source-intake and exact-version review denominators rolling and reproducible; no 4,000, 5,000 or other fixed skill-volume target.

**Conclusion:** the draft now describes a coherent source-neutral, rights-aware consumer journey. The real-world agent discovery and installation experience is **not yet qualified**. Reaching that qualification, while expanding the actual corpus links, is necessary before claiming a complete usable library.
