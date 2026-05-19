import json

from believe_engine.runner import run_match
from believe_engine.trace import trace_json, trace_payload


def test_trace_payload_exposes_stable_fields() -> None:
    result = run_match(seed=5)
    payload = trace_payload(result)

    assert set(payload) == {"seed", "turn_count", "winner_id", "events", "players"}
    assert {"round", "turn_index", "player_id", "type"} <= set(payload["events"][0])
    assert {"player_id", "resources", "progress", "discard_count"} == set(payload["players"][0])


def test_trace_json_is_stable_json() -> None:
    result = run_match(seed=5)

    decoded = json.loads(trace_json(result))

    assert decoded == trace_payload(result)
