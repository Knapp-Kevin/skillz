import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const RENDER = join(ROOT, "scripts", "render-alpha-scenario.ts");

function render(id) {
  const result = spawnSync(process.execPath, [RENDER, id, "--json"], {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 30_000,
  });
  assert.equal(result.status, 0, result.stderr);
  return { text: result.stdout, json: JSON.parse(result.stdout) };
}

test("scenario renderer exposes neutral user evidence but not the answer key", () => {
  for (const id of ["A1", "A2", "A3", "R1", "R2"]) {
    const { text, json } = render(id);
    assert.equal(json.scenario_id, id);
    assert.ok(json.mode);
    assert.ok(json.prompt);
    assert.doesNotMatch(text, /expected_decision/i);
    assert.doesNotMatch(text, /must_observe/i);
    assert.doesNotMatch(text, /must_not/i);
    assert.doesNotMatch(text, /candidate_hint/i);
  }
});

test("first-visit scenarios do not leak the expected third-party candidate", () => {
  assert.doesNotMatch(render("A1").text, /review-team/i);
  assert.doesNotMatch(render("A2").text, /context-engineering/i);
});
