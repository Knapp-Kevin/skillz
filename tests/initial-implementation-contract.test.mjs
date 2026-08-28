import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(ROOT, path), "utf8");

test("initial implementation is explicitly scoped around first-visit and returning-user experience", () => {
  const finish = read("docs/initial-implementation.md");
  assert.match(finish, /First visit/);
  assert.match(finish, /Returning visit/);
  assert.match(finish, /not required before alpha lock/i);
  assert.match(finish, /post-alpha enrichment/i);
});

test("README keeps humans first but gives AI agents an immediate direct route", () => {
  const readme = read("README.md");
  const human = readme.indexOf("## Start here");
  const agentJump = readme.indexOf("AI agent?");
  const agentSection = readme.indexOf("## If you are an AI agent reading this");
  assert.ok(human >= 0, "human start section must exist");
  assert.ok(agentJump >= 0, "AI agent jump must exist near the front door");
  assert.ok(agentSection > human, "full agent operating section should follow human guidance");
  assert.match(readme, /AGENTS\.md/);
  assert.match(readme, /BOOTSTRAP\.md/);
});

test("bootstrap and agent contracts cover both first visit and returning refinement", () => {
  const bootstrap = read("BOOTSTRAP.md");
  const agents = read("AGENTS.md");
  for (const doc of [bootstrap, agents]) {
    assert.match(doc, /First.?visit/i);
    assert.match(doc, /Returning/i);
    assert.match(doc, /smallest/i);
    assert.match(doc, /no change/i);
  }
});

test("governed selection is part of the bootstrap contract", () => {
  const bootstrap = read("BOOTSTRAP.md");
  const agents = read("AGENTS.md");
  assert.match(bootstrap, /select-candidates\.ts/);
  assert.match(agents, /select-candidates\.ts/);
  assert.match(bootstrap, /unverified/i);
  assert.match(bootstrap, /stale/i);
});

test("alpha proof matrix requires reuse refusal creation refinement and no-op", () => {
  const finish = read("docs/initial-implementation.md");
  for (const phrase of [
    "eligible reuse",
    "unsafe or unproven reuse refusal",
    "custom creation",
    "returning refinement",
    "returning no-op",
  ]) assert.match(finish, new RegExp(phrase, "i"));
});
