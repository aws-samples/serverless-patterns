#!/usr/bin/env bash
set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
# generate-and-upload.sh
#
# Generates a test image locally and uploads it to the S3 bucket created
# by the CDK stack, then prints the command to invoke the durable function.
#
# Usage:
#   ./generate-and-upload.sh [STACK_NAME]
# ──────────────────────────────────────────────────────────────────────────────

STACK_NAME="${1:-CdkDotnetDurablefunctionImageprocessingStack}"
IMAGE_NAME="test-image-$(date +%s).png"
OUTPUT_FILE="/tmp/${IMAGE_NAME}"

echo "▶ Retrieving S3 bucket name from stack '${STACK_NAME}'..."
BUCKET_NAME=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --query "Stacks[0].Outputs[?OutputKey=='ImagesBucketName'].OutputValue" \
    --output text)

if [[ -z "$BUCKET_NAME" || "$BUCKET_NAME" == "None" ]]; then
    echo "✗ Could not find ImagesBucketName output. Is the stack deployed?" >&2
    exit 1
fi

echo "  Bucket: ${BUCKET_NAME}"
echo "▶ Generating test image locally..."

# Generate a 1024x1024 gradient PNG using Python (no external dependencies)
python3 -c "
import struct, zlib

width, height = 1024, 1024
raw = b''
for y in range(height):
    raw += b'\x00'  # PNG filter: None
    for x in range(width):
        r = int(70 + 150 * (y / height))
        g = int(100 + 100 * abs(0.5 - x / width) * 2)
        b = int(200 - 120 * (y / height))
        raw += struct.pack('BBB', r, g, b)

compressed = zlib.compress(raw, 6)

def chunk(ctype, data):
    c = ctype + data
    return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

with open('$OUTPUT_FILE', 'wb') as f:
    f.write(b'\x89PNG\r\n\x1a\n')
    f.write(chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)))
    f.write(chunk(b'IDAT', compressed))
    f.write(chunk(b'IEND', b''))

print(f'  Generated: $OUTPUT_FILE ({len(compressed) + 57} bytes)')
"

# Upload to S3
S3_KEY="uploads/${IMAGE_NAME}"
echo "▶ Uploading to s3://${BUCKET_NAME}/${S3_KEY}..."
aws s3 cp "$OUTPUT_FILE" "s3://${BUCKET_NAME}/${S3_KEY}" --content-type "image/png"

echo "✓ Done! Image uploaded to s3://${BUCKET_NAME}/${S3_KEY}"
echo "  The S3 event notification will automatically trigger the image processing pipeline."

# Clean up local temp file
rm -f "$OUTPUT_FILE"
