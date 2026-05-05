import json
import os
from datetime import datetime, timezone

import boto3

lambda_client = boto3.client('lambda')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['CALLBACK_TABLE_NAME'])


def lambda_handler(event, context):
    """Handle human acknowledgment via API Gateway GET /{uuid}"""

    print(f"Received event: {json.dumps(event)}")

    # Extract UUID from path parameters
    request_uuid = event['pathParameters']['uuid']

    print(f"Processing acknowledgment for UUID: {request_uuid}")

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
    <p>This acknowledgment link is invalid or has expired.</p>
</body>
</html>
"""
            }

        callback_id = response['Item']['callbackId']
        incident_id = response['Item'].get('incidentId', 'Unknown')
        tier = response['Item'].get('tier', 'Unknown')
        print(f"Found callback ID: {callback_id} for incident: {incident_id}, tier: {tier}")

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

    # Prepare callback result with acknowledgment and timestamp
    result = {
        'acknowledged': True,
        'timestamp': datetime.now(timezone.utc).isoformat()
    }

    try:
        # Send callback using Lambda API
        result_json = json.dumps(result)

        response = lambda_client.send_durable_execution_callback_success(
            CallbackId=callback_id,
            Result=result_json
        )

        print(f"Callback sent successfully: {response}")

        # Return HTML confirmation page
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html; charset=utf-8'},
            'body': f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Incident Acknowledged</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            text-align: center;
        }}
        .success {{ color: #28a745; }}
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
        <div class="icon">&#10003;</div>
        <h1 class="success">Incident Acknowledged!</h1>
        <p style="font-size: 1.2em;">The escalation workflow has been notified and will update the incident record.</p>
    </div>
</body>
</html>
"""
        }

    except Exception as e:
        print(f"Error sending callback: {str(e)}")
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
    <h1 style="color: #dc3545;">Error Processing Acknowledgment</h1>
    <p>{str(e)}</p>
</body>
</html>
"""
        }
