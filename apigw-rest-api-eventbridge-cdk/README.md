# Amazon API Gateway Rest API to Amazon EventBridge

This pattern creates an Amazon API Gateway REST API and Amazon Eventbridge with CDK in Python.

Learn more about this pattern at Serverless Land Patterns: http://serverlessland.com/patterns/apigw-rest-eventbridge-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) AWS CDK installed.
* [Python 3.x Installed](https://www.python.org/) Python 3.x installed with pip.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-rest-eventbridge-cdk
    ```
1. Install Python dependencies.
    ```
    cd cdk
	pip install -r requirements.txt
    ```
1. Deploy the stack to your default AWS account and region. The output of this command should give you the REST API URL.
    ```
    cdk deploy
    ```

## How it works

This pattern creates an Amazon API Gateway REST API and an Amazon EventBridge. The Amazon API Gateway REST API has an Amazon EventBridge integration and transforms the JSON payload to an EventBridge compliant PutEvent JSON [AWS lambda event source mapping](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html). 

Although this pattern is asynchronous, the Amazon EventBridge response will be shown in the response to showcase the functionality.

## Testing

Upon deployment, you will see the API endpoint URL in the output. It will take the format:

`https://${API_ID}.execute-api.${REGION_NAME}.amazonaws.com/prod/`

1. [Enable the model](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#manage-model-access) in Bedrock if you have not done before. The model used by the sample is "anthropic.claude-v2"

2. Post the request to the api
```bash
 curl -v --location --request POST 'https://${API_ID}.execute-api.${REGION_NAME}.amazonaws.com/prod/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "HelloWorld":"Hello World"
}'
```

3. If the execution is successful, you will get response similar to
```json
 {"Entries":
    [{ "EventId": "fb87cdf5-e00a-46f3-6dbb-6b2b3e7f4e25" }],
    "FailedEntryCount":0}
```

## Documentation
- [Tutorial: Build an API Gateway REST API with AWS integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-aws-proxy.html)
- [How do I use API Gateway as a proxy for another AWS service?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-proxy-integrate-service/)
- [Amazon EventBridge documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Amazon EventBridge PutEvents Action documentation](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html)


## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0