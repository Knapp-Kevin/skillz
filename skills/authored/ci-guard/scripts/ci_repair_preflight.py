#!/usr/bin/env python3
"""Read-only, bounded one-pass CI repair preflight and test-internal cost analysis.

Input is a caller-authored, source-traced JSON manifest. It DOES NOT discover
workflows, authenticate CI runs, execute commands, alter branch rules, or
provide proof of savings. Review the real execution graph separately with
CI Guard's canonical ci_overlap.py. Python >=3.9 standard library only.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import statistics
import sys

MAX_BYTES = 1024 * 1024
MAX_RECORDS = 3000
STAGES = ('DISCOVER', 'PREPARE', 'PROVE', 'CUTOVER', 'OBSERVE', 'ROLLBACK')
CLASSES = {'REPEATED_IMMUTABLE_SETUP', 'JUSTIFIED_ISOLATION',
           'UNIQUE_DETECTION', 'REDUNDANT_SAME_REVISION', 'UNPROVEN', 'DEPENDENCY_WAIT'}


class InvalidManifest(ValueError):
    pass


def require(value, description):
    if not isinstance(value, dict):
        raise InvalidManifest(description + ' must be an object')
    return value


def text(value, description):
    if not isinstance(value, str) or not value.strip() or len(value) > 512:
        raise InvalidManifest(description + ' must be a bounded nonempty string')
    return value


def number(value, description):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not 0 <= value <= 10**7:
        raise InvalidManifest(description + ' must be a finite nonnegative number')
    return value


def unique_strings(value, description):
    if not isinstance(value, list) or len(value) > MAX_RECORDS:
        raise InvalidManifest(description + ' must be a bounded array')
    for entry in value:
        text(entry, description)
    if len(set(value)) != len(value):
        raise InvalidManifest(description + ' contains duplicates')
    return set(value)


def percentile(values, pct):
    ordered = sorted(values)
    if not ordered:
        return None
    index = int((len(ordered) - 1) * pct + 0.5)
    return ordered[index]


def inspect_phases(phases, source):
    if not isinstance(phases, list) or not phases or len(phases) > MAX_RECORDS:
        raise InvalidManifest('phase_observations must be a bounded nonempty list')
    groups = defaultdict(list)
    by_kind = defaultdict(list)
    critical_by_kind = defaultdict(list)
    identifiers = set()
    for p in phases:
        require(p, 'phase')
        ident = text(p.get('id'), 'phase.id')
        if ident in identifiers:
            raise InvalidManifest('duplicate phase ID')
        identifiers.add(ident)
        for field in ('kind', 'operation', 'fingerprint', 'platform',
                      'environment', 'run_id', 'trust_boundary', 'assertion'):
            text(p.get(field), 'phase.' + field)
        if not isinstance(p.get('immutable'), bool) or not isinstance(p.get('mutates'), bool):
            raise InvalidManifest('phase immutable/mutates must be boolean')
        if p.get('isolation') not in ('none', 'fresh-directory', 'process', 'platform', 'trust'):
            raise InvalidManifest('phase.isolation unknown')
        if not isinstance(p.get('equivalence_proven'), bool):
            raise InvalidManifest('phase.equivalence_proven must be boolean')
        if not isinstance(p.get('unique_detection'), bool):
            raise InvalidManifest('phase.unique_detection must be boolean')
        number(p.get('seconds'), 'phase.seconds')
        if not isinstance(p.get('on_critical_path'), bool):
            raise InvalidManifest('phase.on_critical_path must be boolean')
        if p.get('revision') != source:
            raise InvalidManifest('phase source revision mismatch')
        key = (p['kind'], p['operation'], p['fingerprint'])
        groups[key].append(p)
        by_kind[p['kind']].append(p['seconds'])
        if p['on_critical_path']:
            critical_by_kind[p['kind']].append(p['seconds'])
    findings = []
    for key, operations in sorted(groups.items()):
        if len(operations) < 2:
            continue
        ids = [row['id'] for row in operations]
        if key[0] == 'dependency_wait':
            classification = 'DEPENDENCY_WAIT'
        elif any(row['mutates'] or row['isolation'] != 'none' for row in operations):
            classification = 'JUSTIFIED_ISOLATION'
        elif any(row['unique_detection'] for row in operations) or len({r['assertion'] for r in operations}) != 1:
            classification = 'UNIQUE_DETECTION'
        elif len({(r['platform'], r['trust_boundary']) for r in operations}) != 1:
            classification = 'UNPROVEN'
        elif all(row['immutable'] and not row['mutates'] for row in operations):
            classification = 'REPEATED_IMMUTABLE_SETUP'
        elif all(row['equivalence_proven'] for row in operations):
            classification = 'REDUNDANT_SAME_REVISION'
        else:
            classification = 'UNPROVEN'
        assert classification in CLASSES
        findings.append({'operation': key[1], 'fingerprint': key[2],
                         'phase_ids': ids, 'classification': classification,
                         'total_seconds': round(sum(row['seconds'] for row in operations), 3),
                         'removal_authorized': False})
    stats = {}
    for kind, values in sorted(by_kind.items()):
        stats[kind] = {'samples': len(values), 'total_seconds': round(sum(values), 3),
                       'reported_critical_path_seconds': round(sum(critical_by_kind[kind]), 3),
                       'p50_seconds': percentile(values, 0.50),
                       'p90_seconds': percentile(values, 0.90)}
    leader = max(stats, key=lambda x: stats[x]['total_seconds'])
    critical_leader = max(stats, key=lambda x: stats[x]['reported_critical_path_seconds'])
    return {'total_seconds': round(sum(sum(v) for v in by_kind.values()), 3),
            'dominant_phase': leader, 'dominant_reported_critical_phase': critical_leader,
            'phase_timings': stats,
            'overlap_findings': findings,
            'observed_by_provider': False}



def inspect_artifact_waits(document, phases, source):
    """Validate claimed artifact-poll evidence and a proposed safe job DAG.

    All records are caller-supplied. PASS only means the *declared* DAG
    satisfies the safety constraints, NOT that a provider deployed it.
    """
    waits = [x for x in phases if x.get('kind') == 'dependency_wait']
    schedules = document.get('artifact_schedules', [])
    if not isinstance(schedules, list) or len(schedules) > 100:
        raise InvalidManifest('artifact_schedules must be a bounded list')
    issues = []
    if waits and not schedules:
        issues.append('ARTIFACT_SCHEDULE_MISSING')
    matched = set()
    diagnostics = []
    schedule_keys = set()
    total_wait = 0
    for wait in waits:
        for field in ('artifact_id', 'producer_job', 'consumer_job'):
            text(wait.get(field), 'wait.' + field)
        requested = number(wait.get('requested_at_s'), 'wait.requested_at_s')
        available = number(wait.get('available_at_s'), 'wait.available_at_s')
        completed = number(wait.get('consumer_finished_at_s'), 'wait.consumer_finished_at_s')
        if not (requested < available <= completed):
            issues.append('ARTIFACT_TIMELINE_INVALID:' + wait['id'])
        if abs((available - requested) - wait['seconds']) > 0.001:
            issues.append('WAIT_DURATION_INCONSISTENT:' + wait['id'])
        total_wait += wait['seconds']
        diagnostics.append({'phase_id': wait['id'], 'consumer_job': wait['consumer_job'],
                            'producer_job': wait['producer_job'], 'artifact_id': wait['artifact_id'],
                            'claimed_paid_wait_seconds': wait['seconds'],
                            'interpretation': 'DEPENDENCY_WAIT_NOT_TEST_COMPUTE',
                            'provider_receipt_authenticated': False})
    for item in schedules:
        require(item, 'artifact schedule')
        key = (text(item.get('artifact_id'), 'artifact_id'),
               text(item.get('producer_job'), 'producer_job'),
               text(item.get('producer_run_id'), 'producer_run_id'))
        if key in schedule_keys:
            raise InvalidManifest('duplicate artifact schedule')
        schedule_keys.add(key)
        if item.get('producer_revision') != source:
            issues.append('ARTIFACT_SOURCE_STALE:' + key[0])
        available = number(item.get('producer_available_at_s'), 'producer_available_at_s')
        if item.get('producer_status') != 'success':
            issues.append('ARTIFACT_PRODUCER_NOT_SUCCESSFUL:' + key[0])
        routes = item.get('routes')
        if not isinstance(routes, list) or not routes or len(routes) > 30:
            raise InvalidManifest('artifact.routes must be bounded nonempty list')
        names = set()
        full_path = False
        alternative_path = False
        for route in routes:
            require(route, 'artifact route')
            name = text(route.get('name'), 'route.name')
            if name in names:
                raise InvalidManifest('duplicate artifact route')
            names.add(name)
            if not isinstance(route.get('producer_runs'), bool) or not isinstance(route.get('artifact_required'), bool):
                raise InvalidManifest('route must declare producer_runs and artifact_required')
            expected = unique_strings(route.get('consumers_expected'), 'route.consumers_expected')
            selected = unique_strings(route.get('consumers_scheduled'), 'route.consumers_scheduled')
            needs = unique_strings(route.get('needs_producer_for'), 'route.needs_producer_for')
            early = unique_strings(route.get('runner_allocated_while_waiting_for'), 'route.runner_allocated_while_waiting_for')
            if not expected:
                issues.append('NO_CONSUMER_SCOPE:' + name)
            if expected - selected:
                issues.append('LEGITIMATE_CONSUMER_SKIPPED:' + name)
            if selected - expected or needs - expected or early - expected:
                issues.append('UNDECLARED_CONSUMER:' + name)
            if route['producer_runs']:
                full_path = True
                if not route['artifact_required']:
                    issues.append('PRODUCER_ARTIFACT_NOT_REQUIRED:' + name)
                if expected - needs:
                    issues.append('CONSUMER_MISSING_PRODUCER_NEEDS:' + name)
                if early:
                    issues.append('PAID_RUNNER_WAITS_FOR_ARTIFACT:' + name)
                if route.get('producer_failure_blocks') is not True:
                    issues.append('PRODUCER_FAILURE_NOT_PROPAGATED:' + name)
                if route.get('artifact_custody') != 'same-run':
                    issues.append('CROSS_RUN_ARTIFACT_CUSTODY:' + name)
            else:
                alternative_path = True
                if route['artifact_required']:
                    issues.append('ARTIFACT_REQUIRED_WHEN_PRODUCER_SKIPPED:' + name)
                if needs:
                    issues.append('SKIPPED_PRODUCER_UNCONDITIONAL_NEEDS:' + name)
                if early:
                    issues.append('ALTERNATE_PATH_ALLOCATES_WAITING_RUNNER:' + name)
                if not route.get('fallback_verification'):
                    issues.append('ALTERNATE_VERIFICATION_MISSING:' + name)
        if not full_path or not alternative_path:
            issues.append('ARTIFACT_PATH_COVERAGE_INCOMPLETE:' + key[0])
        for wait in waits:
            if (wait['artifact_id'], wait['producer_job'], wait['run_id']) != key:
                continue
            matched.add(wait['id'])
            if abs(available - wait['available_at_s']) > 0.001:
                issues.append('ARTIFACT_AVAILABILITY_MISMATCH:' + wait['id'])
            if wait['revision'] != item['producer_revision']:
                issues.append('ARTIFACT_PRODUCER_REVISION_MISMATCH:' + wait['id'])
            if not any(route['producer_runs'] and wait['consumer_job'] in
                       route['consumers_expected'] for route in routes):
                issues.append('WAIT_CONSUMER_NOT_ROUTED:' + wait['id'])
    for wait in waits:
        if wait['id'] not in matched:
            issues.append('WAIT_ARTIFACT_UNMATCHED:' + wait['id'])
    return {'diagnostics': diagnostics, 'issues': sorted(set(issues)),
            'claimed_runner_occupied_wait_seconds': round(total_wait, 3),
            'measured_runner_minutes_saved': 'NOT_MEASURED',
            'measured_critical_path_delta': 'NOT_MEASURED',
            'requires_provider_timing_and_job_graph': True,
            'provider_authenticated': False}


def assess(document):
    require(document, 'manifest')
    if document.get('schema_version') != 1:
        raise InvalidManifest('unsupported manifest version')
    source = text(document.get('source_revision'), 'source_revision')
    inventory = require(document.get('inventory'), 'inventory')
    plan = require(document.get('repair'), 'repair')
    issues = []
    if inventory.get('complete') is not True or inventory.get('nested_graph_traced') is not True:
        issues.append('INCOMPLETE_EXECUTION_INVENTORY')
    if inventory.get('normative_specs_inspected') is not True or inventory.get('branch_rules_inspected') is not True:
        issues.append('GOVERNANCE_SOURCES_NOT_INSPECTED')
    unresolved = inventory.get('unresolved_paths')
    if not isinstance(unresolved, list) or unresolved:
        issues.append('UNRESOLVED_EXECUTION_PATH')
    if not isinstance(inventory.get('workflows'), list) or not inventory['workflows']:
        issues.append('WORKFLOWS_NOT_ENUMERATED')
    if plan.get('mode') != 'CI_SELF_REPAIR' or plan.get('stages') != list(STAGES):
        issues.append('REPAIR_SEQUENCE_INCOMPLETE')
    if plan.get('one_coordinated_change') is not True or plan.get('draft_preparation') is not True:
        issues.append('PREPARE_NOT_BOUNDED_AND_CHEAP')
    readiness = require(plan.get('readiness'), 'repair.readiness')
    for field in ('source', 'workflow', 'tests', 'policy', 'negative_controls', 'rollback'):
        if readiness.get(field) is not True:
            issues.append('READINESS_MISSING:' + field)
    if plan.get('readiness_head') != source:
        issues.append('READINESS_HEAD_STALE')
    count = number(plan.get('planned_expensive_cycles'), 'planned_expensive_cycles')
    limit = number(plan.get('max_expensive_cycles'), 'max_expensive_cycles')
    if not isinstance(count, int) or not isinstance(limit, int):
        raise InvalidManifest('planned and maximum expensive cycles must be integers')
    if limit > 2 or count > limit or count < 1:
        issues.append('UNBOUNDED_EXPENSIVE_REVALIDATION')
    forecast = plan.get('forecast')
    if not isinstance(forecast, list) or not forecast or len(forecast) > 200:
        raise InvalidManifest('repair.forecast must be a nonempty bounded list')
    seen_events = set()
    for row in forecast:
        require(row, 'forecast event')
        event = text(row.get('event'), 'forecast.event')
        if event in seen_events:
            raise InvalidManifest('duplicate forecast event')
        seen_events.add(event)
        jobs = number(row.get('selected_jobs'), 'forecast.selected_jobs')
        if not isinstance(row.get('expensive'), bool):
            raise InvalidManifest('forecast.expensive must be boolean')
        if event == 'draft' and jobs and row['expensive']:
            issues.append('DRAFT_EXPENSIVE_FANOUT')
        if not isinstance(jobs, int):
            raise InvalidManifest('forecast.selected_jobs must be an integer')
        if event in ('ready', 'release') and jobs == 0:
            issues.append('REQUIRED_FANOUT_ABSENT:' + event)
        if jobs > 1 and row.get('approval') != 'owner-authorized':
            issues.append('FANOUT_NOT_ACKNOWLEDGED:' + event)
        if row.get('inputs_revision') != source:
            issues.append('FANOUT_REVISION_STALE:' + event)
    if not {'draft', 'ready', 'release'}.issubset(seen_events):
        issues.append('FANOUT_EVENTS_INCOMPLETE')
    if number(plan.get('old_unconditional_paths'), 'old_unconditional_paths'):
        issues.append('OLD_UNCONDITIONAL_PATH_REMAINS')
    if plan.get('cheap_preflight_result') != 'success' or plan.get('cheap_preflight_head') != source:
        issues.append('CHEAP_CHECK_MISSING_OR_STALE')
    normative = unique_strings(plan.get('normative_required'), 'normative_required')
    candidate = unique_strings(plan.get('candidate_selected'), 'candidate_selected')
    release = unique_strings(plan.get('release_selected'), 'release_selected')
    policy = unique_strings(plan.get('protected_statuses'), 'protected_statuses')
    if not normative or not candidate or not release:
        issues.append('QUALIFICATION_OBLIGATIONS_EMPTY')
    if normative - candidate:
        issues.append('NORMATIVE_CANDIDATE_CHECK_REMOVED')
    if normative - release:
        issues.append('NORMATIVE_RELEASE_CHECK_REMOVED')
    if policy - candidate:
        issues.append('PROTECTED_STATUS_NOT_SELECTED')
    classes = unique_strings(plan.get('change_classes'), 'change_classes')
    risky = classes & {'workflow', 'policy', 'governance', 'release', 'unknown'}
    if risky and (plan.get('authorized_policy_migration') is not True or
                  not plan.get('full_qualification') is True):
        issues.append('RISKY_POLICY_CHANGE_REQUIRES_FULL_OR_AUTHORIZED_MIGRATION')
    if plan.get('merge_qualified_from_draft') is not False:
        issues.append('DRAFT_NOT_QUALIFIED')
    phase = inspect_phases(document.get('phase_observations'), source)
    artifact = inspect_artifact_waits(document, document.get('phase_observations'), source)
    issues.extend(artifact['issues'])
    # Local cost arithmetic is source-fixture interpretation; do not confuse
    # claimed 'observed' fields with independent provider authentication.
    return {'schema_version': 1, 'status': 'STRUCTURAL_PASS' if not issues else 'HOLD',
            'issues': sorted(set(issues)), 'predicted_fanout': forecast,
            'phase_analysis': phase, 'artifact_dependency_analysis': artifact,
            'optimization_complete': False, 'host_authenticated': False,
            'observed_runner_minutes_delta': 'NOT_MEASURED',
            'observed_critical_path_delta': 'NOT_MEASURED'}


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InvalidManifest('duplicate JSON key')
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        input_path = args.input.absolute()
        if any(p.is_symlink() for p in (input_path, *input_path.parents)):
            raise InvalidManifest('linked input path or ancestor')
        if input_path.stat().st_size > MAX_BYTES:
            raise InvalidManifest('manifest exceeds 1 MiB')
        value = json.loads(input_path.read_text(encoding='utf-8'),
                           object_pairs_hook=reject_duplicate_keys)
        report = assess(value)
    except (InvalidManifest, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print('CI_REPAIR_INVALID: ' + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0 if report['status'] == 'STRUCTURAL_PASS' else 3


if __name__ == '__main__':
    sys.exit(main())
