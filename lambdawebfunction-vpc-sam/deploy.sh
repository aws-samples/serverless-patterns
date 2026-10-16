#!/usr/bin/env bash
#
# deploy.sh — one-command deploy for the lambdawebfunction-vpc-sam pattern.
#
# Lambda Web Functions can only be deployed from a .zip object in Amazon S3 (there is
# no inline-code or source-directory path), so this script packages src/, uploads it to
# S3, captures the object version, and runs sam build + sam deploy with the parameters
# wired for you. Re-run it to ship new code (each run creates a new immutable revision).
#
# This pattern also needs your VPC networking details: the subnets and security groups
# where Lambda provisions the network-connector ENIs. There are no safe defaults, so
# --vpc-id and --subnets are REQUIRED. --security-groups is OPTIONAL: omit it and the
# stack creates an egress-only security group for you; pass your own to bring your own.
#
# Usage:
#   ./deploy.sh --vpc-id vpc-aaa --subnets subnet-aaa,subnet-bbb \
#               [--security-groups sg-aaa,sg-bbb] \
#               [--stack-name NAME] [--bucket BUCKET] [--key KEY] \
#               [--network-protocol IPv4|DualStack] [--region REGION]
#
# Defaults:
#   stack name       : lambdawebfunction-vpc
#   bucket           : <stack-name>-code-<account-id>-<region>   (auto-created if missing)
#   key              : web-function/app.zip
#   network protocol : IPv4
#   region           : --region flag → $AWS_REGION → $AWS_DEFAULT_REGION → aws configure get region → error
#
set -euo pipefail

# ----- defaults -------------------------------------------------------------
STACK_NAME="lambdawebfunction-vpc"
CODE_KEY="web-function/app.zip"
CODE_BUCKET=""
REGION_FLAG=""
VPC_ID=""
SUBNET_IDS=""
SG_IDS=""
NETWORK_PROTOCOL="IPv4"
INTERNAL_TARGET_URL=""

# ----- parse args -----------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --stack-name)       STACK_NAME="$2"; shift 2;;
    --bucket)           CODE_BUCKET="$2"; shift 2;;
    --key)              CODE_KEY="$2"; shift 2;;
    --region)           REGION_FLAG="$2"; shift 2;;
    --vpc-id)           VPC_ID="$2"; shift 2;;
    --subnets)          SUBNET_IDS="$2"; shift 2;;
    --security-groups)  SG_IDS="$2"; shift 2;;
    --network-protocol) NETWORK_PROTOCOL="$2"; shift 2;;
    --internal-target-url) INTERNAL_TARGET_URL="$2"; shift 2;;
    -h|--help)          grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "Unknown argument: $1" >&2; exit 1;;
  esac
done

# ----- required VPC inputs --------------------------------------------------
# --security-groups is optional: when omitted, the stack creates an egress-only SG.
if [[ -z "${VPC_ID}" || -z "${SUBNET_IDS}" ]]; then
  echo "ERROR: --vpc-id and --subnets are required." >&2
  echo "  e.g. ./deploy.sh --vpc-id vpc-aaa --subnets subnet-aaa,subnet-bbb" >&2
  exit 1
fi

case "${NETWORK_PROTOCOL}" in
  IPv4|DualStack) ;;
  *) echo "ERROR: --network-protocol must be IPv4 or DualStack (got '${NETWORK_PROTOCOL}')." >&2; exit 1;;
esac

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
echo "==> Subnets:    ${SUBNET_IDS}"
echo "==> SGs:        ${SG_IDS}"
echo "==> Protocol:   ${NETWORK_PROTOCOL}"

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
  # Block all public access and enforce default encryption on the code bucket.
  aws s3api put-public-access-block --bucket "${CODE_BUCKET}" --region "${REGION}" \
    --public-access-block-configuration \
    BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true
  aws s3api put-bucket-encryption --bucket "${CODE_BUCKET}" --region "${REGION}" \
    --server-side-encryption-configuration \
    '{"Rules":[{"ApplyServerSideEncryptionByDefault":{"SSEAlgorithm":"AES256"},"BucketKeyEnabled":true}]}'
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
# Build parameter overrides. VpcSecurityGroupIds is only included when the user
# supplied security groups -- passing an empty "VpcSecurityGroupIds=" is rejected by
# SAM's --parameter-overrides parser. Omitting it lets the template default ('') apply,
# which triggers the stack to create an egress-only security group.
PARAM_OVERRIDES=(
  "CodeBucket=${CODE_BUCKET}"
  "CodeKey=${CODE_KEY}"
  "CodeVersionId=${CODE_VERSION_ID}"
  "VpcId=${VPC_ID}"
  "VpcSubnetIds=${SUBNET_IDS}"
  "NetworkProtocol=${NETWORK_PROTOCOL}"
)
if [[ -n "${SG_IDS}" ]]; then
  PARAM_OVERRIDES+=("VpcSecurityGroupIds=${SG_IDS}")
fi
if [[ -n "${INTERNAL_TARGET_URL}" ]]; then
  PARAM_OVERRIDES+=("InternalTargetUrl=${INTERNAL_TARGET_URL}")
fi

sam deploy \
  --stack-name "${STACK_NAME}" \
  --region "${REGION}" \
  --capabilities CAPABILITY_IAM \
  --resolve-s3 \
  --no-confirm-changeset \
  --no-fail-on-empty-changeset \
  --parameter-overrides "${PARAM_OVERRIDES[@]}"

echo
echo "==> Done. Stack outputs:"
aws cloudformation describe-stacks --stack-name "${STACK_NAME}" --region "${REGION}" \
  --query "Stacks[0].Outputs" --output table
