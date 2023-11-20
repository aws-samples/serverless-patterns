# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import boto3
import json

client = boto3.client('comprehend')

def lambda_handler(event, context):
    text = event['text']

    response = client.detect_dominant_language(
    Text=text        
    )
    
    lang = response["Languages"][0]["LanguageCode"]
    print(lang)
    if lang == 'en':
        comp_response = "The detected language (dominant language) is English."
    elif lang == 'de':
        comp_response = "The detected language (dominant language) is German."
    elif lang == 'es':
        comp_response = "The detected language (dominant language) is Spanish."
    elif lang == 'it':
        comp_response = "The detected language (dominant language) is Italian."
    elif lang == 'pt':
        comp_response = "The detected language (dominant language) is Portuguese."
    elif lang == 'fr':
        comp_response = "The detected language (dominant language) is French."
    elif lang == 'ja':
        comp_response = "The detected language (dominant language) is Japanese."
    elif lang == 'ko':
        comp_response = "The detected language (dominant language) is Korean."
    elif lang == 'hi':
        comp_response = "The detected language (dominant language) is Hindi."
    elif lang == 'ar':
        comp_response = "The detected language (dominant language) is Arabic."
    elif lang == 'zh':
        comp_response = "The detected language (dominant language) is Chinese (simplified)."
    elif lang == 'zh-TW':
        comp_response = "The detected language (dominant language) is Chinese (traditional)."
    else:
        comp_response = "The language (dominant language) cannot be identified. Please refer. - https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html"
    
        
    return comp_response
    