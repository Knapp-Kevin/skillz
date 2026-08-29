# Skill Verification and Characterization Records

These files describe the repository's current quality assessment of an **exact skill version**.

They are deliberately separate from provenance:

- `registry/skills/` answers **where did this come from, under what license, what does it depend on, and what exact source was inspected?**
- `registry/verification/` answers **what quality state applies to this exact canonical skill content, what is it for, and what evidence supports that state?**

Path convention:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

## Fingerprint binding

Every characterized skill record binds to canonical `SKILL.md` content with Git's blob SHA-1:

```yaml
fingerprint_algorithm: git-blob-sha1
content_blob_sha: <40 hex characters>
```

Characterization, tags, verification, and validation apply only to that fingerprint. If canonical content changes, prior evidence cannot be silently inherited.

The offline integrity checker is:

```bash
node engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

Missing/uninitialized vendored material is reported as unavailable rather than falsely labeled drift. A real hash mismatch reports `STALE / REVERIFY REQUIRED`.

## Status meanings

- `verified`: the exact fingerprint passed the current structured quality/effectiveness review in [`../../docs/skill-verification.md`](../../docs/skill-verification.md). This is not behavioral validation.
- `validated`: `verified` plus representative behavioral evidence.
- `unverified`: discovered/characterized but not eligible for trusted unchanged selection.
- `trusted-baseline`: legacy schema compatibility only. It is no longer a current unchanged-selection state.
- `stale`: prior assessment cannot support current unchanged reuse because content/evidence changed.
- `rejected`: reviewed and unsuitable for unchanged use.
- `retired`: intentionally removed from new selection.

## Selection rule

Only `verified` and `validated` exact-version records are eligible for unchanged third-party consideration, and only when:

- the fingerprint matches when the host can establish it;
- provenance and license obligations are acceptable;
- required dependencies are intact;
- authority/side effects fit the current task;
- portability assumptions fit the current host;
- the skill actually matches the user's capability requirement.

`unverified` and legacy `trusted-baseline` material may inform design but must not be silently installed unchanged. `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection.

A rejected or stale skill can still contain a useful mechanism. Reusing a mechanism does **not** erase the reason the original skill was excluded. The adapting agent must account for that reason and must separately check license/provenance, dependencies, authority, and environment assumptions before carrying material forward.

## Behavioral validation

`validation_status` is separate from `verification_status` by design.

`validation_status: not-run` means exactly that. Upstream tests, strong static design, source reputation, and a high structured score do not become local behavioral proof by linguistic enthusiasm.

## Controlled metadata

Tags come from [`../taxonomy.yaml`](../taxonomy.yaml) and characterize:

- use case;
- lifecycle;
- workflow characteristics;
- authority;
- portability.

Unknown tags should be added to the controlled vocabulary before use.

## Share-ready closure

The share-ready corpus check treats unresolved current states such as `unverified` or legacy `trusted-baseline` as blockers on the governed selection surface. Broad vendored/reference material without an individual companion remains reference/discovery material and does not receive trusted eligibility merely by being physically present in the repository.