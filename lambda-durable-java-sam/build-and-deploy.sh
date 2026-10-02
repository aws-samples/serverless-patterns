#!/bin/bash
set -e

echo "============================================================"
echo "  Lambda Durable Functions Java - Build and Deploy"
echo "============================================================"

AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
AWS_REGION=${AWS_REGION:-$(aws configure get region)}
ECR_REPO="durable-functions-java-examples"
IMAGE_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:latest"

echo ""
echo "AWS Account: $AWS_ACCOUNT_ID"
echo "Region: $AWS_REGION"
echo "ECR Image: $IMAGE_URI"
echo ""

# Step 1: Build the durable functions JAR
echo ">>> Step 1: Building durable functions JAR..."
cd durable-functions-sam/durable-functions
mvn clean package
echo "    Build complete."

# Step 2: Build Docker image
echo ""
echo ">>> Step 2: Building Docker image..."
docker build --platform linux/amd64 --provenance=false -t $ECR_REPO .
echo "    Docker image built."

# Step 3: Delete and recreate ECR repository
echo ""
echo ">>> Step 3: Recreating ECR repository..."
aws ecr delete-repository --repository-name $ECR_REPO --force 2>/dev/null || true
aws ecr create-repository --repository-name $ECR_REPO
echo "    Repository created."

# Step 4: Login to ECR and push
echo ""
echo ">>> Step 4: Pushing image to ECR..."
aws ecr get-login-password --region $AWS_REGION \
  | docker login --username AWS --password-stdin \
    $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

docker tag $ECR_REPO:latest $IMAGE_URI
docker push $IMAGE_URI
echo "    Image pushed."

# Step 5: Deploy SAM stack
echo ""
echo ">>> Step 5: Deploying SAM stack..."
cd ..
sam deploy \
  --template-file template.yaml \
  --stack-name durable-functions-java-examples \
  --capabilities CAPABILITY_NAMED_IAM \
  --no-confirm-changeset \
  --resolve-image-repos

# Step 6: Build the SNS sender
echo ""
echo ">>> Step 6: Building SNS message sender..."
cd ../sns-message-sender
mvn clean package
echo "    SNS sender built."

echo ""
echo "============================================================"
echo "  Deployment Complete!"
echo "============================================================"
echo ""
echo "To trigger a pattern, run:"
echo "  cd sns-message-sender"
echo "  java -cp target/sns-message-sender-1.0-SNAPSHOT.jar sns.producer.DurableFunctionsTrigger DurableFunctionsSNSTopic <pattern>"
echo ""
echo "Available patterns: chaining, fanout, approval, monitoring, timer, errorhandling, mapprocessing, suborchestration"
echo ""
