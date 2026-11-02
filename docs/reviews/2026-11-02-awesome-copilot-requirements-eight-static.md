# Pinned Awesome Copilot requirements and developer-documentation tranche (2026-11-02)

Source: `github/awesome-copilot@f11a4e441c5ff061b4f8ae37952be8c602e4034e`, root MIT license blob `89bc5e962c9944cdb050887062afdaaf89be504a`. This is **source-vetting**, not governed admission or behavioral validation. All eight candidate packages have only one `SKILL.md` in their pinned containing Git trees. Individual fingerprints, scores, authority/rights findings and ten-dimension rationales: [exact ledger](../../registry/discovery/github-awesome-copilot-requirements-issues-eight-static-20261102.json).

## Macro map and decision

Before: 103/432 Awesome Copilot raw paths with terminal path-matched decisions, including 86/415 direct and 17/17 other. After: **111/432** (94 direct, 17 other), leaving **321 direct** paths. Across four sources: **193/4,813 → 201/4,813**; 4,612 raw paths without path-matched terminal decisions. This is not the distinct eligible-skill denominator, which remains unknown. Governed exact-version records remain 1,039.

| Package | Score | Candidate disposition | Decisive evidence |
|---|---:|---|---|
| `create-github-issue-feature-from-specification` | 9/20 | REJECT | Searches for duplicates but unconditionally creates or updates persistent GitHub issues without a distinct approval of target repository, issue content or write operation; specification text may contain private project details |
| `create-github-issues-feature-from-implementation-plan` | 9/20 | REJECT | Creates or edits one persistent issue per phase with no explicit authorization of target repository, issue count or content; could flood project notifications |
| `create-github-issues-for-unmet-specification-requirements` | 10/20 | REJECT | Can publish private requirements and create many GitHub issues without explicit write authority; codebase search is not proof a requirement is absent |
| `create-specification` | 14/20 | REFERENCE-ONLY | Spec creation is in the user-requested task class, but hardcoded /spec destination lacks collision check or explicit target confirmation; generic .NET CI examples are not portable evidence |
| `create-technical-spike` | 14/20 | REJECT | Moves from document drafting into code execution, experiments, external research and repository file changes without separate authorization or data-scope checks |
| `create-tldr-page` | 13/20 | REJECT | Example contains destructive git reset --hard and clean -f commands without warnings or explicit destructive-action boundary; fetching arbitrary URLs or local files needs scope checks |
| `csharp-docs` | 16/20 | REFERENCE-ONLY | Advisory-only checklist; no external writes, secret requests or privileged actions; any code edits require separate task scope |
| `csharp-async` | 13/20 | REFERENCE-ONLY | No autonomous mutation, but overly broad guidance to wrap every await in try/catch and prefer Task.FromException over throwing in async Task methods is technically misleading |

The three issue-generator procedures treat duplicate search as sufficient precondition for GitHub issue creation or update. That is **not action-specific authorization** for external persistent writes or notification. The spike procedure also invokes prototypes, tasks and file edits without a separate gate; the TLDR example includes destructive Git cleanup commands without safety bounds. Keep the useful templates and requirement-ID mapping as reference, not unchanged-use approval. The specification, C# XML documentation and C# async advice remain reference-only; the latter's exception advice needs correction before reuse.

## Package and risk evidence

Every package tree was enumerated at its exact pinned SHA; all eight contain only `SKILL.md`. No additional bundled references, scripts, or asset files are silently omitted. Root MIT scope does not license external tools or generated third-party content. All security scans and behavioral/adversarial validations are **not-run**. No GitHub issue, command, local file write, or remote action described in the candidates was executed.

The coherent family illustrates a recurring failure pattern: superficially safe planning and documentation prompts can cross into external state mutation without permission. Future host-agent adaptation should split read-only analysis, draft preparation and separately authorized publishing. The next source pass should prefer an underrepresented, genuinely unreviewed family after comparing against existing exact-version records.
