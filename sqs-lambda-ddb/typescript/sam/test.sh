#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

#
# This script sends a batch of new messages to the SQS queue.
#

# Set the stack name
STACK_NAME=sqs-lambda-ddb-sam-ts

command -v aws >/dev/null 2>&1 || { echo >&2 "This script requires AWS CLI (https://aws.amazon.com/cli/) to be installed.  Aborting."; exit 1; }

# Get CloudFront QueueURL output value
queue=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='QueueURL'].OutputValue" --output text)

for ((i=0; i<5; i++)); do
    aws sqs send-message-batch \
        --queue-url "$queue" \
        --entries file://messages.json \
        --no-cli-pager
done
