#!/bin/bash

DIR=$(echo $(cd $(dirname "${BASH_SOURCE[0]}") && pwd -P))
ROOT_DIR=$(echo $(cd $(dirname "${BASH_SOURCE[0]}")/.. && pwd -P))

docker build -t etcd3/buf -f "${DIR}/Dockerfile" "$DIR"

#
# Note the HOME funny stuff. The `buf` tool needs to create a .cache directory. It tries
# to do that under HOME and if HOME is not set then under root dir. Now, since the container does not
# run as root, it will not be able to create that directory. Setting HOME env var to a writable directory
# works this around.
#

echo "+---------------------------------------------------------------------+"
echo "| Running dockerized buf (https://github.com/bufbuild/buf)            |"
echo "+---------------------------------------------------------------------+"

docker run \
  --user $(id -u):$(id -g) \
  --volume "${ROOT_DIR}:/workspace" \
  --workdir /workspace \
  --env HOME=/tmp \
  etcd3/buf \
  generate
