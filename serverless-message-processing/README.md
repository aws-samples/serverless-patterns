# Serverless Message Processing Pattern

## Overview
An adaptable pattern for message processing using AWS serverless services, featuring error handling and automatic recovery mechanisms.

## Core Components
- API Gateway (message ingestion)
- SQS Queues (main + DLQs)
- Lambda Functions (processing + recovery)

## Basic Flow
1. Messages enter through API Gateway
2. Main queue receives messages
3. Processor Lambda handles messages
4. Failed messages route to DLQs
5. Decision maker attempts an automated recovery

## Deployment
# Build the SAM application
   ```
sam build
   ```
# Deploy the application
   ```
sam deploy --guided
   ```

## Key Features
- Automatic retry mechanism
- Segregation of recoverable/fatal errors
- Extensible processing logic

## API Reference
# Send Message
   ```

POST /message
Content-Type: application/json
   ```
   ```
{
    "messageType": "TYPE_A|TYPE_B|TYPE_C",
    "payload": {},
    "timestamp": "ISO8601_TIMESTAMP"
}
   ```


## Adaptation Points
- Message validation rules
- Processing logic
- Error handling strategies
- Recovery mechanisms
- Monitoring requirements
- API Design

## Note
This is a sample pattern. Adapt security, scaling, and processing logic according to your requirements.