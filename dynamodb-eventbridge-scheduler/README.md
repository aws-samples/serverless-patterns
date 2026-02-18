# Dynamic Amazon EventBridge Scheduler from Amazon DynamoDB Streams

This pattern demonstrates how to dynamically create, update, and delete Amazon EventBridge Scheduler schedules based on changes in a DynamoDB table using DynamoDB Streams.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns

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
    cd serverless-patterns/dynamodb-eventbridge-scheduler
    ```
3. From the command line, use AWS SAM to build and deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern creates a serverless solution that automatically manages EventBridge Scheduler schedules based on DynamoDB table changes:

1. **DynamoDB Table** (`ScheduleConfigs`) - Stores schedule configurations with streams enabled
2. **Stream Processor Lambda** - Automatically triggered by DynamoDB Stream events to:
   - Create schedules when items are inserted
   - Update schedules when items are modified
   - Delete schedules when items are removed
3. **EventBridge Scheduler** - Executes schedules at specified times
4. **Target Lambda** - The function invoked by EventBridge Scheduler when schedules fire
5. **Auto-Test Schedule** - Automatically creates a test schedule 2 minutes after deployment

### Architecture Flow

```
User inserts item into DynamoDB
    ↓
DynamoDB Stream captures change
    ↓
StreamProcessorFunction triggered
    ↓
Creates/Updates/Deletes EventBridge Schedule
    ↓
EventBridge Scheduler invokes TargetLambdaFunction at scheduled time
```

### DynamoDB Item Structure

```json
{
  "scheduleId": "unique-schedule-id",
  "scheduleExpression": "at(2026-02-15T10:00:00)",
  "payload": "{\"key\": \"value\"}",
  "enabled": true
}
```

**Required Fields:**
- `scheduleId` (String) - Unique identifier for the schedule
- `scheduleExpression` (String) - EventBridge Scheduler expression (rate, cron, or at)

**Optional Fields:**
- `payload` (String) - JSON string passed to the target Lambda
- `enabled` (Boolean) - Whether the schedule is enabled (default: true)

## Testing

### Verify Auto-Created Test Schedule

After deployment, a test schedule is automatically created that fires 5 minutes later (UTC time):

1. Check if the schedule was created:
```bash
aws scheduler get-schedule --name auto-test-schedule
```

2. View the schedule in EventBridge Console:
   - Navigate to EventBridge → Scheduler → Schedules
   - Look for `auto-test-schedule`
   - Note the "Next invocation" time (displayed in your local timezone)

3. After 5 minutes, check the Target Lambda logs:
```bash
aws logs tail /aws/lambda/ScheduledTaskExecutor --follow
```

**Note:** All schedule times use UTC timezone. EventBridge Scheduler expressions use the format `at(YYYY-MM-DDTHH:MM:SS)` in UTC.

### Create Your Own Schedule

1. Get the DynamoDB table name from the stack outputs:
```bash
aws cloudformation describe-stacks --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' \
  --output text
```

2. Insert a new schedule (set time to a few minutes in the future in UTC):
```bash
aws dynamodb put-item \
  --table-name ScheduleConfigs \
  --item '{
    "scheduleId": {"S": "my-test-schedule"},
    "scheduleExpression": {"S": "at(2026-02-12T20:00:00)"},
    "payload": {"S": "{\"message\": \"Hello from my schedule\"}"},
    "enabled": {"BOOL": true}
  }'
```

**Important:** The time must be in UTC and in the future. To get current UTC time:
```bash
date -u +"%Y-%m-%dT%H:%M:%S"
```

3. Verify the schedule was created:
```bash
aws scheduler get-schedule --name my-test-schedule
```

4. Check StreamProcessor logs to see the creation:
```bash
aws logs tail /aws/lambda/ScheduleStreamProcessor --follow
```

### Update a Schedule

```bash
aws dynamodb update-item \
  --table-name ScheduleConfigs \
  --key '{"scheduleId": {"S": "my-test-schedule"}}' \
  --update-expression "SET scheduleExpression = :expr" \
  --expression-attribute-values '{":expr": {"S": "at(2026-02-12T21:00:00)"}}'
```

**Note:** Time must be in UTC and in the future.

### Delete a Schedule

```bash
aws dynamodb delete-item \
  --table-name ScheduleConfigs \
  --key '{"scheduleId": {"S": "my-test-schedule"}}'
```

Verify deletion:
```bash
aws scheduler get-schedule --name my-test-schedule
# Should return ResourceNotFoundException
```

## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```

2. Confirm the stack has been deleted
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
    ```

## Resources

- [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)
- [DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html)
- [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)

This pattern was contributed by Luigi Napoleone Capasso

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
