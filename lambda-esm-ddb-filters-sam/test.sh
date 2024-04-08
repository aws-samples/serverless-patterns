#!/bin/bash
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# This script will add all files from the ./records/ folder as new records to the table-lambda-esm-filter DynamoDB table
# Demo template is expected to be deployed to the AWS CLI's default AWS region

command -v aws >/dev/null 2>&1 || { echo >&2 "This script requires AWS CLI (https://aws.amazon.com/cli/) to be installed.  Aborting."; exit 1; }
command -v jq >/dev/null 2>&1 || { echo >&2 "This script requires jq (https://stedolan.github.io/jq/) to be installed.  Aborting."; exit 1; }

table='table-lambda-esm-filter'

existing=$(aws dynamodb scan \
    --table-name $table \
    --projection-expression 'id')

count=$(echo $existing | jq '.Count')

if [ $count -gt 0 ]
then
    echo "$count record(s) found. Deleting..."

    for ((i=0; i<$count; i++)); do
        key=`echo "$existing" | jq '.Items['$i']'`
        id=`echo "$key" | jq '.id.S'`

        echo "Deleting $id..."

        aws dynamodb delete-item \
            --table-name $table \
            --key "$key"
    done
else
    echo "$table is empty."
fi

echo '--------------------'
echo "Adding new records to $table..."

for f in ./records/*
do
    fileName=$(basename "$f")
    key="${fileName%.*}"

    echo "Adding $key..."
    aws dynamodb put-item \
        --table-name $table \
        --item "$(cat $f)"
done