// Behavioral contract tests for Issue #7 bootstrap/onboarding.
// These tests guard the promises the beginner entry point makes to users and
// the source/provenance facts the orchestration skill depends on.

import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(ROOT, path), "utf8");

test("bootstrap beginner path does not require prior skill knowledge", () => {
  const doc = read("BOOTSTRAP.md");
  assert.match(doc, /You do not need to know what an AI skill is\./);
  assert.match(doc, /Read `BOOTSTRAP\.md` and help me figure out which skills would make you better at helping me\./);
  assert.match(doc, /Do not guess about information you cannot see\./);
  assert.match(doc, /smallest set of skills that actually makes your AI better for you/i);
});

test("bootstrap skill degrades honestly when history or tools are unavailable", () => {
  const skill = read("skills/skill-bootstrap/SKILL.md");
  assert.match(skill, /Unavailable sources are recorded as unavailable/);
  assert.match(skill, /Never claim inaccessible sources were reviewed/);
  assert.match(skill, /Missing evidence is a finding/);
  assert.match(skill, /DO NOT CREATE/);
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

test("community reference source preserves Matt Pocock provenance", () => {
  const sources = read("registry/sources.yaml");
  const modules = read(".gitmodules");
  const provenance = read("docs/third-party-provenance.md");

  assert.match(sources, /id: mattpocock-skills/);
  assert.match(sources, /class: community-vetted/);
  assert.match(sources, /license: MIT/);
  assert.match(sources, /pinned_revision: 6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/);
  assert.match(modules, /https:\/\/github\.com\/mattpocock\/skills\.git/);
  assert.match(provenance, /Copyright \(c\) 2026 Matt Pocock/);
});

test("index generator exposes source trust and excludes non-active community skill areas", () => {
  const script = read("scripts/build-index.ts");
  assert.match(script, /sourceClass: "community-vetted"/);
  assert.match(script, /excludeDirs: \["deprecated", "in-progress"\]/);
  assert.match(script, /sourceRegistry: "registry\/sources\.yaml"/);
  assert.match(script, /bootstrap: "BOOTSTRAP\.md"/);
});

test("portable profile separates execution defaults from biography", () => {
  const profile = read("docs/portable-skill-profile.md");
  assert.match(profile, /describes \*\*how work should be executed\*\*, not who the user is/);
  assert.match(profile, /Do not include biography/);
  assert.match(profile, /explicit current user instruction/);
  assert.match(profile, /Never claim behavioral parity merely because the same profile file loaded successfully/);
});
