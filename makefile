API_DIR = server
DB_DIR = db
GAME_DIR = game


FORCE: 

test: dev unit

dev: FORCE
	pip3 install -r ./requirements-dev.txt

lint: FORCE
	cd $(API_DIR); make lint
	cd $(DB_DIR); make lint
	cd $(GAME_DIR); make lint

unit: FORCE
	cd $(API_DIR); make unit
	cd $(GAME_DIR); make unit
	cd $(DB_DIR); make unit

game_cmd: FORCE
	python3 $(GAME_DIR)/command_line.py