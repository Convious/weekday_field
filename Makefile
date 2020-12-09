ENV = env
BIN = $(ENV)/bin
PIP = $(BIN)/pip
PYTHON = $(BIN)/python
PYTEST = $(BIN)/pytest


environ: $(ENV)/.done

.PHONY: help
help:
	@echo "make                         # build everything"
	@echo "make run                     # run dev server"
	@echo "make test                    # run unit tests"

$(PIP):
	python -m venv env
	$(PIP) install -U pip setuptools wheel

$(ENV)/.done: $(PIP) requirements.txt
	$(PIP) install -r requirements.txt -e .
	touch env/.done

.PHONY: run
run: environ
	$(PYTHON) manage.py runserver

.PHONY: test
test: environ
	$(PYTEST) -vv --tb=native weekday_field/tests

.PHONY: clean
clean: clean_pycache
	rm -rf $(ENV) weekday_field.egg-info

.PHONY: clean_pycache
.clean_pycache:
	find . -name "__pycache__" -type d -exec rm -rf "{}" +
	find . -name "*.pyc" -delete
