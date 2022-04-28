static-checks: check-format lint

# Development Commands
format:
	pipenv run python -m black .
	
check-format:
	pipenv run python -m black --check .

lint:
	pipenv run pylint -E *.py
