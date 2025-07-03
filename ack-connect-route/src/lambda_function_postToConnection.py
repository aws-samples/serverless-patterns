import json
import boto3 

def lambda_handler(event, context):
    
    print("Got an event from parent lambda ", event)
    gatewayapi = boto3.client("apigatewaymanagementapi",endpoint_url = event["url"])
    response = gatewayapi.get_connection(ConnectionId=event['connectionId'])
    print("Response is ", response)
    
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        gatewayapi.post_to_connection(ConnectionId=event['connectionId'], Data="Hello XXX, we are now connected!! ")
    return {}

