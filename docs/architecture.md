# Architecture

This project keeps the engine deliberately small while preserving the pieces
that make turn-based systems testable.

## Boundaries

- `believe_engine.state`: data model only
- `believe_engine.legal_moves`: command discovery
- `believe_engine.rules`: authoritative state transitions
- `believe_engine.runner`: orchestration and seeded automation
- `believe_engine.trace`: event serialization
- `believe_engine.metrics`: summary calculations

The UI layer is intentionally absent. The focus is the deterministic engine
contract, testability, and trace quality.

## Public Model

Each player manages generic resources and project cards. A turn may gather
resources, play a card, convert resources into progress, or pass. The first
player reaching the target progress wins.

All names and values are compact sample data for this repository.

## Verification

`make verify` combines two checks:

- unit and contract tests
- a repository content scan

The scan is intentionally simple. It is not a replacement for human review, but
it helps keep the repository focused on its small sample model.
