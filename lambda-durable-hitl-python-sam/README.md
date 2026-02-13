# Lambda Durable Functions with Human-in-the-Loop (HITL) Pattern

This pattern demonstrates how to implement AWS Lambda Durable Functions with Human-in-the-Loop capabilities using Python 3.13 and the AWS Durable Execution SDK. The pattern showcases how Lambda functions can pause execution, wait for human approval, and resume based on human decisions while maintaining state across the pause/resume cycle.

## Overview

This serverless pattern enables workflows that require human decision-making by pausing Lambda execution, notifying approvers, and resuming based on their decisions. The pattern uses AWS Lambda Durable Functions to maintain execution state across pauses and resumes, making it ideal for approval workflows, content moderation, and any process requiring human judgment.

**Key Features:**
- Durable execution with checkpointed steps (no re-execution on replay)
- Polling-based approval checking with no compute charges during waits
- Automatic timeout handling for overdue approvals
- Complete audit trail in DynamoDB
- SNS notifications for approvers
- CLI tool for testing and managing approvals

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Initiator Layer                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐              ┌──────────────────────────┐    │
│  │  CLI Tool    │              │  Test Invocation         │    │
│  │              │              │  (Manual/Automated)      │    │
│  └──────┬───────┘              └────────┬─────────────────┘    │
│         │                               │                       │
└─────────┼───────────────────────────────┼───────────────────────┘
          │                               │
          │ (6) List/Submit               │ (1) Invoke
          │     Decision                  │     Workflow
          │                               │
┌─────────▼───────────────────────────────▼───────────────────────┐
│                      AWS Lambda Layer                            │
├──────────────────────────────────────────────────────────────────┤
│  ┌────────────────────────────────┐  ┌──────────────────────────┐  │
│  │  Workflow Lambda               │  │  Approval API Lambda     │  │
│  │  (Durable Execution)           │  │                          │  │
│  │                                │  │  - Get approval request  │  │
│  │  - Create approval request     │  │  - Validate status       │  │
│  │  - Pause with callback         │  │  - Invoke callback       │  │
│  │  - Send notification           │  │  - Update status         │  │
│  │  - Resume on callback          │  │                          │  │
│  └────┬───────────────────┬───────┘  └──────────┬───────────────┘  │
│       │                   │                      │                   │
└───────┼───────────────────┼──────────────────────┼───────────────────┘
        │                   │                      │
        │ (2) Store         │ (4) Notify           │ (8,10) Get/Update
        │     Request       │                      │        Status
        │                   │                      │
┌───────▼───────────────────┼──────────────────────▼───────────────────┐
│                    Storage & Notification Layer                       │
├───────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐         ┌──────────────────────────┐       │
│  │  DynamoDB Table     │         │  SNS Topic               │       │
│  │  ApprovalRequests   │         │  ApprovalNotifications   │       │
│  │                     │         │                          │       │
│  │  - approval_id (PK) │         │  - Sends notifications   │       │
│  │  - callback_token   │         │    to approvers          │       │
│  │  - document details │         │                          │       │
│  │  - status           │         └────────┬─────────────────┘       │
│  │  - timestamps       │                  │                         │
│  └─────────────────────┘                  │ (5) Notification        │
│                                            │                         │
└────────────────────────────────────────────┼─────────────────────────┘
                                             │
                                             ▼
                                    ┌────────────────┐
                                    │   Approver     │
                                    │   (Human)      │
                                    └────────────────┘
```

### Components

1. **Workflow Lambda** (`src/workflow/`): Orchestrates the approval workflow using AWS Lambda Durable Functions SDK. It creates approval requests, polls DynamoDB for decisions using durable waits (no compute charges), sends notifications, and completes when a decision is made. Uses `@durable_execution` and `@durable_step` decorators for checkpointing.

2. **Approval API Lambda** (`src/approval_api/`): Processes approval/rejection decisions. It validates requests, updates the approval status in DynamoDB, allowing the workflow to detect the decision and resume.

3. **Shared Module** (`src/shared/`): Contains common code used by both Lambda functions:
   - `models.py`: Data models (WorkflowEvent, ApprovalRequest, WorkflowResult, Decision enum)
   - `dynamodb_operations.py`: DynamoDB operations (create/update approval requests)

4. **DynamoDB Table**: Stores approval request state including document details, status, and timestamps. Uses a Global Secondary Index (StatusIndex) for querying pending approvals.

5. **SNS Topic**: Sends notifications to approvers when new approval requests are created, including approval details and expiration time.

### Execution Flow

1. Test invocation triggers Workflow Lambda with document details (asynchronous invocation required for ExecutionTimeout > 15 minutes)
2. Workflow Lambda creates approval request in DynamoDB (checkpointed step)
3. Workflow Lambda sends SNS notification to approvers (checkpointed step)
4. Workflow Lambda polls DynamoDB every 5 seconds using durable waits (no compute charges during waits)
5. SNS delivers notification to approver
6. Approver invokes Approval API Lambda to submit decision
7. Approval API Lambda updates status in DynamoDB
8. Workflow Lambda detects decision change during next poll
9. Workflow Lambda completes and returns result

**Important**: Durable functions with ExecutionTimeout > 900 seconds (15 minutes) must be invoked asynchronously using `--invocation-type Event`.

## Project Structure

```
lambda-durable-hitl-python-sam/
├── src/
│   ├── approval_api/            # Approval API Lambda function
│   │   ├── app.py              # Processes approval decisions
│   │   ├── Dockerfile          # Container image definition
│   │   └── requirements.txt    # Function dependencies
│   ├── shared/                  # Shared code between Lambda functions
│   │   ├── __init__.py
│   │   ├── models.py           # Data models (WorkflowEvent, ApprovalRequest, etc.)
│   │   └── dynamodb_operations.py  # DynamoDB helper functions
│   └── workflow/                # Workflow Lambda function (durable execution)
│       ├── app.py              # Main workflow orchestrator
│       ├── Dockerfile          # Container image definition
│       └── requirements.txt    # Function dependencies (includes aws-durable-execution-sdk-python)
├── template.yaml               # SAM template (infrastructure as code)
├── example-pattern.json        # Pattern metadata for serverless-patterns repository
├── .gitignore                  # Git ignore patterns
└── README.md                   # This file
```

### Folder Purposes

- **src/approval_api/**: Lambda function that processes approval/rejection decisions. Validates requests, updates DynamoDB status, allowing the workflow to detect decisions and complete.

- **src/shared/**: Common code shared between both Lambda functions. Contains data models (WorkflowEvent, ApprovalRequest, WorkflowResult, Decision enum) and DynamoDB operations (create/update approval requests). Prevents code duplication.

- **src/workflow/**: Main durable execution Lambda function that orchestrates the approval workflow. Uses AWS Durable Execution SDK with `@durable_execution` and `@durable_step` decorators for checkpointing. Polls DynamoDB for decisions using durable waits.

### Key Files

- **template.yaml**: Defines all AWS resources (Lambda functions, DynamoDB table, SNS topic, IAM roles)
- **src/workflow/app.py**: Main durable execution logic with `@durable_execution` decorator
- **src/approval_api/app.py**: Handles approval/rejection decisions
- **src/shared/**: Common code shared between Lambda functions

## Prerequisites

- AWS CLI configured with appropriate credentials
- AWS SAM CLI installed (version 1.100.0 or later)
- Python 3.13 or later
- Docker (for building Lambda container images)
- An AWS account with permissions to create Lambda functions, DynamoDB tables, SNS topics, and IAM roles

## Deployment

### Step 1: Clone and Navigate

```bash
cd lambda-durable-hitl-python-sam
```

### Step 2: Build the Application

```bash
sam build
```

This command builds the Lambda container images and prepares the application for deployment.

### Step 3: Deploy to AWS

For first-time deployment:

```bash
sam deploy --guided
```

You'll be prompted for:
- Stack name (e.g., `lambda-durable-hitl-stack`)
- AWS Region (e.g., `us-east-1`)
- Confirmation for creating IAM roles
- Confirmation for deploying without authorization

For subsequent deployments:

```bash
sam deploy
```

### Step 4: Note the Outputs

After deployment, SAM will output important values:
- `WorkflowFunctionName`: Name of the Workflow Lambda function
- `ApprovalApiFunctionName`: Name of the Approval API Lambda function
- `ApprovalsTableName`: Name of the DynamoDB table
- `SnsTopicArn`: ARN of the SNS topic

Save these values for testing.

## Important Notes

### Durable Function Invocation

- **Asynchronous invocation required**: Durable functions with `ExecutionTimeout > 900 seconds` (15 minutes) MUST be invoked asynchronously using `--invocation-type Event`
- **Version requirement**: You must publish a Lambda version before invoking a durable function (cannot use `$LATEST` or unqualified ARN)
- **No synchronous response**: Asynchronous invocation returns immediately with a 202 status; check DynamoDB or CloudWatch Logs for results

### Polling vs Callback Pattern

This implementation uses a **polling pattern** where the workflow checks DynamoDB every 5 seconds for approval decisions:
- **Advantages**: Simpler implementation, no callback token management, easier to test
- **Durable waits**: Uses `context.wait(Duration.from_seconds(5))` which incurs no compute charges during waits
- **Checkpointing**: Each poll is a checkpointed step, so on replay it won't re-execute completed checks

### Configuration

The SAM template configures the following environment variables:

**Workflow Lambda:**
- `APPROVALS_TABLE_NAME`: DynamoDB table name for approval requests
- `SNS_TOPIC_ARN`: SNS topic ARN for notifications
- `APPROVAL_TIMEOUT_SECONDS`: Default timeout in seconds (default: 300 for testing, can be increased to 3600 for production)

**Approval API Lambda:**
- `APPROVALS_TABLE_NAME`: DynamoDB table name for approval requests

### Customizing Timeout

To change the default approval timeout, update the `ApprovalTimeoutSeconds` parameter in `template.yaml`:

```yaml
Parameters:
  ApprovalTimeoutSeconds:
    Type: Number
    Default: 3600  # 1 hour for production
    Description: Default timeout for approval requests in seconds
    MinValue: 60
    MaxValue: 86400
```

Or pass it during deployment:

```bash
sam deploy --parameter-overrides ApprovalTimeoutSeconds=7200
```

## Testing

### Testing with AWS CLI

All testing can be done using standard AWS CLI commands. No additional tools required.

#### Step 1: Set Environment Variables

```bash
export AWS_DEFAULT_REGION=us-east-1
export STACK_NAME=app-sam  # Your CloudFormation stack name

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

#### Step 2: Invoke the Workflow

```bash
# Publish a Lambda version (required for durable functions)
export WORKFLOW_VERSION=$(aws lambda publish-version \
  --function-name $WORKFLOW_FUNCTION \
  --query 'Version' \
  --output text)

# Invoke workflow asynchronously (required for ExecutionTimeout > 15 minutes)
aws lambda invoke \
  --function-name $WORKFLOW_FUNCTION:$WORKFLOW_VERSION \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{"document_id":"doc-123","document_name":"Q4 Budget Proposal","requester":"user@example.com"}' \
  response.json

# Check response (should show StatusCode: 202)
cat response.json
```

#### Step 3: List Pending Approvals

```bash
# Scan DynamoDB for pending approval requests
aws dynamodb scan \
  --table-name $STACK_NAME-ApprovalRequests \
  --filter-expression "#status = :pending" \
  --expression-attribute-names '{"#status":"status"}' \
  --expression-attribute-values '{":pending":{"S":"pending"}}' \
  --max-items 10
```

Or get all items:

```bash
aws dynamodb scan --table-name $STACK_NAME-ApprovalRequests --max-items 10
```

#### Step 4: Get Approval Details

```bash
# Get specific approval request by ID
aws dynamodb get-item \
  --table-name $STACK_NAME-ApprovalRequests \
  --key '{"approval_id":{"S":"<APPROVAL_ID>"}}'
```

#### Step 5: Submit Approval Decision

**Approve a request:**

```bash
aws lambda invoke \
  --function-name $APPROVAL_API_FUNCTION \
  --cli-binary-format raw-in-base64-out \
  --payload '{"action":"decide","approval_id":"<APPROVAL_ID>","decision":"approved","approver":"test-approver","comments":"Looks good, approved"}' \
  approval_response.json

# Check response
cat approval_response.json
```

**Reject a request:**

```bash
aws lambda invoke \
  --function-name $APPROVAL_API_FUNCTION \
  --cli-binary-format raw-in-base64-out \
  --payload '{"action":"decide","approval_id":"<APPROVAL_ID>","decision":"rejected","approver":"test-approver","comments":"Needs revision"}' \
  approval_response.json

# Check response
cat approval_response.json
```

#### Step 6: Verify Workflow Completion

```bash
# Check DynamoDB to verify status changed
aws dynamodb get-item \
  --table-name $STACK_NAME-ApprovalRequests \
  --key '{"approval_id":{"S":"<APPROVAL_ID>"}}'

# Check CloudWatch Logs for workflow completion
aws logs tail /aws/lambda/$WORKFLOW_FUNCTION --follow
```

### Testing Timeout Scenarios

To test timeout handling, invoke the workflow with a short timeout:

```bash
# Invoke workflow with 60-second timeout
aws lambda invoke \
  --function-name $WORKFLOW_FUNCTION:$WORKFLOW_VERSION \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload '{"document_id":"doc-456","document_name":"Test Doc","requester":"user@example.com","timeout_seconds":60}' \
  response.json
```

Wait for the timeout to expire (60 seconds), then check the approval status:

```bash
# Get approval_id from DynamoDB
aws dynamodb scan --table-name $STACK_NAME-ApprovalRequests --max-items 5

# Check status - should show "timeout"
python approval_cli.py get <approval_id>
```

The status should show "timeout" and the workflow will have completed automatically.

### Running Unit Tests

```bash
# Install test dependencies
pip install -r tests/requirements.txt

# Run all tests
pytest tests/unit/

# Run with coverage
pytest tests/unit/ --cov=src --cov-report=html
```

### Running Property-Based Tests

```bash
# Run property tests
pytest tests/property/

# Run specific property test
pytest tests/property/test_approval_properties.py::test_unique_approval_identifiers
```

## Use Cases

### Document Approval Workflow

The primary use case demonstrated in this pattern is document approval. When a document is submitted for review:

1. The workflow pauses and creates an approval request
2. Approvers receive a notification via SNS
3. Approvers review the document and submit their decision via CLI
4. The workflow resumes with the approval decision
5. The system records the decision, comments, and timestamp

This pattern is ideal for:
- Contract approvals
- Policy document reviews
- Technical design document approvals
- Budget proposal reviews

### Expense Approval System

This pattern can be adapted for expense approval workflows:

1. Employee submits an expense report
2. Workflow pauses and notifies the manager
3. Manager reviews and approves/rejects via CLI or web interface
4. Workflow resumes and processes the expense accordingly
5. System maintains audit trail of all decisions

Key benefits:
- Automatic timeout for overdue approvals
- Complete audit trail in DynamoDB
- Scalable to handle high volumes of expense requests

### Content Moderation Workflow

For content moderation scenarios:

1. User-generated content triggers the workflow
2. Content is flagged for human review
3. Moderator receives notification
4. Moderator reviews and approves/rejects content
5. Workflow resumes and publishes or removes content

Advantages:
- Durable execution ensures no content is lost during review
- Timeout handling for content that requires urgent decisions
- Flexible decision recording with comments

## Cleanup

To remove all resources created by this pattern:

```bash
sam delete
```

This will delete:
- Lambda functions (Workflow and Approval API)
- DynamoDB table (ApprovalRequests)
- SNS topic (ApprovalNotifications)
- IAM roles and policies
- CloudWatch log groups

**Note**: If you've subscribed email addresses to the SNS topic, you'll need to manually unsubscribe them before deletion.

## Security Considerations

- IAM roles follow least privilege principle
- DynamoDB table uses encryption at rest
- Callback tokens are not exposed in logs or error messages
- API Gateway validates request parameters before processing
- All input data is validated before processing

## Cost Considerations

This pattern uses the following AWS services:
- **Lambda**: Pay per invocation and execution time
- **DynamoDB**: On-demand billing for read/write requests
- **SNS**: Pay per notification sent
- **CloudWatch Logs**: Pay for log storage and ingestion

Estimated cost for 1,000 approval requests per month: < $1 USD

## Limitations

- Maximum durable execution timeout: 1 year (configurable via `DurableConfig.ExecutionTimeout`)
- Synchronous invocation only supported for ExecutionTimeout ≤ 900 seconds (15 minutes)
- Must publish Lambda version before invoking durable function (cannot use $LATEST)
- DynamoDB item size limit: 400 KB
- SNS message size limit: 256 KB
- Lambda container image size limit: 10 GB
- Polling interval: 5 seconds (configurable in workflow code)

## Additional Resources

- [AWS Lambda Durable Functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
- [DynamoDB Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
- [SNS Documentation](https://docs.aws.amazon.com/sns/)

## License

This pattern is released under the MIT-0 License. See the LICENSE file for details.
