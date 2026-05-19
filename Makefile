PYTHON ?= python3
PYTEST ?= $(PYTHON) -m pytest

.PHONY: test demo scan verify

test:
	PYTHONPATH=src $(PYTEST) -q

demo:
	PYTHONPATH=src $(PYTHON) examples/run_demo.py

scan:
	PYTHONPATH=src $(PYTHON) scripts/content_scan.py

verify: test scan
