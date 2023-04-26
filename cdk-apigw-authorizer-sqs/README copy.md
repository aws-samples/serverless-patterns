
# Welcome to a CDK Python project for deploying AWS resources for Queue Leveling pattern!


# 1. Clone the repository
git clone https://github.com/aws-samples/pattern-apigw-auth-sqs.git

# 2. Change directory
cd pattern-apigw-auth-sqs

# 3. TO generate a cloudformation templates
## with token autorizer
    cdk synth ApigwSqsAuthStack -o ./cloudformation_templates

## without a token autorizer
cdk synth ApigwSqsStack -o ./cloudformation_templates

# To deploy AWS resources as a CDK project
## Paramters needed for CDK 
 * <storagequeue>=Name of the SQS queue where you want data to be sent
 * <awsregion>=AWS region where you want the APIGW, SQS and token authoizer to be created.
 * <lambdaauthorizerarn>=ARN of the lambda which implemented the token authorizer validation logic.

## To deploy the infrastructure with a token authorizer
cdk deploy ApigwSqsAuthStack --parameters storagequeue=authorizerqueue --parameters awsregion=us-east-1 --parameters lambdaauthorizerarn=arn:aws:lambda:us-east-1:764551143200:function:apigwRequestAuthorizer

## To deploy the infrastructure without a token authorizer
cdk deploy ApigwSqsAuthStack --parameters storagequeue=authorizerqueue --parameters awsregion=us-east-1 