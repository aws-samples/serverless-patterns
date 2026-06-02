#!/bin/bash
set -euo pipefail

APP="npx ts-node --prefer-ts-exts src/bin/apigw-dynamodb-apikey-cdk.ts"
STACK_NAME="ApigwDynamodbApikeyCdkStack"

npm install
cdk deploy "$STACK_NAME" --app "$APP" "$@"
