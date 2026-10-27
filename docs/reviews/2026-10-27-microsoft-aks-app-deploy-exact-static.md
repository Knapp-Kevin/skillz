# Microsoft AKS app deployment: full exact-version static rejection

**Date:** 2026-10-27. **Candidate:** `61fe0305ea70389ed8705eec6026a786f57865cf`. **Registered July pin:** `32cad4ee689c95c309e61aeefcbc6af356f1e6a7` (unchanged). **Scope:** `.github/plugins/azure-skills/skills/azure-kubernetes/azure-kubernetes-app-deploy/` at Git tree `580e5d0cffde99b0b4e571721570f282d5930d9a`, manifest blob `e3e148299871832471b4b056093e386a132e8d4a`. **Evidence:** all 42 bundled blobs (134,906 upstream Git-tree bytes) and the separately shared AKS Automatic constraint reference blob `59f6c6b930628e93627291e585bf1c43b2212e2a` were read statically. No commands, scans or behavioral trials were executed.

## Recomputed four-package frontier

The previous seven-package map closed three distinct packages (53 bundled blobs). The remaining **four** were `azure-app-onboard` (68 blobs), `azure-kubernetes-app-deploy` (42 blobs), `foundry-iq` (85 blobs), and `slack-to-teams` (one local manifest plus 100+ parent shared references). None is an exact-tree alias of another. This tranche deep-reviewed the coherent 42-blob AKS deployment package and its external shared policy dependency. Large onboarding/Foundry packages and cross-platform messaging remain disjoint and unqualified.

## Exact decision

**REJECT unchanged, 13/20 static rubric.** The manifest is a first-class frontmattered skill (MIT, Microsoft, version 1.0.0) with clear use/non-use boundaries: deployment of an existing web/API to an already-running AKS cluster, not cluster creation or unrelated Azure services. Its 42 source-owned files include nine framework packs, 12 Dockerfile/ignore assets, Kubernetes manifests, GitHub Actions deployment template, and quick-deploy/rollback references. Individual provenance and verification companions carry the exact 42-path inventory, tree/blob fingerprints, ten-axis rubric, tags, dependencies, privacy/authority findings, and explicit security/behavioral `not-run`.

**Hard-fail authority:** `phases/quick-deploy.md` Section 4 executes `az aks get-credentials --overwrite-existing`, `az acr build`, namespace creation and `kubectl apply`, and can install Gateway API CRDs from a moving `latest` URL. No separate cluster-owner, environment, traffic, cost, local kubeconfig, or remote-code authorization is established. A narrow confirmation before ACR attachment does not authorize the remaining actions.

**Continuous-deployment boundary:** `templates/github-actions/deploy.yml` deploys on pushes to `main`, uses OIDC `id-token: write`, and has no protected-environment/manual deployment authorization. The workflow is **upstream template evidence**, not a workflow owned by `skillz`. Its rollback condition requires `steps.deploy.outputs.deployed == 'true'`, but that output is written only after `kubectl rollout status` succeeds. A failed apply or rollout therefore does not trigger the advertised rollback. This is a static control-flow defect, not a reproduced runtime failure.

**Privacy/traffic:** default ingress omits a hostname and routes to an external IP; TLS is optional. Cloud resource metadata, identity federation, workload secrets and cluster diagnostics need scoped handling. No literal live credential was observed.

**Policy coherence:** `references/safeguards.md` advertises 13 DS checks, while its linked sibling `azure-kubernetes-automatic-readiness/references/constraint-spec-v1.yaml` describes 21 workload safeguards (with caveats). They are different scopes, not proof of a live policy violation; do not claim comprehensive AKS Automatic enforcement from the 13-item local checklist.

## Preserve useful mechanisms

Retain framework detection, deterministic manifest templates, non-root and read-only filesystem patterns, image tagging by commit SHA, workload identity instead of embedded secrets, explicit ACR-attachment confirmation, evidence-first readiness checks and bounded rollback concepts. Adapt by adding explicit action-specific target, traffic, identity, cost, CI deployment and destructive-recovery gates; bind remote manifests to approved versions; separate generate-only from deploy; correct rollback conditions and reconcile policy scope.

## Accounting and lifecycle

Registered Microsoft July remains **186/186**, candidate structural denominator **208 = 106 carry-forwards + 76 changed + 26 new/ungoverned**. New candidate complete reviews move **22/26 → 23/26** (4 semantic VERIFIED only / 19 REJECT unchanged). The full current-version review frontier moves **80 → 79** (3 new + 76 changed). Four removed-path successor/retirement decisions remain unresolved. Persisted third-party exact-version verification companions move **746 → 747**, pending independent Git-tree readback. No source pin, admission, scanner result or behavioral state changes. Issue #400 remains open; #402 and #415 and draft PRs #412/#413/#416 remain blocked on existing independent security/admission gates. No discovery source admitted.
