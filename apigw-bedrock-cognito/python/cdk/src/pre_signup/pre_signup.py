import os
import logging


# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Get organization domain from environment variable
ORGANIZATION_DOMAIN = os.environ.get("ORGANIZATION_DOMAIN")


def handler(event, context):
    # Log the incoming event
    logger.info(event)

    # Extract email domain
    email_domain = event["request"]["userAttributes"]["email"].split("@")[1]

    # Check if email domain matches organization
    if email_domain == ORGANIZATION_DOMAIN:
        # Automatically confirm user registration and verify email
        event["response"]["autoConfirmUser"] = True
        event["response"]["autoVerifyEmail"] = True

    else:
        # Raise an exception if email is not part of the organization domain
        raise Exception(
            f"Cannot register user as email is not part of domain: {ORGANIZATION_DOMAIN}"
        )

    return event
