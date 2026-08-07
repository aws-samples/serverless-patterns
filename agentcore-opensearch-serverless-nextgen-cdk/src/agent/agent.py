import os
import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from strands import Agent, tool

region = os.environ.get("AWS_REGION", "us-east-1")
collection_endpoint = os.environ["COLLECTION_ENDPOINT"]
host = collection_endpoint.replace("https://", "")

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(
    credentials.access_key,
    credentials.secret_key,
    region,
    "aoss",
    session_token=credentials.token,
)

client = OpenSearch(
    hosts=[{"host": host, "port": 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection,
)


@tool
def search_documents(query: str, index: str = "documents") -> str:
    """Search documents in the OpenSearch Serverless collection.

    Args:
        query: The search query string.
        index: The index to search in. Defaults to 'documents'.

    Returns:
        Search results as a formatted string.
    """
    body = {"query": {"multi_match": {"query": query, "fields": ["*"]}}, "size": 5}
    response = client.search(index=index, body=body)
    hits = response["hits"]["hits"]
    if not hits:
        return "No documents found."
    results = []
    for hit in hits:
        results.append(f"Score: {hit['_score']}, Source: {hit['_source']}")
    return "\n".join(results)


agent = Agent(
    model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    tools=[search_documents],
    system_prompt="You are a helpful search assistant. Use the search_documents tool to find information in the OpenSearch collection.",
)

if __name__ == "__main__":
    agent.serve()
