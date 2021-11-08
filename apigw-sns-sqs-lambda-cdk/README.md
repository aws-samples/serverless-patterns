# Create an Amazon API Gateway REST API that integrates with Amazon SNS and Amazon SQS to implement Topic-Queue-Chaining

This CDK application demonstrates how to set up a topic-queue-chaining pattern using Amazon SNS and Amazon SQS behind an Amazon API Gateway. 
This architecture helps in setting up a highly scalable API that can consume messages/events, fan them out and process them asynchronously. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-sns-sqs-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
    cd apigw-sns-sqs-lambda-cdk/cdk
    ```

3. Install dependencies:
    ```
    npm install
    ```

4. Compile typescript to js:
    ```
    npm run build
    ```

5. [Configure your AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) to point to the AWS account where you want to deploy the solution.

6. If you are using CDK to deploy to your AWS account for the first time, you will have to install the CDK toolkit stack in your account. 
To do this run the command:
    ```
        cdk bootstrap aws://{{your-aws-account-number}}/{{awregion}}
    ```
    Ex: 'cdk bootstrap aws://135xxxyyyzzz/us-west-2'

7. Deploy the stack
    ```
    cdk deploy
    ```

## How it works

This CDK application deploys an Amazon API Gateway REST API that publishes requests to an SNS Topic. The SNS topic fans out these requests to 2 SQS Queues. Requests in each of these queues are processed by Lambda functions. These functions log the requests to the console.

## Testing

1. Get Rest API Endpoint from stack output
```
    RESTAPI_ENDPOINT=$(aws cloudformation describe-stacks \
        --stack-name CdkApigwSnsSqsLambdaStack \
        --query "Stacks[0].Outputs[0].OutputValue" \
        --output text)
```

2. Send a sample request to the API endpoint
```
    curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"name": "Test message", "category": "Testing", "id": 1}' \
        $RESTAPI_ENDPOINT
```

3. Check the lambda logs from cloudwatch log groups connected to the 2 SQS queues. If the setup is successful you should see the message logged by worker type one lambda and worker type lambda. Worker type one lambda processed message from SQS queue 1 and worker type two lambda processed message from SQS queue 2. 
You can navigate to cloudwatch log groups through AWS management console -> CloudWatch ->  Logs -> Log groups -> Filter by keyword 'workerLambdaType'. 

## Cleanup
 
Run the following command to delete all the resources from your AWS account.
```
cdk destroy
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
