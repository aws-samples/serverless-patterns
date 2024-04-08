import json

# import requests


def lambda_handler(event, context):
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello from VPC Lattice Primmary Lambda !!"
        }),
    }
