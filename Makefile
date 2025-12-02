.PHONY: check-formatting format test run all

all: check-formatting test run

check-formatting:
	poetry run black --check .

format:
	poetry run black .

test:
	poetry run python -m unittest

run:
	poetry run solve-all

