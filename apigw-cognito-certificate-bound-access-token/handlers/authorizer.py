import json
import boto3
import logging
from jose import jwt
from jose.utils import base64url_decode
from botocore.exceptions import ClientError
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa

import requests
from datetime import datetime, timezone
import os
import traceback

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    bucket_name = os.environ['BUCKET_NAME']
    object_key = os.environ['CACERT_KEY']

    # Extract the Authorization header
    token = event['headers']['authorization']
    token = token.split(" ")[1] if token.startswith("Bearer ") else token
    
    try:
        # Verify the JWT token
        verified_claims = verify_jwt(token)
        
        # Extract the client certificate from the request
        client_cert_pem = event['requestContext']['identity']['clientCert']['clientCertPem']
        
        # Verify the certificate
        if not verify_certificate(client_cert_pem, bucket_name, object_key):
            logger.error('Invalid client certificate')
            return generate_policy('user', 'Deny', event['methodArn'])
        
        # Check if the certificate is bound to the token
        if not is_cert_bound_to_token(verified_claims, client_cert_pem):
            logger.error("Certificate is not bound to the token")
            return generate_policy('user', 'Deny', event['methodArn'])
        
        return generate_policy('user', 'Allow', event['methodArn'])
    
    except Exception as e:
        # Log the full stack trace
        logger.error("An error occurred:")
        logger.error(traceback.format_exc())
        
        # You can also log the specific error message
        logger.error(f"Error message: {str(e)}")
        
        # Return a Deny policy in case of any error
        return generate_policy('user', 'Deny', event['methodArn'])

def verify_jwt(token):
    # Get the kid (Key ID) from the token header
    headers = jwt.get_unverified_headers(token)
    kid = headers['kid']

    # Get the Cognito User Pool ID from the token
    payload = jwt.get_unverified_claims(token)
    user_pool_id = payload['iss'].split('/')[-1]

    # Get the public keys
    keys_url = f'https://cognito-idp.{boto3.Session().region_name}.amazonaws.com/{user_pool_id}/.well-known/jwks.json'
    response = requests.get(keys_url)
    keys = response.json()['keys']

    # Find the correct public key
    public_key = next((key for key in keys if key['kid'] == kid), None)
    if not public_key:
        raise Exception('Public key not found')

    # Verify the token
    verified_claims = jwt.decode(
        token,
        public_key,
        algorithms=['RS256'],
        audience=payload.get('aud') if payload.get('aud') else payload.get('client_id'),
        issuer=f'https://cognito-idp.{boto3.Session().region_name}.amazonaws.com/{user_pool_id}'
    )
    return verified_claims

from datetime import datetime, timezone
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend

def verify_certificate(cert_pem, bucket_name, object_key):
    try:
        # Load the client certificate
        cert = x509.load_pem_x509_certificate(cert_pem.encode(), default_backend())

        # Load the CA certificate
        ca_cert_pem = get_ca_cert(bucket_name, object_key)
        if not ca_cert_pem:
            return False
        ca_cert = x509.load_pem_x509_certificate(ca_cert_pem.encode(), default_backend())

        # Verify the certificate signature
        ca_public_key = ca_cert.public_key()
        if isinstance(ca_public_key, rsa.RSAPublicKey):
            try:
                ca_public_key.verify(
                    cert.signature,
                    cert.tbs_certificate_bytes,
                    padding.PKCS1v15(),
                    cert.signature_hash_algorithm
                )
            except InvalidSignature:
                logger.error("Invalid certificate signature")
                return False
        else:
            logger.error("Unsupported public key type")
            return False
        
        # Check if the certificate has expired
        now = datetime.now(timezone.utc)
        
        if now < cert.not_valid_before_utc or now > cert.not_valid_after_utc:
            logger.error("Certificate has expired or is not yet valid")
            return False
        
        # Check revocation status
        # implement this
        
        return True
    
    except Exception as e:
        logger.error(f"Certificate verification error: {str(e)}")
        return False
    
def get_ca_cert(bucket_name, object_key):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        return response['Body'].read().decode('utf-8')
    except ClientError as e:
        logger.error(f"Error retrieving CA cert: {str(e)}")
        return None

def check_revocation_status(cert):
    # implement this
    pass

def is_cert_bound_to_token(claims, cert_pem):
    try:
        cert = x509.load_pem_x509_certificate(cert_pem.encode(), default_backend())
        fingerprint = cert.fingerprint(hashes.SHA256()).hex()
        x5t_claim = claims.get('cnf', {}).get('x5t#S256')
        
        if not x5t_claim:
            logger.error("x5t#S256 claim not found in token")
            return False
        
        # Convert the x5t_claim to bytes before decoding
        x5t_hex = base64url_decode(x5t_claim.encode('ascii')).hex()
        
        return fingerprint == x5t_hex
    except Exception as e:
        logger.error(f"Error in is_cert_bound_to_token: {str(e)}")
        logger.error(traceback.format_exc())
        return False

def generate_policy(principal_id, effect, resource):
    return {
        'principalId': principal_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource
                }
            ]
        }
    }