import json
import os
import requests  # We use the requests module to make a HTTP GET request to the Secrets Manager Lambda extension: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html

secret_name = os.environ.get('SECRET_NAME')
secrets_extension_http_port = os.environ.get(
    'PARAMETERS_SECRETS_EXTENSION_HTTP_PORT')
aws_session_token = os.environ.get('AWS_SESSION_TOKEN')

secrets_extension_endpoint = "http://localhost:" + \
    secrets_extension_http_port + "/secretsmanager/get?secretId=" + secret_name
headers = {'X-Aws-Parameters-Secrets-Token': f'{aws_session_token}'}


def lambda_handler(event, context):

    r = requests.get(secrets_extension_endpoint, headers=headers)

    # We use json.loads to parse our secret and account for special characters that may be in our secret and decode them.
    secret = json.loads(r.text)["SecretString"]

    # We print our secret for demonstration purposes. Remove this line in your production systems!
    print(secret)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "secret": secret,
            }
        ),
    }
