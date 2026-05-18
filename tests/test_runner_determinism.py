from portfolio_engine.runner import run_match
from portfolio_engine.trace import trace_payload


def test_same_seed_produces_same_trace() -> None:
    first = trace_payload(run_match(seed=11))
    second = trace_payload(run_match(seed=11))

    assert first == second


def test_different_seed_can_change_opening_card_order() -> None:
    first = trace_payload(run_match(seed=1))
    second = trace_payload(run_match(seed=2))

    assert first["events"] != second["events"]


def test_match_finishes_within_turn_budget() -> None:
    result = run_match(seed=3, max_turns=60)

    assert result.winner_id in {"p1", "p2", "p3"}
    assert result.turn_count <= 60
