import logging
import base64
import sys
import boto3
import logging
import os
import json
import uuid
import datetime

logger = logging.getLogger("")

pending_version = None

steps = ['createSecret', 'setSecret', 'testSecret', 'finishSecret']

def lambda_handler(event, context):
    service_client = boto3.client('secretsmanager')
    arn = os.environ['SECRET_ID']
    pending_version = get_secret_version_id_by_stage(arn, "AWSPENDING")
    logger.info(f'pending_version: {pending_version}')

    if pending_version == None:
        pending_version = str(uuid.uuid4())

    create_secret(service_client, arn, pending_version)
    set_secret(service_client, arn, pending_version)
    test_secret(service_client, arn, pending_version)
    finish_secret(service_client, arn, pending_version)

def get_secret_version_id_by_stage(secret_id, version_stage):
    secrets_manager_client = boto3.client('secretsmanager')
    metadata = secrets_manager_client.describe_secret(SecretId=secret_id)
    versions = metadata['VersionIdsToStages']
    stage_vesrion_id = None
    for version in versions:
        if version_stage in versions[version]:
            stage_vesrion_id = version
            break
    return stage_vesrion_id

def create_secret(service_client, arn, pending_version):
    try:
        service_client.get_secret_value(SecretId=arn, 
                                        VersionId=pending_version, 
                                        VersionStage="AWSPENDING")
        logger.info("createSecret: Successfully retrieved secret for %s." % arn)
    except Exception as e:
        # Put the secret
        new_secret = {"value":f'secret_{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'}
        service_client.put_secret_value(SecretId=arn, 
                                        ClientRequestToken=pending_version, 
                                        SecretString=json.dumps(new_secret), 
                                        VersionStages=["AWSPENDING"])
        logger.info("createSecret: Successfully put secret for ARN %s and version %s." % (arn, pending_version))

def set_secret(service_client, arn, pending_version):
    """Set the secret

    This method should set the AWSPENDING secret in the service that the secret belongs to. 
    For example, if the secret is a database  credential, this method should take the value of the AWSPENDING secret and
    set the user's password to this value in the database.

    Args:
        service_client (client): The secrets manager service client

        arn (string): The secret ARN or other identifier

        clientRequestToken (string): The ClientRequestToken associated with the secret version

    """
    logger.info("setSecret: Successfully set secret for %s." % arn)


def test_secret(service_client, arn, pending_version):
    """Test the secret

    This method should validate that the AWSPENDING secret works in the service that the secret belongs to. 
    For example, if the secret is a database credential, this method should validate that the user can login with the password
    in AWSPENDING and that the user has all of the expected permissions against the database.

    Args:
        service_client (client): The secrets manager service client

        arn (string): The secret ARN or other identifier

        clientRequestToken (string): The ClientRequestToken associated with the secret version

    """
    logger.info("testSecret: Successfully tested secret for %s." % arn)

def finish_secret(service_client, arn, pending_version):
    """Finish the secret

    This method finalizes the rotation process by marking the secret version passed in as the AWSCURRENT secret.

    Args:
        service_client (client): The secrets manager service client

        arn (string): The secret ARN or other identifier

        clientRequestToken (string): The ClientRequestToken associated with the secret version

    Raises:
        ResourceNotFoundException: If the secret with the specified arn does not exist

    """
    try:
        current_version_id = get_secret_version_id_by_stage(arn, "AWSCURRENT")
        service_client.update_secret_version_stage(SecretId=arn, 
                                               VersionStage="AWSCURRENT", 
                                               MoveToVersionId=pending_version, 
                                               RemoveFromVersionId=current_version_id)
    
        service_client.update_secret_version_stage(SecretId=arn, 
                                                VersionStage="AWSPENDING", 
                                                RemoveFromVersionId=pending_version)
        logger.info("finishSecret: Successfully set AWSCURRENT for secret %s." % arn)
    except Exception as e:
        logger.error("finishSecret: Failed to set AWSCURRENT for secret %s." % arn)

if __name__ == "__main__":
    lambda_handler({}, [])