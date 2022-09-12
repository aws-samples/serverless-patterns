#! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: MIT-0
import base64
import json

print('Loading function')

def handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        print("Decoded data: " + data)
    return 'Successfully processed {} records.'.format(len(event['Records']))