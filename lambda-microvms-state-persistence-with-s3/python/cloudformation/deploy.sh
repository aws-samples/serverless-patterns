#!/usr/bin/env bash
#
# Deploy the Lambda MicroVMs state persistence with S3 demo.
#
# The S3 bucket must exist before the CloudFormation stack, because the MicroVM
# image's CodeArtifact.Uri points at the staged artifact. So this script:
#   1. Creates the S3 state/staging bucket (CLI).
#   2. Packages + uploads the MicroVM artifact (src/microvm/) and the middleware
#      Lambda zip (src/middleware/ + bundled boto3 + vendored SDK model).
#   3. Deploys template.yaml (image, IAM roles, DynamoDB, Lambda, API Gateway).
#   4. Prints the stack outputs (Middleware URL for the web UI).
#
# Configuration (env vars, all optional):
#   AWS_REGION    default us-east-1
#   STACK_NAME    default state-persistence-demo
#   STATE_BUCKET  default <STACK_NAME>-state-<accountId>
#   API_STAGE     default prod
#
# Usage:
#   ./deploy.sh
#   AWS_REGION=us-east-1 STACK_NAME=my-notes ./deploy.sh
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

AWS_REGION="${AWS_REGION:-us-east-1}"
STACK_NAME="${STACK_NAME:-state-persistence-demo}"
API_STAGE="${API_STAGE:-prod}"

command -v aws >/dev/null 2>&1 || { echo "ERROR: aws CLI not found on PATH"; exit 1; }

ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
[ -n "$ACCOUNT_ID" ] || { echo "ERROR: could not resolve AWS account (are you logged in?)"; exit 1; }

STATE_BUCKET="${STATE_BUCKET:-${STACK_NAME}-state-${ACCOUNT_ID}}"
ARTIFACT_KEY="microvm-app/artifact.zip"
# Middleware key is content-addressed (filled in after packaging) so a code
# change produces a new S3 key, which makes CloudFormation update the Lambda.
MIDDLEWARE_KEY=""

echo "============================================================"
echo " Deploying: $STACK_NAME"
echo "   region : $AWS_REGION"
echo "   account: $ACCOUNT_ID"
echo "   bucket : $STATE_BUCKET"
echo "============================================================"

# ── Step 1: S3 state/staging bucket ───────────────────────────────────────────
echo "==> [1/4] S3 bucket"
if aws s3api head-bucket --bucket "$STATE_BUCKET" --region "$AWS_REGION" 2>/dev/null; then
  echo "    bucket already exists"
else
  if [ "$AWS_REGION" = "us-east-1" ]; then
    aws s3api create-bucket --bucket "$STATE_BUCKET" --region "$AWS_REGION" >/dev/null
  else
    aws s3api create-bucket --bucket "$STATE_BUCKET" --region "$AWS_REGION" \
      --create-bucket-configuration "LocationConstraint=${AWS_REGION}" >/dev/null
  fi
  aws s3api put-public-access-block --bucket "$STATE_BUCKET" --region "$AWS_REGION" \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
  echo "    created"
fi

# ── Step 2: package + upload artifacts ─────────────────────────────────────────
echo "==> [2/4] Staging artifacts"

# MicroVM artifact: zip the self-contained src/microvm/ folder (Dockerfile at root).
ART_ZIP="$(mktemp -d)/artifact.zip"
( cd src/microvm && zip -rq "$ART_ZIP" . -x '*/__pycache__/*' '__pycache__/*' )
aws s3 cp "$ART_ZIP" "s3://${STATE_BUCKET}/${ARTIFACT_KEY}" --region "$AWS_REGION" >/dev/null
echo "    microvm artifact -> s3://${STATE_BUCKET}/${ARTIFACT_KEY}"

# Middleware Lambda: bundle the package + a current boto3/botocore (the runtime
# boto3 does not know the lambda-microvms service) + the vendored SDK model.
MW_BUILD="$(mktemp -d)"
cp -r "$HERE/src/middleware" "$MW_BUILD/middleware"
python3 -m pip install --quiet --target "$MW_BUILD" "boto3>=1.40.0" "botocore>=1.40.0" 2>&1 | tail -1 || {
  echo "ERROR: failed to install boto3/botocore into the middleware package"; exit 1; }
( cd "$MW_BUILD" && zip -qr middleware.zip . -x '*.sh' '*.md' '*.dist-info/*' '*/__pycache__/*' )
# Content-address the key so each distinct build is a new object → CFN sees a
# changed Code.S3Key and updates the function.
MW_HASH="$(shasum -a 256 "$MW_BUILD/middleware.zip" | cut -c1-12)"
MIDDLEWARE_KEY="middleware/middleware-${MW_HASH}.zip"
aws s3 cp "$MW_BUILD/middleware.zip" "s3://${STATE_BUCKET}/${MIDDLEWARE_KEY}" --region "$AWS_REGION" >/dev/null
echo "    middleware lambda -> s3://${STATE_BUCKET}/${MIDDLEWARE_KEY}"

# ── Step 3: deploy the CloudFormation stack ────────────────────────────────────
echo "==> [3/4] CloudFormation deploy"
# Always-passed overrides.
PARAM_OVERRIDES=(
  StackLabel="$STACK_NAME"
  StateBucket="$STATE_BUCKET"
  ArtifactKey="$ARTIFACT_KEY"
  MiddlewareKey="$MIDDLEWARE_KEY"
  ApiStageName="$API_STAGE"
)
# Optional security/cost controls — forwarded only when set, otherwise the
# template defaults apply (see the Security section of the README).
[ -n "${ALLOWED_ORIGINS:-}" ]                 && PARAM_OVERRIDES+=( AllowedOrigins="$ALLOWED_ORIGINS" )
[ -n "${MAX_LIVE_MICROVMS:-}" ]               && PARAM_OVERRIDES+=( MaxLiveMicrovms="$MAX_LIVE_MICROVMS" )
[ -n "${API_RATE_LIMIT:-}" ]                  && PARAM_OVERRIDES+=( ApiRateLimit="$API_RATE_LIMIT" )
[ -n "${API_BURST_LIMIT:-}" ]                 && PARAM_OVERRIDES+=( ApiBurstLimit="$API_BURST_LIMIT" )
[ -n "${MIDDLEWARE_RESERVED_CONCURRENCY:-}" ] && PARAM_OVERRIDES+=( MiddlewareReservedConcurrency="$MIDDLEWARE_RESERVED_CONCURRENCY" )

aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name "$STACK_NAME" \
  --region "$AWS_REGION" \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides "${PARAM_OVERRIDES[@]}" \
  --no-fail-on-empty-changeset

# ── Step 4: outputs ────────────────────────────────────────────────────────────
echo "==> [4/4] Stack outputs"
get_output() {
  aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$AWS_REGION" \
    --query "Stacks[0].Outputs[?OutputKey=='$1'].OutputValue" --output text
}
MIDDLEWARE_URL="$(get_output MiddlewareUrl)"
IMAGE_ARN="$(get_output MicroVMImageArn)"

echo
echo "============================================================"
echo " Deployment complete."
echo "   Middleware URL : $MIDDLEWARE_URL"
echo "   MicroVM image  : $IMAGE_ARN"
echo
echo " Use the Middleware URL as the 'Middleware URL' in the web UI."
echo " Serve the UI with:  (cd src/web && python3 -m http.server 5173)"
echo "============================================================"
