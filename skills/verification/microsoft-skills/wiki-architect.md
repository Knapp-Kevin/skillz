# Verification: Microsoft Skills `wiki-architect`

- Source family: `microsoft-skills`
- Canonical path: `.github/plugins/deep-wiki/skills/wiki-architect`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `124c5bec7008b1e25940cfc67ea09b069af0dbea`
- `SKILL.md` blob: `53bcf7016efbba50e4f634a7a4b4a40cddcb2234`
- Static disposition: **verified**
- Score: **17/20**
- Behavioral validation: **not-run**
- Controlled tags: `documentation`, `architecture`, `planning`, `source-driven`, `evidence-first`, `synthesis`, `read-only`, `medium`

## Structured semantic review

### Useful material to preserve

The skill has strong source-grounding discipline for documentation planning. It requires repository context resolution before analysis, scans the actual tree and README, derives titles from repository content rather than generic placeholders, requires every generated section prompt to reference real files, bounds catalogue nesting and fan-out, and adapts depth for very small repositories. Its four-audience onboarding model, architecture layering, comparison-language heuristic, and explicit linked-versus-local citation modes are useful prior art for producing navigable documentation plans from code evidence.

### Authority and safety

No authority hard fail was found. The canonical procedure is read-only: it inspects repository state, runs observational Git commands, and emits a JSON catalogue. It does not direct persistent workspace mutation or consequential external actions. A host should still treat any later act of writing generated documentation into the repository, committing/pushing it, or publishing private repository-derived material as a separate consequential action requiring its own authorization boundary.

### Limitations and failure handling

The skill correctly refuses to proceed until source repository context is resolved, but its host assumptions are somewhat narrow. It assumes Git command access for remote and branch discovery and does not fully specify fallback behavior for non-Git hosts, detached HEADs, inaccessible remotes, or partial repository snapshots. The audience-specific guide requirements can also invite unsupported business, cost, risk, or product claims if an agent treats the requested sections as a requirement to fill every field rather than as evidence-bounded prompts. Adaptations should preserve explicit unknowns and omit claims the repository cannot support.

### Secret and sensitive-data discipline

The package does not solicit credentials or require disclosure to an external service. Because repository scanning may encounter secrets, credential-bearing URLs, private deployment data, PII, or sensitive configuration, generated catalogue prompts and citations should not reproduce such values. External publication of private repository-derived documentation is outside the skill's read-only authority profile and requires separate disclosure authorization.

### Trigger and non-trigger boundary

Use when the user wants a repository-grounded wiki/documentation catalogue, architecture map, onboarding structure, or documentation plan. Do not use as authority to modify repository files, publish generated documentation, or infer organizational/business facts not evidenced by the repository. For tiny repositories, preserve the package's reduced-depth rule instead of forcing a full architecture hierarchy.

## Rubric notes

- Trigger precision: 2/2
- Procedural clarity: 2/2
- Authority and safety: 2/2
- Failure handling: 1/2
- Evidence discipline: 2/2
- Dependency coherence: 1/2
- Portability honesty: 1/2
- Usefulness/differentiation: 2/2
- Adversarial resilience: 2/2
- Effectiveness design: 2/2

Total: **17/20**. No current hard-fail condition is unresolved.

## Validation note

This review inspected the exact registered-pin one-file package statically. No external repository was analyzed behaviorally, no documentation catalogue was generated as representative scenario evidence, no files were written, and no publication or repository mutation was performed. Behavioral validation therefore remains `not-run`.
