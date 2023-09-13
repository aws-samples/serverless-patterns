#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

#
# This script sends a batch of new messages to the SQS queue.
#

# Set the stack name
STACK_NAME=sqs-lambda-ddb-sam-ts

command -v aws >/dev/null 2>&1 || { echo >&2 "This script requires AWS CLI (https://aws.amazon.com/cli/) to be installed.  Aborting."; exit 1; }
command -v jq >/dev/null 2>&1 || { echo >&2 "This script requires jq (https://stedolan.github.io/jq/) to be installed.  Aborting."; exit 1; }

# Get CloudFront QueueURL output value
queue=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query "Stacks[0].Outputs[?OutputKey=='QueueURL'].OutputValue" --output text)

for ((i=0; i<5; i++)); do
    aws sqs send-message-batch \
        --queue-url "$queue" \
        --entries file://messages.json \
        --no-cli-pager
done

# ----------------

# #send $TOTAL_MESSAGES to SQS queue
# for ((i=0; i<1; i++)); do

#     messages=()

#     for ((j=0; j<1; j++)); do
#         # messages+=("{\"id\": \"$(i*10+j)\", \"message\": \"Message $i\", \"payload\": \"$(printf '%*s' 4000 | tr ' ' '#')\"}")
#         # id=$((i*10+j))
#         # messages+=("{\"Id\": \"test-message-$id\", \"MessageBody\": \"{\"id\": \"$id\", \"message\": \"Message $id\"}\"}")
#         # body="{\\\"id\\\": \\\"$id\\\", \\\"message\\\": \\\"Message $id\\\"}"
#         # entry="{\"Id\": \"test-message-$id\", \"MessageBody\": \"$body\"}"
#         # echo $entry
#         # messages+=("{\"Id\": \"test-message-$id\", \"MessageBody\": \"$(printf '%q' $body)\"}")
#         echo "{\"id\": \"$(i*10+j)\", \"message\": \"Message $i\", \"payload\": \"$(printf '%*s' 4000 | tr ' ' '#')\"}"
#     done

#     json_message=$(echo ${messages[@]} | jq -s .)

#     echo "Sending ${json_message} messages..."

#     # aws sqs send-message \
#     #     --queue-url "$queue" \
#     #     --message-body "$json_message"

# done
