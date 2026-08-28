// Behavioral contract tests for bootstrap/onboarding and library boundaries.

import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { readFileSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(ROOT, path), "utf8");

test("README is human-first while giving AI agents an explicit jump target", () => {
  const readme = read("README.md");
  const humanStart = readme.indexOf("## Start here");
  const agentSection = readme.indexOf("## If you are an AI agent reading this");

  assert.ok(humanStart >= 0, "human start section must exist");
  assert.ok(agentSection > humanStart, "human instructions must precede the detailed agent section");
  assert.match(readme, /> \*\*AI agent\?\*\* Jump directly to \[If you are an AI agent reading this\]/);
  assert.match(readme, /\[`AGENTS\.md`\]\(AGENTS\.md\)/);
  assert.match(readme, /\[`BOOTSTRAP\.md`\]\(BOOTSTRAP\.md\)/);
});

test("repository exposes first-visit, returning-user, and direct-library paths", () => {
  const readme = read("README.md");
  const bootstrap = read("BOOTSTRAP.md");
  const agents = read("AGENTS.md");

  assert.match(readme, /### First visit: build your skill set/);
  assert.match(readme, /### Returning visit: review, refine, and improve/);
  assert.match(bootstrap, /## First visit: build a fitted skill set/);
  assert.match(bootstrap, /## Returning visit: review, refine, and improve/);
  assert.match(agents, /### Direct library mode/);
  assert.match(agents, /### First-visit bootstrap mode/);
  assert.match(agents, /### Returning-user refinement mode/);
});

test("returning-user flow preserves valid behavior and makes the smallest justified changes", () => {
  const readme = read("README.md");
  const bootstrap = read("BOOTSTRAP.md");
  const agents = read("AGENTS.md");

  assert.match(readme, /preserve custom behavior that still matches how you work/);
  assert.match(readme, /smallest useful set/);
  assert.match(bootstrap, /do not restart from zero/i);
  assert.match(bootstrap, /no change needed/i);
  assert.match(bootstrap, /Preserve custom behavior that still fits/);
  assert.match(agents, /Make the smallest justified changes/);
  assert.match(agents, /no changes are needed/);
});

test("library inventory is structurally separate from engine machinery", () => {
  const engineSkills = [
    "skill-bootstrap",
    "skill-audit",
    "skill-eval",
    "skill-forge",
    "skill-sync",
    "skills-pulse",
    "source-vetting",
  ];

  for (const name of engineSkills) {
    assert.ok(existsSync(join(ROOT, "engine", "skills", name, "SKILL.md")), `${name} must exist under engine/skills`);
    assert.ok(!existsSync(join(ROOT, "skills", name)), `${name} must not count as library inventory`);
  }

  const libraryReadme = read("skills/README.md");
  const engineReadme = read("engine/README.md");
  assert.match(libraryReadme, /Every user-facing skill under `skills\/` counts/);
  assert.match(engineReadme, /Nothing under `engine\/` counts as skill-library inventory/);
});

test("humans can browse local skills by purpose without changing canonical skill IDs", () => {
  const readme = read("README.md");
  const categories = read("skills/categories/README.md");

  for (const category of [
    "Planning & Productivity",
    "Writing & Communication",
    "Research & Analysis",
    "Software & Repositories",
    "Agent Operations & Security",
    "Monitoring & Intelligence",
    "Business & Career",
  ]) {
    assert.match(readme, new RegExp(category.replaceAll("&", "&")));
    assert.match(categories, new RegExp(category.replaceAll("&", "&")));
  }
  assert.match(categories, /canonical skill directories remain directly under \[`skills\/`\]/i);
});

test("repository URL alone invokes first-visit bootstrap when no fitted set is being reviewed", () => {
  const readme = read("README.md");
  const agents = read("AGENTS.md");
  const skill = read("engine/skills/skill-bootstrap/SKILL.md");

  assert.match(readme, /simply provide the repository with no more specific task/);
  assert.match(agents, /begin first-visit bootstrap now/i);
  assert.match(agents, /Do not stop at a repository summary/);
  assert.match(skill, /that action is sufficient to trigger this skill/);
  assert.match(skill, /Begin bootstrap\./);
});

test("bootstrap beginner path does not require skill expertise or manual catalog shopping", () => {
  const readme = read("README.md");
  const doc = read("BOOTSTRAP.md");

  assert.match(readme, /You do not need to understand how agent skills work/);
  assert.match(readme, /You do not need to read hundreds of files/);
  assert.match(doc, /You do not need to understand skills, write code, or browse hundreds of files/);
  assert.match(doc, /Give your AI the GitHub link to this repository\. That is enough to start/);
  assert.match(doc, /smallest skill system that best fits this user/);
});

test("bootstrap uses accessible memory and history without inventing or over-collecting", () => {
  const readme = read("README.md");
  const agents = read("AGENTS.md");
  const skill = read("engine/skills/skill-bootstrap/SKILL.md");

  assert.match(readme, /history, memory, instructions, existing skills, recurring corrections, and workflows/);
  assert.match(agents, /Use relevant memory\/history before asking the user to repeat accessible information/);
  assert.match(agents, /Access to a private connector is capability, not consent to mine it for a profile/);
  assert.match(skill, /begin with relevant interaction history and persistent memory before asking the user to restate how they work/);
  assert.match(skill, /Do \*\*not\*\* sweep unrelated connected private accounts/);
});

test("reference corpus is design evidence and custom skills may beat reuse", () => {
  const readme = read("README.md");
  const agents = read("AGENTS.md");
  const skill = read("engine/skills/skill-bootstrap/SKILL.md");

  assert.match(readme, /Compare before creation\. User-fit before reuse\./);
  assert.match(agents, /Create a custom skill when that better matches the user's actual method/);
  assert.match(skill, /`CREATE` does not mean "no related skill exists\."/);
  assert.match(skill, /Design from the user's needs outward, not from the catalog inward/);
  assert.match(skill, /Do not force a known skill into the architecture merely to increase reuse/);
});

test("quality state is exact-version and source exception rationale is not public contract", () => {
  const readme = read("README.md");
  const agents = read("AGENTS.md");
  const sources = read("registry/sources.yaml");

  assert.match(readme, /The rules are version-specific/);
  assert.match(agents, /An individual characterization record applies only to its recorded Git blob SHA/);
  assert.match(sources, /A skill without an individual quality record is[\s\S]*treated as unverified/);
  assert.doesNotMatch(sources, /verification_default:/);
  assert.doesNotMatch(readme, /sole `trusted-baseline` source/);
  assert.doesNotMatch(agents, /sole current `trusted-baseline` source/);
});

test("bootstrap installation classifies execution paths and completion states", () => {
  const skill = read("engine/skills/skill-bootstrap/SKILL.md");
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
  const skill = read("engine/skills/skill-bootstrap/SKILL.md");
  const handoff = read("docs/installation-handoff.md");
  assert.match(skill, /Never report a UI-required upload as completed unless the host actually confirms it/);
  assert.match(handoff, /one action per numbered step/);
  assert.match(handoff, /end with one test prompt/);
});

test("portable profile records installation separately per host", () => {
  const profile = read("docs/portable-skill-profile.md");
  assert.match(profile, /installation_targets:/);
  assert.match(profile, /Installation is \*\*per host and per surface\*\*/);
  assert.match(profile, /describes \*\*how work should be executed\*\*, not who the user is/);
  assert.match(profile, /Do not include biography/);
});

test("third-party attribution and pinned provenance remain auditable", () => {
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

  const block = sources.match(/- id: mattpocock-skills[\s\S]*?(?=\n\s*- id:|$)/)?.[0] ?? "";
  const recorded = block.match(/pinned_revision:\s*([0-9a-f]{40})/)?.[1];
  assert.ok(recorded, "source registry must record a full pinned_revision");

  const gitlink = spawnSync("git", ["rev-parse", "HEAD:vendor/mattpocock-skills"], {
    cwd: ROOT,
    encoding: "utf8",
  });
  assert.equal(gitlink.status, 0, `must resolve vendored gitlink: ${gitlink.stderr}`);
  assert.equal(recorded, gitlink.stdout.trim(), "recorded provenance revision must match the actual vendored submodule pin");
});

test("index generator treats local skills as library inventory and engine skills separately", () => {
  const script = read("scripts/build-index.ts");
  assert.match(script, /const dir = join\(ROOT, "skills"\)/);
  assert.match(script, /function parseSourceRegistry/);
  assert.match(script, /const sourceRecords = parseSourceRegistry\(\)/);
  assert.match(script, /index_exclude_dirs/);
  assert.match(script, /sourceRegistry: "registry\/sources\.yaml"/);
  assert.match(script, /bootstrap: "BOOTSTRAP\.md"/);
  assert.doesNotMatch(script, /engine\/skills.*scanLocalSkills/s, "engine skills must not be mixed into library inventory");
});
