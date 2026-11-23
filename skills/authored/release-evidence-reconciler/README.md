# Release Evidence Reconciler

**"CI passed. But did we ship the thing we tested?"**

This standalone, original first-party MIT skill separates
source/tag identity, exact-head CI, build artifact, distribution,
actual downloaded bytes, provenance validation and real installation
acceptance. It never treats a build badge as product delivery.

The optional, offline Python 3.9+ standard-library script **hashes real
local bytes**. Its synthetic fixture is a 29-byte text payload, not an
installer. It has no network, cloud, credentials, third-party library,
other Skillz dependency, filesystem write or executable side effect.

```sh
python3 scripts/reconcile.py \
  --manifest examples/synthetic-release.json \
  --artifact-root examples/artifacts \
  --require-local-match

python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The strongest report is `LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS`,
**not verified/secure/functional release**. Authenticated origin,
cryptographic attestation verification, actual installation and
user acceptance require separate authorized host evidence.

Read [SKILL.md](SKILL.md) and [synthetic cases](examples/acceptance.md).
