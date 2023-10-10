# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

import base64
import json

# Handler method transforming the incoming firehose data
def data_transformation_handler(event, context):
    output = []

    # Iterate over the stream data
    for record in event['records']:
        if record is not None:
            stream_data = base64.b64decode(record['data'])
            payload = json.loads(stream_data)

            # Sample Data Transformation
            if payload['SECTOR'].lower() in ['healthcare']:
                payload['SECTOR'] = 'MODERN_HEALTHCARE'

            # Generate Output Record
            output_record = {
                'recordId': record['recordId'],
                'result': 'Ok',
                'data': base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')
            }

            # Append Output
            output.append(output_record)

    return {'records': output}
