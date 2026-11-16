
import json

def handler(event, context):
    print("Lambda function invoked")
    print(json.dumps(event))
    return


