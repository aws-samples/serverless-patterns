# AWS API Gateway to Amazon EventBridge

This pattern deploys an API Gateway HTTP API with a custom domain configuration and permissions to publish HTTP requests as events to EventBridge.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/apigateway-http-eventbridge-custom](https://serverlessland.com/patterns/apigateway-http-eventbridge-custom)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-eventbridge
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The endpoint that will be created might look like, for example: `http://dev-events.example.com/apigw2eb/{source}/{detailType}`

Simply specify any `source` and `detailType` as a path parameters. The `body` of the request could be any valid json object.

### The AWS SAM template deploys the following resources

| Type | Logical ID |
| --- | --- |
| AWS::ApiGatewayV2::Api | HttpApi |
| AWS::Events::EventBus | ApplicationEventBus |
| AWS::ApiGatewayV2::Stage | HttpApiStage |
| AWS::ApiGatewayV2::ApiMapping | HttpApiMapping |
| AWS::IAM::Role | HttpApiIntegrationEventBridgeRole |
| AWS::ApiGatewayV2::Integration | HttpApiIntegrationEventBridge |
| AWS::ApiGatewayV2::Route | HttpApiRoute |
| AWS::CloudFormation::Stack1 | apigw2eb-[STAGE] |

When you send an HTTP POST request, the API Gateway publishes an event to the custom event bus in EventBridge.

## Testing

Use your preferred terminal to send a http request.

```bash
curl --location --request POST 'https://dev-events.example.com/apigw2eb/mysource/mydetailtype' \
--header 'Content-Type: application/json' \
--data-raw '{
    "mybody": {
        "attr1": 1,
        "attr2": [1,2]
    }
}'
```

The response would be like:

```bash
{
    "Entries": [
        {
            "EventId": "1a15592f-87a0-e0d8-8e21-172e63c57212"
        }
    ],
    "FailedEntryCount": 0
}
```

This means your event was published successfuly.

So, the Lambda event for the request above will look like:

```json
{
    "version": "0",
    "id": "1a15592f-87a0-e0d8-8e21-172e63c57594",
    "detail-type": "mydetailtype",
    "source": "com.mycompany.mysource",
    "account": "xxxxxxxxxx74",
    "time": "2021-04-03T14:45:32Z",
    "region": "eu-central-1",
    "resources": [],
    "detail": {
        "mybody": {
            "attr1": 1,
            "attr2": [1, 2]
        }
    }
}
```

Create your own either Lambda function or any other consumer for events you send with this API Gateway endpoint.

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----

## Additional resources

- [Amazon API Gateway V2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.html)
- [Amazon EventBridge](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Events.html)

---

Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
