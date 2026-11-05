# #483: Repair unsafe Git command wildcard advice (2026-11-05)

**Status:** actual first-party source correction in existing draft [PR #703](https://github.com/Knapp-Kevin/skillz/pull/703), NOT accepted release qualification. Issue #483 and security backfill #402 remain open.

## Defect

The previous Permissions Review 1.0.0 source at Git blob `dcaf7ff96c832c69bb5be1c7cd8f4c3ed418b707` recommended narrowing `Bash(*)` to `Bash(git *)` as an example of safer shell permissions. That still permits arbitrary Git subcommands, command-line `-c` configuration overrides and other helper-triggering operations. In a hostile checkout, even `git status` can execute a configured filesystem-monitor executable. This is a misleading privilege-tightening recommendation in a *security auditing* skill.

## Executed local repro, not agent acceptance

- On local Git **2.47.3**, created a temporary throwaway Git repository and a harmless fsmonitor script that appends to a marker file.
- Ran `git -c core.fsmonitor=<temporary helper path> status --porcelain`. **Observed: helper executed; marker present.**
- Ran `git -c core.fsmonitor=false -c core.hooksPath=<empty path> -c core.pager=cat -c diff.external= -c core.safecrlf=false status --porcelain`. **Observed: marker absent.** This is a limited configuration control, *not* a general proof of safe Git containment.
- Evaluated simple shell-style `git *` matching against four examples: `git status --porcelain`, the helper-configured `git -c ... status`, `git push --force origin main` and `git config --global ...`: **4/4 matched.** This is an illustration of a broad prefix, **not** an assertion about the specific Claude Code permission parser.

## Repair

In `skills/permissions-review/SKILL.md`, version incremented **1.0.0 → 1.0.1**. The source now:
1. Explicitly rejects a broad `Bash(git *)` grant as a tightening example and explains why Git is not a read-only command family.
2. Requires host-verified exact executable, subcommands/arguments, target scope, environment/configuration and helper-execution controls before recommending a shell exception.
3. Prefers scoped host-native repository metadata APIs; if enforcement cannot be verified, recommends denial and `NOT ASSESSED`.
4. Replaces the unsafe example in the human-facing output template.

**Exact source Git blob:** `18f46840032829963715ec23894f7826dbbfcb77` (committed by `8216ab5f17bee27e59cd3599746fd65e0165dfec`). **Exact complete one-file Git package tree:** `e942297c3e343ad5af388b23604987a9bb49322d`, independently read from the Git tree object at branch commit `a139d3c0be29c6383154b597559b99d126d425cd`. Git tree contains only `SKILL.md` with the correct blob. SHA-qualified source, first-party provenance, per-skill verification, 44-skill consolidated verification and both active first-party security ledgers were updated within PR #703.

## Acceptance still missing

- Current complete-tree pinned NVIDIA SkillSpector scan is **NOT RUN**. Do not transfer any historical scan of the old package to this tree.
- Actual independent agent-host adversarial tests must show whether Permissions Review suggests dangerously broad shell or Git permissions under hostile or ambiguous configuration and whether observed tool access remains read-only. Local shell reproduction is not that test.
- Source/provenance/static review changes are proposal-only until #703 completes acceptance and merges.
- The **39 repair-package frontier remains 14 exact-tree historical scanner PASS / 25 NOT RUN**, with **0** independently observed agent-host validations and **0** unchanged-use approvals. This source fix does not close #483 or #402.

**Release decision:** HOLD; do not merge #703 based on this bounded local test alone.
