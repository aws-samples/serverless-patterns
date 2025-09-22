# Amazon API Gateway to Amazon SQS with message filtering

This project contains sample AWS CDK code to create an API Gateway Rest API, an SQS Queue and the correct VTL integration mapping template to filter out parts of the message body.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sqs-msg-filtering-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

```
git clone https://github.com/aws-samples/serverless-patterns
```

2. Change directory to the pattern directory:

```
cd apigw-sqs-msg-filtering-cdk/cdk
```

3. Install dependencies

```
npm install
```

4. This project uses typescript as client language for AWS CDK. Run the given command to compile TypeScript to JavaScript

```
npm run build
```

5. Synthesize CloudFormation template from the AWS CDK app

```
cdk synth
```

6. Deploy the stack to your default AWS account and region.

```
cdk deploy
```

## Testing

Run the following command to send a POST request to the REST API endpoint that will then send the filtered message to the SQS queue. Run the commands from the `apigw-sqs-msg-filtering-cdk` folder.

```bash
export API_GATEWAY_SQS_RESOURCE_ENDPOINT=$(aws cloudformation describe-stacks --stack-name ApigwSqsMsgFilteringCdkStack --query 'Stacks[0].Outputs[?OutputKey==`ApiGatewaySqsResourceEndpoint`].OutputValue' --output text)

curl --location --request POST $API_GATEWAY_SQS_RESOURCE_ENDPOINT \  
--header 'Content-Type: application/json' \
-d @test/test-payload.json
```

To check and receive messages in the queue, it can be done in the AWS console or by running the following command. Note, replace {MyQueueUrl} placeholder in the command with the endpoint that has been deployed. The endpoint can be found in the CloudFormation stack output.

```bash
export SQS_QUEUE_URL=$(aws cloudformation describe-stacks --stack-name ApigwSqsMsgFilteringCdkStack --query 'Stacks[0].Outputs[?OutputKey==`SqsQueueUrl`].OutputValue' --output text)

aws sqs receive-message --queue-url $SQS_QUEUE_URL
```

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy --all
   ```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
