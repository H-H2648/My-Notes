Have the following when setting up a big project (involving docker containers, testing, etc.).

**Makefile**:

```
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
```

For information on build and push, check Docker (PROVIDE LINK HERE)

For information on test, check Unit Testing (PROVIDE LINK HERE)

For information on check-format and format, check Black (PROVIDE LINK HERE)

For information on lint, check PyLint (PROVIDE LINK HERE)

**Dockerfile**

```
FROM python:3.7-slim-stretch

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install pipenv

COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock
RUN pipenv install --deploy --system

COPY ./src ./src

```

Please get pipenv (PROVIDE LINK HERE)

**build.sh**
```
set -euf -o pipefail

SERVICE_NAME={Directory of where you want the docker image in GCS}

git_sha=$(git rev-parse --short HEAD)
timestamp=$(date "+%Y%m%d%H%M")
versioned_tag="${timestamp}-${git_sha}"
local_name="$SERVICE_NAME:${versioned_tag}"

docker build -t $local_name .

echo $versioned_tag
```

**push.sh**
```
#!/bin/bash -e

SERVICE_NAME={Directory of where you want the docker image in GCS}
GOOGLE_PROJECT_ID={Your Google Project id}

if [[ -z $1 ]]
then
  echo "versioned_tag argument for image is unset"
  # Get the latest created image TAG for $SERVICE_NAME
  versioned_tag=$(docker images --format "{{.Tag}}\t{{.CreatedAt}}" $SERVICE_NAME | sort -k 2 -h | tail -n 1 | awk '{print $1;}')
  if [[ -z $versioned_tag ]]
  then
    echo "no latest image found for $SERVICE_NAME"
    exit 1
  else
    echo "using latest found version image for $SERVICE_NAME: $versioned_tag"
  fi
else
  versioned_tag=$1
fi

set -euf -o pipefail

local_name="${SERVICE_NAME}:${versioned_tag}"
HOST="us.gcr.io/${GOOGLE_PROJECT_ID}"
host_name_versioned="$HOST/$SERVICE_NAME:$versioned_tag"
echo "Pushing $local_name to location: $host_name_versioned"
docker tag $local_name $host_name_versioned
docker push $host_name_versioned

host_name_latest="$HOST/$SERVICE_NAME:latest"
echo "Pushing $local_name to location: $host_name_latest"
docker tag $local_name $host_name_latest
docker push $host_name_latest
# clean up hosted latest image
docker image rm $host_name_latest

```