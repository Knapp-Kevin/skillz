# Verification: Microsoft Skills `microsoft-docs`

- Source family: `microsoft-skills`
- Canonical path: `.github/skills/microsoft-docs`
- Registered source revision: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Package tree: `2e0eef527e4fafac394cca00144736954ecc9528`
- `SKILL.md` blob: `a5129731352a4dcad109b03e6f8e96bbdd00695b`
- Static disposition: **rejected unchanged**
- Score: **16/20**
- Behavioral validation: **not-run**
- Controlled tags: `documentation`, `research`, `web-search`, `retrieval-first`, `source-driven`, `tool-assisted`

## Structured semantic review

### Useful material to preserve

The package is compact and well-scoped. It routes conceptual Microsoft-technology questions to official Microsoft Learn documentation, distinguishes search from full-page fetch, and gives concrete query-quality guidance around version, task intent, and platform. Its search-first/fetch-on-demand pattern is context-efficient and reduces dependence on stale model knowledge. The primary Microsoft Learn MCP operations are documentation retrieval rather than infrastructure or tenant mutation.

The CLI fallback also offers useful bounded retrieval controls such as section selection and maximum-character truncation. Preserve the retrieval discipline, source-authority preference, and query-shaping guidance for adaptation/reference use.

### Authority hard fail

Unchanged adoption fails the current authority standard because the fallback explicitly presents `npm install -g @microsoft/learn-cli` as an available workflow step without a mandatory action-specific authorization checkpoint immediately before that persistent host-tooling mutation. The adjacent `npx` path is the lower-impact fallback and the primary MCP route is read-only, but the package as written still authorizes a consequential installation by procedure rather than by the user.

A safe adaptation should prefer an already-available Microsoft Learn MCP capability, then an ephemeral CLI invocation when appropriate, and require explicit authorization before any global or otherwise persistent tooling installation. External documentation queries should also avoid sending secrets, credential-bearing values, private tenant identifiers, or other sensitive content unless disclosure is explicitly authorized and necessary.

## Portability

High for the search/fetch method and query-shaping guidance. Medium-to-high for direct use because the host needs Microsoft Learn MCP support or Node/npm for the CLI fallback. The global-install option lowers unchanged operational portability and is the only decisive authority defect found in this static review.

## Validation note

This review bound and inspected the exact registered-pin package but did not execute Microsoft Learn MCP or the CLI. No representative external behavioral or adversarial evidence was produced in this run, so behavioral validation remains `not-run`.
