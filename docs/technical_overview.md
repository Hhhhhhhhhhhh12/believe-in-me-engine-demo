# Technical Overview

This guide is for a quick technical read-through.

## Fast Path

```bash
python3 -m pip install -r requirements-dev.txt
make verify
make demo
```

Expected result:

- the test suite passes
- the content scan passes
- the example run prints a deterministic winner and aggregate metrics

## What To Inspect

- `src/believe_engine/state.py`: immutable data model
- `src/believe_engine/legal_moves.py`: legal command surface
- `src/believe_engine/rules.py`: state transition authority
- `src/believe_engine/runner.py`: seeded orchestration
- `src/believe_engine/trace.py`: serialized event contract
- `tests/`: focused regression coverage

## Design Signals

- State changes are explicit and testable.
- Legal moves are derived from state, not guessed by callers.
- Runs are seeded for reproducibility.
- Trace payloads expose stable fields.
- The content scan is part of `make verify`.

## Scope

The `Believe in Me` name is kept as a project signal. The engine model is a
small sample system built for this repository.
