import json
import os
import uuid
import time
from aws_durable_execution_sdk_python import DurableContext, durable_execution
from aws_durable_execution_sdk_python.config import CallbackConfig, Duration
import boto3

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['CALLBACK_TABLE_NAME'])

@durable_execution
def lambda_handler(event, context: DurableContext):
    """Human-in-the-Loop Approval Pattern using Durable Functions"""
    
    # Parse input
    body = event.get('body')
    if body:
        import json as json_module
        body = json_module.loads(body)
    else:
        body = event
    
    print(f"Received event keys: {list(event.keys())}")
    print(f"Body: {body}")
    request_id = body.get('requestId', 'REQ-UNKNOWN')
    amount = body.get('amount', 0)
    description = body.get('description', 'No description')
    
    # Get API Gateway URL from environment or construct it
    region = os.environ.get('AWS_REGION', 'us-east-2')
    api_base_url = f"https://w8a9tempjb.execute-api.{region}.amazonaws.com/prod"
    
    print(f"Starting approval workflow for request: {request_id}")
    print(f"API Base URL: {api_base_url}")
    
    # Step 1: Validate request
    context.step(
        lambda _: print(f"Request {request_id} validated: ${amount} - {description}"),
        name='validate-request'
    )
    
    # Step 2: Wait for human approval
    def send_approval_request(callback_id, ctx):
        # Generate a short UUID for the URL
        request_uuid = str(uuid.uuid4())
        
        # Store callback ID in DynamoDB with TTL (24 hours from now)
        ttl = int(time.time()) + 86400  # 24 hours
        table.put_item(
            Item={
                'uuid': request_uuid,
                'callbackId': callback_id,
                'requestId': request_id,
                'ttl': ttl
            }
        )
        
        # Construct API Gateway URLs using the UUID
        approve_url = f"{api_base_url}/approve/{request_uuid}"
        reject_url = f"{api_base_url}/reject/{request_uuid}"
        
        sns.publish(
            TopicArn=os.environ['APPROVAL_TOPIC_ARN'],
            Subject=f'⚠️ Approval Required: {request_id}',
            Message=f"""
APPROVAL REQUEST

Request ID: {request_id}
Amount: ${amount}
Description: {description}

Click one of the links below to approve or reject:

✅ APPROVE: {approve_url}

❌ REJECT: {reject_url}

This request expires in 24 hours.
"""
        )
        print(f"Approval request sent. UUID: {request_uuid}, Callback ID: {callback_id}")
    
    # Create callback with 24-hour timeout
    callback = context.create_callback(
        name='wait-for-approval',
        config=CallbackConfig(timeout=Duration.from_hours(24))
    )
    
    # Send approval request with callback ID
    send_approval_request(callback.callback_id, context)
    
    # Wait for callback result
    approval = callback.result()
    
    # Step 3: Process decision
    def process_decision(_):
        if not approval:
            return 'timeout'
        # Parse if string (base64 decoded JSON)
        if isinstance(approval, str):
            import json
            approval_data = json.loads(approval)
            return approval_data.get('decision', 'unknown')
        return approval.get('decision', 'unknown')
    
    decision = context.step(process_decision, name='process-decision')
    
    print(f"Approval workflow completed: {decision}")
    
    # Parse comments
    comments = 'Timed out'
    if approval:
        if isinstance(approval, str):
            import json
            approval_data = json.loads(approval)
            comments = approval_data.get('comments', '')
        else:
            comments = approval.get('comments', '')
    
    return {
        'requestId': request_id,
        'amount': amount,
        'description': description,
        'decision': decision,
        'comments': comments
    }
