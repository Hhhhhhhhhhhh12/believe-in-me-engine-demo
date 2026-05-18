from portfolio_engine.metrics import summarize_results
from portfolio_engine.runner import run_match


def test_summarize_results_counts_games_and_winners() -> None:
    results = [run_match(seed=seed) for seed in range(1, 4)]
    summary = summarize_results(results)

    assert summary["games"] == 3
    assert sum(summary["winner_counts"].values()) == 3
    assert summary["average_turns"] > 0


def test_empty_summary_is_defined() -> None:
    assert summarize_results([]) == {
        "games": 0,
        "winner_counts": {},
        "average_turns": 0.0,
    }
