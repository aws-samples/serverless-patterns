#!/bin/bash

# Virtual Environment Setup Script for MSK Lambda Schema Avro Python SAM
# This script creates and configures a Python virtual environment

set -e

echo "Setting up Python Virtual Environment for MSK Lambda Schema Avro Python SAM"
echo "=========================================================================="

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.9 or later"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Found Python version: $PYTHON_VERSION"

# Check if version is 3.9 or later
if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 9) else 1)'; then
    echo "Python version is compatible"
else
    echo "Error: Python 3.9 or later is required"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "Virtual environment setup completed successfully!"
echo ""
echo "To activate the virtual environment in the future, run:"
echo "  source venv/bin/activate"
echo ""
echo "To deactivate the virtual environment, run:"
echo "  deactivate"
echo ""
echo "To install additional dependencies:"
echo "  pip install <package-name>"
echo "  pip freeze > requirements.txt  # to update requirements.txt"
echo ""
echo "Next steps:"
echo "1. Make sure the virtual environment is activated: source venv/bin/activate"
echo "2. Run the deployment script: ./deploy.sh"
echo "3. Or build and deploy manually: sam build && sam deploy --guided"
