# MCP Tool Surface Auditor

**Where did the tools disappear?** Compare three separately
claimed inventories: backend registration, complete MCP `tools/list`,
and one host's visible tools. Investigate differences without
claiming the host or server caused them.

This **standalone seven-file** first-party MIT skill includes an
optional Python 3.9+ read-only offline script, 33 planted
positive/negative tests and a completely fictional **18 upstream
tools / 12 host-visible tools** case.

```sh
python3 scripts/audit.py --input examples/synthetic-18-versus-12.json
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The example reports six visibility differences specifically at
the MCP-to-host boundary, but **no real host or endpoint was
observed**. The demo is not a credentialed integration test.
Read [SKILL.md](SKILL.md) and
[the adversarial acceptance cases](examples/acceptance.md).
