#!/bin/bash

# Read bucket name from user input
read -p "Enter S3 bucket name to empty: " BUCKET_NAME

# Confirm before emptying
read -p "Are you sure you want to empty s3://$BUCKET_NAME? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi

# Empty bucket using aws s3 rm recursive delete  
aws s3 rm "s3://$BUCKET_NAME" --recursive

echo "Bucket $BUCKET_NAME emptied"