# AWS Lambda durable functions to DynamoDB with Human-in-the-Loop

This pattern demonstrates how to implement Lambda durable functions with Human-in-the-Loop (HITL) approval workflows. The workflow pauses execution, waits for human approval via callback, and resumes based on the decision while maintaining state across the pause/resume cycle.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-hitl-python-sam

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Docker](https://docs.docker.com/get-docker/) installed (for building Lambda container images)
* [Python 3.13](https://www.python.org/downloads/) or later

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd lambda-durable-hitl-python-sam
    ```
1. From the command line, use AWS SAM to build the application:
    ```
    sam build
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yaml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Enter the ApprovalTimeoutSeconds parameter (default: 300 seconds)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern implements a Human-in-the-Loop approval workflow using Lambda durable functions:

1. **Workflow Lambda** creates an approval request in DynamoDB and sends an SNS notification to approvers
2. The workflow pauses execution using `callback.result()` and waits for a callback
3. **Approval API Lambda** processes the approval decision and calls the Lambda durable execution callback API
4. The workflow resumes automatically when the callback is invoked and completes with the decision

The pattern uses the AWS Durable Execution SDK for Python with the `@durable_execution` decorator to maintain state across the pause/resume cycle. The callback pattern ensures no compute charges while waiting for human decisions.

### Architecture Components

- **Workflow Lambda**: Orchestrates the approval workflow using Lambda durable functions SDK with callback pattern
- **Approval API Lambda**: Processes approval/rejection decisions and invokes the callback API to resume the workflow
- **DynamoDB Table**: Stores approval request state including callback tokens, document details, and timestamps
- **SNS Topic**: Sends notifications to approvers when new approval requests are created

## Testing

### Set Environment Variables

```bash
export AWS_DEFAULT_REGION=us-east-1
export STACK_NAME=<your-stack-name>

# Get function names from CloudFormation outputs
export WORKFLOW_FUNCTION=$(aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --query 'Stacks[0].Outputs[?OutputKey==`WorkflowFunctionName`].OutputValue' \
  --output text)

export APPROVAL_API_FUNCTION=$(aws cloudformation describe-stacks \
  --stack-name $STACK_NAME \
  --query 'Stacks[0].Outputs[?OutputKey==`ApprovalApiFunctionName`].OutputValue' \
  --output text)
```

### Invoke the Workflow

```bash
# Invoke workflow with a document approval request
aws lambda invoke \
  --function-name $WORKFLOW_FUNCTION \
  --cli-binary-format raw-in-base64-out \
  --payload '{"document_id":"doc-123","document_name":"Q4 Budget Proposal","requester":"user@example.com"}' \
  response.json

# Check response
cat response.json
```

### List Pending Approvals

```bash
# Scan DynamoDB for pending approval requests
aws dynamodb scan \
  --table-name $STACK_NAME-ApprovalRequests \
  --filter-expression "#status = :pending" \
  --expression-attribute-names '{"#status":"status"}' \
  --expression-attribute-values '{":pending":{"S":"pending"}}' \
  --max-items 10
```

### Submit Approval Decision

```bash
# Get the approval_id from the DynamoDB scan output above

# Approve the request
aws lambda invoke \
  --function-name $APPROVAL_API_FUNCTION \
  --cli-binary-format raw-in-base64-out \
  --payload '{"action":"decide","approval_id":"<APPROVAL_ID>","decision":"approved","approver":"test-approver","comments":"Looks good"}' \
  approval_response.json

# Check response
cat approval_response.json
```

### Verify Workflow Completion

```bash
# Check DynamoDB to verify status changed to approved
aws dynamodb get-item \
  --table-name $STACK_NAME-ApprovalRequests \
  --key '{"approval_id":{"S":"<APPROVAL_ID>"}}'

# Check CloudWatch Logs for workflow completion
aws logs tail /aws/lambda/$WORKFLOW_FUNCTION --follow
```

Expected output: The workflow should complete and return the approval decision. The DynamoDB item should show status as "approved" with the approver's comments and timestamp.

A successful test shows these log messages:
- Workflow logs: `Callback created` → `Approval request created` → `SNS notification sent` → `Waiting for approval callback`
- After approval: `Callback received, workflow resuming` → `Workflow completed successfully` with decision "approved"

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
1. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'$STACK_NAME')].StackStatus"
    ```

----
Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
