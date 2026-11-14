#!/bin/bash
set -e -o pipefail

source ./scripts/bootstrap-utils.sh

bootstrap_util bootstrap_start
# Optionally pass a python version to setup_python_runtime e.g $TARGET_PYTHON_VERSION Default: 3.9.18
bootstrap_util setup_python_runtime
bootstrap_util upgrade_pip_version
# Optionally define which tools to install e.g "${COMMON_TOOLS[*]}"
bootstrap_util install_common_tools 
# Optionally pass requirements file label and path (without the extension) e.g "project" "requirements"
bootstrap_util install_python_dependencies 
bootstrap_util bootstrap_complete
