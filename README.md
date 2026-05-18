# Believe in Me - Engine Demo

This repository is a sanitized portfolio demo for a deterministic game-engine
workflow. It keeps the public-facing `Believe in Me` name, but the model,
cards, numbers, rules, examples, and traces are synthetic.

## What This Shows

- deterministic seeded simulation
- immutable-style state transitions
- legal action generation
- traceable engine events
- small metric aggregation
- focused regression tests

## What This Does Not Include

- unpublished board-game rules
- real card names or card text
- internal analysis outputs
- private test notes
- private workflow documents
- production assets

## Run

```bash
python3 -m pip install -r requirements-dev.txt
make demo
make verify
```

The demo prints a compact trace summary and aggregate metrics for a small
synthetic match.

## Architecture

The engine is deliberately small:

- `state.py` defines plain data structures.
- `legal_moves.py` exposes available commands.
- `rules.py` applies one command at a time.
- `runner.py` drives seeded simulations.
- `trace.py` serializes public-safe events.
- `metrics.py` summarizes runs.

See `docs/architecture.md` and `docs/redaction_policy.md` for the public scope.
