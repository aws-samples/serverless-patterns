import aws_encryption_sdk
from aws_encryption_sdk import CommitmentPolicy
from aws_encryption_sdk.exceptions import DecryptKeyError
from urllib import request, parse
import base64
import json
import boto3
import os

kms_key_arn = os.environ['KEY_ARN']
phone_number_id = os.environ['PHONE_NUMBER_ID']
secret_name = os.environ['SECRET_NAME']
kms_kwargs = dict(key_ids=[kms_key_arn])
master_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(**kms_kwargs)

def send_whatsapp_message(secret, to_number, url, otp):
    headers = {
        'content-type': 'application/json',
        'Authorization': secret
    }
    data = parse.urlencode({
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": to_number,
        "type": "template",
        "template": {
            "name": "otp_message",
            "language": {
            "code": "en"
            },
            "components": [
            {
                "type": "body",
                "parameters": [
                {
                    "type": "text",
                    "text": otp
                }
                ]
            },
            {
                "type": "button",
                "sub_type": "url",
                "index": "0",
                "parameters": [
                {
                    "type": "text",
                    "text": otp
                }
                ]
            }
            ]
        }    
    }).encode()
    req =  request.Request(url, data=data, headers=headers)
    resp = request.urlopen(req)
    result = resp.read().decode('utf-8')
    if '"message_status":"accepted"' in result:
            print("Message sent successfully")

def decrypt(ciphertext):
                    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT)
                    try:
                        decrypted_text, encryptor_header = client.decrypt(source=ciphertext,key_provider=master_key_provider)
                    except DecryptKeyError as err:
                        err_info = "Error decrypting with KMS key. Please check if the KMS key with ARN {} exists and the role that the CustomSMSSender Lambda function assumes has the kms:Decrypt permission on the key".format(kms_key_arn)
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        err_msg = json.dumps({"errorType": exc_type.__name__,
                                              "errorMessage": str(exc_value),
                                              "errorInfo" : err_info,
                                              "stackTrace": traceback.format_exception(exc_type, exc_value, exc_traceback)})
                        logger.error(err_msg)
                        raise err
                    return decrypted_text.decode()


def handler(event, context):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')
    url = 'https://graph.facebook.com/v15.0/' + phone_number_id + '/messages'

    plain_text_code = decrypt(base64.b64decode(event["request"]["code"]))
    PhoneNumber = event["request"]["userAttributes"]["phone_number"]
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret = get_secret_value_response['SecretString']

    send_whatsapp_message(secret,PhoneNumber,url,plain_text_code)
    return