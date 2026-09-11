import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parent

def invoke(name, payload):
    result = subprocess.run([sys.executable, str(ROOT / name)], input=json.dumps(payload), text=True, capture_output=True)
    return result.returncode, json.loads(result.stdout)

def proof(kind='RUNTIME_OBSERVED'):
    return {'status': 'PASS', 'evidence': [{'kind': kind, 'reference': 'test-fixture:observed-business-result'}]}

def layers():
    return {name: proof(kind) for name, kind in {'SOURCE_BUILD': 'BUILD_OBSERVED', 'RUNTIME_UI': 'UI_OBSERVED', 'DATA_BUSINESS': 'BUSINESS_OBSERVED', 'RELEASE_CUTOVER': 'RELEASE_OBSERVED'}.items()}

def matrix():
    return {'task_type': 'mvp_crud', 'layers': layers(), 'journey': {name: proof('UI_OBSERVED') for name in ['login', 'create', 'list', 'edit', 'error']}, 'cases': {name: proof('UI_OBSERVED') for name in ['success', 'error', 'empty', 'retry', 'duplicate', 'permission']}}

class Gates(unittest.TestCase):
    def test_source_only_blocks(self):
        code, result = invoke('check_completion_gate.py', {'layers': {'SOURCE_BUILD': proof('SOURCE_INFERRED')}, 'acceptance_matrix': matrix()})
        self.assertEqual(code, 1)
        for name in ['RUNTIME_UI', 'DATA_BUSINESS', 'RELEASE_CUTOVER']:
            self.assertTrue(any(name in issue for issue in result['issues']))

    def test_complete(self):
        self.assertEqual(invoke('check_completion_gate.py', {'layers': layers(), 'acceptance_matrix': matrix()})[1]['status'], 'DONE_ALLOWED')

    def test_crud_completion_cannot_hide_all_four_evidence_layers_as_na(self):
        na = {'status': 'NOT_APPLICABLE', 'reason': 'Not declared in the outer manifest'}
        value = {
            'task_type': 'mvp_crud',
            'layers': {name: dict(na) for name in layers()},
            'acceptance_matrix': matrix(),
        }
        code, result = invoke('check_completion_gate.py', value)
        self.assertEqual(code, 1)
        self.assertTrue(any('CRUD' in issue or 'RUNTIME_UI' in issue or 'DATA_BUSINESS' in issue for issue in result['issues']))

    def test_reasoned_na(self):
        value = {'layers': {name: {'status': 'NOT_APPLICABLE', 'reason': 'Documentation task has no deployed runtime or business data'} for name in layers()}, 'acceptance_matrix': {'task_type': 'documentation', 'layers': layers(), 'journey': {'read': proof()}, 'cases': {'success': proof(), 'error': {'status': 'NOT_APPLICABLE', 'reason': 'No executable behavior'}}}}
        self.assertEqual(invoke('check_completion_gate.py', value)[0], 0)
        value['layers']['RUNTIME_UI']['reason'] = ''
        self.assertEqual(invoke('check_completion_gate.py', value)[0], 1)

    def test_bad_evidence_blocks(self):
        for evidence in [[], [{'kind': 'UNKNOWN', 'reference': 'x'}], [{'kind': 'UI_OBSERVED', 'reference': ''}]]:
            value = matrix()
            value['journey']['edit']['evidence'] = evidence
            self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)

    def test_crud_missing_required_steps(self):
        for name in ['login', 'edit', 'error']:
            value = matrix()
            del value['journey'][name]
            self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)

    def test_crud_source_http_only_blocks(self):
        for kind in ['SOURCE_INFERRED', 'HTTP_OBSERVED']:
            value = matrix()
            value['journey'] = {name: proof(kind) for name in value['journey']}
            self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)

    def test_cases_cannot_disappear(self):
        value = matrix()
        del value['cases']['permission']
        self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)
        value['cases']['permission'] = {'status': 'NOT_APPLICABLE', 'reason': 'No access-controlled entities'}
        self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 0)

    def test_incomplete_status_blocks(self):
        for status in ['NOT_RUN', 'BLOCKED', 'OLD_RUNTIME', 'DOCUMENTED_ONLY', 'UNKNOWN']:
            value = matrix()
            value['layers']['DATA_BUSINESS']['status'] = status
            self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)

    def test_empty_templates_block(self):
        for script, template in [('check_completion_gate.py', 'completion-manifest.json'), ('check_acceptance_matrix.py', 'acceptance-matrix.json')]:
            self.assertEqual(invoke(script, json.loads((ROOT.parent / 'templates' / template).read_text()))[0], 1)

    def test_health(self):
        events = [{'timestamp': 999 - i, 'ok': i > 1, 'latency_ms': 100000 if i == 0 else 1000} for i in range(5)]
        code, result = invoke('model_health.py', {'now': 1000, 'events': events, 'fallback': 'already-configured'})
        self.assertEqual(code, 1)
        self.assertEqual(result['status'], 'ROUTE_DEGRADED')
        self.assertEqual(result['error_rate'], .4)
        self.assertEqual(result['p95_latency_ms'], 100000)
        self.assertEqual(result['selected_fallback'], 'already-configured')
        self.assertEqual(result['quality'], 'QUALITY_DEGRADED')

    def test_health_threshold_and_window(self):
        events = [{'timestamp': 999, 'ok': i > 0, 'latency_ms': 90000} for i in range(5)]
        events += [{'timestamp': 699, 'ok': False, 'latency_ms': 999999}, {'timestamp': 1001, 'ok': False, 'latency_ms': 999999}]
        code, result = invoke('model_health.py', {'now': 1000, 'events': events})
        self.assertEqual(code, 0)
        self.assertEqual(result['sample_count'], 5)

    def test_empty_and_small_samples(self):
        self.assertEqual(invoke('model_health.py', {'now': 1000, 'events': []})[1]['status'], 'NOT_RUN')
        event = {'timestamp': 999, 'ok': True, 'latency_ms': 1}
        self.assertEqual(invoke('model_health.py', {'now': 1000, 'events': [event]})[1]['status'], 'NOT_ENOUGH_SAMPLES')

    def test_health_each_threshold_and_missing_fallback(self):
        for errors, latency in [(2, 1000), (0, 90001)]:
            events = [{'timestamp': 1000, 'ok': i >= errors, 'latency_ms': latency} for i in range(5)]
            code, result = invoke('model_health.py', {'now': 1000, 'events': events})
            self.assertEqual(code, 1)
            self.assertEqual(result['status'], 'ROUTE_DEGRADED')
            self.assertEqual(result['action'], 'FALLBACK_NOT_CONFIGURED')

    def test_nearest_rank_p95_excludes_top_five_percent(self):
        events = [{'timestamp': 1000, 'ok': True, 'latency_ms': 100000 if i == 19 else 1000} for i in range(20)]
        self.assertEqual(invoke('model_health.py', {'now': 1000, 'events': events})[1]['p95_latency_ms'], 1000)

    def test_health_window_includes_exact_five_minute_boundary(self):
        events = [{'timestamp': 700, 'ok': True, 'latency_ms': 1000} for _ in range(5)]
        self.assertEqual(invoke('model_health.py', {'now': 1000, 'events': events})[0], 0)

    def test_health_rejects_content_and_malformed_events(self):
        for change in [{'prompt': 'must not enter events'}, {'ok': 'true'}, {'latency_ms': -1}, {'latency_ms': float('nan')}, {'timestamp': True}]:
            event = {'timestamp': 1000, 'ok': True, 'latency_ms': 10}
            event.update(change)
            self.assertEqual(invoke('model_health.py', {'now': 1000, 'events': [event]})[0], 2)

    def test_claimed_acceptance_status_is_insufficient(self):
        self.assertEqual(invoke('check_completion_gate.py', {'layers': layers(), 'acceptance_matrix': {'status': 'PASS'}})[0], 1)

    def test_layers_require_matching_evidence(self):
        for name, wrong in [('SOURCE_BUILD', 'UI_OBSERVED'), ('RUNTIME_UI', 'HTTP_OBSERVED'), ('DATA_BUSINESS', 'RUNTIME_OBSERVED'), ('RELEASE_CUTOVER', 'UI_OBSERVED')]:
            value = matrix()
            value['layers'][name] = proof(wrong)
            self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)

    def test_generic_journey_cannot_be_all_na(self):
        value = matrix()
        value['task_type'] = 'documentation'
        value['journey'] = {'read': {'status': 'NOT_APPLICABLE', 'reason': 'No executable path'}}
        self.assertEqual(invoke('check_acceptance_matrix.py', value)[0], 1)

    def test_bounded_local_completion_can_explain_no_workflow(self):
        value = {'task_type': 'local_code', 'workflow_applicable': False, 'layers': {name: {'status': 'NOT_APPLICABLE', 'reason': 'No runtime, data or release changes'} for name in layers()}, 'acceptance_matrix': {'status': 'NOT_APPLICABLE', 'reason': 'Local static-only change with no user workflow'}}
        value['layers']['SOURCE_BUILD'] = proof('BUILD_OBSERVED')
        self.assertEqual(invoke('check_completion_gate.py', value)[0], 0)
        for task_type in ['mvp_crud', 'unknown', None]:
            value['task_type'] = task_type
            self.assertEqual(invoke('check_completion_gate.py', value)[0], 1)
        value['task_type'] = 'local_code'
        value['workflow_applicable'] = True
        self.assertEqual(invoke('check_completion_gate.py', value)[0], 1)

    def test_file_cli_reads_default_template(self):
        result = subprocess.run([sys.executable, str(ROOT / 'model_health.py'), str(ROOT.parent / 'templates' / 'model-health.json')], text=True, capture_output=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['status'], 'NOT_RUN')

    def test_invalid_input(self):
        for script in ['model_health.py', 'check_completion_gate.py', 'check_acceptance_matrix.py']:
            self.assertNotEqual(invoke(script, [])[0], 0)

if __name__ == '__main__':
    unittest.main()

class ZeroEvidenceRegression(unittest.TestCase):
    def test_all_na_without_observation_is_blocked(self):
        na = {'status': 'NOT_APPLICABLE', 'reason': 'No workflow in this local task'}
        value = {'task_type': 'local_code', 'workflow_applicable': False,
                 'layers': {name: dict(na) for name in layers()}, 'acceptance_matrix': dict(na)}
        self.assertEqual(invoke('check_completion_gate.py', value)[1]['status'], 'DONE_BLOCKED')
        value['layers']['EXTRA'] = proof('BUILD_OBSERVED')
        self.assertEqual(invoke('check_completion_gate.py', value)[1]['status'], 'DONE_BLOCKED')
        value['layers']['SOURCE_BUILD'] = proof('BUILD_OBSERVED')
        self.assertEqual(invoke('check_completion_gate.py', value)[1]['status'], 'DONE_ALLOWED')
