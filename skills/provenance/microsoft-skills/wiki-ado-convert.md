# Provenance: Microsoft Skills `wiki-ado-convert`

- Source family: `microsoft-skills`
- Source repository: `https://github.com/microsoft/skills`
- Source class: official Microsoft
- License: MIT
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Canonical package path: `.github/plugins/deep-wiki/skills/wiki-ado-convert`
- Canonical `SKILL.md`: `.github/plugins/deep-wiki/skills/wiki-ado-convert/SKILL.md`
- Package tree: `1a9d5144324d5891454d25e3607ca09439584eb8`
- `SKILL.md` blob: `9c030896cd815faef45a314774d37480329e1f34`
- Freshness evidence: `67ae723a23ba880e3e5c8a3e5e2320092024476e` last changed this package at or before the registered pin on 2026-04-02T16:37:09Z
- Behavioral validation: `not-run`

## Package identity and boundary

`wiki-ado-convert` is an independently front-mattered first-class skill in the registered Microsoft Skills pin under the `deep-wiki` plugin. The exact package contains one file, `SKILL.md`; ordinary plugin README, agent, and command material outside this package does not enlarge this skill boundary.

## Purpose and dependencies

The skill specifies a Node.js ESM build script that converts VitePress/GFM documentation into Azure DevOps Wiki-compatible copies. It covers Mermaid fence and syntax conversion, YAML front-matter removal, parent-relative link handling, VitePress container conversion, wiki landing-page generation, `.order` files, image copying, output verification, and npm script integration. Operational use assumes a writable project workspace, Node.js, documentation source files, and enough repository context to resolve citation/link behavior.

## Authority and portability

Authority profile: **mutating**. The skill preserves source documentation, but its intended workflow creates `scripts/build-ado-wiki.js`, writes converted documentation and support files under `dist/ado-wiki/`, may modify `package.json` for npm integration, and runs the generated converter. Its mandatory source-repository-context question is useful but is not authorization for those persistent project mutations. Unchanged adoption therefore lacks the action-specific authorization checkpoint required immediately before writing or modifying workspace files.

Portability: **medium**. The conversion mechanisms are portable across Node-capable hosts and use built-in Node modules only, but the output contract is specifically coupled to VitePress/GFM input and Azure DevOps Wiki rendering semantics.

## Secret and sensitive-data context

The package does not solicit credentials and has no direct remote publication step. Repository URLs should nevertheless be treated conservatively if they contain embedded credentials, and generated documentation copies can preserve whatever sensitive content exists in the source corpus. Any adaptation should avoid credential-bearing URLs, keep secrets out of generated/logged output, and separately authorize any later external publication or upload step.