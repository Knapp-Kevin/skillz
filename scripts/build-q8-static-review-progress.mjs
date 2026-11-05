#!/usr/bin/env node
// Deterministic, dependency-free reviewer progress graphic. Never executes skills or scanners.
import {readFileSync,writeFileSync} from "node:fs";
import {resolve,dirname} from "node:path";
import {fileURLToPath} from "node:url";
const root=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const file=p=>JSON.parse(readFileSync(resolve(root,p),"utf8"));
const source={
  scanner:"registry/security/q12-featured-security-evidence-reconciliation-20261103.json",
  firstThree:"registry/security/third-party-three-failed-static-dispositions-20261105.json",
  lastFour:"registry/security/remaining-q8-four-failed-static-dispositions-20261105.json",
  nextThree:"registry/security/q8-three-incomplete-high-risk-static-dispositions-20261105.json"
};
function count(sourceRecords,state){return sourceRecords.filter(r=>r.gate_state===state).length}
function evaluate(historic,first,last,next){
  if(!Array.isArray(historic.records)||historic.records.length!==50||![first,last,next].every(v=>Array.isArray(v.records)))throw Error("Missing exact-source evidence");
  const q=new Map(historic.records.map(r=>[r.id,r])),merged=[...first.records,...last.records,...next.records],unique=new Set();
  if(q.size!==50||merged.length!==10||count(historic.records,"passed")!==10||count(historic.records,"failed")!==7||count(historic.records,"incomplete")!==33||first.records.length!==3||last.records.length!==4||next.records.length!==3)throw Error("Q8 denominators changed");
  for(const r of merged){
    if(unique.has(r.id))throw Error("Duplicate source review: "+r.id);
    unique.add(r.id);
    const prior=q.get(r.id),base=r.source||{};
    const blob=base.skill_md_git_blob_sha||base.skill_md_blob_sha||r.source_blob_sha||r.skill_blob_sha;
    const tree=base.complete_package_git_tree_sha||base.package_tree_sha||r.complete_package_tree_sha||r.package_tree_sha;
    const state=r.historical_scanner_state||r.historical_scanner?.state||"failed";
    if(!prior||prior.gate_state!==state||prior.source.skill_md_blob_sha!==blob||prior.source.package_tree_sha!==tree||r.unchanged_use_approved!==false)throw Error("Source identity/status or action approval mismatch: "+r.id);
  }
  return {FAILED_DONE:first.records.length+last.records.length,FAILED_TOTAL:7,INCOMPLETE_DONE:next.records.length,INCOMPLETE_TOTAL:33,LEFT:33-next.records.length,ADJUDICATED:merged.length,FLAGGED_TOTAL:40,FAIL_FILL:470,INCOMPLETE_FILL:Math.round(next.records.length/33*470)};
}
const TEMPLATE="<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1200\" height=\"650\" viewBox=\"0 0 1200 650\" role=\"img\" aria-labelledby=\"title desc\">\n<title id=\"title\">Skillz Q8 risk-review progress, November 5 2026</title>\n<desc id=\"desc\">Direct exact-version static content review progress: @@FAILED_DONE@@ of @@FAILED_TOTAL@@ historically failed packages and @@INCOMPLETE_DONE@@ of @@INCOMPLETE_TOTAL@@ historically incomplete packages reviewed. @@LEFT@@ incomplete packages remain. Historical scanner states unchanged. No observed behavioral acceptance or unchanged-use approvals.</desc>\n<rect width=\"1200\" height=\"650\" fill=\"#0b162a\"/>\n<rect x=\"22\" y=\"20\" width=\"1156\" height=\"610\" rx=\"23\" fill=\"#14263d\" stroke=\"#2a4462\"/>\n<text x=\"54\" y=\"65\" font-family=\"Arial,sans-serif\" font-size=\"26\" font-weight=\"700\" fill=\"#f2f6ff\">SKILLZ / DIRECT STATIC RISK REVIEWS</text>\n<text x=\"1148\" y=\"65\" font-family=\"Arial,sans-serif\" text-anchor=\"end\" font-size=\"14\" font-weight=\"700\" fill=\"#a6bdd5\">NOV 05, 2026</text>\n<text x=\"54\" y=\"96\" font-family=\"Arial,sans-serif\" font-size=\"17\" fill=\"#c9d7e8\">Pinned Q8 source packages, read as data. Scanner outcomes and permissions stay separate.</text>\n<rect x=\"53\" y=\"135\" width=\"526\" height=\"245\" rx=\"16\" fill=\"#213651\"/>\n<rect x=\"602\" y=\"135\" width=\"546\" height=\"245\" rx=\"16\" fill=\"#213651\"/>\n<text x=\"79\" y=\"180\" font-family=\"Arial,sans-serif\" font-size=\"18\" font-weight=\"700\" fill=\"#dde8f5\">HISTORICAL SCANNER: FAILED</text>\n<text x=\"628\" y=\"180\" font-family=\"Arial,sans-serif\" font-size=\"18\" font-weight=\"700\" fill=\"#dde8f5\">HISTORICAL SCANNER: INCOMPLETE</text>\n<text x=\"79\" y=\"259\" font-family=\"Arial,sans-serif\" font-size=\"49\" font-weight=\"800\" fill=\"#f2f6ff\">@@FAILED_DONE@@ / @@FAILED_TOTAL@@</text>\n<text x=\"628\" y=\"259\" font-family=\"Arial,sans-serif\" font-size=\"49\" font-weight=\"800\" fill=\"#f2f6ff\">@@INCOMPLETE_DONE@@ / @@INCOMPLETE_TOTAL@@</text>\n<rect x=\"79\" y=\"293\" width=\"470\" height=\"20\" rx=\"10\" fill=\"#334962\"/>\n<rect x=\"79\" y=\"293\" width=\"@@FAIL_FILL@@\" height=\"20\" rx=\"10\" fill=\"#46cbb6\"/>\n<rect x=\"628\" y=\"293\" width=\"470\" height=\"20\" rx=\"10\" fill=\"#334962\"/>\n<rect x=\"628\" y=\"293\" width=\"@@INCOMPLETE_FILL@@\" height=\"20\" rx=\"10\" fill=\"#46cbb6\"/>\n<text x=\"79\" y=\"345\" font-family=\"Arial,sans-serif\" font-size=\"17\" fill=\"#c0d4e4\">All failed-source cases have bounded review records</text>\n<text x=\"628\" y=\"345\" font-family=\"Arial,sans-serif\" font-size=\"17\" fill=\"#c0d4e4\">@@LEFT@@ still need targeted direct content review</text>\n<rect x=\"53\" y=\"406\" width=\"1095\" height=\"168\" rx=\"16\" fill=\"#1c3149\"/>\n<text x=\"79\" y=\"443\" font-family=\"Arial,sans-serif\" font-size=\"17\" font-weight=\"700\" fill=\"#d8e8f8\">TARGETED HISTORICALLY FLAGGED FRONTIER</text>\n<text x=\"79\" y=\"503\" font-family=\"Arial,sans-serif\" font-size=\"36\" font-weight=\"750\" fill=\"#f1f6ff\">@@ADJUDICATED@@ / @@FLAGGED_TOTAL@@</text>\n<text x=\"320\" y=\"499\" font-family=\"Arial,sans-serif\" font-size=\"16\" fill=\"#c0d4e4\">direct static security dispositions</text>\n<text x=\"79\" y=\"547\" font-family=\"Arial,sans-serif\" font-size=\"15\" fill=\"#b7cde2\">10 other Q8 items have historical scanner PASS; none newly behavior-validated.</text>\n<line x1=\"775\" y1=\"429\" x2=\"775\" y2=\"549\" stroke=\"#466079\" stroke-width=\"1\"/>\n<text x=\"802\" y=\"458\" font-family=\"Arial,sans-serif\" font-size=\"16\" fill=\"#c0d4e4\">Current unchanged-use approvals</text>\n<text x=\"802\" y=\"507\" font-family=\"Arial,sans-serif\" font-size=\"34\" font-weight=\"800\" fill=\"#f1f6ff\">0</text>\n<text x=\"853\" y=\"507\" font-family=\"Arial,sans-serif\" font-size=\"15\" fill=\"#c0d4e4\">behavioral passes: 0</text>\n<text x=\"54\" y=\"609\" font-family=\"Arial,sans-serif\" font-size=\"15\" fill=\"#a9c0d8\">Exact-source reviews are not scanner reruns, host tests, rights clearance, or permission to execute.</text>\n</svg>\n";
function render(data){let result=TEMPLATE;for(const [key,value] of Object.entries(data))result=result.replaceAll("@@"+key+"@@",String(value));if(result.includes("@@"))throw Error("Unexpanded SVG token");return result}
const a=file(source.scanner),b=file(source.firstThree),c=file(source.lastFour),d=file(source.nextThree);
const m=evaluate(a,b,c,d),expected=render(m),dest=resolve(root,"docs/assets/q8-direct-static-risk-review-progress.svg");
if(process.argv.includes("--self-test")){
  const corrupt=structuredClone(a);corrupt.records[0].gate_state="passed";let rejected=false;try{evaluate(corrupt,b,c,d)}catch{rejected=true};if(!rejected)throw Error("Inflated scanner count accepted");
  const duplicated=structuredClone(d);duplicated.records[0].id=b.records[0].id;rejected=false;try{evaluate(a,b,c,duplicated)}catch{rejected=true};if(!rejected)throw Error("Duplicate review accepted");
  console.log("self-test passed: scanner count, IDs, exact trees and no approvals");
}else if(process.argv.includes("--check")){
  if(readFileSync(dest,"utf8")!==expected)throw Error("Generated review graphic differs from source evidence");
  console.log("check passed");
}else{writeFileSync(dest,expected);console.log("wrote Q8 static content review progress graphic")}
