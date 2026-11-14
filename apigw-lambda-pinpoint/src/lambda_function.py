import json
import os

import boto3

# Amazon Pinpoint phone number validation is still supported for all accounts.
pinpoint_client = boto3.client('pinpoint')
# SMS sending uses the AWS End User Messaging SMS and Voice v2 API.
sms_client = boto3.client('pinpoint-sms-voice-v2')

ORIGINATION_IDENTITY = os.environ.get("ORIGINATION_IDENTITY")
MESSAGE = "Your OTP is 1234"
MESSAGE_TYPE = "TRANSACTIONAL"


def lambda_handler(event, context):
    try:
        destination_number = json.loads(event.get('body') or '{}')["destination_number"]
    except (ValueError, KeyError, TypeError):
        return {'statusCode': 400, 'body': "Request body must be JSON with a destination_number."}

    try:
        validation = pinpoint_client.phone_number_validate(
            NumberValidateRequest={'PhoneNumber': destination_number})
        number = validation["NumberValidateResponse"]
        if number["PhoneType"] == "INVALID":
            return {'statusCode': 400, 'body': "The destination number isn't a valid phone number."}

        print("Sending SMS message.")
        response = sms_client.send_text_message(
            DestinationPhoneNumber=number.get("CleansedPhoneNumberE164", destination_number),
            OriginationIdentity=ORIGINATION_IDENTITY,
            MessageBody=MESSAGE,
            MessageType=MESSAGE_TYPE)

        message_id = response['MessageId']
        print(f"Message sent! Message ID: {message_id}.")
        return {'statusCode': 200, 'body': f"Message sent! Message ID: {message_id}."}

    except Exception as e:
        print(f"Couldn't send message: {e}")
        return {'statusCode': 500, 'body': "Couldn't send message!"}
