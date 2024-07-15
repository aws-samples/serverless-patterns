import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
import time

def on_event(event, context):
  print(event)
  request_type = event['RequestType']
  if request_type == 'Create': return on_create(event)
  if request_type == 'Update': return on_update(event)
  if request_type == 'Delete': return on_delete(event)
  raise Exception("Invalid request type: %s" % request_type)


def on_create(event):
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
  props = event["ResourceProperties"]
  print("create new resource with props %s" % props)
  response = create_or_update_index(event)
  print(response)
  return {
      "Data": {
          "response": response
      }
  }
  return { 'PhysicalResourceId': physical_id }

def on_delete(event):
  physical_id = event["PhysicalResourceId"]
  return { 'PhysicalResourceId': physical_id }

def is_complete(event, context):
  physical_id = event["PhysicalResourceId"]
  request_type = event["RequestType"]

  # check if resource is stable based on request_type
  # is_ready = ...

  return { 'IsComplete': True }

def removeHttpsPrefix(endpoint):
    if endpoint.startswith("https://"):
        return endpoint[8:]
    return endpoint

#get aoss_host from os environ
def get_aoss_host(resource_properties):
    if "AOSSHost" not in resource_properties:
        raise Exception("AOSSHost not provided from resource properties")
    return removeHttpsPrefix(resource_properties["AOSSHost"])

def get_aoss_client(host):
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
    if "AOSSIndexName" not in resource_properties:
        raise Exception("AOSSIndexName not provided from resource properties")
    return resource_properties["AOSSIndexName"]
        
#Function to use the opensearch-py library to create an index within an opensearch collection
def create_aoss_index(index_name, aos_client):
    
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
                "id":  { 
                    "type" : "text" 
                },
                "text-metadata":  { 
                    "type" : "text" 
                },
                "x-amz-bedrock-kb-source-uri":  { 
                    "type" : "text" 
                }
            }
        }
    }
    response = aos_client.indices.create(index=index_name, body=index_body)
    print(f"Created index {index_name}")
    return response
    
def create_or_update_index(event):
    resource_properties = event['ResourceProperties']
    aoss_host = get_aoss_host(resource_properties)
    aos_client = get_aoss_client(aoss_host)
    index_name = get_aoss_index_name(resource_properties)
    response = None
    if not aos_client.indices.exists(index=index_name):
        response =  create_aoss_index(index_name=index_name, aos_client=aos_client)    
    return response
