# Reviewer Guide

This guide is for a quick external technical review.

## Fast Path

```bash
python3 -m pip install -r requirements-dev.txt
make verify
make demo
```

Expected result:

- the test suite passes
- the redaction scan passes
- the demo prints a deterministic winner and aggregate metrics

## What To Inspect

- `src/portfolio_engine/state.py`: immutable data model
- `src/portfolio_engine/legal_moves.py`: legal command surface
- `src/portfolio_engine/rules.py`: state transition authority
- `src/portfolio_engine/runner.py`: seeded orchestration
- `src/portfolio_engine/trace.py`: serialized event contract
- `tests/`: focused regression coverage

## Design Signals

- State changes are explicit and testable.
- Legal moves are derived from state, not guessed by callers.
- Runs are seeded for reproducibility.
- Trace payloads expose stable public fields.
- The redaction scan is part of `make verify`.

## Public Scope

The `Believe in Me` name is kept as a public project signal. The engine model,
names, numeric values, events, examples, and docs in this repository are
synthetic.
