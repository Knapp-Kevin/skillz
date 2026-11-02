# Awesome Copilot test-framework and documentation candidate tranche (2026-11-02)

Pinned source: `github/awesome-copilot@f11a4e441c5ff061b4f8ae37952be8c602e4034e`. Root MIT blob `89bc5e962c9944cdb050887062afdaaf89be504a`. **Source-vetting only**, not governed review, admission, security scan or behavioral validation. Individual complete-package fingerprints, rights, 10-dimension scores and rationale: [exact ledger](../../registry/discovery/github-awesome-copilot-test-framework-eight-static-20261102.json).

## Macro map and results

Before **111/432** Awesome Copilot terminal path-matched candidate decisions (94/415 direct; 17/17 other); after **119/432** (102 direct; 17 other), leaving **313** direct paths. Four-source terminal decisions **201/4,813 → 209/4,813**, leaving **4,604 raw paths** without terminal path-matched decisions. Distinct eligible denominator **unknown**; governed review population **1,039 unchanged**. No admission, scan or behavioral test.

| Exact pinned package | Score | Disposition | Decisive limitation |
|---|---:|---|---|
| `csharp-nunit` | 13/20 | REFERENCE-ONLY | NUnit 4 uses Assert.That; legacy Assert.AreEqual and CollectionAssert/StringAssert advice is version-dependent or removed from the modern Assert class |
| `csharp-tunit` | 12/20 | REFERENCE-ONLY | Unpinned TUnit assertions/lifecycle/parallelism claims and all-assertions-async blanket statement are release-sensitive; no installed-version check |
| `csharp-xunit` | 14/20 | REFERENCE-ONLY | Sound general xUnit fixture guidance, but v2/v3 runner and attribute compatibility are not distinguished; generic fluent-assertions dependency unpinned |
| `java-junit` | 14/20 | REFERENCE-ONLY | Claims @BeforeAll/@AfterAll must be static, omitting PER_CLASS lifecycle exception; dependencies and JUnit version are not pinned |
| `javascript-typescript-jest` | 13/20 | REFERENCE-ONLY | Unconditional resetAllMocks can invalidate carefully configured mocks; ESM/TS runner and snapshot approval/secret-scrub guidance missing |
| `dotnet-best-practices` | 10/20 | REJECT | Hardcodes namespace convention, primary constructors, generic CommandHandler, MSTest, Semantic Kernel and localization for every solution; ignores project constraints and compatibility |
| `java-docs` | 14/20 | REFERENCE-ONLY | Useful tags and inheritDoc guidance, but mandatory lowercase/no-period @param, @author and @version suggestions are style-specific and often unnecessary |
| `dotnet-timezone` | 11/20 | REJECT | Pinned reference incorrectly labels Sao Paulo as observing DST (abolished 2019), Cairo as no DST (reintroduced 2023), and code-patterns ToUserTime returns a DateTime converted to DateTimeOffset without reliable zone-offset semantics; static offset tables stale |

## Shared family evidence and differentiated risk

Seven packages are single-file `SKILL.md` trees. `dotnet-timezone` has exactly three files: the skill and `references/code-patterns.md` and `references/timezone-index.md`; the Git tree was reconstructed from exact blobs. All files were read. No source tooling, tests, package installers, network calls from candidate procedures, or scheduling were executed. Source MIT does not relicense NUnit, xUnit, TUnit, JUnit, Jest, NodaTime, TimeZoneConverter, Hangfire or generated materials.

The test guidance shares a useful AAA/isolation structure but mostly lacks project-version checks and approval for package edits or running tests with possible fixture side effects. TUnit is especially version-sensitive; NUnit's classic assertions are not a safe default for NUnit 4. JUnit's `@BeforeAll` static claim omits `@TestInstance(PER_CLASS)`. Jest's blanket mock resets are context-sensitive.

The `.NET Best Practices` procedure attempts to impose unrelated architectural and dependency decisions on arbitrary projects, a clear authority/suitability hard fail. The timezone procedure is more differentiated but has concrete outdated DST data (Brazil, Egypt), location-document privacy ambiguity, and unapproved persistent scheduling examples. Retain patterns for scoped adaptation; do not recommend unchanged use.

## Accounting and next gate

All eight have individual source pin, blob, package tree, file list, terms, dependencies, tags, authority/privacy, ten rubric rationales, disposition and behavioral `not-run`. None matches a governed review by exact leaf name. The four-source raw-path denominator is not a deduplicated eligible-package denominator. Next priority: resolve the two Cloudflare complete-package mirror comparisons and remaining source identity/eligibility gaps before scaling routine batch size.
