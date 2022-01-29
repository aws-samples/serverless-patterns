# CloudWatch RUM with Cognito Identity Pool

This pattern creates a CloudWatch RUM application monitor and an associated Cognito IdentityPool. 

The Cognito Identity Pool is configured to allow unauthenticated access to the CloudWatch RUM web client in order to publish generated events.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/cloudwatch-rum-cognito](https://serverlessland.com/patterns/cloudwatch-rum-cognito)

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
    cd cloudwatch-rum-cognito
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the Application Name
    * Enter the Application Domain
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

Once the template has been deployed you will need to login to the AWS Console and navigate to CloudWatch RUM and identify your application monitor.

Within the application monitor you should see an option for copying/downloading the JavaScript code snippet. This is specific to this CloudWatch RUM application monitor and is used by your application in order for it to sent events back to the service.

If required you can modify the code snippet to configure the CloudWatch RUM web client. See the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-modify-snippet.html) for further information.

## Testing

1. Insert the JavaScript snippet code into your application. It needs to be added within the `<head>` element
2. Deploy your application
3. Use your application to generate events
4. Look at the AWS CloudWatch RUM console for the application monitor and you should be able to see the last updated time and also start to see the events.

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
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
