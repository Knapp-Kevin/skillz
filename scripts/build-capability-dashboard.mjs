#!/usr/bin/env node
// Generated dashboard: no external packages, no network, no source repository writes.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
function html(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&apos;")}

function md(s){return String(s).replace(/\|/g,"\\|").replace(/\r?\n/g," ").trim()}

function dashboardData(audit,catalog,manifest){
 if(!audit||!Array.isArray(audit.domains)||!catalog||!Array.isArray(catalog.valuable_references))throw Error("Source ledgers missing required arrays");
 const approved=catalog.recommended_for_use_in_this_shelf||[];
 if(!Array.isArray(approved))throw Error("Approved list is not an array");
 const ref=catalog.valuable_references,domainIDs=new Set(audit.domains.map(d=>d.id)),all=[...ref,...approved],names=new Set();
 for(const d of audit.domains){
   if(names.has(d.id)||!Array.isArray(d.subdomains)||!d.id||!d.name)throw Error(`Invalid or duplicate domain: ${d.id}`);
   names.add(d.id);const subs=new Set(d.subdomains.map(s=>s.id));if(subs.size!==d.subdomains.length)throw Error(`Duplicate subdomain: ${d.id}`);
 }
 const refs=new Set();
 for(const x of all){
   if(!domainIDs.has(x.domain))throw Error(`Selected method outside canonical domain: ${x.name}/${x.domain}`);
   const d=audit.domains.find(d=>d.id===x.domain);
   if(!d.subdomains.some(s=>s.id===x.subdomain))throw Error(`Selected method outside canonical subdomain: ${x.name}/${x.subdomain}`);
   const key=x.id||`${x.source?.repository}/${x.source?.path}`||x.name;
   if(refs.has(key))throw Error(`Duplicate selected method: ${key}`);
   refs.add(key);
 }
 if(catalog.starter_shelf_totals?.valuable_reference!==ref.length)throw Error("Catalog's Valuable Reference count disagrees with its records");
 if(catalog.starter_shelf_totals?.recommended_for_use!==approved.length)throw Error("Catalog's Recommended-for-use count disagrees with its records");
 const rows=audit.domains.map(d=>{
   const matches=ref.filter(x=>x.domain===d.id),grants=approved.filter(x=>x.domain===d.id);
   const topics=[...new Set([...matches,...grants].map(x=>x.subdomain))];
   return {id:d.id,name:d.name,research_topics:d.subdomains.filter(s=>s.has_any_review_or_candidate_link===true).length,total_topics:d.subdomains.length,reference_methods:matches.length,approved_methods:grants.length,selected_topics:topics.length};
 });
 const totals={domains:rows.length,topics:rows.reduce((a,x)=>a+x.total_topics,0),linked_topics:rows.reduce((a,x)=>a+x.research_topics,0),reference_methods:ref.length,approved_methods:approved.length,selected_topics:rows.reduce((a,x)=>a+x.selected_topics,0),selected_domains:rows.filter(x=>x.selected_topics>0).length};
 if(audit.summary && (audit.summary.canonical_domains!==totals.domains||audit.summary.canonical_subdomains!==totals.topics||audit.summary.subdomains_with_any_review_or_candidate_link!==totals.linked_topics))throw Error("Historical research summary disagrees with domain rows");
 if(catalog.starter_shelf_totals?.distinct_capability_domains_represented!==new Set(ref.map(x=>x.domain)).size)throw Error("Consumer shelf domain count disagrees with selected records");
 return {rows,totals,as_of:manifest.as_of,research_source:manifest.historical_research_audit,featured_source:manifest.current_featured_shelf,research_date:audit.as_of||"2026-11-02"};
}

function dashboardCsv(model){
 const lines=[["Domain ID","Capability domain","Research-linked topics","Total topics","Research link coverage %","Valuable Reference methods","Approved-as-written methods","Subdomains with selected methods"]];
 for(const r of model.rows)lines.push([r.id,r.name,r.research_topics,r.total_topics,r.total_topics?Math.round(r.research_topics/r.total_topics*100):0,r.reference_methods,r.approved_methods,r.selected_topics]);
 return lines.map(cells=>cells.map(x=>`"${String(x).replace(/"/g,'""')}"`).join(",")).join("\n")+"\n";
}

function dashboardSvg(model){
 const W=1120,H=1000,parts=[],T=model.totals,startY=369,rh=33;
 const metrics=[{v:String(T.domains),label:"CAPABILITY AREAS"},{v:`${T.linked_topics} / ${T.topics}`,label:"TOPICS WITH RESEARCH LINKS"},{v:String(T.reference_methods),label:"METHODS SELECTED TO STUDY"},{v:String(T.approved_methods),label:"APPROVED UNCHANGED"}];
 parts.push(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-labelledby="chart-heading chart-detail">`);
 parts.push(`<title id="chart-heading">Skillz capability evidence dashboard for ${T.domains} domains</title><desc id="chart-detail">${T.linked_topics} of ${T.topics} canonical topics have research or candidate links, including some rejected-only sources. ${T.reference_methods} distinct methods are featured for study across ${T.selected_domains} domains; ${T.approved_methods} approved unchanged. The README contains the full accessible table and downloadable CSV.</desc>`);
 parts.push(`<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#0d1a2f"/><stop offset="1" stop-color="#172b49"/></linearGradient><linearGradient id="cyan" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#38bdf8"/><stop offset="1" stop-color="#5eead4"/></linearGradient></defs>`);
 parts.push(`<rect x="0" y="0" width="${W}" height="${H}" rx="24" fill="url(#bg)"/><circle cx="998" cy="70" r="235" fill="#3e6094" opacity=".11"/>`);
 parts.push(`<text x="35" y="63" font-size="34" font-weight="700" fill="#f3f7ff" font-family="Arial,Helvetica,sans-serif">Skillz | Capability overview</text><text x="36" y="101" font-size="18" fill="#c1d1e7" font-family="Arial,Helvetica,sans-serif">Find useful methods across the library. A featured shelf is not the entire catalog.</text>`);
 metrics.forEach(({v,label},i)=>{const x=34+i*270;parts.push(`<rect x="${x}" y="136" width="242" height="96" rx="13" stroke="#3b5371" fill="#1c314c"/><text x="${x+18}" y="179" fill="#f0f6ff" font-size="29" font-weight="700" font-family="Arial,Helvetica,sans-serif">${html(v)}</text><text x="${x+18}" y="208" fill="#bfd0e4" font-size="12.5" font-family="Arial,Helvetica,sans-serif">${html(label)}</text>`)});
 parts.push(`<rect x="37" y="259" width="14" height="14" rx="3" fill="#4fd5dd"/><text x="61" y="272" fill="#dfebf9" font-size="15" font-family="Arial,Helvetica,sans-serif">Topics with any research link (even rejected)</text><rect x="538" y="259" width="14" height="14" rx="3" fill="#af90f3"/><text x="562" y="272" fill="#dfebf9" font-size="15" font-family="Arial,Helvetica,sans-serif">Methods selected to study, not approved to install</text>`);
 parts.push(`<text x="36" y="309" fill="#afc5dd" font-size="15" font-family="Arial,Helvetica,sans-serif">“Not featured” means keep searching the wider evidence index.</text>`);
 for(let col=0;col<2;col++){
  const x=31+col*539,subset=model.rows.slice(col*17,(col+1)*17);
  parts.push(`<rect x="${x}" y="331" width="520" height="601" rx="14" stroke="#344c67" fill="#111f34"/>`);
  parts.push(`<text x="${x+13}" y="357" font-size="14" font-weight="700" fill="#e9f2fe" font-family="Arial,Helvetica,sans-serif">Capability domain</text><text x="${x+216}" y="357" font-size="14" fill="#c6e8f4" font-family="Arial,Helvetica,sans-serif">Links</text><text x="${x+390}" y="357" font-size="14" fill="#d8c7fa" font-family="Arial,Helvetica,sans-serif">Selected</text>`);
  subset.forEach((row,i)=>{
   const y=startY+i*rh,pct=row.total_topics?row.research_topics/row.total_topics:0,chosen=row.reference_methods+row.approved_methods>0;
   parts.push(`<g><title>${html(row.name)}: ${row.research_topics}/${row.total_topics} research-linked topics; ${row.reference_methods} study methods across ${row.selected_topics} topics; ${row.approved_methods} unchanged-use approvals</title>`);
   parts.push(`<rect x="${x+7}" y="${y-18}" width="505" height="31" rx="6" fill="${i%2===0?"#1e314b":"#172842"}"/>`);
   parts.push(`<text x="${x+12}" y="${y+3}" font-size="14" fill="#e7f1fc" font-family="Arial,Helvetica,sans-serif">${html(row.name.length>26?row.name.slice(0,24)+"…":row.name)}</text>`);
   parts.push(`<rect x="${x+216}" y="${y-9}" width="86" height="12" rx="4" fill="#3d506c"/>`);
   if(pct>0)parts.push(`<rect x="${x+216}" y="${y-9}" width="${(pct*86).toFixed(2)}" height="12" rx="4" fill="url(#cyan)"/>`);
   parts.push(`<text x="${x+309}" y="${y+3}" font-size="13.5" fill="#e0eaf8" font-family="Arial,Helvetica,sans-serif">${row.research_topics}/${row.total_topics}</text>`);
   parts.push(`<rect x="${x+381}" y="${y-16}" width="129" height="26" rx="8" stroke="${chosen?"#816bc0":"#3d526c"}" fill="${chosen?"#433467":"#1a2c44"}"/>`);
   parts.push(`<text x="${x+446}" y="${y+2}" text-anchor="middle" font-size="12.5" font-weight="${chosen?"700":"400"}" fill="${chosen?"#f2eaff":"#a7bdd5"}" font-family="Arial,Helvetica,sans-serif">${html(chosen?`${row.reference_methods} refs · ${row.selected_topics} topics`:"not featured")}</text></g>`);
  });
 }
 parts.push(`<text x="38" y="967" fill="#d4e1f1" font-size="15" font-family="Arial,Helvetica,sans-serif">Research breadth ≠ skill quality. Selection ≠ installation clearance. All 33 rows also appear in the README and CSV.</text></svg>`);
 return parts.join("\n")+"\n";
}

function dashboardMarkdown(model){
 const T=model.totals;
 const csv="docs/data/capability-dashboard.csv",svg="docs/assets/capability-dashboard.svg";
 const rows=model.rows.map(r=>`| ${md(r.name)} | ${r.research_topics} / ${r.total_topics} | ${r.reference_methods||"Not featured"} | ${r.selected_topics} / ${r.total_topics} |`).join("\n");
 return [
 "<!-- SKILLZ_CAPABILITY_DASHBOARD:START | generated: scripts/build-capability-dashboard.mjs -->",
 "### Capability dashboard",
 "",
 `**${T.domains} capability areas** · **${T.topics} topics** · **${T.linked_topics} topics with research leads** · **${T.reference_methods} useful methods selected for study** · **${T.approved_methods} approved unchanged**`,
 "",
 `![Generated Skillz capability evidence dashboard, with research-linked topic bars and separately selected study methods across ${T.domains} domains.](${svg})`,
 "",
 `**How to read this:** Turquoise means a topic has a research or candidate link, which can include rejected skills. Purple means at least one method has been selected to study in our *bounded* featured shelf. Neither is installation clearance, and an unfeatured domain can still contain useful candidates.`,
 "",
 `<details><summary>Explore all ${T.domains} capability areas in a spreadsheet-style table</summary>`,
 "",
 "| Capability area | Research-linked topics | Featured study methods | Topics with featured methods |",
 "|---|---:|---:|---:|",
 rows,
 "",
 "</details>",
 "",
 `**[View the full CSV table](${csv})** · [Research source ledger](${model.research_source}) · [Featured reference ledger](${model.featured_source}) · [How the dashboard updates](docs/capability-dashboard-maintenance.md)`,
 "",
 `*As of ${model.as_of}. The research links are from a historical audit; not every candidate is useful. All-corpus qualification totals remain unknown. Never add topic-link counts to selected-method counts.*`,
 "<!-- SKILLZ_CAPABILITY_DASHBOARD:END -->"
 ].join("\n")+"\n";
}

function updateReadme(readme,newBlock){
 const open="<!-- SKILLZ_CAPABILITY_DASHBOARD:START",close="<!-- SKILLZ_CAPABILITY_DASHBOARD:END -->";
 const a=readme.indexOf(open);
 if(a>=0){const b=readme.indexOf(close,a);if(b<0)throw Error("Missing dashboard END marker");return readme.slice(0,a)+newBlock.trimEnd()+readme.slice(b+close.length);}
 const a0=readme.indexOf("### Two different views: research leads and the small featured shelf");
 const b0=readme.indexOf("## Our featured methods:",a0);
 if(a0<0||b0<0||b0<=a0)throw Error("Cannot identify existing dashboard section; refusing to overwrite README");
 return readme.slice(0,a0)+newBlock+"\n"+readme.slice(b0);
}

function selfTest(){
 const fixture={domains:[{id:"fiction",name:"Research & <Study>",subdomains:[{id:"one",has_any_review_or_candidate_link:true},{id:"two",has_any_review_or_candidate_link:false}]}],summary:{canonical_domains:1,canonical_subdomains:2,subdomains_with_any_review_or_candidate_link:1}};
 const catalog={valuable_references:[{id:"a",name:"Method",domain:"fiction",subdomain:"one"}],recommended_for_use_in_this_shelf:[],starter_shelf_totals:{valuable_reference:1,recommended_for_use:0,distinct_capability_domains_represented:1}};
 const manifest={as_of:"2026-11-03",historical_research_audit:"audit.json",current_featured_shelf:"catalog.json"};
 const model=dashboardData(fixture,catalog,manifest);
 if(model.totals.topics!==2||model.totals.linked_topics!==1||model.totals.reference_methods!==1)throw Error("Self-test totals failed");
 if(!dashboardSvg(model).includes("Research &amp; &lt;Study&gt;"))throw Error("SVG escaping failed");
 if(!dashboardCsv(model).includes('"Research & <Study>"'))throw Error("CSV quoting failed");
 const body=dashboardMarkdown(model),intro="Above\n### Two different views: research leads and the small featured shelf\nOLD\n## Our featured methods:\nAfter";
 const once=updateReadme(intro,body),twice=updateReadme(once,body);
 if(once!==twice||!once.includes("## Our featured methods:")||once.includes("\nOLD\n"))throw Error("README idempotence failed");
 try{dashboardData(fixture,{...catalog,valuable_references:[{id:"a",domain:"wrong",subdomain:"one"}]},manifest);throw Error("Expected invalid mapping error")}catch(e){if(e.message==="Expected invalid mapping error")throw e;}
 return true;
}
const ROOT=resolve(dirname(fileURLToPath(import.meta.url)),"..");
const read=(p)=>readFileSync(resolve(ROOT,p),"utf8");
const manifest=JSON.parse(read("registry/capability-dashboard-sources.json"));
const model=dashboardData(JSON.parse(read(manifest.historical_research_audit)),JSON.parse(read(manifest.current_featured_shelf)),manifest);
const paths={
 "README.md":updateReadme(read("README.md"),dashboardMarkdown(model)),
 "docs/data/capability-dashboard.csv":dashboardCsv(model),
 "docs/assets/capability-dashboard.svg":dashboardSvg(model)
};
if(process.argv.includes("--self-test")){selfTest();console.log("dashboard self-test passed");process.exit(0)}
if(process.argv.includes("--check")){
 let dirty=0;
 for(const [p,content] of Object.entries(paths)){if(!existsSync(resolve(ROOT,p))||read(p)!==content){console.error("STALE dashboard output: "+p);dirty++;}}
 if(dirty)process.exit(1);console.log("Capability dashboard is current: "+model.totals.domains+" domains, "+model.totals.reference_methods+" reference methods");process.exit(0);
}
for(const [p,content] of Object.entries(paths)){mkdirSync(dirname(resolve(ROOT,p)),{recursive:true});writeFileSync(resolve(ROOT,p),content,"utf8");console.log("Updated "+p)}
console.log("Dashboard generated from "+manifest.historical_research_audit+" and "+manifest.current_featured_shelf);
