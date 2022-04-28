## MAKE SURE TO INSTALL BLACK, PYLINT WITH PIPENV

## FOR TESTING, INCLUDE UNITTEST FOLDER FOR TESTING
# CI Commands
build:
	bash build.sh

push:
	bash push.sh

static-checks: test check-format lint

test:
	pipenv run python -m unittest discover

check-format:
	pipenv run python -m black --check .

# Development Commands
format:
	pipenv run python -m black .

lint:
	pipenv run pylint -E */*.py
