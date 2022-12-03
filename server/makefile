# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

LINTER = python3 -m flake8 
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

lint: FORCE
	$(LINTER) *.py

unit: FORCE
	pytest $(PYTESTFLAGS)

# test a python file:
%.py: FORCE
	pytest -s tests/test_$*.py