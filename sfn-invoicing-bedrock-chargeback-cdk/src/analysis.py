# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Runs Amazon Bedrock analysis on invoice data and writes chargeback allocation to DynamoDB."""

import json
import os
import boto3
from datetime import datetime


def handler(event, context):
    """Analyze invoices for one BU via Bedrock and write chargeback to DynamoDB."""
    bedrock = boto3.client('bedrock-runtime')
    dynamodb = boto3.resource('dynamodb')

    model_id = os.environ['MODEL_ID']
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)

    invoice_unit_id = event.get('invoiceUnitId', '')
    unit_name = event.get('unitName', 'Unknown')
    invoices = event.get('invoices', [])
    period_start = event.get('periodStart', '')
    period_end = event.get('periodEnd', '')

    # Build prompt for Bedrock
    invoice_summary = json.dumps(invoices, indent=2)
    prompt = (
        f"You are a FinOps analyst. Analyze the following AWS invoice data for business unit '{unit_name}' "
        f"(period: {period_start} to {period_end}).\n\n"
        f"Invoice data:\n{invoice_summary}\n\n"
        "Provide:\n"
        "1. Total spend for this business unit\n"
        "2. Month-over-month trend (increasing/decreasing/stable)\n"
        "3. Chargeback allocation recommendation (percentage split if shared services detected)\n"
        "4. Cost optimization opportunities\n\n"
        "Respond in JSON format with keys: totalSpend, trend, chargebackAllocation, optimizations"
    )

    try:
        response = bedrock.converse(
            modelId=model_id,
            messages=[{'role': 'user', 'content': [{'text': prompt}]}],
            inferenceConfig={'maxTokens': 1024, 'temperature': 0.1},
        )

        analysis_text = response['output']['message']['content'][0]['text']

        # Write to DynamoDB
        table.put_item(Item={
            'invoiceUnitId': invoice_unit_id,
            'period': f"{period_start}_{period_end}",
            'unitName': unit_name,
            'invoiceCount': len(invoices),
            'analysis': analysis_text,
            'analyzedAt': datetime.utcnow().isoformat(),
            'modelId': model_id,
        })

        return {
            'invoiceUnitId': invoice_unit_id,
            'unitName': unit_name,
            'invoiceCount': len(invoices),
            'analysis': analysis_text,
            'status': 'SUCCESS',
        }
    except Exception as e:
        print(f'Error analyzing invoices for unit {invoice_unit_id}: {e}')
        raise
