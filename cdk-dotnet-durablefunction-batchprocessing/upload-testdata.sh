#!/usr/bin/env bash
set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
# upload-testdata.sh
#
# Uploads all files from ./testdata/ to the S3 bucket created by the CDK stack.
# Files are placed under the input/batch/ prefix which can then be passed to
# the durable function for processing.
#
# Usage:
#   ./upload-testdata.sh [STACK_NAME] [PREFIX]
#   STACK_NAME defaults to CdkDotnetDurablefunctionBatchprocessingStack
#   PREFIX defaults to input/batch/
# ──────────────────────────────────────────────────────────────────────────────

STACK_NAME="${1:-CdkDotnetDurablefunctionBatchprocessingStack}"
PREFIX="${2:-input/batch/}"
INPUT_DIR="testdata"

if [[ ! -d "$INPUT_DIR" ]]; then
    echo "✗ Directory ./${INPUT_DIR}/ not found. Run ./download-testdata.sh first." >&2
    exit 1
fi

FILE_COUNT=$(find "$INPUT_DIR" -type f | wc -l | tr -d ' ')
if [[ "$FILE_COUNT" -eq 0 ]]; then
    echo "✗ No files found in ./${INPUT_DIR}/. Run ./download-testdata.sh first." >&2
    exit 1
fi

echo "▶ Retrieving S3 bucket name from stack '${STACK_NAME}'..."
BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --query "Stacks[0].Outputs[?OutputKey=='FilesBucketName'].OutputValue" \
    --output text)

if [[ -z "$BUCKET_NAME" || "$BUCKET_NAME" == "None" ]]; then
    echo "✗ Could not find FilesBucketName output. Is the stack deployed?" >&2
    exit 1
fi

echo "  Bucket: ${BUCKET_NAME}"
echo "  Prefix: ${PREFIX}"
echo "  Files:  ${FILE_COUNT}"
echo ""
echo "▶ Uploading files to s3://${BUCKET_NAME}/${PREFIX}..."

aws s3 sync "$INPUT_DIR" "s3://${BUCKET_NAME}/${PREFIX}" \
    --content-type "text/csv" \
    --quiet

echo ""
echo "✓ Uploaded ${FILE_COUNT} files to s3://${BUCKET_NAME}/${PREFIX}"
echo ""
echo "To invoke the batch processor, run:"
echo ""

FUNCTION_ARN=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --query "Stacks[0].Outputs[?OutputKey=='BatchProcessorFunctionArn'].OutputValue" \
    --output text)

echo "  aws lambda invoke \\"
echo "      --function-name \"${FUNCTION_ARN}:\\\$LATEST\" \\"
echo "      --invocation-type Event \\"
echo "      --cli-binary-format raw-in-base64-out \\"
echo "      --payload '{\"Bucket\":\"${BUCKET_NAME}\",\"Prefix\":\"${PREFIX}\"}' \\"
echo "      /tmp/invoke-response.json"
