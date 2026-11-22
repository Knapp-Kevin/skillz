#!/usr/bin/env python3
"""Compare ONLY independently observed, comparable GitHub CI execution receipts.

Input JSON must come from actual job API/run observations for the SAME source
revision under baseline and optimized workflows. This utility validates input
structure, not provenance; it cannot itself authenticate GitHub receipts.
Python 3.9+ standard library, no network, no writes, no execution.
"""
import argparse
from datetime import datetime
import json
import math
from pathlib import Path
import statistics
import sys


class EvidenceError(ValueError):
    pass


def parse_time(value):
    if not isinstance(value, str):
        raise EvidenceError("timestamps must be UTC strings")
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise EvidenceError('invalid timestamp') from exc
    if dt.utcoffset() is None:
        raise EvidenceError('timestamp timezone unavailable')
    return dt


def summarize_run(data, allow_missing_billing=False):
    if not isinstance(data, dict) or set(data) != {
            'run_id', 'attempt', 'head', 'scenario', 'runner_profile',
            'cache_class', 'protected_status', 'jobs'}:
        raise EvidenceError('run must include source/runner/observed job evidence')
    if (not isinstance(data['run_id'], str) or not data['run_id']
            or not isinstance(data['head'], str) or len(data['head']) not in (40, 64)
            or not isinstance(data['jobs'], list) or not data['jobs']
            or data['protected_status'] != 'success'):
        raise EvidenceError('unqualified or incomplete run')
    total = 0.0
    billing_known = True
    executed_seconds = 0.0
    earliest, latest = None, None
    durations, graph = {}, {}
    for job in data['jobs']:
        if not isinstance(job, dict) or set(job) != {
                'name', 'needs', 'started_at', 'completed_at', 'billed_runner_minutes', 'result'}:
            raise EvidenceError('incomplete job observation')
        if (not isinstance(job['name'], str) or not job['name']
                or job['name'] in durations or not isinstance(job['needs'], list)
                or len(set(job['needs'])) != len(job['needs'])
                or any(not isinstance(x, str) for x in job['needs'])):
            raise EvidenceError('missing or repeated job/dependency identity')
        if job['result'] != 'success':
            raise EvidenceError('failed or skipped required job in success record')
        minutes = job['billed_runner_minutes']
        if minutes is None and allow_missing_billing:
            billing_known = False
        elif (type(minutes) not in (int, float) or
              not math.isfinite(minutes) or minutes < 0):
            raise EvidenceError('unobserved billed minutes')
        start, end = parse_time(job['started_at']), parse_time(job['completed_at'])
        if end < start:
            raise EvidenceError('negative job duration')
        earliest = min(earliest, start) if earliest else start
        latest = max(latest, end) if latest else end
        if minutes is not None:
            total += minutes
        durations[job['name']] = (end-start).total_seconds()
        executed_seconds += durations[job['name']]
        graph[job['name']] = job['needs']
    # The provided dependency graph must cover every required job.
    # This computes the longest executed job-duration chain, not the wall
    # envelope, which separately contains runner queue/scheduling gaps.
    visiting, longest = set(), {}
    def path_length(name):
        if name in visiting:
            raise EvidenceError('cyclic required job dependency graph')
        if name in longest:
            return longest[name]
        if name not in graph:
            raise EvidenceError('incomplete multi-workflow dependency evidence')
        visiting.add(name)
        length = durations[name] + max([path_length(dep) for dep in graph[name]] or [0.0])
        visiting.remove(name)
        longest[name] = length
        return length
    critical = max(path_length(name) for name in graph)
    return {'billed_runner_minutes': round(total, 4) if billing_known else None,
            'executed_job_minutes': round(executed_seconds / 60, 4),
            'critical_path_seconds': round(critical, 3),
            'qualification_elapsed_seconds': round((latest-earliest).total_seconds(), 3)}


def compare(data):
    if not isinstance(data, dict) or set(data) != {'schema_version', 'pairs'}:
        raise EvidenceError('unexpected comparison schema')
    if data['schema_version'] != 1 or not isinstance(data['pairs'], list) or not data['pairs']:
        raise EvidenceError('no observed comparison pairs')
    pairs = []
    for item in data['pairs']:
        if not isinstance(item, dict) or set(item) != {'baseline', 'optimized'}:
            raise EvidenceError('missing paired baseline or optimized receipt')
        b, o = item['baseline'], item['optimized']
        for name in ('head', 'scenario', 'runner_profile', 'cache_class'):
            if b.get(name) != o.get(name):
                raise EvidenceError('noncomparable ' + name)
        if (b.get('run_id') == o.get('run_id') and b.get('attempt') == o.get('attempt')):
            raise EvidenceError('comparison must use distinct actual run receipts')
        old, new = summarize_run(b), summarize_run(o)
        pairs.append({'scenario': b['scenario'], 'head': b['head'],
                      'baseline':old, 'optimized':new,
                      'saved_runner_minutes': round(old['billed_runner_minutes']-new['billed_runner_minutes'],4),
                      'saved_critical_seconds': round(old['critical_path_seconds']-new['critical_path_seconds'],3),
                      'saved_elapsed_seconds': round(old['qualification_elapsed_seconds']-new['qualification_elapsed_seconds'],3)})
    return {'pairs': pairs, 'count': len(pairs),
            'sum_runner_minutes_saved': round(sum(x['saved_runner_minutes'] for x in pairs),4),
            'median_critical_seconds_saved': statistics.median(x['saved_critical_seconds'] for x in pairs),
            'median_elapsed_seconds_saved': statistics.median(x['saved_elapsed_seconds'] for x in pairs),
            'provenance': 'OBSERVED_AS_SUPPLIED_NOT_EXTERNALLY_AUTHENTICATED'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--observations', required=True)
    args=ap.parse_args()
    data=json.loads(Path(args.observations).read_text(encoding='utf-8'))
    print(json.dumps(compare(data),sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (EvidenceError, OSError, ValueError) as exc:
        print('CI_METRICS_UNVERIFIED: ' + str(exc),file=sys.stderr)
        sys.exit(2)
