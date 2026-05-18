from __future__ import annotations

from portfolio_engine.metrics import summarize_results
from portfolio_engine.runner import run_match
from portfolio_engine.trace import trace_payload


def main() -> int:
    primary = run_match(seed=7)
    batch = [run_match(seed=seed) for seed in range(1, 11)]

    print("Believe in Me - Engine Demo")
    print(f"Primary seed: {primary.seed}")
    print(f"Winner: {primary.winner_id}")
    print(f"Turns: {primary.turn_count}")
    print(f"Events: {len(primary.final_state.events)}")
    print("Last event:", trace_payload(primary)["events"][-1])
    print("Metrics:", summarize_results(batch))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
