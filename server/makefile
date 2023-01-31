# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

LINTER = flake8 --ignore=E501,W291,E128,W293
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

all_tests: lint unit

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