# Believe in Me - Engine Core

[![Verify](https://github.com/Hhhhhhhhhhhh12/believe-in-me-engine-demo/actions/workflows/verify.yml/badge.svg)](https://github.com/Hhhhhhhhhhhh12/believe-in-me-engine-demo/actions/workflows/verify.yml)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This repository is a compact deterministic Python engine for a turn-based
resource system. It uses the `Believe in Me` name while keeping the mechanics
small, inspectable, and easy to run locally.

## Why This Exists

The project focuses on reproducibility, state-transition clarity, test
coverage, and traceable engine events. The rule set is intentionally small so
the code can be reviewed quickly.

## What This Shows

- deterministic seeded simulation
- immutable-style state transitions
- legal action generation
- traceable engine events
- small metric aggregation
- focused regression tests

## Project Boundaries

The repository intentionally leaves out:

- production assets
- long-form design notes
- generated analysis outputs
- large data files

## Run

```bash
python3 -m pip install -r requirements-dev.txt
make demo
make verify
```

The command prints a compact trace summary and aggregate metrics for a small
sample match.

Example output:

```text
Believe in Me - Engine Core
Primary seed: 7
Winner: p3
Turns: 45
Events: 46
Metrics: {'games': 10, 'winner_counts': {'p1': 5, 'p2': 4, 'p3': 1}, 'average_turns': 47.5}
```

## Read Path

For a quick technical read, start with:

- `docs/technical_overview.md`
- `docs/architecture.md`
- `docs/content_guidelines.md`
- `tests/`

## Architecture

The engine is deliberately small:

- `state.py` defines plain data structures.
- `legal_moves.py` exposes available commands.
- `rules.py` applies one command at a time.
- `runner.py` drives seeded simulations.
- `trace.py` serializes stable event payloads.
- `metrics.py` summarizes runs.

See `docs/architecture.md` and `docs/content_guidelines.md` for the project scope.
