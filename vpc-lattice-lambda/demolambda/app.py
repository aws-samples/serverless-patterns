import json
import os
import requests

def lambda_handler(event, context):
    url = 'https://' + os.environ['URL']
    response = requests.get(url)
    return {
        'statusCode': 200,
        'body': json.dumps('recieved response from Lambda'+ response.text)
    }
