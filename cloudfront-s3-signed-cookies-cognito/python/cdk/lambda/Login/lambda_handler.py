import json
import os
import base64
import time
from urllib.request import urlopen
from typing import Any, Dict, Tuple

import boto3
from botocore.exceptions import ClientError
from aws_lambda_powertools import Logger
import jwt
from jwt import InvalidTokenError
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

# Configure logging
logger = Logger()

# Initialize AWS clients
cognito_client = boto3.client('cognito-idp')
secrets_client = boto3.client('secretsmanager')

# Environment variables
USER_POOL_ID = os.environ['USER_POOL_ID']
USER_POOL_CLIENT_ID = os.environ['USER_POOL_CLIENT_ID']
ALLOWED_ORIGIN = os.environ.get('ALLOWED_ORIGIN', '*')
PRIVATE_KEY_SECRET_ARN = os.environ.get('PRIVATE_KEY_SECRET_ARN', '')
CLOUDFRONT_DOMAIN = os.environ.get('CLOUDFRONT_DOMAIN', '')
KEY_PAIR_ID = os.environ.get('KEY_PAIR_ID', '')
COOKIE_TTL_SECONDS = int(os.environ.get('COOKIE_TTL_SECONDS', '600'))
COOKIE_DOMAIN = os.environ.get('COOKIE_DOMAIN', '')
COOKIE_SAME_SITE = os.environ.get('COOKIE_SAME_SITE', 'None')
COGNITO_REGION = os.environ.get('COGNITO_REGION', os.environ.get('AWS_REGION', ''))

# Cache for the private key
_private_key_cache: Dict[str, Any] = {}
_jwks_cache: Dict[str, Any] = {}


def get_private_key():
    """Retrieve the private key from Secrets Manager with caching."""
    if "key" not in _private_key_cache:
        try:
            response = secrets_client.get_secret_value(SecretId=PRIVATE_KEY_SECRET_ARN)
            private_key_pem = response["SecretString"]
            
            private_key = serialization.load_pem_private_key(
                private_key_pem.encode("utf-8"),
                password=None,
                backend=default_backend(),
            )
            _private_key_cache["key"] = private_key
        except Exception as e:
            logger.error(f"Error retrieving private key: {e}")
            raise
    
    return _private_key_cache["key"]


def cloudfront_safe_base64(data: bytes) -> str:
    """Encode bytes to CloudFront-safe base64."""
    encoded = base64.b64encode(data).decode("utf-8")
    return encoded.replace("+", "-").replace("=", "_").replace("/", "~")


def create_custom_policy(resource: str, expires_epoch: int) -> str:
    """Create a CloudFront custom policy JSON."""
    policy = {
        "Statement": [
            {
                "Resource": resource,
                "Condition": {
                    "DateLessThan": {
                        "AWS:EpochTime": expires_epoch
                    }
                }
            }
        ]
    }
    return json.dumps(policy, separators=(",", ":"))


def sign_policy(policy_json: str, private_key) -> str:
    """Sign the policy using RSA PKCS1v15 with SHA1."""
    signature = private_key.sign(
        policy_json.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA1(),
    )
    return cloudfront_safe_base64(signature)


def create_signed_cookies(resource: str, expires_epoch: int) -> Tuple[str, str, str]:
    """Create the three CloudFront signed cookies."""
    private_key = get_private_key()
    
    policy_json = create_custom_policy(resource, expires_epoch)
    policy_b64 = cloudfront_safe_base64(policy_json.encode("utf-8"))
    signature = sign_policy(policy_json, private_key)
    
    return (
        f"CloudFront-Policy={policy_b64}",
        f"CloudFront-Signature={signature}",
        f"CloudFront-Key-Pair-Id={KEY_PAIR_ID}",
    )


def get_cors_headers() -> Dict[str, str]:
    """Return CORS headers based on configuration."""
    return {
        'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
        'Access-Control-Allow-Credentials': 'true',
        'Content-Type': 'application/json'
    }


def get_cookie_settings(is_cloudfront: bool = False) -> str:
    """Generate cookie settings based on environment."""
    is_https_origin = ALLOWED_ORIGIN.startswith('https://')
    attrs = ["HttpOnly", "Path=/"]

    if is_cloudfront or is_https_origin:
        attrs.append("Secure")

    if is_cloudfront and COOKIE_SAME_SITE:
        attrs.append(f"SameSite={COOKIE_SAME_SITE}")
    else:
        attrs.append("SameSite=None" if is_https_origin else "SameSite=Lax")

    if is_cloudfront and COOKIE_DOMAIN:
        attrs.append(f"Domain={COOKIE_DOMAIN}")

    return "; ".join(attrs)


@logger.inject_lambda_context(log_event=True)
def handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    request_id = context.aws_request_id
    logger.append_keys(request_id=request_id)

    # Handle preflight OPTIONS requests for CORS
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
                'Access-Control-Allow-Headers': 'Content-Type,Authorization',
                'Access-Control-Allow-Methods': 'OPTIONS,POST',
                'Access-Control-Allow-Credentials': 'true'
            },
            'body': ''
        }

    event_body = json.loads(event.get('body')) if 'body' in event else event
    email = event_body.get('email')
    password = event_body.get('password')
    
    # Validate input
    if not email or not password:
        logger.warning("Login validation failed", extra={
            "reason": "missing_credentials",
            "has_email": bool(email),
            "has_password": bool(event_body.get('password'))
        })
        return {
            'statusCode': 400,
            'headers': get_cors_headers(),
            'body': json.dumps({'message': 'Email and password are required'})
        }

    return log_in_user(email, password)
        

def log_in_user(email: str, password: str) -> Dict[str, Any]:
    """Authenticate user with Cognito and return tokens."""
    try:
        # Authenticate user using Cognito
        response = cognito_client.initiate_auth(
            ClientId=USER_POOL_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password
            }
        )
        
        # Extract tokens from the response
        id_token = response['AuthenticationResult']['IdToken']
        access_token = response['AuthenticationResult']['AccessToken']
        refresh_token = response['AuthenticationResult']['RefreshToken']
        expires_in = response['AuthenticationResult']['ExpiresIn']
        
        # Decode ID token to get user information
        user_info = decode_id_token(id_token)
        user_email = user_info.get('email', email)
        user_full_name = user_info.get('name', '')
        
        logger.info("Authentication successful", extra={
            "email": user_email,
            "full_name": user_full_name,
            "token_expires_in": expires_in
        })
        
        # Generate CloudFront signed cookies
        cf_cookies = []
        if CLOUDFRONT_DOMAIN and KEY_PAIR_ID and PRIVATE_KEY_SECRET_ARN:
            try:
                current_time = int(time.time())
                cf_expires_epoch = current_time + COOKIE_TTL_SECONDS
                resource = f"https://{CLOUDFRONT_DOMAIN}/private/*"
                
                policy_cookie, signature_cookie, key_pair_cookie = create_signed_cookies(
                    resource, cf_expires_epoch
                )
                
                # Build cookie attributes
                cf_cookie_settings = (
                    f"{get_cookie_settings(is_cloudfront=True)}; "
                    f"Max-Age={COOKIE_TTL_SECONDS}"
                )
                
                cf_cookies = [
                    f"{policy_cookie}; {cf_cookie_settings}",
                    f"{signature_cookie}; {cf_cookie_settings}",
                    f"{key_pair_cookie}; {cf_cookie_settings}",
                ]
                
                logger.info("CloudFront signed cookies generated", extra={
                    "expires_epoch": cf_expires_epoch,
                    "resource": resource
                })
            except Exception as e:
                logger.error(f"Failed to generate CloudFront cookies: {e}")
                # Continue without CF cookies
        
        # Build Cognito token cookies
        cookie_settings = get_cookie_settings()
        
        cognito_cookies = [
            f"accessToken={access_token}; {cookie_settings}; Max-Age={expires_in}",
            f"idToken={id_token}; {cookie_settings}; Max-Age={expires_in}",
            f"refreshToken={refresh_token}; {cookie_settings}; Max-Age=2592000"
        ]
        
        # Combine all cookies
        all_cookies = cognito_cookies + cf_cookies
        
        # Return the minimal necessary info in the response body plus cookies
        return {
            'statusCode': 200,
            'multiValueHeaders': {
                'Set-Cookie': all_cookies,
                'Access-Control-Allow-Origin': [ALLOWED_ORIGIN],
                'Access-Control-Allow-Credentials': ['true'],
                'Content-Type': ['application/json']
            },
            'body': json.dumps({
                'message': 'Login successful',
                'isAuthenticated': True,
                'accessToken': access_token,
                'idToken': id_token,
                'cloudfront_cookies_set': len(cf_cookies) > 0,
                'user': {
                    'email': user_email,
                    'fullName': user_full_name
                }
            })
        }
        
    except ClientError as e:
        error_code = e.response.get('Error', {}).get('Code', 'UnknownError')
        error_message = e.response.get('Error', {}).get('Message', str(e))
        
        logger.error("Cognito authentication error", extra={
            "error_code": error_code,
            "error_message": error_message
        })
        
        headers = {
            'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
            'Access-Control-Allow-Credentials': 'true',
            'Content-Type': 'application/json'
        }
        
        if error_code == 'NotAuthorizedException':
            return {
                'statusCode': 401,
                'headers': headers,
                'body': json.dumps({'message': 'Incorrect username or password'})
            }
        elif error_code == 'UserNotFoundException':
            return {
                'statusCode': 404,
                'headers': headers,
                'body': json.dumps({'message': 'User does not exist'})
            }
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'message': f'Login error: {error_message}'})
        }
        
    except Exception as e:
        logger.exception("Unexpected error during login", extra={
            "error": str(e)
        })

        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': ALLOWED_ORIGIN,
                'Access-Control-Allow-Credentials': 'true',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': 'An unexpected error occurred'})
        }


def decode_id_token(id_token):
    """
    Decode and verify the ID token to extract user information.

    Verifies signature against Cognito JWKS and validates issuer and audience.
    """
    try:
        if not COGNITO_REGION:
            logger.error("Unable to verify JWT: missing Cognito region")
            return {}

        jwks = get_jwks()
        unverified_header = jwt.get_unverified_header(id_token)
        key_id = unverified_header.get("kid")

        if not key_id:
            logger.warning("Failed to decode ID token: missing key id in header")
            return {}

        matching_key = next(
            (jwk for jwk in jwks.get("keys", []) if jwk.get("kid") == key_id),
            None,
        )

        if not matching_key:
            logger.warning("Failed to decode ID token: no matching JWKS key", extra={"kid": key_id})
            return {}

        issuer = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{USER_POOL_ID}"
        claims = jwt.decode(
            id_token,
            jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(matching_key)),
            algorithms=["RS256"],
            audience=USER_POOL_CLIENT_ID,
            issuer=issuer,
        )

        if claims.get("token_use") != "id":
            logger.warning("Failed to decode ID token: invalid token_use", extra={"token_use": claims.get("token_use")})
            return {}
        
        return claims

    except (InvalidTokenError, ValueError, KeyError) as e:
        logger.warning("Failed to decode ID token", extra={
            "error": str(e)
        })
        return {}


def get_jwks() -> Dict[str, Any]:
    """Retrieve and cache Cognito JWKS for JWT signature verification."""
    if "keys" in _jwks_cache:
        return _jwks_cache

    if not COGNITO_REGION:
        raise ValueError("Missing Cognito region for JWKS retrieval")

    jwks_url = (
        f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/"
        f"{USER_POOL_ID}/.well-known/jwks.json"
    )

    try:
        with urlopen(jwks_url, timeout=5) as response:
            jwks = json.loads(response.read().decode("utf-8"))

        if not isinstance(jwks, dict) or "keys" not in jwks:
            raise ValueError("Invalid JWKS document")

        _jwks_cache.update(jwks)
        return _jwks_cache
    except Exception as e:
        logger.error("Failed to fetch JWKS", extra={"error": str(e), "jwks_url": jwks_url})
        raise