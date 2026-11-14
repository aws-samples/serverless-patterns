import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import time

def on_event(event, context):
    """
    This function is the entry point for the Lambda function.
    It receives an event and a context object, and based on the request type
    in the event, it calls the appropriate function to handle the request.
    """
    print(event)
    request_type = event['RequestType']
    if request_type == 'Create': return on_create(event)
    if request_type == 'Update': return on_update(event)
    if request_type == 'Delete': return on_delete(event)
    raise Exception("Invalid request type: %s" % request_type)

def on_create(event):
    """
    This function is called when a new resource is being created.
    It prints the resource properties, calls the create_or_update_index function
    to create or update the index, and returns the response from that function.
    """
    props = event["ResourceProperties"]
    print("create new resource with props %s" % props)
    response = create_or_update_index(event)
    print(response)
    return {
        "Data": {
            "response": response
        }
    }

def on_update(event):
    """
    This function is called when an existing resource is being updated.
    It prints the resource properties, calls the create_or_update_index function
    to create or update the index, and returns the response from that function.
    """
    props = event["ResourceProperties"]
    print("create new resource with props %s" % props)
    response = create_or_update_index(event)
    print(response)
    return {
        "Data": {
            "response": response
        }
    }

def on_delete(event):
    """
    This function is called when a resource is being deleted.
    It returns the physical resource ID of the resource being deleted.
    """
    physical_id = event["PhysicalResourceId"]
    return {'PhysicalResourceId': physical_id}

def is_complete(event, context):
    """
    This function checks if the resource is in a stable state based on the request type.
    It returns a dictionary indicating whether the resource is complete or not.
    """
    physical_id = event["PhysicalResourceId"]
    request_type = event["RequestType"]

    # check if resource is stable based on request_type
    # is_ready = ...

    return {'IsComplete': True}

def removeHttpsPrefix(endpoint):
    """
    This function removes the "https://" prefix from a given endpoint string,
    if present, and returns the modified string.
    """
    if endpoint.startswith("https://"):
        return endpoint[8:]
    return endpoint

def get_aoss_host(resource_properties):
    """
    This function retrieves the Amazon OpenSearch Service (AOSS) host from the
    resource properties. It raises an exception if the AOSSHost property is not provided.
    """
    if "AOSSHost" not in resource_properties:
        raise Exception("AOSSHost not provided from resource properties")
    return removeHttpsPrefix(resource_properties["AOSSHost"])

def get_aoss_client(host):
    """
    This function creates and returns an Amazon OpenSearch Service (AOSS) client
    using the provided host. It authenticates the client using AWS credentials
    and the AWS Signature Version 4 signer.
    """
    auth = AWSV4SignerAuth(
        boto3.Session().get_credentials(),
        boto3.session.Session().region_name,
        "aoss"
    )
    # create an opensearch client and use the request-signer
    return OpenSearch(
        hosts=[{'host': host, 'port': 443}],
        http_auth=auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )

def get_aoss_index_name(resource_properties):
    """
    This function retrieves the Amazon OpenSearch Service (AOSS) index name from the
    resource properties. It raises an exception if the AOSSIndexName property is not provided.
    """
    if "AOSSIndexName" not in resource_properties:
        raise Exception("AOSSIndexName not provided from resource properties")
    return resource_properties["AOSSIndexName"]

def create_aoss_index(index_name, aos_client):
    """
    This function creates an index in the Amazon OpenSearch Service (AOSS) using the
    provided index name and client. It configures the index settings and mappings
    for vector search and returns the response from the index creation operation.
    """
    index_body = {
        "settings": {
            "index.knn": True
        },
        "mappings": {
            "properties": {
                "vector": {
                    "type": "knn_vector",
                    "dimension": 1024,
                    "method": {
                        "name": "hnsw",
                        "space_type": "l2",
                        "engine": "faiss",
                        "parameters": {
                            "ef_construction": 512,
                            "m": 16
                        }
                    }
                },
                "text": {
                    "type": "text"
                },
                "id": {
                    "type": "text"
                },
                "text-metadata": {
                    "type": "text"
                },
                "x-amz-bedrock-kb-source-uri": {
                    "type": "text"
                }
            }
        }
    }
    response = aos_client.indices.create(index=index_name, body=index_body)
    print(f"Created index {index_name}")
    return response

def create_or_update_index(event):
    """
    This function creates or updates an index in the Amazon OpenSearch Service (AOSS).
    It retrieves the AOSS host and index name from the resource properties, creates
    an AOSS client, and checks if the index exists. If the index doesn't exist,
    it creates a new index using the create_aoss_index function. It returns the
    response from the index creation or update operation.
    """
    resource_properties = event['ResourceProperties']
    aoss_host = get_aoss_host(resource_properties)
    aos_client = get_aoss_client(aoss_host)
    index_name = get_aoss_index_name(resource_properties)
    response = None
    if not aos_client.indices.exists(index=index_name):
        response = create_aoss_index(index_name=index_name, aos_client=aos_client)
    return response
