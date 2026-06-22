#!/bin/bash
set -e

# Resolve script directory so paths work regardless of where the script is called from
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${SCRIPT_DIR}/build"
SRC_DIR="${SCRIPT_DIR}/../src"
REQUIREMENTS="${SCRIPT_DIR}/../requirements.txt"

echo "Building Lambda deployment package..."

# Step 1: Clean build directory
if [ -d "$BUILD_DIR" ]; then
    echo "Cleaning existing build directory..."
    rm -rf "$BUILD_DIR"
fi
mkdir -p "$BUILD_DIR"

# Step 2: Install runtime dependencies (exclude testing packages)
echo "Installing dependencies..."
grep -v "testing" "$REQUIREMENTS" | grep -v "^#" | grep -v "^$" | \
    pip install --target "$BUILD_DIR" -r /dev/stdin --quiet

# Step 3: Copy application source files
echo "Copying application source..."
cp "$SRC_DIR"/*.py "$BUILD_DIR"/
cp -r "$SRC_DIR/utils" "$BUILD_DIR/utils"

echo "Build complete. Output: $BUILD_DIR"
