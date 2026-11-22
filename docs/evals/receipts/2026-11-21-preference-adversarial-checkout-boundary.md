# Adversarial revisit: private preference root outside the active skill checkout

**Target:** Evidence-Driven Refinement Loop v0.3.3 → v0.3.4 on [PR #826](https://github.com/Knapp-Kevin/skillz/pull/826)  
**Review mode:** Attack the actual optional Python manager's host-path assumption rather than ask the same assistant to grade fictional compliant responses.  
**Scope:** POSIX on-disk manager. **Not** host permission provenance, independent AI evaluation or production user acceptance.

## Frozen negative case

A consuming host supplies an *existing mode-0700 path* outside the skill's own checkout, but **inside another Git repository or linked worktree**. The user's preferences must not be placed in any source repository, irrespective of directory permissions or whether that repository is this skill's repository.

Expected: refuse the location and leave it without `skill-overlays/`. Control: ordinary private configuration roots must continue to support writes, readback, revocation and isolation.

## Observed failure and correction

- The original manager's `reject_checkout_root` only examined `PACKAGE` and its ancestors for a `.git` marker. This could not detect a different repository containing the user-provided storage root.
- Two added tests create temporary unrelated repositories under a separate private temporary directory: one with a conventional `.git/` directory, another with a linked worktree-style `.git` file. The tests call `execute(set...approved=True)` with the nested private directory and demand `PreferenceError` before any child storage is created.
- [Red Actions run 44949812573](https://github.com/Knapp-Kevin/skillz/actions/runs/44949812573) at `54ed4b77` demonstrated **both tests failing on Python 3.9, 3.11 and 3.13**, because neither case raised `PreferenceError`. All other pre-existing manager protections stayed intact.
- The fix checks the actual `root.resolve()` ancestors for a `.git` directory or file, including worktree markers and the root itself being a `.git` directory. It also keeps the original hard prohibition against writing inside the installed skill.
- [Green Actions run 44949878469](https://github.com/Knapp-Kevin/skillz/actions/runs/44949878469) at `3d6da9c7` passed the full suite with the corrected manager, including the added negative cases and real Linux user isolation. The versioned v0.3.4 package is to be separately qualified by exact-head CI.
- v0.3.4 review targets: `SKILL.md` Git blob `85f7e864733a18293a85b1dded50a93c79d75d73`; complete 10-file package tree `463c5c51e3a1c2469420cfa2fde87c39967655a1`; manager blob `9bbce37fedc903ca716094fa9fc4c23dc6010c9a`. All local Markdown links resolved; example version agrees with SKILL.md.

## Adversarial evidence assessment

The earlier **same-assistant consuming-agent emulation** produced expected classifications and formatting decisions against visible acceptance criteria, but it did not independently stress the filesystem policy, authentically distinguish user identities, or establish whether an agent would resist realistic prompt injection in a separate host. It should not be promoted to `independent agent PASS`. The failure above was found by formulating a disconfirming input and exercising a concrete path through the real manager.

This review additionally notes two standing architectural limitations without claiming to repair them:

- **Consent provenance is self-attested by the caller.** The `--approved` flag and `source: explicit-user-confirmation` value are not cryptographic or host-verifiable proof of the user's authorization. Host enforcement is mandatory before writes; arbitrary untrusted documents must not select root paths or carry user-consent authority.
- **Detection is bounded to filesystem evidence.** An external Git environment with no `.git` marker in the work-tree hierarchy, a hostile same-UID process, or a different native storage backend is beyond this test. The claim is refusal of **detected conventional Git checkouts and linked worktrees**, not perfect recognition of every possible repository layout.

**Decision:** Accept the specific source-boundary correction if v0.3.4's final exact-head tests pass. Retain `validation_status: not-run` for independent consumer-host and real user acceptance. Do not merge based solely on the author's same-model conclusions.
