#!/usr/bin/env python3
"""Validate consistency and bounded paired-outcome statistics of supplied skill-trial receipts.

No external calls or authentication. A supplied 'observed' flag is an assertion, not proof.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import stat
import statistics
import sys
from pathlib import Path

MAX_BYTES = 1024 * 1024
MAX_PAIRS = 2000
KINDS = {"HOST_EXECUTED", "CONTROLLED_EMULATION"}
RESULTS = {"PASS", "FAIL", "INCOMPLETE"}
VERIFIERS = {"DETERMINISTIC", "BLIND_JUDGE", "HUMAN", "UNVERIFIED"}
LEAKAGE = {"CLEAR", "POSSIBLE", "UNREVIEWED"}

class Invalid(ValueError):
    pass


def exact(obj, required, optional=()):
    if not isinstance(obj, dict):
        raise Invalid("object expected")
    extra = set(obj) - (set(required) | set(optional))
    missing = set(required) - set(obj)
    if extra or missing:
        raise Invalid("object has missing or unexpected fields")


def text(value, name, maxlen=180):
    if not isinstance(value, str) or not (1 <= len(value) <= maxlen) or any(ord(c) < 32 for c in value):
        raise Invalid("invalid "+name)
    if any(c in value for c in ["?", "#", "@", "/", "\\"]):
        raise Invalid("unsafe "+name+"; use opaque IDs, not URLs or secrets")
    if not re.fullmatch(r"[A-Za-z0-9_.:-]+",value):
        raise Invalid("identifier contains unsupported characters: "+name)
    return value


def digest(value,name):
    if not isinstance(value,str) or not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})",value):
        raise Invalid("invalid 40/64 hexadecimal digest: "+name)
    return value


def boolval(value, name):
    if type(value) is not bool:
        raise Invalid("boolean expected for "+name)
    return value


def integer(value, name, lo, hi):
    if type(value) is not int or not lo <= value <= hi:
        raise Invalid("invalid integer "+name)
    return value


def duplicates(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise Invalid("duplicate JSON key (redacted)")
        d[k] = v
    return d


def parse(src):
    return json.loads(src, object_pairs_hook=duplicates,
                      parse_constant=lambda x: (_ for _ in ()).throw(Invalid("nonfinite constant")))


def arm(a):
    keys = {"run_id", "host_id", "model_id", "agent_version", "config_sha", "snapshot_sha", "grader_sha", "result", "verification_kind", "verifier_independent", "blind_to_arm", "observed_execution", "skill_triggered", "authority_violation", "tokens", "duration_ms", "receipt_sha"}
    exact(a, keys)
    for k in ["run_id", "host_id", "model_id", "agent_version"]:
        text(a[k],k)
    for k in ["config_sha", "snapshot_sha", "grader_sha", "receipt_sha"]:
        digest(a[k],k)
    if a["result"] not in RESULTS or a["verification_kind"] not in VERIFIERS:
        raise Invalid("unsupported result/verifier")
    for k in ["verifier_independent", "blind_to_arm", "observed_execution", "authority_violation"]:
        boolval(a[k],k)
    if a["skill_triggered"] is not None:
        boolval(a["skill_triggered"],"skill_triggered")
    if a["tokens"] is not None:
        integer(a["tokens"],"tokens",0,10**10)
    if a["duration_ms"] is not None:
        integer(a["duration_ms"],"duration_ms",0,10**10)
    return a


def exact_sign_pvalue(wins, losses):
    """Two-sided exact McNemar sign test on discordant paired outcomes."""
    n = wins + losses
    if n == 0:
        return 1.0
    k = min(wins, losses)
    # Avoid underflow for large n. Compute binomial cumulative from log probabilities.
    log2 = math.log(2)
    terms = [math.lgamma(n+1) - math.lgamma(i+1) - math.lgamma(n-i+1) - n*log2 for i in range(k+1)]
    m = max(terms)
    probability = math.exp(m) * sum(math.exp(v-m) for v in terms)
    return min(1.0, 2.0*probability)


def audit(data):
    exact(data,{"schema_version","skill","protocol","pairs"})
    if type(data["schema_version"]) is not int or data["schema_version"] != 1:
        raise Invalid("unknown schema version")
    skill=data["skill"]
    exact(skill,{"id","entrypoint_blob_sha","package_tree_sha"})
    text(skill["id"],"skill.id")
    digest(skill["entrypoint_blob_sha"],"skill.entrypoint_blob_sha")
    digest(skill["package_tree_sha"],"skill.package_tree_sha")
    protocol=data["protocol"]
    exact(protocol,{"id","run_kind","preregistered","minimum_pairs","minimum_delta_pp","holdout_isolated"})
    text(protocol["id"],"protocol.id")
    if protocol["run_kind"] not in KINDS: raise Invalid("invalid run kind")
    boolval(protocol["preregistered"],"preregistered")
    boolval(protocol["holdout_isolated"],"holdout_isolated")
    integer(protocol["minimum_pairs"],"minimum_pairs",1,MAX_PAIRS)
    integer(protocol["minimum_delta_pp"],"minimum_delta_pp",0,100)
    pairs=data["pairs"]
    if not isinstance(pairs,list) or not 1<=len(pairs)<=MAX_PAIRS:
        raise Invalid("pairs must have between 1 and 2000 entries")
    seen_pair=set();seen_run=set();seen_receipt=set();case_types=set();case_counts={}
    excluded=[];valid=[];warnings=[]
    for item in pairs:
        exact(item,{"pair_id","case_id","should_trigger","leakage_review","baseline","treatment"})
        pair_id=text(item["pair_id"],"pair_id")
        case_id=text(item["case_id"],"case_id")
        if pair_id in seen_pair: raise Invalid("duplicate pair_id")
        seen_pair.add(pair_id)
        should=boolval(item["should_trigger"],"should_trigger")
        case_types.add("POSITIVE" if should else "NONTRIGGER")
        case_counts[case_id]=case_counts.get(case_id,0)+1
        if item["leakage_review"] not in LEAKAGE: raise Invalid("invalid leakage review")
        b=arm(item["baseline"]);t=arm(item["treatment"])
        if b["run_id"]==t["run_id"] or b["run_id"] in seen_run or t["run_id"] in seen_run:
            raise Invalid("duplicate run receipt identity")
        seen_run.update((b["run_id"],t["run_id"]))
        if b["receipt_sha"]==t["receipt_sha"] or b["receipt_sha"] in seen_receipt or t["receipt_sha"] in seen_receipt:
            raise Invalid("duplicate run receipt fingerprint")
        seen_receipt.update((b["receipt_sha"],t["receipt_sha"]))
        reasons=[]
        for k in ("host_id","model_id","agent_version","config_sha","snapshot_sha","grader_sha","verification_kind"):
            if b[k]!=t[k]: reasons.append("INCOMPARABLE_"+k.upper())
        if b["skill_triggered"] is True: reasons.append("BASELINE_SKILL_TRIGGERED")
        if should and t["skill_triggered"] is not True: reasons.append("SKILL_NOT_OBSERVED_TRIGGERED")
        if not should and t["skill_triggered"] is True: reasons.append("NONTRIGGER_FIRED")
        if item["leakage_review"]!="CLEAR":reasons.append("LEAKAGE_"+item["leakage_review"])
        if any(x["authority_violation"] for x in (b,t)):reasons.append("AUTHORITY_VIOLATION")
        if any(x["result"]=="INCOMPLETE" for x in (b,t)):reasons.append("INCOMPLETE_ARM")
        if any(not x["observed_execution"] for x in (b,t)):reasons.append("EXECUTION_NOT_OBSERVED")
        if any(x["verification_kind"]=="UNVERIFIED" or not x["verifier_independent"] for x in (b,t)):
            reasons.append("NO_INDEPENDENT_VERIFIER")
        if any(x["verification_kind"] in ("BLIND_JUDGE","HUMAN") and not x["blind_to_arm"] for x in (b,t)):
            reasons.append("JUDGE_NOT_BLINDED")
        if reasons:excluded.append({"pair_id":pair_id,"reasons":sorted(set(reasons))})
        else:valid.append((item,b,t))
    if len(case_types)<2:warnings.append("POSITIVE_AND_NONTRIGGER_COVERAGE_NOT_BOTH_PRESENT")
    if protocol["run_kind"]!="HOST_EXECUTED":warnings.append("EMULATED_RUNS_ARE_NOT_HOST_VALIDATION")
    if not protocol["preregistered"]:warnings.append("NOT_PREREGISTERED")
    if not protocol["holdout_isolated"]:warnings.append("NO_ISOLATED_HOLDOUT")
    if excluded:warnings.append("EXCLUDED_PAIRS_PRESENT")
    repeated=sum(v>1 for v in case_counts.values())
    if repeated:warnings.append("REPEATED_CASES_CORRELATED_UNCERTAINTY_WITHHELD")
    positives=[(b,t) for item,b,t in valid if item["should_trigger"]]
    nontriggers=[(b,t) for item,b,t in valid if not item["should_trigger"]]
    total=len(positives)
    base_pass=sum(b["result"]=="PASS" for b,t in positives)
    treat_pass=sum(t["result"]=="PASS" for b,t in positives)
    wins=sum(b["result"]=="FAIL" and t["result"]=="PASS" for b,t in positives)
    losses=sum(b["result"]=="PASS" and t["result"]=="FAIL" for b,t in positives)
    delta_pp=(100*(treat_pass-base_pass)/total) if total else None
    p=exact_sign_pvalue(wins,losses) if total and not repeated else None
    base_rate=(base_pass/total) if total else None
    ratio=(treat_pass/base_pass) if total and base_pass else None
    nontrigger_safe=all(
        (b["result"]!="PASS" or t["result"]=="PASS")
        for b,t in nontriggers)
    if not nontrigger_safe:
        warnings.append("NONTRIGGER_TASK_REGRESSION")
    enough=(total>=protocol["minimum_pairs"] and len(nontriggers)>=1 and nontrigger_safe)
    good=(protocol["run_kind"]=="HOST_EXECUTED" and protocol["preregistered"] and protocol["holdout_isolated"] and enough and not excluded and not repeated)
    criterion=(delta_pp is not None and delta_pp>=protocol["minimum_delta_pp"] and p is not None and p<0.05)
    determination=("RECORDED_POSITIVE_SIGNAL_NOT_AUTHENTICATED" if good and criterion
                   else "NO_SIGNIFICANT_POSITIVE_SIGNAL" if good
                   else "WITHHELD_INSUFFICIENT_OR_UNQUALIFIED_EVIDENCE")
    btokens=[b["tokens"] for b,t in positives if b["tokens"] is not None]
    ttokens=[t["tokens"] for b,t in positives if t["tokens"] is not None]
    return {"schema_version":1,"skill_id":skill["id"],"protocol_id":protocol["id"],
            "source_authenticity_verified":False,"actual_independent_host_validation_verified":False,
            "total_pairs_supplied":len(pairs),"distinct_case_ids":len(case_counts),"qualified_positive_pairs":total,
            "qualified_nontrigger_pairs":len(nontriggers),"nontrigger_task_regression":not nontrigger_safe,"excluded_pairs":excluded,
            "baseline_passes":base_pass,"treatment_passes":treat_pass,
            "baseline_pass_rate":base_rate,"treatment_pass_rate":treat_pass/total if total else None,
            "paired_delta_percentage_points":delta_pp,"paired_improvements":wins,"paired_regressions":losses,
            "exact_two_sided_discordant_p":p,"relative_pass_ratio":ratio,
            "median_baseline_tokens_if_reported":statistics.median(btokens) if len(btokens)==total and total else None,
            "median_treatment_tokens_if_reported":statistics.median(ttokens) if len(ttokens)==total and total else None,
            "warnings":warnings,"determination":determination,
            "authority":"READ_ONLY_RECEIPT_CHECK_NOT_SOURCE_AUTHENTICATION"}


def main(argv=None):
    parser=argparse.ArgumentParser(description="Read-only paired skill-evaluation receipt audit")
    parser.add_argument("--input",type=Path,required=True)
    args=parser.parse_args(argv)
    try:
        if any(p.is_symlink() for p in (args.input,*args.input.parents)):
            raise Invalid("symlink input or ancestor refused")
        info = args.input.stat()
        if not stat.S_ISREG(info.st_mode):
            raise Invalid("only regular input files are accepted")
        if info.st_size > MAX_BYTES:
            raise Invalid("input exceeds 1MiB")
        with args.input.open("rb") as f:
            payload=f.read(MAX_BYTES+1)
        if len(payload)>MAX_BYTES:raise Invalid("input exceeds 1MiB")
        data=parse(payload.decode("utf-8"))
        result=audit(data)
    except (OSError,UnicodeError,Invalid,ValueError,TypeError) as ex:
        print("INVALID_INPUT: "+str(ex),file=sys.stderr)
        return 2
    print(json.dumps(result,sort_keys=True,indent=2,allow_nan=False))
    return 0

if __name__=="__main__":
    sys.exit(main())
