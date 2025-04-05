import boto3
import cfnresponse
import logging

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create an AWS ACM client
acm = boto3.client('acm')

def lambda_handler(event, context):
    """
    Lambda function handler to create or delete an AWS Certificate Manager (ACM) certificate.

    Args:
        event (dict): The event payload from AWS Lambda.
        context (object): The context object from AWS Lambda.

    Returns:
        None
    """
    logger.info('Received event: {}'.format(event))

    # Retrieve physical ID for the resource
    physical_id = event.get('PhysicalResourceId', 'CustomResourcePhysicalID')

    if event['RequestType'] == 'Create':
        logger.info('Create event')

        # Read the certificate body, private key, and certificate chain from files
        with open('server.crt', 'rb') as f:
            certificate_body = f.read()

        with open('server.key', 'rb') as f:
            private_key = f.read()

        with open('rootCA.pem', 'rb') as f:
            certificate_chain = f.read()

        # Import the certificate into AWS ACM
        response = acm.import_certificate(
            Certificate=certificate_body,
            PrivateKey=private_key,
            CertificateChain=certificate_chain
        )

        print(response)

        # Update the physical ID with the ARN of the imported certificate
        physical_id = response["CertificateArn"]

        # Send a SUCCESS response to CloudFormation
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, physical_id)

    elif event['RequestType'] == 'Delete':
        logger.info('Delete event')
        try:
            # Delete the certificate from AWS ACM
            response = acm.delete_certificate(
                CertificateArn=physical_id
            )

            print(response)
            
            logger.info(f'Successfully deleted certificate: {physical_id}')

            # Send a SUCCESS response to CloudFormation
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {}, physical_id)

        except Exception as e:
            # Log the error and send a FAILED response to CloudFormation
            logger.error(f'Error deleting certificate: {str(e)}')

            # Send a ERROR response to CloudFormation
            cfnresponse.send(event, context, cfnresponse.FAILED, {"Error": str(e)}, physical_id)