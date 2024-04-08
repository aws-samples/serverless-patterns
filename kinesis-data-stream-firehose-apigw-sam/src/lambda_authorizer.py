import json
import boto3
import os

secretsmanager_client = boto3.client('secretsmanager')

def lambda_handler(event, context):

    # print(event)
    access_key = event['authorizationToken']
    methodArn = event['methodArn']
    secret_name = os.environ['SECRET_NAME']
    # print('Secret Name: ' + secret_name)
    # print('Access Key: ' + access_key)

    try:
        response = secretsmanager_client.get_secret_value(
            SecretId=secret_name
        )
        expected_key = response['SecretString']
        # print('Expected key: ' + expected_key)
    except Exception:
        return build_response(False, methodArn)

    if access_key != expected_key:
        return build_response(False, methodArn)

    return build_response(True, methodArn)

def build_response(allowRequest, methodArn):

    output = {
        "principalId": "yyyyyyyy", 
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "Deny",
                    "Resource": "arn:aws:execute-api:*"
                }
            ]
        }
    }

    if allowRequest is True:
        output["policyDocument"]["Statement"][0]["Effect"] = "Allow"

    output["policyDocument"]["Statement"][0]["Resource"] = methodArn

    return output