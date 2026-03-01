# This script should be used to test the pattern. It does the following tasks:
# 	1. Gathers output values from Terraform
# 	2. Adds test data to DynamoDB
# 	3. Starts the Glue job
# 	4. Runs a CLI command to check the contents of S3

#!/bin/bash
set -e

echo "Testing DynamoDB to S3 Glue Zero-ETL Integration..."

# Get the required resource names from terraform outputs
BUCKET_NAME=$(terraform output -raw s3_bucket_name)
TABLE_NAME=$(terraform output -raw dynamodb_table_name)
JOB_NAME=$(terraform output -raw glue_job_name)

# Add data to DynamoDB
echo "Adding test data to DynamoDB..."
aws dynamodb put-item --table-name $TABLE_NAME --item '{"id":{"S":"test1"},"name":{"S":"John"},"age":{"N":"30"}}'
aws dynamodb put-item --table-name $TABLE_NAME --item '{"id":{"S":"test2"},"name":{"S":"Jane"},"age":{"N":"25"}}'
aws dynamodb put-item --table-name $TABLE_NAME --item '{"id":{"S":"test3"},"name":{"S":"Julie"},"age":{"N":"35"}}'

# Run the Glue job
echo "Starting Glue job..."
JOB_RUN_ID=$(aws glue start-job-run --job-name $JOB_NAME --query 'JobRunId' --output text)

echo "✅ Job started with ID: $JOB_RUN_ID"
echo ""
echo "Run this command to monitor job status:"
echo "  aws glue get-job-run --job-name $JOB_NAME --run-id $JOB_RUN_ID"
echo ""
echo "Run this command to check the results in S3:"
echo "  aws s3 ls s3://$BUCKET_NAME/data/ --recursive"
