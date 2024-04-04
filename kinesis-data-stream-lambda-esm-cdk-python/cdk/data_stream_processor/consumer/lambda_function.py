import base64


def handler(event, context):
    print("Event Received: ")
    print(event)
    
    for record in event['Records']:
        #Kinesis data is base64 encoded so decode here
        payload=base64.b64decode(record["kinesis"]["data"])
        print("Decoded payload: " + str(payload))