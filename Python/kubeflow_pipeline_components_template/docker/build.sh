set -euf -o pipefail

#substitute appropriate service name for ENTER_SERVICE_NAME_HERE
SERVICE_NAME=ENTER_SERVICE_NAME_HERE

git_sha=$(git rev-parse --short HEAD)
timestamp=$(date "+%Y%m%d%H%M")
versioned_tag="${timestamp}-${git_sha}"
local_name="$SERVICE_NAME:${versioned_tag}"

docker build -t $local_name .

echo $versioned_tag
