# Running Cloudformation Stack to create AWS resources for end-to-end DAS processing
#!/bin/bash

RANDOM_STRING=$(tr -dc 'a-z0-9' </dev/urandom | head -c 10 ; echo '')
AWS_ACCOUNT_NUMBER=$(aws sts get-caller-identity --profile $1 | jq -r '.Account')
aws s3 mb s3://cft-bucket-$AWS_ACCOUNT_NUMBER-$RANDOM_STRING --no-cli-pager
sleep 30
aws cloudformation deploy --template-file ~/serverless-patterns/das-lambda-java-sam/setup-das-cfn.yaml --stack-name das-stack --s3-bucket cft-bucket-$AWS_ACCOUNT_NUMBER-$RANDOM_STRING --s3-prefix das --capabilities CAPABILITY_NAMED_IAM --no-disable-rollback --no-verify-ssl --output json --profile $1 --region $AWS_REGION --no-cli-pager --parameter-overrides DASLambdaCodeGithubLocation=https://github.com/awsbloggersfo28/serverless-patterns/ --no-fail-on-empty-changeset --no-verify-ssl