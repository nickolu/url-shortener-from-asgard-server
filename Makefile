ROOT_DIR := $(shell pwd)
APP := app.py

test: 
	python3 -m unittest

run:
	. venv/bin/activate
	FLASK_APP=$(APP) flask run 