#!/bin/bash

# This script facilitates checking if the contents are different between `terraform apply` runs

# List of arguments
build_folder=${1}

# Linux has command md5sum and OSX has command md5
if command -v md5sum >/dev/null 2>&1; then
  MD5_PROGRAM=md5sum
elif command -v md5 >/dev/null 2>&1; then
  MD5_PROGRAM=md5
else
  echo "ERROR: md5sum is not installed"
  exit 255
fi

# Take md5 from each object inside the program and then take a md5 of that output
md5_output="$(eval ${MD5_PROGRAM} $build_folder/** | ${MD5_PROGRAM})"

# Output result as JSON back to terraform
echo "{ \"md5\": \"${md5_output}\" }"
