#!/bin/bash
set -e

# Configuration
AWS_REGION=${AWS_REGION:-us-east-1}
ECR_REPOSITORY_NAME=${ECR_REPOSITORY_NAME:-sqs-ecs-app}
IMAGE_TAG=${IMAGE_TAG:-1.0}

# Check if running on macOS
if [[ "$(uname)" == "Darwin" ]]; then
  echo "Running on macOS..."
  # Check for Apple Silicon
  if [[ "$(uname -m)" == "arm64" ]]; then
    echo "Apple Silicon detected, using platform flag for Docker build..."
    PLATFORM_FLAG="--platform linux/amd64"
  else
    PLATFORM_FLAG=""
  fi
else
  PLATFORM_FLAG=""
fi

# Create ECR repository if it doesn't exist
echo "Creating ECR repository if it doesn't exist..."
aws ecr describe-repositories --repository-names ${ECR_REPOSITORY_NAME} --region ${AWS_REGION} || \
  aws ecr create-repository --repository-name ${ECR_REPOSITORY_NAME} --region ${AWS_REGION}

# Get ECR login
echo "Logging in to ECR..."
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin $(aws sts get-caller-identity --query Account --output text).dkr.ecr.${AWS_REGION}.amazonaws.com

# Build the Docker image
echo "Building Docker image..."
docker build ${PLATFORM_FLAG} -t ${ECR_REPOSITORY_NAME}:${IMAGE_TAG} .

# Tag the image for ECR
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REPO_URI=${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY_NAME}
docker tag ${ECR_REPOSITORY_NAME}:${IMAGE_TAG} ${ECR_REPO_URI}:${IMAGE_TAG}

# Push the image to ECR
echo "Pushing image to ECR..."
docker push ${ECR_REPO_URI}:${IMAGE_TAG}

echo "Image URI: ${ECR_REPO_URI}:${IMAGE_TAG}"

sed -i '' "s|ECR_REPO_URI|$ECR_REPO_URI|g" template.yaml
sed -i '' "s|IMAGE_TAG|$IMAGE_TAG|g" template.yaml

echo "Done!"