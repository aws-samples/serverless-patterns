from time import sleep
import boto3
from boto3.dynamodb.types import TypeDeserializer
from typing import Dict, Any
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth, exceptions
import os 

dynamodb = boto3.resource('dynamodb')
converter = TypeDeserializer()

# sample: host = 'abcdefg12345567.us-west-2.aoss.amazonaws.com'  
host = (os.environ['AOSS_ENDPOINT'].split("//"))[1]  # serverless collection endpoint, without https://

region = os.environ['AWS_REGION']
service = 'aoss'

credentials = boto3.Session().get_credentials()
auth = AWSV4SignerAuth(credentials, region, service)

opensearch = OpenSearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
    pool_maxsize=20,
)

def handler(event, context):
    for record in event["Records"]:
        if not record.get("eventName") or not record.get("dynamodb") or not record["dynamodb"].get("Keys"):
            continue

        partition_key = record["dynamodb"]["Keys"]["partitionKey"]["S"]
        # we are using partition key only, but if you need sort key or id, you can do:
        sort_key = record["dynamodb"]["Keys"]["sortKey"]["S"]
        # id = record["dynamodb"]["Keys"]["id"]["S"]

        try:
            if record["eventName"] == "REMOVE":
                # DELETE request to your index
                try:
                    remove_document_from_open_search(partition_key)
                except exceptions.NotFoundError:
                    pass

            else:
                # INSERT and MODIFY, both go to new image
                if not record["dynamodb"].get("NewImage"):
                    continue

                user_document_raw = record["dynamodb"]["NewImage"]
                user_document = {k: converter.deserialize(v) for k, v in user_document_raw.items()}
                
                return index_document_in_open_search(user_document, partition_key, sort_key)
        except Exception as error:
            print(f"Error occurred updating OpenSearch domain: {error}")
            raise error

def remove_document_from_open_search(partition_key: str, ) -> None:
    response = opensearch.indices.delete(
        index=partition_key,
    )

    print("index removed successfully")
    pass

def index_document_in_open_search(user_document: Dict[str, Any], partition_key: str, sort_key: str) -> None:
    response = opensearch.indices.create(
        index = partition_key,
    )

    sleep(5) # wait until the index is operable

    response = opensearch.index(
        index = partition_key,
        body = user_document,
        id = sort_key,
    )

    print("index successfully")
    pass
