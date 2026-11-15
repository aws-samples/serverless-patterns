import os
import boto3
import json
import logging


# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
cognito_client = boto3.client("cognito-idp")
apigateway_client = boto3.client("apigateway")
ssm = boto3.client("ssm")


# Method to get a parameter from AWS Systems Manager Parameter Store
def get_from_parameter_store(key):
    parameter = ssm.get_parameter(Name=key)
    return parameter["Parameter"]["Value"]


# Method to validate the presence of required parameters in a request body
def validate_parameters(body, required_params):
    return all(param in body and len(body[param]) > 1 for param in required_params)


# Method to generate a standardised API response
def generate_response(status_code, success, message, data=None):
    response_data = {"success": success, "message": message}
    if data is not None:
        response_data["data"] = data
    return {"statusCode": status_code, "body": json.dumps(response_data)}


# Method to redact sensitive information in the request body
def redact_password(body):
    redacted_body = body.copy()
    redacted_body["password"] = "REDACTED"
    return redacted_body


# Method to log a redacted version of the event
def log_redacted_event(event):
    redacted_body = redact_password(json.loads(event["body"]))
    redacted_event = event.copy()
    redacted_event["body"] = json.dumps(redacted_body)
    logger.info("Event: %s", redacted_event)


# Method to create an API key and associate it with a usage plan
def create_api_key(user_id):
    response = apigateway_client.create_api_key(
        name=user_id,
        enabled=True,
    )
    api_key_id = response["id"]
    apigateway_client.create_usage_plan_key(
        usagePlanId=USAGE_PLAN_ID,
        keyId=api_key_id,
        keyType="API_KEY",
    )
    logger.info(f"API Key created for user_id: {user_id}.")
    return response["value"]


# Method to update the custom:api_key field in Cognito user attributes
def update_cognito_user_api_key(email, api_key):
    cognito_client.admin_update_user_attributes(
        UserPoolId=USER_POOL_ID,
        Username=email,
        UserAttributes=[
            {
                "Name": "custom:api_key",
                "Value": api_key,
            }
        ],
    )
    logger.info(f"Updated custom:api_key field for email: {email}.")


# Method to create a new Cognito user
def create_cognito_user(email, password, fullname):
    response = cognito_client.sign_up(
        ClientId=USER_POOL_CLIENT_ID,
        Username=email,
        Password=password,
        UserAttributes=[
            {"Name": "name", "Value": fullname},
            {"Name": "email", "Value": email},
        ],
    )
    logger.info(f"Created user: {email}.")
    return response


# Method to authenticate a Cognito user
def login_cognito_user(email, password):
    response = cognito_client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={
            "USERNAME": email,
            "PASSWORD": password,
        },
        ClientId=USER_POOL_CLIENT_ID,
    )
    logger.info(f"Authenticated: {email}")
    return response


CONSTRUCT_ID = os.environ["CONSTRUCT_ID"]
# Load parameters from AWS Systems Manager Parameter Store
USER_POOL_CLIENT_ID = get_from_parameter_store(f"/{CONSTRUCT_ID}/user_pool/client_id")
USER_POOL_ID = get_from_parameter_store(f"/{CONSTRUCT_ID}/user_pool/id")
USAGE_PLAN_ID = get_from_parameter_store(f"/{CONSTRUCT_ID}/api/usage_plan/id")


def handler(event, context):
    try:
        # Log a redacted version of the incoming event
        log_redacted_event(event)

        # Parse the request body and path from the event
        body = json.loads(event["body"])
        path = event["path"]

        # Validate required parameters in the request body
        if not validate_parameters(body, ["email", "password"]) or (
            path == "/register" and not validate_parameters(body, ["fullname"])
        ):
            logger.error("Missing required parameters: email or password.")
            return generate_response(422, False, "Missing required parameters.")

        else:
            email = body["email"]
            password = body["password"]
            fullname = body.get("fullname", "")

        # Handle different paths from the API Gateway
        if path == "/login":
            # Login path, authenticate the user
            response = login_cognito_user(email, password)
            return generate_response(200, True, response["AuthenticationResult"])

        elif path == "/register":
            # Registration path, create a new Cognito user and associated API key
            response = create_cognito_user(email, password, fullname)
            api_key = create_api_key(response["UserSub"])
            update_cognito_user_api_key(email, api_key)
            return generate_response(
                200, True, f"User {email} created successfully.", {"API Key": api_key}
            )

        else:
            # Handle any other request method
            logger.error("Invalid method: %s.", event["httpMethod"])
            return generate_response(400, False, "Invalid method")

    except Exception as err:
        logger.exception(f"Failed to {path[1:]}.")
        return generate_response(
            err.response["ResponseMetadata"]["HTTPStatusCode"],
            False,
            err.response["Error"]["Message"],
        )
