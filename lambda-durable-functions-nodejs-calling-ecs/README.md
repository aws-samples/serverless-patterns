# AWS Lambda durable functions with Amazon ECS Integration

This pattern demonstrates how to use AWS Lambda durable functions to orchestrate long-running Amazon ECS Fargate tasks. The Lambda function can wait up to 24 hours for ECS task completion without incurring compute charges during the wait period.

**Important:** Please check the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) for regions currently supported by AWS Lambda durable functions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-functions-nodejs-calling-ecs

## Architecture

![Architecture Diagram](architecture.png)

The pattern uses Lambda durable functions with the callback pattern to orchestrate ECS Fargate tasks cost-effectively.

### Workflow Steps

1. **Lambda function invoked** with task parameters (message, processing time)
2. **Durable function creates callback ID** using `context.waitForCallback()`
3. **ECS Fargate task started** with callback ID passed as environment variable
4. **Lambda function pauses** (no compute charges during wait)
5. **ECS task processes workload** and logs progress to CloudWatch
6. **ECS task completes** (in production, would call `SendDurableExecutionCallbackSuccess`)
7. **Lambda function resumes** and returns result

## Key Features

- ✅ **24-Hour Wait Time** - Can wait up to 24 hours for ECS task completion
- ✅ **No Compute Charges During Wait** - Function suspended during wait period
- ✅ **Callback Pattern** - ECS tasks call Lambda APIs directly to resume execution
- ✅ **CloudWatch Logs** - Full visibility into both Lambda and ECS execution
- ✅ **Generic Container** - Uses public Python image, easily replaceable
- ✅ **Fargate Serverless** - No EC2 instances to manage

## Prerequisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed
* Node.js runtime (see [supported runtimes for durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-supported-runtimes.html))

## Deployment

1. Navigate to the pattern directory:
   ```bash
   cd lambda-durable-functions-nodejs-calling-ecs
   ```

2. Build the SAM application:
   ```bash
   sam build
   ```

3. Deploy the application:
   ```bash
   sam deploy --guided
   ```
   
   During the guided deployment:
   - Accept default values or customize as needed
   - Allow SAM CLI to create IAM roles when prompted
   - Note the function name from the outputs

4. Note the `CallbackFunctionName` from the CloudFormation outputs

## Testing

### Test the Callback Pattern

Invoke the Lambda function with a test payload:

```bash
aws lambda invoke \
  --function-name <CallbackFunctionName>:prod \
  --invocation-type Event \
  --payload '{"message":"Test ECS task","processingTime":8}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

**Note:** A qualified ARN (version or alias) is required for durable functions. See [invoking durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-invoking.html#durable-invoking-qualified-arns).

### Monitor Execution

Check Lambda logs:
```bash
aws logs tail /aws/lambda/<CallbackFunctionName> --since 2m --follow
```

Check ECS task logs:
```bash
aws logs tail /ecs/lambda-ecs-durable-demo --since 2m --follow
```

### Expected Output

**Lambda Logs:**
```
Starting Lambda durable function - Callback Pattern
Callback ID created: <callback-id>
Starting ECS task with callback ID...
ECS task started: arn:aws:ecs:...
```

**ECS Logs:**
```
=== ECS Task Started ===
Callback ID: <callback-id>
Message: Test ECS task
Processing Time: 8 seconds
Simulating work...
=== Task Completed Successfully ===
Result: {"status":"completed","message":"Processed: Test ECS task"}
Note: In production, call Lambda SendDurableExecutionCallbackSuccess API here
```

## How It Works

### Lambda durable function (Node.js)

The Lambda function uses the `@aws/durable-execution-sdk-js` package:

```javascript
const { withDurableExecution } = require('@aws/durable-execution-sdk-js');

exports.handler = withDurableExecution(async (event, context) => {
  // Create callback and start ECS task
  const result = await context.waitForCallback(
    'ecs-task-callback',
    async (callbackId) => {
      // Start ECS task with callback ID
      const response = await ecs.send(new RunTaskCommand({
        // ... pass callbackId as environment variable
      }));
    },
    { timeout: { hours: 1 } }
  );
  
  return result;
});
```

### ECS Task (Python)

The ECS container receives the callback ID and processes the workload. In production, it would call the Lambda API:

```bash
aws lambda send-durable-execution-callback-success \
  --callback-id $CALLBACK_ID \
  --result '{"status":"completed","data":"..."}'
```

### Key Configuration

**Lambda Function:**
- Runtime: `nodejs22.x` (see [supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/durable-supported-runtimes.html))
- `AutoPublishAlias: prod`
- `DurableConfig` with execution timeout and retention period

**ECS Task:**
- Launch type: `FARGATE`
- Public subnet with `assignPublicIp: ENABLED`
- Container image: `public.ecr.aws/docker/library/python:3.12-alpine`
- CloudWatch Logs enabled

## Customization

### Replace the ECS Container

The pattern uses a generic Python container for demonstration. To use your own container:

1. Update the `Image` in the `ECSTaskDefinition` resource
2. Ensure your container:
   - Reads the `CALLBACK_ID` environment variable
   - Calls `aws lambda send-durable-execution-callback-success` on completion
   - Calls `aws lambda send-durable-execution-callback-failure` on error

### Adjust Timeouts

Modify the durable function timeout in `template.yaml`:

```yaml
DurableConfig:
  ExecutionTimeout: 86400  # 24 hours in seconds
  RetentionPeriodInDays: 7
```

And the callback timeout in the handler:

```javascript
context.waitForCallback('ecs-task-callback', async (callbackId) => {
  // ...
}, {
  timeout: { hours: 24 },  // Maximum wait time
  heartbeatTimeout: { minutes: 5 }  // Optional heartbeat
})
```

## Cleanup

Delete the stack:

```bash
sam delete
```

## Additional Resources

- [AWS Lambda durable functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Amazon ECS on AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)

---

© 2026 Amazon Web Services, Inc. or its affiliates. All Rights Reserved.
