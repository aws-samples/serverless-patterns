# Amazon EventBridge to Amazon CloudWatch

This project contains a sample AWS CDK template to create an EventBridge Rule and a CloudWatch Logs log group. The EventBridge Rule publishes matched events to the log group. In this example, the rule filters for specific attributes in the event before sending to the target.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-cloudwatch-cdk-java.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed and configured
  
## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change the working directory to this pattern's directory
    ```
    cd serverless-patterns/eventbridge-cloudwatch-cdk-java
    ```

3. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap ACCOUNT-NUMBER/REGION # e.g.
   cdk bootstrap 1111111111/us-east-1
   cdk bootstrap --profile test 1111111111/us-east-1
   ```
4. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/cdk-stack.ts` file:
   ```bash
   cdk deploy
   ```
5. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge rule filters the events based upon the defined criteria. Matched events are published to the CloudWatch Logs log group.

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the event delivered to the Amazon CloudWatch by reviewing the logs:

1. Send an event to EventBridge:

```sh
aws events put-events --entries file://event.json
```

2. Check CloudWatch Logs, referencing the log group name from the stack's Outputs section, to see an event matching this example:
```json
{
    "Version": "0",
    "Account": "123456789012",
    "Region": "eu-west-2",
    "Detail": {
        "location": "EUR-"
    },
    "detail-type": "transaction",
    "Source": "cdk.myapp",
    "Time": "2022-05-01T21:32:11Z",
    "Id": "879bd868-08b4-6d45-ea11-252978d0a332",
    "Resources": []
}
```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
