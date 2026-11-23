# MCP Tool Surface Auditor: first-party candidate and differentiation

**Date:** 2026-11-22. **Issue:** #878. **Package:** `skills/authored/mcp-tool-surface-auditor`.
**Release identity:** initial `0.1.0` only because this is a newly authored package,
not a recurring version bump. Authored package is 7 files, MIT.

## Identified gap

Existing first-party Connector Capability Risk Review evaluates whether an
MCP integration has acceptable rights, security/permissions and side effects.
It does not compare a concrete tool name/schema registry across a deployed
server, a complete version-negotiated `tools/list`, and a named agent host's
effective tool list. Generic CI Guard, source debt and repository assessor
do not cover MCP host discovery either.

## Original differentiator

A standalone *read-only* normalized-evidence comparator that finds exactly
which tool-name/schema identities diverge between three stages. It refuses
to make missing-tool assertions if pagination is incomplete, stage captures
differ in revision, principal context or time, or the source is not complete.
A 2026-07-28 capture must include cache hints; earlier revisions are
handled separately. Structural public-cache advisory is not a leak claim.

The fictional 18/18/12 case should report six missing-at-host-boundary
names and zero provider blame. It does **not** report actual observed
MCP transport or host behavior. The optional offline script needs only
Python 3.9 stdlib. No auto refresh, token access, network call or
unprompted feedback issue.

## External prior art (comparison only)

Official MCP specification announcement:
https://blog.modelcontextprotocol.io/posts/2026-07-28/
and official 2026-07-28 SDK caching guidance:
https://py.sdk.modelcontextprotocol.io/client/caching/

MCP connector vetting, dynamic registration and GitHub review agents
already exist externally; no source code or protected agent instruction
text was imported. This skill explicitly avoids promising a proprietary
host refresh API, assigning blame from tool counts or claiming a generic
security assessment is functionally equivalent to tool exposure parity.

## Acceptance and limitations

- 33 synthetic tests planted; hosted exact source QA **PENDING**.
- Package tree `1addc2d5a6ea52e4e14e9bc242161bbe8aef8cdd`; skill blob `61ee3ee491526be54577c3766673261abd6e2960`.
- Independent semantic/host validation **NOT_RUN**; actual user
  integration recovery and social-post ROI **NOT_MEASURED**.
- Published users must not confuse a synthetic comparison with a live
  client test. New behavior must be tested with properly authorized
  version-matched snapshots before any production advice.
