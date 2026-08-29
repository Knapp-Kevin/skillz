# Skill Verification and Characterization Records

These files describe the repository's current quality assessment of an **exact skill version**.

They are separate from provenance:

- `registry/skills/` answers **where did this come from, under what license, what does it depend on, and what exact source was inspected?**
- `registry/verification/` answers **what semantic quality state applies to this exact canonical skill content, what is it for, and what evidence supports that judgment?**

Path convention:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

## Fingerprint binding

Every characterized record binds to canonical `SKILL.md` content with Git's blob SHA-1:

```yaml
fingerprint_algorithm: git-blob-sha1
content_blob_sha: <40 hex characters>
```

Characterization, tags, verification, and validation apply only to that fingerprint. If canonical content changes materially, the prior judgment should not be silently inherited.

Fingerprinting is bookkeeping for exact-version identity. It is not an executable quality gate.

## Status meanings

- `verified`: the exact fingerprint passed the current structured semantic review in [`../../docs/skill-verification.md`](../../docs/skill-verification.md).
- `validated`: `verified` plus representative scenario/adversarial semantic review.
- `unverified`: discovered/characterized but not eligible for trusted unchanged selection.
- `trusted-baseline`: legacy schema compatibility only. It is no longer a current unchanged-selection state.
- `stale`: prior assessment cannot support current unchanged reuse because content or material evidence changed.
- `rejected`: reviewed and unsuitable for unchanged use.
- `retired`: intentionally removed from new selection.

## Selection rule

Only `verified` and `validated` exact-version records are eligible for unchanged third-party consideration, and only when:

- the exact version/fingerprint is established when the host can establish it;
- provenance and license obligations are acceptable;
- required dependencies are intact;
- authority/side effects fit the current task;
- portability assumptions fit the current host;
- the skill actually matches the user's capability requirement.

`unverified` and legacy `trusted-baseline` material may inform design but must not be silently installed unchanged. `stale`, `rejected`, and `retired` material is excluded from normal unchanged selection.

A rejected or stale skill can still contain a useful mechanism. Reusing a mechanism does **not** erase the reason the original skill was excluded. The adapting agent must account for that reason and separately check license/provenance, dependencies, authority, and environment assumptions before carrying material forward.

## Semantic validation

`validation_status` is separate from `verification_status` so stronger scenario/adversarial review can be recorded without pretending it is deterministic runtime proof.

`validation_status: not-run` means no separate scenario-level semantic validation was recorded beyond the structured review. It does **not** mean a CI job or application test failed, because this repository has no runtime correctness surface of that kind.

See [`../../docs/skill-verification.md`](../../docs/skill-verification.md) for the semantic validation model.

## Controlled metadata

Tags come from [`../taxonomy.yaml`](../taxonomy.yaml) and characterize:

- use case;
- lifecycle;
- workflow characteristics;
- authority;
- portability.

Unknown tags should be added to the controlled vocabulary before use.

## Governed corpus boundary

Broad vendored or tracked source material without an individual companion remains reference/discovery material. It does not receive trusted unchanged-selection eligibility merely by being present, popular, official, or adjacent to another reviewed skill.

Repository completion is assessed through coherent metadata plus semantic/adversarial review of the instructions. CI, executable preflights, and test harnesses are not part of this repository's completion model.