// Behavioral contract tests for Issue #7 bootstrap/onboarding.
// These tests guard the promises the beginner entry point makes to users and
// the source/provenance facts the orchestration skill depends on.

import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(ROOT, path), "utf8");

test("bootstrap beginner path does not require prior skill knowledge", () => {
  const doc = read("BOOTSTRAP.md");
  assert.match(doc, /You do not need to know how skills work\./);
  assert.match(doc, /Read `BOOTSTRAP\.md` and help me figure out which skills would make you better at helping me\./);
  assert.match(doc, /Do not guess about information you cannot see\./);
  assert.match(doc, /smallest set of skills that actually makes your AI better for you/i);
});

test("bootstrap beginner path includes installation instead of abandoning the user with files", () => {
  const doc = read("BOOTSTRAP.md");
  assert.match(doc, /either install them for me if you can do that safely, or give me simple step-by-step instructions/i);
  assert.match(doc, /How do I install the skills when they are ready\?/);
  assert.match(doc, /You should not have to figure that out by yourself\./);
  assert.match(doc, /An installation result/);
  assert.match(doc, /what you need to do next/);
  assert.match(doc, /how you know the skill is working/);
});

test("bootstrap skill degrades honestly when history or tools are unavailable", () => {
  const skill = read("skills/skill-bootstrap/SKILL.md");
  assert.match(skill, /Unavailable sources are recorded as unavailable/);
  assert.match(skill, /Never claim inaccessible or out-of-scope sources were reviewed/);
  assert.match(skill, /Missing evidence is a finding/);
  assert.match(skill, /DO NOT CREATE/);
});

test("bootstrap minimizes connected private-source access", () => {
  const skill = read("skills/skill-bootstrap/SKILL.md");
  assert.match(skill, /Use the minimum evidence needed/);
  assert.match(skill, /Do \*\*not\*\* sweep unrelated connected private accounts/);
  assert.match(skill, /Access to a connector is capability, not consent to mine it for a profile/);
  assert.match(skill, /Available but out of scope \/ not inspected/);
});

test("bootstrap compares before creating and preserves process authority", () => {
  const skill = read("skills/skill-bootstrap/SKILL.md");
  for (const disposition of ["ADOPT", "ADAPT", "SUPPLEMENT", "COMPOSE", "CREATE"]) {
    assert.match(skill, new RegExp(`\\*\\*${disposition}\\*\\*`), `missing ${disposition} decision path`);
  }
  assert.match(skill, /Preserve user experience by default/);
  assert.match(skill, /Prefer reuse over creation/);
  assert.match(skill, /proposal as authorization/i);
});

test("bootstrap installation classifies execution paths and completion states", () => {
  const skill = read("skills/skill-bootstrap/SKILL.md");
  const handoff = read("docs/installation-handoff.md");

  for (const mode of ["DIRECT-WRITE", "API-INSTALL", "UI-UPLOAD", "PORTABLE-HANDOFF"]) {
    assert.match(skill, new RegExp(mode), `bootstrap missing installation mode ${mode}`);
    assert.match(handoff, new RegExp(mode), `handoff missing installation mode ${mode}`);
  }

  for (const state of [
    "INSTALLED + VERIFIED",
    "INSTALLED, VERIFICATION PENDING",
    "READY TO UPLOAD",
    "USER ACTION REQUIRED",
    "BLOCKED: HOST DOES NOT SUPPORT SKILLS",
    "BLOCKED: INSTALLATION METHOD NOT ESTABLISHED",
  ]) {
    const pattern = new RegExp(state.replace(/[+]/g, "\\+"));
    assert.match(skill, pattern, `bootstrap missing completion state ${state}`);
    assert.match(handoff, pattern, `handoff missing completion state ${state}`);
  }
});

test("ui upload cannot be reported as installed before the human action occurs", () => {
  const skill = read("skills/skill-bootstrap/SKILL.md");
  const handoff = read("docs/installation-handoff.md");
  assert.match(skill, /Do not end with a vague "install these skills" instruction\./);
  assert.match(skill, /Never report a UI-required upload as completed unless the host actually confirms it/);
  assert.match(handoff, /The user should never be left with a folder of files and the unexplained instruction "install this\."/);
  assert.match(handoff, /one action per numbered step/);
  assert.match(handoff, /end with one test prompt/);
});

test("portable profile records installation separately per host", () => {
  const profile = read("docs/portable-skill-profile.md");
  assert.match(profile, /installation_targets:/);
  assert.match(profile, /mode: direct-write\|api-install\|ui-upload\|portable-handoff/);
  assert.match(profile, /status: installed-verified\|installed-verification-pending\|ready-to-upload\|user-action-required\|blocked-host-unsupported\|blocked-method-unknown/);
  assert.match(profile, /Installation is \*\*per host and per surface\*\*/);
  assert.match(profile, /Are those skills actually installed and working here\?/);
});

test("community reference source preserves Matt Pocock provenance", () => {
  const sources = read("registry/sources.yaml");
  const modules = read(".gitmodules");
  const provenance = read("docs/third-party-provenance.md");
  const upstreamLicense = read("vendor/mattpocock-skills/LICENSE");

  assert.match(sources, /id: mattpocock-skills/);
  assert.match(sources, /class: community-vetted/);
  assert.match(sources, /license: MIT/);
  assert.match(sources, /index_exclude_dirs: deprecated,in-progress/);
  assert.match(modules, /https:\/\/github\.com\/mattpocock\/skills\.git/);
  assert.match(provenance, /Copyright \(c\) 2026 Matt Pocock/);
  assert.match(upstreamLicense, /MIT License/);
  assert.match(upstreamLicense, /Copyright \(c\) 2026 Matt Pocock/);

  const recorded = sources.match(/pinned_revision:\s*([0-9a-f]{40})/)?.[1];
  assert.ok(recorded, "source registry must record a full pinned_revision");

  const gitlink = spawnSync("git", ["rev-parse", "HEAD:vendor/mattpocock-skills"], {
    cwd: ROOT,
    encoding: "utf8",
  });
  assert.equal(gitlink.status, 0, `must resolve vendored gitlink: ${gitlink.stderr}`);
  assert.equal(recorded, gitlink.stdout.trim(), "recorded provenance revision must match the actual vendored submodule pin");
});

test("index generator reads source trust and exclusions from the source registry", () => {
  const script = read("scripts/build-index.ts");
  assert.match(script, /function parseSourceRegistry/);
  assert.match(script, /const sourceRecords = parseSourceRegistry\(\)/);
  assert.match(script, /index_exclude_dirs/);
  assert.match(script, /sourceClass: s\.class/);
  assert.match(script, /sourceRegistry: "registry\/sources\.yaml"/);
  assert.match(script, /bootstrap: "BOOTSTRAP\.md"/);
  assert.doesNotMatch(script, /sourceClass:\s*"community-vetted"/, "community trust class must come from registry/sources.yaml, not a second hard-coded truth");
});

test("portable profile separates execution defaults from biography", () => {
  const profile = read("docs/portable-skill-profile.md");
  assert.match(profile, /describes \*\*how work should be executed\*\*, not who the user is/);
  assert.match(profile, /Do not include biography/);
  assert.match(profile, /explicit current user instruction/);
  assert.match(profile, /Never claim behavioral parity merely because the same profile file loaded successfully/);
});
