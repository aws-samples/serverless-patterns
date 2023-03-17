import json, base64
import logging as log

def lambda_handler(event, context):
    
    print("Target Lambda function invoked")
    print(event)
    if 'rmqMessagesByQueue' not in event:
        print("Invalid event data")
        return {
            'statusCode': 404
        }
    print(f'Div Data received from event source: ')
    for queue in event["rmqMessagesByQueue"]:
        messageCnt = len(event['rmqMessagesByQueue'][queue])
        print(f'Total messages received from event source: {messageCnt}' )
        for message in event['rmqMessagesByQueue'][queue]:
            data = base64.b64decode(message['data'])
            print(data)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
