# Offline historical source reference audit

Run from an authorized Skillz checkout at the exact candidate PR revision:

```sh
node scripts/qa/audit-legacy-source-references.mjs --self-test
node scripts/qa/audit-legacy-source-references.mjs --legacy todo-harvester
node scripts/qa/check-authored-capability-links.mjs
node scripts/build-current-routing-graphic.mjs --check
```

The script uses only Node built-ins and `git ls-files`. It **does not**
install packages, invoke third-party skill content, call networks, mutate
the repo, browse private home directories, or enable scheduling.
Its only output is a sanitized file/line summary of references and
unknown coverage. Any source file that is unreadable, oversize or a
symlink blocks full-text coverage rather than being silently ignored.

History records and immutable Git commit URLs are allowed as
**historical citations**, not selectable current methods. The script
checks active name, capability, local-verification and category indexes
for lingering historical IDs. Unknown or active references return
nonzero and hold retirement.

The script was authored and statically inspected in this session.
**Native execution and real repository-wide results NOT RUN** in this
environment because there is no reachable GitHub checkout. Self-test
cases document intended behavior, not an observed PASS. The source
retirement pilot remains a draft until this check and relevant QA
actually pass.
