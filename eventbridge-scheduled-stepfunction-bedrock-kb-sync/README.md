# Amazon Bedrock Knowledge Base Synchronization Flow with EventBridge Scheduler 

This pattern demonstrates an automated synchronization process for Amazon Bedrock Knowledge Bases using Amazon EventBridge Scheduler and AWS Step Functions. The solution enables periodic synchronization of data sources, ensuring your Knowledge Base stays up-to-date with the latest content.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-scheduled-stepfunction-bedrock-kb-sync


Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture
![Architecture diagram](docs/images/KBSyncPipeline.jpg)

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/eventbridge-scheduled-stepfunction-bedrock-kb-sync/cdk
    ```
3. Setup local developer environment and dependencies:
    ```
    make bootstrap-venv
    source .venv/bin/activate
    ```
4. From the command line, configure AWS CDK:
   ```bash
   cdk bootstrap
   ```
5. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the `lib/appsync-eventbridge-datasource-stack.ts` file:
   ```bash
   cdk deploy --all
   ```
6. This command will take sometime to run. After successfully completing, the below stacks deployed.
```
KbRoleStack
CommonLambdaLayerStack
OSSStack
KbSyncPipelineStack
KbInfraStack
```

## How it works

Here's a detailed summary of your serverless pattern for automated Knowledge Base synchronization:

Pattern Overview: This is a scheduled, serverless workflow that automates the synchronization of Amazon Bedrock Knowledge Bases using AWS EventBridge Scheduler, AWS Step Functions, and Amazon Bedrock.

Key Components:
    a) EventBridge Scheduler
        - Runs every 15 minutes
        - Triggers the Step Function workflow
        - Passes Amazon Bedrock Knowledge Base ID as input parameter
        - Enables consistent and automated synchronization

    b) Step Functions Workflow
        -Main Flow:
        - Receives Knowledge Base ID from EventBridge
        - Orchestrates the entire synchronization process
        - Handles error scenarios and retries
        - Manages parallel processing of multiple data sources

    Step 1: Data Source Retrieval
        Queries all associated data sources for the given Knowledge Base ID
        Prepares the list for processing
        Validates data source configurations

    Step 2: Map State for Parallel Processing
        Iterates through each data source
        Processes multiple data sources concurrently
        Manages state for each sync operation

    Step 3: Synchronization Process (For each data source)
        Initiates the sync operation
        Monitors sync status
        Handles completion and failures
        Reports sync results

    Step 4: Status Reporting
        Aggregates sync results
        Records success/failure metrics
        Generates summary reports

## Testing

Step 1: Upload Sample Documents to Amazon S3
        - Navigate to Amazon S3 in AWS Console
        - Locate the bucket named kb-data-source-{account-id}
        - Upload your sample documents to this bucket

Step 2: Wait for Scheduler Execution
        - The EventBridge scheduler is configured to run every 15 minutes
        - You can monitor the scheduler in EventBridge console
        Note: The next execution will occur at the next 15-minute interval

Step 3: Monitor Step Function Execution
        - Navigate to AWS Step Functions console
        - Locate the state machine execution named KnowledgeBaseSyncStateMachine
        - Monitor the workflow progress through different states
        - Verify successful completion of all steps

Step 4: Verify Sync Status in Amazon Bedrock
        - Go to Amazon Bedrock console
        - Navigate to Knowledge Bases
        - Select your Knowledge Base
        - Click on Data Sources
        - Check the Sync History tab
        - Verify the sync status shows as "Completed"
        - Review sync details including:
            Timestamp of sync
            Number of documents processed
            Any errors or warnings


Step 45: Validation Points
        - Confirm documents are indexed
        - Check sync completion status
        - Verify no errors in sync history
        - Ensure all uploaded documents are processed

Troubleshooting
If sync fails or documents aren't appearing:

    Check S3 bucket permissions
    Review Step Function execution logs
    Verify document format compatibility
    Check Knowledge Base configuration

![KB Pipeline Architecture](docs/images/KBSyncPipeline.png)

## Delete stack

```bash
cdk destroy --all
```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
