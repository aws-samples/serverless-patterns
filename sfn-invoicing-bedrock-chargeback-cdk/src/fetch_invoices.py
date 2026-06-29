# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Fetches invoice summaries for a specific Invoice Unit."""

import json
import boto3
import os
from datetime import datetime, timedelta


def handler(event, context):
    """Fetch invoice summaries for one invoice unit (called per-unit by Map state)."""
    client = boto3.client('invoicing')
    sts = boto3.client('sts')

    invoice_unit_id = event.get('invoiceUnitId', '')
    unit_name = event.get('name', 'Unknown')

    # Get current account ID for selector
    account_id = sts.get_caller_identity()['Account']

    # Fetch invoices from the last 30 days (API limit: max 1 month)
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=30)

    try:
        response = client.list_invoice_summaries(
            Selector={
                'ResourceType': 'ACCOUNT_ID',
                'Value': account_id,
            },
            Filter={
                'TimeInterval': {
                    'StartDate': start_date.strftime('%Y-%m-%dT00:00:00Z'),
                    'EndDate': end_date.strftime('%Y-%m-%dT00:00:00Z'),
                },
            },
        )

        invoices = []
        for summary in response.get('InvoiceSummaries', []):
            invoices.append({
                'invoiceId': summary.get('InvoiceId', ''),
                'accountId': summary.get('AccountId', ''),
                'billingPeriod': str(summary.get('BillingPeriod', {})),
                'totalAmount': str(summary.get('BaseCurrencyAmount', {}).get('Amount', '0')),
                'currency': summary.get('BaseCurrencyAmount', {}).get('Currency', 'USD'),
                'invoiceType': summary.get('InvoiceType', ''),
            })

        return {
            'invoiceUnitId': invoice_unit_id,
            'unitName': unit_name,
            'invoices': invoices,
            'totalInvoices': len(invoices),
            'periodStart': start_date.strftime('%Y-%m-%d'),
            'periodEnd': end_date.strftime('%Y-%m-%d'),
        }
    except Exception as e:
        print(f'Error fetching invoices for unit {invoice_unit_id}: {e}')
        raise
