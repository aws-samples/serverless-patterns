# Webhook SNS Pattern - CDK Version

This is a simplified AWS CDK implementation of a webhook integration pattern that receives webhook events via API Gateway, queues them in SQS, and processes them with Lambda to send SMS notifications via SNS.

## Architecture

```
API Gateway (POST) → SQS Queue → Lambda Function → SNS (SMS)
```

## Components

- **API Gateway**: REST API endpoint to receive webhook events
- **SQS Queue**: Decouples the API from processing and provides reliability
- **Lambda Function**: Processes messages and sends SMS via SNS
- **SNS**: Sends SMS messages to phone numbers

## Prerequisites

- AWS CLI configured with appropriate permissions
- Python 3.9+
- AWS CDK v2 installed (`npm install -g aws-cdk`)

## Deployment

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Bootstrap CDK (if not done before):
```bash
cdk bootstrap
```

3. Deploy the stack:
```bash
cdk deploy
```

4. Note the API Gateway endpoint URL from the output.

## Testing

### SMS Sandbox Verification (Required for New AWS Accounts)

If your AWS account is in SMS sandbox mode (default for new accounts), you'll need to verify your phone number before receiving SMS messages:

1. **Check if your account is in sandbox mode:**
```bash
aws sns get-sms-sandbox-account-status --region your-region
```

2. **If in sandbox mode, verify your phone number:**
```bash
# Add your phone number to sandbox
aws sns create-sms-sandbox-phone-number --phone-number "+your-phone-number" --region your-region

# Check your phone for verification code, then verify it
aws sns verify-sms-sandbox-phone-number --phone-number "+your-phone-number" --one-time-password "YOUR_CODE" --region your-region
```

3. **Alternative: Request production access** through the AWS Console (SNS → Text messaging → Sandbox) for unrestricted SMS sending.

### API Testing

The API is protected with an API key. After deployment, you'll need to retrieve the API key value before testing.

#### Get the API Key Value

1. **Note the API Key ID from the deployment output**, then get the actual key value:
```bash
aws apigateway get-api-key --api-key YOUR_API_KEY_ID --include-value
```

2. **Copy the `value` field from the response** - this is your actual API key.

#### Send Test Request

Send a POST request to the API Gateway endpoint with the API key header:

Example using curl (update URL with your own API domain, API key, and phoneNumber with your phone number including country code e.g. +1234567890):
```bash
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/prod/ \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_ACTUAL_API_KEY_VALUE" \
  -d '{"phoneNumber": "+your-phone-number", "message": "Hello from webhook!"}'
```

Expected response:
```json
{
  "SendMessageResponse": {
    "ResponseMetadata": {
      "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    "SendMessageResult": {
      "MD5OfMessageAttributes": null,
      "MD5OfMessageBody": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "MD5OfMessageSystemAttributes": null,
      "MessageId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "SequenceNumber": null
    }
  }
}
```

You should also receive an SMS on your mobile with the following message:
```
Hello from webhook!
```

## Important Notes

- **Phone Number Format**: Use E.164 format (e.g., +1234567890)
- **SMS Costs**: SNS SMS messages incur charges - be mindful of costs
- **Permissions**: Ensure your AWS account has SNS SMS permissions enabled
- **PoC Only**: This is a simplified pattern for proof of concept. For production usage, consider implementing authentication/authorization, Dead Letter Queues (DLQ) for failed message processing, proper error handling and retry logic, adding monitoring and alerting (CloudWatch alarms), rate limiting, and further input validation and sanitization.

## Use Cases

This pattern works well for various webhook integrations including:
- Marketing automation platforms
- CRM systems
- E-commerce platforms
- Monitoring and alerting systems
- Any system that needs to send SMS notifications based on webhook events

## Cleanup

To remove all resources:
```bash
cdk destroy
```

## Customization

- Modify `lambda/app.py` to change message processing logic
- Update the CDK stack to add additional features like DLQ, encryption, etc.
- Add API authentication/authorization as needed
- Integrate with different notification channels (email, Slack, etc.)
