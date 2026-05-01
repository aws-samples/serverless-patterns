# Investigation Failure Escalation Workflow with AWS Lambda durable functions

This pattern demonstrates an investigation failure escalation workflow using AWS Lambda durable functions. When a DevOps Agent's investigation fails or times out, the durable function gathers failure context, creates an incident ticket in DynamoDB, pages on-call personnel via SNS, and uses durable function callbacks to wait for human acknowledgment. The function incurs no compute charges while waiting for a response.

**Important:** Please check the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) for regions currently supported by AWS Lambda durable functions.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-durable-investigation-escalation

## Architecture

The pattern uses two Lambda functions, two DynamoDB tables, an SNS topic, and an API Gateway endpoint:

- **Escalation_Function** (Durable Lambda) — Orchestrates the entire workflow: validates the event, gathers context, creates an incident, pages on-call personnel, and tracks resolution. Pauses execution (no compute charges) while waiting for acknowledgment.
- **Callback_Handler** (Standard Lambda) — Receives acknowledgment clicks via API Gateway and sends durable execution callbacks to resume the paused Escalation_Function.
- **Incident_Table** (DynamoDB) — Stores incident records with failure context, escalation history, and resolution status.
- **Callback_Table** (DynamoDB) — Maps short UUIDs to durable function callback IDs for clean acknowledgment URLs.
- **Notification_Topic** (SNS) — Sends escalation email notifications to on-call personnel.
- **Escalation_API** (API Gateway) — Provides the `GET /{uuid}` acknowledgment endpoint.

### Workflow Steps

1. **gather-context** — The DevOps Agent invokes the Escalation_Function directly via `aws lambda invoke`. The function validates the incoming event and extracts failure context (investigation ID, failure type, service, region, error details, timestamp), generating a unique incident ID.
2. **create-incident** — Writes an incident record to the Incident_Table with status `open` and an empty escalation history. *(Integration Point)*
3. **notify-oncall** — Creates a durable callback with a configurable timeout, stores the UUID-to-callback mapping, and publishes a notification via SNS with an acknowledgment link. The function then pauses, incurring no compute charges while waiting. *(Integration Point)*
4. **resolve-incident** — When an on-call responder clicks the acknowledgment link, the Callback_Handler sends a durable callback, resuming the function. The incident is updated to `status: acknowledged`. *(Integration Point)*
5. **resolve-unacknowledged** — If the timeout expires without acknowledgment, the incident is updated to `status: unacknowledged` and the workflow completes. *(Integration Point)*

## Key Features

- ✅ **No Compute Charges During Wait** — Function is suspended while waiting for human response
- ✅ **Configurable Timeout** — Acknowledgment timeout duration configurable via SAM template parameter
- ✅ **Extensible Integration Points** — Incident ticket and notification operations are isolated as helper functions that can be replaced with calls to Jira, ServiceNow, PagerDuty, Opsgenie, or other ITSM tools

## Prerequisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) >= 1.150.0 (required for `DurableConfig` support)
* Python 3.14 runtime (automatically provided by Lambda)

## Deployment

1. Navigate to the pattern directory:
   ```bash
   cd lambda-durable-investigation-escalation
   ```

2. Build the SAM application:
   ```bash
   sam build
   ```

3. Deploy the application:
   ```bash
   sam deploy --guided --region us-east-2
   ```

   During the guided deployment, provide the required values:
   - **OncallEmail**: Email address to receive escalation notifications
   - **AckTimeout**: Timeout in seconds to wait for acknowledgment (default: 900)
   - Allow SAM CLI to create IAM roles when prompted

4. **Confirm SNS subscription**: Check your email and click the confirmation link from Amazon SNS

5. Note the `ApiEndpoint` and `EscalationFunctionArn` from the outputs

## Input Payload Format

The Escalation_Function expects the following JSON payload when invoked:

```json
{
  "investigationId": "INV-2025-001",
  "failureType": "investigation_failed",
  "service": "payment-service",
  "region": "us-east-1",
  "errorDetails": "Connection timeout after 3 retries to downstream API",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `investigationId` | string | Yes | Unique identifier for the failed investigation |
| `failureType` | string | Yes | One of `investigation_failed` or `investigation_timed_out` |
| `service` | string | Yes | The service that was being investigated |
| `region` | string | Yes | The AWS region where the failure occurred |
| `errorDetails` | string | Yes | Description of the error or failure |
| `timestamp` | string | Yes | ISO 8601 timestamp of the failure |

If any required field is missing or `failureType` is invalid, the function records a validation failure in the Incident_Table and terminates without sending notifications.

## Testing

### Trigger an Escalation

Invoke the Escalation_Function directly using the Lambda CLI:

```bash
aws lambda invoke \
  --function-name <EscalationFunctionArn> \
  --invocation-type Event \
  --region us-east-2 \
  --cli-binary-format raw-in-base64-out \
  --payload '{
    "investigationId": "INV-2025-001",
    "failureType": "investigation_failed",
    "service": "payment-service",
    "region": "us-east-1",
    "errorDetails": "Connection timeout after 3 retries to downstream API",
    "timestamp": "2025-01-15T10:30:00Z"
  }' \
  /dev/null
```

### Check Your Email

You will receive an escalation notification email containing:
- Incident ID and investigation details
- Failure type, service, region, and error details
- An **acknowledgment link**

### Acknowledge the Incident

Click the acknowledgment link in the email. You will see an HTML confirmation page indicating the incident has been acknowledged. The Escalation_Function resumes and updates the incident record to `acknowledged`.

If you do not click the link within the timeout (default 15 minutes), the incident is marked `unacknowledged`.

### Verify in DynamoDB

```bash
aws dynamodb scan --table-name <stack-name>-incidents --region us-east-2
```

## Integrating with a DevOps Agent

The Escalation_Function is designed to be invoked programmatically by a DevOps Agent when an investigation fails. The agent calls `lambda:Invoke` with `InvocationType: Event` (async, non-blocking) and passes the payload described above.

### Example: Python (boto3)

```python
import boto3
import json
from datetime import datetime, timezone

lambda_client = boto3.client('lambda', region_name='us-east-2')

def trigger_escalation(investigation_id, failure_type, service, region, error_details):
    lambda_client.invoke(
        FunctionName='<EscalationFunctionArn>',
        InvocationType='Event',
        Payload=json.dumps({
            'investigationId': investigation_id,
            'failureType': failure_type,
            'service': service,
            'region': region,
            'errorDetails': str(error_details),
            'timestamp': datetime.now(timezone.utc).isoformat()
        })
    )
```

Call this from your agent's error handler:

```python
try:
    result = run_investigation(issue)
except TimeoutError:
    trigger_escalation('INV-123', 'investigation_timed_out', 'my-service', 'us-east-1', 'Timed out')
except Exception as e:
    trigger_escalation('INV-123', 'investigation_failed', 'my-service', 'us-east-1', str(e))
```

### IAM Permission

The agent's execution role needs `lambda:InvokeFunction` on the Escalation Function:

```yaml
- Effect: Allow
  Action: lambda:InvokeFunction
  Resource: <EscalationFunctionArn>
```

## Configuration

| Parameter | Default | Description |
|---|---|---|
| `AckTimeout` | 900 (15 min) | Seconds to wait for on-call acknowledgment before marking unacknowledged |
| `OncallEmail` | — | Email address subscribed to the SNS notification topic |

To change values after deployment:

```bash
sam deploy --parameter-overrides AckTimeout=600 OncallEmail=oncall@example.com --region us-east-2
```

The timeout must be less than the overall `DurableConfig.ExecutionTimeout` of 3600 seconds (1 hour) defined in the SAM template.

## Extensibility and Integration Points

The incident ticket and notification operations are isolated into dedicated helper functions in `src/helpers.py`. You can replace any of these functions with calls to external ITSM and alerting services without modifying the core orchestration logic in `lambda_function.py`.

### Helper Functions

| Function | Default Behavior | Replacement Example |
|---|---|---|
| `create_incident_ticket(incident)` | DynamoDB `put_item` to Incident_Table | Jira, ServiceNow, Zendesk, or any ITSM platform with a REST API |
| `resolve_incident(incident_id, status, details)` | DynamoDB `update_item` on Incident_Table | Jira issue transition, ServiceNow resolve, or Zendesk ticket update |
| `send_escalation_notification(topic_arn, message)` | SNS `publish` to Notification_Topic | PagerDuty Events API v2, Opsgenie Alert API, Slack, or Microsoft Teams webhook |
| `store_callback_mapping(uuid, callback_id, incident_id, tier, ttl)` | DynamoDB `put_item` to Callback_Table | Typically not replaced |

### Swapping DynamoDB for an ITSM Tool

1. Replace `create_incident_ticket()` to call the external API and create a ticket.
2. Replace `resolve_incident()` to transition the external ticket to a resolved state.
3. Add API keys or credentials as environment variables or AWS Secrets Manager references.
4. Update the SAM template IAM policies to allow outbound HTTPS calls if running in a VPC.

### Swapping SNS for an Alerting Service

1. Replace `send_escalation_notification()` to call the external API (e.g., PagerDuty, Opsgenie, Slack).
2. Pass the acknowledgment URL in the notification payload so responders can still click to acknowledge.
3. Add the API integration key as an environment variable or Secrets Manager reference.

## Monitoring

### CloudWatch Logs

```bash
aws logs tail /aws/lambda/<stack-name>-EscalationFunction \
  --region us-east-2 --follow

aws logs tail /aws/lambda/<stack-name>-CallbackHandlerFunction \
  --region us-east-2 --follow
```

## Cleanup

```bash
sam delete --stack-name <your-stack-name> --region us-east-2
```

## Learn More

- [Lambda durable functions Documentation](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)
- [Durable Execution SDK (Python)](https://github.com/aws/aws-durable-execution-sdk-python)
- [Callback Operations](https://docs.aws.amazon.com/lambda/latest/dg/durable-callback.html)
- [SendDurableExecutionCallbackSuccess API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/client/send_durable_execution_callback_success.html)

---

Copyright 2025 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
