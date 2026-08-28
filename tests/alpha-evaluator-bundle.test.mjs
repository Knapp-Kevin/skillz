import { test } from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const VERIFY = join(ROOT, "scripts", "verify-alpha-evaluator-bundle.mjs");
const PUBLIC_PATH = join(ROOT, "docs", "evals", "fixtures", "initial-alpha-scenarios.json");

function privateBundle() {
  const bytes = readFileSync(PUBLIC_PATH);
  const fixture = JSON.parse(bytes.toString("utf8"));
  return {
    schema_version: 2,
    set_id: fixture.set_id,
    public_fixture_sha256: createHash("sha256").update(bytes).digest("hex"),
    scenarios: fixture.scenarios.map((scenario) => ({
      id: scenario.id,
      expected_decision: "FIXTURE_EXPECTATION",
      must_observe: ["criterion one", "criterion two", "criterion three"],
      must_not: ["forbidden one", "forbidden two", "forbidden three"],
    })),
  };
}

function runVerifier(path) {
  return spawnSync(process.execPath, [VERIFY, "--rubric", path], {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 30_000,
  });
}

function runWithBundle(t, mutate = () => {}) {
  const dir = mkdtempSync(join(tmpdir(), "skillz-alpha-evaluator-"));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const bundle = privateBundle();
  mutate(bundle);
  const path = join(dir, "private-rubric.json");
  writeFileSync(path, JSON.stringify(bundle, null, 2) + "\n");
  return runVerifier(path);
}

test("private evaluator bundle verifies when external location set id digest and scenario coverage match", (t) => {
  const result = runWithBundle(t);
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /PRIVATE \/ VERIFIED/);
  assert.match(result.stdout, /OUTSIDE REPOSITORY/);
});

test("private evaluator bundle rejects a valid rubric stored inside the treatment repository", (t) => {
  const path = join(ROOT, "skillz-initial-alpha-v2-private-rubric-test.json");
  t.after(() => rmSync(path, { force: true }));
  writeFileSync(path, JSON.stringify(privateBundle(), null, 2) + "\n");

  const result = runVerifier(path);
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /inside the repository\/treatment workspace/i);
});

test("private evaluator bundle rejects a public-fixture digest mismatch", (t) => {
  const result = runWithBundle(t, (bundle) => {
    bundle.public_fixture_sha256 = "0".repeat(64);
  });
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /SHA-256 mismatch/);
});

test("private evaluator bundle rejects missing scenario coverage", (t) => {
  const result = runWithBundle(t, (bundle) => {
    bundle.scenarios.pop();
  });
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /missing public scenario id|scenario count mismatch/);
});

test("private evaluator bundle rejects incomplete frozen scoring criteria", (t) => {
  const result = runWithBundle(t, (bundle) => {
    bundle.scenarios[0].must_observe = ["only one"];
  });
  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /must_observe must contain at least 3 criteria/);
});
