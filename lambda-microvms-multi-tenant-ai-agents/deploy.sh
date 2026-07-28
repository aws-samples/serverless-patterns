#!/usr/bin/env bash
# End-to-end deploy for multi-tenant OpenClaw on Lambda MicroVMs.
#
# CloudFormation does almost everything — including the MicroVM image and the VPC egress
# connector, which ARE native CFN resources (AWS::Lambda::MicrovmImage /
# AWS::Lambda::NetworkConnector). The only thing CFN can't do is put *bytes* in S3, so this
# script's imperative part is just: ensure a bucket + upload the two zips. Then one
# `cloudformation deploy` builds the image, provisions the connector, and wires the
# orchestrator Lambda via GetAtt.
#
# Prereqs: AWS CLI v2 >= 2.35 (has the lambda-microvms models), python3, uv (or a modern
# pip), zip. Credentials for a MicroVMs launch region with Bedrock Claude access.
#
# Usage:  ./deploy.sh [REGION] [STACK_NAME]   (both optional; sensible defaults)
#   e.g.  ./deploy.sh                     -> us-east-1 / openclaw-mt
#         ./deploy.sh eu-west-1           -> eu-west-1 / openclaw-mt
#         ./deploy.sh eu-west-1 mystack   -> eu-west-1 / mystack
# Region is first: switching region is far more common than renaming the stack.
set -euo pipefail

REGION="${1:-us-east-1}"
STACK="${2:-openclaw-mt}"
HERE="$(cd "$(dirname "$0")" && pwd)"

say(){ printf '\n\033[1;36m== %s ==\033[0m\n' "$*"; }

# ---------- 0. Pre-flight (fail fast, before anything is created) ----------
say "0/4 Pre-flight checks"
if ! aws lambda-microvms help >/dev/null 2>&1; then
  echo "ERROR: this AWS CLI has no 'lambda-microvms' subcommands (needs AWS CLI v2 >= 2.35)."
  echo "       installed: $(aws --version 2>&1)"
  exit 1
fi
# Cheap read against the target region: catches not-yet-launched regions (the launch
# list keeps growing — probe instead of hardcoding it) and missing credentials.
if ! ERR="$(aws lambda-microvms list-microvms --region "$REGION" 2>&1 >/dev/null)"; then
  echo "ERROR: Lambda MicroVMs isn't reachable in region '$REGION':"
  printf '       %s\n' "$ERR"
  echo "       If the service hasn't launched in '$REGION' yet, use a launch region and re-run."
  exit 1
fi
echo "  aws cli ok; region '$REGION' ok"

ACCOUNT="$(aws sts get-caller-identity --query Account --output text)"
# Gateway token: explicit $GATEWAY_TOKEN wins; otherwise reuse .gateway-token, minting
# it once per checkout (random) so redeploys are idempotent and no shared default ships.
TOKEN_FILE="$HERE/.gateway-token"
if [ -z "${GATEWAY_TOKEN:-}" ]; then
  [ -f "$TOKEN_FILE" ] || openssl rand -hex 16 > "$TOKEN_FILE"
  GATEWAY_TOKEN="$(cat "$TOKEN_FILE")"
  TOKEN_NOTE="(kept in ${TOKEN_FILE#$HERE/}; redeploys reuse it)"
else
  TOKEN_NOTE="(from \$GATEWAY_TOKEN)"
fi
BUCKET="${STACK}-artifact-${ACCOUNT}-${REGION}"
# S3 keys carry a content hash: CloudFormation only rebuilds the MicroVM image /
# updates the Lambda when a resource PROPERTY changes, so a fixed key means code
# changes silently never reach AWS on redeploy. Hash of the inputs fixes that
# (and makes an unchanged redeploy a true no-op).
IMG_SRC="Dockerfile openclaw.json hooks.py start.sh efs-monitor.sh gw-bridge.cjs materialize-models.mjs"
IMG_HASH="$(cd "$HERE/src/microvm" && cat $IMG_SRC | shasum -a 256 | cut -c1-12)"
IMG_KEY="microvm-images/openclaw-${IMG_HASH}.zip"
CODE_HASH="$(shasum -a 256 "$HERE/src/orchestrator/handler.py" | cut -c1-12)"
CODE_KEY="lambda/orchestrator-${CODE_HASH}.zip"

# ---------- 1. Artifact bucket (the one imperative prerequisite) ----------
say "1/4 Ensure artifact bucket: $BUCKET"
if ! aws s3api head-bucket --bucket "$BUCKET" 2>/dev/null; then
  if [ "$REGION" = "us-east-1" ]; then
    aws s3api create-bucket --bucket "$BUCKET" --region "$REGION" >/dev/null
  else
    aws s3api create-bucket --bucket "$BUCKET" --region "$REGION" \
      --create-bucket-configuration LocationConstraint="$REGION" >/dev/null
  fi
  aws s3api put-public-access-block --bucket "$BUCKET" \
    --public-access-block-configuration BlockPublicAcls=true,BlockPublicPolicy=true,IgnorePublicAcls=true,RestrictPublicBuckets=true
fi

# ---------- 2. MicroVM image artifact (Dockerfile + app) ----------
say "2/4 Package & upload MicroVM image artifact ($IMG_KEY)"
IMGZIP="$(mktemp -d)/microvm.zip"
( cd "$HERE/src/microvm" && zip -j -q "$IMGZIP" $IMG_SRC )
aws s3 cp "$IMGZIP" "s3://${BUCKET}/${IMG_KEY}" --region "$REGION"

# ---------- 3. Orchestrator Lambda zip (boto3 + lambda-microvms model overlay + handler) ----------
say "3/4 Bundle & upload orchestrator Lambda"
PKG="$(mktemp -d)"
if command -v uv >/dev/null 2>&1; then
  uv pip install --quiet --python "$(command -v python3)" --target "$PKG" boto3
else
  python3 -m pip install --quiet --upgrade --target "$PKG" boto3 \
    || { echo "ERROR: install uv (https://docs.astral.sh/uv/) or a recent pip"; exit 1; }
fi
# PyPI boto3 may lag the lambda-microvms service model; overlay it from the local AWS CLI's
# botocore data (the CLI ships it — that's how this very script calls the service).
CLI_DATA="$(python3 - "$(readlink "$(command -v aws)" || command -v aws)" <<'PY'
import os,sys,glob
root=os.path.realpath(sys.argv[1])
for _ in range(6):
    root=os.path.dirname(root)
    hit=glob.glob(os.path.join(root,'**','botocore','data','lambda-microvms'),recursive=True)
    if hit: print(os.path.dirname(hit[0])); break
PY
)"
if [ -n "$CLI_DATA" ] && [ -d "$PKG/botocore/data" ]; then
  cp -R "$CLI_DATA/lambda-microvms" "$PKG/botocore/data/" 2>/dev/null || true
  cp -R "$CLI_DATA/lambda-core"     "$PKG/botocore/data/" 2>/dev/null || true
fi
# Hard gate: the bundle MUST contain the model, or the orchestrator only fails at invoke
# time with an unrelated-looking UnknownServiceError. Fail the deploy here instead.
if ! python3 -c "import sys;sys.path.insert(0,'$PKG');import boto3;assert 'lambda-microvms' in boto3.session.Session().get_available_services();print('  boto3',boto3.__version__,'+ lambda-microvms model')" 2>/dev/null; then
  echo "ERROR: couldn't get the 'lambda-microvms' service model into the Lambda bundle."
  echo "       Bundled boto3 lacks it, and extracting it from the local AWS CLI failed"
  echo "       (CLI data dir found: '${CLI_DATA:-none}')."
  echo "       Fix: install AWS CLI v2 >= 2.35 via the official installer, or upgrade"
  echo "       boto3 on PyPI to a version that ships the lambda-microvms model."
  exit 1
fi
cp "$HERE/src/orchestrator/handler.py" "$PKG/"
CODEZIP="$(mktemp -d)/orchestrator.zip"; ( cd "$PKG" && zip -q -r "$CODEZIP" . )
echo "  code key: $CODE_KEY"
aws s3 cp "$CODEZIP" "s3://${BUCKET}/${CODE_KEY}" --region "$REGION"

# ---------- 4. One CloudFormation deploy: builds image, connector, everything, wired ----------
say "4/4 CloudFormation deploy (builds MicroVM image ~5min + connector + all infra)"
aws cloudformation deploy --region "$REGION" --stack-name "$STACK" \
  --template-file "$HERE/template.yaml" \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
      ProjectName="$STACK" \
      GatewayToken="$GATEWAY_TOKEN" \
      ArtifactBucketName="$BUCKET" \
      MicrovmImageKey="$IMG_KEY" \
      OrchestratorCodeKey="$CODE_KEY"

API="$(aws cloudformation describe-stacks --region "$REGION" --stack-name "$STACK" \
  --query "Stacks[0].Outputs[?OutputKey=='ApiEndpoint'].OutputValue" --output text)"

say "DONE"
cat <<EOF

  API endpoint : ${API}
  Gateway token: ${GATEWAY_TOKEN}  ${TOKEN_NOTE}
  Add a tenant : ./add-tenant.sh ${REGION} ${STACK} <tenantId> [telegramBotToken] [webhookSecret]
  Test (chat)  : ./chat.sh ${REGION} ${STACK} <tenantId> "your message"
  Teardown     : ./teardown.sh ${REGION} ${STACK}
EOF
