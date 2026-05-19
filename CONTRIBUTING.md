# Contributing

This repository is intentionally small and public-safe. Contributions should
preserve that shape.

## Local Check

```bash
python3 -m pip install -r requirements-dev.txt
make verify
```

## Scope Rules

- Keep the engine model synthetic.
- Keep examples compact and deterministic.
- Add tests for behavior changes.
- Do not add production assets, private notes, or unpublished source material.

## Pull Request Standard

A useful pull request explains:

- what behavior changed
- which tests cover it
- whether the redaction scan was updated
