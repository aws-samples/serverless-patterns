import json
import base64

def handler(event, context):
    
    #print the event object received by Lambda
    print(json.dumps(event))
    
    # decode the message received in base 64
    data_base64 = event["Records"][0]["kinesis"]["data"]
    decoded_data = base64.b64decode(data_base64)
    print(decoded_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
