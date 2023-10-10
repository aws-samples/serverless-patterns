#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

#
# This script deploys stack to the default AWS account and region.
#

# Set the stack name
STACK_NAME=sqs-lambda-ddb-sam-ts

command -v sam >/dev/null 2>&1 || { echo >&2 "This script requires AWS SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) to be installed.  Aborting."; exit 1; }

# Build SAM template
sam build
# Deploy SAM template with $STACK_NAME as the stack name
sam deploy --stack-name $STACK_NAME --resolve-s3 --capabilities CAPABILITY_IAM