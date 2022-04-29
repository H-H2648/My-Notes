install-dependencies-ci:
	pipenv install --deploy --dev

static-checks-ci: test check-format lint

test:
	echo "not implemented"

check-format:
	pipenv run python -m black --check .

# Development Commands
format:
	pipenv run python -m black .

lint:
	pipenv run pylint -E */*.py

# CICD won't fail because of linting
lint-test:
	pipenv run pylint --fail-under=0 dataflow

build:
	bash build.sh

push:
	bash push.sh

static-checks: check-format lint-test
