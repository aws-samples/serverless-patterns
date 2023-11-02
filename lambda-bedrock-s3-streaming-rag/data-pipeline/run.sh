#!/bin/bash

# Function to display help message
usage() {
  echo "Usage: $0 <stack-name>"
  echo "Please provide your stack name. You can find it in your samconfig.toml"
  echo "Example: $0 my-stack-name"
}

# Check if at least one argument is provided
if [ "$#" -ne 1 ]; then
  usage
  exit 1
fi

# Define the directory and file extension for documents
directory="./docs"
file_extension="pdf"  # Change this to your desired file extension

# Function to display error message
error_message() {
  echo "Error: No valid documents found in $directory. Make sure your document has a .pdf extension"
}


# Find and print all documents in the directory
documents=$(find "$directory" -type f -name "*.$file_extension")
if [ -z "$documents" ]; then
  error_message
  exit 1
else
  echo "Importing documents into LanceDB:"
  echo "$documents"
fi

rm -rf /tmp/embeddings
python3 ingest.py


STACK_NAME=$1
BUCKET_NAME=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`DocumentBucketName`].OutputValue' --output text)


cp -r /tmp/embeddings ./

echo "Exporting embeddings to s3://${BUCKET_NAME}"
aws s3 sync ./embeddings s3://${BUCKET_NAME}
