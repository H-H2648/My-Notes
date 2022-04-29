set -euf -o pipefail

#SOME_SERVICE_NAME to repalce with actual service name
SERVICE_NAME=SOME_SERVICE_NAME


git_sha=$(git rev-parse --short HEAD)
timestamp=$(date "+%Y%m%d%H%M")
versioned_tag="${timestamp}-${git_sha}"
local_name="$SERVICE_NAME:${versioned_tag}"

docker build -t $local_name .

echo $versioned_tag
