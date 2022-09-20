LINTER = python3 -m flake8
API_DIR = server
DB_DIR = db

FORCE: 

test: dev lint unit

dev: FORCE
	pip3 install -r ./requirements-dev.txt

lint: FORCE
	$(LINTER) $(API_DIR)/*.py
	$(LINTER) $(DB_DIR)/*.py

unit: FORCE
	cd $(API_DIR); python3 -m pytest -vv --verbose --tb=short