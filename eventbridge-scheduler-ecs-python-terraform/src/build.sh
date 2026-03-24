#!/bin/bash
# Build script for the EventBridge ECS cron job container

set -e

# Configuration
IMAGE_NAME="eventbridge-ecs-cron"
IMAGE_TAG="${1:-latest}"
FULL_IMAGE_NAME="${IMAGE_NAME}:${IMAGE_TAG}"

echo "Building Docker image: ${FULL_IMAGE_NAME}"

# Build the Docker image
docker build -t "${FULL_IMAGE_NAME}" .

echo "Build completed successfully!"
echo "Image: ${FULL_IMAGE_NAME}"

# Show image details
echo ""
echo "Image details:"
docker images "${IMAGE_NAME}" --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"

echo ""
echo "To run the container locally:"
echo "docker run --rm ${FULL_IMAGE_NAME}"
echo ""
echo "To run with environment variables:"
echo "docker run --rm --env-file .env ${FULL_IMAGE_NAME}"