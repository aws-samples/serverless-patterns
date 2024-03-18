# AWS Systems Manager Automation to AWS Step Functions

This SAM template deploys an AWS Systems Manger Automation Document that consumes input parameters at execution time and invokes Step functions by passing the parameters as input payload for the Step function. The template also deploys Lambda functions, required IAM permissions to execute the automation and a sample RDS table used to take the snapshot.

(**Note**: RDS is used in this repo just for demonstration purposes. You may use this pattern across multiple services as needed.)

This Systems Manager Automation Document used in this pattern contains one step that invokes the Step functions. However, you can use this in documents with multiple steps as well. To learn more about Systems Manger Documents, refer to https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/systems-manager-automation-to-stepfunctions.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd systems-manager-automation-to-stepfunctions
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
    ```
4. During the prompts:
    * Enter a stack name : STACK_NAME
    * Enter the desired AWS Region: AWS_REGION
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided --capabilities CAPABILITY_NAMED_IAM` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.


## How it works

When the Systems Manger Automation Document is invoked, the execution parameters are sent as a payload to invoke the Step function, which takes the snapshot of RDS table's items with the parameters from the automation execution.

## Testing

1. After the stack is deployed, navigate to Systems Manager Automation, select the Automation document owned by me and select execetion Automation. Enter the RDS DB name from SAM template execuion Outputs section as Automation Execution input value to start the execution i.e. "sam-app-rdsdatabase-xxxx". This should be empty initially. (Note that these values should be of the type 'String' and "instance_id" is the rds_db_name)

2. In Automation Document execution details allow you to observe overall status along with execution output from Stepfunction.

3. Further more In  Step functions, the Graph view will allow you to observe overal proccess of your execution from Start to end.
You can Monitor all the steps while the execution is in progress.

4. Once the Execution Status is "Success", you can validate this by navigating to RDS, Snapshots in order to see your newly created snapshots.

## Cleanup

1. Delete the SAM Template
    ```
    sam delete
    ```
1. Confirm the stack has been deleted
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
