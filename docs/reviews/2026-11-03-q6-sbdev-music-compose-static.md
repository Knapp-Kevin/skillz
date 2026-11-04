# Q6 independent music-composition review: decision-preserving draft workflow

**Date:** 2026-11-03. **Status:** one source-pinned, individually graded STATIC REFERENCE-ONLY review, NOT a recommendation to install or run unchanged. No scan, package execution, generated audio, or representative host test occurred. This is an independent source family from the eight jtydhr88 reviews now on main at `c4e848674c613a57ddf359250afc4497ea676653`. No overlap credit.

## What is useful

**Music Compose** helps a creator compare different hooks, melodies or arrangements without accidentally replacing choices already approved. The distinct transferable idea is to separate *drafting*, *selection*, *approval* and *locking* for individual musical components. A short hook comparison can be resolved with notation or MIDI before paying for a full audio render. Keep the parent draft of each chosen part, so a final composition assembled from several drafts does not lose its history. This is a useful production decision-management method, not a proven music-quality improvement.

**Canonical source:** [sb-dev/music-production-skills](https://github.com/sb-dev/music-production-skills/tree/aa3933bc87f54a48ec018bb868bf6385b340db22) at exact commit `aa3933bc87f54a48ec018bb868bf6385b340db22`; first-class nested `skills/music-compose/SKILL.md` blob `7cd753c860ffbc12756bd8485884dea2710abb90`. Root MIT LICENSE blob `1efcb2e58067d6b47988fdbdb1555ac9c86844dc`, copyright 2026 Music Production Skills contributors. Root README blob `b4e94d6f6350a522f73f7867b2881620f75f7934`. No per-file license exception was visible in the inspected files; that does not establish rights to external music, reference recordings, generated output, model weights, or optional peer packs. Complete package-tree SHA and alias/mirror crosswalk are **UNKNOWN**, so SKILL.md equality must not be used to infer package equivalence. Exact-tree governed review reuse is **NOT ESTABLISHED**.

## Individually inspected package evidence

| Owned file | Blob SHA | Why read |
| --- | --- | --- |
| `skills/music-compose/SKILL.md` | `7cd753c860ffbc12756bd8485884dea2710abb90` | All triggers, nontriggers, workflow, authority and optional dependencies |
| `references/composition.md` | `e08e25bd545a83d1f2e4f9f3df63a632820eca8c` | Component state and inexpensive composition drafts |
| `references/arrangement.md` | `c7307951c9ed3645fc9b52fec1cb9803d6401d58` | Section energy and handoff boundary |
| `references/drafting-and-selection.md` | `f5a75f563be47bdc10c0e7cf1326febb556164de` | Parent/variant lineage and component-level selection |
| `references/reference-analysis.md` | `93f1bcf9e8b96b945ffee2da32c381a6b38db613` | Transferable characteristics instead of artist imitation |
| `references/midi.md` | `5aca915c978973cd4e760d48ff959f36899dfd92` | Host command and MIDI assumptions |
| `package.json` | `dd6a289e196a7b6d1bf8f1c27d5198978ca506da` | `@tonejs/midi ^2.0.28`, `tonal ^6.4.2`, private package |
| `scripts/inspect-midi.ts` | `eb90d47269abaed36b6b2c55d3f7ca8c6fc4b6ef` | Reads MIDI and prints basic statistics |
| `scripts/transpose-midi.ts` | `2b3fd0093f8969e9edf9f9a3cfb7f5f9a3e889b8` | Reads input and writes arbitrary user-provided output path |
| `scripts/validate-composition.ts` | `986ac4bb2a05d922c1270e85b31e6ece43f10157` | Parses **JSON**, validates a few required fields |
| `assets/selection.example.yaml` | `31e18fff8f0d8a6c455d1336749753906488a647` | YAML selection example; not accepted by JSON-only validator |

All five references named by the entrypoint, three named helper scripts, package.json and one linked example were inspected. A full Git tree listing and other unlinked bundled files were **not** independently enumerated. A `package-lock.json` fetch returned 404 at the pinned commit; absence of a fetched lockfile does not prove the whole repository lacks a lockfile elsewhere. This is **not** full-package verified.

## Ten-axis grade: 15/20

| Axis | Score | Individual reason |
| --- | ---: | --- |
| Trigger precision | 2 | Explicitly handles composition, arrangement, alternatives and MIDI; excludes mastering, provider infrastructure and final audio production |
| Procedural clarity | 2 | Concrete small-draft → compare → select → approve/lock → refine → handoff sequence |
| Authority and privacy | 1 | Preserves approval concepts, but optional external model/token flow and local writes need action-specific permission; no private reference audio egress authorized |
| Failure handling | 1 | Validation and refinement checks exist, but output collision/overwrite and YAML/JSON mismatch are not addressed |
| Evidence discipline | 2 | Lineage, parent variants and selected component provenance are explicit, although outcomes are not empirically tested |
| Dependency coherence | 2 | Named peer model skills and local helpers are optional and distinguished from core text workflow |
| Portability honesty | 1 | Core method is host-agnostic; Node 22+, caret npm dependencies and peer provider APIs are version-sensitive |
| Distinct usefulness | 2 | Locking per-component musical decisions across drafts is not the same method as the jtydhr88 harmonic/notation/arrangement craft skills |
| Adversarial resilience | 1 | Source reference analysis avoids direct artist imitation, but untrusted references and injected instructions are not explicitly bounded |
| Effectiveness design | 1 | Cheap comparison and lineage can be inspected, but no real composing session, blind comparison or downstream preservation test was observed |

**Static disposition: REFERENCE-ONLY (15/20).** Useful method, not unchanged-package approval. **Behavioral validation: NOT RUN. Security scan: NOT RUN. Installation: NOT AUTHORIZED.** No public positive shelf promotion is proposed until exact package identity, alias crosswalk, rights and safety gates are reconciled. No change to the 19 current Valuable References on main.

## Material static defects and hard authority boundary

1. **Documentation/validator mismatch:** `references/midi.md` instructs `validate-composition.ts composition.yaml` and the sample artifact is YAML. The actual validator uses `JSON.parse(await readFile(...))` and its usage string requires `composition.json`. The example command fails for ordinary YAML; do not call this validator tested or claim the sample is accepted.
2. **Arbitrary overwrite:** `transpose-midi.ts` calls `writeFile(output, ...)` without a no-clobber check, output-root confinement or a same-input guard. It can replace an existing file at a host-selected output path. The script has a useful MIDI range check but **no action-specific authorization or overwrite safety**. Never run it as part of passive review.
3. **Unpinned dependencies:** npm ranges `^2.0.28` and `^6.4.2` are not exact dependency locks. `npm install` and any package execution require host-controlled trust review and explicit authorization; there is no repository-owned install action.
4. **External audio model escalation:** Replicate `find-models`, `compare-models`, `run-models` and token use are described as optional. Tool availability or having a token is not permission to send prompts, audio, lyrics, private references or spend money. Require action-specific approval and rights review before any call.
5. **Source/derivative rights:** Root MIT covers authored material under that license, not reference songs, samples, model terms, peer packs or third-party audio. A music reference may be analyzed as high-level properties; do not copy protected passages, lyrics or melodies into catalog content.

**Source-family accounting:** One independently inspected nested skill package in one source family, eleven named owned file blobs observed, **zero** newly verified complete package trees, **zero** unchanged-use approvals, **zero** behavioral/security passes. Distinct eligible global denominator UNKNOWN. This review is a separate draft-stage artifact and must not be added to governed Q1–Q5 counts or the consumer-positive 19 without a qualified integration.

**Next qualification gate:** Enumerate and hash the exact package tree and mirrors, reconcile the identity crosswalk, check the scripts' write behavior with a disposable host-only test if authorized, fix/verify the YAML/JSON contract upstream or document it as a hard caveat, and then decide whether the method merits a source-neutral Valuable Reference promotion. Preserve all existing published evidence.
