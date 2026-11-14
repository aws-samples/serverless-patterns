import json
import base64

def handler(event, context):
    
    #print the event object received by Lambda
    print(json.dumps(event))
 
    #extract the name of the object added to the bucket
    object_key = event["Records"][0]["s3"]["object"]["key"]
    print(object_key)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
