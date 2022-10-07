LINTER = python3 -m flake8

FORCE:

lint: FORCE
	$(LINTER) *.py

unit: FORCE
	pytest -vv --verbose --tb=short
