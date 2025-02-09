import boto3
import json
import random
import string
import os
from datetime import datetime

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
sns_client = boto3.client('sns')

# Retrieve DynamoDB table name and SNS topic ARN from environment variables
TABLE_NAME = os.environ['TABLE_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

def generate_random_string(length=8):
    """Generate a random string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def insert_into_dynamodb(random_value, message):
    """Insert data into DynamoDB"""
    table = dynamodb.Table(TABLE_NAME)
    item = {
        'id': generate_random_string(),  # Unique ID
        'random_value': random_value,
        'message': message,
        'timestamp': datetime.now().isoformat()  # Record the current time
    }
    table.put_item(Item=item)
    print(f"Inserted into DynamoDB: {item}")

def send_to_sns(message):
    """Send a message to SNS"""
    response = sns_client.publish(
        TopicArn=TOPIC_ARN,
        Message=message
    )
    print(f"Sent to SNS: {message}, MessageId: {response['MessageId']}")

def lambda_handler(event, context):
    print(event)
    """AWS Lambda handler function"""
    try:
        # Extract the list of records from the SQS event
        records = event.get('Records', [])
        
        for record in records:
            # Parse the body of each record
            body_str = record.get('body', '{}')  # Get the body as a string
            body = json.loads(body_str)  # Parse the body as JSON
            
            # Check if the message is for DynamoDB insertion
            if body.get("Insert") == "DynamoDB":
                # Generate a random value and construct a message
                random_value = random.randint(1, 100)  # Random number between 1 and 100
                message = f"Random value is {random_value}"
                insert_into_dynamodb(random_value, message)
            else:
                # Send a message to SNS
                send_to_sns("No DynamoDB insertion requested.")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Processing completed'})
        }
    
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
