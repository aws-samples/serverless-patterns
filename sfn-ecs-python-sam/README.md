# AWS Step Functions to Amazon ECS with Python

This pattern demonstrates how to invoke an Amazon ECS task from AWS Step Functions using Python, showcasing both **synchronous (polling)** and **callback** integration patterns.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns

**Important:** This application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details.

## Security Note

This pattern is designed for learning and demonstration purposes. The IAM roles and security group use permissive configurations to simplify deployment and focus on the integration patterns:

- **Security Group**: Allows all outbound traffic (required for pulling Docker images and calling AWS APIs)
- **IAM Roles**: Use wildcard (`*`) resources for ECS task management and Step Functions callbacks

**For production use**, you should:
- Restrict security group egress to specific AWS service endpoints using VPC endpoints
- Scope IAM policies to specific resources (task definitions, state machines)
- Implement least privilege access based on your security requirements
- Consider using AWS PrivateLink for service-to-service communication
- Enable VPC Flow Logs for network traffic monitoring

Deploy this pattern in a non-production AWS account or isolated environment for testing.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Architecture

### Pattern 1: Synchronous (Polling) Integration

```
┌─────────────┐      ┌──────────────────┐      ┌─────────────┐
│   Step      │      │   ECS Task       │      │  CloudWatch │
│  Functions  │─────▶│   (Python)       │─────▶│    Logs     │
│   (Sync)    │      │                  │      │             │
└─────────────┘      └──────────────────┘      └─────────────┘
      │                       │
      │                       │
      └───────────────────────┘
         Waits for completion
```

**How it works:**
1. Step Functions invokes the ECS task using `arn:aws:states:::ecs:runTask.sync`
2. Step Functions **polls** the task status automatically
3. The workflow **waits** until the ECS task completes
4. Once complete, Step Functions continues to the next state
5. If the task fails, Step Functions can catch the error and retry

**Use cases:**
- Short to medium-duration tasks (< 1 year)
- When you need the task result before proceeding
- Simple workflows where waiting is acceptable

### Pattern 2: Callback Integration

```
┌─────────────┐      ┌──────────────────┐      ┌─────────────┐
│   Step      │      │   ECS Task       │      │  CloudWatch │
│  Functions  │─────▶│   (Python)       │─────▶│    Logs     │
│  (Callback) │      │                  │      │             │
└─────────────┘      └──────────────────┘      └─────────────┘
      ▲                       │
      │                       │
      └───────────────────────┘
         Task sends callback
```

**How it works:**
1. Step Functions invokes the ECS task using `arn:aws:states:::ecs:runTask.waitForTaskToken`
2. Step Functions passes a **task token** to the ECS container via environment variable
3. Step Functions **pauses** and waits for a callback
4. The Python application in ECS processes the work
5. When done, the Python app calls `send_task_success()` or `send_task_failure()` with the task token
6. Step Functions receives the callback and continues

**Use cases:**
- Long-running tasks
- Human approval workflows
- External system integrations
- When you need to decouple task execution from workflow progression

## Deployment Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/sfn-ecs-python-sam
```

### Step 2: Build and Deploy

```bash
sam build
sam deploy --guided
```

During the prompts:
- **Stack Name**: `sfn-ecs-python-stack`
- **AWS Region**: Your preferred region (e.g., `us-east-1`)
- **Confirm changes before deploy**: Y
- **Allow SAM CLI IAM role creation**: Y
- **Save arguments to samconfig.toml**: Y

### Step 3: Note the Outputs

After deployment, note the following outputs:
- `SyncStateMachineArn` - ARN for the synchronous pattern
- `CallbackStateMachineArn` - ARN for the callback pattern
- `ECSClusterName` - Name of the ECS cluster
- `TaskDefinitionArn` - ARN of the task definition

## How to Test

### Testing the Synchronous Pattern

1. **Start the execution:**

```bash
aws stepfunctions start-execution \
    --state-machine-arn <SyncStateMachineArn> \
    --input '{"message": "Hello from sync pattern", "processingTime": 10}'
```

2. **Monitor the execution:**

```bash
aws stepfunctions describe-execution \
    --execution-arn <execution-arn-from-previous-command>
```

3. **View the output:**

The execution will wait for the ECS task to complete and return the result:

```json
{
  "status": "success",
  "message": "Processed: Hello from sync pattern",
  "processingTime": 10,
  "timestamp": "2024-02-05T10:30:00Z"
}
```

### Testing the Callback Pattern

1. **Start the execution:**

```bash
aws stepfunctions start-execution \
    --state-machine-arn <CallbackStateMachineArn> \
    --input '{"message": "Hello from callback pattern", "processingTime": 30}'
```

2. **Monitor the execution:**

```bash
aws stepfunctions describe-execution \
    --execution-arn <execution-arn-from-previous-command>
```

The execution will show status as `RUNNING` while waiting for the callback.

3. **View ECS task logs:**

```bash
aws logs tail /ecs/sfn-ecs-python-callback --follow
```

4. **The task will automatically send the callback** when processing completes.

## Step-by-Step Explanation

### Understanding the Synchronous Pattern

**Step 1: State Machine Definition**

The state machine uses the `.sync` integration pattern:

```json
{
  "Type": "Task",
  "Resource": "arn:aws:states:::ecs:runTask.sync",
  "Parameters": {
    "Cluster": "my-cluster",
    "TaskDefinition": "my-task",
    "LaunchType": "FARGATE",
    "NetworkConfiguration": {
      "AwsvpcConfiguration": {
        "Subnets": ["subnet-xxx"],
        "SecurityGroups": ["sg-xxx"],
        "AssignPublicIp": "ENABLED"
      }
    },
    "Overrides": {
      "ContainerOverrides": [{
        "Name": "python-container",
        "Environment": [{
          "Name": "MESSAGE",
          "Value.$": "$.message"
        }]
      }]
    }
  }
}
```

**Step 2: ECS Task Execution**

The Python container starts and processes the input:

```python
import os
import time
import json

def main():
    message = os.environ.get('MESSAGE', 'No message')
    processing_time = int(os.environ.get('PROCESSING_TIME', '5'))
    
    print(f"Processing: {message}")
    time.sleep(processing_time)
    
    result = {
        "status": "success",
        "message": f"Processed: {message}",
        "processingTime": processing_time
    }
    
    print(json.dumps(result))

if __name__ == "__main__":
    main()
```

**Step 3: Step Functions Polling**

- Step Functions automatically polls ECS every few seconds
- Checks if the task is still running
- When the task completes (or fails), Step Functions captures the result
- The workflow continues to the next state

### Understanding the Callback Pattern

**Step 1: State Machine Definition**

The state machine uses the `.waitForTaskToken` integration pattern:

```json
{
  "Type": "Task",
  "Resource": "arn:aws:states:::ecs:runTask.waitForTaskToken",
  "Parameters": {
    "Cluster": "my-cluster",
    "TaskDefinition": "my-task",
    "LaunchType": "FARGATE",
    "Overrides": {
      "ContainerOverrides": [{
        "Name": "python-container",
        "Environment": [{
          "Name": "TASK_TOKEN",
          "Value.$": "$$.Task.Token"
        }, {
          "Name": "MESSAGE",
          "Value.$": "$.message"
        }]
      }]
    }
  }
}
```

**Key difference:** The `$$.Task.Token` is passed to the container.

**Step 2: ECS Task with Callback**

The Python container receives the task token and sends a callback:

```python
import os
import boto3
import json
import time

def main():
    task_token = os.environ.get('TASK_TOKEN')
    message = os.environ.get('MESSAGE', 'No message')
    processing_time = int(os.environ.get('PROCESSING_TIME', '5'))
    
    sfn_client = boto3.client('stepfunctions')
    
    try:
        print(f"Processing: {message}")
        time.sleep(processing_time)
        
        result = {
            "status": "success",
            "message": f"Processed: {message}",
            "processingTime": processing_time
        }
        
        # Send success callback
        sfn_client.send_task_success(
            taskToken=task_token,
            output=json.dumps(result)
        )
        
    except Exception as e:
        # Send failure callback
        sfn_client.send_task_failure(
            taskToken=task_token,
            error='ProcessingError',
            cause=str(e)
        )

if __name__ == "__main__":
    main()
```

**Step 3: Callback Mechanism**

- Step Functions pauses execution after starting the ECS task
- The task token acts as a unique identifier for this specific execution
- The Python app calls `send_task_success()` or `send_task_failure()`
- Step Functions receives the callback and resumes execution
- The output from the callback becomes the state output

## Key Differences Between Patterns

| Feature | Synchronous (.sync) | Callback (.waitForTaskToken) |
|---------|-------------------|------------------------------|
| **Max Duration** | 1 year | 1 year |
| **Polling** | Automatic by Step Functions | No polling needed |
| **Task Awareness** | Task doesn't know about Step Functions | Task must send callback |
| **Complexity** | Simple | Moderate (requires SDK calls) |
| **Use Case** | Standard batch jobs | Long-running, human approval, external systems |
| **Failure Handling** | Automatic | Manual (task must call send_task_failure) |
| **Cost** | State transitions for polling | Fewer state transitions |

## Cleanup

To delete the resources:

```bash
sam delete
```

## Resources

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Step Functions ECS Integration](https://docs.aws.amazon.com/step-functions/latest/dg/connect-ecs.html)
- [Task Token Pattern](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token)

---

Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0