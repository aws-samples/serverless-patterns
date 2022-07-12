import base64

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Decoded data: " + data)
    return 'Successfully processed {} records.'.format(len(event['Records']))