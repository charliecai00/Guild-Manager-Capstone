LINTER = python3 -m flake8
API_DIR = server
DB_DIR = db
GAME_DIR = game

FORCE: 

# test: dev lint unit
test: dev lint

dev: FORCE
	pip3 install -r ./requirements-dev.txt

lint: FORCE
	$(LINTER) $(API_DIR)/*.py
	$(LINTER) $(DB_DIR)/*.py

unit: FORCE
	cd $(API_DIR); python3 -m pytest -vv --verbose --tb=short

game_cmd: FORCE
	py $(GAME_DIR)/command_line.py