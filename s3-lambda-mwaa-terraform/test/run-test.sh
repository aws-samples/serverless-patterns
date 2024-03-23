# This code transpiles Typescript code into Javascript and packages third party libs to be deployed as lambda layer.  
# © 2023 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.  
# This AWS Content is provided subject to the terms of the AWS Customer Agreement available at  
# http://aws.amazon.com/agreement or other written agreement between Customer and either
# Amazon Web Services, Inc. or Amazon Web Services EMEA SARL or both.

#!/bin/bash
set -ex

# CLI Arguments
if [ -z $1 ]
then
    echo "S3 bucket name was not passsed."
    exit -1
else
	S3_BUCKET_NAME=$1
fi

# Upload input.json to S3 bucket
aws s3 cp test/input.json s3://$S3_BUCKET_NAME/input.json --sse "AES256"


