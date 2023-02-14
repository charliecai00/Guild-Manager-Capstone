# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

LINTER = flake8

FORCE:

all_tests: lint unit

# lint: FORCE
# 	$(LINTER) *.py
# 	$(LINTER) tests/*.py
# 	$(LINTER) object_classes/*.py

# unit: FORCE
# 	python3 tests/game_object_test.py -v

lint_local:
	python3 -m $(LINTER) *.py
	python3 -m $(LINTER) tests/*.py
	python3 -m $(LINTER) object_classes/*.py