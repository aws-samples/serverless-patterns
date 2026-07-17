#!/usr/bin/env bash
set -euo pipefail

# ──────────────────────────────────────────────────────────────────────────────
# download-testdata.sh
#
# Downloads public domain books from Project Gutenberg and splits them into
# individual chapter/section files for batch processing. Each file becomes
# one parallel task in the durable function workflow.
#
# Files are saved to ./testdata/ which is excluded from source control.
#
# Usage:
#   ./download-testdata.sh
# ──────────────────────────────────────────────────────────────────────────────

OUTPUT_DIR="testdata"

# Project Gutenberg plain text URLs (public domain books)
declare -a BOOKS=(
    "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"   # Pride and Prejudice
    "https://www.gutenberg.org/cache/epub/84/pg84.txt"       # Frankenstein
    "https://www.gutenberg.org/cache/epub/11/pg11.txt"       # Alice in Wonderland
    "https://www.gutenberg.org/cache/epub/1661/pg1661.txt"   # Sherlock Holmes
    "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"   # Moby Dick
    "https://www.gutenberg.org/cache/epub/98/pg98.txt"       # A Tale of Two Cities
)

declare -a NAMES=(
    "pride-and-prejudice"
    "frankenstein"
    "alice-in-wonderland"
    "sherlock-holmes"
    "moby-dick"
    "tale-of-two-cities"
)

echo "▶ Downloading books from Project Gutenberg and splitting into files..."
echo "  Target: ./${OUTPUT_DIR}/"
echo ""

rm -rf "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR"

TOTAL_FILES=0

for i in "${!BOOKS[@]}"; do
    URL="${BOOKS[$i]}"
    NAME="${NAMES[$i]}"
    TEMP_FILE="/tmp/${NAME}.txt"

    echo "  Downloading: ${NAME}..."
    curl -sL "$URL" -o "$TEMP_FILE"

    # Split the book into chunks of ~500 lines each
    # This produces roughly 10-15 files per book, giving us 60-90 total
    CHUNK_NUM=0
    while IFS= read -r line; do
        CHUNK_FILE="${OUTPUT_DIR}/${NAME}-$(printf '%03d' $CHUNK_NUM).txt"
        echo "$line" >> "$CHUNK_FILE"

        # Start a new chunk every 500 lines
        if [[ $(wc -l < "$CHUNK_FILE" | tr -d ' ') -ge 500 ]]; then
            CHUNK_NUM=$((CHUNK_NUM + 1))
        fi
    done < "$TEMP_FILE"

    CHUNK_COUNT=$((CHUNK_NUM + 1))
    TOTAL_FILES=$((TOTAL_FILES + CHUNK_COUNT))
    echo "    → Split into ${CHUNK_COUNT} files"

    rm -f "$TEMP_FILE"
done

echo ""
echo "✓ Created ${TOTAL_FILES} files in ./${OUTPUT_DIR}/"
echo "  Total size: $(du -sh "$OUTPUT_DIR" | cut -f1)"
