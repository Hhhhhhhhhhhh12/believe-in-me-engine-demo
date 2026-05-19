# Believe in Me - Engine Demo

[![Verify](https://github.com/Hhhhhhhhhhhh12/believe-in-me-engine-demo/actions/workflows/verify.yml/badge.svg)](https://github.com/Hhhhhhhhhhhh12/believe-in-me-engine-demo/actions/workflows/verify.yml)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This repository is a sanitized portfolio demo for a deterministic game-engine
workflow. It keeps the public-facing `Believe in Me` name, but the model,
cards, numbers, rules, examples, and traces are synthetic.

## Why This Exists

The goal is to show the engineering shape of a game-engine project without
publishing private product content. The demo focuses on reproducibility,
state-transition clarity, test coverage, and public-safe trace output.

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

Example output:

```text
Believe in Me - Engine Demo
Primary seed: 7
Winner: p3
Turns: 45
Events: 46
Metrics: {'games': 10, 'winner_counts': {'p1': 5, 'p2': 4, 'p3': 1}, 'average_turns': 47.5}
```

## Review Path

For a quick external review, start with:

- `docs/reviewer_guide.md`
- `docs/architecture.md`
- `docs/redaction_policy.md`
- `tests/`

## Architecture

The engine is deliberately small:

- `state.py` defines plain data structures.
- `legal_moves.py` exposes available commands.
- `rules.py` applies one command at a time.
- `runner.py` drives seeded simulations.
- `trace.py` serializes public-safe events.
- `metrics.py` summarizes runs.

See `docs/architecture.md` and `docs/redaction_policy.md` for the public scope.
