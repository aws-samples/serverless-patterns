import boto3
import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the Cognito client
cognito = boto3.client('cognito-idp')

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")

    # Extract relevant information from the event
    user_pool_id = event['userPoolId']
    username = event['userName']
    
    try:
        # Retrieve the user's attributes from Cognito
        user_response = cognito.admin_get_user(
            UserPoolId=user_pool_id,
            Username=username
        )
        
        # Find the certificate fingerprint in the user's attributes
        cert_fingerprint = next(
            (attr['Value'] for attr in user_response['UserAttributes'] 
             if attr['Name'] == 'custom:cert_fingerprint'),
            None
        )
        
        if not cert_fingerprint:
            logger.warning(f"No certificate fingerprint found for user {username}")
            return event
        
        logger.info(f"Found certificate fingerprint for user {username}: {cert_fingerprint}")
        
        # Prepare the response structure
        response = {
            'claimsAndScopeOverrideDetails': {
                'accessTokenGeneration': {
                    'claimsToAddOrOverride': {
                        'cnf': {
                            'x5t#S256': cert_fingerprint
                        }
                    }
                }
            }
        }
        
        # Add the response to the event
        event['response'] = response
        
        logger.info(f"Added certificate fingerprint and version to access token claims for user {username}")
        
    except Exception as e:
        logger.error(f"Error processing pre-token generation for user {username}: {str(e)}")
        # In case of an error, we don't modify the event
        # This allows the token generation to proceed without the certificate binding
    
    logger.info(f"Returning event: {json.dumps(event)}")
    return event