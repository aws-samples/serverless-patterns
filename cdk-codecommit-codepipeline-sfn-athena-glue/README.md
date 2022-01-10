# AWS CodeCommit -> CodePipeline -> SFN -> Athena -> Glue

This pattern in CDK offers an example to generate an AWS Code Pipeline which invokes Steps Functions to execute Athena Named Queries in Glue Data Catalog.

![Pattern](./pattern.png "Patern")

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/codepipeline-sfn-glue-cdk.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed
## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd cdk-codecommit-codepipeline-sfn-athena-glue
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```bash
      npx cdk bootstrap aws://accountnumber/region
      npx cdk synth
      npx cdk deploy
    ```

## How it works

CDK CodePipeline is spin up against AWS CodeCommit repository, which will trigger AWS StepFunction to call AWS Athena NamedQueries to create Views and Tables.

Branch Name and CodeCommit repository details needs to be provided in the configuration file `src/config.ts`.

If the s3 stack fails due to already existing s3 bucket name, simpley change the prefix (from `src/config.ts`) to some random unique value with 8-12 characters. This will make s3 Buckets name unique.

## Testing

1. Deploy the app, by specifying account and region within configurations. On successful creation you can see CodePipline on AWS management Console.
2. Under Step Functions, step function will be created named `test-QueryFlows`, which will have execution and defination, which contain AWS Athena NamedQueries.
3. On successful execution of pipeline, Table named `emp_master`, `emp_details` will be created in `EmployeeRoster` Database along with view `emp_roster`.
4. Pipleine named `DemoPipeline-NonProd` will be created that will have stage to run the athena query based state machine.

## Handing Errors
1. If Pipline is failed due to not having permission to `states:DescribeExecution`, then its requested to add the below inline policy under the role created.

```bash
{
    "Action": "states:DescribeExecution",
    "Resource": "arn:aws:states:{region}:{account}:execution:{stateMachineName}:*",
    "Effect": "Allow"
}
```

## Cleanup

1. Delete the stack
    ```bash
    aws cloudformation delete-stack --stack-name STACK_NAME
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```
1. ```bash
    cdk destroy
   ```
----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
