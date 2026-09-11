"""Four-layer DONE gate reconstructed from September 3-4 historical contracts."""
import sys
from check_acceptance_matrix import LAYERS, check_layers, check_record, cli, evaluate as acceptance

def evaluate(value):
    if not isinstance(value, dict):
        raise ValueError('input must be a JSON object')
    issues = []
    check_layers(value.get('layers'), issues)
    if value.get('task_type') == 'mvp_crud':
        outer_layers = value.get('layers') if isinstance(value.get('layers'), dict) else {}
        for required in ('SOURCE_BUILD', 'RUNTIME_UI', 'DATA_BUSINESS'):
            record = outer_layers.get(required)
            if not isinstance(record, dict) or record.get('status') not in ('PASS', 'RUNTIME_PASS'):
                issues.append(f'CRUD completion requires a passing outer {required} evidence layer')
    matrix = value.get('acceptance_matrix')
    if not isinstance(matrix, dict):
        issues.append('acceptance_matrix: a declared status alone is insufficient; provide the matrix')
    elif matrix.get('status') == 'NOT_APPLICABLE':
        if value.get('task_type') not in ('local_code', 'documentation') or value.get('workflow_applicable') is not False:
            issues.append('acceptance_matrix: N/A requires local_code/documentation scope and workflow_applicable=false; CRUD cannot opt out')
        check_record(matrix, 'acceptance_matrix', issues)
        layer_records = value.get('layers')
        layer_records = layer_records if isinstance(layer_records, dict) else {}
        if not any(isinstance(record, dict) and record.get('status') in ('PASS', 'RUNTIME_PASS') for record in (layer_records.get(name) for name in LAYERS)):
            issues.append('completion: all N/A is not evidence; at least one passing evidence layer is required when workflow acceptance is inapplicable')
    else:
        if value.get('task_type') == 'mvp_crud' and matrix.get('task_type') != 'mvp_crud':
            issues.append('acceptance_matrix: completion CRUD scope requires a CRUD matrix')
        issues.extend('acceptance_matrix.' + issue for issue in acceptance(matrix)['issues'])
    return {'status': 'DONE_BLOCKED' if issues else 'DONE_ALLOWED', 'issues': issues}

if __name__ == '__main__':
    sys.exit(cli(evaluate, 'DONE_ALLOWED'))
