# Architecture

The demo follows the same engineering shape that matters in a production game
engine without publishing production content.

## Boundaries

- `portfolio_engine.state`: data model only
- `portfolio_engine.legal_moves`: command discovery
- `portfolio_engine.rules`: authoritative state transitions
- `portfolio_engine.runner`: orchestration and seeded automation
- `portfolio_engine.trace`: event serialization
- `portfolio_engine.metrics`: summary calculations

The UI layer is intentionally absent. The portfolio value is the deterministic
engine contract, testability, and trace quality.

## Public Model

Each player manages generic resources and project cards. A turn may gather
resources, play a card, convert resources into progress, or pass. The first
player reaching the target progress wins.

All names and values are synthetic placeholders for the public demo.

## Verification

`make verify` combines two checks:

- unit and contract tests
- a repository redaction scan

The scan is intentionally simple. It is not a replacement for human review, but
it makes accidental disclosure harder before changes are pushed.
