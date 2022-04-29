#!/bin/bash -e

# should be consistent with SERVICE_NAME in build.sh
SERVICE_NAME=SOME_SERVICE
GCR_PROJECT_ID=SOME_PROJECT
GCR_FOLDER=S0ME_FOLDER

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
HOST="us.gcr.io/${GCR_PROJECT_ID}/${GCR_FOLDER}"
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
