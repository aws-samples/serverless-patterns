# AWS Systems Manager Automation to AWS Lambda

This SAM template deploys an AWS Systems Manger Automation Document that consumes input parameters at execution time and invokes a Lambda function by passing the parameters as input payload for the Lambda function. The template also deploys the Lambda function, required IAM permissions to execute the automation and a sample DynamoDB table used to test the pattern.

(**Note**: DynamoDB is used in this repo just for demonstration purposes. You may use this pattern across multiple services as needed.)

This Systems Manager Automation Document used in this pattern contains one step that invokes the Lambda function. However, you can use this in documents with multiple steps as well. To learn more about Systems Manger Documents, refer to https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/ssm-lambda.

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
    cd systems-manager-automation-to-lambda
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the following output Values from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

    * ```
      DynamoDBTableName
      ```

    * ```
      SystemsManagerAutomationDocumentName
      ```  


## How it works

When the Systems Manger Automation Document is invoked, the execution parameters are sent as a payload to invoke the Lambda function, which updates the DynamoDB table's items with the parameters from the automation execution.

## Testing

1. After the stack is deployed, run this command to scan the DynamoDB table for items. This should be empty initially.

   ```
   aws dynamodb scan --table-name <$DynamoDBTableName>
   ```

2. Start the Automation Execution by passing in the parameter values of your choice for "$album_name" and "$artist_name" (Note that these values should be of the type 'String')

    ```
    aws ssm start-automation-execution --document-name <$SystemsManagerAutomationDocumentName> --parameters "DocumentInputTableName=<$DynamoDBTableName>, PartitonKeyInput=<$album_name>, SortKeyInput=<$artist_name>"
    ```  
3. Get the value of the `AutomationExecutionId` from the previous step's output and run the following command to verify the execution ran successfully.

    ```
    aws ssm get-automation-execution --automation-execution-id <$AutomationExecutionId> --query '[AutomationExecution][0].AutomationExecutionStatus'
    ```

4. Once the Execution Status is "success", you can validate this by scanning the dynamoDB table once again. This should return the item(s) you passed in step 2.

    ```
    aws dynamodb scan --table-name <$DynamoDBTableName>
    ```

## Cleanup

1. Delete the stack
    ```
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
