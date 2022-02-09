# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import boto3

def lambda_handler(event, context):
    
    text = event['text']
    client = boto3.client('comprehend')
    sentiment =client.detect_sentiment(Text=text,LanguageCode='en')
    prediction = sentiment['Sentiment']
    score = sentiment['SentimentScore']
    
    return {
        'comprehend_prediction': prediction,
        'comprehend_scores': score
    }
