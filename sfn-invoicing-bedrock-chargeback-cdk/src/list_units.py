# Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

"""Lists all AWS Invoice Units in the account."""

import json
import boto3


def handler(event, context):
    """Return all invoice units for the Step Functions Map state to iterate."""
    client = boto3.client('invoicing')

    try:
        units = []
        paginator = client.get_paginator('list_invoice_units')
        for page in paginator.paginate():
            for unit in page.get('InvoiceUnits', []):
                units.append({
                    'invoiceUnitId': unit['InvoiceUnitArn'].split('/')[-1],
                    'invoiceUnitArn': unit['InvoiceUnitArn'],
                    'name': unit.get('Name', 'Unknown'),
                    'description': unit.get('Description', ''),
                })
        return {'units': units, 'count': len(units)}
    except Exception as e:
        print(f'Error listing invoice units: {e}')
        raise
