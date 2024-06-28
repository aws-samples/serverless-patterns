#!/bin/bash

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

# Check that docker is installed
which docker >/dev/null || {
    echo 'ERROR: docker is not installed'
    exit 1
}

# Connect into aws and login into ECR
SLEEP_INT=$((1 + RANDOM % 11))
for CTR in {1..5}; do
    
    # Check that docker is running
    docker ps >/dev/null 
    DOCKER_STATUS=$?
   
    # Check that ECR creds are obtained
    aws ecr get-login-password --region ${TARGET_AWS_REGION} | docker login --username AWS --password-stdin ${ECR_BASE_ARN}
    ECR_GET_CREDS_STATUS=$?

    if [ ${ECR_GET_CREDS_STATUS} -ne 0 ] || [ ${DOCKER_STATUS} -ne 0 ]; then
        echo "ERROR: aws ecr login failed, trying again in ${SLEEP_INT} Seconds"
        sleep ${SLEEP_INT}
        ((CTR=CTR+1))
        continue
    else   
        echo "SUCCESS: aws ecr login succeded in ${CTR} attempt"
        break
    fi
    exit 1
done

# Build image
docker build --no-cache -t ${IMAGE_NAME} ${BUILD_FOLDER} --platform linux/amd64 || {
    echo 'ERROR: docker build faied'
    exit 1
}

# Docker Tag and Push
docker tag ${IMAGE_NAME} ${IMAGE_URI}:${MYTAG}
docker push ${IMAGE_URI}:${MYTAG} || {
    echo 'ERROR: docker push faied'
    exit 1
}

# Get the sha of the image
SHA_IMAGE=$(docker inspect --format='{{.RepoDigests}}' ${IMAGE_URI}:${MYTAG})
echo "Tags Used for ${IMAGE_NAME} Image are ${MYTAG} with this SHA : ${SHA_IMAGE}"