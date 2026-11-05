#!/usr/bin/env node
// Skillz Q8 direct-source review graphic. Deterministic, network-free, no source scripts executed.
// Add each new exact-source review ledger to this manifest; counts derive from actual records.
import {readFileSync,writeFileSync} from "node:fs";
import {resolve,dirname} from "node:path";
import {fileURLToPath} from "node:url";
const ROOT=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const FILE=p=>JSON.parse(readFileSync(resolve(ROOT,p),"utf8"));
const HISTORICAL="registry/security/q12-featured-security-evidence-reconciliation-20261103.json";
const REVIEW_LEDGERS=[
  "registry/security/third-party-three-failed-static-dispositions-20261105.json",
  "registry/security/remaining-q8-four-failed-static-dispositions-20261105.json",
  "registry/security/q8-three-incomplete-high-risk-static-dispositions-20261105.json",
  "registry/security/q8-three-incomplete-privacy-and-code-static-dispositions-20261105.json",
  "registry/security/q8-three-incomplete-execution-and-rights-static-dispositions-20261105.json"
];
const TEMPLATE="<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1200\" height=\"650\" viewBox=\"0 0 1200 650\" role=\"img\" aria-labelledby=\"title desc\">\n<title id=\"title\">Skillz Q8 risk-review progress, November 5 2026</title>\n<desc id=\"desc\">Direct exact-version static content review progress: @@FAILED_DONE@@ of @@FAILED_TOTAL@@ historically failed packages and @@INCOMPLETE_DONE@@ of @@INCOMPLETE_TOTAL@@ historically incomplete packages reviewed. @@LEFT@@ incomplete packages remain. Historical scanner states unchanged. No observed behavioral acceptance or unchanged-use approvals.</desc>\n<rect width=\"1200\" height=\"650\" fill=\"#0b162a\"/>\n<rect x=\"22\" y=\"20\" width=\"1156\" height=\"610\" rx=\"23\" fill=\"#14263d\" stroke=\"#2a4462\"/>\n<text x=\"54\" y=\"65\" font-family=\"Arial,sans-serif\" font-size=\"26\" font-weight=\"700\" fill=\"#f2f6ff\">SKILLZ / DIRECT STATIC RISK REVIEWS</text>\n<text x=\"1148\" y=\"65\" font-family=\"Arial,sans-serif\" text-anchor=\"end\" font-size=\"14\" font-weight=\"700\" fill=\"#a6bdd5\">NOV 05, 2026</text>\n<text x=\"54\" y=\"96\" font-family=\"Arial,sans-serif\" font-size=\"17\" fill=\"#c9d7e8\">Pinned Q8 source packages, read as data. Scanner outcomes and permissions stay separate.</text>\n<rect x=\"53\" y=\"135\" width=\"526\" height=\"245\" rx=\"16\" fill=\"#213651\"/>\n<rect x=\"602\" y=\"135\" width=\"546\" height=\"245\" rx=\"16\" fill=\"#213651\"/>\n<text x=\"79\" y=\"180\" font-family=\"Arial,sans-serif\" font-size=\"18\" font-weight=\"700\" fill=\"#dde8f5\">HISTORICAL SCANNER: FAILED</text>\n<text x=\"628\" y=\"180\" font-family=\"Arial,sans-serif\" font-size=\"18\" font-weight=\"700\" fill=\"#dde8f5\">HISTORICAL SCANNER: INCOMPLETE</text>\n<text x=\"79\" y=\"259\" font-family=\"Arial,sans-serif\" font-size=\"49\" font-weight=\"800\" fill=\"#f2f6ff\">@@FAILED_DONE@@ / @@FAILED_TOTAL@@</text>\n<text x=\"628\" y=\"259\" font-family=\"Arial,sans-serif\" font-size=\"49\" font-weight=\"800\" fill=\"#f2f6ff\">@@INCOMPLETE_DONE@@ / @@INCOMPLETE_TOTAL@@</text>\n<rect x=\"79\" y=\"293\" width=\"470\" height=\"20\" rx=\"10\" fill=\"#334962\"/>\n<rect x=\"79\" y=\"293\" width=\"@@FAIL_FILL@@\" height=\"20\" rx=\"10\" fill=\"#46cbb6\"/>\n<rect x=\"628\" y=\"293\" width=\"470\" height=\"20\" rx=\"10\" fill=\"#334962\"/>\n<rect x=\"628\" y=\"293\" width=\"@@INCOMPLETE_FILL@@\" height=\"20\" rx=\"10\" fill=\"#46cbb6\"/>\n<text x=\"79\" y=\"345\" font-family=\"Arial,sans-serif\" font-size=\"17\" fill=\"#c0d4e4\">All failed-source cases have bounded review records</text>\n<text x=\"628\" y=\"345\" font-family=\"Arial,sans-serif\" font-size=\"17\" fill=\"#c0d4e4\">@@LEFT@@ still need targeted direct content review</text>\n<rect x=\"53\" y=\"406\" width=\"1095\" height=\"168\" rx=\"16\" fill=\"#1c3149\"/>\n<text x=\"79\" y=\"443\" font-family=\"Arial,sans-serif\" font-size=\"17\" font-weight=\"700\" fill=\"#d8e8f8\">TARGETED HISTORICALLY FLAGGED FRONTIER</text>\n<text x=\"79\" y=\"503\" font-family=\"Arial,sans-serif\" font-size=\"36\" font-weight=\"750\" fill=\"#f1f6ff\">@@ADJUDICATED@@ / @@FLAGGED_TOTAL@@</text>\n<text x=\"320\" y=\"499\" font-family=\"Arial,sans-serif\" font-size=\"16\" fill=\"#c0d4e4\">direct static security dispositions</text>\n<text x=\"79\" y=\"547\" font-family=\"Arial,sans-serif\" font-size=\"15\" fill=\"#b7cde2\">10 other Q8 items have historical scanner PASS; none newly behavior-validated.</text>\n<line x1=\"775\" y1=\"429\" x2=\"775\" y2=\"549\" stroke=\"#466079\" stroke-width=\"1\"/>\n<text x=\"802\" y=\"458\" font-family=\"Arial,sans-serif\" font-size=\"16\" fill=\"#c0d4e4\">Current unchanged-use approvals</text>\n<text x=\"802\" y=\"507\" font-family=\"Arial,sans-serif\" font-size=\"34\" font-weight=\"800\" fill=\"#f1f6ff\">0</text>\n<text x=\"853\" y=\"507\" font-family=\"Arial,sans-serif\" font-size=\"15\" fill=\"#c0d4e4\">behavioral passes: 0</text>\n<text x=\"54\" y=\"609\" font-family=\"Arial,sans-serif\" font-size=\"15\" fill=\"#a9c0d8\">Exact-source reviews are not scanner reruns, host tests, rights clearance, or permission to execute.</text>\n</svg>\n";
function verifyAndCount(history, ledgers) {
  if(!Array.isArray(history?.records)||history.records.length!==50)throw Error("Historical Q8 population missing or changed");
  const counts={passed:0,failed:0,incomplete:0},sourceById=new Map();
  for(const item of history.records) {
    if(sourceById.has(item.id)||!(item.gate_state in counts))throw Error("Duplicate or unknown original scanner record");
    counts[item.gate_state]++;sourceById.set(item.id,item);
  }
  if(counts.passed!==10||counts.failed!==7||counts.incomplete!==33)throw Error("Historical scanner denominators changed");
  const reviewed=new Set();let reviewedFailed=0,reviewedIncomplete=0;
  for(const ledger of ledgers) {
    if(!Array.isArray(ledger?.records))throw Error("Review ledger missing records");
    for(const record of ledger.records) {
      if(reviewed.has(record.id))throw Error("Duplicate reviewed package: "+record.id);
      reviewed.add(record.id);
      const original=sourceById.get(record.id),base=record.source||{};
      const blob=base.skill_md_git_blob_sha||base.skill_md_blob_sha||record.source_blob_sha||record.skill_blob_sha;
      const tree=base.complete_package_git_tree_sha||base.package_tree_sha||record.complete_package_tree_sha||record.package_tree_sha;
      const state=record.historical_scanner_state||record.historical_scanner?.state||"failed";
      const digest=record.historical_scan?.report_sha256||record.historical_scanner?.report_sha256;
      const rubric=record.static_rubric||record.rubric,score=record.static_score??record.score_total;
      if(!original||!["failed","incomplete"].includes(state)||original.gate_state!==state)throw Error("Review has wrong historical state: "+record.id);
      if(!blob||!tree||blob!==original.source.skill_md_blob_sha||tree!==original.source.package_tree_sha)throw Error("Exact Git identity mismatch: "+record.id);
      if(digest!==original.evidence?.report_sha256)throw Error("Original scanner receipt mismatch: "+record.id);
      if(!rubric||Object.keys(rubric).length!==10||!Object.values(rubric).every(x=>Number.isInteger(x)&&x>=0&&x<=2)||Object.values(rubric).reduce((x,y)=>x+y,0)!==score)throw Error("Ten-axis review rubric mismatch: "+record.id);
      if(record.unchanged_use_approved!==false)throw Error("Missing unchanged-use hold: "+record.id);
      if(state==="failed")reviewedFailed++;else reviewedIncomplete++;
    }
  }
  if(reviewedFailed>counts.failed||reviewedIncomplete>counts.incomplete)throw Error("Reviewed count exceeds population");
  return {FAILED_DONE:reviewedFailed,FAILED_TOTAL:counts.failed,INCOMPLETE_DONE:reviewedIncomplete,INCOMPLETE_TOTAL:counts.incomplete,LEFT:counts.incomplete-reviewedIncomplete,ADJUDICATED:reviewed.size,FLAGGED_TOTAL:counts.failed+counts.incomplete,FAIL_FILL:Math.round(reviewedFailed/counts.failed*470),INCOMPLETE_FILL:Math.round(reviewedIncomplete/counts.incomplete*470)};
}
function render(model) {
  let svg=TEMPLATE;
  for(const [key,value] of Object.entries(model))svg=svg.replaceAll("@@"+key+"@@",String(value));
  if(svg.includes("@@"))throw Error("Unexpanded chart placeholder");
  return svg;
}
const original=FILE(HISTORICAL),reviewed=REVIEW_LEDGERS.map(FILE);
const model=verifyAndCount(original,reviewed);
const output=render(model),destination=resolve(ROOT,"docs/assets/q8-direct-static-risk-review-progress.svg");
if(process.argv.includes("--self-test")) {
  function rejects(badHistorical,badLedgers,label) {try{verifyAndCount(badHistorical,badLedgers)}catch{return;}throw Error("Adversarial invariant accepted: "+label);}
  const mutatedHistorical=structuredClone(original);mutatedHistorical.records[0].gate_state="passed";rejects(mutatedHistorical,reviewed,"inflated scanner status");
  const duplicate=structuredClone(reviewed);duplicate[duplicate.length-1].records[0].id=reviewed[0].records[0].id;rejects(original,duplicate,"duplicated review ID");
  const forged=structuredClone(reviewed);forged.at(-1).records[0].historical_scan.report_sha256="0".repeat(64);rejects(original,forged,"forged scanner digest");
  const wrongScore=structuredClone(reviewed);wrongScore.at(-1).records[0].static_score++;rejects(original,wrongScore,"rubric score mismatch");
  const unauthorized=structuredClone(reviewed);unauthorized.at(-1).records[0].unchanged_use_approved=true;rejects(original,unauthorized,"unauthorized unchanged-use approval");
  console.log("SELF-TEST PASS",JSON.stringify(model));
}else if(process.argv.includes("--check")) {
  if(readFileSync(destination,"utf8")!==output)throw Error("README risk-review SVG is stale");
  console.log("CHECK PASS",JSON.stringify(model));
}else {writeFileSync(destination,output);console.log("GRAPHIC WRITTEN",JSON.stringify(model));}
