LINTER = python3 -m flake8
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

lint: FORCE
	$(LINTER) *.py

unit: FORCE
	pytest $(PYTESTFLAGS)