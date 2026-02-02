#!/bin/bash

bucket_name="aws-sam-cli-samclisourcebucket-${ACCOUNT}-${AWS_DEFAULT_REGION}"

BUCKET_EXISTS=$(aws s3api head-bucket --bucket ${bucket_name} 2>&1 || true)
if [ -z "$BUCKET_EXISTS" ]; then
  echo "Bucket exists"
else
  aws s3api create-bucket --bucket ${bucket_name} --region "${AWS_DEFAULT_REGION}" --create-bucket-configuration LocationConstraint="${AWS_DEFAULT_REGION}"
  echo "Bucket created: ${bucket_name}"
fi

curr_path="${PWD}"

cd ..

sam build

sam deploy --s3-bucket ${bucket_name}

cd ${curr_path}

wait