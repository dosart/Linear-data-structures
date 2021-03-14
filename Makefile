.PHONY: install selfcheck test lint check build

install:
	 poetry install

selfcheck:
	poetry check

test:
	poetry run python -m pytest tests/

lint:
	poetry run flake8 data_structure

check: selfcheck test lint

build: check
	poetry build

