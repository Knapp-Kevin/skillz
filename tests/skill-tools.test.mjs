// Behavior tests for skill-audit and skill-sync scripts.
// Plan: docs/plan-qor-phase1-meta-skill-audit-sync.md (gate 412faf5c…).
// Each test invokes the script as a child process and asserts on exit code
// plus output or filesystem state — no presence-only assertions.

import { test } from "node:test";
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync, existsSync, readFileSync, writeFileSync, readdirSync, realpathSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const AUDIT = join(ROOT, "skills", "skill-audit", "scripts", "audit.ts");
const SYNC = join(ROOT, "skills", "skill-sync", "scripts", "sync.ts");

function run(script, args) {
  const res = spawnSync(process.execPath, [script, ...args], {
    cwd: ROOT, encoding: "utf8", timeout: 120_000,
  });
  return { code: res.status, out: `${res.stdout}\n${res.stderr}` };
}

function tmp(label) {
  return mkdtempSync(join(tmpdir(), `skillz-${label}-`));
}

test("audit-fails-on-bad-skill", () => {
  const { code, out } = run(AUDIT, ["--skills-dir", join(ROOT, "tests", "fixtures")]);
  assert.equal(code, 1, `expected exit 1, got ${code}\n${out}`);
  assert.match(out, /bad-skill/, "finding must name the offending skill dir");
  assert.match(out, /wrong-name/, "finding must name the mismatched frontmatter name");
});

test("audit-passes-on-repo", () => {
  const { code, out } = run(AUDIT, []);
  assert.equal(code, 0, `repo self-audit must pass\n${out}`);
});

test("audit-rejects-bad-registry-status", () => {
  const { code, out } = run(AUDIT, ["--registry", join(ROOT, "tests", "fixtures", "bad-registry.yaml")]);
  assert.equal(code, 1, `expected exit 1, got ${code}\n${out}`);
  assert.match(out, /yolo/, "finding must name the invalid status value");
});

test("sync-dry-run-mutates-nothing", () => {
  const dest = tmp("dry");
  try {
    const { code, out } = run(SYNC, ["--dest", dest]);
    assert.equal(code, 0, out);
    assert.equal(readdirSync(dest).length, 0, "dry-run must not write to dest");
    assert.match(out, /claude-pulse: create/, "dry-run must plan a create per portable skill");
    assert.match(out, /skills-pulse: create/);
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});

test("sync-apply-copies-and-reports-drift", () => {
  const dest = tmp("apply");
  try {
    const first = run(SYNC, ["--apply", "--dest", dest]);
    assert.equal(first.code, 0, first.out);
    const copied = join(dest, "claude-pulse", "SKILL.md");
    assert.ok(existsSync(copied), "apply must copy SKILL.md");
    writeFileSync(copied, readFileSync(copied, "utf8") + "\n<!-- drift -->\n");
    const second = run(SYNC, ["--dest", dest]);
    assert.equal(second.code, 0, second.out);
    assert.match(second.out, /claude-pulse: update/, "mutated copy must report update");
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});

test("sync-excludes-repo-bound", () => {
  const dest = tmp("bound");
  try {
    const { code, out } = run(SYNC, ["--apply", "--dest", dest]);
    assert.equal(code, 0, out);
    assert.match(out, /skill-audit: skip:repo-bound/);
    assert.match(out, /skill-sync: skip:repo-bound/);
    assert.ok(!existsSync(join(dest, "skill-audit")), "repo-bound skill must not deploy");
    assert.ok(!existsSync(join(dest, "skill-sync")), "repo-bound skill must not deploy");
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});

test("sync-junction-under-temp-root", () => {
  const root = tmp("junction");
  try {
    const { code, out } = run(SYNC, ["--apply", "--claude-user", "--claude-user-root", root]);
    assert.equal(code, 0, out);
    const link = join(root, "claude-pulse");
    assert.ok(existsSync(link), "junction must exist under temp root");
    assert.equal(
      realpathSync(link),
      realpathSync(join(ROOT, "skills", "claude-pulse")),
      "junction must resolve to the skill directory",
    );
    assert.ok(!existsSync(join(root, "skill-audit")), "no repo-bound entries under temp root");
    assert.ok(!existsSync(join(root, "skill-sync")), "no repo-bound entries under temp root");
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test("sync-coreforge-manifest-shape", () => {
  const dest = tmp("coreforge");
  try {
    const { code, out } = run(SYNC, ["--apply", "--coreforge", dest]);
    assert.equal(code, 0, out);
    const manifest = JSON.parse(readFileSync(join(dest, "claude-pulse", "manifest.json"), "utf8"));
    assert.deepEqual(
      Object.keys(manifest).sort(),
      ["category", "description", "entryPoint", "name", "permissions", "runtime", "skillId", "version"],
      "manifest must contain exactly the declared field set",
    );
    assert.equal(manifest.skillId, "claude-pulse");
    assert.equal(manifest.entryPoint, "SKILL.md");
    const fm = readFileSync(join(ROOT, "skills", "claude-pulse", "SKILL.md"), "utf8");
    const version = fm.match(/^\s+version:\s*(\S+)/m)?.[1];
    assert.equal(manifest.version, version, "manifest version must match frontmatter");
  } finally {
    rmSync(dest, { recursive: true, force: true });
  }
});
