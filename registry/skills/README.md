# Third-Party Skill Provenance Records

Each YAML file below this directory answers where an individually characterized third-party skill came from, which upstream revision/path was inspected, what license applies, when the skill itself last changed, whether its dependencies are intact, where it is available, and why it is useful enough to characterize.

Path convention:

```text
registry/skills/<source-id>/<skill-name>.yaml
```

These records are intentionally separate from upstream `SKILL.md` files. Vendored repositories are not modified merely to attach our local metadata.

Provenance is **not** a quality certificate. Quality state, controlled tags, and hash-bound characterization live separately under [`../verification/`](../verification/).

Volatile source-level reputation/adoption context such as repository stars, forks, activity dates, and archive state lives once in [`../source-signals.yaml`](../source-signals.yaml), not duplicated across every skill companion. Those signals are context only and never substitute for individual exact-version verification.

When directly establishable, a provenance companion may also record `upstream_first_seen_at`, skill-specific `usage_evidence`, or skill-specific `reception_evidence`. Do not infer those facts from repository age or popularity.

For the complete field contract and the order in which agents should weigh this metadata, see [`../../docs/companion-metadata.md`](../../docs/companion-metadata.md).

See also [`../../docs/curation-policy.md`](../../docs/curation-policy.md), [`../../docs/skill-verification.md`](../../docs/skill-verification.md), and [`../taxonomy.yaml`](../taxonomy.yaml).
