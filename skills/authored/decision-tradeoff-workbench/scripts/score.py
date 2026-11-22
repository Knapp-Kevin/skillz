#!/usr/bin/env python3
"""Offline decision score arithmetic, not evidence verification or decision authority."""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1024 * 1024
ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
VALID_STATES = {"OWNER_SUPPLIED", "SOURCE_RECORDED", "UNKNOWN"}

class InputError(ValueError):
    pass


def distinct_pairs(pairs):
    output = {}
    for k, v in pairs:
        if k in output:
            raise InputError(f"duplicate JSON field: {k}")
        output[k] = v
    return output


def invalid_constant(value):
    raise InputError(f"invalid JSON constant: {value}")


def numeric(value, name, *, minimum=Decimal(0), maximum=Decimal(1000)):
    if isinstance(value, bool) or not isinstance(value, (int, str, Decimal)):
        raise InputError(f"{name}: requires a decimal number or numeric string")
    try:
        n = Decimal(str(value))
    except InvalidOperation as exc:
        raise InputError(f"{name}: invalid decimal") from exc
    if not n.is_finite() or n < minimum or n > maximum or n.as_tuple().exponent < -6:
        raise InputError(f"{name}: nonfinite, out of bounds or excessive precision")
    return n


def ident(value, name):
    if not isinstance(value, str) or not ID.fullmatch(value):
        raise InputError(f"{name}: must match {ID.pattern}")
    return value


def number(n):
    return format(n.normalize(), 'f') if n else '0'


def check_keys(obj, allowed, name):
    if not isinstance(obj, dict):
        raise InputError(f"{name}: object required")
    extra = obj.keys() - allowed
    if extra:
        raise InputError(f"{name}: unsupported keys {sorted(extra)}")


def exact_weights(criteria, alt_weights, name):
    if not isinstance(alt_weights, dict) or set(alt_weights) != {x['id'] for x in criteria}:
        raise InputError(f"{name}: weights must cover every criterion exactly")
    result = {c['id']: numeric(alt_weights[c['id']], f"{name}.{c['id']}") for c in criteria}
    if sum(result.values()) <= 0:
        raise InputError(f"{name}: requires a positive total weight")
    return result


def outcome(criteria, alternatives, weights, *, max_score):
    total = sum(weights.values()) if weights is not None else None
    rows = []
    for alt in alternatives:
        cells = alt['cells']
        observed = [c['id'] for c in criteria if cells[c['id']]['score'] is not None]
        missing = [c['id'] for c in criteria if cells[c['id']]['score'] is None]
        failed = [c['id'] for c in criteria if c['hard_gate_min'] is not None and cells[c['id']]['score'] is not None and cells[c['id']]['score'] < c['hard_gate_min']]
        unknown_gates = [c['id'] for c in criteria if c['hard_gate_min'] is not None and cells[c['id']]['score'] is None]
        gate = 'FAIL' if failed else 'UNKNOWN' if unknown_gates else 'PASS'
        subtotal = sum(weights[cid] * cells[cid]['score'] for cid in observed) if weights is not None else None
        observed_weight = sum(weights[cid] for cid in observed) if weights is not None else None
        breakdown = [
            {
                'criterion': c['id'],
                'score': number(cells[c['id']]['score']) if cells[c['id']]['score'] is not None else None,
                'evidence_status': cells[c['id']]['status'],
                'weighted_product': number(weights[c['id']] * cells[c['id']]['score'])
                    if weights is not None and cells[c['id']]['score'] is not None else None,
            } for c in criteria
        ]
        rows.append({
            'id': alt['id'],
            'cell_breakdown': breakdown,
            'hard_gate': gate,
            'failed_gates': failed,
            'unknown_gates': unknown_gates,
            'observed_criteria': observed,
            'unknown_criteria': missing,
            'observed_count': len(observed),
            'total_count': len(criteria),
            'observed_weight': number(observed_weight) if weights is not None else None,
            'total_weight': number(total) if weights is not None else None,
            'partial_weighted_total': number(subtotal) if weights is not None else None,
            'maximum_possible_total': number(subtotal + (total - observed_weight) * max_score) if weights is not None else None,
        })
    if weights is None:
        return {'state': 'UNAPPROVED_WEIGHTS', 'winner': None, 'rows': rows}
    if all(row['hard_gate'] == 'FAIL' for row in rows):
        return {'state': 'NO_FEASIBLE_ALTERNATIVE', 'winner': None, 'rows': rows}
    if any(row['hard_gate'] == 'UNKNOWN' for row in rows):
        return {'state': 'UNKNOWN_HARD_GATE', 'winner': None, 'rows': rows}
    viable = [r for r in rows if r['hard_gate'] == 'PASS']
    if any(r['unknown_criteria'] for r in viable):
        return {'state': 'INCOMPLETE_COMPARABLE_EVIDENCE', 'winner': None, 'rows': rows}
    if not viable:
        return {'state': 'NO_FEASIBLE_ALTERNATIVE', 'winner': None, 'rows': rows}
    best = max(Decimal(r['partial_weighted_total']) for r in viable)
    top = [r['id'] for r in viable if Decimal(r['partial_weighted_total']) == best]
    return {'state': 'TIE_ON_RECORDED_INPUT' if len(top) > 1 else 'LEADER_ON_RECORDED_INPUT',
            'winner': top[0] if len(top) == 1 else None, 'tied': top if len(top)>1 else [], 'rows': rows}


def score(doc):
    check_keys(doc, {'schema_version', 'weights_approved', 'score_max', 'criteria', 'alternatives', 'scenarios'}, 'root')
    if type(doc.get('schema_version')) is not int or doc['schema_version'] != 1:
        raise InputError('schema_version must equal 1')
    if type(doc.get('weights_approved')) is not bool:
        raise InputError('weights_approved must be boolean')
    max_score = numeric(doc.get('score_max'), 'score_max', minimum=Decimal('0.000001'), maximum=Decimal(100))
    raw_criteria, raw_options, raw_scenarios = doc.get('criteria'), doc.get('alternatives'), doc.get('scenarios', [])
    if not isinstance(raw_criteria, list) or not (1 <= len(raw_criteria) <= 30):
        raise InputError('criteria: 1..30 entries required')
    if not isinstance(raw_options, list) or not (2 <= len(raw_options) <= 20):
        raise InputError('alternatives: 2..20 entries required')
    if not isinstance(raw_scenarios, list) or len(raw_scenarios) > 20:
        raise InputError('scenarios: at most 20 entries')
    criteria, seen = [], set()
    for i, row in enumerate(raw_criteria):
        check_keys(row, {'id', 'weight', 'hard_gate_min'}, f'criteria[{i}]')
        cid = ident(row.get('id'), f'criteria[{i}].id')
        if cid in seen: raise InputError(f'duplicate criterion id: {cid}')
        seen.add(cid)
        minimum = None if row.get('hard_gate_min') is None else numeric(row['hard_gate_min'], f'{cid}.hard_gate_min', maximum=max_score)
        criteria.append({'id': cid, 'hard_gate_min': minimum, 'weight': row.get('weight')})
    base_weights = None
    if doc['weights_approved']:
        base_weights = exact_weights(criteria, {c['id']: c['weight'] for c in criteria}, 'criteria')
    elif any(c['weight'] is not None for c in criteria):
        # Optional illustration values are not silently used for an actual ranking.
        for c in criteria:
            if c['weight'] is not None: numeric(c['weight'], f"criteria.{c['id']}")
    alternatives, seen = [], set()
    for i, alt in enumerate(raw_options):
        check_keys(alt, {'id', 'cells'}, f'alternatives[{i}]')
        aid = ident(alt.get('id'), f'alternatives[{i}].id')
        if aid in seen: raise InputError(f'duplicate alternative id: {aid}')
        seen.add(aid)
        cells = alt.get('cells')
        if not isinstance(cells, dict) or set(cells) != {c['id'] for c in criteria}:
            raise InputError(f'{aid}: cells must cover every criterion exactly, UNKNOWN permitted')
        parsed = {}
        for cid, cell in cells.items():
            check_keys(cell, {'score', 'status', 'source'}, f'{aid}.{cid}')
            status = cell.get('status')
            if not isinstance(status, str) or status not in VALID_STATES: raise InputError(f'{aid}.{cid}: invalid evidence status')
            raw_score = cell.get('score')
            if status == 'UNKNOWN':
                if raw_score is not None: raise InputError(f'{aid}.{cid}: UNKNOWN must have null score')
                value = None
            else:
                if raw_score is None: raise InputError(f'{aid}.{cid}: scored evidence requires a value')
                if not isinstance(cell.get('source'), str) or not cell['source'].strip() or len(cell['source']) > 512:
                    raise InputError(f'{aid}.{cid}: scored cell requires source reference')
                value = numeric(raw_score, f'{aid}.{cid}.score', maximum=max_score)
            parsed[cid] = {'score': value, 'status': status}
        alternatives.append({'id': aid, 'cells': parsed})
    base = outcome(criteria, alternatives, base_weights, max_score=max_score)
    scenario_results, scenario_ids = [], set()
    for i, case in enumerate(raw_scenarios):
        check_keys(case, {'id', 'weights'}, f'scenarios[{i}]')
        sid = ident(case.get('id'), f'scenarios[{i}].id')
        if sid in scenario_ids: raise InputError('duplicate scenario id')
        scenario_ids.add(sid)
        weights = exact_weights(criteria, case.get('weights'), f'scenarios.{sid}')
        scenario_results.append({'id': sid, 'illustrative_only': True,
                                 'outcome': outcome(criteria, alternatives, weights, max_score=max_score)})
    return {'schema_version': 1, 'evidence_verified': False,
            'note': 'Arithmetic only. Source authenticity, score rubric, owner confirmation and permissions were not verified by this tool.',
            'base': base, 'scenarios': scenario_results}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', required=True, type=Path, help='Explicitly supplied local JSON file')
    args = p.parse_args(argv)
    try:
        # Refuse symlinked input and parents before stat/open, without
        # implying protection against concurrent hostile path replacement.
        input_path = args.input.absolute()
        if any(part.is_symlink() for part in (input_path, *input_path.parents)):
            raise InputError('symlinked input or ancestor')
        if input_path.stat().st_size > MAX_BYTES:
            raise InputError('input too large')
        with input_path.open('r', encoding='utf-8') as source:
            doc = json.load(source, object_pairs_hook=distinct_pairs, parse_float=Decimal, parse_constant=invalid_constant)
        result = score(doc)
    except (InputError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f'INVALID_INPUT: {exc}', file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0

if __name__ == '__main__':
    sys.exit(main())
