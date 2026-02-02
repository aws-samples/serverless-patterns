# Idempotent HTTP requests with Amazon EventBridge API Destinations

This pattern describe how to use EventBridge API Destinations with the IETF HTTP `Idempotency-Key`
[header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) to invoke HTTP APIs supporting
idempotent API operations. Using API destinations, you can route events between AWS services, integrated software as a
service (SaaS) applications, and your applications outside of AWS by using API calls.

> Idempotence is the property of certain operations in mathematics and computer science whereby they can be applied
> multiple times without changing the result beyond the initial application.  It does not matter if the operation is
> called only once, or 10s of times over. Idempotency is important in building a fault-tolerant HTTP API. An HTTP
> request method is considered idempotent if the intended effect on the server of multiple identical requests with that
> method is the same as the effect for a single such request.

Source: https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/

Learn more about this pattern at Serverless Land Patterns:
https://serverlessland.com/patterns/eventbridge-api-destinations-idempotency-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free
Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any
AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already
  have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls
  and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd eventbridge-api-destinations-idempotency-cdk/src
    ```
1. Install dependencies:

    ```
    npm install
    ```
    
1. In the file `lib/eb-api-destination-stack.ts` change the variable `webhookUrl` to match your desired HTTP API target. For example, you can generate a unique webhook URL for testing using https://webhook.site.
    
1. From the command line, configure AWS CDK (unless already done):

   ```
   # cdk bootstrap <ACCOUNT-NUMBER/REGION>
   cdk bootstrap 1111111111/us-east-1
   ```

1. From the command line, use AWS CDK to deploy the AWS resources for the pattern:
   
    ```
    cdk deploy 
    ```

1. Note down the event bus ARN from the output value of `EbApiDestinationStack.busArn` which is used for testing in
   later steps.

## How it works

This pattern creates a custom event bus with an event filtering rule matching all events sent from the same account.
These events are then sent to an API Destination, i.e., the HTTP target you configured during the above steps. Each
event is sent as a JSON request to the HTTP target. If event delivery fails, i.e., after 3 retries in this sample,
events are sent to an Amazon SQS dead-letter queue (DLQ).

EventBridge allows developers to create dynamic mappings from event fields to HTTP headers. A custom client-controlled
field value from the event body e.g., `customID` in `events.json` file in this sample, is used as the IETF HTTP
`Idempotency-Key` [header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) value. The HTTP
target can then use the IETF standardized `Idempotency-Key` in the HTTP request to detect duplicate requests.  The
reason for using a specific field from the event body as the `Idempotency-Key` is to give the developer (event producer)
control over the value used in that header. EventBridge generates a unique event ID per request, which could be used in
this example as the header value. However, this ID can also change and thus might not be stable, for example when a
client needs to retry sending an event to EventBridge after a failed or timed out `PutEvents` call. 

The header key name and value, i.e., event field reference, can be changed based on your needs and event schema. See
`headerParameters` in the target configuration in `src/lib/eb-api-destination-stack.ts` (and make sure to change the
event sample in `src/events.json` accordingly).

## Testing

After the CDK stack is deployed send a test event to EventBridge. In `src/events.json` replace the `EventBusName`
placeholder value with the ARN you copied from the deployment step above. Also change this file if you made other
changes to the stack configuration e.g., using a different header key or event field reference.

```
# from within the src/ folder
aws events put-events --entries file://events.json
```

Your output shoud look like:

```
{
    "FailedEntryCount": 0,
    "Entries": [
        {
            "EventId": "3c3f6b7d-9ef1-d718-5d10-c5427beb6c40"
        }
    ]
}
```

In your HTTP API e.g., https://webhook.site/, you should see a new event (HTTP request) with the `Idempotency-Key`
header value from the sample event used in the `put-events` call e.g., `idempotency-key:
e9bf3c4d-638c-4fb3-898b-1ac6c1988000`. The value is different from the `EventID` seen in the above `put-events` response
because we are using a client-controlled event ID as described above. If you want to use the EventBridge event ID as the
header value, change `headerParameters` in `src/lib/eb-api-destination-stack.ts` to `'Idempotency-Key': '$.id'`. 

Note that HTTP headers are case-insensitive when transferred over the network.

## Cleanup

Delete the stack:

```
cdk destroy
```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0