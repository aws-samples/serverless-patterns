import json
import os
import boto3


def lambda_handler(event, context):

    # Extract the input data from the request body
    input_payload = json.loads(event['body'])['query']

    # Fetch the endpoint name from the environment variable
    endpoint_name = os.environ['SAGEMAKER_ENDPOINT_NAME']

    # Create a SageMaker runtime client
    runtime = boto3.client('sagemaker-runtime')

    try:
        """Query the SageMaker endpoint."""
        payload = json.dumps(input_payload)
        response = runtime.invoke_endpoint(EndpointName=endpoint_name,
                                           ContentType='application/json',
                                           Body=payload)
        query_response = response['Body'].read().decode('utf-8')

        # Return the result as the Lambda function response
        return {
            'statusCode': 200,
            'body': query_response
        }
    except Exception as e:
        # Handle any errors that occur during the invocation
        return {
            'statusCode': 500,
            'body': str(e)
        }
