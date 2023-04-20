# AWS Service 1 to AWS Service 2

This pattern helps build CloudWatch Dashboard with AWS Lambda Metrics. The Dashboard built with 3 widgets,
1. Invocations - from AWS/Lambda Namespace
2. memory_utilization - from LambdaInsights Namespace 
3. Custom Metrics (Proxy-Request & Proxy-Successful) - from Custom Nmespace

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.Net Core](https://dotnet.microsoft.com/en-us/download/dotnet)
    - 6.0 for the Lambda Function - https://dotnet.microsoft.com/en-us/download/dotnet/6.0
* [Docker](https://docs.docker.com/get-docker/) installed and running
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd cw-dashboard-lambda-metrics
    ```
3. Install dependencies
    ```
    dotnet restore src
    ```
4. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

Cloudwatch Dashboard created on top of the metrics produced by Lambda Function. Along with the default metrics in the default Namespace, Docker Lambda Function instrumented with Lambda Insight to get the Insight Metrics. Lambda uses Powertools to send the custom metrics. In Lambda function we have two custom metrics one for all the requests and one for successful. 

## Testing

Run some transactions from AWS Console - Lambda - Testing using the following events.

- Payload with validate response

    ```json
    {
        "requestUrl": "https://random.dog/woof.json"
    }
    ```
- Payload with OK status_code with no response 

    ```json
    {
        "requestUrl": "https://httpbin.org/status/200"
    }
    ```
- Payload with error status_code with no response 

    ```json
    {
        "requestUrl": "https://httpbin.org/status/500"
    }
    ```

After running some transactions. Dashboard should start showing the data in graph.

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0