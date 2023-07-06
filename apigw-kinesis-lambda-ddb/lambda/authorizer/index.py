from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
import boto3
import json
import base64

logger = Logger()
tracer = Tracer()
client = boto3.client("secretsmanager")


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    username = get_secret("gateway/username", "UserName")
    password = get_secret("gateway/password", "Password")
    expected_auth_header = "Basic " + base64_encode(f"{username}:{password}")
    method_arn = event["methodArn"]

    effect = "Deny"
    if (
        "Authorization" in event["headers"]
        and event["headers"]["Authorization"] == expected_auth_header
    ):
        effect = "Allow"

    statement = {
        "principalId": "user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Resource": [method_arn],
                    "Effect": effect,
                }
            ],
        },
    }

    logger.info(f"Response: {statement}")
    return statement


# Method to read secret from secrets manager
def get_secret(secret_name: str, secret_key: str) -> str:
    response = client.get_secret_value(SecretId=secret_name)
    value = json.loads(response["SecretString"])
    return value[secret_key]


# Method to base64 encode string
def base64_encode(string: str) -> str:
    return base64.b64encode(string.encode("utf-8")).decode("utf-8")
