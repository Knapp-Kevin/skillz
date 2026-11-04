#!/usr/bin/env node
// Passive snapshot renderer. Built-in Node only; no network, no third-party code.
import {readFileSync,writeFileSync} from "node:fs";
import {resolve,dirname} from "node:path";
import {fileURLToPath} from "node:url";
function esc(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;")}
function check(s){if(s.schema_version!=="skillz-public-security-and-curation-v3"||s.non_additive!==true||s.merged_main.domains!==33||s.merged_main.research_topics>s.merged_main.topics||s.q8_merged_checkpoint.study_domains>s.merged_main.domains||s.approved_unchanged!==0||s.behaviorally_validated!==0)throw Error("Unsafe/invalid dashboard source");if(s.q8_merged_checkpoint.publication_state!=="MERGED_STUDY_ONLY"||s.merged_main.study_references!==s.q8_merged_checkpoint.study_references||s.merged_main.study_domains!==s.q8_merged_checkpoint.study_domains||s.merged_main.selected_topics>s.merged_main.topics||s.open_prs_at_snapshot<0)throw Error("Merged Q8 status inconsistent");const f=s.repair_frontier;if(!f||f.changed_packages!==f.existing_exact_tree_static_pass+f.needs_new_exact_tree_scan||f.observed_behavior_pass!==0||f.unchanged_use_approvals!==0||f.by_pr.reduce((n,x)=>n+x.total,0)!==f.changed_packages||f.by_pr.reduce((n,x)=>n+x.matched_pass,0)!==f.existing_exact_tree_static_pass)throw Error("Repair frontier totals disagree");for(const v of Object.values(s.security))if(v.total!==v.passed+v.failed+v.incomplete)throw Error("Security totals do not match")}

function checkFrontierSnapshot(s,f){
 const v=s.repair_frontier,t=f?.totals;
 const whole=n=>Number.isSafeInteger(n)&&n>=0;
 if(f?.schema_version!=="skillz-active-repair-security-frontier-v1"||f.issue!==s.security_issue||!v||!t||!Array.isArray(f.by_pr)||!Array.isArray(v.by_pr)||!Array.isArray(f.records))throw Error("Invalid canonical security frontier");
 const parity=[["changed_packages","changed_packages"],["existing_exact_tree_static_pass","verified_pinned_scan_pass"],["needs_new_exact_tree_scan","need_new_scan"],["observed_behavior_pass","behavioral_validations"],["unchanged_use_approvals","unchanged_use_approvals"]];
 for(const [published,source] of parity)if(!whole(t[source])||v[published]!==t[source])throw Error("Public security total differs from canonical frontier: "+published);
 if(f.by_pr.length!==v.by_pr.length||s.open_prs_at_snapshot!==f.by_pr.length)throw Error("Stale published open-PR count");
 const prs=new Map();
 for(const p of f.by_pr){
  if(!whole(p.pr)||p.pr===0||!(/^[a-f0-9]{40}$/).test(p.head)||prs.has(p.pr)||!whole(p.total)||!whole(p.matched_pass)||!whole(p.new_scans_needed)||p.total!==p.matched_pass+p.new_scans_needed)throw Error("Invalid canonical PR allocation");
  prs.set(p.pr,p);
 }
 const seenPublic=new Set();
 for(const p of v.by_pr){
  const source=prs.get(p.pr);
  if(!source||seenPublic.has(p.pr)||!["head","total","matched_pass","new_scans_needed"].every(k=>p[k]===source[k]))throw Error("Stale or conflicting public PR allocation: "+p.pr);
  seenPublic.add(p.pr);
 }
 const ids=new Set(),counts=new Map();
 let passing=0,pending=0;
 for(const item of f.records){
  const pr=prs.get(item.pr);
  if(!pr||typeof item.id!=="string"||!item.id||ids.has(item.id)||item.pr_head!==pr.head||item.host_behavior!=="not-run"||item.unchanged_use_approved!==false)throw Error("Malformed or duplicated package entry");
  ids.add(item.id);
  const n=counts.get(item.pr)||{total:0,matched_pass:0,new_scans_needed:0};
  n.total++;
  if(item.security_state==="passed"){
   if(item.package_tree_sha!==item.prior_scanned_tree_sha||item.security_evidence?.coverage_status!=="complete"||!(/^[a-f0-9]{64}$/).test(item.security_evidence?.report_sha256||""))throw Error("Nonmatching exact-tree scanner pass: "+item.id);
   passing++;n.matched_pass++;
  }else if(item.security_state==="not-run-current-tree"){
   if(item.security_evidence!==null||item.package_tree_sha===item.prior_scanned_tree_sha)throw Error("Incorrect pending package identity: "+item.id);
   pending++;n.new_scans_needed++;
  }else throw Error("New scan disposition needs explicit accounting support: "+item.id);
  counts.set(item.pr,n);
 }
 for(const [id,pr] of prs){
  const count=counts.get(id);
  if(!count||!["total","matched_pass","new_scans_needed"].every(k=>pr[k]===count[k]))throw Error("Per-PR package counts disagree: "+id);
 }
 if(ids.size!==t.changed_packages||passing!==t.verified_pinned_scan_pass||pending!==t.need_new_scan||passing+pending!==ids.size)throw Error("Canonical package counts disagree with details");
 return true;
}

function rect(x,y,w,h,fill,r=12){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${fill}"/>`}
function label(x,y,v,size=16,color="#e6ecfa",weight=400,anchor="start"){return `<text x="${x}" y="${y}" fill="${color}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}">${esc(v)}</text>`}
function bar(x,y,w,title,v){const parts=[["passed","#43c8b0"],["failed","#ee7785"],["incomplete","#788da9"]];let out=label(x,y-12,title,18,"#f0f4ff",700),at=x;for(const [key,color]of parts){const width=w*v[key]/v.total;out+=rect(at,y,width,20,color,0);at+=width}out+=label(x,y+50,`${v.passed} pass`,15,"#43c8b0",700)+label(x+144,y+50,`${v.failed} fail`,15,"#ee7785",700)+label(x+272,y+50,`${v.incomplete} incomplete`,15,"#b4c4d7",700);return out}
function repairBar(x,y,w,v){const done=w*v.existing_exact_tree_static_pass/v.changed_packages;let a=label(x,y-12,`${v.by_pr.length} OPEN REPAIR PRS  •  ${v.changed_packages} EXACT PACKAGES`,17,"#f0f4ff",700);a+=rect(x,y,done,20,"#43c8b0",0)+rect(x+done,y,w-done,20,"#788da9",0);a+=label(x,y+47,`${v.existing_exact_tree_static_pass} matching static passes`,15,"#43c8b0",700)+label(x+307,y+47,`${v.needs_new_exact_tree_scan} need new scans`,15,"#b4c4d7",700);return a}
function render(s){check(s);const a=s.merged_main,b=s.q8_merged_checkpoint,e=[];e.push(`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760" role="img" aria-labelledby="title desc"><title id="title">Skillz security and capability snapshot ${esc(s.as_of)}</title><desc id="desc">Merged Q8 ${a.study_references} study methods across ${a.study_domains} domains and ${a.selected_topics} distinct subtopics, ${b.exact_static_decisions} exact static decisions and ${b.review_queue} awaiting qualification. Main historical first-party scan 25 passed, 1 failed, 25 incomplete. Q8 study reference scan 10 passed, 7 failed, 33 incomplete. Unmerged repair frontier: ${s.repair_frontier.existing_exact_tree_static_pass} existing exact-tree passes, ${s.repair_frontier.needs_new_exact_tree_scan} need new scans. No unchanged-use approvals.</desc>`);e.push(rect(0,0,1200,760,"#0b1628",0));e.push(rect(24,24,1152,712,"#13243a",22));e.push(label(55,75,"SKILLZ  /  SECURITY + CURATION STATUS",25,"#f0f4ff",800));e.push(label(1140,75,`SNAPSHOT ${s.as_of}`,14,"#a8bdd5",600,"end"));e.push(rect(54,97,530,112,"#1b304b",14));e.push(rect(604,97,540,112,"#1b304b",14));e.push(label(78,128,"MERGED MAIN  •  SELECTED FOR STUDY",15,"#a8bdd5",700));e.push(label(78,174,`${a.study_references} methods  /  ${a.study_domains} domains`,30,"#f0f4ff",750));e.push(label(629,128,"Q8 MERGED  •  QUALIFICATION PROGRESS",15,"#a8bdd5",700));e.push(label(629,174,`${b.exact_static_decisions.toLocaleString("en-US")} decisions  /  ${b.review_queue.toLocaleString("en-US")} queued`,25,"#f0f4ff",750));e.push(label(64,250,`${a.domains} domains  ·  ${a.topics} topics  ·  ${a.research_topics} with research leads`,17,"#d4e0ed",600));e.push(label(64,283,`${a.first_party_skills} first-party skills  ·  ${a.selected_topics} featured subtopics  ·  ${s.approved_unchanged} approved unchanged`,15,"#aec0d6"));e.push(rect(54,312,1090,355,"#1b304b",14));e.push(label(77,348,"PINNED STATIC SECURITY SCANS  •  DIFFERENT POPULATIONS",17,"#e6edfa",750));e.push(bar(78,390,690,"FIRST-PARTY MAIN SNAPSHOT  •  51 PACKAGES",s.security.first_party_main));e.push(bar(78,482,690,"Q8 STUDY REFERENCE SNAPSHOT  •  50 PACKAGES",s.security.q8_study_merged));e.push(repairBar(78,580,690,s.repair_frontier));e.push(rect(839,383,274,122,"#12263b",12));e.push(label(976,421,"0",44,"#f0f4ff",800,"middle"));e.push(label(976,446,"APPROVED UNCHANGED",13,"#a8bed5",700,"middle"));e.push(label(976,474,"ISSUE #402: OPEN",15,"#f4ae8b",700,"middle"));e.push(label(56,713,"Dated evidence only. Passed static scans never authorize use; all 34 repair packages need independent behavior acceptance.",14,"#a8bdd5"));e.push("</svg>");return e.join("\n")+"\n"}
const root=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const src=resolve(root,"registry/public-security-curation-status-20261104.json");
const dest=resolve(root,"docs/assets/security-and-curation-status.svg");
const raw=JSON.parse(readFileSync(src,"utf8"));
const frontier=JSON.parse(readFileSync(resolve(root,"registry/security/active-first-party-repair-frontier-20261104.json"),"utf8"));
checkFrontierSnapshot(raw,frontier);
const svg=render(raw);
if(process.argv.includes("--self-test")){const bad=structuredClone(raw);bad.security.first_party_main.passed++;let rejected=false;try{render(bad)}catch{rejected=true}if(!rejected)throw Error("self test: did not reject bad totals");const corrupt=structuredClone(raw);corrupt.repair_frontier.by_pr[0].head="0".repeat(40);let staleRejected=false;try{checkFrontierSnapshot(corrupt,frontier)}catch{staleRejected=true}if(!staleRejected)throw Error("self test: stale PR head accepted");
const inflated=structuredClone(frontier);inflated.totals.verified_pinned_scan_pass++;let inflatedRejected=false;try{checkFrontierSnapshot(raw,inflated)}catch{inflatedRejected=true}if(!inflatedRejected)throw Error("self test: unsupported scanner pass accepted");
const wrongPackage=structuredClone(frontier);wrongPackage.records[0].package_tree_sha="0".repeat(40);let treeRejected=false;try{checkFrontierSnapshot(raw,wrongPackage)}catch{treeRejected=true}if(!treeRejected)throw Error("self test: mismatched package tree accepted");
console.log("self-test passed");}
else if(process.argv.includes("--check")){if(readFileSync(dest,"utf8")!==svg)throw Error("SVG differs from input");console.log("check passed");}
else{writeFileSync(dest,svg);console.log("wrote SVG");}
