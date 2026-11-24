# Cross-host authored corpus baseline, 2026-11-24

**Scope:** all 42 first-party authored skill entrypoints on the PR branch
`fix/cross-host-skill-compatibility-20261124`. Source tree:
`1dfe3e004b7481f65b8e784263db41fe18560405`.
Static checks do not qualify actual installation, script permissions or
consumer success in any host.

## Confirmed Microsoft declarative-agent entrypoint size findings

Microsoft declarative-agent skills require `SKILL.md` instructions to
stay **under 20,000 characters**. The following six entrypoint character
counts were confirmed from exact branch file contents, not blob sizes.

| Skill | `SKILL.md` characters | Static disposition |
| --- | ---: | --- |
| ci-guard | 52,526 | HOLD: refactor needed |
| repository-readme-architect | 45,723 | HOLD: refactor needed |
| file-lifecycle-curator | 32,118 | HOLD: refactor needed |
| sandler-conversation-strategist | 23,695 | HOLD: refactor needed |
| meddpicc-opportunity-assurance | 23,356 | HOLD: refactor needed |
| evidence-driven-refinement-loop | 22,910 | HOLD: refactor needed |
| effort-allocation-navigator | **18,378** | Under length limit in this PR; host behavior NOT TESTED |

The remaining 35 authored entrypoints are under the 20,000-character
threshold by source-tree blob size (byte counts are an upper bound on
Unicode character counts for valid UTF-8 text). This alone does **not**
establish their Microsoft package readiness: file types, referenced
support, count/depth, sandbox tools and total package size must also pass.

## Governed remediation sequence

1. **Preserve full authoritative content first.** Extract long sections
   into bundled `references/` files without deleting instructions, safety
   obligations, feedback disclosure or multi-turn continuity. The short
   entrypoint must explicitly direct the host to load normative detail at
   the relevant execution step.
2. **Qualify the complete rewritten package**, not just a reduced
   character count. Check local link closure, package contents, source
   rights, runtime/sandbox assumptions, negative triggers, missing tools,
   authority refusal, and exact prior behavior regressions.
3. **Refresh exact package identities and reviews** in
   `registry/authored-skills-index.json` and both companions, preserve
   historical evidence, and do not inflate SemVer for formatting-only
   corrections.
4. **Keep host observation separate**: Copilot, ChatGPT, Claude, Codex,
   Gemini CLI/Apps, Hermes, Microsoft 365 and other concrete surfaces
   require their own installation/readback and behavioral receipts.
   Unavailable or unsupported targets retain a portable user handoff.

The optional repo maintainer check is now
`python3 engine/builder/host_compat.py --all`. It emits per-target
blockers, not blanket compatible badges; an operator with the full
checkout should run it before claiming any host's `PACKAGE_READY`.
The offline script is not a scanner, installer, host test or publication
system.

**Priority:** correct the six confirmed oversize skills incrementally
by user impact, preserving their current regressions. Do not suppress
known holds to manufacture a 100% compatibility score.
