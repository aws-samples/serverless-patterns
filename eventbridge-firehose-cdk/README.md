# AWS Service 1 to AWS Service 2

This pattern << explain usage >>

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
2. Change directory to the pattern directory:
    ```
    cd _patterns-model
    ```
3. Bootstrap environment -- only if you haven't already 
    ```
    cdk bootstrap
    ```

4.  Deploy the stack to your default AWS account and region:
    ```
    cdk deploy
    ```
## How it works

The CDK stack deploys the resources and the IAM permissions required to run the application.

The EventBridge rule filters the events based upon the defined criteria. When matching events are sent to EventBridge that trigger the rule, they are delivered as a JSON event payload to the Kinesis Firehose Delivery Stream. The Kinesis Firehose then delivers the JSON object to the S3 Destination bucket.

Depending on intended use, Kinesis Firehose Transformations, partitioning, compression etc. can be applied. 

## Testing

Use the [AWS CLI](https://aws.amazon.com/cli/) to send a test event to EventBridge and observe the event delivered to the Lambda function by reviewing the Amazon CloudWatch Logs associated with the function:

1. Send an event to EventBridge:

```
aws events put-events --entries file://event.json
```

2. Check that test events are being sent to the destination S3 bucket (it will take a few minutes for events to begin streaming):

```
aws s3 ls s3://{destination bucket name} --recursive --human-readable --summarize
```

3. Check the destination S3 bucket to see that test item was delivered. 


## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
```

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
