# AWS Event Source Mapping for Lambda from Amazon Kinesis Data Stream

This pattern demonstrates the ability to filter Amazon Kinesis events so that only a subset of all events is sent to an AWS Lambda function for processing. Demo stack will create a single Amazon Kinesis Data Stream (stream-lambda-esm-filter) and a number of AWS Lambda functions that are subscribed to that stream using different filter configurations.

Review [Filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) for more details on the message filtering configuration.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-esm-kinesis-filters-sam/](https://serverlessland.com/patterns/lambda-esm-kinesis-filters-sam/)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

``` sh
git clone https://github.com/aws-samples/serverless-patterns
```

1. Change directory to the pattern directory:

    ``` sh
    cd lambda-esm-kinesis-filters-sam
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:

    ``` sh
    sam deploy --guided
    ```

    or

    ```sh
    sam deploy --stack-name <STACK_NAME> --resolve-s3 --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region - AWS CLI default region is recommended if you are planning to run the test (test.sh) script
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

A new Amazon Kinesis Data Stream (stream-lambda-esm-filter) is created. Multiple AWS Lambda functions are subscribed to that stream with different filter settings. This way we demonstrate how various filtering settings affect which Amazon Kinesis Data Stream events are sent to each AWS Lambda function for processing.

All AWS Lambda functions use the same code for demo purposes.

The following considerations should be taken into account when working with Amazon Kinesis Data Stream events:

* Event payload is base64 encoded and Lambda function is responsible for decoding it before processing
* Event filtering for Amazon Kinesis Data Stream supports a subset of [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html), for example, `Or (multiple fields)` and `Ends with` didn't work
* Filter definition should not contain any whitespace (tabs, space, etc.) in order to work properly!

## Testing

You can execute a test script to submit a number of test messages to the demo Kinesis Data Stream (stream-lambda-esm-filter).

```sh
./test.sh
```

This script sends a series of test events to `stream-lambda-esm-filter` Kinesis Data Stream.
All test events (see below) are defined in the [events](./events/) folder. The test script reads all files from that folder and sends them as individual events having partition key set to the source file name (without extension).

### Pre-configured test messages

1. Plain string [events/plain-string.txt](events/plain-string.txt)

    ```txt
    plain string event payload
    ```

1. Basic JSON [events/base-json.json](events/base-json.json)

    ```json
    {
        "kind": "Event",
        "apiVersion": "audit.k8s.io/v1",
        "level": "Request",
        "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
        "user": {
            "username": "eks:pod-identity-mutating-webhook",
            "groups": [ "system:authenticated" ]
        },
        "sourceIPs": [ "10.0.0.1" ],
        "RBAC": false,
        "responseStatus":{
            "metadata":{},
            "code":200
        }
    }
    ```

1. Basic JSON with responseStatus code set to 300 [events/code-is-300.json](events/code-is-300.json)

    ```json
    {
        "kind": "Event",
        "apiVersion": "audit.k8s.io/v1",
        "level": "Request",
        "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
        "user": {
            "username": "eks:pod-identity-mutating-webhook",
            "groups": [ "system:authenticated" ]
        },
        "sourceIPs": [ "10.0.0.1" ],
        "RBAC": false,
        "responseStatus":{
            "metadata":{},
            "code":300
        }
    }
    ```

1. Basic JSON with RBAC flag set to true [events/rbac-is-set.json](events/rbac-is-set.json)

    ```json
    {
        "kind": "Event",
        "apiVersion": "audit.k8s.io/v1",
        "level": "Request",
        "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
        "user": {
            "username": "eks:pod-identity-mutating-webhook",
            "groups": [ "system:authenticated" ]
        },
        "sourceIPs": [ "10.0.0.1" ],
        "RBAC": true,
        "responseStatus":{
            "metadata":{},
            "code":200
        }
    }
    ```

1. Basic JSON with kind set to Custom and a new region property [events/custom-with-region.json](events/custom-with-region.json)

    ```json
    {
        "kind": "Custom",
        "region": "us-east-1",
        "apiVersion": "audit.k8s.io/v1",
        "level": "Request",
        "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
        "user": {
            "username": "eks:pod-identity-mutating-webhook",
            "groups": [ "system:authenticated" ]
        },
        "sourceIPs": [ "10.0.0.1" ],
        "RBAC": false,
        "responseStatus":{
            "metadata":{},
            "code":200
        }
    }
    ```

### Viewing test results

Navigate to CloudWatch console and inspect messages logged to the following log groups:

| Log Group | Pattern(s) | Match messages | Comment |
| --- | --- | --- | --- |
| /aws/lambda/fn-esm-no-filter | | ALL | logs all test messages |
| /aws/lambda/fn-filter-between-inclusive | `{"data":{"responseStatus":{"code":[{"numeric":[">=",300,"<=",350]}]}}}` | 3 | interval start value is included, documentation demonstrates exclusive start value: `"Price":[{"numeric":[">",10,"<=",20]}]` |
| /aws/lambda/fn-filter-events | `{"data":{"kind":["Event"]}}` | 2, 3, 4 | tests for a single property value equality |
| /aws/lambda/fn-filter-events-and-response-code | `{"data":{"kind":["Event"],"responseStatus":{"code":[{"numeric":["=",300]}]}}}` | 3 | tests for multiple properties, including nested object |
| /aws/lambda/fn-filter-multiple-patterns | `{"data":{"responseStatus":{"code":[{"numeric":[">=",300]}]}}}` and `{"data":{"RBAC":[true]}}` | 3, 4 | demonstrates that multiple patterns are ORed. Additionally demonstrates the use of `>=` comparison operator, while documentation covers only equality and interval use cases. |
| /aws/lambda/fn-filter-not-event-kind | `{"data":{"kind":[{"anything-but":["Event"]}]}}` | 5 | tests for a single field inequality |
| /aws/lambda/fn-filter-on-data-and-metadata | `{"data":{"kind":["Event"]},"partitionKey":["code-is-300"]}` | 3 | demonstrates filtering on a combination of data and metadata conditions |
| /aws/lambda/fn-filter-starts-with | `{"data":{"region":[{"prefix":"us-"}]}}` | 5 | tests for a string prefix |

## Cleanup

1. Delete the stack

    ```bash
    sam delete --stack-name <STACK_NAME>
    ```

1. Confirm the stack has been deleted

    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<STACK_NAME>')].StackStatus"
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
