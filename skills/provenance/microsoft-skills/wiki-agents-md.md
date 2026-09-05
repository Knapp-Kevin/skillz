# Provenance: Microsoft Skills `wiki-agents-md`

- Source family: `microsoft-skills`
- Source repository: `https://github.com/microsoft/skills`
- Source class: official Microsoft
- License: MIT
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Canonical package path: `.github/plugins/deep-wiki/skills/wiki-agents-md`
- Canonical `SKILL.md`: `.github/plugins/deep-wiki/skills/wiki-agents-md/SKILL.md`
- Package tree: `d41f5a10717c8a334cd4d2f2368dbfbef40d47e5`
- `SKILL.md` blob: `45e93b32d3d7f2120cb9b3b7f51e9271e3e0189c`
- Freshness evidence: `4cf58ce31ea6e814a21ff4db46b5f52391ba8bfc` last changed this package at or before the registered pin on 2026-02-13T02:28:22Z
- Behavioral validation: `not-run`

## Package identity and boundary

`wiki-agents-md` is an independently front-mattered first-class skill in the registered Microsoft Skills pin under the `deep-wiki` plugin. The exact package contains one file, `SKILL.md`; adjacent deep-wiki commands, agents, README material, and sibling skills are outside this skill boundary.

## Purpose and dependencies

The skill teaches an agent to derive repository-specific `AGENTS.md` context files from existing project evidence, with exact build/test commands, project structure, code conventions, git workflow evidence, and explicit operational boundaries. It also directs creation of a small `CLAUDE.md` redirect companion. Operational use assumes read access to repository manifests, source/configuration files, CI configuration, and a writable workspace for folders where the files are absent.

## Authority and portability

Authority profile: **mutating**. The skill has a strong non-overwrite guard and instructs the agent to skip any existing `AGENTS.md` or `CLAUDE.md`, but it still directs creation of new persistent files across the repository without a mandatory action-specific authorization checkpoint immediately before those writes. File absence is a safety precondition, not authorization to mutate the workspace.

Portability: **high**. The method is language-agnostic, adapts to common build manifests and repository layouts, and depends mainly on the host agent's ability to inspect repository evidence and write Markdown files.

## Secret and sensitive-data context

The skill explicitly prohibits putting secrets, API keys, or tokens in generated `AGENTS.md` content and relies on repository-local evidence rather than requesting credentials. Adaptations should also avoid reproducing credential-bearing URLs, private operational data, or sensitive configuration values discovered while scanning source and CI files. External publication or committing/pushing generated guidance remains a separate consequential action requiring its own authority.