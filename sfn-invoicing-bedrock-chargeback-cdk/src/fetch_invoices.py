# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Fetches invoice summaries for a specific Invoice Unit."""

import json
import boto3
from datetime import datetime, timedelta


def handler(event, context):
    """Fetch invoice summaries for one invoice unit (called per-unit by Map state)."""
    client = boto3.client('invoicing')

    invoice_unit_id = event.get('invoiceUnitId', '')
    unit_name = event.get('name', 'Unknown')

    # Fetch invoices from the last 90 days
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=90)

    try:
        response = client.list_invoice_summaries(
            Filter={
                'InvoiceUnitId': invoice_unit_id,
                'TimeRange': {
                    'StartDate': start_date.strftime('%Y-%m-%d'),
                    'EndDate': end_date.strftime('%Y-%m-%d'),
                },
            }
        )

        invoices = []
        for summary in response.get('InvoiceSummaries', []):
            invoices.append({
                'invoiceId': summary.get('InvoiceId', ''),
                'issuedDate': summary.get('IssuedDate', ''),
                'totalAmount': str(summary.get('TotalAmount', {}).get('Amount', '0')),
                'currency': summary.get('TotalAmount', {}).get('Currency', 'USD'),
                'status': summary.get('Status', ''),
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
