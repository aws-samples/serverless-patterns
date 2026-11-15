# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json

client = boto3.client('translate')

def lambda_handler(event, context):
    text = event['text']
    source_language = event['sl']
    target_language = event['tl']
    response = client.translate_text(
    Text=text,
    SourceLanguageCode=source_language,
    TargetLanguageCode=target_language
    )
    print(response['TranslatedText'])
    return response