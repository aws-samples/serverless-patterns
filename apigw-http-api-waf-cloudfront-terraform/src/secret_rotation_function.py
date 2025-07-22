import boto3
import json
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

unique_key_length = int(os.environ["UNIQUE_KEY_LENGTH"])

def lambda_handler(event, context):
    service_client = boto3.client('secretsmanager')

    secretArn = event['SecretId']
    secretToken = event['ClientRequestToken']
    secretStep = event['Step']
    metadata = service_client.describe_secret(SecretId=secretArn)

    if not metadata['RotationEnabled']:
        logger.error("Secret %s is not enabled for rotation" % secretArn)
        raise ValueError("Secret %s is not enabled for rotation" % secretArn)
    versions = metadata['VersionIdsToStages']
    if secretToken not in versions:
        logger.error("Secret version %s has no stage for rotation of secret %s." % (secretToken, secretArn))
        raise ValueError("Secret version %s has no stage for rotation of secret %s." % (secretToken, secretArn))
    if "AWSCURRENT" in versions[secretToken]:
        logger.info("Secret version %s already set as AWSCURRENT for secret %s." % (secretToken, secretArn))
        return
    elif "AWSPENDING" not in versions[secretToken]:
        logger.error("Secret version %s not set as AWSPENDING for rotation of secret %s." % (secretToken, secretArn))
        raise ValueError("Secret version %s not set as AWSPENDING for rotation of secret %s." % (secretToken, secretArn))

    if secretStep == "createSecret":
        create_secret(service_client, secretArn, secretToken)

    elif secretStep == "setSecret":
        set_secret(service_client, secretArn, secretToken)

    elif secretStep == "testSecret":
        test_secret(service_client, secretArn, secretToken)

    elif secretStep == "finishSecret":
        finish_secret(service_client, secretArn, secretToken)

    else:
        raise ValueError("Invalid step parameter") 

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Encryption completed",         
        }),
    }

def create_secret(service_client, arn, token):
    # Make sure the current secret exists
    response = service_client.get_secret_value(SecretId=arn, VersionStage="AWSCURRENT")

    # Now try to get the secret version, if that fails, put a new secret
    try:
        service_client.get_secret_value(SecretId=arn, VersionId=token, VersionStage="AWSPENDING")
        logger.info("createSecret: Successfully retrieved secret for %s." % arn)
    except service_client.exceptions.ResourceNotFoundException:
        #Generate passphrase
        pwdResponse= service_client.get_random_password(PasswordLength=unique_key_length)
        newUniqueKey = pwdResponse["RandomPassword"]

        # Put the secret
        response = service_client.put_secret_value(
            SecretId=arn,
            ClientRequestToken=token,
            SecretString=newUniqueKey,
            VersionStages=['AWSPENDING']
        )
        logger.info("createSecret: Successfully put secret for ARN %s and version %s." % (arn, token))
        logger.info(response)

def set_secret(service_client, arn, token):
    # This is where the secret should be set in the service
    logger.info("Skip set secret step")


def test_secret(service_client, arn, token):
    # This is where the secret should be tested against the external service using the secret
    logger.info("Skip test secret step")


def finish_secret(service_client, arn, token):
    # First describe the secret to get the current version
    metadata = service_client.describe_secret(SecretId=arn)
    current_version = None
    for version in metadata["VersionIdsToStages"]:
        if "AWSCURRENT" in metadata["VersionIdsToStages"][version]:
            if version == token:
                # The correct version is already marked as current, return
                logger.info("finishSecret: Version %s already marked as AWSCURRENT for %s" % (version, arn))
                return
            current_version = version
            break

    # Finalize by staging the secret version current
    service_client.update_secret_version_stage(SecretId=arn, VersionStage="AWSCURRENT", MoveToVersionId=token, RemoveFromVersionId=current_version)
    logger.info("finishSecret: Successfully set AWSCURRENT stage to version %s for secret %s." % (token, arn))