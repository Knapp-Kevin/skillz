# PR #416: Three pulse portability corrections (2026-10-28)

## Scope and exact identity

This bounded follow-up resolves three independently identified stale host/runtime assumptions in the draft PR #416. All three complete SKILL.md files were read at PR head `777e92c9adf71cddec2fb54cf2919faa025fcb55`; only the quoted assumptions and optional scheduling wording changed. The corrected manifest blobs were committed at `17edbdf0559c74eb1fd03013578258a96c96c3ea` and each corresponding first-party provenance, individual semantic verification, and consolidated local-verification entry was reconciled to those exact blobs.

| Skill | Corrected Git blob SHA | Static score / disposition | Authority | Dependencies |
|---|---|---|---|---|
| `mcp-pulse` | `d1a2d62b9f4ffa90a1c13480ca00034ddffd52ee` | 17/20 VERIFIED semantic | read-only retrieval; optional scheduling requires separate explicit approval | Bundled `sources.json`; authorized host browsing/search; no MCP runtime required |
| `gemini-pulse` | `1b6a1d2d4bca784a6bcaf75bd056b189c65f2ced` | 16/20 VERIFIED semantic | read-only retrieval; optional scheduling requires separate explicit approval | Bundled `sources.json`; authorized host browsing/search; no Qor distribution required |
| `perplexity-pulse` | `f831906d8de3835e92eabae208566bb55dcc22be` | 16/20 VERIFIED semantic | read-only retrieval; optional scheduling requires separate explicit approval | Bundled `sources.json`; authorized host browsing/search; no Sonar backend required |

## Individual findings and dispositions

- **MCP Pulse:** Removed the false claim that the passive repository's own contract depends on MCP. MCP is an optional interoperability surface of external hosts. Replaced the host-specific `/schedule` instruction with explicit user-approved optional scheduling. Preserve spec/security-first research and UTC query-window handling. **VERIFIED semantic only**, 17/20; no package-security or behavioral pass.
- **Gemini Pulse:** Replaced the assumed Qor-logic `.gemini/commands/` distribution with conditional relevance to the user's actual Gemini CLI/ADK integration. Preserve official-source priority and missing-evidence disclosure. **VERIFIED semantic only**, 16/20; no package-security or behavioral pass.
- **Perplexity Pulse:** Removed the implied repository-owned research backend. Sonar is only a possible external host option subject to user fit, access, terms and data-handling authorization. Preserve product/API distinction. **VERIFIED semantic only**, 16/20; no package-security or behavioral pass.

## Macro and gate findings

All three defects were host-portability assumptions, not a justification to introduce adapters, repository-owned runtime, scripts, schedulers, tests or scanners. No new first-party skill, source, dependency, denominator or taxonomy tag was introduced. First-party inventory remains 44. This is a focused **static exact-version semantic re-review** of three modified packages; it is not an executed adversarial test, an independent acceptance decision, or a SkillSpector result. Security and behavioral states remain **not-run**. Existing historical scanner evidence does not transfer to these changed fingerprints. PR #416 remains DRAFT / HOLD pending complete exact-final package-security reports for all 21 modified skills and independent acceptance.
