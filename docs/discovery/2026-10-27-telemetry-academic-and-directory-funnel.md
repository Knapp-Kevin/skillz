# Discovery funnel: directory freshness, academic-review candidate and overlap (2026-10-27)

**Scope:** external-host public discovery and bounded source vetting only. No repository crawler, monitor, installer, runtime, CI, scheduled scan, source admission or package execution. This record is separate from the eight-package admitted-source Microsoft freshness assessment in the same PR.

## Three public discovery surfaces actually checked

1. **TrustedSkills**: https://trustedskills.dev/ (public website, reported last sync **2026-10-26**). At inspection it claimed **41,155 indexed skills**, 6,499 publishers and 27,966 entries with a `Checked` badge. These are **provider claims and index entries**, not independently deduplicated first-class packages or human-reviewed security/quality evidence. The site explicitly says that no human has reviewed the code behind the listings, that its static checks do not establish behavioral correctness, and that many installations resolve live mutable upstream versions. **New discovery surface lead**, no source admission. Its checked/official badges must never become `skillz` verification or installation authority.
2. **GitHub curated directory**: https://github.com/alfarius42/awesome-agent-skills at observed revision `8d1cdcddf14462f5d4127047f54c9f4f7c4f2404`; root README Git blob `d2916e16e21ba9083162452106dd3777f7623111`. The README's banner and update badge point to VoltAgent's collection and its `549+` label; this appears to be an alternate/forked exposure of the VoltAgent directory, **not a separate independent 549-skill source**. It lists official and community sources, including already registered Anthropic, Vercel and Cloudflare material. **Directory / REFERENCE ONLY**, deduplicate upstream repo/path/revision before any candidate intake.
3. **Hugging Face official agent-skills documentation**: https://huggingface.co/docs/hub/agents-skills (public documentation checked this run). It lists first-class `hf-cli`, datasets, training, evaluation, Trackio, paper publishing, tool builder, Gradio and Transformers JS workflows. This is a **known discovery ecosystem**, not automatically a new source identity; the documentation is not an exact package revision and cannot establish current eligible denominator. **Reference / known-surface check**, no new admission.

A follow-up targeted lookup from the public directory uncovered one concrete original-source package candidate below. The website's per-skill listing was independently checked against GitHub rather than treated as provenance.

## Canonical candidate: academic-paper-reviewer

- **Original repository:** https://github.com/Imbad0202/academic-research-skills (GitHub is case-insensitive for owner resolution). **Observed upstream HEAD:** `b34c63f828b3535f403079a4f42bc7955da2f64b`.
- **Exact manifest:** `academic-paper-reviewer/SKILL.md`, Git blob `e18873a80a3015f3f915dd9c3e13e6dc826320e6`. Metadata declares version `1.11.1`, `last_updated: 2026-08-15`, `data_access_level: raw`, and related skills `academic-paper` / `academic-pipeline`. The upstream repository being recently updated **does not prove this skill itself changed in the last 24 hours**.
- **README:** blob `32759cb15f12a75002be6d816c335bd44c4ef15b`. It advertises a larger research-to-publication suite with a multi-step plugin/agent installation model; the complete eligible denominator, alias paths, dependency references and full package tree have **not** been enumerated.
- **License:** root `LICENSE` blob `dedfb8b7880e51fe623fa5ea7e27c118eed4e2b9` is **CC BY-NC 4.0**. This is not equivalent to MIT or unrestricted commercial reuse. **No copying, vendoring, unchanged admission or adaptation into a commercially distributed skill corpus without an appropriate rights decision.** Reference and evaluation notes remain possible.
- **Differentiated method:** five-seat role-separated peer-review panel (journal fit, three reviewer perspectives, devil's advocate), editorial synthesis, re-review, calibration and Socratic modes. The manifest explicitly acknowledges that role separation does **not** establish independent error processes. This is more substantive than a one-line review prompt, but its effectiveness is not behaviorally tested here.
- **Authority/privacy risks:** full unpublished manuscripts and raw research materials may include confidential, proprietary or regulated content; role-dispatch and external tool access must not infer consent to transmit, publish, upload or disclose. The long routing contract and related skills create a nontrivial dependency/host compatibility boundary.
- **Terminal discovery disposition:** **REFERENCE-ONLY** for the present commercial/general-purpose passive corpus because of the noncommercial license and unresolved dependencies/authority. This is **not** a quality rejection, a security scan, or an assertion that every package in the upstream family has the same fitness. No candidate admission issue opened because no admission is proposed.

## Funnel and omissions

| This run | Observed |
|---|---:|
| Distinct public discovery surfaces actually inspected | 3 |
| Newly recorded canonical discovery leads (2 directories, 1 original source) | 3 |
| Concrete first-class skill manifests independently inspected | 1 |
| New unchanged admissions / registered source identities | 0 / 0 |
| Full source denominators newly established | 0 |
| Exact-version package-security scans / behavioral validations | 0 / 0 |
| Repo-owned execution machinery added | 0 |

**Omission risk:** A directory's `Checked` label, popularity, and listing freshness are not comparable to `skillz`'s exact-version semantic/authority gate. A directory mirror is not a second original source. The academic source is a useful negative example of **high methodological value combined with noncommercial terms and confidential-data risks**. Continue discovery using source identity, exact manifest path, content revision and explicit license gates, rather than counting listings or stars.

**Next discovery action:** choose a differentiated original-source candidate with commercially compatible terms and a tractable complete package denominator; use issue-first intake only when there is a real admission decision to resolve. Keep Track A's Microsoft source freshness work moving in parallel.
