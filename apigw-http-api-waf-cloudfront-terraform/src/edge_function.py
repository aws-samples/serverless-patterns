import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

region_name = "us-east-1"
session = boto3.session.Session()

verify_id_header_name = "x-origin-verify"
verify_id_region_header_name = "x-origin-verify-region"


def lambda_handler(event, context):
    logger.info(f"event: {event}")
    logger.info(f"context {context}")

    # Get headers
    request = event["Records"][0]["cf"]["request"]
    headers = request["origin"]["custom"]["customHeaders"]

    # Retrieve secret name from CloudFront custom header (x-origin-verify)
    secret_name = headers[verify_id_header_name][0]["value"]

    # Retrieve region from CloudFront custom header (x-origin-verify-region)
    region_name = headers[verify_id_region_header_name][0]["value"]

    # Get secret from Secrets Manager
    client = session.client(service_name="secretsmanager", region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    logger.info(f"get_secret_value_response {get_secret_value_response}")
    secret_string = get_secret_value_response["SecretString"]

    # If secret retrieved
    if secret_string:
        # Add custom header 'x-origin-verify-edge'
        headers[verify_id_header_name] = [
            {"key": verify_id_header_name, "value": secret_string}
        ]

    logger.info(f"output request {request}")
    return request
