# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0 (2026)
"""Bedrock Enrichment: Called by Amazon EventBridge Pipes as enrichment step.
Classifies sentiment, extracts entities, and generates summary using
Amazon Bedrock before the message reaches the target."""

import json
import os
from datetime import datetime, timezone

import boto3

BEDROCK_CLIENT = boto3.client('bedrock-runtime')
MODEL_ID = os.environ.get('MODEL_ID', 'us.anthropic.claude-sonnet-4-6-20250514-v1:0')
DYNAMODB = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('ENRICHED_TABLE', '')


def lambda_handler(event, context):
    """Enrich messages from Amazon EventBridge Pipes with Amazon Bedrock AI."""
    # Pipes sends a list of records for batch enrichment
    results = []

    for record in event:
        try:
            # Parse SQS message body
            body = json.loads(record.get('body', '{}'))
            message = body.get('message', record.get('body', ''))
            message_id = record.get('messageId', 'unknown')

            # Call Amazon Bedrock for enrichment
            enrichment = invoke_bedrock(message)

            results.append({
                'messageId': message_id,
                'originalMessage': message[:500],
                'sentiment': enrichment.get('sentiment', 'UNKNOWN'),
                'entities': json.dumps(enrichment.get('entities', [])),
                'summary': enrichment.get('summary', ''),
                'enrichedAt': datetime.now(timezone.utc).isoformat(),
                'ttl': str(int(datetime.now(timezone.utc).timestamp()) + 86400 * 7),
            })

            # Write enriched data to Amazon DynamoDB
            if TABLE_NAME:
                try:
                    table = DYNAMODB.Table(TABLE_NAME)
                    table.put_item(Item={
                        'messageId': message_id,
                        'originalMessage': message[:500],
                        'sentiment': enrichment.get('sentiment', 'UNKNOWN'),
                        'entities': json.dumps(enrichment.get('entities', [])),
                        'summary': enrichment.get('summary', ''),
                        'enrichedAt': datetime.now(timezone.utc).isoformat(),
                        'ttl': int(datetime.now(timezone.utc).timestamp()) + 86400 * 7,
                    })
                except Exception as ddb_err:
                    print(f'DynamoDB write failed: {ddb_err}')

        except Exception as e:
            print(f'Enrichment failed for record: {e}')
            results.append({
                'messageId': record.get('messageId', 'unknown'),
                'originalMessage': str(record.get('body', ''))[:500],
                'sentiment': 'ERROR',
                'entities': '[]',
                'summary': f'Enrichment failed: {str(e)[:100]}',
                'enrichedAt': datetime.now(timezone.utc).isoformat(),
                'ttl': str(int(datetime.now(timezone.utc).timestamp()) + 86400 * 7),
            })

    return results


def invoke_bedrock(message: str) -> dict:
    """Call Amazon Bedrock to classify sentiment, extract entities, summarize."""
    prompt = f"""Analyze the following message and return a JSON object with:
- "sentiment": one of POSITIVE, NEGATIVE, NEUTRAL, MIXED
- "entities": array of extracted entity strings (people, orgs, products)
- "summary": one-sentence summary (max 100 chars)

Message: {message[:1000]}

Return ONLY valid JSON, no explanation."""

    try:
        response = BEDROCK_CLIENT.invoke_model(
            modelId=MODEL_ID,
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                'anthropic_version': 'bedrock-2023-05-31',
                'max_tokens': 200,
                'messages': [{'role': 'user', 'content': prompt}],
            }),
        )

        result = json.loads(response['body'].read())
        text = result['content'][0]['text']

        # Strip markdown code blocks if present (```json ... ```)
        text = text.strip()
        if text.startswith('```'):
            text = text.split('\n', 1)[1] if '\n' in text else text[3:]
        if text.endswith('```'):
            text = text[:-3].strip()

        # Parse the JSON response from Bedrock
        enrichment = json.loads(text)
        return enrichment

    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f'Bedrock response parse error: {e}')
        return {'sentiment': 'UNKNOWN', 'entities': [], 'summary': 'Parse error'}
    except Exception as e:
        print(f'Bedrock invocation error: {e}')
        raise
