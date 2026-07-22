"""
AWS Invoice Retrieval and Bedrock Analysis

Retrieves invoice summaries and PDFs via AWS Invoicing APIs,
archives PDFs to S3, and generates cost analysis using Amazon Bedrock.
"""

import json
import os
import urllib.request
from datetime import datetime, timedelta

import boto3

BUCKET_NAME = os.environ['BUCKET_NAME']
MODEL_ID = os.environ['MODEL_ID']

s3_client = boto3.client('s3')
invoicing_client = boto3.client('invoicing', region_name='us-east-1')
bedrock_client = boto3.client('bedrock-runtime')


def handler(event, context):
    """Retrieve invoices, archive PDFs to Amazon S3, and analyze with Amazon Bedrock."""
    try:
        # Determine billing period (previous month)
        today = datetime.utcnow()
        first_of_month = today.replace(day=1)
        last_month_end = first_of_month - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)

        start_date = last_month_start.strftime('%Y-%m-%dT00:00:00')
        end_date = last_month_end.strftime('%Y-%m-%dT23:59:59')

        account_id = context.invoked_function_arn.split(':')[4]

        # Step 1: List invoice summaries
        response = invoicing_client.list_invoice_summaries(
            Selector={'ResourceType': 'ACCOUNT_ID', 'Value': account_id},
            Filter={'TimeInterval': {'StartDate': start_date, 'EndDate': end_date}}
        )

        invoices = response.get('InvoiceSummaries', [])
        if not invoices:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'No invoices found for the billing period', 'period': f'{last_month_start.strftime("%Y-%m")}'}),
            }

        results = []
        for invoice in invoices:
            invoice_id = invoice['InvoiceId']
            total_amount = invoice.get('BaseCurrencyAmount', {}).get('TotalAmount', '0')
            currency = invoice.get('BaseCurrencyAmount', {}).get('CurrencyCode', 'USD')

            # Step 2: Get invoice PDF
            pdf_response = invoicing_client.get_invoice_pdf(InvoiceId=invoice_id)
            document_url = pdf_response['InvoicePDF']['DocumentUrl']

            # Download PDF via presigned URL
            pdf_data = urllib.request.urlopen(document_url).read()

            # Step 3: Archive PDF to Amazon S3
            s3_key = f"invoices/{last_month_start.strftime('%Y/%m')}/{invoice_id}.pdf"
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=s3_key,
                Body=pdf_data,
                ContentType='application/pdf',
            )

            results.append({
                'invoiceId': invoice_id,
                'amount': total_amount,
                'currency': currency,
                's3Key': s3_key,
            })

        # Step 4: Analyze with Bedrock
        summary_prompt = build_analysis_prompt(invoices, last_month_start.strftime('%Y-%m'))
        analysis = invoke_bedrock(summary_prompt)

        # Store analysis in Amazon S3
        analysis_key = f"analysis/{last_month_start.strftime('%Y/%m')}/summary.json"
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=analysis_key,
            Body=json.dumps({'analysis': analysis, 'invoices': results}, indent=2),
            ContentType='application/json',
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Processed {len(invoices)} invoice(s)',
                'period': last_month_start.strftime('%Y-%m'),
                'totalInvoices': len(invoices),
                'analysisKey': analysis_key,
                'analysis': analysis,
            }),
        }

    except Exception as e:
        print(f"Error: {str(e)}")
        raise


def build_analysis_prompt(invoices, period):
    """Build a prompt for Bedrock to analyze invoice data."""
    invoice_data = []
    for inv in invoices:
        invoice_data.append({
            'invoiceId': inv.get('InvoiceId'),
            'type': inv.get('InvoiceType'),
            'total': inv.get('BaseCurrencyAmount', {}).get('TotalAmount'),
            'currency': inv.get('BaseCurrencyAmount', {}).get('CurrencyCode'),
            'subtotal': inv.get('BaseCurrencyAmount', {}).get('AmountBreakdown', {}).get('SubTotalAmount'),
            'discounts': inv.get('BaseCurrencyAmount', {}).get('AmountBreakdown', {}).get('Discounts', {}).get('TotalAmount'),
            'taxes': inv.get('BaseCurrencyAmount', {}).get('AmountBreakdown', {}).get('Taxes', {}).get('TotalAmount'),
        })

    return f"""Analyze the following AWS invoice data for billing period {period}.
Provide:
1. A concise executive summary of total spend
2. Breakdown by invoice type (if multiple)
3. Tax and discount analysis
4. Month-over-month trend observation (note if this is the first month of data)
5. Actionable cost optimization recommendations based on the amounts

Invoice data:
{json.dumps(invoice_data, indent=2)}

Respond in structured JSON with keys: executiveSummary, breakdown, taxAnalysis, recommendations."""


def invoke_bedrock(prompt):
    """Invoke Amazon Bedrock for invoice analysis."""
    response = bedrock_client.invoke_model(
        modelId=MODEL_ID,
        contentType='application/json',
        accept='application/json',
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 1024,
            'messages': [{'role': 'user', 'content': prompt}],
        }),
    )
    result = json.loads(response['body'].read())
    return result['content'][0]['text']
