import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const SELECTOR = join(ROOT, "engine", "skills", "skill-bootstrap", "scripts", "select-candidates.ts");
const FIXTURE = join(ROOT, "tests", "fixtures", "governed-index.json");

function run(args) {
  const res = spawnSync(process.execPath, [SELECTOR, "--index", FIXTURE, "--json", ...args], {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 30_000,
  });
  return { code: res.status, out: res.stdout, err: res.stderr };
}

test("governed selector prefers eligible exact-version candidates", () => {
  const { code, out, err } = run(["--use-case", "debugging"]);
  assert.equal(code, 0, err);
  const result = JSON.parse(out);
  assert.equal(result.count, 1);
  assert.equal(result.candidates[0].name, "verified-debug");
  assert.equal(result.candidates[0].selectionUse, "eligible-unchanged");
  assert.match(result.candidates[0].matched.join(" "), /use_case:debugging/);
});

test("unverified material is excluded from trusted unchanged selection by default", () => {
  const { code, out, err } = run(["--use-case", "debugging"]);
  assert.equal(code, 0, err);
  const names = JSON.parse(out).candidates.map((c) => c.name);
  assert.ok(!names.includes("unverified-debug"));
  assert.ok(!names.includes("stale-debug"));
});

test("unverified material can be surfaced explicitly as design evidence", () => {
  const { code, out, err } = run(["--use-case", "debugging", "--include-unverified", "--limit", "10"]);
  assert.equal(code, 0, err);
  const result = JSON.parse(out);
  const unverified = result.candidates.find((c) => c.name === "unverified-debug");
  assert.ok(unverified, "explicit review mode should surface unverified design evidence");
  assert.equal(unverified.selectionUse, "design-evidence-only");
  assert.ok(!result.candidates.some((c) => c.name === "stale-debug"), "stale material stays blocked");
});

test("validation state contributes ranking without replacing tag fit", () => {
  const { code, out, err } = run(["--use-case", "research"]);
  assert.equal(code, 0, err);
  const result = JSON.parse(out);
  assert.equal(result.candidates[0].name, "validated-research");
  assert.equal(result.candidates[0].verificationStatus, "validated");
});
