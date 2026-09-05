# Provenance: Microsoft Skills `wiki-architect`

- Source family: `microsoft-skills`
- Source repository: `https://github.com/microsoft/skills`
- Source class: official Microsoft
- License: MIT
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Canonical package path: `.github/plugins/deep-wiki/skills/wiki-architect`
- Canonical `SKILL.md`: `.github/plugins/deep-wiki/skills/wiki-architect/SKILL.md`
- Package tree: `124c5bec7008b1e25940cfc67ea09b069af0dbea`
- `SKILL.md` blob: `53bcf7016efbba50e4f634a7a4b4a40cddcb2234`
- Freshness evidence: `67ae723a23ba880e3e5c8a3e5e2320092024476e` last changed this `SKILL.md` at or before the registered pin on 2026-04-02T16:37:09Z
- Behavioral validation: `not-run`

## Package identity and boundary

`wiki-architect` is an independently front-mattered first-class skill in the registered Microsoft Skills pin under the `deep-wiki` plugin. The exact package contains one file, `SKILL.md`; adjacent deep-wiki commands, agents, README material, and sibling skills are outside this package boundary.

## Purpose, triggers, and dependencies

The skill teaches an agent to inspect a repository and produce a hierarchical JSON documentation catalogue with onboarding guides and architecture-oriented sections grounded in real files. It is intended for wiki/documentation creation, repository mapping, high-level architecture understanding, tables of contents, and onboarding plans. It is not a code-modification or deployment procedure.

Operational use assumes read access to the repository tree and README plus Git commands for remote and branch discovery. It requires resolving whether citations should target a source repository URL or local file paths before analysis. No bundled scripts, templates, references, or other package dependencies exist.

## Authority and portability

Authority profile: **read-only**. The procedure inspects repository state and emits JSON. Its Git commands are observational and it does not direct file creation, commits, pushes, deployments, user communications, paid-resource creation, credential changes, or other persistent/external mutation.

Portability: **medium**. The architecture and evidence-grounding method is broadly portable, but the procedure assumes a Git-backed working copy for its canonical remote/branch-resolution path and does not define a complete fallback for hosts without Git command access or for detached/nonstandard branch states.

## Secret and sensitive-data context

The package does not request credentials or instruct external transmission of repository contents. Because it scans repository source and configuration and may emit repository URLs plus file-level citations, a host agent should avoid reproducing secrets, credential-bearing URLs, private operational values, unredacted PII, or other sensitive material encountered during analysis. Publishing the resulting catalogue beyond the user's authorized context would be a separate disclosure action requiring its own authority review.
