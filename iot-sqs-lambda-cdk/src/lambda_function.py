# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 
# SPDX-License-Identifier: MIT-0

import json

def handler(event, context):
    
    #print the event object received by Lambda
    print(json.dumps(event))
    
    # extract and log the body of the message received 
    message_body = event["Records"][0]["body"]
    print(message_body)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
