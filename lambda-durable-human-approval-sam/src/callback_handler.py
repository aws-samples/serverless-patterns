import json
import os
import boto3

lambda_client = boto3.client('lambda', region_name='us-east-2')
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table(os.environ['CALLBACK_TABLE_NAME'])

def lambda_handler(event, context):
    """Handle approval/rejection via API Gateway"""
    
    print(f"Received event: {json.dumps(event)}")
    
    # Get UUID and decision from path parameters
    request_uuid = event['pathParameters']['uuid']
    decision = event['pathParameters']['decision']  # 'approve' or 'reject'
    
    print(f"Processing {decision} for UUID: {request_uuid}")
    
    # Fetch callback ID from DynamoDB
    try:
        response = table.get_item(Key={'uuid': request_uuid})
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'text/html; charset=utf-8'},
                'body': """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Not Found</title>
</head>
<body style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; text-align: center;">
    <h1 style="color: #dc3545;">Request Not Found</h1>
    <p>This approval link is invalid or has expired.</p>
</body>
</html>
"""
            }
        
        callback_id = response['Item']['callbackId']
        request_id = response['Item'].get('requestId', 'Unknown')
        print(f"Found callback ID: {callback_id} for request: {request_id}")
        
    except Exception as e:
        print(f"Error fetching from DynamoDB: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; text-align: center;">
    <h1 style="color: #dc3545;">Error</h1>
    <p>{str(e)}</p>
</body>
</html>
"""
        }
    
    # Prepare callback result
    result = {
        'decision': 'approved' if decision == 'approve' else 'rejected',
        'comments': f"{'Approved' if decision == 'approve' else 'Rejected'} via web link"
    }
    
    try:
        # Send callback using Lambda API
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/client/send_durable_execution_callback_success.html
        result_json = json.dumps(result)
        
        # Use the boto3 method (requires boto3 >= 1.35.9)
        response = lambda_client.send_durable_execution_callback_success(
            CallbackId=callback_id,
            Result=result_json
        )
        
        print(f"Callback sent successfully: {response}")
        
        # Return HTML response
        icon = '&#10003;' if decision == 'approve' else '&#10007;'  # HTML entities for checkmark and X
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Request {result['decision'].title()}</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            max-width: 600px; 
            margin: 50px auto; 
            padding: 20px;
            text-align: center;
        }}
        .success {{ color: #28a745; }}
        .rejected {{ color: #dc3545; }}
        .card {{ 
            border: 1px solid #ddd; 
            border-radius: 8px; 
            padding: 40px; 
            background: #f9f9f9;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{ margin-top: 0; font-size: 2em; }}
        .icon {{ font-size: 4em; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="card">
        <div class="icon">{icon}</div>
        <h1 class="{'success' if decision == 'approve' else 'rejected'}">
            Request {result['decision'].title()}!
        </h1>
        <p style="font-size: 1.2em;">The workflow has been notified and will continue processing.</p>
    </div>
</body>
</html>
"""
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; text-align: center;">
    <h1 style="color: #dc3545;">Error Processing Request</h1>
    <p>{str(e)}</p>
</body>
</html>
"""
        }
