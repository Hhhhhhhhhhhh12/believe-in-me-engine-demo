from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from typing import Any

from .runner import RunResult


def summarize_results(results: Iterable[RunResult]) -> dict[str, Any]:
    materialized = list(results)
    winner_counts = Counter(result.winner_id or "none" for result in materialized)
    average_turns = (
        sum(result.turn_count for result in materialized) / len(materialized)
        if materialized
        else 0.0
    )
    return {
        "games": len(materialized),
        "winner_counts": dict(sorted(winner_counts.items())),
        "average_turns": round(average_turns, 2),
    }
