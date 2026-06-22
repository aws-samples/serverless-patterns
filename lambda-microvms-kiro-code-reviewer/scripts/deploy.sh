#!/bin/bash
# Deploy the AWS Lambda MicroVMs Kiro code reviewer sample application.
#
# Prerequisites:
#   - AWS CLI v2 with lambda-microvms subcommand available
#   - KIRO_API_KEY environment variable set with your Kiro API key
#
# This script:
#   1. Creates a staging S3 bucket and uploads the MicroVM app artifact
#   2. Creates a Secrets Manager secret and stores the Kiro API Key
#   3. Deploys the CloudFormation stack (IAM roles, log group, CodeCommit repo,
#      MicroVM image — all in a single deploy)
#   4. Exports stack outputs as environment variables
#
# Usage:
#   export KIRO_API_KEY="your-kiro-api-key"
#   ./scripts/deploy.sh [stack-name] [region]
#
# Example:
#   export KIRO_API_KEY="kiro_xxxxxxxxxxxx"
#   ./scripts/deploy.sh kiro-reviewer us-east-2

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
MICROVM_APP_DIR="$PROJECT_ROOT/src/microvm-app"

STACK_NAME="${1}"
REGION="${2}"

# Derived names
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
STAGING_BUCKET="${STACK_NAME}-staging-${ACCOUNT_ID}"
ARTIFACT_KEY="microvm-app/artifact.zip"
SECRET_NAME="${STACK_NAME}/kiro-api-key"

# ── Validate prerequisites ────────────────────────────────────────────────────

if [ -z "${KIRO_API_KEY:-}" ]; then
  echo "ERROR: KIRO_API_KEY environment variable is not set."
  echo ""
  echo "Set it with:"
  echo "  export KIRO_API_KEY=\"your-kiro-api-key\""
  echo ""
  exit 1
fi

echo "============================================"
echo "Deploying AWS Lambda MicroVM Kiro Code Reviewer"
echo "============================================"
echo ""
echo "Stack:          $STACK_NAME"
echo "Region:         $REGION"
echo "Account:        $ACCOUNT_ID"
echo "Staging Bucket: $STAGING_BUCKET"
echo ""

# ── Step 1: Create staging bucket and upload artifact ─────────────────────────

echo "--- Step 1: Create staging bucket and upload artifact ---"

# Create bucket if it doesn't exist
if ! aws s3api head-bucket --bucket "$STAGING_BUCKET" --region "$REGION" 2>/dev/null; then
  echo "Creating staging bucket: $STAGING_BUCKET"
  aws s3api create-bucket \
    --bucket "$STAGING_BUCKET" \
    --region "$REGION" \
    --create-bucket-configuration LocationConstraint="$REGION"
  aws s3api put-public-access-block \
    --bucket "$STAGING_BUCKET" \
    --region "$REGION" \
    --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
else
  echo "Staging bucket already exists: $STAGING_BUCKET"
fi

# Package and upload artifact
ARTIFACT_ZIP="/tmp/microvm-artifact.zip"
rm -f "$ARTIFACT_ZIP"
cd "$MICROVM_APP_DIR"
zip -r "$ARTIFACT_ZIP" Dockerfile app.py requirements.txt
echo "Created: $ARTIFACT_ZIP"

aws s3 cp "$ARTIFACT_ZIP" "s3://$STAGING_BUCKET/$ARTIFACT_KEY" --region "$REGION"
echo "Uploaded to s3://$STAGING_BUCKET/$ARTIFACT_KEY"
echo ""

# ── Step 2: Create secret and store Kiro API Key ─────────────────────────────

echo "--- Step 2: Create secret and store Kiro API Key ---"

# Create or update the secret
KIRO_SECRET_ARN=$(aws secretsmanager describe-secret \
  --secret-id "$SECRET_NAME" \
  --region "$REGION" \
  --query "ARN" --output text 2>/dev/null || echo "")

if [ -z "$KIRO_SECRET_ARN" ]; then
  echo "Creating secret: $SECRET_NAME"
  KIRO_SECRET_ARN=$(aws secretsmanager create-secret \
    --name "$SECRET_NAME" \
    --description "Kiro API Key for Lambda MicroVMs code reviewer sample" \
    --secret-string "$KIRO_API_KEY" \
    --region "$REGION" \
    --query "ARN" --output text)
else
  echo "Secret already exists, updating value..."
  aws secretsmanager put-secret-value \
    --secret-id "$KIRO_SECRET_ARN" \
    --secret-string "$KIRO_API_KEY" \
    --region "$REGION"
fi

echo "Kiro Secret ARN: $KIRO_SECRET_ARN"
echo ""
# ── Step 3: Deploy CloudFormation stack ───────────────────────────────────────

echo "--- Step 3: Deploy CloudFormation stack ---"
cd "$PROJECT_ROOT"
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name "$STACK_NAME" \
  --region "$REGION" \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    StackLabel="$STACK_NAME" \
    StagingBucket="$STAGING_BUCKET" \
    ArtifactKey="$ARTIFACT_KEY" \
    KiroSecretArn="$KIRO_SECRET_ARN" \
  --no-fail-on-empty-changeset
echo "CloudFormation stack deployed."
echo ""

# ── Step 4: Retrieve stack outputs ────────────────────────────────────────────

echo "--- Step 4: Retrieve stack outputs ---"

get_output() {
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$REGION" \
    --query "Stacks[0].Outputs[?OutputKey==\`$1\`].OutputValue" \
    --output text
}

export IMAGE_ARN=$(get_output "MicroVMImageArn")
export EXECUTION_ROLE_ARN=$(get_output "MicroVMExecutionRoleArn")
export REPO_NAME=$(get_output "CodeReviewRepoName")
export REPO_CLONE_URL=$(get_output "CodeReviewRepoCloneUrl")
export PR_ID=$(get_output "PullRequestId")
export SOURCE_COMMIT=$(get_output "SourceCommitId")
export DESTINATION_COMMIT=$(get_output "DestinationCommitId")

echo "Image ARN:          $IMAGE_ARN"
echo "Execution Role ARN: $EXECUTION_ROLE_ARN"
echo "Repo Name:          $REPO_NAME"
echo "PR ID:              $PR_ID"
echo "Source Commit:      $SOURCE_COMMIT"
echo "Destination Commit: $DESTINATION_COMMIT"
echo ""

# ── Summary ───────────────────────────────────────────────────────────────────

echo "============================================"
echo "Deployment Complete!"
echo "============================================"
echo ""
echo "The following environment variables are now exported:"
echo ""
echo "  export IMAGE_ARN=\"$IMAGE_ARN\""
echo "  export EXECUTION_ROLE_ARN=\"$EXECUTION_ROLE_ARN\""
echo "  export REPO_NAME=\"$REPO_NAME\""
echo "  export PR_ID=\"$PR_ID\""
echo "  export SOURCE_COMMIT=\"$SOURCE_COMMIT\""
echo "  export DESTINATION_COMMIT=\"$DESTINATION_COMMIT\""
echo "  export REGION=\"$REGION\""
echo ""
echo "To test the Kiro Code Reviewer, run a MicroVM and send a review request."
echo "See the README for the full curl command."
echo ""
