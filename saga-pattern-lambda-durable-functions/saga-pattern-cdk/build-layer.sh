#!/bin/bash
# Build script for the saga-layer Lambda layer
# Uses a temporary virtual environment for clean, isolated builds

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LAMBDA_DIR="${SCRIPT_DIR}/lambda/saga-workflow"
BUILD_DIR="${SCRIPT_DIR}/layer-build"
VENV_DIR="${SCRIPT_DIR}/.venv-build"
OUTPUT_FILE="${SCRIPT_DIR}/saga-layer.zip"

echo "Building Lambda layer for saga workflow..."

# Find Python 3.11+ (required for aws-durable-execution-sdk-python)
if command -v python3.12 &> /dev/null; then
    PYTHON_CMD="python3.12"
elif command -v python3.11 &> /dev/null; then
    PYTHON_CMD="python3.11"
elif command -v python3 &> /dev/null; then
    if python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)"; then
        PYTHON_CMD="python3"
    else
        PY_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
        echo "ERROR: Python 3.11+ is required but found Python ${PY_VERSION}."
        exit 1
    fi
else
    echo "ERROR: Python 3.11+ is required but not found."
    exit 1
fi

echo "Using Python: ${PYTHON_CMD} ($(${PYTHON_CMD} --version))"

# Clean up any previous build artifacts
rm -rf "${BUILD_DIR}" "${VENV_DIR}" "${OUTPUT_FILE}"

# Create a temporary virtual environment for isolated builds
echo "Creating temporary virtual environment..."
${PYTHON_CMD} -m venv "${VENV_DIR}"
source "${VENV_DIR}/bin/activate"

# Upgrade pip in the venv
pip install --upgrade pip --quiet

# Create the layer directory structure
mkdir -p "${BUILD_DIR}/python"

# Install dependencies into the layer directory (isolated from global packages)
echo "Installing dependencies..."
pip install -r "${LAMBDA_DIR}/requirements.txt" -t "${BUILD_DIR}/python" --quiet

# Deactivate and remove the virtual environment
deactivate
rm -rf "${VENV_DIR}"

# Create the zip file
cd "${BUILD_DIR}"
zip -r "${OUTPUT_FILE}" python -q

# Clean up build directory
rm -rf "${BUILD_DIR}"

echo "Layer built successfully: ${OUTPUT_FILE}"
echo "Layer size: $(du -h "${OUTPUT_FILE}" | cut -f1)"
