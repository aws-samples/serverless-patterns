import json 
import boto3 

lambdaClient = boto3.client('lambda')
def lambda_handler(event, context):
    print("Got an event from some route ", event)     
    if event['requestContext']['routeKey'] == "$connect":  
         url = "https://" + event["requestContext"]["domainName"] + "/" + event["requestContext"]["stage"] 

    response = lambdaClient.invoke(FunctionName="WebsocketPostToConnectionId",InvocationType="Event",Payload=json.dumps({"url": url, "connectionId":event['requestContext']['connectionId']}))    
    payload = "This won't be received by the client"    
    return {'statusCode': 200,'body': payload}