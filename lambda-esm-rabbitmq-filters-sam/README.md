# AWS Event Source Mapping for Lambda from RabbitMQ

You can use event filtering to control which events Lambda sends to your function for processing. You can use this template to explore and test how to configure event filtering for AmazonMQ RabbitMQ messages triggering a lambda function. The SAM template deploys multiple Lambda consumer functions, an MQ broker and the permissions required to run the application. The template also deploys an additional helper Lambda function used for creating the RabbitMQ Queues and pushing messages to it for testing purposes.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-esm-rabbitmq-filters-sam/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Set up your username and password for RabbitMQ access. In a new terminal window enter:
    ```
    aws secretsmanager create-secret --name MQaccess --secret-string '{"username": "your-username", "password": "your-password"}'
    ```
1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-esm-rabbitmq-filters-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.
    * Enter the SecretARN which came as an output from the first step
    * Enter the SecretName which came as an output from the first step (for example `MQaccess`)

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing. Take note of the output `MQBrokerHost` & `LambdaHelper` - you will need it for testing later on.

## Included scenarios
**No Filter** - A simple trigger without a filter criteria
**Prefix** - A filter checking whether a particular JSON field value begins with a particular value. Note here we are filtering based on the RabbitMQ message properties, not the payload
```
{
    "basicProperties":{
        "appId":[{"prefix":"my"}]
    }
}
```

**Anything But** - A filter checking whether a particular JSON value is not what we have defined in the filter rule
```
{
    "data":{
        "address":{"state":[{"anything-but":"GA"}]}
    }
}
```

**IP** - A filter checking whether the inspected value is an IP address within a certain CIDR
```
{
    "data":{
        "sourceIPAddress":[{"cidr":"10.0.0.0/24"}]
    }
}
```

**AND** - Logical AND. This filter will match any rating between 0 and 5 (excluding 0) AND the country needs to match AND the "street" key needs to be present (the exists filter only works on leaf nodes!)
```
{
    "data" : {
      "rating" : [ { "numeric": [ ">", 0, "<=", 5]}],
      "address" : {
          "country": [ "USA" ],
          "street": [ { "exists": true  } ]
      }
    }
}
```

**OR** - Logical OR. The filter will match if any of the rules match. Note this combines filters for both the message data and message properties passed from RabbitMQ. The appId property is "myShinyApp" OR Rating is 4 or 5 OR the OR (the country is "USA" and there is a street address present)
```
{
    "basicProperties":{"appId": ["myShinyApp"]}
}
{
    "data":{"rating":[4,5]}
}
{
    "data":{
        "address":{
            "country":["USA"],
            "street":[{"exists":true}]
        }
    }
}
```

## Filters that do not work with RabbitMQ
*Suffix* - Also known as Ends with. Filter like this: `"FileName": [ { "suffix": ".png" } ]` does not work with ESM for AWS MQ

*$Or* - Also known as Or (multiple fields). Filter like this: `"$or": [ { "Location": [ "New York" ] }, { "Day": [ "Monday" ] } ]` does not work with ESM for AWS MQ

*equals-ignore-case* - `"Name": [ { "equals-ignore-case": "alice" } ]` This operator is not supported by ESM filters for AWS MQ

## Example test json

Use this JSON to invoke the MQHelper lambda function. 

The `host` field points to the RabbitMQ (use the output from the SAM template)

The `appId` field will be passed as an app_id basic property to the RabbitMQ

The `secret` field is your secret in AWS Secrets Manager (output from `aws secretsmanager create-secret...`)

The `queues` array is a list of queues that will be created on the RabbitMQ. The `messageBody` will be sent as a payload, along with the `appId` field as a basic property, to all RabbitMQ queues.

The `messageBody` will be used as a payload for the messages sent to RabbitMQ

```
{
    "host": "<uniqueID>.mq.us-east-1.amazonaws.com",
    "appId": "myShinyApp",
    "queues": ["noFilterQ","prefixQ", "anythingButQ", "IPQ", "andQ", "orQ"],
    "secret": "MQaccess",
    "messageBody": {
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
}

```

## Example payload from RabbitMQ

```
{
   "eventSourceArn":"arn:aws:mq:us-east-1:983412437965:broker:myQueue:b-5582a567-c8f0-425d-bf92-e05a369d8af9",
   "rmqMessagesByQueue":{
      "anythingButQ::/":[
         {
            "basicProperties":{
               "contentType":"None",
               "contentEncoding":"None",
               "headers":"None",
               "deliveryMode":"None",
               "priority":"None",
               "correlationId":"None",
               "replyTo":"None",
               "expiration":"None",
               "messageId":"None",
               "timestamp":"None",
               "type":"None",
               "userId":"None",
               "appId":"myShinyApp",
               "clusterId":"None",
               "bodySize":183
            },
            "redelivered":false,
            "data":"eyJyZWdpb24iOiAidXMtZWFzdC0xIiwgInNvdXJjZUlQQWRkcmVzcyI6ICIxMC4wLjAuMTEiLCAicmF0aW5nIjogNCwgImZpbGVOYW1lIjogIm1ldGFkYXRhLnR4dCIsICJhZGRyZXNzIjogeyJjb3VudHJ5IjogIlVTQSIsICJzdHJlZXQiOiAiNTYgRm94IERyIiwgImNpdHkiOiAiQm9zdG9uIiwgInN0YXRlIjogIk1BIn19"
         }
      ]
   },
   "eventSource":"aws:rmq"
}
```

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to invoke the `MQHelper` lambda function. The function will create all required queues in RabbitMQ and send the message to all of them, which will be used as a trigger for the Lambda functions. Using event source mapping (ESM), the message content will be evaluated against the defined rules on the event trigger. If the rules match, the lambda function will be triggered, otherwise the message will be discarded. The Function name is in the outputs of the AWS SAM deployment (the key is `LambdaHelper`):

1. Invoke the helper lambda function in order to create the RabbitMQ Queues and publish a message into each one:

```bash
aws lambda invoke --function-name <your_function_name> --payload file://events/testMessage.json --cli-binary-format raw-in-base64-out response.json
```

1. Verify your messages have been posted by checking the function output:

```bash
cat response.json
```

Your result should look similar to this: `{"statusCode": 200, "body": "\"Posted 6 messages!\""}`

1. Retrieve the logs from Cloudwatch Logs and verify all functions have run:
```bash
aws logs describe-log-groups --log-group-name-pattern MQFunction
```

1. Navigate to CloudWatch console and view the following log groups:

| Log Group | Pattern(s) | Comment |
| --- | --- | --- |
| /aws/lambda/\*MQFunctionNoFilter\* | | matches all test messages |
| /aws/lambda/\*MQFunctionPrefix\* | `{"basicProperties":{"appId":[{"prefix":"my"}]}}` | matches the message if the basic property appId begins with "my" |
| /aws/lambda/\*MQFunctioIP\* | `{data":{"sourceIPAddress":[{ "cidr":"10.0.0.0/24"}]}}` | matches messages that have sourceIPAddress within the cidr range specified (10.0.0.0->10.0.0.255) |
| /aws/lambda/\*MQFunctionAnythingBut\* | `{"data":{"address":{"state":[{"anything-but":"GA"}]}}}` | matches messages that have a value in address->state not equal to "GA" |
| /aws/lambda/\*MQFunctionAnd\* | `{"data":{"rating":[{"numeric":[">",0,"<=",5]}],"address":{"country":["USA"],"street":[{"exists":true}]}}}` | Logical AND. It will match any rating between 0 and 5 (excluding 0) AND the country needs to match AND the "street" key needs to be present (the exists filter only works on leaf nodes!) |
| /aws/lambda/\*MQFunctionOr\* | `{"data":{"rating":[4,5]}}, {"basicProperties":{"appId": ["myShinyApp"]}}, {"data":{"address":{"country":["USA"],"street":[{"exists":true}]}}}`| Logical OR. The filter will match if any of the rules match. Note this combines filters for both the message data and message properties passed from RabbitMQ. The appId property is "myShinyApp" OR Rating is 4 or 5 OR the OR (the country is "USA" and there is a street address present) |


## Cleanup
 
1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
1. Delete your secret from AWS Secrets Manager
    ```bash
    aws secretsmanager delete-secret --secret-id your-secret-id --force-delete-without-recovery
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
