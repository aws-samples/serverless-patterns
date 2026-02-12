# Saga Pattern with Lambda Durable Functions

This CDK project implements the saga pattern for distributed transactions using AWS Lambda Durable Functions. It demonstrates how to coordinate multiple microservices (flight, hotel, and car rental) with automatic rollback capabilities when any step fails.

## Architecture Overview

The saga orchestrator coordinates a travel booking workflow that:
1. Reserves a flight
2. Reserves a hotel room
3. Reserves a car rental

If any step fails, the orchestrator automatically executes compensating transactions to rollback previously completed reservations, ensuring data consistency across all services.

## Components

### Lambda Functions

**Saga Orchestrator (Durable Function)**
- Coordinates the entire workflow across all three services
- Manages state and execution history
- Automatically triggers rollback on failure
- Execution timeout: 1 hour
- Retention period: 30 days

**Flight Service**
- `saga-reserve-flight`: Creates flight booking reservations
- `saga-cancel-flight`: Compensating transaction to cancel flight bookings

**Hotel Service**
- `saga-reserve-hotel`: Creates hotel room reservations
- `saga-cancel-hotel`: Compensating transaction to cancel hotel reservations

**Car Service**
- `saga-reserve-car`: Creates car rental reservations
- `saga-cancel-car`: Compensating transaction to cancel car rentals

### DynamoDB Tables

- `saga-flight-bookings`: Stores flight booking records
- `saga-hotel-reservations`: Stores hotel reservation records
- `saga-car-rentals`: Stores car rental records

All tables use:
- Pay-per-request billing mode
- Point-in-time recovery enabled
- Partition key based on reservation/booking/rental ID

## Prerequisites

- Node.js and npm installed
- AWS CDK CLI installed (`npm install -g aws-cdk`)
- AWS credentials configured
- Python 3.14 runtime available in your AWS region

## Deployment

### Install dependencies
```bash
npm install
```

### Build the project
```bash
npm run build
```

### Deploy to AWS
```bash
npx cdk deploy
```

The deployment will output the ARNs of all Lambda functions and DynamoDB table names.

## Useful Commands

* `npm run build`   - Compile TypeScript to JavaScript
* `npm run watch`   - Watch for changes and compile automatically
* `npm run test`    - Run Jest unit tests
* `npx cdk deploy`  - Deploy this stack to your AWS account/region
* `npx cdk diff`    - Compare deployed stack with current state
* `npx cdk synth`   - Generate CloudFormation template
* `npx cdk destroy` - Remove all resources from AWS

## Testing the Saga Pattern

After deployment, invoke the saga orchestrator function with a test payload to see the distributed transaction in action. If any service fails, watch the automatic rollback compensate for completed steps.

## Configuration

The `cdk.json` file tells the CDK Toolkit how to execute your app and includes context values for feature flags and environment settings.
