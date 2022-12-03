# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

API_DIR = server
DB_DIR = db
GAME_DIR = game

CURRDIR = $(shell pwd)
export PYTHONPATH = $(CURRDIR)

FORCE: 

tests: lint unit

dev: FORCE
	pip3 install -r ./requirements-dev.txt

lint: FORCE
	echo "PYTHONPATH=$(PYTHONPATH)"
	cd $(API_DIR); make lint
	cd $(DB_DIR); make lint
	cd $(GAME_DIR); make lint

unit: FORCE
	cd $(API_DIR); make unit
	cd $(GAME_DIR); make unit
	cd $(DB_DIR); make unit

game_cmd: FORCE
	python3 $(GAME_DIR)/command_line.py