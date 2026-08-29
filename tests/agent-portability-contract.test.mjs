import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(ROOT, path), "utf8");

const START = read("AGENT_START_HERE.md");
const README = read("README.md");
const BOOTSTRAP = read("BOOTSTRAP.md");
const AGENTS = read("AGENTS.md");
const SMOKE = read("docs/evals/connector-native-smoke.md");

test("agent use has a zero-local-runtime entry contract", () => {
  assert.match(START, /If you can read this repository, you can use `skillz`/);
  assert.match(START, /Connector\/API\/web path/);
  assert.match(START, /do not require a local clone, shell, Git executable, Node, Bun/i);
  assert.match(README, /No shell, clone, Node, or local filesystem\? That is supported/i);
  assert.match(README, /maintenance_runtime/i);
  assert.match(BOOTSTRAP, /not required for normal bootstrap or refinement/i);
  assert.match(AGENTS, /Missing local execution is not a normal-use blocker/i);
});

test("connector-native quality lookup is exact-version aware", () => {
  for (const text of [START, BOOTSTRAP, AGENTS]) {
    assert.match(text, /content.*SHA|blob.*SHA|fingerprint/i);
    assert.match(text, /do not.*fabricat|rather than fabricat|Do not invent/i);
  }
});

test("portability smoke records a connector-only exact fingerprint match", () => {
  assert.match(SMOKE, /connector-only ChatGPT host/i);
  assert.match(SMOKE, /061c25a524acaa93d4534e9e08a793c0a5fe45fd/);
  assert.match(SMOKE, /exact fingerprint match established without local execution/i);
  assert.match(SMOKE, /maintenance\/release proof, not a prerequisite for normal agent use/i);
});
