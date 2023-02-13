# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

LINTER = flake8
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

# all_tests: lint unit

lint: FORCE
		$(LINTER) *.py
		$(LINTER) tests/*.py

unit: FORCE
		pytest $(PYTESTFLAGS)

# test a python file:
%.py: FORCE
		pytest -s tests/test_$*.py

lint_local:
		python3 -m $(LINTER) *.py
		python3 -m $(LINTER) tests/*.py

unit_local:
		python3 -m pytest $(PYTESTFLAGS)