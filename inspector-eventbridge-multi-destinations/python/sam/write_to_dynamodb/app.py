import json
import boto3
from decimal import Decimal

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = 'MyDynamoDBTable'

# entry point to the function
def lambda_handler(event, context):
    try:
        print("Received EventBridge event:", json.dumps(event))
        
        # Extract necessary fields
        payload = json.dumps(event)
        detail = event.get('detail', {})
        eventid = event.get('id', {})
        severity = detail.get('severity')
        status = detail.get('status')
        inspectorScore_float = detail.get('inspectorScore')
        inspectorScore = Decimal(str(inspectorScore_float))
        
        # Write data to DynamoDB
        table = dynamodb.Table(table_name)
        response = table.put_item(
            Item={
                'UUID': eventid,
                'Severity': severity,
                'Score': inspectorScore,
                'Status': status,
                'Payload': payload
            }
        )
        
        print("DynamoDB Response:", response)
        
        return {
            'statusCode': 200,
            'body': json.dumps('Data successfully written to DynamoDB')
        }
    except Exception as e:
        error_message = str(e)
        print("Error:", error_message)
        return {
            'statusCode': 500,
            'body': json.dumps('Error occurred while processing the event: ' + error_message)
        }