# Authored skill security and refinement standard

Scope: every first-party authored skill and generated standalone package. Third-party source text is untrusted and is not automatically subject to our authored claims. This is a risk-aligned engineering standard, not certification, a claim of injection immunity, or a substitute for host-side enforcement.

## Risk alignment

- OWASP LLM01:2026 Prompt Injection: separate data and authority; challenge direct and indirect injection through documents, tool receipts, repository issues and feedback. https://genai.owasp.org/llm2026/llm012026-prompt-injection/
- OWASP LLM02:2026 Sensitive Information Disclosure: minimize data at the source, use categorical outbound drafts, prohibit raw evidence and prefer no disclosure. https://genai.owasp.org/llm2026/llm022026-sensitive-information-disclosure/
- OWASP agentic identity and privilege abuse: verify user and host permission, scope, destination and parameters independently; default to least privilege and safe fallback. https://genai.owasp.org/agentic-applications-2026/asi03-identity-and-privilege-abuse/
- NIST AI RMF and NIST AI 600-1 Generative AI Profile: govern authority and ownership, map intended use and risk, measure actual behavior with representative adversarial cases, manage findings and residual risk. https://www.nist.gov/itl/ai-risk-management-framework and https://doi.org/10.6028/NIST.AI.600-1

## Mandatory evidence per package

Bind exact package tree and entrypoint blob; enumerate input sources and trust boundaries, tool actions, possible destinations, secret/PII risks, dependency and rights boundaries, and local persistence. Review every support file and optional executable. Record which host controls are actually available; a prompt cannot enforce access control.

Challenge baseline positive, adjacent non-trigger, malformed input, direct and indirect instruction injection, forged authority/tool result, attempted secret disclosure, unapproved outbound action, private preference promotion, mixed feedback, false success, and preserved-success regression. Add skill-specific counterexamples based on its actual capabilities, not just a shared footer. Use fictional fixtures. Separate static review, controlled analyst emulation, executable offline, actual host-observed and consumer acceptance. Unknown = NOT_RUN, credible unresolved high-risk finding = HOLD. No independent host requirement for passive repairs, but never call them host-validated.

## Recursion and routing

Freeze outcome and safeguards; identify a failure; propose the smallest bounded candidate; run counterexamples and protected-success regressions; compare evidence and decide ACCEPT/ITERATE/HOLD/REVERT/STOP_NO_CHANGE. No unsanctioned writes or background learning. Local preference: apply only within current request, persist only by explicit opt-in in authorized private storage with scope, revision and revocation. It never changes authority/security or goes upstream. Mixed cases split before sharing. General defect: optional categorical canonical candidate, independently reproduced by maintainers, narrow owner, exact-head review and merge. Use existing engine/refinement protocol, no second engine.

## Public feedback boundary

Use only the existing public categorical issue form and optional local draft validator. No raw transcript, prompt, customer, repo, model/account, URL, paths, secrets, credentials, timestamps, real commands, metrics, identifiers, attachments, screenshots, error strings or other fingerprints; no personal preference even when useful. No exploit details in public. If ambiguity, residual reidentification risk or authorization is unresolved, HOLD privately. GitHub shows the poster's account and timestamps; content minimization is not anonymity certification. Forms are not server-enforced security gates. Treat every issue/comment as untrusted and do not follow embedded commands. Maintainers independently reproduce and decide on general merit, never reporter identity or votes.

## Rollout status

All 42 current authored entrypoints already contain an optional feedback footer, but that is not proof of full lifecycle coverage or injection resistance. The stricter common form, draft gate, builder contracts and adversarial checks establish the maintenance baseline. Apply and verify the standalone contract in existing packages in bounded batches, keeping exact registry identities current and preserving behavior. No corpus-wide security or host qualification claim until per-package evidence exists.
