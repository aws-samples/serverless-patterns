#!/bin/bash

# Fail fast
set -e

# This is the order of arguments
ECR_BASE_ARN=${1}
BUILD_FOLDER=${2}
IMAGE_NAME=${3}
IMAGE_URI=${4}
TARGET_AWS_REGION=${5}
MYTAG=$(date +%Y%m%d%H%M%S)

# Check that git is installed
which git >/dev/null || {
    echo 'ERROR: git is not installed'
    exit 1
}

# Check that aws is installed
which aws >/dev/null || {
    echo 'ERROR: aws-cli is not installed'
    exit 1
}

# Check that docker is installed and running
which docker >/dev/null && docker ps >/dev/null || {
    echo 'ERROR: docker is not running'
    exit 1
}

# Connect into aws
aws ecr get-login-password --region ${TARGET_AWS_REGION} | docker login --username AWS --password-stdin ${ECR_BASE_ARN} || {
    echo 'ERROR: aws ecr login failed'
    exit 1
}

# Build image
docker build --no-cache -t ${IMAGE_NAME} ${BUILD_FOLDER} --platform linux/amd64

# Docker Tag and Push
docker tag ${IMAGE_NAME}:latest ${IMAGE_URI}:latest
docker tag ${IMAGE_URI}:latest ${IMAGE_URI}:${MYTAG}
docker push ${IMAGE_URI}:latest
docker push ${IMAGE_URI}:${MYTAG}

echo "Tags Used for ${IMAGE_NAME} Image are ${MYTAG}"
