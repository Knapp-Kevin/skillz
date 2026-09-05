# Verification: Microsoft Skills `wiki-agents-md`

- Source family: `microsoft-skills`
- Canonical path: `.github/plugins/deep-wiki/skills/wiki-agents-md`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `d41f5a10717c8a334cd4d2f2368dbfbef40d47e5`
- `SKILL.md` blob: `45e93b32d3d7f2120cb9b3b7f51e9271e3e0189c`
- Static disposition: **rejected unchanged**
- Score: **15/20**
- Behavioral validation: **not-run**
- Controlled tags: `documentation`, `repository-maintenance`, `implementation`, `source-driven`, `evidence-first`, `human-review`, `mutating`, `high`

## Structured semantic review

### Useful material to preserve

The skill provides strong repository-context guidance: inspect existing manifests/configuration before inventing commands, derive conventions from real source files, keep root and nested guidance scoped, omit irrelevant sections, preserve existing `AGENTS.md` and `CLAUDE.md` files, distinguish project context from agent personas, and encode explicit always/ask-first/never boundaries. Its concise template, real-command requirement, no-placeholder rule, generated-file non-overwrite guard, and explicit prohibition on credentials are useful prior art for agent-facing repository documentation.

### Authority hard fail

Unchanged adoption fails the current authority standard. After checking only that target files are absent, the procedure directs the agent to create `AGENTS.md` and `CLAUDE.md` files at the repository root and potentially across multiple pertinent subdirectories. Those are persistent workspace mutations. The existence checks prevent overwrite but do not establish action-specific authorization to create new files. Any adaptation must obtain explicit authorization immediately before the first persistent write, with scope covering the intended folders; additional materially broader write scope requires renewed authorization.

### Secret and sensitive-data discipline

The skill correctly says never to include credentials, API keys, or tokens. Because it scans manifests, CI configuration, project files, and source to derive commands and conventions, adaptations should also avoid reproducing secrets, credential-bearing URLs, private deployment details, or sensitive operational values that may be present in those files. Committing, pushing, or externally publishing generated guidance is a separate consequential action requiring its own authority review.

### Trigger and non-trigger boundary

Use as reference when creating or improving agent-facing repository context from real project evidence, particularly build/test commands, scoped nested guidance, project structure, code conventions, and explicit operational boundaries. Do not use unchanged as authorization to create repository files merely because they are missing, and do not overwrite existing guidance.

## Portability

High conceptual portability. The procedure is largely language- and framework-agnostic and includes evidence sources for JavaScript/TypeScript, Python, Rust, Go, Java, and .NET projects. Actual use still depends on a host agent with repository inspection and authorized write capability.

## Validation note

This review inspected the exact registered-pin one-file package statically. No `AGENTS.md` or `CLAUDE.md` was generated in an external repository, no project files were modified, no commit or push was performed, and no representative behavioral/adversarial evidence was produced. Behavioral validation therefore remains `not-run`.