import { test } from "node:test";
import assert from "node:assert/strict";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const VERIFIER = join(ROOT, "scripts", "verify-vendor-materialization.ts");

function git(cwd, args) {
  const result = spawnSync("git", args, { cwd, encoding: "utf8" });
  assert.equal(result.status, 0, `git ${args.join(" ")} failed: ${result.stderr}`);
  return result.stdout.trim();
}

function runVerifier(repoRoot) {
  return spawnSync(process.execPath, [VERIFIER, "--repo-root", repoRoot], {
    cwd: ROOT,
    encoding: "utf8",
  });
}

function makeFixture(t) {
  const base = mkdtempSync(join(tmpdir(), "skillz-vendor-materialization-"));
  t.after(() => rmSync(base, { recursive: true, force: true }));

  const source = join(base, "source");
  mkdirSync(source);
  git(source, ["init", "-q"]);
  git(source, ["config", "user.email", "fixture@example.test"]);
  git(source, ["config", "user.name", "Fixture"]);
  writeFileSync(join(source, "SKILL.md"), "---\nname: sample\ndescription: Sample. Use when testing.\n---\n");
  git(source, ["add", "SKILL.md"]);
  git(source, ["commit", "-qm", "initial source"]);

  const parent = join(base, "parent");
  mkdirSync(parent);
  git(parent, ["init", "-q"]);
  git(parent, ["config", "user.email", "fixture@example.test"]);
  git(parent, ["config", "user.name", "Fixture"]);
  mkdirSync(join(parent, "registry"));
  writeFileSync(join(parent, "registry", "sources.yaml"), [
    "version: 2",
    "sources:",
    "  - id: sample-source",
    "    name: Sample Source",
    "    source: https://example.test/sample",
    "    class: fixture",
    "    source_role: vendored-corpus",
    "    resolved_path: skills/sources/sample",
    "    inclusion: vendored",
    "",
  ].join("\n"));
  git(parent, ["add", "registry/sources.yaml"]);
  git(parent, ["commit", "-qm", "registry"]);
  git(parent, ["-c", "protocol.file.allow=always", "submodule", "add", "-q", source, "skills/sources/sample"]);
  git(parent, ["commit", "-qam", "pin sample source"]);

  return { base, source, parent, submodule: join(parent, "skills", "sources", "sample") };
}

test("vendor materialization verifier accepts a clean superproject and initialized clean exact pin", (t) => {
  const { parent } = makeFixture(t);
  const result = runVerifier(parent);
  assert.equal(result.status, 0, result.stderr || result.stdout);
  assert.match(result.stdout, /PASS: clean superproject; all 1 vendored sources are initialized, clean, and pinned exactly/);
});

test("vendor materialization verifier rejects dirty superproject state", (t) => {
  const { parent } = makeFixture(t);
  writeFileSync(join(parent, "UNTRACKED.txt"), "not part of the evaluated commit\n");

  const result = runVerifier(parent);
  assert.notEqual(result.status, 0);
  assert.match(`${result.stdout}\n${result.stderr}`, /superproject is dirty/i);
});

test("vendor materialization verifier rejects an uninitialized or missing submodule", (t) => {
  const { parent, submodule } = makeFixture(t);
  rmSync(submodule, { recursive: true, force: true });
  const result = runVerifier(parent);
  assert.notEqual(result.status, 0);
  assert.match(`${result.stdout}\n${result.stderr}`, /not materialized|not initialized/i);
});

test("vendor materialization verifier rejects a submodule HEAD different from the gitlink", (t) => {
  const { parent, submodule } = makeFixture(t);
  git(submodule, ["config", "user.email", "fixture@example.test"]);
  git(submodule, ["config", "user.name", "Fixture"]);
  writeFileSync(join(submodule, "SKILL.md"), `${readFileSync(join(submodule, "SKILL.md"), "utf8")}\nchanged\n`);
  git(submodule, ["add", "SKILL.md"]);
  git(submodule, ["commit", "-qm", "advance without updating gitlink"]);

  const result = runVerifier(parent);
  assert.notEqual(result.status, 0);
  assert.match(`${result.stdout}\n${result.stderr}`, /does not match pinned gitlink/i);
});

test("vendor materialization verifier rejects dirty source content", (t) => {
  const { parent, submodule } = makeFixture(t);
  writeFileSync(join(submodule, "UNTRACKED-SKILL.md"), "not part of the pin\n");

  const result = runVerifier(parent);
  assert.notEqual(result.status, 0);
  assert.match(`${result.stdout}\n${result.stderr}`, /is dirty/i);
});
