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
    username = get_secret("endpoint/username", "UserName")
    password = get_secret("endpoint/password", "Password")
    expected_auth_header = "Basic " + base64_encode(f"{username}:{password}")

    is_authorized = False
    if (
        "authorization" in event["headers"]
        and event["headers"]["authorization"] == expected_auth_header
    ):
        is_authorized = True

    return {"isAuthorized": is_authorized}


# Method to read secret from secrets manager
def get_secret(secret_name: str, secret_key: str) -> str:
    response = client.get_secret_value(SecretId=secret_name)
    value = json.loads(response["SecretString"])
    return value[secret_key]


# Method to base64 encode string
def base64_encode(string: str) -> str:
    return base64.b64encode(string.encode("utf-8")).decode("utf-8")
