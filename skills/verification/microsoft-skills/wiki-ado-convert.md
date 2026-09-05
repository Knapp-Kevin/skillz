# Verification: Microsoft Skills `wiki-ado-convert`

- Source family: `microsoft-skills`
- Canonical path: `.github/plugins/deep-wiki/skills/wiki-ado-convert`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `1a9d5144324d5891454d25e3607ca09439584eb8`
- `SKILL.md` blob: `9c030896cd815faef45a314774d37480329e1f34`
- Static disposition: **rejected unchanged**
- Score: **15/20**
- Behavioral validation: **not-run**
- Controlled tags: `documentation`, `implementation`, `verification`, `compatibility-aware`, `deterministic`, `source-driven`, `tool-assisted`, `mutating`, `medium`

## Structured semantic review

### Useful material to preserve

The skill provides high-signal deterministic conversion guidance for moving VitePress/GFM documentation into Azure DevOps Wiki format: an explicit incompatibility matrix, scoped Mermaid transformations, front-matter removal, link-preservation rules, built-in-only Node.js implementation guidance, skipped-directory boundaries, non-destructive source/output separation, landing-page quality requirements, `.order` generation, image copying, citation preservation, and a concrete post-conversion verification checklist. Its requirement to resolve whether the source repository is local-only or remotely addressable before generation is also a useful provenance/citation safeguard.

### Authority hard fail

Unchanged adoption fails the current authority standard. The skill directs the agent to generate `scripts/build-ado-wiki.js`, write a transformed documentation tree under `dist/ado-wiki/`, create `.order` files and a landing page as needed, integrate an npm script in project configuration, and run the generated converter. Those are persistent workspace mutations. The preliminary question about source-repository context resolves link behavior, but it is not an action-specific authorization checkpoint for creating or modifying project files. Any adaptation must obtain explicit authorization immediately before the first persistent workspace mutation and again before materially modifying existing project configuration when that scope was not already authorized.

### Secret and sensitive-data discipline

No direct credential solicitation or external publication occurs in the skill. The generated copies can preserve source documentation content and linked repository URLs, so adaptations should reject credential-bearing URLs, avoid copying secrets or sensitive material into broadly visible output locations, and treat any subsequent Azure DevOps publication/upload as a separate externally consequential action requiring its own authority and disclosure review.

### Trigger and non-trigger boundary

Use as reference when converting VitePress/GFM documentation for Azure DevOps Wiki compatibility, especially Mermaid syntax, front matter, relative links, container directives, landing pages, ordering files, and deterministic verification. Do not use unchanged as authorization to create scripts, alter `package.json`, write generated documentation, or publish documentation externally.

## Portability

Medium unchanged portability. The generated implementation uses only Node.js built-ins and the transformation logic is straightforward to adapt, but the procedure assumes VitePress/GFM source conventions, Node-capable project workspaces, and Azure DevOps Wiki-specific output semantics.

## Validation note

This review inspected the exact registered-pin one-file package statically. No script was generated, no project file or npm configuration was modified, no documentation tree was transformed, no Azure DevOps Wiki was published, and no representative external behavioral/adversarial evidence was produced. Behavioral validation therefore remains `not-run`.