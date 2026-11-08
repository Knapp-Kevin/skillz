#!/usr/bin/env node
// Maintenance-only integrity check. Reads local passive JSON; no network, install, CI or execution of skills.
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const load = (p) => JSON.parse(fs.readFileSync(path.join(root, p), 'utf8'));
const fail = (msg) => { throw new Error('Authored capability index: ' + msg); };
const authored = load('registry/authored-skills-index.json').skills;
const directory = load('registry/capability-directory.json');
const names = load('registry/governed-review-name-index.json');
const records = new Map(directory.skill_records.map(r => [r.id, r]));
const byPath = new Map(directory.domains.flatMap(d => d.subdomains.map(s => [d.id + '/' + s.id, s])));
const firstParty = new Set(names.first_party_ids);
const unique = new Set();

for (const skill of authored) {
  if (unique.has(skill.id)) fail('duplicate authored ID ' + skill.id);
  unique.add(skill.id);
  if (!skill.package_path?.startsWith('skills/authored/')) fail(skill.id + ': unexpected package folder');
  const entry = skill.package_path + '/SKILL.md';
  if (skill.entrypoint !== entry || !fs.existsSync(path.join(root, entry))) fail(skill.id + ': missing entrypoint');
  if (!skill.verification_path || !fs.existsSync(path.join(root, skill.verification_path))) fail(skill.id + ': missing verification');
  if (!skill.provenance_path || !fs.existsSync(path.join(root, skill.provenance_path))) fail(skill.id + ': missing provenance');
  if (!/^[0-9a-f]{40}$/.test(skill.skill_blob_sha ?? '') || !/^[0-9a-f]{40}$/.test(skill.package_tree_sha ?? '')) fail(skill.id + ': missing exact Git identity');
  const id = 'local-skills/' + skill.id;
  if (!firstParty.has(id)) fail(skill.id + ': absent governed review name');
  const record = records.get(id);
  if (!record || record.source_role !== 'first-party' || record.source_class !== 'first-party-authored') fail(skill.id + ': absent/wrong canonical record');
  if (record.content_blob_sha !== skill.skill_blob_sha || record.complete_package_tree_sha !== skill.package_tree_sha || record.evidence_path !== skill.verification_path || record.skill_path !== entry) fail(skill.id + ': review or source fingerprint drift');
  if (!Array.isArray(skill.capability_paths) || !skill.capability_paths.length) fail(skill.id + ': no capability routes');
  if (new Set(skill.capability_paths).size !== skill.capability_paths.length) fail(skill.id + ': duplicate routes');
  const recPaths = record.capability_paths || [];
  if (new Set(recPaths).size !== recPaths.length || recPaths.length !== skill.capability_paths.length || skill.capability_paths.some(p => !recPaths.includes(p))) fail(skill.id + ': mismatched mapped paths');
  for (const p of skill.capability_paths) {
    const s = byPath.get(p);
    if (!s || s.matched_skill_ids.filter(x => x === id).length !== 1) fail(skill.id + ': missing or repeated subdomain link ' + p);
  }
  if (record.validation_status !== skill.behavioral_validation) fail(skill.id + ': contradictory behavioral status');
}

if (names.record_counts.first_party !== names.first_party_ids.length ||
    names.record_counts.third_party !== names.third_party_ids.length ||
    names.record_counts.total !== names.first_party_ids.length + names.third_party_ids.length) fail('name denominators drift');
const mapped = new Set(directory.domains.flatMap(d => d.subdomains.flatMap(s => s.matched_skill_ids)));
if (mapped.size !== records.size || [...records.keys()].some(id => !mapped.has(id))) fail('directory skill records differ from linked IDs');
if (directory.identity_level_capability_links_mapped !== records.size) fail('mapped identity count drift');
if (directory.governed_identity_denominator !== names.record_counts.total) fail('governed denominator drift');
if (directory.unmapped_review_identity_count !== names.record_counts.total - records.size) fail('unmapped denominator drift');
const linkedSubs = [...byPath.values()].filter(s => s.matched_skill_ids.length).length;
if (directory.navigation_population.subdomains_with_evidence_linked_examples !== linkedSubs) fail('linked subdomain count drift');
for (const d of directory.domains) {
  const overview = directory.browse_overview.find(b => b.domain === d.id);
  if (!overview) fail('missing domain overview ' + d.id);
  if (overview.linked_reviewed_examples !== new Set(d.subdomains.flatMap(s => s.matched_skill_ids)).size) fail('domain overview count drift ' + d.id);
  if (overview.subdomains_with_linked_examples !== d.subdomains.filter(s => s.matched_skill_ids.length).length) fail('subdomain overview count drift ' + d.id);
}
console.log('Authored routing OK:', authored.length, 'authored,', records.size, 'mapped identities,', linkedSubs, 'linked subdomains');
