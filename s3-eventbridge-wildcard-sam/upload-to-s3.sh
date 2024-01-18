#!/bin/bash

# Prompt for S3 bucket name
read -p "Enter S3 bucket name: " BUCKET

# Set date and timestamp 
DATE=$(date +%Y-%m-%d)
TIMESTAMP=$(date +%s)

# S3 folder for ABC 
FOLDER="$DATE/$TIMESTAMP/ABC"

# Create folder structure for ABC data in S3
aws s3api put-object --bucket $BUCKET --key $FOLDER/

# Upload ABC data to S3 
CSV_FILE="abc-data.csv"

if [ -f "$CSV_FILE" ]; then
  aws s3 cp $CSV_FILE s3://$BUCKET/$FOLDER/
else
  echo "File $CSV_FILE does not exist"
  exit 1
fi


# S3 folder for XYZ 
FOLDER="$DATE/$TIMESTAMP/XYZ"

# Create folder structure for XYZ data in S3
aws s3api put-object --bucket $BUCKET --key $FOLDER/

# Upload XYZ data to S3 
CSV_FILE="xyz-data.csv"

if [ -f "$CSV_FILE" ]; then
  aws s3 cp $CSV_FILE s3://$BUCKET/$FOLDER/
else
  echo "File $CSV_FILE does not exist"
  exit 1
fi

echo "ABC and XYZ data uploaded to S3 bucket $BUCKET"
aws s3 ls s3://$BUCKET --recursive
