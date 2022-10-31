API_DIR = server
DB_DIR = db
GAME_DIR = game
REQ_DIR = .

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

all_tests: FORCE
	cd $(DB_DIR); make tests
	cd $(API_DIR); make tests
	cd $(GAME_DIR); make tests

dev_env: FORCE
	export PYTHONPATH=$(pwd):$PYTHONPATH
	pip install -r $(REQ_DIR)/requirements-dev.txt

all_docs: FORCE
	cd $(API_DIR); make docs
	cd $(DB_DIR); make docs
	cd $(GAME_DIR); make docs

game_cmd: FORCE
	python3 $(GAME_DIR)/command_line.py