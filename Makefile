ROOT_DIR := $(shell pwd)
APP := app.py

test: 
	python3 -m unittest

activate: 
	. $(ROOT_DIR)/venv/bin/activate

run:
	FLASK_APP=$(APP) flask run 