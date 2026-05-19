# Contributing

This repository is intentionally small. Contributions should preserve that
shape.

## Local Check

```bash
python3 -m pip install -r requirements-dev.txt
make verify
```

## Scope Rules

- Keep the engine model compact.
- Keep examples compact and deterministic.
- Add tests for behavior changes.
- Do not add production assets, large generated outputs, or local credentials.

## Pull Request Standard

A useful pull request explains:

- what behavior changed
- which tests cover it
- whether the content scan was updated
