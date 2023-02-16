# AWS Event Source Mapping for Lambda from Amazon SQS

You can use event filtering to control which events Lambda sends to your function for processing. You can use this template to explore and test how to configure event filtering for SQS messages triggering a lambda function. The SAM template deploys multiple Lambda function, multiple SQS queues and the permissions required to run the application. The template also deploys an SNS topic that helps automate the testing of the pattern.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-esm-sqs-filters-sam/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

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
    cd serverless-patterns/lambda-esm-sqs-filters-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## Included scenarios
**No Filter** - A simple trigger without a filter criteria
**Prefix** - A filter checking whether a particular JSON field value begins with a particular value
```
{
    "body":{
        "region":[{"prefix":"us-"}]
    }
}
```

**Anything But** - A filter checking whether a particular JSON value is not what we have defined in the filter rule
```
{
    "body":{
        "address":{"state":[{"anything-but":"GA"}]}
    }
}
```

**IP** - A filter checking whether the inspected value is an IP address within a certain CIDR
```
{
    "body":{
        "sourceIPAddress":[{"cidr":"10.0.0.0/24"}]
    }
}
```

**AND** - Logical AND. This filter will match any rating between 0 and 5 (excluding 0) AND the country needs to match AND the "street" key needs to be present (the exists filter only works on leaf nodes!)
```
{
    "body" : {
      "rating" : [ { "numeric": [ ">", 0, "<=", 5]}],
      "address" : {
          "country": [ "USA" ],
          "street": [ { "exists": true  } ]
      }
    }
}
```

**OR** - Logical OR. The filter will match if any of the rules match. Rating is 4 or 5 OR the filename is "metadata.txt" OR (the country is "USA" and there is a street address present)
```
{
    "body":{"rating":[4,5]}
}
{
    "body":{"fileName": ["metadata.txt"]}
}
{
    "body":{
        "address":{
            "country":["USA"],
            "street":[{"exists":true}]
        }
    }
}
```

## Filters that do not work with SQS
*Suffix* - Also known as Ends with. Filter like this: `"FileName": [ { "suffix": ".png" } ]` does not work with ESM for SQS

*$Or* - Also known as Or (multiple fields). Filter like this: `"$or": [ { "Location": [ "New York" ] }, { "Day": [ "Monday" ] } ]` does not work with ESM for SQS

*Filters on `messageAttributes`* - When sending an SQS message, there is an option to add additional attributes to the message. ESM filters do not work on these. Filters do work on the `body` & `attributes` (see ecample payload below) part of the message, but not on the messageAttributes.

*equals-ignore-case* - `"Name": [ { "equals-ignore-case": "alice" } ]` This operator is not supported by ESM filters for SQS

## Example test json
```
{
    "region": "us-east-1",
    "sourceIPAddress": "10.0.0.11",
    "rating": 4,
    "fileName": "metadata.txt",
    "address": {
        "country": "USA",
        "street": "56 Fox Dr",
        "city": "Boston",
        "state": "MA"
    }
}
```

## Example payload from SQS

```
{
    "Records": [
        {
            "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
            "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
            "body": "test",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082649183",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082649185"
            },
            "messageAttributes": {
                'customAttribute': {
                DataType: 'String',
                StringValue: 'CustomValue'
                }
            },
            "md5OfBody": "098f6bcd4621d373cade4e832627b4f6",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2"
        }
    ]
}

```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to publish a message to the SNS topic. SNS will send the message to all SQS Queues, which will be used as a trigger for the Lambda functions. Using event source mapping (ESM), the message content will be evaluated against the defined rules on the event trigger. If the rules match, the lambda function will be triggered, otherwise the message will be discarded. The SNS topic name is in the outputs of the AWS SAM deployment (the key is `SNSArn`):

1. Publish a test message to the SNS topic to send it to all test SQS queues:

```bash
aws sns publish --topic-arn ENTER_YOUR_TOPIC_ARN --message file://events/testMessage.json
```
2. Retrieve the logs from Cloudwatch Logs and verify all functions have run:
```bash
aws logs describe-log-groups --log-group-name-pattern EsmSqsFilter
```

3. Navigate to CloudWatch console and view the following log groups:

| Log Group | Pattern(s) | Comment |
| --- | --- | --- |
| /aws/lambda/\*EsmSqsFilterFunctionNoFilter\* | | matches all test messages |
| /aws/lambda/\*EsmSqsFilterFunctionPrefix\* | `{"body":{"region":[{"prefix":"us-"}]}}` | matches the message if the region begins with "us-" |
| /aws/lambda/\*EsmSqsFilterFunctionIP\* | `{body":{"sourceIPAddress":[{ "cidr":"10.0.0.0/24"}]}}` | matches messages that have sourceIPAddress within the cidr range specified (10.0.0.0->10.0.0.255) |
| /aws/lambda/\*EsmSqsFilterFunctionAnythingBut\* | `{"body":{"address":{"state":[{"anything-but":"GA"}]}}}` | matches messages that have a value in address->state not equal to "GA" |
| /aws/lambda/\*EsmSqsFilterFunctionAnd\* | `{"body":{"rating":[{"numeric":[">",0,"<=",5]}],"address":{"country":["USA"],"street":[{"exists":true}]}}}` | Logical AND. It will match any rating between 0 and 5 (excluding 0) AND the country needs to match AND the "street" key needs to be present (the exists filter only works on leaf nodes!) |
| /aws/lambda/\*EsmSqsFilterFunctionOr\* | `{"body":{"rating":[4,5]}}, {"body":{"fileName": ["metadata.txt"]}}, {"body":{"address":{"country":["USA"],"street":[{"exists":true}]}}}}`| Logical OR. The filter will match if any of the rules match. Rating is 4 or 5 OR the filename is "metadata.txt" OR (the country is "USA" and there is a street address present) |


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
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
