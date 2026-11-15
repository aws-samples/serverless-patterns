import os
import boto3

tag_client = boto3.client('resourcegroupstaggingapi')
log_client = boto3.client('logs')
lambda_client = boto3.client('lambda')

AWS_REGION = os.environ['AWS_REGION']
AWS_ACCOUNT_ID = boto3.client('sts').get_caller_identity()['Account']

# Input comes in a form of Foo=Bar,Baz=Foo, which is then sanitized into [(Foo, Bar), (Baz, Foo)]
tag_pairs = list(filter(lambda x: x != '', map(str.strip, os.environ['EXPORT_TAGS'].split(','))))
EXPORT_TAGS = [list(map(str.strip, item.split('='))) for item in tag_pairs]


def handler(event, context):
    tag_filters = []
    for (key, value) in EXPORT_TAGS:
        tag_filters.append({
            'Key': key,
            'Values': [value]
        })

    response = tag_client.get_resources(TagFilters=tag_filters, ResourceTypeFilters=['logs'])

    log_groups = []

    arn_prefix = 'arn:aws:logs:{}:{}:log-group:'.format(AWS_REGION, AWS_ACCOUNT_ID)
    for item in response.get('ResourceTagMappingList'):
        log_groups.append({"name": item.get('ResourceARN').replace(arn_prefix, '')})

    return {'logGroups': log_groups}
