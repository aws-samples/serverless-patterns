#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# This script will send all files from the ./events/ folder as messages to stream-lambda-esm-filter Kinesis Data Stream
# Demo template is expected to be deployed to the AWS CLI's default AWS region

command -v aws >/dev/null 2>&1 || { echo >&2 "This script requires AWS CLI (https://aws.amazon.com/cli/) to be installed.  Aborting."; exit 1; }

# detect AWS CLI major version number
aws_version=$(aws --version 2>&1 | cut -d '.' -f1 | cut -d '/' -f2)

stream='stream-lambda-esm-filter'

for f in ./events/*
do
    fileName=$(basename "$f")
    key="${fileName%.*}"

    echo "Sending $key payload..."
    if [ $aws_version -eq 1 ]
    then
        # send payload as-is to AWS CLI v1
        aws kinesis put-record \
            --stream-name "$stream" \
            --data  "$(cat "$f")" \
            --partition-key "$key"
    else
        # AWS CLI v2 expects payload data to be base64 encoded
        aws kinesis put-record \
            --stream-name "$stream" \
            --data  "$(base64 -i "$f")" \
            --partition-key "$key"
    fi

    echo '--------------------'
done
