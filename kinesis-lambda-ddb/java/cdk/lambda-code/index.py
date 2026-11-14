import json
import boto3
import base64

dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the Kinesis record's data from base64
        kinesis_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        payload = json.loads(kinesis_data)  # Deserialize the JSON string
        # Define your DynamoDB table name
        dynamodb_table_name = 'table-name'

        # Create an item to put into DynamoDB
    
        item = {
            'id': {
                'S': payload['id']
            },
            'price': {
                'N': str(payload['price'])
            },
            'name': {
                'S': payload['name']
            }
        }

        # Put the item into DynamoDB
        response = dynamodb.put_item(
            TableName=dynamodb_table_name,
            Item=item
        )

        print(f"PutItem response: {response}")

    return {
        'statusCode': 200,
        'body': 'Data pushed to DynamoDB successfully!'
    }
