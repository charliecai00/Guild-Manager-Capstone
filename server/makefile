LINTER = python3 -m flake8
PYTESTFLAGS = -vv --verbose --tb=short

FORCE:

tests: lint unit

unit: FORCE
	pytest $(PYTESTFLAGS)

lint: FORCE
	$(LINTER) *.py

# test a python file:
%.py: FORCE
	pytest -s tests/test_$*.py

# create html files from python files
docs: FORCE
	pydoc3 -w ./*py
	git add *html