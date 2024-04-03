import logging
import boto3
from botocore.exceptions import ClientError
import json
import logging
import os
import secrets

logger = logging.getLogger()
logger.setLevel(logging.INFO)
s3_client = boto3.client('s3')
ddb_client = boto3.client('dynamodb')
ddb_table = os.environ['NONCE_TABLE']

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    print('The presigned URL is {}'.format(response))
    return response


def create_nonce():
    # Generate a nonce with 16 bytes (128 bits)
    nonce = secrets.token_bytes(16)    
    return nonce

def create_ddb_entry(nonce, url):
    count = "0"
    res = ddb_client.put_item(TableName=ddb_table, Item={'nonce_id': {'S': nonce.hex()}, 'url': {'S': url}, 'count': {'S': count}})
    return res


def lambda_handler(event, context):
    logger.info('Received event for generate url : ' + json.dumps(event))
    # read the event values as json objects

    # Convert the dictionary to JSON string
    json_data = json.dumps(event)

    # Now you can parse the JSON string
    json_event = json.loads(json_data)
    body = json_event['body']
    jbody = json.loads(body)
    url = create_presigned_url(jbody['bucket_name'], jbody['object_name'])
    nonce = create_nonce()
    create_ddb_entry(nonce, url)
    requestContext = json_event["requestContext"]
    domain_name = requestContext["domainName"]
    stage = requestContext["stage"]
    # /prod/generate-url
    url = 'https://'+domain_name+'/'+stage+'/access-object'
    response = {
    "statusCode": 200,
    "body": url+'?nonce='+nonce.hex()
    }
    return response