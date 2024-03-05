.PHONY: all generate_in requirements.txt requirements-test.txt

all: generate_in requirements.txt requirements-test.txt

generate_in:
	python tools/make-requirements-in.py

requirements.txt: requirements.in pyproject.toml
	pip-compile -q --no-annotate --resolver=backtracking --upgrade --allow-unsafe --no-header  --unsafe-package n/a --no-strip-extras requirements.in -o requirements.txt

requirements-test.txt: requirements-test.in pyproject.toml
	pip-compile -q --no-annotate --resolver=backtracking --upgrade --allow-unsafe --no-header  --unsafe-package n/a --no-strip-extras requirements-test.in -o requirements-test.txt
