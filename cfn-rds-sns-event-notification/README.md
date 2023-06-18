# Amazon RDS to Amazon SNS

RDS Event Subscriptions allow users to configure notifications for RDS Events (provided through an SNS topic). This template configures an event subscription for failure, low storage, and availability event categories for RDS Instances.

Learn more about this pattern at Serverless Land Patterns:https://serverlessland.com/patterns/cfn-rds-sns-event-notification

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
- [Create an RDS Instance and copy Name of RDS Instance somewhere in notes. You will need it during template deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html#USER_CreateDBInstance.Creating)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
1. Change directory to the pattern directory:
   ```
   cd cfn-rds-sns-event-notification
   ```
1. From the command line, use AWS CLI to deploy the AWS resources for the pattern as specified in the template.yml file:
   ```
   aws cloudformation create-stack --stack-name <NameOfTheStack> --template-body file://template.yaml --parameters ParameterKey=SNSEndpoint,ParameterValue=<EmailID> ParameterKey=RDSInstanceName,ParameterValue=<NameOfTheDatabase> ParameterKey=Name,ParameterValue=<NameOfTheTopic>
   ```
1. You can also use AWS CloudFormation console and paste the template.yml file in the designer and deploy it by passing the below required parameters.

   - Enter a stack name
   - Enter a topic name
   - In SNSEndpoint, Provide your email address to receive notification from Amazon SNS
   - In RDSInstanceName, Provide name of RDS Instance you created during Deployment instructions

## How it works

RDS Event Subscriptions allow users to configure notifications for RDS Events (provided through an SNS topic). This template configures an event subscription for failure, low storage, and availability event categories for RDS Instances.

## Testing

Once the CFN deployment is successful, first thing to do is to confirm the Email subscription. You will receive an email to confirm it. Then go to RDS console. Select the RDS Instance you have created. Stop the Instance and Restart it again. You will receive a notification related to it on your Email Address. Moving forward, you will receive failure, low storage, and availability events that happen on your RDS Instance.

## Cleanup

1. Delete the stack
   ```bash
   aws cloudformation delete-stack --stack-name <NameOfTheStack>
   ```
1. Confirm the stack has been deleted
   ```bash
   aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
   ```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0