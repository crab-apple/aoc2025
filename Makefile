.PHONY: check-formatting format test run all

all: check-formatting run

check-formatting:
	poetry run black --check .

format:
	poetry run black .

run:
	poetry run solve-all

