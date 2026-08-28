import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const RENDER = join(ROOT, "scripts", "render-alpha-scenario.ts");
const IDS = ["K7M", "Q2F", "L9C", "W4H", "D8N"];

function render(id) {
  const result = spawnSync(process.execPath, [RENDER, id, "--json"], {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 30_000,
  });
  assert.equal(result.status, 0, result.stderr);
  return { text: result.stdout, json: JSON.parse(result.stdout) };
}

test("scenario renderer exposes neutral public context but not evaluator-only fields", () => {
  for (const id of IDS) {
    const { text, json } = render(id);
    assert.equal(json.scenario_set, "initial-alpha-v2-2026-08-28");
    assert.equal(json.scenario_id, id);
    assert.ok(json.mode);
    assert.ok(json.prompt);
    assert.doesNotMatch(text, /expected_decision/i);
    assert.doesNotMatch(text, /must_observe/i);
    assert.doesNotMatch(text, /must_not/i);
    assert.doesNotMatch(text, /candidate_hint/i);
    assert.doesNotMatch(text, /answer_key/i);
  }
});

test("rotated first-visit scenarios do not leak private candidate hints", () => {
  assert.doesNotMatch(render("K7M").text, /google-agents-cli-eval/i);
  assert.doesNotMatch(render("Q2F").text, /browser-testing-with-devtools/i);
});

test("legacy compromised scenario identifiers are no longer valid treatment inputs", () => {
  for (const id of ["A1", "A2", "A3", "R1", "R2"]) {
    const result = spawnSync(process.execPath, [RENDER, id, "--json"], {
      cwd: ROOT,
      encoding: "utf8",
      timeout: 30_000,
    });
    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /Unknown scenario/);
  }
});
