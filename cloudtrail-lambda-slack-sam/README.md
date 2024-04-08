# AWS Lambda and Cloudtrail data events

![Concept](./cloudtrail-lambda-slack-sam.png)

This pattern demonstrates how customers can monitor manual invocations of their sensitive lambda functions through slack with the help of Cloudtrail and Cloudwatch Subscription filter.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudtrail-lambda-slack-sam

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have, create them and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Testing

Invoke the lambda function manually from the console and after 5 minutes you should see the message in your slack channel showing the user invocation.

```

#sample message:
User 'arn:aws:iam::<account-id>:user/RogueUser' performed Invoke on function 'arn:aws:lambda:us-east-1:<account-id>:function:testfunction' at 2023-03-27T13:04:09Z


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/cloudtrail-lambda-slack-sam
    ```
1. From the command line, run the sam command as follows:
```
sam deploy --stack-name {give a stack name} --parameter-overrides S3bucketname={Give a unique bucket name} SlackWebhookUrl={Add your channel url here} LambdaList="{FunctionA ARN}","{FunctionB ARN}"  --capabilities CAPABILITY_NAMED_IAM
```

1. Note the outputs from the deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates an AWS Cloudtrail for capturing data events of your lambda function to be monitored and the events will be pushed to Cloudwatch logs. It will also create a Lambda function which will have the code to push Slack notifications for the events fetched from the Cloudwatch using subscription filter to fetch only IAM user events.


## Testing

Open the lambda function which you added to monitor and manually test invoke it. After 5 minutes you should see the message in your slack channel showing the user invocation.

#sample message:
```
User 'arn:aws:iam::<account-id>:user/RogueUser' performed Invoke on function 'arn:aws:lambda:us-east-1:<account-id>:function:testfunction' at 2023-03-27T13:04:09Z
```

## Cleanup
 
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/cloudtrail-lambda-slack-sam
    ```
1. Delete all created resources
    ```
    sam delete --stack-name {your stack name}
    ```

----
Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0

