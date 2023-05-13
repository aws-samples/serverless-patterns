import json

# import requests


def lambda_handler(event, context):
    
    # Example body of msg received from SQS:
    # {
	#   "order_id":"103",
	#   "address": "Singapore",
	#   "amount": "50"
    # }
    
    print(event)
    
    # get order details
    requestToApi = json.loads(event[0]['body'])
    
    # enrich it 
    requestToApi['type'] = 'Food'


    return requestToApi

