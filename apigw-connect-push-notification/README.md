# Amazon API Gateway integration with Amazon Connect Customer for Push Notification 

This pattern creates an Amazon API Gateway REST API that directly integrates with the Amazon Connect to invoke [CreateNotification](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateNotification.html) API. It uses API Gateway's native AWS service integration with VTL mapping templates to transform requests and responses.

In-app notifications are on-screen alerts that appear in the Amazon Connect header. They provide a central way to communicate important information to users that are logged into Amazon Connect.

Supported Use Cases
-  System notifications such as availability impacts, failover events, policy changes, and critical feature updates.
- Custom organizational messages specified in API requests by your team for desired use cases, for example training reminders, schedule adherence alerts, and emergency notifications to your teams.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-connect-notification

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
- An [Amazon Connect instance](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html) already provisioned

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change directory to the pattern directory:
   ```
    cd apigw-connect-push-notification
    ```
3. From the command line, use AWS SAM to deploy the AWS resources for the pattern:
    ```
    sam build
    sam deploy --guided
    ```

4. During the prompts:
    - Enter a stack name
    - Enter your preferred AWS Region
    - Enter your Amazon Connect instance ID (found in the instance ARN: `arn:aws:connect:<region>:<account>:instance/<instance-id>`)
    - Allow SAM CLI to create IAM roles with the required permissions

5. Note the outputs from the SAM deployment process. These contain the API endpoint URL needed for testing.

## How it works

```
Client → API Gateway (REST) → Amazon Connect CreateNotification API → In-App Notification
```

1. A client sends a **POST** request to the API Gateway REST endpoint with a JSON body containing notification details.
2. API Gateway validates the request body against the OpenAPI schema.
3. A VTL **request mapping template** transforms the client payload into the format expected by the Connect `CreateNotification` API (which uses `PUT /notifications/{InstanceId}`).
4. API Gateway assumes an IAM role and directly calls the Connect API on the backend.
5. A VTL **response mapping template** transforms the Connect API response back to a clean client-facing JSON format.
6. Amazon Connect delivers the notification to the specified users' in-app notification panel.


## Testing

### Using curl

```bash
# Get the API endpoint from the stack outputs
API_ENDPOINT=$(aws cloudformation describe-stacks \
  --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`NotificationApiEndpoint`].OutputValue' \
  --output text)

# Send a HIGH priority notification to a specific agent
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "recipients": ["arn:aws:connect:<region>:<account>:instance/<instance-id>/agent/<agent-id>"],
    "content": {"en_US": "Hello! This is a test notification from the serverless pattern."},
    "priority": "HIGH"
  }' \
  "$API_ENDPOINT"
```

### Expected Response

```json
{
  "message": "Notification created successfully",
  "notificationId": "abc123-def456-...",
  "notificationArn": "arn:aws:connect:<region>:<account>:instance/<instance-id>/notification/<id>"
}
```

### Broadcast to All Users

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "recipients": ["arn:aws:connect:<region>:<account>:instance/<instance-id>"],
    "content": {
      "en_US": "System maintenance scheduled for tonight at 11 PM EST.",
      "es_ES": "Mantenimiento del sistema programado para esta noche a las 11 PM EST."
    },
    "priority": "LOW"
  }' \
  "$API_ENDPOINT"
```

### Full Payload Example (All Optional Fields)

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "recipients": ["arn:aws:connect:us-east-1:123456789012:instance/abcd-1234/agent/agent-001"],
    "content": {
      "en_US": "Training session tomorrow at 2 PM. [Join here](https://example.com/training)",
      "es_ES": "Sesión de capacitación mañana a las 2 PM. [Unirse aquí](https://example.com/training)"
    },
    "priority": "HIGH",
    "expiresAt": 1735689600,
    "clientToken": "unique-idempotency-token-abc123",
    "tags": {"team": "support", "category": "training"}
  }' \
  "$API_ENDPOINT"
```

## Request Body Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `recipients` | string[] | Yes | User ARNs or instance ARN (max 200) |
| `content` | object | Yes | Map of locale → text (max 500 chars/locale) |
| `priority` | string | No | `HIGH` or `LOW` (default: LOW) |
| `expiresAt` | number | No | Unix timestamp for expiry (default: 1 week) |
| `clientToken` | string | No | Idempotency token (max 500 chars) |
| `tags` | object | No | Key-value tags for TBAC |

## Cleanup

```bash
sam delete --stack-name <your-stack-name>
```


## Resources

- [Amazon Connect Notifications - Admin Guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-notifications.html)
- [CreateNotification API Reference](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateNotification.html)
- [API Gateway AWS Service Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-aws-proxy.html)
- [VTL Mapping Template Reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html)

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
