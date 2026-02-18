# Saga Pattern with AWS Lambda Durable Functions (Node.js)

This pattern demonstrates the Saga pattern for distributed transactions using AWS Lambda durable functions in Node.js. It coordinates a multi-step travel booking process (flight, hotel, car) with automatic compensating transactions on failure.

## What is the Saga Pattern?

The Saga pattern manages distributed transactions by breaking them into a sequence of local transactions. Each step can succeed or fail independently, and if any step fails, compensating transactions automatically undo previously completed steps to maintain data consistency.

## Architecture

This implementation uses a single Lambda durable function that:
1. Executes reservation steps sequentially (flight → hotel → car)
2. Tracks completed steps automatically via `context.step()`
3. Implements compensating transactions in reverse order on failure
4. Maintains state across retries without external storage

## Key Features

- **Automatic Checkpointing**: Each `context.step()` creates a checkpoint
- **Fault Tolerance**: Execution resumes from last checkpoint on failure
- **Compensating Transactions**: Automatic rollback in reverse order
- **No External State Store**: Durable functions handle state management
- **Failure Simulation**: Test different failure scenarios

## How It Works

### Success Flow
```
Reserve Flight → Reserve Hotel → Reserve Car → SUCCESS
```

### Failure Flow (e.g., hotel fails)
```
Reserve Flight → Reserve Hotel (FAILS) → Cancel Flight → ROLLBACK COMPLETE
```

### Failure Flow (e.g., car fails)
```
Reserve Flight → Reserve Hotel → Reserve Car (FAILS) → Cancel Hotel → Cancel Flight → ROLLBACK COMPLETE
```

## Deployment

### Prerequisites
- AWS CLI configured
- SAM CLI installed
- Node.js 22.x

### Deploy
```bash
sam build
sam deploy --guided
```

Follow the prompts:
- Stack Name: `saga-pattern-demo`
- AWS Region: Your preferred region
- Confirm changes: Y
- Allow SAM CLI IAM role creation: Y
- Disable rollback: N
- Save arguments to configuration file: Y

## Testing

### Success Case
```bash
aws lambda invoke \
  --function-name <FunctionName>:prod \
  --invocation-type Event \
  --payload '{"tripId":"trip-001","userId":"user-123"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

### Simulate Flight Failure
```bash
aws lambda invoke \
  --function-name <FunctionName>:prod \
  --invocation-type Event \
  --payload '{"tripId":"trip-002","userId":"user-123","simulateFailure":"flight"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

### Simulate Hotel Failure (triggers flight cancellation)
```bash
aws lambda invoke \
  --function-name <FunctionName>:prod \
  --invocation-type Event \
  --payload '{"tripId":"trip-003","userId":"user-123","simulateFailure":"hotel"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

### Simulate Car Failure (triggers hotel and flight cancellation)
```bash
aws lambda invoke \
  --function-name <FunctionName>:prod \
  --invocation-type Event \
  --payload '{"tripId":"trip-004","userId":"user-123","simulateFailure":"car"}' \
  --cli-binary-format raw-in-base64-out \
  response.json
```

## Viewing Logs

```bash
sam logs --stack-name saga-pattern-demo --tail
```

Or view in CloudWatch Logs console.

## Expected Output

### Success Case
```json
{
  "status": "SUCCESS",
  "message": "Trip booked successfully",
  "tripId": "trip-001",
  "userId": "user-123",
  "reservations": {
    "flight": {
      "reservationId": "FL-1234567890",
      "from": "SFO",
      "to": "NYC",
      "date": "2026-03-15",
      "status": "CONFIRMED"
    },
    "hotel": {
      "reservationId": "HT-1234567891",
      "name": "Grand Hotel NYC",
      "checkIn": "2026-03-15",
      "checkOut": "2026-03-18",
      "status": "CONFIRMED"
    },
    "car": {
      "reservationId": "CR-1234567892",
      "type": "SUV",
      "pickupDate": "2026-03-15",
      "returnDate": "2026-03-18",
      "status": "CONFIRMED"
    }
  }
}
```

### Failure Case (hotel fails)
```json
{
  "status": "FAILED",
  "message": "Trip booking failed, all reservations rolled back",
  "tripId": "trip-003",
  "userId": "user-123",
  "error": "Hotel reservation failed - no rooms available",
  "compensatedServices": ["flight"]
}
```

## How Durable Functions Enable Saga Pattern

1. **State Management**: `context.step()` automatically checkpoints each operation
2. **Idempotency**: Steps are executed exactly once, even on retries
3. **Compensation Tracking**: `completedSteps` array tracks what needs rollback
4. **Automatic Recovery**: Failed executions resume from last checkpoint
5. **No External Dependencies**: No DynamoDB or Step Functions needed

## Cleanup

```bash
sam delete --stack-name saga-pattern-demo
```

## Learn More

- [AWS Lambda Durable Functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Saga Pattern](https://microservices.io/patterns/data/saga.html)
- [Distributed Transactions](https://aws.amazon.com/blogs/compute/building-a-serverless-distributed-application-using-a-saga-orchestration-pattern/)
