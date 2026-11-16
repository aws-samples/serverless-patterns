# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import boto3
translate_client = boto3.client('translate')

def lambda_handler(event, context):
    # Fetch the message body from the request event
    req_body = json.loads(event['body'])

    try:
        # Call translate_text API with the text and language given in the request body
        translate_response = translate_client.translate_text(
            Text=req_body["OriginalText"],
            SourceLanguageCode='auto',
            TargetLanguageCode=req_body["TranslateToLanguage"]
        )

        # Get the translated text from the response
        response_text = translate_response['TranslatedText']
    except Exception as errormessage:
        # Get the error messages if translation fails
        response_text = str(errormessage)

    # return translated text or error response if translation fails
    return {
        'statusCode': 200,
        'body': json.dumps(response_text)
    }
