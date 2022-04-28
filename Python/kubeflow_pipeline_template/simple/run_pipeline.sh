#!/usr/bin/env bash

set -euf -o pipefail

if [[ -z "$VARIABLE_NAME" ]]; then
    echo "error - this script requires {VARIABLE}."
    exit 1
fi


echo "Running pipeline."
python3 pipeline.py \
  --variable-name $VARIABLE_NAME \
  
echo "Completed running pipeline. Check Kubeflow Experiments page."
