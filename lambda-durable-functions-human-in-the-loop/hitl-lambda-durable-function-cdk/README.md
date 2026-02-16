# Human in the Loop - CDK Implementation

This directory contains the AWS CDK implementation of the Human-in-the-Loop pattern using Lambda Durable Functions.

## What's Included

This CDK stack deploys:

- **Lambda Durable Function** - Orchestrates the HITL workflow with automatic checkpointing and retry logic
- **Callback Handler Lambda** - Processes approval/rejection callbacks from email links
- **DynamoDB Table** - Stores callback tokens securely with 1-hour TTL (matches callback timeout)
- **SNS Topic** - Sends email notifications with approval links
- **API Gateway** - Provides callback endpoint for email links
- **IAM Roles** - Properly scoped permissions for all resources
- **CloudWatch Logs** - Structured JSON logging for all functions

## Architecture

```
┌─────────────────┐
│  Durable        │
│  Function       │──────┐
│  (Orchestrator) │      │
└─────────────────┘      │
         │               │
         ▼               ▼
  ┌─────────────┐ ┌─────────────┐
  │  DynamoDB   │ │  SNS Topic  │
  │  (Tokens)   │ └─────────────┘
  └─────────────┘        │
         ▲               ▼
         │        ┌─────────────┐
         │        │    Email    │
         │        │ (short IDs) │
         │        └─────────────┘
         │               │
         │               ▼
         │        ┌─────────────┐
         │        │ API Gateway │
         │        │   /verify   │
         │        └─────────────┘
         │               │
         │               ▼
         │        ┌─────────────┐
         └────────│  Callback   │
                  │   Handler   │
                  └─────────────┘
```

## Prerequisites

- [Node.js 20+](https://nodejs.org/)
- [AWS CLI](https://aws.amazon.com/cli/) configured with credentials
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html) installed globally: `npm install -g aws-cdk`
- An AWS account with appropriate permissions

## Deployment

1. Install dependencies:
   ```bash
   npm install
   ```

2. Bootstrap CDK (first time only):
   ```bash
   cdk bootstrap
   ```

3. Deploy the stack with your email address:
   ```bash
   cdk deploy --context Email=your-email@example.com
   ```

4. **Confirm your SNS subscription**: Check your email inbox for a message with the subject **"AWS Notification - Subscription Confirmation"**. The email will contain:
   
   ```
   You have chosen to subscribe to the topic:
   arn:aws:sns:<REGION>:<ACCOUNT_NUMBER>:hitl-approval-notifications
   
   To confirm this subscription, click or visit the link below 
   (If this was in error no action is necessary):
   Confirm subscription
   ```
   
   **Click the "Confirm subscription" link.** Without this confirmation, you won't receive approval emails.
   
   > **Tip**: Check your spam/junk folder if you don't see the email.

5. Note the stack outputs:
   - `Hitl-ApiUrl` - API Gateway endpoint for callbacks
   - `Hitl-Sns-TopicArn` - SNS topic ARN
   - `Hitl-Durable-Function-Name` - Durable function name
   - `Hitl-Callback-Table-Name` - DynamoDB table for callback tokens

## Testing

1. **Confirm SNS subscription**: Check your email for "AWS Notification - Subscription Confirmation" and click the confirmation link.

2. **Invoke the durable function** in the Lambda console with this test event (expense report example):
   ```json
   {
     "submissionId": "DOC-2026-001234",
     "submissionType": "expense_report",
     "submitter": {
       "name": "Alice Johnson",
       "email": "alice.johnson@example.com",
       "department": "Engineering",
       "employeeId": "EMP-5678"
     },
     "document": {
       "title": "Q1 2026 Conference Travel Expenses",
       "amount": 2450.00,
       "currency": "USD",
       "category": "Travel & Entertainment",
       "description": "AWS re:Invent 2026 conference attendance",
       "items": [
         {
           "description": "Round-trip flight",
           "amount": 850.00,
           "date": "2026-11-28"
         }
       ],
       "attachments": ["s3://receipts/flight.pdf"]
     },
     "submittedAt": "2026-02-13T14:30:00Z"
   }
   ```
   
   See `events/` folder for more examples.

3. **Check your email** for the approval request with document details and APPROVE/REJECT links.

4. **Click a link** to complete the workflow, or use the console "Send success" feature to manually complete the callback.

## Project Structure

```
hitl-lambda-durable-function-cdk/
├── bin/
│   └── hitl-lambda-durable-function-cdk.ts    # CDK app entry point
├── lib/
│   └── hitl-lambda-durable-function-cdk-stack.ts  # Stack definition
├── lambdas/
│   ├── hitl-durable-functions/
│   │   ├── index.mjs                          # Durable function orchestrator
│   │   └── package.json                       # Dependencies
│   └── callback-handler/
│       ├── index.mjs                          # Callback handler
│       └── package.json                       # Dependencies
├── events/
│   ├── event.json                             # Test event
│   ├── callback-approve.json                  # Approval payload
│   └── callback-reject.json                   # Rejection payload
├── test/
│   └── hitl-lambda-durable-function-cdk.test.ts  # Unit tests
├── cdk.json                                   # CDK configuration
├── package.json                               # Project dependencies
└── tsconfig.json                              # TypeScript configuration
```

## Key CDK Constructs

### Durable Function Configuration

```typescript
const hitlDurableFunction = new NodejsFunction(this, 'HitlDurableFunction', {
  runtime: aws_lambda.Runtime.NODEJS_22_X,
  durableConfig: {
    executionTimeout: Duration.hours(1),
    retentionPeriod: Duration.days(30)
  },
  environment: {
    SNS_TOPIC_ARN: approvalTopic.topicArn,
    API_URL: api.url,
  },
});
```

### SNS Email Subscription

```typescript
const approvalTopic = new aws_sns.Topic(this, 'ApprovalTopic', {
  displayName: 'Human Approval Notifications',
});

approvalTopic.addSubscription(new EmailSubscription(email));
```

### API Gateway with Callback Handler

```typescript
const api = new aws_apigateway.RestApi(this, 'HitlCallbackApi', {
  restApiName: 'HITL-Callback-API',
});

const verifyResource = api.root.addResource('verify');
verifyResource.addMethod('GET', new aws_apigateway.LambdaIntegration(callbackHandler));
```

## Environment Variables

The durable function uses these environment variables:

- `SNS_TOPIC_ARN` - ARN of the SNS topic for sending emails
- `API_URL` - API Gateway URL for callback links
- `CALLBACK_TABLE_NAME` - DynamoDB table name for storing callback tokens

The callback handler uses:

- `CALLBACK_TABLE_NAME` - DynamoDB table name for looking up callback tokens

## IAM Permissions

The stack creates these IAM policies:

- **Durable Function**: SNS publish permissions, DynamoDB write permissions
- **Callback Handler**: Lambda durable execution callback permissions, DynamoDB read permissions

## Monitoring

View logs in CloudWatch:

```bash
# Durable function logs
aws logs tail /aws/lambda/hitl-durable-function --follow

# Callback handler logs
aws logs tail /aws/lambda/hitl-callback-handler --follow
```

Monitor durable executions in the Lambda console under the "Durable executions" tab.

## Cleanup

Remove all resources:

```bash
cdk destroy
```

This will delete:
- Lambda functions
- API Gateway
- SNS topic and subscriptions
- IAM roles
- CloudWatch log groups

## Useful CDK Commands

- `npm run build` - Compile TypeScript to JavaScript
- `npm run watch` - Watch for changes and compile
- `npm run test` - Run Jest unit tests
- `cdk diff` - Compare deployed stack with current state
- `cdk synth` - Emit synthesized CloudFormation template
- `cdk deploy` - Deploy stack to AWS
- `cdk destroy` - Remove all stack resources

## Troubleshooting

**Issue**: Email not received
- Check spam/junk folder
- Verify SNS subscription was confirmed
- Check SNS topic subscriptions in AWS Console

**Issue**: Callback link doesn't work
- Verify API Gateway URL in environment variables
- Check CloudWatch logs for errors
- Ensure callback handler has correct IAM permissions

**Issue**: Deployment fails
- Ensure CDK is bootstrapped: `cdk bootstrap`
- Check AWS credentials are configured
- Verify you have necessary IAM permissions

## Learn More

- [AWS Lambda Durable Functions](https://aws.amazon.com/lambda/lambda-durable-functions/)
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/)
- [Lambda Durable Functions SDK (JavaScript)](https://github.com/aws/durable-execution-sdk-js)

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
