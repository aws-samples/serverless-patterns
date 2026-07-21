#!/usr/bin/env bash
# Tear down everything. CloudFormation now owns the MicroVM image and the VPC egress
# connector, so it removes those itself — we only have to (a) terminate running MicroVMs
# first (they're created imperatively by the orchestrator at runtime, NOT stack-managed,
# and their ENIs/connector use would block stack deletion), then (b) delete the stack,
# then (c) empty & drop the artifact bucket (also not stack-managed).
# Usage: ./teardown.sh [REGION] [STACK]   (region first; both default to us-east-1 / openclaw-mt)
#   e.g. ./teardown.sh eu-west-1 mystack
set -uo pipefail
REGION="${1:-us-east-1}"; STACK="${2:-openclaw-mt}"
ACCOUNT="$(aws sts get-caller-identity --query Account --output text)"
BUCKET="${STACK}-artifact-${ACCOUNT}-${REGION}"
say(){ printf '\n== %s ==\n' "$*"; }

say "1. terminate THIS stack's running MicroVMs (runtime-created, not stack-managed)"
# MicroVM instances carry no stack tag, but get-microvm returns imageArn, and this stack's
# image is named "<STACK>-openclaw" (see MicrovmImage.Name in template.yaml). Filter on that
# so we never terminate VMs belonging to another stack sharing the account/region.
IMAGE_SUFFIX=":microvm-image:${STACK}-openclaw"
found=0
for id in $(aws lambda-microvms list-microvms --region "$REGION" \
              --query "items[?state!='TERMINATED'].microvmId" --output text 2>/dev/null); do
  arn="$(aws lambda-microvms get-microvm --region "$REGION" --microvm-identifier "$id" \
           --query imageArn --output text 2>/dev/null)"
  case "$arn" in
    *"$IMAGE_SUFFIX") echo "  terminate $id (image: ${arn##*:})"; found=1
      aws lambda-microvms terminate-microvm --region "$REGION" --microvm-identifier "$id" >/dev/null 2>&1 || true ;;
    *) echo "  skip $id (image: ${arn##*:} — not this stack)" ;;
  esac
done
# let ENIs from the connector detach before CFN tries to delete the SG/subnet
[ "$found" = 1 ] && sleep 20 || true

say "2. delete CloudFormation stack (removes image, connector, EFS, VPC, IAM, DDB, Lambda, API)"
aws cloudformation delete-stack --region "$REGION" --stack-name "$STACK"
echo "  waiting for delete to complete..."
if aws cloudformation wait stack-delete-complete --region "$REGION" --stack-name "$STACK" 2>/dev/null; then
  echo "  stack deleted"
else
  echo "  NOTE: if delete stalled on the VPC/SG, a MicroVM or the connector's ENIs may still"
  echo "  be detaching. Re-run this script; CloudFormation delete is idempotent."
fi

say "3. empty & delete artifact bucket"
aws s3 rm "s3://$BUCKET" --recursive >/dev/null 2>&1 || true
aws s3api delete-bucket --bucket "$BUCKET" --region "$REGION" >/dev/null 2>&1 || true
echo "DONE"
