# Multi-Day Scheduled Task Orchestration with AWS Lambda durable functions

This pattern demonstrates multi-day workflows with scheduled waits using AWS Lambda durable functions, showcasing automatic checkpointing and zero compute cost during wait periods.

**Important:** Check regional availability for AWS Lambda durable functions before deployment.

## Architecture

![Architecture Diagram](architecture.png)

The solution uses a streamlined architecture:
- **Durable Function**: Handles async scheduled task orchestration with 7-day workflow and automatic checkpointing
- **Task Management Function**: Unified function providing task listing, status queries, and deletion operations
- **DynamoDB**: Stores task state and progress for real-time monitoring
- **API Gateway**: RESTful API for task creation, status queries, and management

### Workflow Concept

The pattern demonstrates a multi-day workflow with scheduled waits between steps. Each step is automatically checkpointed, and the function incurs no compute charges during wait periods.





## Prerequisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed
* [Node.js 24+](https://nodejs.org/) installed

## Deployment

1. Navigate to the pattern directory:
   ```bash
   cd lambda-durable-scheduled-tasks-sam
   ```

2. Install dependencies:
   ```bash
   cd src && npm install && cd ..
   ```

3. Build the SAM application:
   ```bash
   sam build
   ```

4. Deploy the application:
   ```bash
   sam deploy --guided
   ```


5. Note the `TaskApiEndpoint` from the outputs.

## Testing

### Step 1: Get Your API Endpoint

Retrieve your API endpoint from the CloudFormation stack:

```bash
aws cloudformation describe-stacks \
  --stack-name lambda-durable-scheduled-tasks \
  --query 'Stacks[0].Outputs[?OutputKey==`TaskApiEndpoint`].OutputValue' \
  --output text
```

### Step 2: Start a Scheduled Task

Create a new scheduled task with custom configuration:

```bash
API_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name lambda-durable-scheduled-tasks \
  --query 'Stacks[0].Outputs[?OutputKey==`TaskApiEndpoint`].OutputValue' \
  --output text)

curl -X POST ${API_ENDPOINT}/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "config": {
      "reportType": "weekly",
      "dataSource": "analytics",
      "notifyEmail": "admin@example.com"
    }
  }'
```

Response:
```json
{
  "taskId": "TASK-1733328000000",
  "status": "INITIALIZED",
  "message": "Task started successfully"
}
```

### Step 3: Check Task Status

Query the task status to see progress:

```bash
TASK_ID="TASK-1733328000000"  # Use your actual task ID

curl ${API_ENDPOINT}/tasks/${TASK_ID}
```

Response:
```json
{
  "taskId": "TASK-1733328000000",
  "status": "DAY_3_COMPLETE",
  "currentDay": 3,
  "progress": {
    "percentage": 43,
    "completedDays": 3,
    "totalDays": 7,
    "steps": [
      {
        "day": 1,
        "action": "Data Collection",
        "result": {
          "records": 7543,
          "sources": ["database", "api", "files"]
        },
        "completedAt": "2024-12-04T10:00:00.000Z"
      },
      {
        "day": 2,
        "action": "Batch Processing",
        "result": {
          "recordsProcessed": 1823,
          "errors": 3
        },
        "completedAt": "2024-12-05T10:00:00.000Z"
      }
    ]
  },
  "config": {
    "reportType": "weekly",
    "dataSource": "analytics",
    "notifyEmail": "admin@example.com"
  },
  "startTime": "2024-12-04T10:00:00.000Z"
}
```

### Step 4: List All Tasks

View all tasks in the system:

```bash
curl ${API_ENDPOINT}/tasks
```

Response:
```json
{
  "tasks": [
    {
      "taskId": "TASK-1733328000000",
      "status": "DAY_3_COMPLETE",
      "currentDay": 3,
      "progress": {...}
    }
  ],
  "count": 1
}
```

### Step 5: Testing with Shorter Waits (Development)

For testing purposes, the default wait times are set to 1 minute. To test with real 24-hour intervals, modify the wait times in `src/index.js`:

```javascript
// Change from 1 minute to 24 hours for real intervals
await context.wait({ hours: 24 });  // Instead of { minutes: 1 }
```

This allows you to test the complete 7-day workflow in just 7 minutes during development.

### Step 6: Monitor Execution

View CloudWatch logs for detailed execution information:

```bash
aws logs tail /aws/lambda/lambda-durable-scheduled-tasks-ScheduledTask \
  --follow
```

### Step 7: View Final Report

Once the task completes (status: `COMPLETED`), retrieve the final report:

```bash
curl ${API_ENDPOINT}/tasks/${TASK_ID}
```

The response will include a `finalReport` field with comprehensive statistics:

```json
{
  "taskId": "TASK-1733328000000",
  "status": "COMPLETED",
  "finalReport": {
    "taskId": "TASK-1733328000000",
    "reportType": "weekly",
    "summary": {
      "totalDays": 7,
      "totalRecordsProcessed": 17543,
      "totalErrors": 23,
      "successRate": "99.87%"
    },
    "dailyBreakdown": [
      { "day": 1, "type": "collection", "records": 7543 },
      { "day": 2, "type": "processing", "records": 1823, "errors": 3 },
      { "day": 3, "type": "processing", "records": 1654, "errors": 5 }
    ],
    "generatedAt": "2024-12-11T10:00:00.000Z"
  }
}
```

## API Reference

### POST /tasks
Start a new scheduled task

**Request Body:**
```json
{
  "config": {
    "reportType": "weekly",
    "dataSource": "analytics",
    "notifyEmail": "admin@example.com"
  }
}
```

**Response:**
```json
{
  "taskId": "TASK-1733328000000",
  "status": "INITIALIZED",
  "message": "Task started successfully"
}
```

### GET /tasks
List all tasks

**Response:**
```json
{
  "tasks": [
    {
      "taskId": "TASK-1733328000000",
      "status": "DAY_3_COMPLETE",
      "currentDay": 3,
      "progress": {
        "percentage": 43,
        "completedDays": 3,
        "totalDays": 7,
        "steps": [...]
      },
      "config": {...},
      "startTime": "2024-12-04T10:00:00.000Z"
    }
  ],
  "count": 1
}
```

### GET /tasks/{taskId}
Get task status and progress

**Response:**
```json
{
  "taskId": "TASK-1733328000000",
  "status": "DAY_3_COMPLETE",
  "currentDay": 3,
  "progress": {
    "percentage": 43,
    "completedDays": 3,
    "totalDays": 7,
    "steps": [...]
  }
}
```

### DELETE /tasks
Delete all tasks from DynamoDB

**Response:**
```json
{
  "message": "All tasks deleted successfully",
  "deletedCount": 5
}
```

## Task Status Values

Tasks progress through various states from `INITIALIZED` to `COMPLETED` or `FAILED`, with intermediate checkpoints automatically saved.





## Cleanup

Delete the CloudFormation stack:

```bash
sam delete --stack-name lambda-durable-scheduled-tasks
```

## Learn More

- [AWS Lambda durable functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [JavaScript/TypeScript SDK](https://github.com/aws/aws-durable-execution-sdk-js)
- [AWS Blog Post](https://aws.amazon.com/blogs/aws/build-multi-step-applications-and-ai-workflows-with-aws-lambda-durable-functions/)


## License

This library is licensed under the MIT-0 License. See the LICENSE file.

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
