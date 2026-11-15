import json
from datetime import datetime
from datetime import timedelta
import boto3
import pytz
from dateutil import parser

trustedAdvisor = boto3.client('support')
utc = pytz.UTC


def lambda_handler(event, context):
    response = trustedAdvisor.describe_trusted_advisor_checks(language='en')
    for tacheck in response['checks']:
        if tacheck['name'] in 'Amazon S3 Bucket Permissions':
            checkId = tacheck['id']
            checkResult = trustedAdvisor.describe_trusted_advisor_check_result(checkId=checkId, language='en')
            if utc.localize(datetime.now()) > parser.parse(checkResult['result']['timestamp']) + timedelta(minutes=6):
                trustedAdvisor.refresh_trusted_advisor_check(checkId=checkId)

    return {
        'statusCode': 200,
        'body': json.dumps('Trusted Advisor Check: Amazon S3 Bucket Permissions, has been triggered to refresh.')
    }
