# Skill Verification and Characterization Records

These files describe **our current quality assessment of an exact skill version**.

They are deliberately separate from [`../skills/`](../skills/) provenance records:

- `registry/skills/` answers **where did this come from, under what license, and when did upstream change it?**
- `registry/verification/` answers **what do we think this exact version is good for, how much do we trust it, and what evidence supports that status?**

Path convention:

```text
registry/verification/<source-id>/<skill-name>.yaml
```

## Fingerprint binding

Every characterized skill record binds to the canonical `SKILL.md` using Git's blob SHA-1:

```yaml
fingerprint_algorithm: git-blob-sha1
content_blob_sha: <40 hex characters>
```

Characterization, tags, verification, and validation apply **only** to that content hash. If the current canonical file produces a different blob SHA, the prior assessment is stale and the skill must be re-reviewed before it is selected as trusted unchanged material.

Run the offline integrity check with:

```bash
node engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

The check performs no network calls. Missing or uninitialized submodules are reported as unavailable, not as false hash mismatches. A real fingerprint mismatch exits non-zero and reports `STALE / REVERIFY REQUIRED`.

## Status meanings

- `unverified`: characterized or discovered, but has not passed the repository's trusted-selection requirements.
- `trusted-baseline`: the exact fingerprint is eligible under an established source-quality policy; integrity and characterization are still required.
- `verified`: passed the structured quality/effectiveness review in [`../../docs/skill-verification.md`](../../docs/skill-verification.md). This is not behavioral validation.
- `validated`: verified and supported by representative behavioral evidence showing improved outcomes.
- `stale`: prior assessment is invalid because the canonical content changed or required evidence no longer matches.
- `rejected`: reviewed and not suitable for normal selection.
- `retired`: previously usable, but intentionally removed from new selection.

## Selection rule

Bootstrap may use `trusted-baseline`, `verified`, or `validated` skills unchanged when the exact fingerprint matches and the characterization fits the user.

`unverified` skills remain valuable design evidence and may be verified on demand, but should not be silently installed as trusted material. `stale`, `rejected`, and `retired` skills are excluded from default direct selection.

Tags come from [`../taxonomy.yaml`](../taxonomy.yaml). Unknown tags should be added to the controlled vocabulary before use.
