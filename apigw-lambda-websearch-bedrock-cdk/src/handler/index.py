"""
AWS Lambda function that grounds AI responses in live web data.
Orchestrates Amazon Bedrock AgentCore Web Search for facts, then
Amazon Bedrock for inference to produce cited, accurate answers.
"""

import json
import os
import urllib.request
import boto3


def search_web(gateway_url, region, query, max_results=5):
    """Search the web via Amazon Bedrock AgentCore Gateway MCP protocol."""
    try:
        import botocore.session
        from botocore.auth import SigV4Auth
        from botocore.awsrequest import AWSRequest

        session = botocore.session.get_session()
        credentials = session.get_credentials().get_frozen_credentials()

        mcp_request = {
            'jsonrpc': '2.0',
            'id': '1',
            'method': 'tools/call',
            'params': {
                'name': 'web-search___WebSearch',
                'arguments': {'query': query[:200], 'maxResults': max_results},
            },
        }

        payload = json.dumps(mcp_request).encode('utf-8')
        request = AWSRequest(
            method='POST', url=gateway_url, data=payload,
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
        )
        SigV4Auth(credentials, 'bedrock-agentcore', region).add_auth(request)

        req = urllib.request.Request(
            gateway_url, data=payload, headers=dict(request.headers), method='POST',
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        # Extract search results from MCP response
        content = result.get('result', {}).get('content', [])
        if content:
            return json.loads(content[0].get('text', '{}'))
        return {}
    except Exception as e:
        return {'error': str(e)}


def invoke_bedrock(model_id, region, question, search_results):
    """Invoke Amazon Bedrock to synthesize a grounded answer with citations."""
    try:
        client = boto3.client('bedrock-runtime', region_name=region)

        # Format search results as context
        sources = search_results.get('results', [])
        context_parts = []
        for i, s in enumerate(sources[:5], 1):
            context_parts.append(
                f"[{i}] {s.get('title', 'Untitled')} ({s.get('url', '')})\n{s.get('text', '')[:500]}"
            )
        context = '\n\n'.join(context_parts)

        prompt = f"""Answer the following question using ONLY the provided web search results. 
Include citation numbers [1], [2], etc. for each fact you reference.
If the search results don't contain enough information, say so.

Question: {question}

Web Search Results:
{context}

Answer (with citations):"""

        response = client.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                'anthropic_version': 'bedrock-2023-05-31',
                'max_tokens': 1024,
                'messages': [{'role': 'user', 'content': prompt}],
            }),
        )

        body = json.loads(response['body'].read())
        answer = body['content'][0]['text']

        return {
            'answer': answer,
            'sources': [{'title': s.get('title'), 'url': s.get('url')} for s in sources[:5]],
        }
    except Exception as e:
        return {'error': str(e)}


def handler(event, context):
    """Orchestrate web search + Bedrock inference for grounded AI answers."""
    try:
        # Parse input from Amazon API Gateway
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event
        question = body.get('question', '')

        if not question:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'question field is required'}),
            }

        gateway_url = os.environ['GATEWAY_URL']
        region = os.environ.get('AWS_REGION', 'us-east-1')
        model_id = os.environ.get('MODEL_ID', 'us.anthropic.claude-sonnet-4-20250514-v1:0')

        # Step 1: Search the web for relevant facts
        search_results = search_web(gateway_url, region, question)
        if 'error' in search_results:
            return {
                'statusCode': 502,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': f'Web search failed: {search_results["error"]}'}),
            }

        # Step 2: Feed results to Amazon Bedrock for grounded inference
        grounded_response = invoke_bedrock(model_id, region, question, search_results)

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps(grounded_response),
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)}),
        }
