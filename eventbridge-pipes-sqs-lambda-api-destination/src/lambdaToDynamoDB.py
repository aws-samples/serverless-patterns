import json
import boto3

# import requests

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    print(event)
  
    order = json.loads(event['body'])
    
    # Example of 'order':
    # {
	#   "order_id":"103",
	#   "address": "Singapore",
	#   "amount": "50"
	#   "type": "Food"
    # }
    
    order = json.loads(event['body'])
    order_id = order['order_id']
    address = order['address']
    amount = order['amount']
    type = order['type']
    
    insert_order = client.put_item(
        TableName='OrderTable',
        Item={
            'id': { 'S': order_id},
            'Address': { 'S': address },
            'Amount': { 'S': amount },
            'Type': { 'S': type }
        }
    )
    response = "Order Id " + order_id + " received successfully"
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": json.dumps(response)
        }),
    }
