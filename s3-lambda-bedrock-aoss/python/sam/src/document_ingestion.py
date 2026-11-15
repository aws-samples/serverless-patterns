import json
import boto3 
import os
from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
from PyPDF2 import PdfReader

#copy an object from s3 to /tmp
def copy_object_to_tmp(bucket, key):
    s3_client = boto3.client("s3")
    file_name = os.path.basename(key)
    local_path = f"/tmp/{file_name}"
    s3_client.download_file(bucket, key, local_path)
    print(f"Downloaded file to local path {local_path}")
    return local_path

#create a list variable named pages, use PdfReader to extract pages, enumerating over the pages collecting the index and page. 
# Then add an item to the pages list, each item to include a page number and the page text
def extract_pages_from_pdf(local_path):
    reader = PdfReader(local_path, 'rb')
    pages = []
    for index, page in enumerate(reader.pages):
        pages.append([index, page.extract_text()])
    print(f"Extracted {len(pages)} pages")
    return pages

#Given a list of pages, create embeddings for each page and store the embedding to OpenSearch vector index
def embed_and_store_pages(pages):
    responses=[]
    for page in pages:
        embedding = create_embeddings(content=page[1])
        print(f"Created embeddings for page #{page[0]+1}")
        response = index_document_page(page_number=page[0], page_text=page[1], embedding=embedding)
        print(f"Indexed content for page #{page[0]+1}")
        responses.append(response)
    return responses

def create_embeddings(content, modelId="amazon.titan-embed-text-v1"):
    bedrock_client = boto3.client("bedrock-runtime", region_name=os.environ["BEDROCK_MODEL_REGION"])
    accept = "application/json"
    contentType = "application/json"
    body = json.dumps({"inputText": content})
    response = bedrock_client.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType
    )
    response_body = json.loads(response.get("body").read())
    embedding = response_body.get("embedding")
    return embedding

#function to remove a prefix of https:// from the given string if present
def removePrefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  

def get_aoss_client():
    host = os.environ['AOS_HOST']
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

def index_document_page(page_number, page_text, embedding):
    index = os.environ['AOSS_INDEX_NAME']
    aoss_client = get_aoss_client()
    aoss_client.index(
        index=index,
        body={"page_vector": embedding,"page_number":page_number, "page_text": page_text}
    )

def lambda_handler(event, context):
    bucket = event['detail']['bucket']['name']
    key = event['detail']['object']['key']
    print(f"Processing document key {key} from  Bucket {bucket}")
    local_file = copy_object_to_tmp(bucket, key)
    pages = extract_pages_from_pdf(local_file)
    responses = embed_and_store_pages(pages)

    #delete local_file
    os.remove(local_file)
    print(f"Finished Processing document. {len(responses)} document page(s) indexed")
    return {"statusCode": 200, "body": json.dumps(responses)}