"""Offline five-minute policy evaluator. Does not call or configure any model."""
import math
import sys
from check_acceptance_matrix import cli

def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)

def evaluate(value):
    if not isinstance(value, dict):
        raise ValueError('input must be a JSON object')
    now = value.get('now')
    minimum = value.get('minimum_samples', 5)
    events = value.get('events')
    if not number(now) or not isinstance(minimum, int) or isinstance(minimum, bool) or minimum < 1 or not isinstance(events, list):
        raise ValueError('now must be epoch seconds; minimum_samples a positive integer; events an array')
    selected = []
    for event in events:
        if not isinstance(event, dict) or set(event) - {'timestamp', 'ok', 'latency_ms'}:
            raise ValueError('events allow only timestamp, ok and latency_ms; no request content')
        if not number(event.get('timestamp')) or not isinstance(event.get('ok'), bool) or not number(event.get('latency_ms')) or event['latency_ms'] < 0:
            raise ValueError('invalid event timestamp, boolean ok or nonnegative latency_ms')
        if now - 300 <= event['timestamp'] <= now:
            selected.append(event)
    count = len(selected)
    result = {'status': 'NOT_RUN' if count == 0 else 'NOT_ENOUGH_SAMPLES', 'sample_count': count, 'window_seconds': 300, 'minimum_samples': minimum, 'action': 'NO_ROUTE_CHANGE', 'quality': 'NOT_EVALUATED'}
    if count < minimum:
        return result
    rate = sum(not event['ok'] for event in selected) / count
    p95 = sorted(event['latency_ms'] for event in selected)[math.ceil(count * .95) - 1]
    degraded = rate > .2 or p95 > 90000
    result.update(status='ROUTE_DEGRADED' if degraded else 'ROUTE_HEALTHY', error_rate=rate, p95_latency_ms=p95)
    if degraded:
        fallback = value.get('fallback')
        if fallback is not None and (not isinstance(fallback, str) or not fallback.strip()):
            raise ValueError('fallback must be a configured route name')
        result.update(action='USE_CONFIGURED_FALLBACK' if fallback else 'FALLBACK_NOT_CONFIGURED', selected_fallback=fallback, quality='QUALITY_DEGRADED')
    else:
        result['quality'] = 'NOT_EVALUATED'
    return result

if __name__ == '__main__':
    sys.exit(cli(evaluate, 'ROUTE_HEALTHY'))
