#!/usr/bin/env bash
#
# deploy.sh — one-command deploy for the cloudfront-lambdawebfunction-oac-sam pattern.
#
# Lambda Web Functions can only be deployed from a .zip object in Amazon S3 (there is
# no inline-code or source-directory path), so this script packages src/, uploads it to
# S3, captures the object version, and runs sam build + sam deploy with the parameters
# wired for you. Re-run it to ship new code (each run creates a new immutable revision).
#
# Usage:
#   ./deploy.sh [--stack-name NAME] [--bucket BUCKET] [--key KEY] [--region REGION]
#
# All flags are optional. Defaults:
#   stack name : cloudfront-lambdawebfunction-oac
#   bucket     : <stack-name>-code-<account-id>-<region>   (auto-created if missing)
#   key        : web-function/app.zip
#   region     : --region flag → $AWS_REGION → $AWS_DEFAULT_REGION → aws configure get region → error
#
set -euo pipefail

# ----- defaults -------------------------------------------------------------
STACK_NAME="cloudfront-lambdawebfunction-oac"
CODE_KEY="web-function/app.zip"
CODE_BUCKET=""
REGION_FLAG=""

# ----- parse args -----------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --stack-name) STACK_NAME="$2"; shift 2;;
    --bucket)     CODE_BUCKET="$2"; shift 2;;
    --key)        CODE_KEY="$2"; shift 2;;
    --region)     REGION_FLAG="$2"; shift 2;;
    -h|--help)    grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "Unknown argument: $1" >&2; exit 1;;
  esac
done

# ----- resolve region (explicit precedence, fail fast) ----------------------
REGION="${REGION_FLAG:-${AWS_REGION:-${AWS_DEFAULT_REGION:-$(aws configure get region 2>/dev/null || true)}}}"
if [[ -z "${REGION}" ]]; then
  echo "ERROR: No AWS region. Pass --region, or set AWS_REGION / AWS_DEFAULT_REGION, or run 'aws configure'." >&2
  exit 1
fi

# Lambda Web Functions launch Regions (Oct 2026). Warn (don't block) if elsewhere.
case "${REGION}" in
  us-east-1|us-east-2|us-west-2|ap-northeast-1|eu-west-1) ;;
  *) echo "WARNING: ${REGION} is not a known Lambda Web Functions Region (us-east-1, us-east-2, us-west-2, ap-northeast-1, eu-west-1). Continuing anyway." >&2;;
esac

ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
if [[ -z "${CODE_BUCKET}" ]]; then
  CODE_BUCKET="${STACK_NAME}-code-${ACCOUNT_ID}-${REGION}"
fi

echo "==> Region:     ${REGION}"
echo "==> Account:    ${ACCOUNT_ID}"
echo "==> Stack:      ${STACK_NAME}"
echo "==> Code s3://  ${CODE_BUCKET}/${CODE_KEY}"

# ----- ensure the S3 bucket exists (with versioning) ------------------------
if aws s3api head-bucket --bucket "${CODE_BUCKET}" --region "${REGION}" 2>/dev/null; then
  echo "==> Bucket exists: ${CODE_BUCKET}"
else
  echo "==> Creating bucket: ${CODE_BUCKET}"
  if [[ "${REGION}" == "us-east-1" ]]; then
    # us-east-1 must NOT send a LocationConstraint.
    aws s3api create-bucket --bucket "${CODE_BUCKET}" --region "${REGION}"
  else
    aws s3api create-bucket --bucket "${CODE_BUCKET}" --region "${REGION}" \
      --create-bucket-configuration LocationConstraint="${REGION}"
  fi
  aws s3api put-bucket-versioning --bucket "${CODE_BUCKET}" \
    --versioning-configuration Status=Enabled --region "${REGION}"
fi

# ----- package src/ into app.zip (entry file at the zip root) ---------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ZIP_PATH="$(mktemp -d)/app.zip"
echo "==> Zipping src/ -> ${ZIP_PATH}"
( cd "${SCRIPT_DIR}/src" && zip -r -q "${ZIP_PATH}" . )

# ----- upload and capture the version id ------------------------------------
echo "==> Uploading to s3://${CODE_BUCKET}/${CODE_KEY}"
aws s3 cp "${ZIP_PATH}" "s3://${CODE_BUCKET}/${CODE_KEY}" --region "${REGION}"
CODE_VERSION_ID="$(aws s3api head-object --bucket "${CODE_BUCKET}" --key "${CODE_KEY}" \
  --region "${REGION}" --query VersionId --output text 2>/dev/null || echo "")"
[[ "${CODE_VERSION_ID}" == "None" ]] && CODE_VERSION_ID=""
echo "==> Object version: ${CODE_VERSION_ID:-<unversioned>}"

# ----- build & deploy -------------------------------------------------------
echo "==> sam build"
sam build

echo "==> sam deploy"
sam deploy \
  --stack-name "${STACK_NAME}" \
  --region "${REGION}" \
  --capabilities CAPABILITY_IAM \
  --resolve-s3 \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset \
  --parameter-overrides \
    CodeBucket="${CODE_BUCKET}" \
    CodeKey="${CODE_KEY}" \
    CodeVersionId="${CODE_VERSION_ID}"

echo
echo "==> Done. Stack outputs:"
aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${REGION}" \
  --query "Stacks[0].Outputs" --output table
