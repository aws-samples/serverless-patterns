import boto3
import os
import botocore.credentials
from botocore.awsrequest import AWSRequest
from botocore.httpsession import URLLib3Session
from botocore.auth import SigV4Auth

def lambda_handler(event, context):
    """
    Lambda function handler to make a GET request to a custom domain name with a specific path.

    Args:
        event (dict): The event payload from AWS Lambda.
        context (object): The context object from AWS Lambda.

    Returns:
        str: The response text from the GET request.
    """

    # Getting custom domain name from the environment variable
    custom_domain_name = os.environ['CUSTOM_DOMAIN_NAME']

    # Constructing the URL for the GET request
    request = AWSRequest(method="GET", url="https://" + custom_domain_name + "/prod/mypath")

    # Creating a URLLib3Session object with SSL/TLS verification using the provided root CA certificate
    session = URLLib3Session(
        verify='./rootCA.pem'
    )

    # Sending the GET request and getting the response
    r = session.send(request.prepare())

    # Printing the response text, headers, and status code for debugging purposes
    print(r.text)
    print(r.headers)
    print(r.status_code)

    # Returning the response text
    return r.text