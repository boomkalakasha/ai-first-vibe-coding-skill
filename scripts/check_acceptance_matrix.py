"""Recovered contract implementation, not the lost original. Stdlib only."""
import json
from pathlib import Path
import sys

LAYERS = ('SOURCE_BUILD', 'RUNTIME_UI', 'DATA_BUSINESS', 'RELEASE_CUTOVER')
KINDS = {'SOURCE_INFERRED', 'BUILD_OBSERVED', 'RUNTIME_OBSERVED', 'UI_OBSERVED', 'HTTP_OBSERVED', 'BUSINESS_OBSERVED', 'RELEASE_OBSERVED'}

def check_record(record, label, issues, allow_na=True, runtime=False, ui=False):
    if not isinstance(record, dict):
        issues.append(label + ': missing evidence record')
        return
    status = record.get('status')
    if status == 'NOT_APPLICABLE' and allow_na:
        if not isinstance(record.get('reason'), str) or not record['reason'].strip():
            issues.append(label + ': NOT_APPLICABLE needs a reason')
        return
    if status not in ('PASS', 'RUNTIME_PASS'):
        issues.append(label + ': not passing')
        return
    evidence = record.get('evidence')
    if not isinstance(evidence, list) or not evidence:
        issues.append(label + ': empty evidence')
        return
    valid = []
    for item in evidence:
        if not isinstance(item, dict) or item.get('kind') not in KINDS or not isinstance(item.get('reference'), str) or not item['reference'].strip():
            issues.append(label + ': unknown or empty evidence')
        else:
            valid.append(item['kind'])
    if runtime and not any(kind in {'RUNTIME_OBSERVED', 'UI_OBSERVED', 'BUSINESS_OBSERVED', 'RELEASE_OBSERVED'} for kind in valid):
        issues.append(label + ': source/build/HTTP-only cannot prove runtime business completion')
    if ui and 'UI_OBSERVED' not in valid:
        issues.append(label + ': CRUD journey requires UI_OBSERVED evidence')

def check_layers(value, issues):
    value = value if isinstance(value, dict) else {}
    matching = {'SOURCE_BUILD': {'SOURCE_INFERRED', 'BUILD_OBSERVED'}, 'RUNTIME_UI': {'RUNTIME_OBSERVED', 'UI_OBSERVED'}, 'DATA_BUSINESS': {'BUSINESS_OBSERVED'}, 'RELEASE_CUTOVER': {'RELEASE_OBSERVED'}}
    for name in LAYERS:
        record = value.get(name)
        check_record(record, name, issues, runtime=name != 'SOURCE_BUILD')
        if isinstance(record, dict) and record.get('status') in ('PASS', 'RUNTIME_PASS'):
            evidence = record.get('evidence')
            evidence = evidence if isinstance(evidence, list) else []
            if not any(isinstance(item, dict) and item.get('kind') in matching[name] for item in evidence):
                issues.append(name + ': requires matching layer observation: ' + ', '.join(sorted(matching[name])))

def evaluate(value):
    if not isinstance(value, dict):
        raise ValueError('input must be a JSON object')
    issues = []
    task_type = value.get('task_type')
    if not isinstance(task_type, str) or not task_type.strip():
        issues.append('task_type is required')
    crud = task_type == 'mvp_crud'
    check_layers(value.get('layers'), issues)
    journey = value.get('journey')
    journey = journey if isinstance(journey, dict) else {}
    if not journey:
        issues.append('journey: empty')
    if not any(isinstance(record, dict) and record.get('status') in ('PASS', 'RUNTIME_PASS') for record in journey.values()):
        issues.append('journey: at least one measured passing step is required')
    for name in sorted(set(journey) | (set(('login', 'create', 'list', 'edit', 'error')) if crud else set())):
        check_record(journey.get(name), 'journey.' + name, issues, allow_na=not crud, runtime=True, ui=crud)
    cases = value.get('cases')
    cases = cases if isinstance(cases, dict) else {}
    required = {'success', 'error', 'empty', 'retry', 'duplicate', 'permission'} if crud else {'success', 'error'}
    for name in sorted(set(cases) | required):
        check_record(cases.get(name), 'cases.' + name, issues, allow_na=name != 'success' and (name != 'error' or not crud), runtime=True)
    return {'status': 'ACCEPTANCE_MATRIX_BLOCKED' if issues else 'ACCEPTANCE_MATRIX_PASS', 'issues': issues}

def cli(evaluator, passing_status):
    try:
        if len(sys.argv) > 2:
            raise ValueError('usage: script.py [input.json]; otherwise read JSON from stdin')
        raw = Path(sys.argv[1]).read_text(encoding='utf-8-sig') if len(sys.argv) == 2 else sys.stdin.read()
        result = evaluator(json.loads(raw))
        code = 0 if result['status'] == passing_status else 1
    except (ValueError, TypeError, KeyError, OSError) as error:
        result, code = {'status': 'INVALID_INPUT', 'issues': [str(error)]}, 2
    print(json.dumps(result, ensure_ascii=True, allow_nan=False))
    return code

if __name__ == '__main__':
    sys.exit(cli(evaluate, 'ACCEPTANCE_MATRIX_PASS'))
