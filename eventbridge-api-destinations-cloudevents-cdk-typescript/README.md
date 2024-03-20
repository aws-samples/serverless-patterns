# Send CloudEvents with Amazon EventBridge API destinations

If your EventBridge API destinations target expects [CloudEvents](https://cloudevents.io/) an EventBridge [Input
Transformer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-transform-target-input.html) can be used to
perform a lossless conversion from the EventBridge event format to CloudEvents.

This pattern demonstrates using an input transformation in an EventBridge rule on a custom event bus to convert an
EventBridge event to a *structured* and *binary* encoded CloudEvent (JSON). To learn more about the differences between
CloudEvents encoding for HTTP see [HTTP content
modes](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/bindings/http-protocol-binding.md#13-content-modes).

Learn more about this pattern at Serverless Land Patterns:
https://serverlessland.com/patterns/eventbridge-api-destinations-cloudevents-cdk-typescript

Important: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* A public HTTPS endpoint supporting CloudEvents e.g., https://webhook.site/ for demo purposes

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
    
1. Change directory to the pattern directory:
    ```
    cd eventbridge-api-destinations-cloudevents-cdk-typescript
    ```
    
1. Install dependencies:

    ```
    npm install
    ```
    
1. From the command line, configure AWS CDK (unless already done) for your account and region:

   ```
   # cdk bootstrap <ACCOUNT-NUMBER/REGION>
   cdk bootstrap 1111111111/us-east-1
   ```

1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
   
    ```
    cdk deploy 
    ```

## How it works

This pattern demonstrates how to convert AWS EventBridge events to CloudEvents using custom HTTP headers and input
transformers in an EventBridge rule with two targets on a custom event bus. The two targets are HTTP API endpoints (in
this case pointing to the same URL defined in the variable `webhookUrl`) using API destinations to deliver the converted
CloudEvents. This example uses two targets to showcase how binary and structured encoded CloudEvents can be used in
EventBridge API destinations.

For binary encoding, dynamic event path references are used to populate the HTTP headers, using the standard API
destinations `content-type` header value `"application/json;charset=UTF-8"`. The event payload (EventBridge `detail`
content) is mapped to the HTTP request body with an input transformer (`$.detail`).

For structured encoding, an input transformer is used to construct the full CloudEvent JSON object sent in the HTTP
request body. This requires the `content-type` header to be set to `"application/cloudevents+json; charset=UTF-8"` to
conform with the CloudEvents specification.

The table below shows the event field mappings used in input transformers and HTTP headers in this pattern. For demo
purposes, `region` is mapped to an CloudEvent extension attribute. 

| EventBridge                              | CloudEvents (structured) via HTTP body          | CloudEvents (binary) via HTTP headers |
| ---------------------------------------- | ----------------------------------------------- | ------------------------------------- |
| `id`                                     | `id`                                            | `ce-id`                               |
| `source`                                 | `source`                                        | `ce-source`                           |
| `detail-type`                            | `type`                                          | `ce-type`                             |
| `time`                                   | `time`                                          | `ce-time`                             |
| `detail`                                 | `data`                                          | n/a (HTTP request body)               |
| `region`                                 | `region`                                        | `region` (extension attribute)        |
| `content-type` (API destinations header) | `"application/cloudevents+json; charset=UTF-8"` | `"application/json;charset=UTF-8"`    |


> [!NOTE]  
> If the incoming event in EventBridge already contains a full CloudEvent in the `detail` field, the input transformer
> mapping for structured encoding is simplified by simply referencing `$.detail` as the outgoing event (input
> transformer template).

## Testing

Step-by-step instructions to understand the implementation for the pattern:

1. Modify the variable `webhookUrl` to match your HTTP target
1. Deploy the `EventbridgeApiDestinationsCloudeventsCdkTypescriptStack` as described [above](#deployment-instructions)
2. Verify the custom event bus, rule, input transformer and API destinations targets were created
3. In the AWS console, open the custom event bus and click on `Send Events` in the upper right (the rule used in this example will match any event from the same account)
4. Make sure the right event bus is selected
5. For `Event source` enter `test.source`
6. For `Detail type` enter `test.event`
7. For `Event detail` enter `{"hello":"world"}`
8. Check the logs of your HTTP endpoint for two incoming events (one for binary, one for structured CloudEvents encoding)
9. If you don't see an event, try sending it again or inspect the SQS dead-letter queue created as part of this stack

## Cleanup

Delete the stack:

```
cdk destroy
```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0