# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

import base64
import json

# Handler method - ESM Lambda with filter criteria
def esm_lambda_with_filter_handler(event, context):
    # Iterate over the stream data
    for record in event['Records']:
        decoded_data = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        print(decoded_data)
