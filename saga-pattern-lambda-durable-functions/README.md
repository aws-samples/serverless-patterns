# Saga Pattern with AWS Lambda durable functions

This pattern demonstrates how to implement the Saga pattern for distributed transactions using AWS Lambda durable functions. The example implements a travel booking system that coordinates flight, hotel, and car reservations with automatic compensating transactions (rollbacks) on failure.

Durable functions are regular Lambda functions that allow you to write sequential code in your preferred programming language. They track progress, automatically retry on failures, and suspend execution for up to one year at defined points, without paying for idle compute during waits.

This saga is built using the `aws-durable-execution-sdk` with Python 3.14 runtime and deployed using AWS CDK (TypeScript).

**Important:** This application uses various AWS services and there are costs associated with these services after the Free Tier usage. Please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

![Saga Architecture](./images/saga-architecture.png)

### Components

- **Saga Orchestrator**: AWS Lambda durable function that coordinates the distributed transaction
- **Service Functions**: Individual Lambda functions for each service (flight, hotel, car)
  - Reserve functions: Create reservations in Amazon DynamoDB
  - Cancel functions: Rollback reservations (compensating transactions)
- **Amazon DynamoDB Tables**: Store reservation state for each service

### Saga Flow

**Success Path:**
```
Reserve Flight → Reserve Hotel → Reserve Car → Complete
```

**Failure Path (with Compensation):**
```
Reserve Flight → Reserve Hotel → Reserve Car (FAILS)
                                           ↓
                    Compensation (Reverse Order):
                           ↓
                    Cancel Hotel
                           ↓
                    Cancel Flight
```

## Requirements

- [AWS Account](https://aws.amazon.com/free/)
- [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- [Python 3.11+](https://www.python.org/downloads/) installed (required for building the Lambda layer)
- [Node.js 22+](https://nodejs.org/) installed
- [AWS CDK](https://aws.amazon.com/cdk/) installed (`npm install -g aws-cdk`)
- [Git](https://git-scm.com/) installed

## Deployment Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aws-samples/serverless-patterns
cd serverless-patterns/saga-pattern-lambda-durable-functions/saga-pattern-cdk
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Build the Lambda Layer

The saga orchestrator requires a Lambda layer with the durable execution SDK. Build it using:

```bash
./build-layer.sh
```

This creates `saga-layer.zip` in the current directory containing the required Python dependencies.

> **Note:** The build script requires Python 3.11+ and uses a temporary virtual environment for clean, isolated builds.

### 4. Bootstrap AWS CDK (First Time Only)

```bash
cdk bootstrap
```

Or with a specific profile:

```bash
cdk bootstrap --profile your-profile-name
```

### 5. Deploy the Stack

```bash
npm run build
cdk deploy
```

The deployment creates:
- 3 Amazon DynamoDB tables (flight-bookings, hotel-reservations, car-rentals)
- 7 Lambda functions (1 orchestrator + 6 service functions)
- 1 Amazon SQS dead letter queue for failed saga executions
- IAM roles and permissions

### 6. Note the Outputs

After deployment, CDK outputs the ARNs for all Lambda functions and DynamoDB table names.

## How It Works

The Saga pattern maintains data consistency across microservices without using distributed transactions. Instead, it uses:

1. **Sequential Execution**: Services are invoked one after another
2. **State Tracking**: Each successful operation is tracked
3. **Compensating Transactions**: On failure, successful operations are undone in reverse order
4. **Idempotency**: Operations can be safely retried

### Key Features

- **No Distributed Locks**: Each service manages its own data independently
- **Eventual Consistency**: System reaches consistent state through compensations
- **Fault Tolerance**: Handles partial failures gracefully
- **Auditability**: Complete log trail of all operations
- **Automatic Retry**: Durable functions handle retries automatically

## Testing

The saga pattern implementation includes built-in failure flags for easy testing of compensating transactions.

### Failure Flags

Each reserve function supports a failure flag that simulates service failures:
- `failBookFlight` - Causes flight reservation to fail
- `failBookHotel` - Causes hotel reservation to fail  
- `failBookCar` - Causes car reservation to fail

When set to `true`, the service throws an exception before creating any records, triggering the saga compensation logic.

### Test Scenario 1: Success Path (All Services Work)

**Using AWS CLI (Async Invocation):**

```bash
aws lambda invoke \
  --function-name saga-durable-function \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload file://test-success.json \
  response.json
```

**test-success.json:**
```json
{
  "passengerName": "Michael Johnson",
  "flightNumber": "AA456",
  "departure": "LAX",
  "destination": "MIA",
  "flightPrice": 380.00,
  "guestName": "Michael Johnson",
  "hotelName": "Hilton Downtown Miami",
  "roomType": "Ocean View Suite",
  "checkIn": "2026-04-10",
  "checkOut": "2026-04-15",
  "hotelPrice": 320.00,
  "driverName": "Michael Johnson",
  "carType": "Convertible",
  "pickupLocation": "Miami Airport",
  "dropoffLocation": "Miami Airport",
  "pickupDate": "2026-04-10",
  "dropoffDate": "2026-04-15",
  "carPrice": 150.00
}
```

**Expected Response:**
```json
{
  "success": true,
  "transactionId": "uuid-here",
  "message": "All travel arrangements completed successfully",
  "bookings": {
    "flight": "booking-id",
    "hotel": "reservation-id",
    "car": "rental-id"
  }
}
```

**Validation:**
- All three services succeed
- Amazon DynamoDB records show `status: "RESERVED"`
- No compensations triggered

### Test Scenario 2: Flight Fails Immediately

**Using AWS CLI:**

```bash
aws lambda invoke \
  --function-name saga-durable-function \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload file://test-fail-flight-booking.json \
  response.json
```

**test-fail-flight-booking.json:**
```json
{
  "passengerName": "Sarah Williams",
  "departure": "ORD",
  "destination": "SEA",
  "failBookFlight": true
}
```

**Expected Behavior:**
- Flight fails immediately
- Hotel and car never attempted
- No compensations needed (nothing to rollback)
- Amazon DynamoDB: No records created

### Test Scenario 3: Hotel Fails After Flight Succeeds

**Using AWS CLI:**

```bash
aws lambda invoke \
  --function-name saga-durable-function \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload file://test-fail-hotel-booking.json \
  response.json
```

**test-fail-hotel-booking.json:**
```json
{
  "passengerName": "David Martinez",
  "departure": "DFW",
  "destination": "BOS",
  "flightPrice": 420.00,
  "guestName": "David Martinez",
  "hotelName": "Boston Harbor Hotel",
  "failBookHotel": true
}
```

**Expected Behavior:**
- Flight reserved
- Hotel fails
- Compensation: Flight cancelled (reverse order)
- Amazon DynamoDB: Flight record updated to `status: "CANCELLED"`

### Test Scenario 4: Car Fails After Flight and Hotel Succeed

**Using AWS CLI:**

```bash
aws lambda invoke \
  --function-name saga-durable-function \
  --invocation-type Event \
  --cli-binary-format raw-in-base64-out \
  --payload file://test-fail-car-booking.json \
  response.json
```

**test-fail-car-booking.json:**
```json
{
  "passengerName": "Jane Smith",
  "departure": "SFO",
  "destination": "NYC",
  "guestName": "Jane Smith",
  "hotelName": "Marriott Times Square",
  "driverName": "Jane Smith",
  "failBookCar": true
}
```

**Expected Behavior:**
- Flight reserved
- Hotel reserved
- Car fails
- Compensation: Hotel cancelled, then flight cancelled (reverse order)
- Amazon DynamoDB: Flight and hotel records with `status: "CANCELLED"`

![Saga Failure Console](./images/saga-failure-with-car.png)

### Verify Compensation in DynamoDB

After triggering a failure, verify the compensation worked:

```bash
# Check flight bookings
aws dynamodb scan --table-name saga-flight-bookings \
  --projection-expression "bookingId, #s, updatedAt" \
  --expression-attribute-names '{"#s":"status"}'

# Check hotel reservations
aws dynamodb scan --table-name saga-hotel-reservations \
  --projection-expression "reservationId, #s, updatedAt" \
  --expression-attribute-names '{"#s":"status"}'

# Check car rentals
aws dynamodb scan --table-name saga-car-rentals \
  --projection-expression "rentalId, #s, updatedAt" \
  --expression-attribute-names '{"#s":"status"}'
```

Look for:
- `status` field: `"RESERVED"` or `"CANCELLED"`
- `updatedAt` timestamp changes after cancellation
- No orphaned records

### Async vs Sync Invocation

Use `--invocation-type Event` (async) for durable functions — Lambda returns 202 immediately and the function runs in the background. Use `--invocation-type RequestResponse` (default) for synchronous execution.

## Monitoring

### Amazon CloudWatch Logs

Each Lambda function logs to CloudWatch:
- `/aws/lambda/saga-durable-function` - Orchestrator logs
- `/aws/lambda/saga-reserve-flight` - Flight service logs
- `/aws/lambda/saga-reserve-hotel` - Hotel service logs
- `/aws/lambda/saga-reserve-car` - Car service logs

### Amazon CloudWatch Insights Query

Find all compensation events:

```
fields @timestamp, @message
| filter @message like /compensation/
| sort @timestamp desc
| limit 100
```

## Cleanup

To avoid incurring charges, delete all resources:

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
