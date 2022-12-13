# A NYU Capstone Project
# The Guild Manager by JV · CC · ZQ · ZF

API_DIR = server
DB_DIR = db
GAME_DIR = game

CURRDIR = $(shell pwd)
export PYTHONPATH = $(CURRDIR)

FORCE: 

all_tests: lint unit

dev_env: FORCE
	pip3 install -r ./requirements-dev.txt

prd: FORCE
	pip3 install -r ./requirements.txt

lint: FORCE
	cd $(API_DIR); make lint
	cd $(DB_DIR); make lint
	cd $(GAME_DIR); make lint

unit: FORCE
	cd $(API_DIR); make unit
	cd $(DB_DIR); make unit
	cd $(GAME_DIR); make unit
