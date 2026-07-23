#!/usr/bin/env bash
set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
# download-testdata.sh
#
# Downloads NOAA Global Historical Climatology Network Daily (GHCN-D) CSV files
# from the public S3 bucket s3://noaa-ghcn-pds/csv/by_year/.
#
# Only files smaller than 100KB are downloaded — this keeps the test dataset
# lightweight while still providing real-world data for batch processing.
#
# Files are saved to ./testdata/ which is excluded from source control.
#
# Usage:
#   ./download-testdata.sh          # Downloads up to 20 files
#   ./download-testdata.sh 50       # Downloads up to 50 files
#   MAX_FILES=10 ./download-testdata.sh
# ──────────────────────────────────────────────────────────────────────────────

OUTPUT_DIR="testdata"
SOURCE_BUCKET="noaa-ghcn-pds"
SOURCE_PREFIX="csv/by_year/"
MAX_SIZE_BYTES=102400  # 100KB
MAX_FILES="${1:-${MAX_FILES:-20}}"

echo "▶ Downloading up to ${MAX_FILES} NOAA GHCN-D CSV files < 100KB from s3://${SOURCE_BUCKET}/${SOURCE_PREFIX}"
echo "  Target: ./${OUTPUT_DIR}/"
echo ""

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

FILE_COUNT=0

# List all objects under the prefix, filter to files under 100KB, then download up to MAX_FILES
aws s3api list-objects-v2 \
    --bucket "$SOURCE_BUCKET" \
    --prefix "$SOURCE_PREFIX" \
    --no-sign-request \
    --query "Contents[?Size<\`${MAX_SIZE_BYTES}\`].[Key,Size]" \
    --output text | head -n "$MAX_FILES" | while IFS=$'\t' read -r key size; do

    # Skip empty lines or the prefix directory itself
    if [[ -z "$key" || "$key" == "$SOURCE_PREFIX" ]]; then
        continue
    fi

    FILENAME=$(basename "$key")
    DEST_PATH="${OUTPUT_DIR}/${FILENAME}"

    echo "  Downloading: ${FILENAME} ($(numfmt --to=iec-i --suffix=B "$size" 2>/dev/null || echo "${size} bytes"))"
    aws s3 cp "s3://${SOURCE_BUCKET}/${key}" "$DEST_PATH" --no-sign-request --quiet

    FILE_COUNT=$((FILE_COUNT + 1))
done

# Count files actually downloaded (the while loop runs in a subshell)
ACTUAL_COUNT=$(find "$OUTPUT_DIR" -type f | wc -l | tr -d ' ')

echo ""
echo "✓ Downloaded ${ACTUAL_COUNT} files to ./${OUTPUT_DIR}/"
echo "  Total size: $(du -sh "$OUTPUT_DIR" | cut -f1)"
