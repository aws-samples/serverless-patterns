# Running Cloudformation Stack to create AWS resources for end-to-end DAS processing
#!/bin/bash

random_number=$RANDOM
AWS_ACCOUNT_NUMBER=$(aws sts get-caller-identity --profile $1 | jq -r '.Account')
echo "Creating S3 bucket..."
aws s3 mb s3://cft-bucket-$AWS_ACCOUNT_NUMBER-$random_number --profile $1 --no-cli-pager
sleep 30
AWS_REGION=$(aws configure get region --profile $1)
echo "Deploying CloudFormation template..."
aws cloudformation deploy --template-file ./setup-das-cfn.yaml --stack-name $2 --s3-bucket cft-bucket-$AWS_ACCOUNT_NUMBER-$random_number --s3-prefix das --capabilities CAPABILITY_NAMED_IAM --no-disable-rollback --output json --profile $1 --region $AWS_REGION --no-cli-pager --parameter-overrides DASLambdaCodeGithubLocation=https://github.com/aws-samples/serverless-patterns/ --no-fail-on-empty-changeset

